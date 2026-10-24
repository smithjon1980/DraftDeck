/**
 * BOSS OpenDots -> OpenBot source-policy SPIKE, not production gateway.
 *
 * Runs in ephemeral OpenDots checkout under Vitest, imports the exact pinned
 * upstream OpenBot evaluateActionPolicy from boss-openbot-policy/policy.ts.
 *
 * Network transport is injected into the REAL OpenDots ComputerService. It
 * simulates BOSS policy mediation; network lockout and deployment are NOT tested.
 */
import { afterEach, expect, it } from "vitest";
import { WorkspaceStore } from "../src/server/workspace.js";
import { ComputerService } from "../src/server/computer-service.js";
import { evaluateActionPolicy } from "../boss-openbot-policy/policy.ts";
import type { ActionPolicy, PolicyContext } from "../boss-openbot-policy/policy.ts";

const instances:WorkspaceStore[]=[];
afterEach(()=>{for(const w of instances.splice(0))w.close()});
const base="http://127.0.0.1:4312";
const config={
  baseUrl:"http://127.0.0.1",
  runtimeUrl:"http://127.0.0.1",
  voiceName:"voice",
  slackUsers:[],
  computerNamespace:"opendots",
  computerSupervisorUrl:base,
  computerSupervisorToken:"SYNTHETIC-SUPERVISOR-TOKEN",
  computerToken:"SYNTHETIC-COMPUTER-MASTER"
};
function init() {
 const w=new WorkspaceStore(":memory:","human-reviewer"); instances.push(w);
 const dot=w.dots()[0].id;
 w.computers.patch(dot,{enabled:true,browser:true,files:true,shell:true});
 return {w,dot};
}
const policy:ActionPolicy={
  mode:"enforce",
  deny:[
    'intent == "run_command"',
    'intent == "activate"',
    'contains(file.path, "approved/")',
    'contains(file.path, ".env")',
    'intent == "navigate"',
    'intent == "write_file" && bot.id != "BOSS-OWNER-DOT"'
  ],
  allow:[
    'intent == "write_file" && file.path == "candidates/slide02.jsx" && bot.id == "BOSS-OWNER-DOT"',
    'intent == "read_file" && file.path == "source/public-brief.txt"'
  ]
};
type RecordRow={dotId:string;action:string;decision:string;allowed:boolean;forward:boolean;source:string};
function fakeCompute(rule=policy) {
 const records:RecordRow[]=[];
 const effects:{dotId:string;action:string;args:unknown}[]=[];
 let auditFails=false;
 const transport:typeof fetch=async(input,init)=>{
  const u=new URL(String(input));
  const path=u.pathname;
  if(path==="/computers"){
   return Response.json({computers:[...new Set([..."AB"].map(t=>t))].filter(Boolean).flatMap(()=>{
    return [];
   })]});
  }
  // The caller's x-openbot-bot-id header is NOT a trusted identity in
  // production. This spike uses it to construct test context and explicitly
  // forbids production adoption until signed actor/bot context is provided.
  const suppliedDot=new Headers(init?.headers).get("x-openbot-bot-id")||"";
  const computerName=u.hostname;
  const targetDot=computerName.replace(/^opendots-computer-/,"");
  if(targetDot!==suppliedDot)return Response.json({error:"identity mismatch"},{status:403});
  const payload=init?.body?JSON.parse(String(init.body)):{};
  const intent=path==="/exec"?"run_command":path==="/files/write"?"write_file":
    path==="/files/read"?"read_file":path==="/navigate"?"navigate":
    path==="/click"||path==="/key"||path==="/type"?"activate":"read";
  const file=typeof payload.path==="string"?payload.path:"";
  const ctx:PolicyContext={
   tool:{name: "computer_"+path.replace(/^\//,"").replace(/\//g,"_")},
   bot:{id:targetDot},actor:{id:"human-reviewer"},
   page:{url:"",host:""},
   file:{path:file,name:file.split("/").at(-1)||"",extension:file.split(".").at(-1)||""},
   mcp:{server:"",tool:"",effect:""},element:{ref:"",role:"",name:""},
   command:typeof payload.command==="string"?payload.command:"",
   intent,
   initiator:{kind:"person",id:"human-reviewer"}
  };
  const decision=evaluateActionPolicy(rule,ctx);
  const next:RecordRow={dotId:targetDot,action:path,decision:decision.source,
    allowed:decision.allowed,forward:decision.forward,source:decision.reason};
  // The audit must be accepted before execution; a failed insertion prevents effect.
  if(auditFails)throw new Error("SYNTHETIC_EVIDENCE_APPEND_FAILED");
  records.push(next);
  if(!decision.forward)return Response.json({error:"blocked"},{status:403});
  effects.push({dotId:targetDot,action:path,args:payload});
  return Response.json({path:"SYNTHETIC_SUCCESS"});
 };
 function service(w:WorkspaceStore) {
  // The actual OpenDots ComputerService code gets this test transport.
  return new ComputerService(w,config,()=>false,async(input,init)=>{
   const u=new URL(String(input));
   if(u.pathname==="/computers"){
    const ids=w.dots().map(d=>d.id);
    return Response.json({computers:ids.map(id=>({botId:id,container:"opendots-computer-"+id,status:"running",
      url:"http://opendots-computer-"+id+":4100"}))});
   }
   return transport(input,init);
  });
 }
 return {records,effects,service,failAudit:()=>{auditFails=true}};
}

it("BOSS mediated: native OpenDots action accepts only bounded JSX candidate", async()=>{
 const {w,dot}=init();
 // For the synthetic fixture ONLY, bind the exact allowed Dot ID explicitly.
 const gated=fakeCompute({...policy,allow:[
  'intent == "write_file" && file.path == "candidates/slide02.jsx" && bot.id == "'+dot+'"'
 ],deny:policy.deny.filter(x=>!x.includes("BOSS-OWNER-DOT"))});
 const app=gated.service(w);
 const r=await app.action(dot,"files_write",{path:"candidates/slide02.jsx",contents:"export default function Slide(){}"},"agent");
 expect(r).toMatchObject({path:"SYNTHETIC_SUCCESS"});
 expect(gated.records).toHaveLength(1);
 expect(gated.records[0].allowed).toBe(true);
 expect(gated.effects).toHaveLength(1);
 expect(w.computers.audit(dot)[0].outcome).toBe("succeeded");
});

it("BOSS mediated: protected approved source stays blocked even though OpenDots files permission is enabled", async()=>{
 const {w,dot}=init();
 const gate=fakeCompute();
 const app=gate.service(w);
 await expect(app.action(dot,"files_write",{path:"approved/episode01.txt",contents:"changed"},"agent")).rejects.toThrow("HTTP 403");
 expect(gate.records).toHaveLength(1);
 expect(gate.records[0].allowed).toBe(false);
 expect(gate.effects).toHaveLength(0);
 expect(w.computers.audit(dot)[0].outcome).toBe("failed");
});
it("BOSS mediated: shell is blocked even though OpenDots shell permission is enabled",async()=>{
 const {w,dot}=init(); const gate=fakeCompute();
 await expect(gate.service(w).action(dot,"exec",{command:"echo SYNTHETIC"},"agent"))
  .rejects.toThrow("HTTP 403");
 expect(gate.effects).toHaveLength(0);
 expect(gate.records[0].allowed).toBe(false);
});
it("BOSS mediated: an OpenBot malformed deny rule blocks rather than passes",async()=>{
 const {w,dot}=init();
 const gate=fakeCompute({mode:"enforce",deny:["(( BROKEN"],allow:["true"]});
 await expect(gate.service(w).action(dot,"files_write",{path:"candidates/slide02.jsx",contents:"x"},"agent"))
  .rejects.toThrow("HTTP 403");
 expect(gate.effects).toHaveLength(0);
});
it("BOSS mediated: failed synthetic audit append prevents computer effect",async()=>{
 const {w,dot}=init();const gate=fakeCompute({mode:"enforce",deny:[],allow:["true"]});
 gate.failAudit();
 await expect(gate.service(w).action(dot,"files_write",{path:"candidates/slide02.jsx",contents:"x"},"agent"))
 .rejects.toThrow(/unavailable|invalid response/);
 expect(gate.effects).toHaveLength(0);
 expect(gate.records).toHaveLength(0);
 expect(w.computers.audit(dot)[0].outcome).toBe("failed");
});
it("BOSS mediated: 25 concurrently denied protected writes yield 25 refusals and zero effects",async()=>{
 const {w,dot}=init();const gate=fakeCompute();const app=gate.service(w);
 const list=await Promise.allSettled(Array.from({length:25},()=>app.action(dot,"files_write",
 {path:"approved/episode01.txt",contents:"NO"},"agent")));
 expect(list.every(x=>x.status==="rejected")).toBe(true);
 expect(gate.effects).toHaveLength(0);
 expect(gate.records).toHaveLength(25);
});
// This is a *warning demonstration*, not a bypass that would be allowed for deployment.
it("BOSS diagnostic: removing the transport policy adapter permits a write in OpenDots without any OpenBot decision",async()=>{
 const {w,dot}=init();
 let directEffects=0;
 const rawTransport:typeof fetch=async(input)=>{
  const u=new URL(String(input));
  if(u.pathname==="/computers")
   return Response.json({computers:[{botId:dot,container:"opendots-computer-"+dot,status:"running",
    url:"http://opendots-computer-"+dot+":4100"}]});
  directEffects++;
  return Response.json({path:"UNMEDIATED_SYNTHETIC_WRITE"});
 };
 const app=new ComputerService(w,config,()=>false,rawTransport);
 await expect(app.action(dot,"files_write",{path:"approved/episode01.txt",contents:"changed"},"agent"))
 .resolves.toMatchObject({path:"UNMEDIATED_SYNTHETIC_WRITE"});
 expect(directEffects).toBe(1);
 // This establishes that per-Dot files permission DOES NOT equal OpenBot CEL evaluation.
 // Production design must remove direct routing to ungoverned computer endpoints.
});
