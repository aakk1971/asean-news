"""Generate MP3 audio from TV presenter scripts using Azure Speech Service.

Usage:
  python generate-tts.py                         # process today's TV page
  python generate-tts.py ASEAN-TV-2026-11-06.html # process a specific file

Environment variables (set as GitHub secrets):
  AZURE_SPEECH_KEY    — subscription key from the Azure Speech resource
  AZURE_SPEECH_REGION — region, e.g. southeastasia

The script reads the TV HTML, extracts each article's English and Chinese
presenter scripts, and generates newscast-style MP3 files in the audio/ folder.
"""

import html as html_mod, json, os, pathlib, re, sys, time, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
AUDIO_DIR = ROOT / 'audio'

# Azure configuration
KEY = os.environ.get('AZURE_SPEECH_KEY', '')
REGION = os.environ.get('AZURE_SPEECH_REGION', 'southeastasia')
TTS_URL = f'https://{REGION}.tts.speech.microsoft.com/cognitiveservices/v1'

# Voice choices — newscast style for a professional TV sound
VOICES = {
    'en': 'en-US-GuyNeural',       # male anchor
    'en-f': 'en-US-JennyNeural',   # female analyst (for duo mode)
    'zh': 'zh-CN-YunxiNeural',     # male anchor
    'zh-f': 'zh-CN-XiaoxiaoNeural' # female analyst (for duo mode)
}

SSML_TEMPLATE = '''<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'
  xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='{lang}'>
  <voice name='{voice}'>
    <mstts:express-as style='newscast'>
      <prosody rate='-5%' pitch='+0Hz'>
        {text}
      </prosody>
    </mstts:express-as>
  </voice>
</speak>'''


def extract_scripts(html_path):
    """Parse the TV HTML and extract scripts per article."""
    text = html_path.read_text(encoding='utf-8')

    # Find all articles with their IDs
    articles = []
    # Split by <article id="...">
    parts = re.split(r'<article\s+id="([^"]+)"', text)
    # parts[0] is before first article, then alternating id, content
    for i in range(1, len(parts), 2):
        article_id = parts[i]
        content = parts[i + 1] if i + 1 < len(parts) else ''
        # Cut at next </article>
        content = content.split('</article>')[0]

        scripts = {'id': article_id, 'en': '', 'zh': ''}

        # Find English script section
        en_match = re.search(
            r'<h3>English presenter script</h3>(.*?)(?=</section>)',
            content, re.DOTALL
        )
        if en_match:
            paragraphs = re.findall(r'<p>(.*?)</p>', en_match.group(1), re.DOTALL)
            scripts['en'] = ' '.join(
                re.sub(r'<[^>]+>', '', html_mod.unescape(p)).strip()
                for p in paragraphs
            )

        # Find Chinese script section
        zh_match = re.search(
            r'<h3>中文主播稿</h3>(.*?)(?=</section>)',
            content, re.DOTALL
        )
        if zh_match:
            paragraphs = re.findall(r'<p>(.*?)</p>', zh_match.group(1), re.DOTALL)
            scripts['zh'] = ' '.join(
                re.sub(r'<[^>]+>', '', html_mod.unescape(p)).strip()
                for p in paragraphs
            )

        if scripts['en'] or scripts['zh']:
            articles.append(scripts)

    return articles


def synthesize(text, lang, voice_key):
    """Call Azure TTS REST API and return MP3 bytes."""
    voice = VOICES[voice_key]
    lang_tag = 'en-US' if lang == 'en' else 'zh-CN'

    # Escape XML special characters in the text
    safe_text = (text
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
        .replace("'", '&apos;'))

    ssml = SSML_TEMPLATE.format(lang=lang_tag, voice=voice, text=safe_text)

    req = urllib.request.Request(TTS_URL, data=ssml.encode('utf-8'), headers={
        'Ocp-Apim-Subscription-Key': KEY,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3',
        'User-Agent': 'ASEANBusinessBrief/1.0'
    })

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as e:
            if attempt < 2:
                print(f'  Retry {attempt + 1}: {e}')
                time.sleep(2 * (attempt + 1))
            else:
                raise


def find_tv_page():
    """Find today's TV HTML file."""
    # Check command line argument
    if len(sys.argv) > 1 and sys.argv[1] != '--self-test':
        p = ROOT / sys.argv[1]
        if p.exists():
            return p
        raise FileNotFoundError(f'TV page not found: {p}')

    # Find the most recent TV page
    candidates = sorted(ROOT.glob('ASEAN-TV-*.html'), reverse=True)
    if candidates:
        return candidates[0]

    raise FileNotFoundError('No ASEAN-TV-*.html file found')


def generate_manifest(results):
    """Write audio/manifest.json so the TV page knows which files exist."""
    manifest = {}
    for article_id, lang, filename, duration_hint in results:
        if article_id not in manifest:
            manifest[article_id] = {}
        manifest[article_id][lang] = {
            'file': filename,
            'voice': VOICES[lang] if lang in VOICES else VOICES.get(lang, '')
        }
    (AUDIO_DIR / 'manifest.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8'
    )
    print(f'Manifest written: {len(manifest)} articles')


def main():
    if not KEY:
        print('AZURE_SPEECH_KEY not set. Skipping TTS generation.')
        print('To set up: create an Azure Speech resource and add the key')
        print('as a GitHub repository secret named AZURE_SPEECH_KEY.')
        return

    tv_page = find_tv_page()
    print(f'Processing: {tv_page.name}')

    articles = extract_scripts(tv_page)
    print(f'Found {len(articles)} articles with scripts')

    AUDIO_DIR.mkdir(exist_ok=True)
    results = []

    for article in articles:
        for lang in ['en', 'zh']:
            text = article[lang]
            if not text:
                continue

            filename = f'{article["id"]}-{lang}.mp3'
            filepath = AUDIO_DIR / filename

            # Skip if file already exists and is non-empty
            if filepath.exists() and filepath.stat().st_size > 1000:
                print(f'  Skip (exists): {filename}')
                results.append((article['id'], lang, filename, None))
                continue

            print(f'  Generating: {filename} ({len(text)} chars)...')
            try:
                audio_data = synthesize(text, lang, lang)
                filepath.write_bytes(audio_data)
                size_kb = len(audio_data) / 1024
                print(f'  OK: {filename} ({size_kb:.0f} KB)')
                results.append((article['id'], lang, filename, None))
            except Exception as e:
                print(f'  FAILED: {filename} — {e}')

    generate_manifest(results)
    print(f'Done: {len(results)} audio files in audio/')


def self_test():
    """Verify script extraction works without Azure credentials."""
    test_html = '''<!doctype html><html><body>
    <article id="test1">
    <div class="scripts"><section>
    <h3>English presenter script</h3>
    <p>First paragraph of the English script.</p>
    <p>Second paragraph with analysis.</p>
    </section><section lang="zh-Hans">
    <h3>中文主播稿</h3>
    <p>中文稿件第一段。</p>
    <p>中文分析第二段。</p>
    </section></div>
    </article>
    <article id="test2">
    <div class="scripts"><section>
    <h3>English presenter script</h3>
    <p>Another story.</p>
    </section><section lang="zh-Hans">
    <h3>中文主播稿</h3>
    <p>另一条新闻。</p>
    </section></div>
    </article></body></html>'''

    tmp = ROOT / '_tts_test.html'
    tmp.write_text(test_html, encoding='utf-8')
    try:
        articles = extract_scripts(tmp)
        assert len(articles) == 2, f'Expected 2 articles, got {len(articles)}'
        assert articles[0]['id'] == 'test1'
        assert 'First paragraph' in articles[0]['en']
        assert '中文稿件' in articles[0]['zh']
        assert articles[1]['id'] == 'test2'
        print('TTS self-test passed')
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        self_test()
    else:
        main()
