const fs = require('fs');
const contentLeft = fs.readFileSync('ref_sections/contentLeft.html', 'utf8');

console.log('contentLeft length:', contentLeft.length);
// Find positions of key markers:
const markers = [
  '<div class="_gRekoP">',
  '<div class="_ZOaIER"',
  '<div class="_YidPyi"',
  '<div class="_QZaLue"><h2 class="_XZmvOH">Where you\'ll sleep',
  '<div class="_QZaLue" id="amenities">',
  '<div class="_QZaLue"><div><div class="_zAWnNQ">'
];

markers.forEach(m => {
  console.log(m, 'at index:', contentLeft.indexOf(m));
});
