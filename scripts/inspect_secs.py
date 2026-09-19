import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']

for idx in [20, 23, 28, 29, 30, 31]:
    if idx < len(sections):
        s = sections[idx]
        sec = s.get('section') or {}
        print(f"=== SECTION {idx}: {s.get('sectionId')} ({sec.get('__typename')}) ===")
        print(json.dumps(sec, indent=2)[:2000])
