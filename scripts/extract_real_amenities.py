import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

amenities_node = data['niobeClientData'][0][1]['data']['node']['pdpPresentation']['amenities']
see_all = amenities_node['seeAllAmenitiesGroups']

extracted = []
total_count = 0
for group in see_all:
    title = group['title']
    items = []
    for a in group['amenities']:
        items.append({
            'label': a['title'],
            'avail': a.get('available', True)
        })
        total_count += 1
    extracted.append({
        'title': title,
        'items': items
    })

print(f"Extracted {len(extracted)} groups with total {total_count} amenities!")
with open('real_amenities.json', 'w', encoding='utf-8') as out:
    json.dump(extracted, out, indent=2)

print("Saved real_amenities.json")
