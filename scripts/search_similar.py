import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Search for similar listings or nearby in airbnb_state.json
found_listings = []
def search_similar(obj, path=""):
    if isinstance(obj, dict):
        if 'listing' in obj or 'pricingQuote' in obj or 'structuredContent' in obj:
            if 'name' in obj or 'title' in obj:
                found_listings.append((path, obj.get('name') or obj.get('title'), obj))
        for k, v in obj.items():
            search_similar(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            search_similar(item, f"{path}[{i}]")

search_similar(data)
print(f"Found {len(found_listings)} possible listings")
for p, name, o in found_listings[:10]:
    print(f"Listing at {p}: {name}")
    # print image if any
    for k in ['picture', 'pictures', 'images', 'media', 'thumbnail']:
        if k in o:
            print(f"  has {k}: {str(o[k])[:150]}")
