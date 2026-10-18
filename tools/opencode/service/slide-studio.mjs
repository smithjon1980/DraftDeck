import express from 'express';
import path from 'node:path';
import {mkdir,readFile,writeFile,rename,readdir} from 'node:fs/promises';
import {randomUUID,createHash} from 'node:crypto';
import {z} from 'zod';
const text=n=>z.string().max(n);
const source=z.object({id:z.string().uuid(),name:text(160),reference:text(1000),excerpt:text(60000)}).strict();
const coordinate=z.number().finite().min(0);
const callout=z.object({id:text(64),title:text(80),text:text(180),x:coordinate.max(1650),y:coordinate.max(880),side:z.enum(['left','right']),bendX:coordinate.max(1920),bendY:coordinate.max(1080),targetX:coordinate.max(1920),targetY:coordinate.max(1080)}).strict();
const assembly=z.object({artworkId:z.literal('connector-v1'),callouts:z.array(callout).min(1).max(12).refine(calls=>new Set(calls.map(c=>c.id)).size===calls.length)}).strict();
const slide=z.object({id:z.string().uuid(),title:text(140),lead:text(400),body:text(1800),question:text(250),evidence:text(1000),sourceIds:z.array(z.string().uuid()).max(20),assetId:text(120),variant:z.enum(['A','B','C','D']),assembly:assembly.optional()}).strict();
const schema=z.object({title:text(160).min(1),audience:text(300),bridge1:text(3000),bridge2:text(3000),sources:z.array(source).max(20),slides:z.array(slide).min(1).max(12)}).strict();
const hash=d=>createHash('sha256').update(JSON.stringify(d)).digest('hex');
function validate(d){const v=schema.parse(d);const ids=new Set(v.sources.map(s=>s.id)); if(ids.size!==v.sources.length||new Set(v.slides.map(s=>s.id)).size!==v.slides.length)throw Error('Duplicate IDs'); if(v.slides.some(s=>s.sourceIds.some(id=>!ids.has(id))))throw Error('Unknown source reference');return v;}
export async function createSlideStudio({directory,root}){
 await mkdir(directory,{recursive:true});let queue=Promise.resolve();
 const serialized=fn=>{const p=queue.then(fn);queue=p.catch(()=>{});return p;};
 const file=id=>{if(!/^[0-9a-f-]{36}$/.test(id))throw Error('Invalid project ID');return path.join(directory,id+'.json');};
 const load=async id=>JSON.parse(await readFile(file(id),'utf8'));
 const persist=async d=>{const p=file(d.id),tmp=p+'.tmp';await writeFile(tmp,JSON.stringify(d),{mode:0o600});await rename(tmp,p);return d;};
 const router=express.Router();
 router.use((_req,res,next)=>{res.set('Cache-Control','private, no-store');res.set('X-Content-Type-Options','nosniff');next();});
 router.use('/api',express.json({limit:'2mb'}));
 const handle=fn=>(req,res,next)=>serialized(()=>fn(req,res)).catch(next);
 router.get('/api/templates/connector',handle(async(_req,res)=>res.json(JSON.parse(await readFile(path.join(root,'studio/connector.seed.json'),'utf8')))));
 router.get('/api/projects',handle(async(_req,res)=>{const names=(await readdir(directory)).filter(n=>/^[0-9a-f-]{36}\.json$/.test(n));const rows=await Promise.all(names.map(async n=>{const d=await load(n.slice(0,-5));return {id:d.id,title:d.content.title,revision:d.revision,updatedAt:d.updatedAt,review:d.review};}));res.json(rows.sort((a,b)=>b.updatedAt.localeCompare(a.updatedAt)));}));
 router.get('/api/projects/:id',handle(async(req,res)=>res.json(await load(req.params.id))));
 router.post('/api/projects',handle(async(req,res)=>{if((await readdir(directory)).filter(n=>n.endsWith('.json')).length>=100)return res.status(409).json({error:'Project limit reached. Export a backup and contact the administrator.'});const content=validate(req.body.content);const now=new Date().toISOString();res.status(201).json(await persist({id:randomUUID(),revision:1,updatedAt:now,content,contentHash:hash(content),review:null}));}));
 router.put('/api/projects/:id',handle(async(req,res)=>{const old=await load(req.params.id);if(req.body.revision!==old.revision)return res.status(409).json({error:'This project changed in another tab. Reload before saving.'});const content=validate(req.body.content);const contentHash=hash(content);res.json(await persist({...old,content,contentHash,revision:old.revision+1,updatedAt:new Date().toISOString(),review:contentHash===old.contentHash?old.review:null}));}));
 router.post('/api/projects/:id/review',handle(async(req,res)=>{const d=await load(req.params.id);if(req.body.revision!==d.revision)return res.status(409).json({error:'Reload the current project before recording approval.'});const c=d.content;if(!c.bridge1.trim()||!c.bridge2.trim()||c.slides.some(s=>!s.title.trim()||!s.body.trim()||!s.question.trim()||!s.evidence.trim()||!s.sourceIds.length||s.sourceIds.some(id=>!c.sources.find(x=>x.id===id)?.excerpt.trim())))return res.status(422).json({error:'Complete both story bridges and every slide’s title, body, reflection, evidence, and linked source excerpt before approval.'});if(req.body.confirmed!==true)return res.status(422).json({error:'Explicit review confirmation is required.'});res.json(await persist({...d,revision:d.revision+1,updatedAt:new Date().toISOString(),review:{status:'HUMAN_REVIEW_RECORDED',contentHash:d.contentHash,at:new Date().toISOString(),actor:req.bossIdentity?.email||'authenticated owner',scope:'Selected layouts and supplied copy; source accuracy and export fidelity require review.'}}));}));
 router.use(express.static(path.join(root,'public/studio'),{etag:false,cacheControl:false,fallthrough:false}));
 router.use((err,_req,res,_next)=>{const status=err.code==='ENOENT'?404:err instanceof z.ZodError?422:err.type==='entity.too.large'?413:400;res.status(status).json({error:status===404?'Project not found.':status===413?'Project is too large.':err instanceof z.ZodError?'Invalid project fields or content exceeds the supported limits.':'Could not process the project.'});});
 return router;
}
