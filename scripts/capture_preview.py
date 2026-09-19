import subprocess
import time
import os
import urllib.request

chrome_paths = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe')
]

chrome_bin = None
for p in chrome_paths:
    if os.path.exists(p):
        chrome_bin = p
        break

print("Using Chrome:", chrome_bin)

# Start a local static server on port 4173 serving dist/
server_proc = subprocess.Popen(['python', '-m', 'http.server', '4173', '--directory', 'dist'])
time.sleep(1)

try:
    # 1. Capture primary listing page
    print("Capturing listing page...")
    subprocess.run([
        chrome_bin,
        '--headless',
        '--disable-gpu',
        '--window-size=1440,900',
        '--screenshot=preview_listing.png',
        'http://localhost:4173'
    ], check=True)
    print("Saved preview_listing.png")

finally:
    server_proc.terminate()
    print("Server terminated")
