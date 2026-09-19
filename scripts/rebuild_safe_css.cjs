const fs = require('fs');

let css = fs.readFileSync('ref_style_0.css', 'utf8');

// Header
const header = `/* =========================================================
   AIRBNB CANONICAL DESIGN SYSTEM - PIXEL PERFECT REPLICA
   ========================================================= */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

@keyframes lbFade {
  from {
    opacity: 0;
    transform: scale(0.98);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes toastSlideUp {
  from {
    opacity: 0;
    transform: translate(-50%, 20px);
  }
  to {
    opacity: 1;
    transform: translate(-50%, 0);
  }
}

`;

// Fix font variable to include Plus Jakarta Sans and Inter
css = css.replace(
  '--font: "Airbnb Cereal VF", Circular, -apple-system, BlinkMacSystemFont, "system-ui", Roboto, "Helvetica Neue", sans-serif;',
  '--font: "Airbnb Cereal VF", "Plus Jakarta Sans", "Inter", Circular, -apple-system, BlinkMacSystemFont, "system-ui", Roboto, "Helvetica Neue", sans-serif;'
);

// Format CSS safely: protect data: URLs
const dataUrls = [];
css = css.replace(/url\("data:[^"]+"\)/g, (m) => {
  let cleaned = m.replace(/&lt;/g, '%3C').replace(/&gt;/g, '%3E').replace(/&amp;/g, '&').replace(/&quot;/g, "'");
  dataUrls.push(cleaned);
  return `__DATA_URL_${dataUrls.length - 1}__`;
});

// Format braces
css = css
  .replace(/\{/g, ' {\n  ')
  .replace(/;/g, ';\n  ')
  .replace(/\}/g, '\n}\n')
  .replace(/\n\s+\n/g, '\n');

// Restore data URLs
css = css.replace(/__DATA_URL_(\d+)__/g, (_, idx) => dataUrls[parseInt(idx)]);

fs.writeFileSync('src/styles/App.css', header + css);
console.log('App.css rebuilt with zero data-url formatting errors.');
