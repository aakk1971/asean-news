/* Audio player: plays Azure TTS MP3 files instead of the browser's robotic voice.
   Falls back to speechSynthesis if no audio files are available.

   Loads audio/manifest.json to find which articles have MP3 files.
   Drives the mouth animation from the real audio amplitude using
   the Web Audio API AnalyserNode. */

(function () {
  'use strict';

  var manifest = null;
  var audioCtx = null;
  var currentAudio = null;
  var currentAnalyser = null;
  var currentArticleId = null;
  var playing = false;

  // Load the manifest to see which audio files exist
  fetch('audio/manifest.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) {
      if (data) {
        manifest = data;
        upgradeControls();
      }
    })
    .catch(function () { /* no manifest = use speechSynthesis fallback */ });

  function getAudioContext() {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    return audioCtx;
  }

  function stop() {
    playing = false;
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
      currentAudio = null;
    }
    currentAnalyser = null;
    currentArticleId = null;
    // Dispatch a custom event so presenter-mouth.js knows to close the mouth
    window.dispatchEvent(new CustomEvent('tts-stop'));
  }

  function playAudio(articleId, lang, statusEl) {
    if (!manifest || !manifest[articleId] || !manifest[articleId][lang]) {
      return false; // no audio file, fall back to speechSynthesis
    }

    stop();

    var info = manifest[articleId][lang];
    var audio = new Audio('audio/' + info.file);
    currentAudio = audio;
    currentArticleId = articleId;
    playing = true;

    // Set up Web Audio analyser for mouth movement
    var ctx = getAudioContext();
    var source = ctx.createMediaElementSource(audio);
    var analyser = ctx.createAnalyser();
    analyser.fftSize = 256;
    analyser.smoothingTimeConstant = 0.3;
    source.connect(analyser);
    analyser.connect(ctx.destination);
    currentAnalyser = analyser;

    // Dispatch event so presenter-mouth.js can use the analyser
    window.dispatchEvent(new CustomEvent('tts-play', {
      detail: { articleId: articleId, analyser: analyser, audio: audio }
    }));

    var total = 0;
    audio.addEventListener('loadedmetadata', function () {
      total = Math.round(audio.duration);
    });

    audio.addEventListener('timeupdate', function () {
      if (!playing) return;
      var elapsed = Math.round(audio.currentTime);
      var langLabel = lang === 'zh' ? '中文' : 'English';
      if (total > 0) {
        var pct = Math.round(audio.currentTime / audio.duration * 100);
        statusEl.textContent = 'Playing ' + langLabel + ' · ' + elapsed + 's / ' + total + 's (' + pct + '%)';
      } else {
        statusEl.textContent = 'Playing ' + langLabel + ' · ' + elapsed + 's';
      }
    });

    audio.addEventListener('ended', function () {
      playing = false;
      currentAudio = null;
      currentAnalyser = null;
      statusEl.textContent = 'Finished / 播报完毕';
      window.dispatchEvent(new CustomEvent('tts-stop'));
    });

    audio.addEventListener('error', function () {
      playing = false;
      statusEl.textContent = 'Audio failed to load / 音频加载失败';
      window.dispatchEvent(new CustomEvent('tts-stop'));
    });

    if (ctx.state === 'suspended') ctx.resume();
    audio.play().catch(function (e) {
      statusEl.textContent = 'Playback blocked: tap to enable audio / 请点击以启用音频';
    });

    return true;
  }

  function upgradeControls() {
    // Find all news-narration control boxes and upgrade their play buttons
    document.querySelectorAll('.news-narration').forEach(function (box) {
      var article = box.closest('article[id]');
      if (!article) return;
      var articleId = article.id;
      if (!manifest[articleId]) return; // no audio for this article

      // Find the status element
      var status = box.querySelector('[role="status"]');
      if (!status) return;

      // Find the play buttons and upgrade them
      var buttons = box.querySelectorAll('button');
      buttons.forEach(function (btn) {
        if (btn.textContent.indexOf('English') >= 0) {
          // Clone and replace to remove old listeners
          var newBtn = btn.cloneNode(true);
          newBtn.textContent = '▶ English (AI Voice)';
          newBtn.onclick = function () {
            speechSynthesis.cancel(); // stop any browser voice
            if (!playAudio(articleId, 'en', status)) {
              // Fall back: re-attach old click behavior via the original
              btn.click();
            }
          };
          btn.replaceWith(newBtn);
        } else if (btn.textContent.indexOf('中文') >= 0) {
          var newBtn = btn.cloneNode(true);
          newBtn.textContent = '▶ 中文 (AI Voice)';
          newBtn.onclick = function () {
            speechSynthesis.cancel();
            if (!playAudio(articleId, 'zh', status)) {
              btn.click();
            }
          };
          btn.replaceWith(newBtn);
        } else if (btn.textContent.indexOf('Stop') >= 0) {
          var newBtn = btn.cloneNode(true);
          newBtn.onclick = function () {
            stop();
            speechSynthesis.cancel();
            status.textContent = 'Stopped / 已停止';
          };
          btn.replaceWith(newBtn);
        }
      });

      // Update the note text
      var notes = box.querySelectorAll('p');
      notes.forEach(function (p) {
        if (p.textContent.indexOf('Browser voice') >= 0 ||
            p.textContent.indexOf('浏览器语音') >= 0) {
          p.textContent = 'Listen to this edition · 收听本期新闻 (6 Nov 2026). ' +
            'AI newscast voice by Azure Speech Service. / AI新闻播报语音（Azure语音服务）。';
        }
      });

      // Hide voice-choice selects (not needed with pre-generated audio)
      box.querySelectorAll('.voice-choice').forEach(function (sel) {
        sel.closest('label').style.display = 'none';
      });
    });

    // Update honest labels
    document.querySelectorAll('.news-narration p').forEach(function (p) {
      if (/simulated mouth movement/.test(p.textContent)) {
        p.textContent = p.textContent
          .replace(
            'Browser voice with an animated presenter (simulated mouth movement, not exact lip sync).',
            'AI newscast voice with animated presenter (mouth moves with audio amplitude).'
          )
          .replace(
            '浏览器语音配动画主播（模拟口型，非精确同步）。',
            'AI新闻播报语音配动画主播（口型随音频幅度变化）。'
          );
      }
    });
  }

  // Expose the analyser and playing state for presenter-mouth.js
  window.ABTTSPlayer = {
    getAnalyser: function () { return currentAnalyser; },
    isPlaying: function () { return playing; },
    getArticleId: function () { return currentArticleId; },
    stop: stop
  };

  // Clean up on page unload
  window.addEventListener('pagehide', stop);
})();
