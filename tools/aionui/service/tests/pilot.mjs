import test from 'node:test';import assert from 'node:assert/strict';import express from 'express';
import {mkdtemp,rm} from 'node:fs/promises';import os from 'node:os';import path from 'node:path';
import {createPilot} from '../pilot.mjs';import {createAionuiBroker} from '../../../opencode/service/aionui-broker.mjs';
const secret='a'.repeat(43),origin='https://pilot.example',issuer='https://boss.example',owner='owner@example.com';
async function listen(app){const server=app.listen(0,'127.0.0.1');await new Promise(r=>server.once('listening',r));return{url:'http://127.0.0.1:'+server.address().port,close:()=>new Promise(r=>server.close(r))}}
const cookie=r=>{const all=r.headers.getSetCookie();return(all.find(x=>x.startsWith('__Host-boss_aion_session='))||all[0]).split(';')[0]};
test('Google handoff is state-bound, one-use and owner-only; machine routes reject missing credentials',async()=>{
 let now=1000;const b=express();b.use(createAionuiBroker({env:{BOSS_AIONUI_BRIDGE_SECRET:secret,BOSS_AIONUI_ORIGIN:origin},google:{authenticate:req=>req.headers['x-test-google']==='yes'?{email:owner,subject:'verified-subject'}:null},now:()=>now,opencodeStatus:async()=>({healthy:true})}));const boss=await listen(b);
 try{
  const state='s'.repeat(43);let r=await fetch(boss.url+'/tools/aionui/connect?state='+state,{redirect:'manual'});assert.equal(r.status,303);assert.ok(r.headers.get('location').startsWith('/login?return='));
  r=await fetch(boss.url+'/tools/aionui/connect?state='+state,{headers:{'x-test-google':'yes'},redirect:'manual'});assert.equal(new URL(r.headers.get('location')).origin,origin);const code=new URL(r.headers.get('location')).searchParams.get('code');
  const exchange=()=>fetch(boss.url+'/internal/aionui/exchange',{method:'POST',headers:{Authorization:'Bearer '+secret,'Content-Type':'application/json'},body:JSON.stringify({state,code})});
  assert.equal((await fetch(boss.url+'/internal/aionui/exchange',{method:'POST'})).status,401);
  assert.equal((await exchange()).status,200);assert.equal((await exchange()).status,401);
  r=await fetch(boss.url+'/tools/aionui/connect?state='+state,{headers:{'x-test-google':'yes'},redirect:'manual'});const expiredCode=new URL(r.headers.get('location')).searchParams.get('code');now+=61000;
  assert.equal((await fetch(boss.url+'/internal/aionui/exchange',{method:'POST',headers:{Authorization:'Bearer '+secret,'Content-Type':'application/json'},body:JSON.stringify({state,code:expiredCode})})).status,401);
 }finally{await boss.close()}
});
test('Pilot rejects unauthenticated and cross-origin saves, detects stale revisions, and retains edits across restart',async()=>{
 const directory=await mkdtemp(path.join(os.tmpdir(),'boss-pilot-'));let handle;
 async function start(email=owner){const p=await createPilot({origin,issuer,secret,allowedEmail:owner,directory,fetcher:async()=>Response.json({identity:{email,subject:'verified-subject'}})});const app=express();app.use(p.router);app.get('/private',p.guard,(_req,res)=>res.json({ok:true}));return listen(app)}
 async function login(h){let r=await fetch(h.url+'/auth/start',{redirect:'manual'});const tx=cookie(r),state=new URL(r.headers.get('location')).searchParams.get('state');r=await fetch(h.url+'/auth/callback?state='+state+'&code='+'c'.repeat(43),{headers:{Cookie:tx},redirect:'manual'});assert.equal(r.status,303);return cookie(r)}
 try{
  handle=await start();assert.equal((await fetch(handle.url+'/private')).status,401);
  assert.equal((await fetch(handle.url+'/auth/callback?state=wrong&code='+'c'.repeat(43))).status,400);
  const auth=await login(handle),html='<!doctype html><html><body><section data-document-role="page"><h1>Original source title retained here</h1></section></body></html>';
  assert.equal((await fetch(handle.url+'/internal/seed-deck',{method:'POST',body:html,headers:{'Content-Type':'text/html'}})).status,401);
  let r=await fetch(handle.url+'/internal/seed-deck',{method:'POST',body:html,headers:{Authorization:'Bearer '+secret,'Content-Type':'text/html'}});assert.equal(r.status,201);
  r=await fetch(handle.url+'/pilot/deck',{headers:{Cookie:auth}});const etag=r.headers.get('ETag');assert.ok((await r.text()).includes('Original source title'));
  const save=(tag,orig=origin)=>fetch(handle.url+'/pilot/deck',{method:'PUT',headers:{Cookie:auth,Origin:orig,'Content-Type':'text/html','If-Match':tag},body:html.replace('Original','Edited')});
  assert.equal((await save(etag,'https://other.example')).status,403);assert.equal((await save(etag)).status,200);assert.equal((await save(etag)).status,409);
  await handle.close();handle=await start();assert.equal((await fetch(handle.url+'/pilot/deck',{headers:{Cookie:auth}})).status,401);const auth2=await login(handle);
  assert.ok((await(await fetch(handle.url+'/pilot/deck',{headers:{Cookie:auth2}})).text()).includes('Edited source title'));
  await handle.close();handle=await start('other@example.com');let s=await fetch(handle.url+'/auth/start',{redirect:'manual'});const tx=cookie(s),state=new URL(s.headers.get('location')).searchParams.get('state');assert.equal((await fetch(handle.url+'/auth/callback?state='+state+'&code='+'c'.repeat(43),{headers:{Cookie:tx},redirect:'manual'})).status,403);
 }finally{if(handle)await handle.close();await rm(directory,{recursive:true,force:true})}
});
