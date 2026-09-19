const fs = require('fs');
const html = fs.readFileSync('clean_structure.html', 'utf8');

const regex = /<img[^>]*>/gi;
let match;
const imgs = [];
while ((match = regex.exec(html)) !== null) {
  const tag = match[0];
  const src = (tag.match(/src="([^"]+)"/) || [])[1];
  const alt = (tag.match(/alt="([^"]*)"/) || [])[1];
  const className = (tag.match(/class="([^"]+)"/) || [])[1];
  imgs.push({ src, alt, className });
}

// Group by prefix
const ui = imgs.filter(x => x.src && x.src.includes('/ui/'));
const chips = imgs.filter(x => x.src && x.src.includes('/chips/'));
const avatars = imgs.filter(x => x.src && x.src.includes('/avatars/'));
const similar = imgs.filter(x => x.src && x.src.includes('/similar/'));
const photos = imgs.filter(x => x.src && !x.src.includes('/ui/') && !x.src.includes('/chips/') && !x.src.includes('/avatars/') && !x.src.includes('/similar/'));

console.log('UI images:', [...new Set(ui.map(x => x.src))]);
console.log('Chip images:', [...new Set(chips.map(x => x.src))]);
console.log('Avatar images:', [...new Set(avatars.map(x => x.src))]);
console.log('Similar stays images:', [...new Set(similar.map(x => x.src))]);
console.log('Property photos count:', new Set(photos.map(x => x.src)).size);
console.log('Property photos:', [...new Set(photos.map(x => x.src))].slice(0, 10));
