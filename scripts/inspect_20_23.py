import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sections = data['niobeClientData'][0][1]['data']['presentation']['stayProductDetailPage']['sections']['sections']

print("=== Section 20 ===")
print(json.dumps(sections[20], indent=2))

print("=== Section 23 ===")
print(json.dumps(sections[23], indent=2))
