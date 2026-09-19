const fs = require('fs');
const html = fs.readFileSync('clean_structure.html', 'utf8');

const ids = Array.from(html.matchAll(/id=["']([^"']+)["']/gi)).map(m => m[1]);
console.log('All IDs:', ids);

// Look at the sections
const sections = Array.from(html.matchAll(/<(header|section|aside|footer|main|nav|div\s+id="[^"]+")[^>]*>/gi)).map(m => m[0]);
console.log('Key container tags:\n', sections.join('\n'));
