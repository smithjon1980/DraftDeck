import express from 'express';
import {randomBytes,createHash,timingSafeEqual} from 'node:crypto';
import {mkdir,readFile,writeFile,rename} from 'node:fs/promises';
import path from 'node:path';
const random=()=>randomBytes(32).toString('base64url');
const eq=(a,b)=>{const x=Buffer.from(a||''),y=Buffer.from(b||'');return x.length===y.length&&timingSafeEqual(x,y)};
const readCookie=(req,name)=>{const a=String(req.headers.cookie||'').split(';').map(x=>x.trim()).filter(x=>x.startsWith(name+'='));return a.length===1?a[0].slice(name.length+1):''};
const cookie=(name,v,seconds)=>`${name}=${v}; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=${seconds}`;
const clean=html=>html.replace(/<!-- BOSS_PILOT_SAVE_START -->[\s\S]*?<!-- BOSS_PILOT_SAVE_END -->/g,'');
const digest=b=>'"'+createHash('sha256').update(b).digest('hex')+'"';
export async function createPilot({origin,issuer,secret,allowedEmail,directory,fetcher=fetch,now=Date.now}){
 if(!secret||secret.length<32||!allowedEmail)throw Error('Pilot requires bridge secret and explicit owner email');
 if(!/^https:\/\//.test(issuer)||new URL(issuer).origin!==issuer)throw Error('Invalid issuer');
 if(origin&&(!/^https:\/\//.test(origin)||new URL(origin).origin!==origin))throw Error('Invalid pilot origin');
 await mkdir(directory,{recursive:true});const file=path.join(directory,'BOSS_Deep_Dive_20_Slides.html');
 let tail=Promise.resolve();const serialized=fn=>{const p=tail.then(fn);tail=p.catch(()=>{});return p};
 const current=async()=>{try{const bytes=await readFile(file);return {bytes,etag:digest(bytes)}}catch(e){if(e.code==='ENOENT')return null;throw e}};
 const sessions=new Map(),router=express.Router();
 const prune=()=>{for(const[k,v]of sessions)if(v.expires<=now())sessions.delete(k)};
 function identity(req){const s=sessions.get(readCookie(req,'__Host-boss_aion_session'));return s&&s.expires>now()?s.identity:null}
 function guard(req,res,next){
  const who=identity(req);if(!who)return req.method==='GET'&&req.headers.accept?.includes('text/html')?res.redirect(303,'/auth/start'):res.sendStatus(401);
  if(!['GET','HEAD','OPTIONS'].includes(req.method)&&req.headers.origin!==origin)return res.sendStatus(403);
  req.pilotIdentity=who;next();
 }
 router.use((_req,res,next)=>{res.set('Cache-Control','private, no-store').set('Referrer-Policy','no-referrer').set('X-Content-Type-Options','nosniff');next()});
 router.get('/auth/start',(req,res)=>{
  if(!origin)return res.status(503).send('Pilot address is being configured.');
  const state=random();res.append('Set-Cookie',cookie('__Host-boss_aion_tx',state,300));
  const u=new URL('/tools/aionui/connect',issuer);u.searchParams.set('state',state);res.redirect(303,u.href);
 });
 router.get('/auth/callback',async(req,res)=>{
  const state=readCookie(req,'__Host-boss_aion_tx');res.append('Set-Cookie',cookie('__Host-boss_aion_tx','',0));
  if(!origin||!state||typeof req.query.state!=='string'||!eq(state,req.query.state)||typeof req.query.code!=='string'||!/^[A-Za-z0-9_-]{43}$/.test(req.query.code))return res.sendStatus(400);
  try{
   const r=await fetcher(issuer+'/internal/aionui/exchange',{method:'POST',headers:{Authorization:'Bearer '+secret,'Content-Type':'application/json'},body:JSON.stringify({code:req.query.code,state}),signal:AbortSignal.timeout(12000)});
   if(!r.ok)return res.sendStatus(401);const {identity:who}=await r.json();
   if(who?.email!==allowedEmail||typeof who.subject!=='string'||!who.subject)return res.sendStatus(403);
   prune();if(sessions.size>=500)return res.sendStatus(429);const key=random();sessions.set(key,{identity:who,expires:now()+8*3600000});
   res.append('Set-Cookie',cookie('__Host-boss_aion_session',key,8*3600));res.redirect(303,'/pilot');
  }catch{res.status(503).send('Sign-in handoff unavailable. Please start again.')}
 });
 router.post('/auth/logout',guard,(req,res)=>{sessions.delete(readCookie(req,'__Host-boss_aion_session'));res.append('Set-Cookie',cookie('__Host-boss_aion_session','',0));res.redirect(303,'/auth/start')});
 const machine=(req,res,next)=>eq(req.headers.authorization,'Bearer '+secret)?next():res.sendStatus(401);
 router.post('/internal/seed-deck',machine,express.text({type:'text/html',limit:'16mb'}),(req,res,next)=>serialized(async()=>{
  if(typeof req.body!=='string'||req.body.length<100||!req.body.includes('data-document-role="page"'))return res.sendStatus(422);
  const bytes=Buffer.from(clean(req.body)),old=await current();if(old)return digest(bytes)===old.etag?res.json({status:'ALREADY_PRESENT',etag:old.etag}):res.status(409).json({error:'Existing deck retained'});
  const temp=file+'.seed';await writeFile(temp,bytes,{mode:0o600});await rename(temp,file);res.status(201).json({status:'SEEDED',etag:digest(bytes)});
 }).catch(next));
 router.get('/pilot',guard,(_req,res)=>res.type('html').send(`<!doctype html><html lang="en"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BOSS AionUi pilot</title><style>body{font:18px Arial;background:white;color:black;max-width:850px;margin:40px auto;padding:24px;border-top:2px solid black}h1{font:48px Georgia}a{color:black;display:block;border-bottom:1px solid black;padding:22px 0}p{line-height:1.6}button{font:inherit;background:white;border:1px solid black;padding:12px}</style><p>Bioscillate Operating System by Seven</p><h1>Your private workspace</h1><a href="/deck">Open the 20-slide deck · edit text and save to workspace</a><a href="/">Open AionUi · agents, files and previews</a><a href="/pilot/opencode-status">Check the existing OpenCode connection</a><p>Deck saves persist on this pilot’s volume. Text editing is available; arbitrary slide-layout editing is not established.</p><form method="post" action="/auth/logout"><button>Sign out of this pilot</button></form></html>`));
 router.get('/pilot/opencode-status',guard,async(_req,res)=>{try{const r=await fetcher(issuer+'/internal/aionui/opencode-status',{headers:{Authorization:'Bearer '+secret},signal:AbortSignal.timeout(15000)});res.status(r.status).type('json').send(await r.text())}catch{res.status(503).json({error:'Status unavailable'})}});
 router.get('/pilot/deck',guard,async(_req,res,next)=>{try{const d=await current();if(!d)return res.sendStatus(404);res.set('ETag',d.etag).type('html').send(d.bytes)}catch(e){next(e)}});
 router.put('/pilot/deck',guard,express.text({type:'text/html',limit:'16mb'}),(req,res,next)=>serialized(async()=>{
  const d=await current();if(!d)return res.sendStatus(404);if(req.headers['if-match']!==d.etag)return res.status(409).json({error:'Deck changed. Reload before saving.'});
  if(typeof req.body!=='string'||req.body.length<100||!req.body.includes('data-document-role="page"'))return res.sendStatus(422);
  const bytes=Buffer.from(clean(req.body)),temp=file+'.saving';await writeFile(temp,bytes,{mode:0o600});await rename(temp,file);res.set('ETag',digest(bytes)).json({status:'SAVED'});
 }).catch(next));
 router.get('/deck',guard,async(_req,res,next)=>{try{
  const d=await current();if(!d)return res.status(404).send('The deck is being installed.');
  const script=`<!-- BOSS_PILOT_SAVE_START --><script>(()=>{let revision=${JSON.stringify(d.etag)};const button=document.getElementById('save');if(!button)return;button.textContent='Save to workspace';const status=document.createElement('span');status.setAttribute('role','status');button.after(status);button.onclick=async()=>{button.disabled=true;status.textContent=' Saving…';try{const html='<!doctype html>'+document.documentElement.outerHTML;const r=await fetch('/pilot/deck',{method:'PUT',headers:{'Content-Type':'text/html','If-Match':revision},body:html});if(!r.ok)throw Error(r.status===409?'Another save changed this deck. Reload first.':'Save failed ('+r.status+')');revision=r.headers.get('ETag');status.textContent=' Saved to workspace';}catch(e){status.textContent=' '+e.message;}finally{button.disabled=false}}})()</script><!-- BOSS_PILOT_SAVE_END -->`;
  res.type('html').send(clean(d.bytes.toString()).replace('</body>',script+'</body>'));
 }catch(e){next(e)}});
 return {router,guard,identity};
}
