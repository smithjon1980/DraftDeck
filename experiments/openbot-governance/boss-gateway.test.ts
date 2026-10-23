/**
 * BOSS-to-OpenBot GATEWAY conformance on pinned upstream code with synthetic-only
 * provider, browser snapshot, network transport and audit. No physical side effects.
 */
import {describe,expect,test} from "bun:test";
import type {AuditEventInput,AuditStore} from "../src/audit";
import {ActionRefusedError,createComputerGateway} from "../src/computer/gateway";
import type {ActionPolicy} from "../src/computer/policy";
import type {ComputerProvider} from "../src/computer/provider";

const ACTOR = {id:"boss-synthetic-operator"};
const POLICY:ActionPolicy={
 mode:"enforce",
 deny:[
   'intent == "run_command"',
   'intent == "write_file" && (contains(file.path,"approved/") || contains(file.path,"release/"))',
 ],
 allow:[
   'intent == "write_file" && contains(file.path,"candidates/")',
   'intent == "read_file" && contains(file.path,"source/")',
 ],
};

function makeGateway(options:{auditFails?:boolean}={}) {
 const rows:AuditEventInput[]=[];
 const computerCalls:Array<{endpoint:string,rowsBefore:number}>=[];
 const auditStore:AuditStore={insert:async event=>{
   if(options.auditFails)throw new Error("SYNTHETIC_AUDIT_UNAVAILABLE");
   rows.push(event);
 }};
 const provider:ComputerProvider={
  name:"synthetic",
  isolation:"per-bot",
  locate:async()=>"http://agent-computer:4100",
  status:async botId=>({botId,state:"ready"}),
  stop:async()=>({wasRunning:false}),
  reset:async()=>({cleared:false}),
  list:async()=>[],
 };
 const fetchImpl=(async (url:string) =>{
   const path=new URL(url).pathname;
   if(path==="/snapshot")return Response.json({
     snapshotId:7,url:"https://example.invalid/mock",title:"Synthetic",truncated:false,elements:[]
   });
   computerCalls.push({endpoint:path,rowsBefore:rows.length});
   if(path==="/files/write")return Response.json({path:"candidates/slide02.html",bytes:17,appended:false});
   if(path==="/files/read")return Response.json({path:"source/public-sample.txt",text:"test",truncated:false,bytes:4});
   if(path==="/exec")return Response.json({command:"echo test",exitCode:0,stdout:"test",stderr:"",truncated:false,timedOut:false,elapsedMs:1});
   return Response.json({error:"unexpected mock route"},{status:404});
 }) as unknown as typeof fetch;
 const gateway=createComputerGateway({provider,auditStore,fetchImpl,policy:()=>POLICY});
 return {gateway,rows,computerCalls};
}

describe("BOSS synthetic actions through REAL OpenBot gateway",()=>{
 test("candidate write proceeds only after the allowed event is audited",async()=>{
  const {gateway,rows,computerCalls}=makeGateway();
  await gateway.writeFile("boss-slide-agent",ACTOR,{
   path:"candidates/slide02.html",contents:"SYNTHETIC PRIVATE-FREE DATA"
  });
  expect(computerCalls.map(x=>x.endpoint)).toEqual(["/files/write"]);
  expect(computerCalls[0].rowsBefore).toBe(1);
  expect(rows).toHaveLength(1);
  expect(rows[0].eventType).toBe("computer.action_allowed");
  expect(JSON.stringify(rows[0])).not.toContain("SYNTHETIC PRIVATE-FREE DATA");
 });
 test("approved manuscript write is refused without sending to computer",async()=>{
  const {gateway,rows,computerCalls}=makeGateway();
  await expect(gateway.writeFile("boss-slide-agent",ACTOR,{
   path:"approved/episode01-v4.txt",contents:"malicious overwrite mock",
  })).rejects.toThrow(ActionRefusedError);
  expect(computerCalls).toHaveLength(0);
  expect(rows).toHaveLength(1);
  expect(rows[0].eventType).toBe("computer.action_refused");
  expect(JSON.stringify(rows[0])).not.toContain("malicious overwrite mock");
 });
 test("release path write is refused and audited",async()=>{
  const {gateway,rows,computerCalls}=makeGateway();
  await expect(gateway.writeFile("boss-slide-agent",ACTOR,{
   path:"release/slide02.html",contents:"synthetic release request",
  })).rejects.toThrow(ActionRefusedError);
  expect(computerCalls).toHaveLength(0);
  expect(rows[0].eventType).toBe("computer.action_refused");
 });
 test("missing audit persistence blocks a normally allowed candidate write",async()=>{
  const {gateway,rows,computerCalls}=makeGateway({auditFails:true});
  await expect(gateway.writeFile("boss-slide-agent",ACTOR,{
   path:"candidates/slide02.html",contents:"synthetic candidate",
  })).rejects.toThrow();
  expect(rows).toHaveLength(0);
  expect(computerCalls).toHaveLength(0);
 });
 test("shell is refused with an audit event and no command execution",async()=>{
  const {gateway,rows,computerCalls}=makeGateway();
  await expect(gateway.runCommand("boss-slide-agent",ACTOR,{
   command:"echo synthetic",
  })).rejects.toThrow(ActionRefusedError);
  expect(computerCalls).toHaveLength(0);
  expect(rows[0].eventType).toBe("computer.action_refused");
 });
});
