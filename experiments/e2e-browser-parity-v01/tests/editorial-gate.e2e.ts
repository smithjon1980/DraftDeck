import { test } from '@e2e-dev/web';
import { expect } from 'e2e';

test('editable headline persists while CAD SVG geometry is intact', async ({app,screen})=>{
  await app.open('/');
  const field=screen.getByRole('textbox',{name:'Headline'});
  await field.fill('HAVE — Human Authority, Verified Execution');
  await screen.getByRole('button',{name:'Save candidate'}).click();
  await expect(screen.getByRole('status')).toContainText('RELEASE STILL ON HOLD');
  await app.open('/');
  await expect(screen.getByRole('textbox',{name:'Headline'})).toHaveValue('HAVE — Human Authority, Verified Execution');
  await expect(screen.locator('svg#cad g#geometry rect#frame')).toHaveAttribute('stroke','#00BCEB');
});

test('unauthenticated UI approval is explicitly denied', async ({app,browser})=>{
  await app.open('/');
  await screen.getByRole('button',{name:'Approve release'}).click();
  await expect(screen.getByRole('status')).toContainText('DENIED');
});
