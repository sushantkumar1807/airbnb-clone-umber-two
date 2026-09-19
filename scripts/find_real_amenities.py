import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']

for i, s in enumerate(sections):
    sec_id = s.get('sectionId')
    if sec_id and 'AMENITIES' in sec_id:
        print(f"Found {sec_id} at index {i}")
        sec = s.get('section', {})
        print(json.dumps(sec, indent=2)[:3000])
