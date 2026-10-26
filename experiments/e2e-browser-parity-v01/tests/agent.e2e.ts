import {test} from '@e2e-dev/web';
import {expect} from 'e2e';
test('agent navigates synthetic editorial fixture',async({app,agent,browser})=>{await app.open('/');await agent.act('Click the Approve release button once');await expect(browser.getByRole('status')).toContainText('DENIED');});
