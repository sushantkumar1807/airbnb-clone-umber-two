const fs = require('fs');
const html = fs.readFileSync('ref_dump.html', 'utf8');

// List of major IDs/sections in ref_dump.html:
const sectionNames = [
  'siteHeader',
  '_JXzroy',
  'photos',
  '_Zndiww',
  'contentLeft',
  'bookingSticky',
  'reviews',
  'location',
  '_KpcKWX',
  'lightbox',
  'amenModal',
  '_HALoyX'
];

fs.mkdirSync('ref_sections', { recursive: true });

// Extract by ID
for (const id of sectionNames) {
  // Find start of tag with this id
  const startIdx = html.indexOf(`id="${id}"`);
  if (startIdx !== -1) {
    // find the tag opening '<' before id
    const tagStart = html.lastIndexOf('<', startIdx);
    // Find matching close or grab next 10000 chars
    // Let's grab context
    console.log(`Found id="${id}" at index ${startIdx} (tagStart ${tagStart})`);
  } else {
    console.log(`id="${id}" NOT found`);
  }
}
