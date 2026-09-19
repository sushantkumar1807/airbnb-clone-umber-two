import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Search for amenity groups
found = []
def search_amenities(obj, path=""):
    if isinstance(obj, dict):
        if 'amenityId' in obj or 'available' in obj and 'title' in obj:
            found.append((path, obj))
        for k, v in obj.items():
            search_amenities(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            search_amenities(item, f"{path}[{i}]")

search_amenities(data)
print(f"Found {len(found)} amenity items in state")
for p, o in found[:20]:
    print(f"{p}: {o.get('title') or o.get('name')}")
