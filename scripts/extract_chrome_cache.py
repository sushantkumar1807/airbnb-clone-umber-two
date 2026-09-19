import os
import glob
import re

base_dir = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
target_host = b'airbnb-clone-umber-two.vercel.app'
matches = []

for root, dirs, files in os.walk(base_dir):
    if 'Cache_Data' in root:
        for f in files:
            if f.startswith('f_'):
                fpath = os.path.join(root, f)
                try:
                    with open(fpath, 'rb') as fp:
                        data = fp.read()
                        if target_host in data:
                            urls = re.findall(rb'https://airbnb-clone-umber-two\.vercel\.app/[^\s\x00"\'<>]+', data)
                            for u in set(urls):
                                matches.append((fpath, u.decode('utf-8', errors='ignore'), len(data)))
                except Exception:
                    pass

print(f"Found {len(matches)} matches across all Chrome caches!")
for fpath, u, sz in matches[:40]:
    print(f"{sz} bytes | {u} -> {os.path.basename(fpath)}")
