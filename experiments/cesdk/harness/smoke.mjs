import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';

const output = 'evidence';
await mkdir(output, { recursive: true });
const server = spawn('npm', ['run', 'dev', '--', '--port', '4177', '--strictPort'], { stdio: ['ignore', 'pipe', 'pipe'] });
let serverOutput = '';
server.stdout.on('data', (chunk) => { serverOutput += chunk.toString(); });
server.stderr.on('data', (chunk) => { serverOutput += chunk.toString(); });
let browser;
let result = { criterion: 'C01', status: 'BLOCKED', version: null, errors: [], console: [], url: 'http://127.0.0.1:4177', timestamp: new Date().toISOString() };
try {
  let ready = false;
  for (let i = 0; i < 40; i++) {
    if (server.exitCode !== null) throw new Error('Vite server exited: ' + serverOutput);
    try { const response = await fetch(result.url); if (response.ok) { ready = true; break; } } catch {}
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  if (!ready) throw new Error('Vite server unavailable: ' + serverOutput);
  browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  page.on('pageerror', error => result.errors.push(String(error)));
  page.on('console', message => result.console.push(message.type() + ': ' + message.text()));
  await page.goto(result.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForFunction(() => {
    const s = document.querySelector('#status')?.textContent || '';
    return s.includes('initialized') || s.startsWith('BLOCKED:');
  }, { timeout: 90000 });
  result.statusText = await page.locator('#status').textContent();
  result.version = await page.evaluate(() => window.bossCesdkTest?.version || null);
  result.status = result.statusText?.includes('initialized') && result.version ? 'PASS' : 'FAIL';
  await page.screenshot({ path: output + '/cesdk-c01.png', fullPage: true });
} catch (error) {
  result.errors.push(String(error));
  result.status = 'FAIL';
} finally {
  await writeFile(output + '/cesdk-c01.json', JSON.stringify(result, null, 2) + '\n');
  await browser?.close();
  server.kill('SIGTERM');
}
console.log(JSON.stringify(result, null, 2));
if (result.status !== 'PASS') process.exitCode = 1;
