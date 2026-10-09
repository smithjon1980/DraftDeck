import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { chromium } from 'playwright';

const artifactDir = new URL('./artifacts/', import.meta.url);
await mkdir(artifactDir, { recursive: true });
const server = spawn(process.execPath, ['node_modules/vite/bin/vite.js', 'preview', '--host', '127.0.0.1', '--port', '4173', '--strictPort'], { stdio: 'pipe' });
let browser;
const report = [];
try {
  await new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('Preview server did not start')), 15000);
    server.stdout.on('data', data => {
      if (String(data).includes('4173')) { clearTimeout(timer); resolve(); }
    });
    server.on('error', reject);
    server.on('exit', code => { clearTimeout(timer); reject(new Error('Preview server exited: ' + code)); });
  });
  browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  for (const width of [1968, 1440, 768, 390]) {
    await page.setViewportSize({ width, height: 1200 });
    await page.goto('http://127.0.0.1:4173');
    await page.locator('[data-slide-id="02"]').waitFor();
    await page.waitForFunction(() => {
      const viewport = document.querySelector('.slide-viewport');
      const slide = document.querySelector('.slide-canvas');
      return Math.abs(slide.getBoundingClientRect().width - Math.min(viewport.clientWidth, 1920)) < 1;
    });
    const result = await page.evaluate(() => {
      const slides = [...document.querySelectorAll('[data-document-role="page"]')];
      const failures = [];
      for (const slide of slides) {
        const css = getComputedStyle(slide);
        const bounds = slide.getBoundingClientRect();
        if (css.width !== '1920px' || css.height !== '1080px') failures.push('Logical dimensions');
        if (css.backgroundColor !== 'rgb(255, 255, 255)' || css.color !== 'rgb(0, 0, 0)') failures.push('Canvas colors');
        if (slide.querySelector('[data-document-role="page"]')) failures.push('Nested page');
        if (slide.querySelector('canvas, svg, iframe')) failures.push('Non-native slide layer');
        if (Math.abs(bounds.width / bounds.height - 16 / 9) > 0.001) failures.push('Aspect ratio');
        for (const el of slide.querySelectorAll('*')) {
          const style = getComputedStyle(el);
          if (style.boxShadow !== 'none' || style.borderRadius !== '0px') failures.push('Shadow/rounding');
          for (const side of ['Top', 'Bottom', 'Left', 'Right']) {
            if (parseFloat(style['border' + side + 'Width']) > 1) failures.push('Thick border');
          }
          if (el.matches('p, h1, h2, h3, span')) {
            if (style.color !== 'rgb(0, 0, 0)') failures.push('Text color');
            const rect = el.getBoundingClientRect();
            if (rect.left < bounds.left - 1 || rect.top < bounds.top - 1 || rect.right > bounds.right + 1 || rect.bottom > bounds.bottom + 1) failures.push('Text outside canvas');
            if (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) failures.push('Text overflow');
          }
        }
      }
      return {
        ids: slides.map(slide => slide.dataset.slideId),
        failures: [...new Set(failures)],
        documentOverflow: document.documentElement.scrollWidth > innerWidth,
        scale: getComputedStyle(slides[0]).transform,
      };
    });
    assert.deepEqual(result.ids, ['01', '02', '06']);
    assert.deepEqual(result.failures, []);
    assert.equal(result.documentOverflow, false);
    await page.getByLabel('View', { exact: true }).selectOption('02');
    assert.equal(await page.locator('[data-document-role="page"]').count(), 1);
    await page.getByRole('heading', { name: "The Problem Isn't Networking", exact: true }).waitFor();
    for (const text of ['Recruit', 'Sell', 'Expand the network', 'Learn', 'Build', 'Verify, Deploy, Support', 'Growth through distribution', 'Value through delivered work']) {
      assert.equal(await page.getByText(text, { exact: true }).count(), 1);
    }
    await page.locator('[data-slide-id="02"]').screenshot({ path: new URL('slide-02-' + width + '.png', artifactDir).pathname });
    report.push({ viewportWidth: width, ...result, passed: true });
  }
  assert.deepEqual(errors, []);
  await page.setViewportSize({ width: 1968, height: 1200 });
  await page.getByLabel('View', { exact: true }).selectOption('all');
  for (const id of ['01', '06']) {
    await page.locator('[data-slide-id="' + id + '"]').screenshot({ path: new URL('slide-' + id + '-1968.png', artifactDir).pathname });
  }
  await writeFile(new URL('report.json', artifactDir), JSON.stringify({ status: 'geometry-checks-passed', creativeApproval: 'UNKNOWN', logoVerified: false, report }, null, 2));
  console.log(JSON.stringify(report, null, 2));
  // Allow visual review through text-only GitHub log readers as well as
  // the downloadable artifact. These are diagnostic screenshots, never
  // source slides or Canva import substitutes.
  const reviewImage = await readFile(new URL('slide-02-1968.png', artifactDir));
  console.log('BOSS_REVIEW_PNG_BASE64=' + reviewImage.toString('base64'));
} finally {
  await browser?.close();
  server.kill('SIGTERM');
}
