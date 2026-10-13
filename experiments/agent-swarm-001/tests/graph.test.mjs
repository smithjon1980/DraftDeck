import test from 'node:test';
import assert from 'node:assert/strict';
import {run} from '../src/graph.mjs';
test('missing source must HOLD before specialists', async()=>{
 const r=await run({id:"x",artifact_type:"pdf"});
 assert.equal(r.decision,"HOLD");
 assert.equal(r.history.length,1);
});
test('valid request with missing proof must HOLD', async()=>{
 const r=await run({id:"x",artifact_type:"pdf",source_ref:"L0",required_text:["Actual text"],observed_text:["Actual text"]});
 assert.equal(r.decision,"HOLD");assert.equal(r.pdf_report.has_evidence,false);
});
test('claimed PDF plus verified story still requires human review',async()=>{
 const r=await run({id:"x",artifact_type:"pdf",source_ref:"L0",required_text:["Actual text"],observed_text:["Actual text"],pdf_path_verified:true,story_asset_verified:true},["sha256:fixture-evidence"]);
 assert.equal(r.decision,"REVIEW_REQUIRED");assert.notEqual(r.decision,"RELEASED");
});
test('text mismatch must HOLD even with other evidence',async()=>{
 const r=await run({id:"x",artifact_type:"pdf",source_ref:"L0",required_text:["Exact source"],observed_text:["Wrong"],pdf_path_verified:true,story_asset_verified:true},["sha256:fixture-evidence"]);
 assert.equal(r.decision,"HOLD");assert.deepEqual(r.pdf_report.missing,["Exact source"]);
});
