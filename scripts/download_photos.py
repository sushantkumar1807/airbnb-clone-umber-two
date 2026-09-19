import os
import urllib.request
import json
import time

os.makedirs('assets/photos', exist_ok=True)
os.makedirs('assets/nearby', exist_ok=True)

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']
sec30 = sections[30]['section']
media = sec30.get('mediaItems', [])

print(f"Total media items to download: {len(media)}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

downloaded_photos = []

# Map label prefixes to category keys
cat_map = {
    'Living room 1': 'living1',
    'Living room 2': 'living2',
    'Full kitchen': 'kitchen',
    'Bedroom': 'bedroom',
    'Full bathroom': 'bathroom',
    'Gym': 'gym',
    'Exterior': 'exterior',
    'Pool': 'pool',
    'Additional photos': 'additional'
}

for i, m in enumerate(media):
    label = m.get('accessibilityLabel', f'Photo {i+1}')
    base_url = m.get('baseUrl', '')
    aspect = m.get('aspectRatio', 1.33)
    orientation = m.get('orientation', 'LANDSCAPE')
    
    # Determine category
    cat_key = 'additional'
    for prefix, k in cat_map.items():
        if label.startswith(prefix):
            cat_key = k
            break
            
    filename = f"photo_{i+1:02d}_{cat_key}.jpg"
    filepath = os.path.join('assets', 'photos', filename)
    
    # High res URL with Airbnb image service query
    download_url = f"{base_url}?im_w=1200"
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) < 1000:
        try:
            req = urllib.request.Request(download_url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                with open(filepath, 'wb') as out_f:
                    out_f.write(content)
            print(f"[{i+1}/{len(media)}] Downloaded {filename} ({len(content)} bytes)")
            time.sleep(0.05)
        except Exception as e:
            print(f"[{i+1}/{len(media)}] Failed to download {download_url}: {e}")
    else:
        print(f"[{i+1}/{len(media)}] Already exists {filename}")

    downloaded_photos.append({
        'id': i,
        'cat': cat_key,
        'label': label,
        'src': f"assets/photos/{filename}",
        'remoteSrc': download_url,
        'aspectRatio': aspect,
        'orientation': orientation
    })

with open('assets/photos_data.json', 'w', encoding='utf-8') as out_f:
    json.dump(downloaded_photos, out_f, indent=2)

print(f"Successfully saved {len(downloaded_photos)} photos metadata to assets/photos_data.json")
