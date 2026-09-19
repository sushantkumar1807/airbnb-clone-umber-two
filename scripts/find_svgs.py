import re
css = open('ref_style_0.css', 'r', encoding='utf-8').read()
matches = re.findall(r'url\("data:image/svg\+xml[^"]+"\)', css)
for idx, m in enumerate(matches):
    print(f'Match {idx}: {m}')
