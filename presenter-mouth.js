/* Animated presenter mouth: moves the presenter's jaw while the browser voice is speaking.
   Simulated movement on a still photo, not true lip sync. */
(function () {
  var IMG = 'asean-tv-studio.png', W = 1672, H = 941;
  // Regions in original image pixels
  var JAW = { x: 1222, y: 323, w: 128, h: 52 };   // lower lip + chin, moves down
  var GAP = { x: 1258, y: 320, w: 58, h: 16 };    // dark mouth opening behind the jaw
  var MAX_DROP = 6;                                // jaw drop in image pixels at full open

  var css = document.createElement('style');
  css.textContent =
    '.pm-gap,.pm-jaw{position:absolute;pointer-events:none;z-index:1}' +
    '.pm-gap{background:radial-gradient(ellipse at 50% 45%,#3a1714 0%,#55251f 40%,rgba(85,37,31,0) 70%);opacity:0;border-radius:50%}' +
    '.pm-jaw{background-repeat:no-repeat;will-change:transform;' +
    '-webkit-mask-image:radial-gradient(ellipse 50% 60% at 50% 42%,#000 62%,transparent 100%);' +
    'mask-image:radial-gradient(ellipse 50% 60% at 50% 42%,#000 62%,transparent 100%)}' +
    '.pm-live{position:absolute;left:82.3%;top:1.1%;width:16.7%;height:10%;z-index:3;background:#9b1c18;color:#fff;border:1px solid #e3b98a;border-radius:4px;font:700 clamp(7px,1.25vw,13px)/1.25 Arial,sans-serif;letter-spacing:.5px;display:none;align-items:center;justify-content:center;text-align:center}' +
    '.screen.pm-talking .pm-live{display:flex}.screen.pm-talking .status{visibility:hidden}';
  document.head.append(css);

  function pct(r) {
    return {
      left: r.x / W * 100 + '%', top: r.y / H * 100 + '%',
      width: r.w / W * 100 + '%', height: r.h / H * 100 + '%'
    };
  }
  function place(el, r) { var p = pct(r); for (var k in p) el.style[k] = p[k]; }

  var rigs = [];
  document.querySelectorAll('.screen').forEach(function (screen) {
    var img = screen.querySelector('img[src="' + IMG + '"]');
    if (!img) return;
    var gap = document.createElement('div'); gap.className = 'pm-gap'; place(gap, GAP);
    var jaw = document.createElement('div'); jaw.className = 'pm-jaw'; place(jaw, JAW);
    jaw.style.backgroundImage = 'url(' + IMG + ')';
    jaw.style.backgroundSize = (W / JAW.w * 100) + '% ' + (H / JAW.h * 100) + '%';
    jaw.style.backgroundPosition = (JAW.x / (W - JAW.w) * 100) + '% ' + (JAW.y / (H - JAW.h) * 100) + '%';
    var live = document.createElement('span'); live.className = 'pm-live'; live.innerHTML = '● ON AIR / 播报中<br>AI PRESENTER';
    img.after(gap, jaw);
    screen.append(live);
    rigs.push({ screen: screen, img: img, gap: gap, jaw: jaw, open: 0 });
  });
  if (!rigs.length || !('speechSynthesis' in window)) return;

  // Remember which report's controls were pressed last, so that report's presenter talks.
  var current = null;
  document.addEventListener('click', function (e) {
    var box = e.target.closest && e.target.closest('.news-narration');
    if (!box) return;
    var holder = box.closest('article, section, #tv');
    var rig = null;
    if (holder) rig = rigs.find(function (r) { return holder.contains(r.screen); });
    current = rig || rigs.find(function (r) { var b = r.screen.getBoundingClientRect(); return b.bottom > 0 && b.top < innerHeight; }) || rigs[0];
  }, true);

  // Word boundaries (when the voice supports them) give an extra "syllable" kick.
  var kick = 0;
  var origSpeak = speechSynthesis.speak.bind(speechSynthesis);
  speechSynthesis.speak = function (u) {
    try { u.addEventListener('boundary', function () { kick = 1; }); } catch (e) {}
    return origSpeak(u);
  };

  var target = 0, nextChange = 0;
  function frame(t) {
    var speaking = speechSynthesis.speaking && !speechSynthesis.paused;
    rigs.forEach(function (r) {
      var on = speaking && r === current;
      r.screen.classList.toggle('pm-talking', on);
      if (on) {
        if (t > nextChange || kick) {
          // syllable rhythm: mostly open/half-open, with brief closures
          var roll = Math.random();
          target = roll < 0.18 ? 0.05 : roll < 0.55 ? 0.45 + Math.random() * 0.25 : 0.75 + Math.random() * 0.25;
          if (kick) target = Math.max(target, 0.7);
          kick = 0;
          nextChange = t + 85 + Math.random() * 90;
        }
      }
      var goal = on ? target : 0;
      r.open += (goal - r.open) * (goal > r.open ? 0.45 : 0.3);
      if (r.open < 0.01) r.open = 0;
      var h = r.img.clientHeight || 1;
      var drop = r.open * MAX_DROP * (h / H);
      r.jaw.style.transform = 'translateY(' + drop.toFixed(2) + 'px)';
      r.gap.style.opacity = Math.min(0.9, r.open * 1.2).toFixed(2);
      r.gap.style.transform = 'scaleY(' + (0.5 + r.open * 0.6).toFixed(2) + ')';
    });
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  // Update the honest labels: the presenter is now animated, but not true lip sync.
  document.querySelectorAll('.news-narration p').forEach(function (p) {
    if (/no lip sync/.test(p.textContent)) {
      p.textContent = p.textContent
        .replace('Browser voice with a still image; no lip sync.', 'Browser voice with an animated presenter (simulated mouth movement, not exact lip sync).')
        .replace('浏览器语音配静态图，无口型同步。', '浏览器语音配动画主播（模拟口型，非精确同步）。');
    }
  });
  document.querySelectorAll('.screen .status').forEach(function (s) {
    s.innerHTML = 'PRESS ▶ TO HEAR THE REPORT<br>按 ▶ 收听播报';
  });
})();
