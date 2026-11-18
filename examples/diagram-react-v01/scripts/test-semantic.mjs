import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parseMermaid, parsePlantUML } from "./compile-semantic.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"../../..");
const file=(name)=>fs.readFileSync(path.join(root,"tests","diagram-golden-paths",name),"utf8");
const flowSource=file("main-street-copy-intake.mmd");
const sequenceSource=file("main-street-copy-clarification.puml");
test("source-governed Mermaid graph accounts for every node, group and directed edge",()=>{
  const m=parseMermaid(flowSource);
  assert.equal(m.groups.length,3);
  assert.equal(m.nodes.length,8);
  assert.equal(m.edges.length,9);
  assert.equal(m.nodes.find(x=>x.id==="B").kind,"decision");
  assert.equal(m.nodes.find(x=>x.id==="F").kind,"decision");
  assert.equal(m.nodes.find(x=>x.id==="C").kind,"hold");
  for(const key of ["B->C:No","C->B:null","F->G:No","F->H:Yes",
                     "INTAKE->PRODUCTION:All required data verified",
                     "PRODUCTION->QUALITY:Completed item"]){
    assert(m.edges.some(e=>e.from+"->"+e.to+":"+e.label===key),key);
  }
});
test("PlantUML actor set, message direction and alternate branch survive conversion",()=>{
  const m=parsePlantUML(sequenceSource);
  assert.deepEqual(m.actors.map(x=>x.id),["Customer","Counter","Order","Production"]);
  const messages=m.items.filter(x=>x.type==="message");
  assert.equal(messages.length,8);
  assert.equal(m.items.filter(x=>x.type==="alt").length,1);
  assert.equal(m.items.filter(x=>x.type==="else").length,1);
  assert.equal(m.items.filter(x=>x.type==="end").length,1);
  assert.deepEqual(messages.at(-1),{type:"message",from:"Counter",to:"Production",
    label:"Release only after validation",reply:false,branch:"main"});
  assert.equal(messages.find(x=>x.label.includes("HOLD")).branch,"alt");
});
test("unsupported Mermaid syntax is not silently redrawn",()=>{
  assert.throws(()=>parseMermaid(flowSource.replace("flowchart LR","sequenceDiagram")),
    /REQUIRES_FLOWCHART_LR/);
  assert.throws(()=>parseMermaid(flowSource.replace('C --> B','C -.-> B')),
    /UNSUPPORTED_MERMAID_STATEMENT/);
  assert.throws(()=>parseMermaid(flowSource.replace('C --> B','C --> Z')),
    /UNKNOWN_DESTINATION/);
  assert.throws(()=>parseMermaid(flowSource.replace('C --> B','C --> B\n    click B "javascript:alert(1)"')),
    /UNSUPPORTED_MERMAID_STATEMENT/);
});
test("unsupported PlantUML constructs and missing participant fail closed",()=>{
  assert.throws(()=>parsePlantUML(sequenceSource.replace("Customer -> Counter","Unknown -> Counter")),
    /UNKNOWN_MESSAGE_PARTICIPANT/);
  assert.throws(()=>parsePlantUML(sequenceSource.replace("else Required fields complete","note over Counter: invented branch")),
    /UNSUPPORTED_PLANTUML_STATEMENT/);
  assert.throws(()=>parsePlantUML(sequenceSource.replace("else Required fields complete","")),
    /UNBALANCED_OR_UNSPLIT_ALT/);
});
