import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

photos = []
def search(obj, path=""):
    if isinstance(obj, dict):
        if 'pictureUrl' in obj and isinstance(obj['pictureUrl'], str) and 'Hosting-1599895892448055764' in obj['pictureUrl']:
            photos.append((path, obj))
        elif 'baseUrl' in obj and isinstance(obj['baseUrl'], str) and 'Hosting-1599895892448055764' in obj['baseUrl']:
            photos.append((path, obj))
        for k, v in obj.items():
            search(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            search(item, f"{path}[{i}]")

search(data)

print(f"Total matching photos: {len(photos)}")
for pth, p in photos[:3]:
    print(f"Path: {pth}")
    print(f"Keys: {list(p.keys())}")
    for k, v in p.items():
        if not isinstance(v, (dict, list)):
            print(f"  {k}: {v}")
