import subprocess
import time
import json
import urllib.request
import os

chrome_bin = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Start static server
server_proc = subprocess.Popen(['python', '-m', 'http.server', '4173', '--directory', 'dist'])
time.sleep(1)

# Start Chrome with remote debugging
chrome_proc = subprocess.Popen([
    chrome_bin,
    '--headless',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=1440,900',
    'http://localhost:4173'
])
time.sleep(2)

try:
    # Query DevTools targets
    with urllib.request.urlopen('http://localhost:9222/json') as resp:
        targets = json.loads(resp.read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        print("Connected to Chrome:", ws_url)
        
    import asyncio
    # Simple python websocket client or run evaluation via node script
except Exception as e:
    print("DevTools query:", e)
finally:
    chrome_proc.terminate()
    server_proc.terminate()
