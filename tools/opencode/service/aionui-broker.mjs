import express from 'express';
import {randomBytes,timingSafeEqual} from 'node:crypto';
export function createAionuiBroker({google,env=process.env,now=Date.now,opencodeStatus}){
 const router=express.Router(),codes=new Map();
 const secret=env.BOSS_AIONUI_BRIDGE_SECRET,origin=env.BOSS_AIONUI_ORIGIN;
 const enabled=typeof secret==='string'&&secret.length>=32&&typeof origin==='string'&&/^https:\/\//.test(origin)&&new URL(origin).origin===origin;
 const equal=(a,b)=>{const x=Buffer.from(a||''),y=Buffer.from(b||'');return x.length===y.length&&timingSafeEqual(x,y)};
 const machine=(req,res,next)=>enabled&&equal(req.headers.authorization,'Bearer '+secret)?next():res.sendStatus(401);
 router.use(['/tools/aionui/connect','/internal/aionui'],(_req,res,next)=>{res.set('Cache-Control','private, no-store').set('Referrer-Policy','no-referrer');next()});
 router.get('/tools/aionui/connect',(req,res)=>{
  if(!enabled)return res.status(503).send('The private pilot is awaiting its address.');
  const state=req.query.state;if(typeof state!=='string'||!/^[A-Za-z0-9_-]{43}$/.test(state))return res.sendStatus(400);
  const user=google.authenticate(req);
  if(!user)return res.redirect(303,'/login?return='+encodeURIComponent('/tools/aionui/connect?state='+state));
  for(const [key,c]of codes)if(c.expires<=now())codes.delete(key);
  if(codes.size>=500)return res.sendStatus(429);
  const code=randomBytes(32).toString('base64url');codes.set(code,{state,user,expires:now()+60000});
  const to=new URL('/auth/callback',origin);to.searchParams.set('code',code);to.searchParams.set('state',state);res.redirect(303,to.href);
 });
 router.post('/internal/aionui/exchange',machine,express.json({limit:'2kb'}),(req,res)=>{
  const code=req.body?.code,state=req.body?.state;if(typeof code!=='string'||typeof state!=='string')return res.sendStatus(400);
  const entry=codes.get(code);codes.delete(code);
  if(!entry||entry.expires<=now()||!equal(state,entry.state))return res.sendStatus(401);
  res.json({identity:entry.user});
 });
 router.get('/internal/aionui/opencode-status',machine,async(_req,res)=>{
  try{res.json(await opencodeStatus())}catch{res.status(503).json({error:'OpenCode status unavailable'})}
 });
 return router;
}
