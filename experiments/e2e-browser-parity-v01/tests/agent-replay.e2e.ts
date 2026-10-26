import { test } from '@e2e-dev/web';
import { expect } from 'e2e';
test('synthetic approval remains denied after agent navigation', async ({app,agent,screen}) => {
  await app.open('/');
  await agent.act('Find and click the button labeled Approve release once.');
  await expect(screen.getByRole('status')).toContainText('DENIED');
});
