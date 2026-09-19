const fs = require('fs');
const js = fs.readFileSync('decoded_bundle.js', 'utf8');
console.log('JS length:', js.length);

const dataUrls = js.match(/data:image\/[^;]+;base64,[A-Za-z0-9+/=]+/g) || [];
console.log('Data URLs found:', dataUrls.length);

const assets = js.match(/\/assets\/images\/[^"'\s\)]+/g) || [];
console.log('Assets referenced in bundle count:', new Set(assets).size);
console.log('Assets list:', Array.from(new Set(assets)).slice(0, 30));
