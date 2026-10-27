#!/usr/bin/env node
import assert from 'node:assert/strict';
import {inspect,EXACT_PALETTE,SEVEN} from './check_handoff.mjs';
const sha='a'.repeat(64);
const base={
 contract:'BOSS-FIGMA-BRIDGE-V1', candidate_id:'PUBLIC-SYNTHETIC-01',
 mode:'LAYOUT_STUDY', status:'CANDIDATE', profile:'SLIDE_1920X1080',
 source:{id:'SYNTHETIC.P001',revision:'test-only',digest:sha},
 references:[{id:'reference-synthetic',sha256:'b'.repeat(64),scope:'COMPOSITION_ONLY'}],
 tokens:{...EXACT_PALETTE}, layout_variant:SEVEN[0],
 figma:{file_key:null,frame_nodes:[]},
 approvals:{art:null,story:null,human_design_review_ref:null},
 tests:{token_parity:'NOT_TESTED',reference_comparison:'NOT_TESTED',source_copy_parity:'NOT_TESTED'},
 release_authorized:false,paid_generation_requested:false,paid_generation_authorized:false
};
const changed=(f)=>{const d=structuredClone(base);f(d);return d;};
assert.deepEqual(inspect(base),[],'candidate valid without invented approval');
const bad=[
 changed(m=>{m.tokens.magenta='#FF00FF';}),
 changed(m=>{m.source.digest='unknown';}),
 changed(m=>{m.references[0].scope='CONTENT_APPROVED_ALL';}),
 changed(m=>{m.layout_variant='template #8';}),
 changed(m=>{m.release_authorized=true;}),
 changed(m=>{m.paid_generation_requested=true;}),
 changed(m=>{m.mode='COMPOSITION_HANDOFF';m.status='HANDOFF_READY';}),
 changed(m=>{m.mode='WEB_COMPONENT_SPEC';m.profile='WEB_RESPONSIVE';m.status='HANDOFF_READY';})
];
bad.forEach((m,i)=>assert.ok(inspect(m).length, 'must fail bad fixture '+i));
const ready=changed(m=>{
 m.mode='COMPOSITION_HANDOFF';m.status='HANDOFF_READY';
 m.figma={file_key:'private-verified-file-id',frame_nodes:['1:2']};
 m.approvals={art:{status:'APPROVED',sha256:'c'.repeat(64),human_record_ref:'private/approval/art'},
 story:{status:'APPROVED',sha256:'d'.repeat(64),human_record_ref:'private/approval/story'},
 human_design_review_ref:'private/approval/layout'};
 m.tests={token_parity:'PASS',reference_comparison:'PASS',source_copy_parity:'PASS'};
});
assert.deepEqual(inspect(ready),[],'structurally handoff ready is not a release');
assert.ok(inspect(changed(m=>Object.assign(m,ready,{approvals:{...ready.approvals,art:{status:'APPROVED',sha256:'no-hash',human_record_ref:'private/approval/art'}}}))).length);
console.log('PASS: synthetic Figma bridge controls (1 candidate, 1 handoff, 9 negative checks). No visual, identity, or release approval tested.');
