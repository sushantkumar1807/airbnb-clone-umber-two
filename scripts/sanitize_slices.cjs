const fs = require('fs');

const files = fs.readdirSync('ref_sections');
for (const f of files) {
  let content = fs.readFileSync('ref_sections/' + f, 'utf8').trim();
  console.log(`Checking ${f}...`);
  // If f is heroGrid, check if it ends with </section>
  if (f === 'heroGrid.html') {
    const lastSection = content.lastIndexOf('</section>');
    if (lastSection !== -1) {
      content = content.substring(0, lastSection + 10);
      fs.writeFileSync('ref_sections/' + f, content);
      console.log(`Trimmed ${f} to </section>`);
    }
  }
}
