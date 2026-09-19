const fs = require('fs');
const html = fs.readFileSync('ref_dump.html', 'utf8');

const slices = [
  { name: 'siteHeader', start: 439, end: 6426 },
  { name: 'stickySubnav', start: 6426, end: 7175 },
  { name: 'listingHeader', start: 7175, end: 8604 },
  { name: 'heroGrid', start: 8604, end: 10570 },
  { name: 'contentLeft', start: 10570, end: 39762 },
  { name: 'bookingSticky', start: 39762, end: 41727 },
  { name: 'reviews', start: 41727, end: 66158 },
  { name: 'locationAndWide', start: 66158, end: 81247 },
  { name: 'photoTourModal', start: 81247, end: 98072 },
  { name: 'lightboxModal', start: 98072, end: 100348 },
  { name: 'amenModal', start: 100348, end: 137678 },
  { name: 'toast', start: 137678, end: 137850 }
];

fs.mkdirSync('ref_sections', { recursive: true });
for (const s of slices) {
  const content = html.substring(s.start, s.end).trim();
  fs.writeFileSync(`ref_sections/${s.name}.html`, content);
  console.log(`Saved ${s.name}.html (${content.length} chars)`);
}
