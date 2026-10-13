import { Annotation, StateGraph, START, END } from '@langchain/langgraph';
const allowedTypes=['instructional_pdf','vector_asset','research_report'];
const State=Annotation.Root({
 request:Annotation(),run_id:Annotation(),route:Annotation(),status:Annotation(),evidence:Annotation(),attempts:Annotation(),max_attempts:Annotation(),file_url:Annotation(),error:Annotation(),steps:Annotation()
});
function event(s,step){return [...(s.steps||[]),step];}
export const workers={
  intake:async s=>{
    const r=s.request;
    const good=r&&allowedTypes.includes(r.kind)&&typeof r.title==='string'&&r.title.trim().length>0&&typeof r.source_ref==='string'&&r.source_ref.trim().length>0;
    return {status:good?'ACCEPTED':'HOLD',route:good?r.kind:'invalid',error:good?null:'INVALID_OR_UNAUTHENTICATED_INPUT',steps:event(s,'INTAKE')};
  },
  source:async s=>({status:'SOURCE_CHECKED',steps:event(s,'SOURCE')}),
  design:async s=>({status:'DESIGNED',steps:event(s,'DESIGN')}),
  vector:async s=>({status:'VECTOR_READY',steps:event(s,'VECTOR')}),
  research:async s=>({status:'REPORT_READY',steps:event(s,'RESEARCH')}),
  pdf:async s=>({status:'PDF_CANDIDATE',steps:event(s,'PDF')}),
  verify:async s=>{const valid=!(s.request?.simulate_failure);
    return {status:valid?'VERIFIED':'REJECTED',error:valid?null:'SIMULATED_QA_FAILURE',steps:event(s,'VERIFY')}},
  repair:async s=>({attempts:(s.attempts||0)+1,steps:event(s,'REPAIR'),status:'REPAIRED'}),
  hold:async s=>({status:'HOLD',file_url:null,steps:event(s,'HOLD')}),
  deliver:async s=>({status:'DELIVERY_PENDING_STORAGE',file_url:null,steps:event(s,'DELIVER_PENDING')})
};
const graph=new StateGraph(State).addNode('intake',workers.intake).addNode('source',workers.source).addNode('design',workers.design).addNode('vector',workers.vector).addNode('research',workers.research).addNode('pdf',workers.pdf).addNode('verify',workers.verify).addNode('repair',workers.repair).addNode('hold',workers.hold).addNode('deliver',workers.deliver)
.addEdge(START,'intake')
.addConditionalEdges('intake',s=>s.status==='HOLD'?'hold':'source')
.addConditionalEdges('source',s=>({instructional_pdf:'design',vector_asset:'vector',research_report:'research'})[s.route]||'hold')
.addEdge('design','pdf').addEdge('vector','verify').addEdge('research','verify').addEdge('pdf','verify')
.addConditionalEdges('verify',s=>s.status==='VERIFIED'?'deliver':(s.attempts||0)<(s.max_attempts||0)?'repair':'hold')
.addEdge('repair','verify').addEdge('hold',END).addEdge('deliver',END);
export const workflow=graph.compile();
export async function runRequest(request,{run_id='candidate-001',max_attempts=1}={}){
 return workflow.invoke({request,run_id,attempts:0,max_attempts:Math.max(0,Math.min(2,max_attempts)),steps:[],evidence:[]},{recursionLimit:25});
}
