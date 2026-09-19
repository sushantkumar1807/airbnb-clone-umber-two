import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']

for i, s in enumerate(sections):
    sec = s.get('section') or {}
    sec_id = s.get('sectionId') or sec.get('id') or sec.get('__typename')
    typename = sec.get('__typename')
    title = sec.get('title') or sec.get('heading') or ''
    media = sec.get('mediaItems', [])
    print(f"[{i}] {sec_id} | typename: {typename} | media: {len(media)} | title: {title}")
