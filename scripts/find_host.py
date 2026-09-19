import json

with open('airbnb_state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Search for host details
def find_host(obj, path=""):
    if isinstance(obj, dict):
        if 'host' in obj or 'user' in obj or 'avatarUrl' in obj or 'profilePicUrl' in obj:
            print(f"Path: {path}")
            for k in ['name', 'firstName', 'hostName', 'avatarUrl', 'profilePicUrl', 'thumbnailUrl']:
                if k in obj:
                    print(f"  {k}: {obj[k]}")
        for k, v in obj.items():
            find_host(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            find_host(item, f"{path}[{i}]")

find_host(data)
