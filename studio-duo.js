/* ASEAN Business Brief TV — illustrated two-person studio (Anchor + AI Analyst).
   Builds a dialogue from each report's script: the anchor reads the verified facts,
   the analyst gives the labelled analysis. Browser voices; simulated mouth movement. */
(function () {
  var reports = Array.prototype.slice.call(document.querySelectorAll('article[id]'))
    .filter(function (a) { return a.querySelector('.scripts section'); });
  if (!reports.length) return;

  var css = document.createElement('style');
  css.textContent = [
    '.duo{position:relative;max-width:900px;margin:8px 0 0;background:#0a1d28;border:1px solid #2c4b58;border-radius:6px;overflow:hidden}',
    '.duo svg{display:block;width:100%;height:auto}',
    '.duo .board{position:absolute;left:36.6%;top:12.4%;width:26.8%;height:27.5%;display:flex;flex-direction:column;justify-content:center;padding:0 1.4%;box-sizing:border-box;color:#fff;overflow:hidden;text-align:left}',
    '.duo .board small{font:700 clamp(6px,1.05vw,11px)/1.2 Arial,sans-serif;color:#dcb97f;letter-spacing:.6px;margin-bottom:4%}',
    '.duo .board strong{font:700 clamp(8px,1.55vw,17px)/1.18 Arial,sans-serif}',
    '.duo .board span{font:clamp(7px,1.15vw,12px)/1.3 Arial,"Microsoft YaHei",sans-serif;color:#cfe3e6;margin-top:4%}',
    '.duo .tag{position:absolute;top:2.2%;right:1.6%;background:#9b1c18;color:#fff;font:700 clamp(7px,1.15vw,12px)/1 Arial,sans-serif;padding:.7% 1.2%;border-radius:3px;letter-spacing:.6px;opacity:.35;transition:opacity .3s}',
    '.duo.on .tag{opacity:1}',
    '.duo .who{position:absolute;bottom:3.2%;padding:.6% 1.4%;font:700 clamp(7px,1.2vw,13px)/1.2 Arial,sans-serif;color:#fff;background:#123b4b;border-left:4px solid #c6a26a;transition:background .25s,transform .25s}',
    '.duo .who.anchor{left:3.5%}.duo .who.analyst{right:3.5%}',
    '.duo .who.speaking{background:#9b1c18;transform:translateY(-3px)}',
    '.duo-bar{max-width:900px;background:#102633;border:1px solid #2c4b58;border-top:0;padding:12px 14px;box-sizing:border-box}',
    '.duo-bar button{margin:3px 6px 3px 0;padding:9px 15px;cursor:pointer;background:#153a50;color:#fff;border:1px solid #8caaa9;border-radius:4px;font:inherit}',
    '.duo-bar button.stop{background:transparent}',
    '.duo-bar .cap{min-height:3.4em;margin:10px 0 4px;padding:10px 12px;background:#081822;border-left:3px solid #c6a26a;font-size:15px;line-height:1.55}',
    '.duo-bar .cap b{color:#dcb97f}',
    '.duo-bar .st{font-size:12px;color:#9fb6bd;margin:4px 0 0}',
    '.duo-bar .note{font-size:12px;color:#9fb6bd;margin:6px 0 0}',
    'article.has-duo .scripts .news-narration{display:none}'
  ].join('');
  document.head.append(css);

  /* ---------- drawing ---------- */
  function studioSVG(uid) {
    var bokeh = '';
    var spots = [[90,120,18],[170,210,10],[1440,140,16],[1510,250,9],[1350,90,8],[260,90,7],[1290,230,11],[60,300,8],[1550,330,12]];
    spots.forEach(function (b) { bokeh += '<circle cx="' + b[0] + '" cy="' + b[1] + '" r="' + b[2] + '" fill="#f2c27a" opacity=".22"/>'; });
    var win = '';
    for (var i = 0; i < 9; i++) {
      win += '<rect x="' + (40 + i * 175) + '" y="40" width="150" height="430" fill="url(#win' + uid + ')" opacity=".55"/>';
    }
    return '' +
'<svg viewBox="0 0 1600 900" role="img" aria-label="Illustrated TV studio: news anchor on the left and AI business analyst on the right at a news desk">' +
'<defs>' +
 '<linearGradient id="bg' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d2533"/><stop offset="1" stop-color="#16394a"/></linearGradient>' +
 '<linearGradient id="win' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f4c60"/><stop offset="1" stop-color="#0f2b38"/></linearGradient>' +
 '<linearGradient id="desk' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a6243"/><stop offset="1" stop-color="#5d3f2a"/></linearGradient>' +
 '<linearGradient id="front' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#123444"/><stop offset="1" stop-color="#0a1f2a"/></linearGradient>' +
 '<radialGradient id="spot' + uid + '" cx=".5" cy=".3" r=".6"><stop offset="0" stop-color="#ffffff" stop-opacity=".10"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>' +
'</defs>' +
'<rect width="1600" height="900" fill="url(#bg' + uid + ')"/>' + win +
'<g opacity=".5">' + bokeh + '</g>' +
'<rect x="0" y="470" width="1600" height="10" fill="#c6a26a" opacity=".35"/>' +
// back screen
'<rect x="572" y="96" width="456" height="268" rx="6" fill="#0f3442" stroke="#c6a26a" stroke-width="4"/>' +
'<rect x="572" y="96" width="456" height="268" rx="6" fill="url(#spot' + uid + ')"/>' +
'<rect x="790" y="364" width="20" height="60" fill="#0b2531"/>' +
'<ellipse cx="400" cy="430" rx="300" ry="260" fill="url(#spot' + uid + ')"/>' +
'<ellipse cx="1200" cy="430" rx="300" ry="260" fill="url(#spot' + uid + ')"/>' +
anchor() + analyst() +
// desk
'<path d="M90 650 L1510 650 L1560 700 L40 700 Z" fill="url(#desk' + uid + ')"/>' +
'<rect x="40" y="700" width="1520" height="200" fill="url(#front' + uid + ')"/>' +
'<rect x="40" y="700" width="1520" height="6" fill="#c6a26a"/>' +
'<rect x="300" y="664" width="190" height="22" rx="2" fill="#f4f1ea" transform="rotate(-3 395 675)"/>' +
'<rect x="1110" y="662" width="150" height="24" rx="3" fill="#20313a"/><rect x="1118" y="666" width="134" height="16" rx="2" fill="#3f7f86" opacity=".7"/>' +
hands() +
'<text x="800" y="790" text-anchor="middle" fill="#e9dcc6" font-family="Georgia,serif" font-size="46" font-weight="700" letter-spacing="2">ASEAN BUSINESS BRIEF</text>' +
'<text x="800" y="832" text-anchor="middle" fill="#c6a26a" font-family="Arial,sans-serif" font-size="22" letter-spacing="6">东盟商业简报 · TV</text>' +
'</svg>';
  }

  function face(o) {
    // o: cx, cy, rx, ry, skin, shade, lip, brow, cls
    var cx = o.cx, cy = o.cy;
    var ex = o.eyeGap, ey = cy - 12;
    return '' +
'<ellipse cx="' + (cx - o.rx + 4) + '" cy="' + (cy + 8) + '" rx="13" ry="21" fill="' + o.shade + '"/>' +
'<ellipse cx="' + (cx + o.rx - 4) + '" cy="' + (cy + 8) + '" rx="13" ry="21" fill="' + o.shade + '"/>' +
'<ellipse cx="' + cx + '" cy="' + cy + '" rx="' + o.rx + '" ry="' + o.ry + '" fill="' + o.skin + '"/>' +
'<path d="M' + (cx - o.rx + 10) + ' ' + (cy + 30) + ' Q' + cx + ' ' + (cy + o.ry + 14) + ' ' + (cx + o.rx - 10) + ' ' + (cy + 30) + ' Q' + cx + ' ' + (cy + o.ry - 4) + ' ' + (cx - o.rx + 10) + ' ' + (cy + 30) + 'Z" fill="' + o.shade + '" opacity=".35"/>' +
// brows
'<path class="brow" d="M' + (cx - ex - 17) + ' ' + (ey - 20) + ' Q' + (cx - ex) + ' ' + (ey - 29) + ' ' + (cx - ex + 16) + ' ' + (ey - 21) + '" stroke="' + o.brow + '" stroke-width="' + o.browW + '" fill="none" stroke-linecap="round"/>' +
'<path class="brow" d="M' + (cx + ex - 16) + ' ' + (ey - 21) + ' Q' + (cx + ex) + ' ' + (ey - 29) + ' ' + (cx + ex + 17) + ' ' + (ey - 20) + '" stroke="' + o.brow + '" stroke-width="' + o.browW + '" fill="none" stroke-linecap="round"/>' +
// eyes
'<g class="eyes">' +
 '<ellipse cx="' + (cx - ex) + '" cy="' + ey + '" rx="12" ry="8" fill="#fbf7f2"/>' +
 '<ellipse cx="' + (cx + ex) + '" cy="' + ey + '" rx="12" ry="8" fill="#fbf7f2"/>' +
 '<g class="pupils"><circle cx="' + (cx - ex) + '" cy="' + ey + '" r="6.2" fill="#2b1d16"/><circle cx="' + (cx + ex) + '" cy="' + ey + '" r="6.2" fill="#2b1d16"/>' +
 '<circle cx="' + (cx - ex + 2) + '" cy="' + (ey - 2) + '" r="1.8" fill="#fff"/><circle cx="' + (cx + ex + 2) + '" cy="' + (ey - 2) + '" r="1.8" fill="#fff"/></g>' +
 '<g class="lids" transform="scale(1 0)" style="transform-origin:' + cx + 'px ' + (ey - 9) + 'px">' +
  '<rect x="' + (cx - ex - 14) + '" y="' + (ey - 10) + '" width="28" height="20" rx="8" fill="' + o.skin + '"/>' +
  '<rect x="' + (cx + ex - 14) + '" y="' + (ey - 10) + '" width="28" height="20" rx="8" fill="' + o.skin + '"/></g>' +
 '<path d="M' + (cx - ex - 13) + ' ' + (ey - 4) + ' Q' + (cx - ex) + ' ' + (ey - 12) + ' ' + (cx - ex + 13) + ' ' + (ey - 4) + '" stroke="#3a2a22" stroke-width="2.5" fill="none"/>' +
 '<path d="M' + (cx + ex - 13) + ' ' + (ey - 4) + ' Q' + (cx + ex) + ' ' + (ey - 12) + ' ' + (cx + ex + 13) + ' ' + (ey - 4) + '" stroke="#3a2a22" stroke-width="2.5" fill="none"/>' +
'</g>' +
// nose
'<path d="M' + (cx - 2) + ' ' + (cy - 6) + ' Q' + (cx - 10) + ' ' + (cy + 22) + ' ' + (cx - 6) + ' ' + (cy + 27) + ' Q' + cx + ' ' + (cy + 31) + ' ' + (cx + 9) + ' ' + (cy + 26) + '" stroke="' + o.shade + '" stroke-width="3.5" fill="none" stroke-linecap="round"/>' +
// mouth
'<g class="mouth">' +
 '<ellipse class="mi" cx="' + cx + '" cy="' + (cy + 52) + '" rx="' + o.mw + '" ry="1.5" fill="#4a1714"/>' +
 '<rect class="teeth" x="' + (cx - o.mw + 6) + '" y="' + (cy + 49) + '" width="' + (o.mw * 2 - 12) + '" height="5" rx="2" fill="#f6f2ea" opacity="0"/>' +
 '<path d="M' + (cx - o.mw) + ' ' + (cy + 51) + ' Q' + (cx - o.mw / 2) + ' ' + (cy + 45) + ' ' + cx + ' ' + (cy + 48) + ' Q' + (cx + o.mw / 2) + ' ' + (cy + 45) + ' ' + (cx + o.mw) + ' ' + (cy + 51) + '" stroke="' + o.lip + '" stroke-width="' + o.lipW + '" fill="none" stroke-linecap="round"/>' +
 '<path class="ll" d="M' + (cx - o.mw + 3) + ' ' + (cy + 54) + ' Q' + cx + ' ' + (cy + 63) + ' ' + (cx + o.mw - 3) + ' ' + (cy + 54) + '" stroke="' + o.lip + '" stroke-width="' + (o.lipW + 1) + '" fill="none" stroke-linecap="round"/>' +
'</g>';
  }

  function anchor() {
    var cx = 400, cy = 330;
    return '<g class="p-anchor">' +
'<path d="M210 700 C210 560 260 488 352 470 L448 470 C540 488 590 560 590 700 Z" fill="#1c2b4b"/>' +
'<path d="M356 470 L400 572 L444 470 Z" fill="#f3f3f1"/>' +
'<path d="M390 486 L410 486 L417 506 L405 590 L395 590 L383 506 Z" fill="#8f1d2c"/>' +
'<path d="M389 474 L411 474 L409 490 L391 490 Z" fill="#7a1725"/>' +
'<path d="M352 470 L400 588 L366 528 L322 486 Z" fill="#15213b"/><path d="M448 470 L400 588 L434 528 L478 486 Z" fill="#15213b"/>' +
'<path d="M462 514 L494 514 L490 524 L466 524 Z" fill="#f3f3f1"/>' +
'<rect x="368" y="400" width="64" height="80" rx="14" fill="#b88763"/>' +
'<g class="head">' +
 face({ cx: cx, cy: cy, rx: 76, ry: 94, skin: '#c9976f', shade: '#a77753', lip: '#8a5442', lipW: 4, brow: '#1f1a18', browW: 6, eyeGap: 30, mw: 21 }) +
 '<path d="M322 302 C312 214 368 190 410 194 C462 197 492 230 480 304 C472 266 448 244 410 246 C366 248 342 262 322 302 Z" fill="#1e1a19"/>' +
'</g></g>';
  }

  function analyst() {
    var cx = 1200, cy = 336;
    return '<g class="p-analyst">' +
'<path d="M1108 300 C1090 400 1100 470 1086 520 L1314 520 C1300 470 1310 400 1292 300 Z" fill="#191312"/>' +
'<path d="M1020 700 C1020 570 1066 494 1150 478 L1250 478 C1334 494 1380 570 1380 700 Z" fill="#2c6c70"/>' +
'<path d="M1158 478 L1200 560 L1242 478 Z" fill="#f6efe7"/>' +
'<path d="M1150 478 L1200 600 L1168 540 L1124 494 Z" fill="#245b5f"/><path d="M1250 478 L1200 600 L1232 540 L1276 494 Z" fill="#245b5f"/>' +
'<path d="M1176 500 Q1200 528 1224 500" stroke="#d8b46a" stroke-width="3" fill="none"/><circle cx="1200" cy="522" r="5" fill="#d8b46a"/>' +
'<rect x="1172" y="406" width="56" height="80" rx="14" fill="#c8977a"/>' +
'<g class="head">' +
 face({ cx: cx, cy: cy, rx: 70, ry: 88, skin: '#dcae8f', shade: '#bf8d6f', lip: '#b04a52', lipW: 5, brow: '#2a1d18', browW: 4.5, eyeGap: 28, mw: 19 }) +
 '<g fill="none" stroke="#2a2a2e" stroke-width="3.5"><rect x="1153" y="308" width="38" height="28" rx="9"/><rect x="1209" y="308" width="38" height="28" rx="9"/><path d="M1191 320 L1209 320"/></g>' +
 '<path d="M1126 318 C1114 236 1160 200 1206 202 C1258 204 1288 240 1276 320 C1264 280 1244 258 1214 256 C1192 270 1160 286 1126 318 Z" fill="#1d1615"/>' +
 '<path d="M1126 318 C1118 360 1124 400 1132 420 C1112 400 1104 350 1112 300 Z" fill="#1d1615"/>' +
 '<path d="M1276 320 C1286 360 1280 400 1270 422 C1292 400 1298 350 1290 300 Z" fill="#1d1615"/>' +
'</g></g>';
  }

  function hands() {
    return '' +
'<path d="M300 700 Q300 660 340 652 L380 652 L380 700 Z" fill="#1c2b4b"/><ellipse cx="392" cy="664" rx="26" ry="15" fill="#c9976f"/>' +
'<path d="M500 700 Q500 660 460 652 L430 652 L430 700 Z" fill="#1c2b4b"/><ellipse cx="420" cy="666" rx="24" ry="14" fill="#c9976f"/>' +
'<path d="M1060 700 Q1060 662 1100 654 L1150 654 L1150 700 Z" fill="#2c6c70"/><ellipse cx="1160" cy="666" rx="23" ry="13" fill="#dcae8f"/>' +
'<path d="M1340 700 Q1340 662 1300 654 L1252 654 L1252 700 Z" fill="#2c6c70"/><ellipse cx="1244" cy="667" rx="22" ry="13" fill="#dcae8f"/>';
  }

  /* ---------- characters runtime ---------- */
  function rig(svg, sel, cx, pivotY, lookDir) {
    var g = svg.querySelector(sel);
    return {
      head: g.querySelector('.head'), pupils: g.querySelector('.pupils'), lids: g.querySelector('.lids'),
      mi: g.querySelector('.mi'), ll: g.querySelector('.ll'), teeth: g.querySelector('.teeth'),
      cx: cx, pivotY: pivotY, lookDir: lookDir, open: 0, target: 0, next: 0,
      tilt: 0, tiltGoal: 0, nod: 0, nodGoal: 0, blinkAt: performance.now() + 1000 + Math.random() * 3000, blink: 0, look: 0
    };
  }

  function pickVoices(lang) {
    var all = speechSynthesis.getVoices().filter(function (v) { return v.lang.toLowerCase().indexOf(lang) === 0; });
    var male = /guy|ryan|andrew|david|mark|george|daniel|james|thomas|brian|christopher|eric|roger|william|liam|yunxi|yunyang|yunjian|kangkang|male/i;
    var female = /jenny|aria|zira|sonia|libby|hazel|susan|samantha|karen|moira|tessa|victoria|emma|ava|michelle|natasha|clara|xiaoxiao|xiaoyi|huihui|yaoyao|tingting|ting-ting|meijia|female/i;
    function score(v, re) { return (re.test(v.name) ? 50 : 0) + (/natural|neural|online/i.test(v.name) ? 20 : 0) + (v.localService ? 0 : 1); }
    var a = all.slice().sort(function (x, y) { return score(y, male) - score(x, male); })[0];
    var b = all.slice().sort(function (x, y) { return score(y, female) - score(x, female); })[0];
    if (b && a && b.voiceURI === a.voiceURI) {
      var other = all.filter(function (v) { return v.voiceURI !== a.voiceURI; });
      if (other.length) b = other.sort(function (x, y) { return score(y, female) - score(x, female); })[0];
    }
    return { anchor: a, analyst: b, same: !a || !b || a.voiceURI === b.voiceURI };
  }

  var QUESTIONS_EN = ['What should businesses take from this?', 'How should we read this?', 'What does this mean for companies in the region?'];
  var NEXT_EN = 'And what should we watch next?';

  function buildDialogue(article, i) {
    var sec = article.querySelectorAll('.scripts section');
    var en = Array.prototype.map.call(sec[0].querySelectorAll('p'), function (p) { return p.textContent.trim(); });
    var zh = Array.prototype.map.call(sec[1].querySelectorAll('p'), function (p) { return p.textContent.trim(); });
    var strip = function (t) { return t.replace(/^(Our analysis|What comes next)\s*:\s*/i, '').replace(/^原创分析[：:]\s*/, ''); };
    var d = { en: [], zh: [] };
    if (en[0]) d.en.push(['anchor', en[0]]);
    if (en[1]) { d.en.push(['anchor', QUESTIONS_EN[i % QUESTIONS_EN.length]]); d.en.push(['analyst', strip(en[1])]); }
    if (en[2]) { d.en.push(['anchor', NEXT_EN]); d.en.push(['analyst', strip(en[2])]); }
    d.en.push(['anchor', 'Thank you.']);
    if (zh[0]) d.zh.push(['anchor', zh[0]]);
    if (zh[1]) { d.zh.push(['anchor', '这对企业意味着什么？']); d.zh.push(['analyst', strip(zh[1])]); }
    d.zh.push(['anchor', '谢谢。']);
    return d;
  }

  var stages = [];
  var activeStage = null, serial = 0;

  reports.forEach(function (article, i) {
    var old = article.querySelector('.screen');
    var title = (article.querySelector('h2') || {}).textContent || 'ASEAN Business Brief';
    var zhTitle = (article.querySelector('h3[lang]') || {}).textContent || '';
    var place = ((article.querySelector('.tag') || {}).textContent || '').trim();

    var stage = document.createElement('div');
    stage.className = 'duo';
    stage.innerHTML = studioSVG(article.id) +
      '<div class="board"><small>ASEAN NEWS · 6 NOV 2026' + (place ? ' · ' + place.toUpperCase() : '') + '</small><strong></strong><span></span></div>' +
      '<div class="tag">● ON AIR / 播报中</div>' +
      '<div class="who anchor">ANCHOR / 主播</div><div class="who analyst">AI ANALYST / AI分析员</div>';
    stage.querySelector('.board strong').textContent = title;
    stage.querySelector('.board span').textContent = zhTitle;

    var bar = document.createElement('div');
    bar.className = 'duo-bar';
    bar.innerHTML = '<button type="button" data-l="en">▶ Watch in English</button><button type="button" data-l="zh">▶ 中文播报</button><button type="button" class="stop">■ Stop / 停止</button>' +
      '<div class="cap" aria-live="polite">Press ▶ to hear the anchor and the AI analyst discuss this report. / 按 ▶ 收听主播与AI分析员讨论本则新闻。</div>' +
      '<p class="st"></p><p class="note">Illustrated studio. Voices are your browser\'s text-to-speech; mouth movement is simulated, not exact lip sync. The analyst is an AI character presenting our labelled analysis. / 插画演播室；浏览器语音，口型为模拟。分析员为AI角色，讲述本报标注的分析内容。</p>';

    if (old) { old.before(stage); old.remove(); } else { article.querySelector('h3[lang]') ? article.querySelector('h3[lang]').after(stage) : article.prepend(stage); }
    stage.after(bar);
    article.classList.add('has-duo');

    var svg = stage.querySelector('svg');
    var st = {
      el: stage, bar: bar, cap: bar.querySelector('.cap'), status: bar.querySelector('.st'),
      dialogue: buildDialogue(article, i), speaker: null,
      who: { anchor: stage.querySelector('.who.anchor'), analyst: stage.querySelector('.who.analyst') },
      p: { anchor: rig(svg, '.p-anchor', 400, 440, 1), analyst: rig(svg, '.p-analyst', 1200, 446, -1) }
    };
    stages.push(st);

    bar.querySelectorAll('button[data-l]').forEach(function (b) {
      b.addEventListener('click', function () { play(st, b.getAttribute('data-l')); });
    });
    bar.querySelector('.stop').addEventListener('click', function () { stopAll('Stopped / 已停止'); });
  });

  function stopAll(msg) {
    serial++;
    if ('speechSynthesis' in window) speechSynthesis.cancel();
    stages.forEach(function (s) { s.speaker = null; s.el.classList.remove('on'); s.who.anchor.classList.remove('speaking'); s.who.analyst.classList.remove('speaking'); });
    if (activeStage && msg) activeStage.status.textContent = msg;
    activeStage = null;
  }

  function play(st, lang) {
    if (!('speechSynthesis' in window)) { st.status.textContent = 'Voice is not available in this browser. Please read the scripts below. / 此浏览器不支持语音。'; return; }
    stopAll();
    var v = pickVoices(lang);
    if (!v.anchor) {
      st.status.textContent = lang === 'zh' ? '未找到中文语音，请在设备中安装中文语音后重试。' : 'No English voice is available on this device.';
      return;
    }
    var lines = st.dialogue[lang];
    var token = serial, n = 0;
    activeStage = st;
    st.el.classList.add('on');
    st.status.textContent = v.same ? 'Only one voice is installed on this device; the analyst uses a higher pitch. / 本设备仅一种语音。' : '';
    function next() {
      if (token !== serial) return;
      if (n >= lines.length) {
        st.speaker = null; st.el.classList.remove('on');
        st.who.anchor.classList.remove('speaking'); st.who.analyst.classList.remove('speaking');
        st.cap.innerHTML = '<b>Finished / 播报完毕</b>';
        activeStage = null; return;
      }
      var who = lines[n][0], text = lines[n][1]; n++;
      var u = new SpeechSynthesisUtterance(text);
      var voice = who === 'anchor' ? v.anchor : (v.analyst || v.anchor);
      u.voice = voice; u.lang = voice.lang;
      u.rate = lang === 'zh' ? 1 : 0.98;
      u.pitch = v.same ? (who === 'anchor' ? 0.85 : 1.25) : 1;
      u.onstart = function () {
        if (token !== serial) return;
        st.speaker = who;
        st.who.anchor.classList.toggle('speaking', who === 'anchor');
        st.who.analyst.classList.toggle('speaking', who === 'analyst');
        var label = who === 'anchor' ? (lang === 'zh' ? '主播' : 'Anchor') : (lang === 'zh' ? 'AI分析员' : 'AI Analyst');
        st.cap.innerHTML = '<b></b> ';
        st.cap.firstChild.textContent = label + ':';
        st.cap.append(text);
      };
      u.onboundary = function () { if (st.speaker) st.p[st.speaker].kick = 1; };
      u.onend = function () { if (token === serial) { st.speaker = null; setTimeout(next, 260); } };
      u.onerror = function (e) { if (token === serial && e.error !== 'interrupted' && e.error !== 'canceled') { st.status.textContent = 'Playback failed (' + e.error + '). Try again. / 播放失败，请重试。'; stopAll(); } };
      speechSynthesis.speak(u);
    }
    next();
  }

  /* ---------- animation loop ---------- */
  function animate(t) {
    stages.forEach(function (st) {
      var vis = st.el.getBoundingClientRect();
      if (vis.bottom < -50 || vis.top > innerHeight + 50) return;
      ['anchor', 'analyst'].forEach(function (k) {
        var r = st.p[k], talking = st.speaker === k && speechSynthesis.speaking;
        // mouth
        if (talking && (t > r.next || r.kick)) {
          var roll = Math.random();
          r.target = roll < 0.16 ? 0.05 : roll < 0.55 ? 0.4 + Math.random() * 0.3 : 0.75 + Math.random() * 0.25;
          if (r.kick) r.target = Math.max(r.target, 0.65);
          r.kick = 0;
          r.next = t + 80 + Math.random() * 95;
        }
        var goal = talking ? r.target : 0;
        r.open += (goal - r.open) * (goal > r.open ? 0.5 : 0.32);
        if (r.open < 0.01) r.open = 0;
        r.mi.setAttribute('ry', (1.5 + r.open * 11).toFixed(2));
        r.mi.setAttribute('transform', 'translate(0 ' + (r.open * 4).toFixed(2) + ')');
        r.ll.setAttribute('transform', 'translate(0 ' + (r.open * 9).toFixed(2) + ')');
        r.teeth.setAttribute('opacity', r.open > 0.3 ? '0.9' : '0');
        // head: speaker faces camera with small gestures; listener turns slightly toward speaker
        var someoneTalking = !!st.speaker;
        if (t > (r.headNext || 0)) {
          r.tiltGoal = talking ? (Math.random() * 5 - 2.5) : (someoneTalking ? r.lookDir * 3 : Math.random() * 2 - 1);
          r.nodGoal = talking ? Math.random() * 4 : (someoneTalking && Math.random() < 0.3 ? 4 : 0);
          r.headNext = t + (talking ? 500 + Math.random() * 700 : 1200 + Math.random() * 1500);
        }
        r.tilt += (r.tiltGoal - r.tilt) * 0.06;
        r.nod += (r.nodGoal - r.nod) * 0.08;
        r.head.setAttribute('transform', 'rotate(' + r.tilt.toFixed(2) + ' ' + r.cx + ' ' + r.pivotY + ') translate(0 ' + r.nod.toFixed(2) + ')');
        // eyes look at the other person while listening
        var lookGoal = (!talking && someoneTalking) ? r.lookDir * 4 : 0;
        r.look += (lookGoal - r.look) * 0.1;
        r.pupils.setAttribute('transform', 'translate(' + r.look.toFixed(2) + ' 0)');
        // blinking
        if (t > r.blinkAt) { r.blink = 1; r.blinkAt = t + 2200 + Math.random() * 3800; }
        if (r.blink > 0) { r.blink -= 0.12; }
        var lid = r.blink > 0 ? Math.sin(Math.min(1, r.blink) * Math.PI) : 0;
        r.lids.setAttribute('transform', 'scale(1 ' + lid.toFixed(2) + ')');
      });
    });
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
  window.ABDuo = { stages: stages, play: play, stop: stopAll };
  window.addEventListener('pagehide', function () { stopAll(); });
  if ('speechSynthesis' in window) speechSynthesis.getVoices();
})();
