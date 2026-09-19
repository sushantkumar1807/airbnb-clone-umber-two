import urllib.request
import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find all photo objects and structure them by category
# Let's inspect where photos are defined in airbnb_state.json with their captions
photos_by_cat = {}
seen_urls = set()

def find_photos(obj):
    if isinstance(obj, dict):
        if 'pictureUrl' in obj and 'caption' in obj:
            cap = obj['caption']
            url = obj['pictureUrl']
            if url not in seen_urls and 'Hosting-1599895892448055764' in url:
                seen_urls.add(url)
                print(f"CAPTION: {cap} => {url}")
        for v in obj.values():
            find_photos(v)
    elif isinstance(obj, list):
        for item in obj:
            find_photos(item)

find_photos(data)
