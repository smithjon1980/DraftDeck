import { test } from '@e2e-dev/web';
import { expect } from 'e2e';
test('headline persists and CAD SVG viewBox remains intact', async ({app,screen})=>{
 await app.open('/');
 await screen.getByRole('textbox',{name:'Headline'}).fill('HAVE — Human Authority, Verified Execution');
 await screen.getByRole('button',{name:'Save candidate'}).click();
 await expect(screen.getByRole('status')).toContainText('RELEASE STILL ON HOLD');
 await app.open('/');
 await expect(screen.getByRole('textbox',{name:'Headline'})).toHaveValue('HAVE — Human Authority, Verified Execution');
 await expect(screen.getByRole('img',{name:'Editable CAD geometry'})).toHaveAttribute('viewBox','0 0 240 80');
});
test('unauthenticated UI approval is explicitly denied',async ({app,screen})=>{
 await app.open('/');
 await screen.getByRole('button',{name:'Approve release'}).click();
 await expect(screen.getByRole('status')).toContainText('DENIED');
});
