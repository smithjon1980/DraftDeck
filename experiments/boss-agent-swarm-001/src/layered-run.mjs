import { Annotation, StateGraph, START, END } from '@langchain/langgraph';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { createHash } from 'node:crypto';
import { buildPdf } from './pdf-worker.mjs';

const hash=v=>createHash('sha256').update(v).digest('hex');
const State=Annotation.Root({runId:Annotation(),root:Annotation(),status:Annotation(),scene:Annotation(),outputs:Annotation(),qa:Annotation(),events:Annotation()});
const add=(s,event)=>[...(s.events||[]),event];

async function intake(s){
 if(!/^[a-z0-9-]{1,80}$/.test(s.runId))return {status:'HOLD',events:add(s,'INVALID_RUN_ID')};
 if(!s.scene?.source?.ref || s.scene.source.ref.startsWith('FIXTURE_ONLY')===false)return {status:'HOLD',events:add(s,'SOURCE_NOT_APPROVED_FOR_TRIAL')};
 return {status:'TRIAL_ONLY',events:add(s,'SUPERVISOR_ACCEPTED_FIXTURE')};
}
async function layer(s,name,result){
 const dir=join(s.root,'layers',name,'attempt-1');
 await mkdir(dir,{recursive:true});
 const path=join(dir,name+'.json');
 const data=JSON.stringify(result,null,2)+'\n';
 await writeFile(path,data);
 return {outputs:{...s.outputs,[name]:{path,sha256:hash(data)}},events:add(s,name.toUpperCase()+'_WORKER')};
}
const story=s=>layer(s,'story',{kind:'story',asset_type:'none',color:'#FFFFFF',narrative:'Human-directed logistics chain',no_embedded_text:true});
const art=s=>layer(s,'art',{kind:'art',steps:['INTAKE','PACKAGE','ROUTE','VERIFY','DELIVER'],warning:'HOLD',editable_geometry:true});
const text=s=>layer(s,'text',{kind:'text',title:'From AI Consumer to Governed Operator.',description:'Stop asking what the model can generate. Start defining what the business needs, who is authorized, and what counts as verified delivery.',footer:'DATA IS CARGO. VERIFICATION IS PROOF OF DELIVERY.',source_status:'FIXTURE_ONLY_NOT_AUTHENTICATED'});

async function assemble(s){
 const verified={};
 for(const key of ['story','art','text']){
  const rec=s.outputs?.[key];if(!rec)return {status:'HOLD',events:add(s,'MISSING_'+key.toUpperCase())};
  const raw=await readFile(rec.path,'utf8');
  if(hash(raw)!==rec.sha256)return {status:'HOLD',events:add(s,'HASH_MISMATCH_'+key.toUpperCase())};
  verified[key]=JSON.parse(raw);
 }
 const esc=x=>String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
 const t=verified.text,a=verified.art;
 const stages=a.steps.map((x,i)=>'<div class="step">'+esc(x)+'</div>'+(i<a.steps.length-1?'<span class="arrow">→</span>':'')).join('');
 const html='<!doctype html><html lang="en"><head><meta charset="utf-8"><style>@page{size:16in 9in;margin:0}*{box-sizing:border-box;print-color-adjust:exact;-webkit-print-color-adjust:exact}html,body{padding:0;margin:0}.page{width:1536px;height:864px;padding:55px 68px;background:'+verified.story.color+';color:#111;font-family:Georgia,serif}.head{display:flex;justify-content:space-between;border-bottom:2px solid #111;font:700 19px Arial;padding-bottom:18px}.eyebrow{margin-top:39px;font:700 15px monospace;color:#b34700}h1{font-size:64px;line-height:1.1;margin:20px 0 24px}p{font-size:26px;line-height:1.4;max-width:1200px}.chain{display:flex;align-items:center;gap:14px;margin:75px 0 58px;font:700 18px monospace}.step{padding:22px 18px;border:2px solid #111;background:white;flex:1;text-align:center}.arrow,.hold{color:#b34700}.hold{font:700 20px monospace;border-top:1px solid #222;padding-top:28px}footer{margin-top:110px;border-top:2px solid #111;padding-top:15px;font:700 15px monospace}</style></head><body><main class="page"><div class="head"><span>bioscillate / BOSS</span><span>DAY ZERO / LAYERED SWARM TRIAL</span></div><div class="eyebrow">INSTRUCTIONAL DISPATCH · THREE ISOLATED WORKERS</div><h1>'+esc(t.title)+'</h1><p>'+esc(t.description)+'</p><div class="chain">'+stages+'</div><div class="hold">FAIL / UNCERTAIN → '+esc(a.warning)+' → HUMAN REVIEW</div><footer>'+esc(t.footer)+'</footer></main></body></html>';
 const path=join(s.root,'overview-layered.html');await writeFile(path,html);
 const pdf=join(s.root,'overview-layered.pdf');
 const manifest=await buildPdf({source:path,output:pdf,runId:s.runId});
 return {status:'ASSEMBLED',outputs:{...s.outputs,html:{path,sha256:hash(html)},pdf:{path:pdf,sha256:manifest.sha256}},events:add(s,'CHROMIUM_PDF_BUILT')};
}
async function verify(s){
 if(s.status!=='ASSEMBLED')return {status:'HOLD',events:add(s,'ASSEMBLY_FAILED')};
 const output=await readFile(s.outputs.pdf.path);
 const text=await readFile(s.outputs.text.path,'utf8');const copy=JSON.parse(text);
 const ok=output.subarray(0,5).toString()==='%PDF-' && hash(output)===s.outputs.pdf.sha256 && copy.title.length>0;
 const qa={status:ok?'PASS_STRUCTURAL_ONLY':'FAIL',visual_fidelity:'NOT_ESTABLISHED',release_authorized:false,layer_hashes_verified:ok,pdf_sha256:s.outputs.pdf.sha256};
 await writeFile(join(s.root,'qa.json'),JSON.stringify(qa,null,2)+'\n');
 return {status:ok?'AWAITING_HUMAN_VISUAL_REVIEW':'HOLD',qa,events:add(s,'INDEPENDENT_STRUCTURAL_CHECK')};
}
const graph=new StateGraph(State).addNode('intake',intake).addNode('story',story).addNode('art',art).addNode('text',text).addNode('assemble',assemble).addNode('verify',verify).addEdge(START,'intake').addConditionalEdges('intake',s=>s.status==='HOLD'?END:'story').addEdge('story','art').addEdge('art','text').addEdge('text','assemble').addEdge('assemble','verify').addEdge('verify',END).compile();
export async function runLayered({runId='layered-trial-001',root='output/layered-trial-001',sourceRef='FIXTURE_ONLY_DAY_ZERO'}={}){
 const dir=resolve(root);await mkdir(dir,{recursive:true});
 const result=await graph.invoke({runId,root:dir,scene:{source:{ref:sourceRef}},outputs:{},events:[]});
 await writeFile(join(dir,'run-result.json'),JSON.stringify({run_id:runId,status:result.status,events:result.events,outputs:result.outputs,qa:result.qa},null,2)+'\n');
 return result;
}
