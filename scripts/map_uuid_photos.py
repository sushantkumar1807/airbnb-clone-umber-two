import json
import os
from PIL import Image

with open('ref_photos_map.json', 'r') as f:
    photos_map = json.load(f)

# Listing photos list
import glob
local_photos = sorted(glob.glob('public/assets/photos/photo_*.webp'))

print(f"Total mapped photos: {len(photos_map)}, Total local photos: {len(local_photos)}")

for item in photos_map:
    idx = item['idx']
    src = item['src']
    uuid_filename = os.path.basename(src)
    if idx < len(local_photos):
        local_src = local_photos[idx]
        target_path = os.path.join('public', 'assets', 'images', uuid_filename)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        if not os.path.exists(target_path):
            im = Image.open(local_src).convert('RGB')
            im.save(target_path, 'JPEG', quality=88)

print("UUID photos populated in public/assets/images/!")
