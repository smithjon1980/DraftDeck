import React, { useLayoutEffect, useRef, useState } from "react";

// The markup of every semantic label is native HTML. Only connector strokes
// are SVG geometry. The components consume generated IR, not a copied drawing.
const highlight = (label, kind) => kind === "hold" || /\bHOLD\b/i.test(label);
function BossProcessNode({node,position}) {
  return <div data-boss-node={node.id} data-boss-native-label={node.id}
    className={"boss-process-node "+(highlight(node.label,node.kind)?"boss-process-node--hold":"")}>
    <div className="boss-node-index">{position}</div>
    <div className="boss-node-wording">{node.label}</div>
  </div>;
}
function BossDecisionNode({node,position}) {
  return <div data-boss-node={node.id} data-boss-native-label={node.id} className="boss-decision-node">
    <span aria-hidden="true" className="boss-diamond-shape" />
    <span className="boss-diamond-text">
      <span className="boss-node-index boss-node-index--decision">{position}</span>
      <span className="boss-node-wording">{node.label}</span>
    </span>
  </div>;
}
function BossFlowNode({node,position}) {
  if(node.kind==="decision")return <BossDecisionNode node={node} position={position}/>;
  return <BossProcessNode node={node} position={position}/>;
}
function stageOrder(group,model) {
  const nodeMap = new Map(model.nodes.map(n=>[n.id,n]));
  return group.nodes.map(n=>nodeMap.get(n));
}
function BossStage({group,model,index}) {
  const nodes=stageOrder(group,model);
  // A decision with two distinct forward outcomes is represented as a
  // decision node above two independent native-HTML branch cards.
  const fork=nodes.find(n=>n.kind==="decision" &&
    new Set(model.edges.filter(e=>e.from===n.id && group.nodes.includes(e.to)).map(e=>e.to)).size>=2);
  const branchIds=fork?model.edges.filter(e=>e.from===fork.id&&group.nodes.includes(e.to)).map(e=>e.to):[];
  const beforeFork=fork?nodes.filter(n=>n.id!==fork.id&&!branchIds.includes(n.id)):[];
  const sequences=fork?beforeFork: nodes;
  const getNum=id=>String(model.nodes.findIndex(n=>n.id===id)+1).padStart(2,"0");
  return <section data-boss-stage={group.id} className="boss-stage">
    <header className="boss-stage-heading">
      <span className="boss-stage-id">PHASE {String(index+1).padStart(2,"0")}</span>
      <strong>{group.title.replace(/^\d+\s*\/\s*/,"")}</strong>
    </header>
    <div className="boss-stage-contents">
      {sequences.map(n=><BossFlowNode key={n.id} node={n} position={getNum(n.id)}/>)}
      {fork&& <BossFlowNode node={fork} position={getNum(fork.id)}/>}
      {fork&& <div className="boss-stage-branches">
        {branchIds.map(id=><BossFlowNode key={id} node={nodes.find(n=>n.id===id)} position={getNum(id)}/>)}
      </div>}
    </div>
    <p className="boss-stage-footnote">STRUCTURE: MERMAID / SOURCE-TRACEABLE</p>
  </section>;
}
function anchor(bounds,root,side){
  const r=root.getBoundingClientRect();
  return {
    left:bounds.left-r.left, right:bounds.right-r.left,
    top:bounds.top-r.top, bottom:bounds.bottom-r.top,
    cx:(bounds.left+bounds.right)/2-r.left,
    cy:(bounds.top+bounds.bottom)/2-r.top
  };
}
function wireEdge(edge,canvas){
  const stageEdge=Boolean(canvas.querySelector('[data-boss-stage="'+edge.from+'"]'));
  const a=canvas.querySelector(stageEdge?'[data-boss-stage="'+edge.from+'"]':'[data-boss-node="'+edge.from+'"]');
  const b=canvas.querySelector(stageEdge?'[data-boss-stage="'+edge.to+'"]':'[data-boss-node="'+edge.to+'"]');
  if(!a||!b)throw Error("UNROUTED_EDGE:"+edge.from+"->"+edge.to);
  const p=anchor(a.getBoundingClientRect(),canvas),q=anchor(b.getBoundingClientRect(),canvas);
  let d, labelX,labelY;
  if(stageEdge){
    const y=Math.min(p.top+250,p.bottom-45);
    const x1=p.right+3,x2=q.left-3;
    d="M "+x1+" "+y+" L "+x2+" "+y;
    labelX=(x1+x2)/2;labelY=y-62;
  }else if(q.cy > p.cy+20){
    // Downward flow; branch fan-out keeps distinct destination targets.
    const x1=p.cx,y1=p.bottom,x2=q.cx,y2=q.top;
    const mid=y1+(y2-y1)*0.52;
    d="M "+x1+" "+y1+" L "+x1+" "+mid+" L "+x2+" "+mid+" L "+x2+" "+(y2-6);
    labelX=(x1+x2)/2+7;labelY=Math.min(mid+4,y2-23);
  }else {
    // A return edge loops outside the node bounds; never disguise a cycle.
    const loopX=Math.max(p.right,q.right)+19;
    d="M "+p.right+" "+p.cy+" L "+loopX+" "+p.cy+" L "+loopX+" "+q.cy+" L "+(q.right+5)+" "+q.cy;
    labelX=loopX+1;labelY=(p.cy+q.cy)/2-14;
  }
  return {...edge,d,labelX,labelY,stageEdge,
    color:highlight(edge.label||"", "")?"magenta":((edge.label||"")==="No"?"magenta":"cyan")};
}
export function BossFlowDiagram({model}) {
  const canvas=useRef(null);
  const [paths,setPaths]=useState([]);
  useLayoutEffect(()=>{
    const measure=()=>{
      if(!canvas.current)return;
      setPaths(model.edges.map(edge=>wireEdge(edge,canvas.current)));
    };
    measure();
    window.addEventListener("resize",measure);
    return()=>window.removeEventListener("resize",measure);
  },[model]);
  if(model.format!=="boss-restricted-mermaid-flowchart-v1")throw Error("INVALID_FLOW_IR");
  return <div data-boss-composer="flow" data-edges-ready={paths.length===model.edges.length}
    data-source-hash={model.sourceSha256} ref={canvas} className="boss-flow">
    <div className="boss-flow-columns">
      {model.groups.map((group,i)=><BossStage key={group.id} group={group} model={model} index={i}/>)}
    </div>
    <svg className="boss-flow-wires" aria-hidden="true">
      <defs>
        <marker id="boss-tip-cyan" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 0 L 8 4 L 0 8 z" fill="#00BCEB"/>
        </marker>
        <marker id="boss-tip-magenta" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 0 L 8 4 L 0 8 z" fill="#E30074"/>
        </marker>
      </defs>
      {paths.map((p,i)=><path key={i} data-boss-edge={p.from+"->"+p.to}
        d={p.d} stroke={p.color==="magenta"?"#E30074":"#00BCEB"}
        strokeWidth="2.5" fill="none" markerEnd={"url(#boss-tip-"+p.color+")"}/>)}
    </svg>
    {paths.filter(p=>p.label).map((p,i)=><span key={i}
      data-boss-edge-label={p.from+"->"+p.to}
      className={"boss-edge-label "+(p.color==="magenta"?"boss-edge-label--magenta":"")}
      style={{left:p.labelX,top:p.labelY}}>{p.label}</span>)}
  </div>;
}
function BossActor({actor}) {
  return <div data-boss-actor={actor.id} className="boss-actor">
    <div className="boss-actor-icon">{actor.kind==="actor"?"◉":"▣"}</div>
    <span className="boss-actor-label">{actor.label}</span>
  </div>;
}
function SequenceMessage({item,actors,index}) {
  const a=actors.findIndex(x=>x.id===item.from),b=actors.findIndex(x=>x.id===item.to);
  if(a<0||b<0)throw Error("UNKNOWN_SEQUENCE_PARTICIPANT");
  const start=12.5+a*25,end=12.5+b*25;
  const x1=start+"%",x2=end+"%";
  const left=Math.min(start,end),span=Math.abs(start-end);
  const isHold=/\bHOLD\b|missing/i.test(item.label);
  return <div className={"boss-seq-message "+(isHold?"boss-seq-message--hold":"")}
      data-boss-message={index} data-from={item.from} data-to={item.to} data-branch={item.branch}>
    <div data-boss-native-label={index} className="boss-seq-message-label"
      style={{left:(left+1)+"%",width:Math.max(span-2,23)+"%"}}>
      <span className="boss-seq-message-number">{String(index).padStart(2,"0")}</span>
      {item.label}
    </div>
    <svg className="boss-seq-message-arrow" aria-hidden="true" preserveAspectRatio="none">
      <defs><marker id={"seq-tip-"+index} markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M 0 0 L 8 4 L 0 8 z" fill={isHold?"#E30074":"#00BCEB"}/>
      </marker></defs>
      <line x1={x1} y1="35" x2={x2} y2="35"
        stroke={isHold?"#E30074":"#00BCEB"}
        strokeWidth="2.5" strokeDasharray={item.reply?"7 4":undefined}
        markerEnd={"url(#seq-tip-"+index+")"}/>
    </svg>
  </div>;
}
export function BossSequenceDiagram({model}) {
  if(model.format!=="boss-restricted-plantuml-sequence-v1")throw Error("INVALID_SEQUENCE_IR");
  let messageIndex=0;
  return <div className="boss-sequence" data-boss-composer="sequence"
    data-source-hash={model.sourceSha256}>
    <div className="boss-seq-header">{model.actors.map(a=><BossActor key={a.id} actor={a}/>)}</div>
    <div className="boss-seq-timeline">
      <div className="boss-seq-lifelines" aria-hidden="true">
        {model.actors.map(a=><span key={a.id} className="boss-seq-lifeline"/>)}
      </div>
      {model.items.map((it,i)=>{
        if(it.type==="message"){messageIndex+=1;return <SequenceMessage key={i}
          item={it} actors={model.actors} index={messageIndex}/>;}
        return <div key={i} data-boss-branch={it.type} className={"boss-seq-condition boss-seq-condition--"+it.type}>
          {it.type==="alt"?"ALT · "+it.label:it.type==="else"?"ELSE · "+it.label:"END · CONDITIONAL BRANCH"}
        </div>;
      })}
    </div>
  </div>;
}
