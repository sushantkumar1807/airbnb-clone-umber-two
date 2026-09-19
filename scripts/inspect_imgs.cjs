const fs = require('fs');
const html = fs.readFileSync('clean_structure.html', 'utf8');

const regex = /<img[^>]*>/gi;
let match;
let i = 0;
while ((match = regex.exec(html)) !== null && i < 50) {
  const tag = match[0];
  const src = (tag.match(/src="([^"]+)"/) || [])[1];
  const alt = (tag.match(/alt="([^"]*)"/) || [])[1];
  const className = (tag.match(/class="([^"]+)"/) || [])[1];
  console.log(`[${++i}] src: ${src} | alt: ${alt} | class: ${className}`);
}
