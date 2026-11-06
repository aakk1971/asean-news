/* Expert panel: adds a female analyst beside the male anchor in each article.
   Creates a side-by-side TV discussion layout.
   Requires expert-analyst.png in the same directory.
   If the image is not found, shows a placeholder. */
(function () {
  'use strict';

  var EXPERT_IMG = 'expert-analyst.png';

  // Check if the expert image exists before building the layout
  var img = new Image();
  img.onload = function () { buildPanels(true); };
  img.onerror = function () { buildPanels(false); };
  img.src = EXPERT_IMG;

  function buildPanels(imageExists) {
    var css = document.createElement('style');
    css.textContent =
      '.duo-panel{display:grid;grid-template-columns:1fr 1fr;gap:0;max-width:850px;background:#000}' +
      '.duo-panel .screen{max-width:100%}' +
      '.duo-panel .expert-screen{position:relative;background:#0a1e2a;overflow:hidden;display:flex;flex-direction:column}' +
      '.duo-panel .expert-screen img{width:100%;height:100%;object-fit:cover;display:block}' +
      '.duo-panel .expert-screen .expert-label{position:absolute;bottom:0;left:0;right:0;background:#123b4be8;padding:8px 14px;font:bold clamp(10px,1.5vw,16px)/1.3 Arial,sans-serif;color:white}' +
      '.duo-panel .expert-screen .expert-badge{position:absolute;top:8px;left:8px;background:#1a6b4a;color:#fff;padding:4px 10px;border-radius:3px;font:700 clamp(8px,1.1vw,12px)/1.2 Arial,sans-serif;letter-spacing:.5px;z-index:2}' +
      '.duo-panel .screen .anchor-badge{position:absolute;top:8px;left:8px;background:#9b1c18;color:#fff;padding:4px 10px;border-radius:3px;font:700 clamp(8px,1.1vw,12px)/1.2 Arial,sans-serif;letter-spacing:.5px;z-index:2}' +
      '.expert-placeholder{display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;color:#7aa;font:14px/1.5 Arial,sans-serif;height:100%;min-height:200px}' +
      '@media(max-width:600px){.duo-panel{grid-template-columns:1fr}.duo-panel .expert-screen{min-height:200px}}';
    document.head.append(css);

    document.querySelectorAll('article[id]').forEach(function (article) {
      var screen = article.querySelector('.screen');
      if (!screen) return;

      // Don't wrap if already wrapped
      if (screen.parentElement.classList.contains('duo-panel')) return;

      // Create the duo panel wrapper
      var panel = document.createElement('div');
      panel.className = 'duo-panel';

      // Move the existing screen into the panel
      screen.replaceWith(panel);
      panel.append(screen);

      // Add anchor badge to existing screen
      var anchorBadge = document.createElement('span');
      anchorBadge.className = 'anchor-badge';
      anchorBadge.textContent = 'ANCHOR / 主播';
      screen.append(anchorBadge);

      // Create the expert panel
      var expertScreen = document.createElement('div');
      expertScreen.className = 'expert-screen';

      if (imageExists) {
        var expertImg = document.createElement('img');
        expertImg.src = EXPERT_IMG;
        expertImg.alt = 'AI expert analyst studio still';
        expertScreen.append(expertImg);
      } else {
        var placeholder = document.createElement('div');
        placeholder.className = 'expert-placeholder';
        placeholder.innerHTML = 'Expert analyst image<br>专家分析师图像<br><br><small>Image pending / 图像待添加</small>';
        expertScreen.append(placeholder);
      }

      // Expert badge
      var expertBadge = document.createElement('span');
      expertBadge.className = 'expert-badge';
      expertBadge.textContent = 'EXPERT / 专家';
      expertScreen.append(expertBadge);

      // Expert lower label
      var expertLabel = document.createElement('div');
      expertLabel.className = 'expert-label';
      expertLabel.innerHTML = 'EXPERT ANALYST<br>专家分析';
      expertScreen.append(expertLabel);

      panel.append(expertScreen);
    });
  }
})();
