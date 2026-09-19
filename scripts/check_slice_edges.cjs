const fs = require('fs');

const files = fs.readdirSync('ref_sections');
for (const f of files) {
  const content = fs.readFileSync('ref_sections/' + f, 'utf8').trim();
  console.log(`[${f}] (${content.length} chars)`);
  console.log('  START:', content.substring(0, 60).replace(/\n/g, ' '));
  console.log('  END:  ', content.substring(content.length - 60).replace(/\n/g, ' '));
}
