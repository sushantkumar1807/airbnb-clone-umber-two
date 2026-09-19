const fs = require('fs');

// 1. heroGrid.html: ends at </section>
let hero = fs.readFileSync('ref_sections/heroGrid.html', 'utf8');
hero = hero.substring(0, hero.lastIndexOf('</section>') + 10);
fs.writeFileSync('ref_sections/heroGrid.html', hero);

// 2. stickySubnav.html: ends at </div></div></div> (close of _JXzroy)
let sticky = fs.readFileSync('ref_sections/stickySubnav.html', 'utf8');
const subnavClose = sticky.indexOf('</button></div></div></div>');
if (subnavClose !== -1) {
  sticky = sticky.substring(0, subnavClose + '</button></div></div></div>'.length);
}
fs.writeFileSync('ref_sections/stickySubnav.html', sticky);

// 3. contentLeft.html: ends at Clear dates</button></div></div></div> (close of calendar)
let cl = fs.readFileSync('ref_sections/contentLeft.html', 'utf8');
const clClose = cl.indexOf('Clear dates</button></div></div></div>');
if (clClose !== -1) {
  cl = cl.substring(0, clClose + 'Clear dates</button></div></div></div>'.length);
}
fs.writeFileSync('ref_sections/contentLeft.html', cl);

// 4. bookingSticky.html: ends at </a></div></div> (close of bookingSticky)
let bs = fs.readFileSync('ref_sections/bookingSticky.html', 'utf8');
// remove leading <aside> if present or trailing </aside>...
const reportIdx = bs.indexOf('Report this listing</a></div></div>');
if (reportIdx !== -1) {
  bs = bs.substring(0, reportIdx + 'Report this listing</a></div></div>'.length);
}
fs.writeFileSync('ref_sections/bookingSticky.html', bs);

// 5. locationAndWide.html:
let lw = fs.readFileSync('ref_sections/locationAndWide.html', 'utf8');
const lwClose = lw.lastIndexOf('</section>');
if (lwClose !== -1) {
  lw = lw.substring(0, lwClose + 10);
}
fs.writeFileSync('ref_sections/locationAndWide.html', lw);

// 6. toast.html:
let toast = fs.readFileSync('ref_sections/toast.html', 'utf8');
const toastClose = toast.indexOf('</div>');
if (toastClose !== -1) {
  toast = toast.substring(0, toastClose + 6);
}
fs.writeFileSync('ref_sections/toast.html', toast);

console.log('All slices cleaned and trimmed successfully!');
