import express from 'express';import http from 'node:http';import httpProxy from 'http-proxy';
import {spawn,spawnSync} from 'node:child_process';import {randomBytes} from 'node:crypto';
import {mkdir,readFile,writeFile} from 'node:fs/promises';import path from 'node:path';
import {createPilot} from './pilot.mjs';
const origin=process.env.PUBLIC_ORIGIN||(process.env.RAILWAY_PUBLIC_DOMAIN?'https://'+process.env.RAILWAY_PUBLIC_DOMAIN:undefined);
const issuer=process.env.BOSS_AUTH_ISSUER,secret=process.env.BOSS_AIONUI_BRIDGE_SECRET,owner=process.env.GOOGLE_ALLOWED_EMAIL;
const state=process.env.AIONUI_DATA_DIR||'/data/state',workspace=process.env.BOSS_AIONUI_WORKSPACE||'/data/workspace';
const binary=process.env.AIONUI_BACKEND_BIN||'/usr/local/bin/aioncore',backendPort=Number(process.env.AIONUI_BACKEND_PORT||25808),port=Number(process.env.PORT||8080);
await mkdir(state,{recursive:true});await mkdir(workspace,{recursive:true});
const credentialFile=path.join(state,'.pilot-backend-password');let password;
try{password=(await readFile(credentialFile,'utf8')).trim()}catch(e){if(e.code!=='ENOENT')throw e;password=randomBytes(36).toString('base64url');await writeFile(credentialFile,password+'\n',{mode:0o600,flag:'wx'})}
const childEnv={...process.env};for(const key of ['BOSS_AIONUI_BRIDGE_SECRET','GOOGLE_CLIENT_SECRET','GOOGLE_CLIENT_ID','OPENCODE_SERVER_PASSWORD','BOSS_MCP_TOKEN'])delete childEnv[key];
const logDir=process.env.AIONUI_LOG_DIR||'/data/logs';
childEnv.AIONUI_WORK_DIR=workspace;childEnv.AIONUI_CACHE_DIR=process.env.XDG_CACHE_HOME||'/data/cache';childEnv.AIONUI_LOG_DIR=logDir;
const setup=spawnSync(binary,['--data-dir',state,'user','set-password','--password-stdin'],{input:password+'\n',env:childEnv,encoding:'utf8'});
if(setup.status!==0)throw Error('Backend account bootstrap failed');
const child=spawn(binary,['--host','127.0.0.1','--port',String(backendPort),'--data-dir',state,'--work-dir',workspace,'--log-dir',logDir,'--log-level','warn'],{env:childEnv,stdio:['ignore','ignore','inherit']});
const backend='http://127.0.0.1:'+backendPort;let backendToken='',expires=0,pending;
async function token(){if(backendToken&&expires>Date.now())return backendToken;if(pending)return pending;
 pending=(async()=>{const r=await fetch(backend+'/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:'admin',password}),signal:AbortSignal.timeout(10000)});if(!r.ok)throw Error('Backend authentication unavailable');const d=await r.json();const t=d.token||d.data?.token;if(!t)throw Error('Backend token unavailable');backendToken=t;expires=Date.now()+15*60000;return t})();try{return await pending}finally{pending=null}}
const pilot=await createPilot({origin,issuer,secret,allowedEmail:owner,directory:workspace});const app=express();app.disable('x-powered-by');
app.use((req,res,next)=>{if(req.path==='/health')return next();if(origin&&req.headers.host!==new URL(origin).host)return res.sendStatus(403);if(req.headers.origin&&req.headers.origin!==origin)return res.sendStatus(403);next()});
app.get('/health',async(_req,res)=>{try{const r=await fetch(backend+'/health',{signal:AbortSignal.timeout(2000)});res.status(r.ok?200:503).json({healthy:r.ok})}catch{res.status(503).json({healthy:false})}});
app.use(pilot.router);
const proxy=httpProxy.createProxyServer({target:backend,ws:true});proxy.on('error',(_e,_req,res)=>{if(typeof res.writeHead==='function'&&!res.headersSent)res.writeHead(502);res.end()});
app.post('/login',pilot.guard,(_req,res)=>res.sendStatus(405));app.post('/logout',pilot.guard,(_req,res)=>res.redirect(307,'/auth/logout'));
app.use('/api',pilot.guard,async(req,res)=>{try{const t=await token();delete req.headers.origin;delete req.headers.cookie;req.url='/api'+req.url;proxy.web(req,res,{headers:{Authorization:'Bearer '+t}})}catch{res.sendStatus(503)}});
const renderer=process.env.AIONUI_RENDERER_DIR||'/app/renderer';
app.use(pilot.guard,express.static(renderer,{index:false}));app.get(/.*/,pilot.guard,(_req,res)=>res.sendFile(path.join(renderer,'index.html')));
app.use((err,_req,res,_next)=>{if(!res.headersSent)res.status(err.status===413?413:500).json({error:'Pilot request failed'})});
const listener=http.createServer(app);listener.on('upgrade',async(req,socket,head)=>{
 if(!pilot.identity(req)||req.headers.origin!==origin||!origin||req.headers.host!==new URL(origin).host){socket.end('HTTP/1.1 401 Unauthorized\r\nConnection: close\r\n\r\n');return}
 try{const t=await token();delete req.headers.cookie;delete req.headers.origin;proxy.ws(req,socket,head,{headers:{Authorization:'Bearer '+t}})}catch{socket.destroy()}
});listener.listen(port,'0.0.0.0',()=>console.log('BOSS AionUi pilot listener ready'));
child.on('error',()=>{console.error('AionCore could not start');listener.close();process.exitCode=1});child.on('exit',code=>{listener.close();process.exitCode=code||0});
for(const s of ['SIGTERM','SIGINT'])process.on(s,()=>{child.kill(s);listener.close(()=>process.exit(0))});
