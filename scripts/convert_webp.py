import os
from PIL import Image
import json

photos_dir = 'assets/photos'
nearby_dir = 'assets/nearby'

os.makedirs('public/assets/photos', exist_ok=True)
os.makedirs('public/assets/nearby', exist_ok=True)

total_orig_size = 0
total_webp_size = 0

def convert_dir(src_dir, dest_dir, quality=82):
    global total_orig_size, total_webp_size
    for fname in os.listdir(src_dir):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            src_path = os.path.join(src_dir, fname)
            base_name = os.path.splitext(fname)[0]
            dest_path = os.path.join(dest_dir, base_name + '.webp')
            
            orig_size = os.path.getsize(src_path)
            total_orig_size += orig_size
            
            with Image.open(src_path) as im:
                # Convert RGBA to RGB if needed
                if im.mode in ('RGBA', 'LA', 'P'):
                    im = im.convert('RGB')
                im.save(dest_path, 'WEBP', quality=quality, method=6)
                
            webp_size = os.path.getsize(dest_path)
            total_webp_size += webp_size
            ratio = (1 - webp_size / orig_size) * 100
            print(f"Converted {fname}: {orig_size//1024}KB -> {webp_size//1024}KB (-{ratio:.1f}%)")

print("=== Converting Property Photos ===")
convert_dir(photos_dir, 'public/assets/photos')

print("\n=== Converting Nearby Stays Photos ===")
convert_dir(nearby_dir, 'public/assets/nearby')

print(f"\n==========================================")
print(f"TOTAL ORIGINAL: {total_orig_size / (1024*1024):.2f} MB")
print(f"TOTAL WEBP:     {total_webp_size / (1024*1024):.2f} MB")
reduction = (1 - total_webp_size / total_orig_size) * 100
print(f"OVERALL PAYLOAD REDUCTION: -{reduction:.1f}%")
print(f"==========================================")
