import zipfile
import os

# Ensure execution from project root
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(repo_root)

zip_name = 'playpower_airbnb_clone_submission.zip'

# Files and directories to include in clean submission package
includes = [
    'src',
    'public',
    'dist',
    '.agents',
    'scripts',
    'extra',
    'index.html',
    'package.json',
    'package-lock.json',
    'vite.config.js',
    'README.md',
    'architecture_diagram.png',
    'architecture_diagram.svg',
    'architecture_design.md',
    'prompts_sequence.md',
    'Playpower Labs Assignment_ Airbnb-Clone App.md'
]

print(f"Creating {zip_name}...")
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for item in includes:
        if os.path.isfile(item):
            zf.write(item, item)
            print(f"Added file: {item}")
        elif os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, '.')
                    zf.write(full_path, rel_path)
            print(f"Added dir: {item}")

size_mb = os.path.getsize(zip_name) / (1024 * 1024)
print(f"Successfully created {zip_name} ({size_mb:.2f} MB)")
