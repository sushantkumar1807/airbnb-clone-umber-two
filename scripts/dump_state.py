import re
import json

with open('airbnb_room.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<script[^>]*id="data-deferred-state-0"[^>]*>(.*?)</script>', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print("Parsed JSON successfully!")
    with open('airbnb_state.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, indent=2)
    print("Saved airbnb_state.json")
else:
    print("Not found data-deferred-state-0")
