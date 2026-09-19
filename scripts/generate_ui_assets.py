import os
from PIL import Image, ImageDraw, ImageFont
import math

os.makedirs('public/assets/images/ui', exist_ok=True)
os.makedirs('public/assets/images/chips', exist_ok=True)
os.makedirs('public/assets/images/avatars', exist_ok=True)
os.makedirs('public/assets/images/similar', exist_ok=True)

# 1. discount.svg
discount_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none">
  <path d="M14.5 3.5L3.5 14.5C2.5 15.5 2.5 17.1 3.5 18.1L13.9 28.5C14.9 29.5 16.5 29.5 17.5 28.5L28.5 17.5C29.5 16.5 29.5 14.9 28.5 13.9L21.5 6.9C21 6.4 20.3 6.1 19.6 6.1L16.2 6.1C15.6 6.1 14.9 5.8 14.5 5.4L14.5 3.5Z" fill="#F4511E" stroke="#E64A19" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="23" cy="11" r="2.5" fill="#FFF"/>
  <path d="M11 19L17 13M12.5 14H12.51M15.5 18H15.51" stroke="#FFF" stroke-width="2" stroke-linecap="round"/>
</svg>'''
with open('public/assets/images/ui/discount.svg', 'w', encoding='utf-8') as f:
    f.write(discount_svg)

# 2. searchbar-house.png (48x48)
img_house = Image.new('RGBA', (96, 96), (255, 255, 255, 0))
draw = ImageDraw.Draw(img_house)
# Draw cute Airbnb coral house icon
draw.polygon([(48, 16), (82, 44), (74, 44), (74, 76), (22, 76), (22, 44), (14, 44)], fill=(255, 56, 92, 255))
draw.rectangle([(38, 48), (58, 76)], fill=(255, 255, 255, 255))
draw.polygon([(48, 10), (88, 44), (82, 48), (48, 20), (14, 48), (8, 44)], fill=(230, 30, 77, 255))
img_house = img_house.resize((48, 48), Image.Resampling.LANCZOS)
img_house.save('public/assets/images/ui/searchbar-house.png', 'PNG')

# 3. laurel-left.png and laurel-right.png (height 110px, ~70x110)
def draw_laurel(flipped=False):
    w, h = 140, 220
    img = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    
    # Draw curved stem
    points = []
    for t in range(100):
        angle = -math.pi * 0.4 + (t / 100.0) * math.pi * 0.95
        r = 85
        cx, cy = 110, 110
        x = cx - math.cos(angle) * r
        y = cy + math.sin(angle) * r
        points.append((x, y))
    
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=(34, 34, 34, 255), width=4)
        
    # Draw leaves along stem
    for i in range(10, len(points) - 5, 8):
        x, y = points[i]
        # calculate tangent
        dx = points[i+1][0] - points[i-1][0]
        dy = points[i+1][1] - points[i-1][1]
        norm = math.hypot(dx, dy)
        if norm > 0:
            nx, ny = -dy / norm, dx / norm
            # outer leaf
            lx, ly = x + nx * 18, y + ny * 18
            d.ellipse([lx - 9, ly - 6, lx + 9, ly + 6], fill=(34, 34, 34, 255))
            # inner leaf
            lx2, ly2 = x - nx * 10, y - ny * 10
            d.ellipse([lx2 - 7, ly2 - 5, lx2 + 7, ly2 + 5], fill=(34, 34, 34, 255))
            
    img = img.resize((70, 110), Image.Resampling.LANCZOS)
    if flipped:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img

laurel_left = draw_laurel(flipped=False)
laurel_left.save('public/assets/images/ui/laurel-left.png', 'PNG')
laurel_right = draw_laurel(flipped=True)
laurel_right.save('public/assets/images/ui/laurel-right.png', 'PNG')

# 4. Chip icons (40x40 transparent PNGs with nice distinct icons)
chips = [
    ('comfort', (230, 81, 0)),
    ('accuracy', (46, 125, 50)),
    ('hot-tub', (2, 136, 209)),
    ('condition', (156, 39, 176)),
    ('hospitality', (216, 27, 96)),
    ('cleanliness', (0, 150, 136)),
    ('amenities', (245, 124, 0)),
    ('decor', (121, 85, 72)),
    ('indoor-spaces', (69, 90, 100)),
    ('location', (198, 40, 40))
]

for name, color in chips:
    img = Image.new('RGBA', (80, 80), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([6, 6, 74, 74], fill=(color[0], color[1], color[2], 25))
    d.ellipse([10, 10, 70, 70], outline=color, width=3)
    if name == 'comfort':
        # bed/sofa
        d.rectangle([22, 38, 58, 54], fill=color)
        d.rectangle([20, 28, 32, 38], fill=color)
    elif name == 'accuracy':
        # target
        d.ellipse([26, 26, 54, 54], outline=color, width=3)
        d.ellipse([36, 36, 44, 44], fill=color)
    elif name == 'hot-tub':
        # waves / tub
        d.arc([20, 30, 60, 56], 0, 180, fill=color, width=4)
        d.line([(24, 30), (56, 30)], fill=color, width=3)
    elif name == 'condition':
        # star/sparkle
        d.polygon([(40, 18), (44, 32), (58, 34), (46, 44), (50, 58), (40, 48), (30, 58), (34, 44), (22, 34), (36, 32)], fill=color)
    elif name == 'hospitality':
        # heart
        d.polygon([(40, 58), (20, 36), (20, 26), (30, 20), (40, 28), (50, 20), (60, 26), (60, 36)], fill=color)
    elif name == 'cleanliness':
        # sparkles
        d.ellipse([24, 24, 38, 38], fill=color)
        d.ellipse([42, 36, 58, 52], fill=color)
    elif name == 'amenities':
        # cup
        d.rectangle([26, 32, 50, 54], fill=color)
        d.arc([46, 36, 58, 48], 270, 90, fill=color, width=3)
    elif name == 'decor':
        # lamp
        d.polygon([(26, 40), (54, 40), (48, 22), (32, 22)], fill=color)
        d.line([(40, 40), (40, 58)], fill=color, width=3)
    elif name == 'indoor-spaces':
        # door
        d.rectangle([26, 20, 54, 58], outline=color, width=3)
        d.ellipse([46, 38, 50, 42], fill=color)
    elif name == 'location':
        # pin
        d.ellipse([28, 20, 52, 44], fill=color)
        d.polygon([(30, 38), (50, 38), (40, 58)], fill=color)
        d.ellipse([36, 28, 44, 36], fill=(255, 255, 255, 255))
    img = img.resize((40, 40), Image.Resampling.LANCZOS)
    img.save(f'public/assets/images/chips/{name}.png', 'PNG')

# 5. Avatars
avatar_colors = [
    ('host.jpeg', (230, 81, 0), 'M', 'Mirashya'),
    ('co1.jpg', (30, 136, 229), 'S', 'Sharath'),
    ('co2.jpg', (67, 160, 71), 'A', 'Aman'),
    ('co3.jpg', (142, 36, 170), 'M', 'Maria'),
    ('rev1.jpeg', (0, 137, 123), 'A', 'Aheesh'),
    ('rev2.jpeg', (229, 57, 53), 'S', 'Samiksha'),
    ('rev3.jpeg', (57, 73, 171), 'V', 'Vaibhav'),
    ('rev4.jpeg', (109, 76, 65), 'M', 'Mohd'),
    ('rev5.jpeg', (216, 27, 96), 'S', 'Simran')
]

for filename, bg, initial, name in avatar_colors:
    img = Image.new('RGB', (120, 120), bg)
    d = ImageDraw.Draw(img)
    # circle face styling
    d.ellipse([30, 24, 90, 84], fill=(255, 255, 255, 210))
    d.ellipse([20, 88, 100, 150], fill=(255, 255, 255, 210))
    img.save(f'public/assets/images/avatars/{filename}', 'JPEG', quality=92)

# 6. Copy nearby photos to similar/
for i in range(1, 9):
    src_p = f'public/assets/nearby/nearby_0{i}.webp'
    tgt_p = f'public/assets/images/similar/s{((i-1)%6)+1}.jpeg'
    if os.path.exists(src_p):
        im = Image.open(src_p).convert('RGB')
        im.save(tgt_p, 'JPEG', quality=88)

print("UI Assets and Avatars generated successfully!")
