import os
import urllib.request

os.makedirs('assets/nearby', exist_ok=True)

# Curated high quality vacation rental / apartment / pool photos
nearby_urls = [
    ("nearby_01.jpg", "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80"),
    ("nearby_02.jpg", "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=600&q=80"),
    ("nearby_03.jpg", "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=600&q=80"),
    ("nearby_04.jpg", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80"),
    ("nearby_05.jpg", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80"),
    ("nearby_06.jpg", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80"),
    ("nearby_07.jpg", "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=600&q=80"),
    ("nearby_08.jpg", "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=600&q=80"),
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in nearby_urls:
    path = os.path.join('assets', 'nearby', name)
    if not os.path.exists(path) or os.path.getsize(path) < 1000:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                with open(path, 'wb') as f:
                    f.write(data)
            print(f"Downloaded {name} ({len(data)} bytes)")
        except Exception as e:
            print(f"Error {name}: {e}")
    else:
        print(f"Already exists {name}")
