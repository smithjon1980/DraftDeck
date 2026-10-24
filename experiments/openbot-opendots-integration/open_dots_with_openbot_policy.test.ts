import { afterEach, expect, it } from "vitest";
import { WorkspaceStore } from "../src/server/workspace.js";
import { ComputerService } from "../src/server/computer-service.js";
import { evaluateActionPolicy } from "../src/server/boss-openbot-policy.js";

const stores: WorkspaceStore[]=[];
afterEach(()=>{for(const s of stores.splice(0))s.close()});
function setup(gate:boolean) {
 const workspace=new WorkspaceStore(":memory:","synthetic-owner");
 stores.push(workspace);
 const id=workspace.dots()[0].id;
 workspace.computers.patch(id,{enabled:true,files:true,browser:true,shell:true});
 const decisions: Array<{intent:string,allowed:boolean,forward:boolean,source:string}>=[];
 const executed: string[]=[];
 let failedAudit=false;
 const transport:typeof fetch=async (input,init)=>{
  const url=String(input),path=new URL(url).pathname;
  if(path==="/computers")return Response.json({computers:[{botId:id,container:"opendots-computer-"+id,status:"running",url:"http://opendots-computer-"+id+":4100"}]});
  if(path==="/files/read"||path==="/files/write"||path==="/exec"||path==="/navigate") {
   let intent=path==="/files/read"?"read_file":path==="/files/write"?"write_file":path==="/exec"?"run_command":"navigate";
   const body=init?.body?JSON.parse(String(init.body)):{};
   if(gate){
    const filePath=String(body.path||"");
    const decision=evaluateActionPolicy({
     mode:"enforce",
     deny:['intent == "run_command"','contains(file.path, "approved/")','intent == "navigate"'],
     allow:['intent == "read_file" && file.path == "public/example.txt"','intent == "write_file" && file.path == "candidates/slide02.jsx"']
    },{
     tool:{name:"computer_"+path.split("/").pop()},
     bot:{id},actor:{id:"synthetic-owner"},page:{url:"",host:""},
     intent,file:{path:filePath,name:filePath.split("/").pop()||"",extension:filePath.split(".").pop()||""},
     mcp:{server:"",tool:"",effect:""},command:body.command||"",key:"",
     initiator:{kind:"person",id:"synthetic-owner"}
    } as Parameters<typeof evaluateActionPolicy>[1]);
    decisions.push({intent,allowed:decision.allowed,forward:decision.forward,source:decision.source});
    // Synthetic audit insertion; deliberately fail before any action dispatch.
    if(failedAudit) throw new Error("Synthetic audit service unavailable");
    if(!decision.forward)return Response.json({error:"REFUSED_BY_BOSS_POLICY"},{status:403});
   }
   executed.push(path+":"+String(body.path||""));
   return Response.json({text:"synthetic-ok",path:body.path??""});
  }
  return Response.json({error:"unknown mocked route"},{status:404});
 };
 const service=new ComputerService(workspace,{
  baseUrl:"http://localhost",voiceName:"test",slackUsers:[],runtimeUrl:"http://localhost",
  computerSupervisorUrl:"http://127.0.0.1:4312",
  computerSupervisorToken:"SYNTHETIC-SUPERVISOR",
  computerToken:"SYNTHETIC-COMPUTER"
 },()=>false,transport,1200);
 return {service,id,workspace,decisions,executed,setAuditFailure:(x:boolean)=>failedAudit=x};
}
it("BOSS integration: permitted OpenDots source read flows through actual OpenBot policy",async()=>{
 const x=setup(true);
 const result=await x.service.action(x.id,"files_read",{path:"public/example.txt"},"agent");
 expect(result).toMatchObject({text:"synthetic-ok"});
 expect(x.decisions).toHaveLength(1);
 expect(x.decisions[0]).toMatchObject({allowed:true,forward:true,source:"allow"});
 expect(x.executed).toEqual(["/files/read:public/example.txt"]);
 expect(x.workspace.computers.audit(x.id)[0].outcome).toBe("succeeded");
});
it("BOSS integration: protected text write is stopped despite OpenDots files permission",async()=>{
 const x=setup(true);
 await expect(x.service.action(x.id,"files_write",{path:"approved/ep01.md",text:"changed"},"agent")).rejects.toThrow();
 expect(x.decisions).toHaveLength(1);
 expect(x.decisions[0]).toMatchObject({allowed:false,forward:false,source:"deny"});
 expect(x.executed).toHaveLength(0);
 expect(x.workspace.computers.audit(x.id)[0].outcome).toBe("failed");
});
it("BOSS integration: bounded JSX candidate write is allowed and accounted for",async()=>{
 const x=setup(true);
 await x.service.action(x.id,"files_write",{path:"candidates/slide02.jsx",text:"export default ()=>null"},"agent");
 expect(x.executed).toEqual(["/files/write:candidates/slide02.jsx"]);
 expect(x.decisions[0]?.allowed).toBe(true);
});
it("BOSS integration: unavailable audit stops downstream dispatch",async()=>{
 const x=setup(true);x.setAuditFailure(true);
 await expect(x.service.action(x.id,"files_read",{path:"public/example.txt"},"agent")).rejects.toThrow();
 expect(x.executed).toHaveLength(0);
 expect(x.workspace.computers.audit(x.id)[0].outcome).toBe("failed");
});
it("BOSS bypass probe: current unmodified OpenDots transport without gateway would permit protected write",async()=>{
 const x=setup(false);
 await x.service.action(x.id,"files_write",{path:"approved/ep01.md",text:"changed"},"agent");
 expect(x.executed).toEqual(["/files/write:approved/ep01.md"]);
 expect(x.decisions).toHaveLength(0);
 // This PASS establishes an implementation gap, not a security property.
});
it("BOSS integration: unknown file with no explicit allow is refused",async()=>{
 const x=setup(true);
 await expect(x.service.action(x.id,"files_write",{path:"candidates/unapproved-other.js",text:"x"},"agent")).rejects.toThrow();
 expect(x.decisions[0]).toMatchObject({allowed:false,forward:false,source:"default"});
 expect(x.executed).toHaveLength(0);
});
