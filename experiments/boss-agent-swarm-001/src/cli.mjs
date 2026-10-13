import {runRequest} from './swarm.mjs';
const request={kind:'instructional_pdf',title:'Day Zero Overview 01',source_ref:'authenticated:test-fixture-only'};
const result=await runRequest(request);
console.log(JSON.stringify({run_id:result.run_id,status:result.status,steps:result.steps,file_url:result.file_url||null},null,2));
