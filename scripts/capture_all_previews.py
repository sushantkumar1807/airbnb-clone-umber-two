import subprocess
import time
import os

chrome_bin = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Start server
server_proc = subprocess.Popen(['python', '-m', 'http.server', '4173', '--directory', 'dist'])
time.sleep(1.5)

try:
    listing_png = os.path.abspath('preview_listing.png')
    print("Capturing listing page to:", listing_png)
    subprocess.run([
        chrome_bin,
        '--headless',
        '--disable-gpu',
        '--window-size=1440,900',
        f'--screenshot={listing_png}',
        'http://localhost:4173'
    ], check=True)
    print("Listing screenshot saved!")
    
finally:
    server_proc.terminate()
    print("Server stopped")
