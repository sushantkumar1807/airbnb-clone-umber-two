const fs = require('fs');

let css = fs.readFileSync('formatted_ref.css', 'utf8');

// Prepend Google font import & keyframes
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

fs.writeFileSync('src/styles/App.css', header + css);
console.log('App.css successfully updated with canonical reference stylesheet!');
