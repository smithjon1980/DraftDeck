import {createHash, randomUUID} from "node:crypto";
import {writeFileSync} from "node:fs";
import {evaluateActionPolicy} from "./upstream/server/src/computer/policy.ts";

const secret="SYNTHETIC_KEY_NEVER_USED_FOR_REAL_AUTH";
const contexts=[];
const results=[];
const digest=x=>createHash("sha256").update(JSON.stringify(x)).digest("hex");
const policy={
  mode:"enforce",
  deny:[
    'intent == "write_tool"',
    'intent == "run_command"',
    'intent == "activate"',
    'contains(file.path, "approved")',
    'initiator.kind == "routine" && intent == "write_file"'
  ],
  allow:[
    'intent == "read"',
    'intent == "read_file" && file.path == "source/synthetic.txt"',
    'intent == "write_file" && file.path == "candidates/slide02.jsx"'
  ]
};
function context(request) {
 const path=request.path??"";
 return {
  tool:{name:request.tool??"computer_read_file"},
  bot:{id:request.bot??"story"},
  actor:{id:request.actor??"reviewer"},
  page:{url:"",host:""},
  element:{ref:"",role:"",name:""},
  file:{path,name:path.split("/").at(-1)??"",extension:path.split(".").at(-1)??""},
  mcp:{server:request.server??"",tool:request.mcpTool??"",effect:request.effect??""},
  command:request.command??"",key:request.key??"",
  intent:request.intent??"read",
  initiator:{kind:request.initiator??"person",id:request.actor??"reviewer"}
 };
}
const simulator={
 calls:[], audit:[], approvals:new Map(), executions:new Map(), replayKeys:new Set(),
 // Here OpenDots is the caller. It is NEVER able to call the mock computer directly.
 async request(req){
  const ctx=context(req);
  const d=evaluateActionPolicy(policy,ctx);
  const entry={id:randomUUID(),intent:ctx.intent,actor:ctx.actor.id,bot:ctx.bot.id,
   source:d.source,rule:d.matched,decision:d.allowed?"allow":"deny",
   forwarded:false,hash:digest(req)};
  this.audit.push(entry);
  if(!d.allowed||!d.forward) return {status:"DENIED",receipt:entry.id};
  if(req.consequential){
   const id=randomUUID();
   this.approvals.set(id,{digest:digest(req),request:req,status:"pending",actor:{id:ctx.actor.id},used:false});
   return {status:"APPROVAL_REQUIRED",approvalId:id};
  }
  this.calls.push({id:randomUUID(),action:req.intent,path:req.path});
  entry.forwarded=true;
  return {status:"EXECUTED",receipt:entry.id};
 },
 approve(id,decision,{actor,request}){
  const p=this.approvals.get(id);
  if(!p||p.status!=="pending")return "DENIED";
  if(!actor||actor===p.request.bot||actor!==p.actor.id)return "DENIED";
  if(digest(request)!==p.digest)return "DENIED";
  if(decision!=="approve"){p.status="denied";return "DENIED";}
  p.status="consumed";
  this.calls.push({id:randomUUID(),action:p.request.intent,path:p.request.path});
  return "EXECUTED";
 }
};
async function test(name,fn){
 try{const ok=await fn();results.push({name,status:ok?"PASS":"FAIL"})}
 catch(e){results.push({name,status:"FAIL",error:String(e)})}
}
await test("OpenDots public read through gateway",async()=> (await simulator.request({intent:"read"})).status==="EXECUTED");
await test("OpenDots candidate write through gateway",async()=> (await simulator.request({intent:"write_file",path:"candidates/slide02.jsx"})).status==="EXECUTED");
await test("protected narration write refused",async()=> (await simulator.request({intent:"write_file",path:"approved/EP01.md"})).status==="DENIED");
await test("external MCP write refused",async()=> (await simulator.request({intent:"write_tool",server:"github",mcpTool:"merge",effect:"write"})).status==="DENIED");
await test("browser activation refused",async()=> (await simulator.request({intent:"activate",tool:"computer_click"})).status==="DENIED");
await test("routine write refused",async()=> (await simulator.request({intent:"write_file",path:"candidates/slide02.jsx",initiator:"routine"})).status==="DENIED");
await test("unknown file fails closed",async()=> (await simulator.request({intent:"write_file",path:"source/other.txt"})).status==="DENIED");
await test("consequential write requires human approval",async()=>{
 const r=await simulator.request({intent:"write_file",path:"candidates/slide02.jsx",consequential:true});
 return r.status==="APPROVAL_REQUIRED"&&!!r.approvalId;
});
await test("agent cannot self approve",async()=>{
 const q={intent:"write_file",path:"candidates/slide02.jsx",consequential:true,bot:"story"};
 const r=await simulator.request(q);
 return simulator.approve(r.approvalId,"approve",{actor:"story",request:q})==="DENIED";
});
await test("changed action cannot reuse approval",async()=>{
 const q={intent:"write_file",path:"candidates/slide02.jsx",consequential:true};
 const r=await simulator.request(q);
 return simulator.approve(r.approvalId,"approve",{actor:"reviewer",request:{...q,path:"approved/EP01.md"}})==="DENIED";
});
await test("valid approval executes exactly once and replay fails",async()=>{
 const q={intent:"write_file",path:"candidates/slide02.jsx",consequential:true};
 const r=await simulator.request(q);
 const before=simulator.calls.length;
 const first=simulator.approve(r.approvalId,"approve",{actor:"reviewer",request:q});
 const second=simulator.approve(r.approvalId,"approve",{actor:"reviewer",request:q});
 return first==="EXECUTED"&&second==="DENIED"&&simulator.calls.length===before+1;
});
await test("denial is auditable and never dispatched",async()=>{
 const before=simulator.calls.length;
 const r=await simulator.request({intent:"run_command",command:"echo synthetic"});
 return r.status==="DENIED"&&simulator.calls.length===before&&simulator.audit.at(-1).decision==="deny";
});
await test("50 concurrent denial requests never reach computer",async()=>{
 const before=simulator.calls.length;
 const r=await Promise.all(Array.from({length:50},()=>simulator.request({intent:"write_file",path:"approved/EP01.md"})));
 return r.every(x=>x.status==="DENIED")&&simulator.calls.length===before;
});
const out={
 status:results.every(x=>x.status==="PASS")?"ISOLATED_GATEWAY_SIMULATION_PASS":"FAIL",
 tests:results,
 count:results.length,
 passed:results.filter(x=>x.status==="PASS").length,
 mockedComputerCalls:simulator.calls.length,
 deniedDecisions:simulator.audit.filter(x=>x.decision==="deny").length,
 source:"UNMODIFIED_PINNED_OPENBOT_POLICY_FUNCTION",
 claims:{
  actualOpenDotsApplicationConnected:false,
  actualOpenBotPolicyFunctionExecuted:true,
  syntheticOpenDotsCaller:true,
  realMcpGateway:false,
  persistentApprovals:false,
  productionReady:false
 }
};
writeFileSync("results.json",JSON.stringify(out,null,2));
console.log(JSON.stringify(out,null,2));
if(out.status==="FAIL")process.exitCode=1;
