import json
import re

with open('airbnb-clone-source (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('src/data/listingData.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

# Extract PHOTOS and NEARBY from listingData.js
m_photos = re.search(r'photos:\s*(\[.*?\]),\s*reviews:', js_text, re.DOTALL)
m_nearby = re.search(r'nearby:\s*(\[.*?\])\s*\}\;', js_text, re.DOTALL)

photos_json = m_photos.group(1) if m_photos else '[]'
nearby_json = m_nearby.group(1) if m_nearby else '[]'

# Let's update sleep cards HTML in airbnb-clone-source (1).html
old_sleep = """      <section class="sleep" aria-label="Where you'll sleep">
        <h2>Where you'll sleep</h2>
        <div class="sleep-grid">
          <div class="sleep-card">
            <div class="ph" style="--c1:#e7d3ae;--c2:#a67c52"><span class="ph-label">Bedroom</span></div>
            <p class="room">Bedroom</p><p class="item">1 double bed</p>
          </div>
          <div class="sleep-card">
            <div class="ph" style="--c1:#e2b877;--c2:#8a5a2b"><span class="ph-label">Living room</span></div>
            <p class="room">Living room</p><p class="item">1 sofa</p>
          </div>
        </div>
      </section>"""

new_sleep = """      <section class="sleep" aria-label="Where you'll sleep">
        <h2>Where you'll sleep</h2>
        <div class="sleep-grid">
          <div class="sleep-card">
            <img src="/assets/photos/photo_13_bedroom.webp" alt="Bedroom" style="height:220px;border-radius:12px;margin-bottom:10px;object-fit:cover;width:100%;background:#ebebeb;" loading="lazy" />
            <p class="room">Bedroom</p><p class="item">1 double bed</p>
          </div>
          <div class="sleep-card">
            <img src="/assets/photos/photo_01_living1.webp" alt="Living room" style="height:220px;border-radius:12px;margin-bottom:10px;object-fit:cover;width:100%;background:#ebebeb;" loading="lazy" />
            <p class="room">Living room</p><p class="item">1 sofa</p>
          </div>
        </div>
      </section>"""

if old_sleep in html:
    html = html.replace(old_sleep, new_sleep)
    print("Replaced sleep section")

# Replace galleryIdx and PHOTOS array
old_gallery_data = re.search(r'const PHOTOS = \[.*?\];.*?PHOTOS\.forEach\(.*?\);', html, re.DOTALL)
if old_gallery_data:
    new_gallery_data = f"const PHOTOS = {photos_json};"
    html = html.replace(old_gallery_data.group(0), new_gallery_data)
    print("Replaced PHOTOS array with 43 real WebP photos")

# Replace galleryIdx = [0,1,3,7,15] with [3, 4, 12, 5, 28]
html = html.replace('const galleryIdx = [0,1,3,7,15];', 'const galleryIdx = [3, 4, 12, 5, 28];')
print("Updated galleryIdx to [3, 4, 12, 5, 28]")

# Replace phEl function to create an img tag
old_phel = """function phEl(photo, extraClass){
  const d = document.createElement('div');
  d.className = 'ph' + (extraClass?(' '+extraClass):'');
  d.style.setProperty('--c1', photo.c1);
  d.style.setProperty('--c2', photo.c2);
  const span = document.createElement('span');
  span.className='ph-label';
  span.textContent = photo.label;
  d.appendChild(span);
  return d;
}"""

new_phel = """function phEl(photo, extraClass){
  const img = document.createElement('img');
  img.className = extraClass || '';
  img.src = photo.webp || photo.src;
  img.alt = photo.label;
  img.loading = 'lazy';
  img.decoding = 'async';
  img.style.width = '100%';
  img.style.height = '100%';
  img.style.objectFit = 'cover';
  img.style.display = 'block';
  return img;
}"""

if old_phel in html:
    html = html.replace(old_phel, new_phel)
    print("Replaced phEl function with real image generator")

# Replace NEARBY array
old_nearby = re.search(r'const NEARBY = \[.*?\];', html, re.DOTALL)
if old_nearby:
    new_nearby = f"const NEARBY = {nearby_json};"
    html = html.replace(old_nearby.group(0), new_nearby)
    print("Replaced NEARBY array with 8 real WebP nearby stays")

# Update renderNearby paint function to use img instead of placeholder div
old_paint_card = """      const ph = document.createElement('div');
      ph.className='ph'; ph.style.setProperty('--c1',n.c1); ph.style.setProperty('--c2',n.c2);
      card.appendChild(ph);"""

new_paint_card = """      const img = document.createElement('img');
      img.src = n.img; img.alt = n.title; img.loading = 'lazy';
      img.style.height = '200px'; img.style.borderRadius = '12px'; img.style.marginBottom = '10px'; img.style.objectFit = 'cover'; img.style.width = '100%';
      card.appendChild(img);"""

if old_paint_card in html:
    html = html.replace(old_paint_card, new_paint_card)
    print("Updated nearby render paint card")

with open('airbnb-clone-source (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("airbnb-clone-source (1).html updated successfully!")
