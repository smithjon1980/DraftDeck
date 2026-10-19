// Strict, intentionally small source->semantic-model adapters.
// The real Mermaid and PlantUML engines validate the same source in CI.
// These parsers ONLY admit the reviewed teaching subset; no silent fallbacks.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const hash = s => crypto.createHash("sha256").update(s).digest("hex");
function reject(line, label) { throw Error("UNSUPPORTED_" + label + ": " + line); }
function safeText(text) {
  if (typeof text !== "string" || text.length > 140 || /[<>]/.test(text)) {
    throw Error("UNSAFE_OR_OVERSIZE_LABEL");
  }
  return text;
}
function endpoint(raw, nodes) {
  const m = raw.trim().match(/^([A-Z][A-Z0-9_]*)(?:\["([^"]+)"\]|\{"([^"]+)"\})?$/);
  if (!m) reject(raw,"MERMAID_ENDPOINT");
  const [_, id, rect, diamond] = m;
  if (rect || diamond) {
    const shape = diamond ? "decision" : "process";
    const label = safeText(rect || diamond);
    const existing = nodes.get(id);
    if (existing && (existing.label !== label || existing.shape !== shape)) throw Error("NODE_CONFLICT:"+id);
    nodes.set(id, {id,label,shape});
  }
  return id;
}
export function parseMermaid(source) {
  if (typeof source !== "string" || source.length > 12000) throw Error("INVALID_SOURCE");
  const lines = source.split(/\r?\n/).map(x=>x.trim()).filter(Boolean);
  if (lines.shift() !== "flowchart LR") throw Error("REQUIRES_FLOWCHART_LR");
  const groups=[], nodes=new Map(), edges=[];
  let current=null;
  for (const line of lines) {
    const opening=line.match(/^subgraph ([A-Z][A-Z0-9_]*)\["([^"]+)"\]$/);
    if (opening) {
      if(current) throw Error("NESTED_SUBGRAPH_UNSUPPORTED");
      current={id:opening[1],title:safeText(opening[2]),direction:null,nodes:[]};
      if(groups.some(x=>x.id===current.id))throw Error("DUPLICATE_GROUP");
      groups.push(current);
      continue;
    }
    if (line === "direction TB") { if(!current||current.direction)throw Error("INVALID_DIRECTION");current.direction="TB";continue; }
    if (line === "end") { if(!current)throw Error("UNBALANCED_END");current=null;continue; }
    const arrow=line.split(/\s+-->\s*/);
    if(arrow.length!==2) reject(line,"MERMAID_STATEMENT");
    let rhs=arrow[1], label=null;
    const labelMatch=rhs.match(/^\|([^|]+)\|\s*(.+)$/);
    if(labelMatch) {label=safeText(labelMatch[1]);rhs=labelMatch[2];}
    const from=endpoint(arrow[0],nodes),to=endpoint(rhs,nodes);
    if(current) {
      for(const id of [from,to])if(nodes.has(id)&&!current.nodes.includes(id))current.nodes.push(id);
    }
    edges.push({from,to,label});
  }
  if(current||groups.length===0)throw Error("UNBALANCED_OR_EMPTY_GROUP");
  const groupsById=new Map(groups.map(x=>[x.id,x]));
  for(const group of groups) if(group.direction!=="TB"||group.nodes.length===0) throw Error("EMPTY_OR_UNDIRECTED_GROUP:"+group.id);
  const nodeOwners=new Map();
  for(const group of groups)for(const id of group.nodes){
    if(nodeOwners.has(id))throw Error("NODE_IN_MULTIPLE_GROUPS:"+id);
    nodeOwners.set(id,group.id);
  }
  for(const {from,to} of edges){
    if(!((nodes.has(from)&&nodeOwners.has(from))||groupsById.has(from)))throw Error("UNKNOWN_SOURCE:"+from);
    if(!((nodes.has(to)&&nodeOwners.has(to))||groupsById.has(to)))throw Error("UNKNOWN_DESTINATION:"+to);
    if(nodes.has(from)&&nodes.has(to)&&nodeOwners.get(from)!==nodeOwners.get(to))throw Error("CROSS_GROUP_NODE_EDGE_UNSUPPORTED");
    if(groupsById.has(from)!==groupsById.has(to))throw Error("MIXED_GROUP_AND_NODE_EDGE");
  }
  if(new Set(edges.map(e=>e.from+"->"+e.to+":"+e.label)).size!==edges.length)throw Error("DUPLICATE_EDGE");
  return {format:"boss-restricted-mermaid-flowchart-v1",direction:"LR",groups,
    nodes:Array.from(nodes.values()).map(n=>({...n,kind:n.label.startsWith("HOLD")?"hold":n.shape})),
    edges, sourceSha256:hash(source)};
}
export function parsePlantUML(source) {
  if(typeof source!=="string"||source.length>12000)throw Error("INVALID_SOURCE");
  const lines=source.split(/\r?\n/).map(x=>x.trim()).filter(Boolean);
  if(lines.shift()!=="@startuml"||lines.pop()!=="@enduml")throw Error("INVALID_PLANTUML_ENVELOPE");
  let title=null,block=null;
  const actors=[],items=[];
  const aliases=new Set();
  for(const line of lines){
    const t=line.match(/^title (.+)$/);
    if(t){if(title)throw Error("DUPLICATE_TITLE");title=safeText(t[1]);continue;}
    const a=line.match(/^actor ([A-Z][A-Za-z0-9_]*)$/);
    const p=line.match(/^participant "([^"]+)" as ([A-Z][A-Za-z0-9_]*)$/);
    if(a||p){
      if(items.length)throw Error("LATE_PARTICIPANT");
      const alias=a?a[1]:p[2];if(aliases.has(alias))throw Error("DUPLICATE_ACTOR");
      aliases.add(alias);actors.push({id:alias,label:safeText(a?alias:p[1]),kind:a?"actor":"participant"});continue;
    }
    const msg=line.match(/^([A-Z][A-Za-z0-9_]*)\s+(-->|->)\s+([A-Z][A-Za-z0-9_]*)\s*:\s*(.+)$/);
    if(msg){
      if(!aliases.has(msg[1])||!aliases.has(msg[3]))throw Error("UNKNOWN_MESSAGE_PARTICIPANT");
      items.push({type:"message",from:msg[1],to:msg[3],reply:msg[2]==="-->",label:safeText(msg[4]),
        branch:block?.phase||"main"});continue;
    }
    const alt=line.match(/^alt (.+)$/);
    if(alt){if(block)throw Error("NESTED_ALT_UNSUPPORTED");block={phase:"alt",name:safeText(alt[1]),elseSeen:false};items.push({type:"alt",label:block.name});continue;}
    const otherwise=line.match(/^else (.+)$/);
    if(otherwise){if(!block||block.elseSeen)throw Error("INVALID_ELSE");block.phase="else";block.elseSeen=true;items.push({type:"else",label:safeText(otherwise[1])});continue;}
    if(line==="end"){if(!block||!block.elseSeen)throw Error("UNBALANCED_OR_UNSPLIT_ALT");block=null;items.push({type:"end"});continue;}
    reject(line,"PLANTUML_STATEMENT");
  }
  if(block||!title||actors.length<2||!items.some(x=>x.type==="message"))throw Error("INCOMPLETE_SEQUENCE");
  return {format:"boss-restricted-plantuml-sequence-v1",title,actors,items,
    sourceSha256:hash(source)};
}
export function compileFixtures(projectRoot) {
  const repo=path.resolve(projectRoot,"../..");
  const fixtures=path.join(repo,"tests","diagram-golden-paths");
  const out=path.join(projectRoot,"dist","diagrams");fs.mkdirSync(out,{recursive:true});
  const flow=parseMermaid(fs.readFileSync(path.join(fixtures,"main-street-copy-intake.mmd"),"utf8"));
  const sequence=parsePlantUML(fs.readFileSync(path.join(fixtures,"main-street-copy-clarification.puml"),"utf8"));
  fs.writeFileSync(path.join(out,"intake.ir.json"),JSON.stringify(flow,null,2)+"\n");
  fs.writeFileSync(path.join(out,"clarification.ir.json"),JSON.stringify(sequence,null,2)+"\n");
  return {flow,sequence};
}
const mainPath=process.argv[1]&&path.resolve(process.argv[1]);
if(mainPath===fileURLToPath(import.meta.url)){
  const {flow,sequence}=compileFixtures(path.resolve(path.dirname(mainPath),".."));
  console.log(JSON.stringify({status:"RESTRICTED_IR_COMPILED",nodes:flow.nodes.length,
    flowEdges:flow.edges.length,participants:sequence.actors.length,
    messages:sequence.items.filter(x=>x.type==="message").length}));
}
