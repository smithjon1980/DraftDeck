import {describe,it,expect} from "vitest";
import {createHmac,createHash} from "node:crypto";
import {WorkspaceStore} from "../src/server/workspace.js";
import {ComputerService} from "../src/server/computer-service.js";
import {computerTools} from "../src/server/computer-tools.js";
import {evaluateActionPolicy} from "./boss-openbot-policy.js";

const master="TEST_ONLY_MASTER_COMPUTER_SECRET_NOT_REAL";
const policy={mode:"enforce",deny:[
 'intent == "run_command"',
 'intent == "activate"',
 'intent == "navigate"',
 'intent == "write_file" && contains(file.path, "approved/")'
],allow:[
 'intent == "read_file" && file.path == "source/public.txt"',
 'intent == "write_file" && file.path == "candidates/s02.txt"'
]};
const fingerprint=(action:string,body:any,botId:string)=>createHash("sha256").update(JSON.stringify({action,body,botId})).digest("hex");
const context=(id:string,action:string,body:any)=>({
 tool:{name:"computer_"+action},bot:{id},actor:{id:"BOSS-OWNER"},
 page:{url:"",host:""},element:{ref:"",name:"",role:""},mcp:{server:"",tool:"",effect:""},
 file:{path:String(body.path??""),name:"",extension:""},command:String(body.command??""),key:String(body.key??""),
 intent:action==="exec"?"run_command":action==="files_read"?"read_file":action==="files_write"?"write_file":
 action==="navigate"?"navigate":["click","key","type"].includes(action)?"activate":"unknown",
 initiator:{kind:"person",id:"BOSS-OWNER"}
});
class Trial {
 ws=new WorkspaceStore(":memory:","BOSS-OWNER");
 id=this.ws.dots()[0].id;
 sent:string[]=[];
 audited:string[]=[];
 failAudit=false;
 failPolicy=false;
 humanApproval=new Set<string>();
 service:ComputerService;
 constructor(){
  this.ws.computers.patch(this.id,{enabled:true,browser:true,files:true,shell:true});
  this.service=new ComputerService(this.ws,{
   baseUrl:"http://127.0.0.1",voiceName:"synthetic",slackUsers:[],runtimeUrl:"http://127.0.0.1",
   computerSupervisorUrl:"http://127.0.0.1:4312",computerSupervisorToken:"TEST",
   computerToken:master,computerNamespace:"opendots"
  },()=>false,this.boundary);
 }
 close(){this.ws.close()}
 authorize(action:string,body:any){this.humanApproval.add(fingerprint(action,body,this.id))}
 boundary:typeof fetch=async (url,init)=>{
  const address=String(url);
  if(address.endsWith("/computers"))return Response.json({computers:[{botId:this.id,container:"opendots-computer-"+this.id,status:"running",url:"http://opendots-computer-"+this.id+":4100"}]});
  const dest=new URL(address);
  const token=createHmac("sha256",master).update("opendots-computer:"+this.id).digest("hex");
  const headers=new Headers(init?.headers);
  if(dest.hostname!=="opendots-computer-"+this.id || headers.get("authorization")!=="Bearer "+token || headers.get("x-openbot-bot-id")!==this.id)throw Error("IDENTITY_DENIED");
  const action=dest.pathname.slice(1).replace(/^files\//,"files_");
  const body=init?.body?JSON.parse(String(init.body)):{};
  const key=fingerprint(action,body,this.id);
  const decision=this.failPolicy?{allowed:false,forward:false}:evaluateActionPolicy(policy,context(this.id,action,body) as any);
  if(!decision.allowed||!decision.forward){if(this.failAudit)throw Error("AUDIT_UNAVAILABLE");this.audited.push("DENY:"+action);throw Error("DENIED")}
  if(action==="files_write"){
   if(!this.humanApproval.has(key)){if(this.failAudit)throw Error("AUDIT_UNAVAILABLE");this.audited.push("APPROVAL_REQUIRED");throw Error("EXPLICIT_HUMAN_APPROVAL_REQUIRED")}
   this.humanApproval.delete(key);
  }
  if(this.failAudit)throw Error("AUDIT_UNAVAILABLE");
  this.audited.push("ALLOW:"+action);
  this.sent.push(action);
  if(action==="files_read")return Response.json({path:body.path,text:"PUBLIC SYNTHETIC",bytes:16});
  if(action==="files_write")return Response.json({path:body.path,bytes:body.contents.length,appended:false});
  return Response.json({ok:true});
 }
 call(action:any,body:any){return this.service.action(this.id,action,body,"agent")}
}
describe("BOSS candidate non-bypassable boundary at OpenDots ComputerService transport",()=>{
 it("real upstream OpenDots tool can read a scoped source through gated transport",async()=>{const h=new Trial();try{const tools=computerTools(h.service,h.id,()=>{},new AbortController().signal);const t=tools.find(x=>x.name==="computer_files_read")!;await expect(t.execute?.({path:"source/public.txt"})).resolves.toMatchObject({text:"PUBLIC SYNTHETIC"});expect(h.sent).toEqual(["files_read"]);expect(h.audited).toEqual(["ALLOW:files_read"])}finally{h.close()}});
 for(const [action,body] of [["files_write",{path:"approved/narration.md",contents:"TAMPER"}],["exec",{command:"echo synthetic"}],["navigate",{url:"https://example.test"}],["click",{ref:"button-1"}],["key",{key:"Enter"}],["files_read",{path:"secret.txt"}]] as const){
  it("rejects unauthorized "+action+" before forwarding",async()=>{const h=new Trial();try{await expect(h.call(action,body)).rejects.toThrow();expect(h.sent).toHaveLength(0)}finally{h.close()}});
 }
 it("candidate write requires one-shot human approval bound to exact bytes",async()=>{const h=new Trial();try{const body={path:"candidates/s02.txt",contents:"FIRST"};await expect(h.call("files_write",body)).rejects.toThrow();h.authorize("files_write",body);await expect(h.call("files_write",{...body,contents:"ALTERED"})).rejects.toThrow();await h.call("files_write",body);await expect(h.call("files_write",body)).rejects.toThrow();expect(h.sent).toEqual(["files_write"])}finally{h.close()}});
 it("audit outage prevents dispatch of an otherwise allowed read",async()=>{const h=new Trial();try{h.failAudit=true;await expect(h.call("files_read",{path:"source/public.txt"})).rejects.toThrow();expect(h.sent).toHaveLength(0);expect(h.audited).toHaveLength(0)}finally{h.close()}});
 it("policy evaluator failure cannot become allow",async()=>{const h=new Trial();try{h.failPolicy=true;await expect(h.call("files_read",{path:"source/public.txt"})).rejects.toThrow();expect(h.sent).toHaveLength(0)}finally{h.close()}});
 it("25 denied shell requests have no dispatches",async()=>{const h=new Trial();try{const r=await Promise.allSettled(Array.from({length:25},()=>h.call("exec",{command:"echo x"})));expect(r.every(x=>x.status==="rejected")).toBe(true);expect(h.sent).toHaveLength(0);expect(h.audited).toHaveLength(25)}finally{h.close()}});
 it("explicit NEGATIVE CONTROL: bypass persists without gated transport",async()=>{const ws=new WorkspaceStore(":memory:","BOSS-OWNER");try{const id=ws.dots()[0].id;ws.computers.patch(id,{enabled:true,files:true});let writes=0;const direct:typeof fetch=async (url)=>String(url).endsWith("/computers")?Response.json({computers:[{botId:id,container:"opendots-computer-"+id,status:"running",url:"http://opendots-computer-"+id+":4100"}]}):(++writes,Response.json({path:"approved/narration.md",bytes:1,appended:false}));const svc=new ComputerService(ws,{baseUrl:"http://127.0.0.1",voiceName:"synthetic",slackUsers:[],runtimeUrl:"http://127.0.0.1",computerSupervisorUrl:"http://127.0.0.1:4312",computerSupervisorToken:"TEST",computerToken:master,computerNamespace:"opendots"},()=>false,direct);await svc.action(id,"files_write",{path:"approved/narration.md",contents:"X"},"agent");expect(writes).toBe(1)}finally{ws.close()}});
});
