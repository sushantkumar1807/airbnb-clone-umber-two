const fs = require('fs');
const html = fs.readFileSync('clean_structure.html', 'utf8');

const regex = /<button[^>]+data-idx="(\d+)"[^>]*>([\s\S]*?)<\/button>/gi;
let match;
const photosMap = [];
while ((match = regex.exec(html)) !== null) {
  const idx = parseInt(match[1]);
  const content = match[2];
  const src = (content.match(/src="([^"]+)"/) || [])[1];
  const alt = (content.match(/alt="([^"]*)"/) || [])[1];
  photosMap.push({ idx, src, alt });
}
photosMap.sort((a, b) => a.idx - b.idx);
console.log('Total mapped photos:', photosMap.length);
console.log(JSON.stringify(photosMap.slice(0, 15), null, 2));
fs.writeFileSync('ref_photos_map.json', JSON.stringify(photosMap, null, 2));
