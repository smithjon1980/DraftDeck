import test from 'node:test';import assert from 'node:assert/strict';import{runRequest}from'../src/swarm.mjs';
const base={title:'Day Zero',source_ref:'test:fixture-only'};
test('instructional PDF takes design and PDF route but cannot claim delivered storage',async()=>{const r=await runRequest({...base,kind:'instructional_pdf'});assert.equal(r.status,'DELIVERY_PENDING_STORAGE');assert.deepEqual(r.steps,['INTAKE','SOURCE','DESIGN','PDF','VERIFY','DELIVER_PENDING']);assert.equal(r.file_url,null)});
test('vector job skips PDF',async()=>{const r=await runRequest({...base,kind:'vector_asset'});assert.deepEqual(r.steps,['INTAKE','SOURCE','VECTOR','VERIFY','DELIVER_PENDING'])});
test('research job skips rendering',async()=>{const r=await runRequest({...base,kind:'research_report'});assert.deepEqual(r.steps,['INTAKE','SOURCE','RESEARCH','VERIFY','DELIVER_PENDING'])});
test('invalid input holds immediately',async()=>{const r=await runRequest({kind:'instructional_pdf',title:'Day Zero'});assert.equal(r.status,'HOLD');assert.deepEqual(r.steps,['INTAKE','HOLD'])});
test('QA failure bounded to one repair then HOLD',async()=>{const r=await runRequest({...base,kind:'instructional_pdf',simulate_failure:true},{max_attempts:1});assert.equal(r.status,'HOLD');assert.deepEqual(r.steps,['INTAKE','SOURCE','DESIGN','PDF','VERIFY','REPAIR','VERIFY','HOLD']);assert.equal(r.attempts,1)});
