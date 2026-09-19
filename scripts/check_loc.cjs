const fs = require('fs');
const loc = fs.readFileSync('ref_sections/locationAndWide.html', 'utf8');

console.log('locationAndWide length:', loc.length);
const markers = [
  '<section class="_WNEjqG" id="location">',
  '<section class="_WNEjqG"><h2 class="_XZmvOH">Meet your host',
  '<section class="_WNEjqG"><h2 class="_XZmvOH">Things to know',
  '<section class="_WNEjqG"><div class="_cixxXf">'
];

markers.forEach(m => {
  console.log(m, 'at index:', loc.indexOf(m));
});
