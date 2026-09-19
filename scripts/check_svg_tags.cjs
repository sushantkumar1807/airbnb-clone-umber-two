const fs = require('fs');

const files = fs.readdirSync('ref_sections');
for (const f of files) {
  const content = fs.readFileSync('ref_sections/' + f, 'utf8');
  const tags = ['path', 'circle', 'rect', 'line', 'polygon'];
  for (const t of tags) {
    const opens = (content.match(new RegExp(`<${t}\\b`, 'gi')) || []).length;
    const closes = (content.match(new RegExp(`</${t}>`, 'gi')) || []).length;
    const selfCloses = (content.match(new RegExp(`<${t}[^>]*/>`, 'gi')) || []).length;
    if (opens !== closes + selfCloses) {
      console.log(`In ${f}: <${t}> opens=${opens}, closes=${closes}, selfCloses=${selfCloses}`);
    }
  }
}
