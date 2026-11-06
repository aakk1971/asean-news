"""Fetch allowlisted RSS/Atom headlines. No article bodies, images, or inferred figures."""
import concurrent.futures, datetime as dt, email.utils, hashlib, html, json, pathlib, re, sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT = pathlib.Path(__file__).resolve().parent
UTC = dt.timezone.utc

def text(value):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]*>', ' ', html.unescape(value or ''))).strip()

def date(value):
    if not value: return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
    except (ValueError, TypeError):
        try: parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError: return None
    if parsed.tzinfo is None: return None
    return parsed.astimezone(UTC)

def child(node, name):
    for el in node:
        if el.tag.split('}')[-1] == name: return ''.join(el.itertext())
    return ''

def parse(payload, source, now):
    if b'<!DOCTYPE' in payload.upper() or b'<!ENTITY' in payload.upper(): raise ValueError('XML entities not allowed')
    doc = ET.fromstring(payload)
    if doc.tag.split('}')[-1] not in ('rss', 'feed', 'RDF'): raise ValueError('Not an RSS/Atom feed')
    items = []
    for node in doc.iter():
        if node.tag.split('}')[-1] not in ('item', 'entry'): continue
        title = text(child(node, 'title'))[:300]
        link = child(node, 'link').strip()
        if not link:
            link = next((el.get('href','') for el in node if el.tag.split('}')[-1] == 'link' and el.get('rel','alternate') == 'alternate'), '')
        url = urllib.parse.urlsplit(link)
        if not title or url.scheme != 'https' or url.hostname not in source['allowedHosts']: continue
        link = urllib.parse.urlunsplit((url.scheme,url.netloc,url.path,url.query,''))
        published = date(child(node,'pubDate') or child(node,'published') or child(node,'date') or child(node,'updated'))
        if published is None or published > now + dt.timedelta(minutes=10) or published < now - dt.timedelta(days=7): continue
        items.append({'id':hashlib.sha256(link.encode()).hexdigest()[:16], 'title':title, 'url':link, 'publishedAt':published.isoformat(), 'sourceId':source['id'], 'sourceName':source['name'], 'country':source['country'], 'language':'en', 'status':'source-headline', 'firstSeenAt':now.isoformat()})
    unique = {item['url']:item for item in items}
    return sorted(unique.values(), key=lambda x:x['publishedAt'], reverse=True)[:30]

def fetch_source(source, now):
    errors=[]
    for url in [source['url']] + source.get('fallbackUrls',[]):
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'ASEANBusinessBrief/1.0 (+https://asean-news.vercel.app/)', 'Accept':'application/rss+xml, application/atom+xml, text/xml, application/xml'})
            with urllib.request.urlopen(request,timeout=20) as response:
                if urllib.parse.urlsplit(response.geturl()).hostname not in source['allowedHosts']: raise ValueError('Unexpected redirect host')
                body=response.read(2_000_001)
            if len(body)>2_000_000: raise ValueError('Feed exceeds size limit')
            items=parse(body,source,now)
            return items, {'id':source['id'],'name':source['name'],'country':source['country'],'url':url,'checkedAt':now.isoformat(),'ok':True,'itemsFound':len(items)}
        except Exception as exc: errors.append(type(exc).__name__ + ': ' + str(exc)[:120])
    return [], {'id':source['id'],'name':source['name'],'country':source['country'],'url':source['url'],'checkedAt':now.isoformat(),'ok':False,'error':'; '.join(errors)}

def refresh():
    now=dt.datetime.now(UTC)
    config=json.loads((ROOT/'news-sources.json').read_text(encoding='utf-8'))
    path=ROOT/'news-feed.json'
    previous=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'items':[]}
    old={item['url']:item for item in previous.get('items',[])}
    result=[]; statuses=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(lambda s:fetch_source(s,now),config['feeds']))
    for source,(items,status) in zip(config['feeds'],results):
        statuses.append(status)
        if not status['ok']:
            items=[i for i in previous.get('items',[]) if i['sourceId']==source['id'] and date(i.get('publishedAt')) and date(i['publishedAt'])>=now-dt.timedelta(days=7)]
        for item in items:
            if item['url'] in old: item['firstSeenAt']=old[item['url']].get('firstSeenAt',item['firstSeenAt'])
        result.extend(items)
    result=list({item['url']:item for item in result}.values())
    result.sort(key=lambda i:i['publishedAt'],reverse=True)
    success=any(s['ok'] for s in statuses)
    payload={'schemaVersion':1,'checkedAt':now.isoformat(),'lastSuccessfulAt':now.isoformat() if success else previous.get('lastSuccessfulAt'),'status':'ok' if all(s['ok'] for s in statuses) else 'partial' if success else 'failed','items':result[:60],'sources':statuses,'coverageNote':config['coverageNote']}
    temporary=path.with_suffix('.json.tmp');temporary.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');temporary.replace(path)
    print(json.dumps({'status':payload['status'],'items':len(result),'sources':statuses}))
    if not success: raise SystemExit('All feeds failed; retained previous data with failure status')

if __name__=='__main__':
    if '--self-test' in sys.argv:
        source={'id':'fixture','name':'Fixture','country':'Test','allowedHosts':['example.com']}
        now=dt.datetime(2026,11,6,tzinfo=UTC)
        fixture=b'<rss><channel><item><title>A &amp; B</title><link>https://example.com/a</link><pubDate>Thu, 05 Nov 2026 12:00:00 GMT</pubDate></item><item><title>Unsafe</title><link>javascript:alert(1)</link><pubDate>Thu, 05 Nov 2026 12:00:00 GMT</pubDate></item><item><title>Undated</title><link>https://example.com/b</link></item></channel></rss>'
        rows=parse(fixture,source,now); assert len(rows)==1 and rows[0]['title']=='A & B'
        assert parse(fixture,source,now+dt.timedelta(days=10))==[]
        try: parse(b'<!DOCTYPE x><rss/>',source,now); raise AssertionError('Entity guard missing')
        except ValueError: pass
        print('Parser self-tests passed')
    else: refresh()
