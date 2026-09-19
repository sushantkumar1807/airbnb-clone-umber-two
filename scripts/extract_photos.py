import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traverse recursively to find all dictionaries with pictureUrl or baseUrl or photos
photos = []
photo_tours = []

def search(obj, path=""):
    if isinstance(obj, dict):
        if 'pictureUrl' in obj and isinstance(obj['pictureUrl'], str) and 'muscache' in obj['pictureUrl']:
            photos.append((path, obj))
        if 'baseUrl' in obj and isinstance(obj['baseUrl'], str) and 'muscache' in obj['baseUrl']:
            photos.append((path, obj))
        if 'photoTour' in obj:
            photo_tours.append((path, obj['photoTour']))
        for k, v in obj.items():
            search(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            search(item, f"{path}[{i}]")

search(data)

print(f"Found {len(photos)} photos, {len(photo_tours)} photo_tours")

# Let's inspect photo_tours
for pth, pt in photo_tours:
    print(f"PhotoTour at {pth}:")
    if isinstance(pt, dict):
        print(f"Keys: {list(pt.keys())}")
        if 'rooms' in pt:
            print(f"Rooms count: {len(pt['rooms'])}")
            for r in pt['rooms']:
                print(f"Room: {r.get('name') or r.get('roomType')}, photos: {len(r.get('photos', []))}")
                for photo in r.get('photos', []):
                    print(f"   Photo: {photo.get('caption')} -> {photo.get('pictureUrl') or photo.get('baseUrl')}")

# If no photoTour in that exact format, let's look at photos found
unique_urls = {}
for pth, p in photos:
    url = p.get('pictureUrl') or p.get('baseUrl')
    caption = p.get('caption') or p.get('accessibilityLabel') or ''
    if url not in unique_urls:
        unique_urls[url] = (caption, pth)

print(f"\nUnique photo URLs count: {len(unique_urls)}")
for i, (u, (cap, pth)) in enumerate(unique_urls.items()):
    print(f"{i}: {u} | {cap}")
