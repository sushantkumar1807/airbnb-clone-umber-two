import { spawn } from 'node:child_process';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const chromeBin = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

// 1. Start static server
const server = spawn('python', ['-m', 'http.server', '4173', '--directory', 'dist']);
await new Promise(r => setTimeout(r, 1000));

// 2. Start Chrome with remote debugging
const chrome = spawn(chromeBin, [
  '--headless',
  '--disable-gpu',
  '--remote-debugging-port=9222',
  '--window-size=1440,900',
  'http://localhost:4173'
]);
await new Promise(r => setTimeout(r, 2000));

try {
  // Query targets
  const res = await fetch('http://localhost:9222/json');
  const targets = await res.json();
  const pageTarget = targets.find(t => t.type === 'page');
  console.log('Target found:', pageTarget.url);

  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
  await new Promise(res => ws.onopen = res);
  console.log('Connected to CDP');

  let id = 1;
  const send = (method, params = {}) => new Promise((resolve) => {
    const msgId = id++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === msgId) {
        ws.removeEventListener('message', handler);
        resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id: msgId, method, params }));
  });

  await send('Page.enable');
  await send('Runtime.enable');
  await new Promise(r => setTimeout(r, 1500));

  // 1. Click "Show all photos" to open Photo Tour
  console.log('Opening Photo Tour...');
  await send('Runtime.evaluate', {
    expression: `document.getElementById('show-all-photos').click()`
  });
  await new Promise(r => setTimeout(r, 1000));

  // Capture Photo Tour
  const ptShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('preview_photo_tour.png', Buffer.from(ptShot.data, 'base64'));
  console.log('Saved preview_photo_tour.png');

  // 2. Click first photo in Photo Tour to open Lightbox
  console.log('Opening Lightbox...');
  await send('Runtime.evaluate', {
    expression: `
      const ptPhotos = document.querySelectorAll('.pt-photo-grid img');
      if (ptPhotos.length > 0) ptPhotos[0].click();
    `
  });
  await new Promise(r => setTimeout(r, 1000));

  // Capture Lightbox
  const lbShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('preview_lightbox.png', Buffer.from(lbShot.data, 'base64'));
  console.log('Saved preview_lightbox.png');

  ws.close();
} catch (err) {
  console.error('Error during capture:', err);
} finally {
  chrome.kill();
  server.kill();
  console.log('Cleaned up processes');
}
