import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']

sec30 = sections[30]['section']
media = sec30.get('mediaItems', [])
print(f"Total media in Photo Tour: {len(media)}")

for i, m in enumerate(media):
    label = m.get('accessibilityLabel', '')
    url = m.get('baseUrl', '')
    print(f"{i:2d}: {label:30s} -> {url}")
