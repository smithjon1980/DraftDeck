import { test } from '@e2e-dev/web';
import { expect } from 'e2e';

test('editable headline persists while CAD SVG geometry is intact', async ({app,browser})=>{
  await app.open('/');
  const field=browser.getByRole('textbox',{name:'Headline'});
  await field.fill('HAVE — Human Authority, Verified Execution');
  await browser.getByRole('button',{name:'Save candidate'}).click();
  await expect(browser.getByRole('status')).toContainText('RELEASE STILL ON HOLD');
  await app.open('/');
  await expect(browser.getByRole('textbox',{name:'Headline'})).toHaveValue('HAVE — Human Authority, Verified Execution');
  await expect(browser.locator('svg#cad g#geometry rect#frame')).toHaveAttribute('stroke','#00BCEB');
});

test('unauthenticated UI approval is explicitly denied', async ({app,browser})=>{
  await app.open('/');
  await browser.getByRole('button',{name:'Approve release'}).click();
  await expect(browser.getByRole('status')).toContainText('DENIED');
});
