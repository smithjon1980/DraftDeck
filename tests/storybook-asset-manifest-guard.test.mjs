import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const base = () => ({
 candidate_id:'ep0-p001-v1',source_id:'ep0-p001',source_digest:'sha256:locked-manuscript',
 source_status:'PINNED',story_brief_id:'brief-1',generation_prompt_digest:'sha256:prompt',output_digest:'sha256:image',
 reference_assets:[{id:'reference-layout',digest:'sha256:reference',approved_scope:'COMPOSITION_ONLY'}],
 required_subjects:['business owner'],forbidden_subjects:['cafe','cat'],detected_subjects:['business owner'],
 allowed_palette:['#FFFFFF','#00BCEB','#E30074','#000000'],review_status:'SUBJECT_REVIEWED',human_approval:null
});
function run(m) {
 const dir=mkdtempSync(join(tmpdir(),'boss-guard-'));
 try { const p=join(dir,'manifest.json');writeFileSync(p,JSON.stringify(m));return spawnSync(process.execPath,['scripts/check-storybook-asset-manifest.mjs',p],{encoding:'utf8'}); }
 finally {rmSync(dir,{recursive:true,force:true});}
}
test('valid manifest only structurally passes',()=>assert.equal(run(base()).status,0));
test('cat injection is held',()=>assert.notEqual(run({...base(),detected_subjects:['business owner','cat']}).status,0));
test('cafe injection is held',()=>assert.notEqual(run({...base(),detected_subjects:['business owner','cafe']}).status,0));
test('unapproved unknown character is held',()=>assert.notEqual(run({...base(),detected_subjects:['business owner','rabbit']}).status,0));
test('wrong green brand palette is held',()=>assert.notEqual(run({...base(),allowed_palette:['#008000']}).status,0));
test('missing source digest is held',()=>assert.notEqual(run({...base(),source_digest:''}).status,0));
test('inherited approval on changed digest is held',()=>assert.notEqual(run({...base(),human_approval:{candidate_digest:'old-digest',scope:'composition'}}).status,0));
