import re
import json

with open('airbnb_room.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Look for data-state or script tags with JSON
scripts = re.findall(r'<script[^>]*id="data-deferred-state-0"[^>]*>(.*?)</script>', html, re.DOTALL)
if not scripts:
    scripts = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.DOTALL)

print(f"Found {len(scripts)} json script tags")

# Let's search for muscache images
img_pattern = re.compile(r'https://a0\.muscache\.com/im/pictures/[a-zA-Z0-9_\-\.\/]+')
urls = img_pattern.findall(html)
clean_urls = []
for u in urls:
    # strip trailing params or weird chars
    u_clean = u.split('?')[0].rstrip('\\"\'')
    if u_clean.endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif')) or '/pictures/' in u_clean:
        if u_clean not in clean_urls:
            clean_urls.append(u_clean)

print(f"Total clean image URLs: {len(clean_urls)}")
for i, u in enumerate(clean_urls[:30]):
    print(f"{i}: {u}")

# Let's check for photoTour or photo objects in json
photo_blocks = re.findall(r'\{[^{}]*"pictureUrl"[^{}]*\}', html)
print(f"Found {len(photo_blocks)} photo blocks")
if photo_blocks:
    for b in photo_blocks[:5]:
        print("Block:", b[:200])

# Let's look for categories or rooms
room_blocks = re.findall(r'\{[^{}]*"roomType"[^{}]*\}', html)
print(f"Found {len(room_blocks)} room blocks")
