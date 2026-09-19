import subprocess
import time
import os

chrome_bin = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Build project first
subprocess.run(['npm', 'run', 'build'], check=True, shell=True)

# Start static server
server_proc = subprocess.Popen(['python', '-m', 'http.server', '4173', '--directory', 'dist'])
time.sleep(1.5)

try:
    # 1. Listing Page
    p1 = os.path.abspath('preview_listing.png')
    subprocess.run([
        chrome_bin,
        '--headless',
        '--disable-gpu',
        '--window-size=1440,900',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=3000',
        f'--screenshot={p1}',
        'http://localhost:4173'
    ], check=True)
    print("Saved preview_listing.png")

finally:
    server_proc.terminate()
    print("Server terminated")
