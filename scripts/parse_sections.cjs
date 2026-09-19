const fs = require('fs');
const html = fs.readFileSync('clean_structure.html', 'utf8');

// List of major IDs/sections:
const sections = [
  { name: 'siteHeader', pattern: /<header class="_Ugwssa" id="siteHeader">[\s\S]*?<\/header>/ },
  { name: 'stickySubnav', pattern: /<div class="_JXzroy[^"]*" id="_JXzroy"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'listingHeader', pattern: /<section class="_DbxOEt" id="photos">[\s\S]*?<\/section>/ },
  { name: 'heroGrid', pattern: /<section class="_Zndiww" id="_Zndiww"[\s\S]*?<\/section>/ },
  { name: 'contentLeftTop', pattern: /<div class="_gRekoP">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'guestFavourite', pattern: /<div class="_NIsTQW">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'hostRow', pattern: /<div class="_McRwJR">[\s\S]*?<\/div>\s*<\/div>/ },
  { name: 'highlights', pattern: /<div class="_ZOaIER"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'description', pattern: /<div class="_YidPyi"[\s\S]*?<\/button>\s*<\/div>/ },
  { name: 'sleep', pattern: /<div class="_QZaLue">\s*<h2 class="_XZmvOH">Where you'll sleep[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'amenities', pattern: /<div class="_QZaLue" id="amenities">[\s\S]*?<\/button>\s*<\/div>/ },
  { name: 'calendar', pattern: /<div class="_QZaLue">\s*<div>\s*<div class="_zAWnNQ">[\s\S]*?<\/button>\s*<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'bookingSticky', pattern: /<aside class="_iJTxKe">[\s\S]*?<\/aside>/ },
  { name: 'reviews', pattern: /<section class="_WNEjqG" id="reviews">[\s\S]*?<\/section>/ },
  { name: 'location', pattern: /<section class="_WNEjqG" id="location">[\s\S]*?<\/section>/ },
  { name: 'hostSection', pattern: /<div class="_UiBrsI">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'thingsToKnow', pattern: /<div class="_qYvLOs">[\s\S]*?<\/div>\s*<\/div>/ },
  { name: 'nearby', pattern: /<div class="_cixxXf">[\s\S]*?<\/div>\s*<\/div>/ },
  { name: 'photoTourModal', pattern: /<div class="_KpcKWX[^"]*" id="_KpcKWX"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/ },
  { name: 'lightboxModal', pattern: /<div class="_zFbfbh[^"]*" id="lightbox"[\s\S]*?<\/div>\s*<\/div>/ },
  { name: 'amenitiesModal', pattern: /<div class="_yBjuYG[^"]*" id="amenModal"[\s\S]*?<\/div>\s*<\/div>/ },
  { name: 'toast', pattern: /<div class="_HALoyX[^"]*" id="_HALoyX"[\s\S]*?<\/div>/ }
];

console.log('Testing sections extraction...');
for (const s of sections) {
  const m = html.match(s.pattern);
  console.log(`${s.name}: ${m ? 'FOUND (' + m[0].length + ' chars)' : 'NOT FOUND'}`);
}
