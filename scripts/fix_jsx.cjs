const fs = require('fs');

function cleanHtmlToJsx(html) {
  let jsx = html
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/\bclass=/g, 'className=')
    .replace(/\bfor=/g, 'htmlFor=')
    .replace(/\bclip-rule=/g, 'clipRule=')
    .replace(/\bfill-rule=/g, 'fillRule=')
    .replace(/\bstroke-width=/g, 'strokeWidth=')
    .replace(/\bstroke-linecap=/g, 'strokeLinecap=')
    .replace(/\bstroke-linejoin=/g, 'strokeLinejoin=')
    .replace(/\bstroke-miterlimit=/g, 'strokeMiterlimit=')
    .replace(/\bxmlns:xlink=/g, 'xmlnsXlink=')
    .replace(/\bxlink:href=/g, 'xlinkHref=')
    .replace(/<br>/gi, '<br />')
    .replace(/<hr>/gi, '<hr />');

  // Self-close void HTML tags only: img, input
  jsx = jsx.replace(/<(img|input)([^>]*?)(?<!\/)>/gi, '<$1$2 />');

  // SVG tags that may be void if they don't have matching close tag
  const svgTags = ['rect', 'circle', 'line', 'polyline', 'polygon', 'path'];
  for (const tag of svgTags) {
    // If there's no </tag>, self close it
    const selfCloseRegex = new RegExp(`<(${tag})([^>]*?)(?<!\\/)>(?!([\\s\\S]*?<\\/\\1>))`, 'gi');
    // But easier: if the tag doesn't have a matching close tag nearby, self-close
    // Actually in SVG, if there is </path>, let it be <path ...></path>!
    // If there is <path ...> without </path>, make it <path ... />
  }

  // Convert inline style strings: style="..." to style={{ ... }}
  jsx = jsx.replace(/style="([^"]*)"/g, (m, styleStr) => {
    const props = styleStr.split(';').filter(p => p.trim());
    const objProps = props.map(p => {
      const parts = p.split(':');
      if (parts.length < 2) return '';
      let key = parts[0].trim();
      let val = parts.slice(1).join(':').trim();
      // camelCase key
      key = key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
      return `${key}: '${val}'`;
    }).filter(Boolean);
    return `style={{ ${objProps.join(', ')} }}`;
  });

  return jsx;
}

// Let's test on Highlights
const contentLeftHtml = fs.readFileSync('ref_sections/contentLeft.html', 'utf8');
const hlHtml = contentLeftHtml.substring(10824, 14536).trim();

// Check if <path> in hlHtml has </path>
console.log('Original hlHtml has </path>?', hlHtml.includes('</path>'));
