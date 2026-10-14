import { Annotation, StateGraph, START, END } from "@langchain/langgraph";
import { pathToFileURL } from "node:url";

/** Model-free supervisor trial. Each specialist is a replaceable node; no actual agents or side effects yet. */
const State = Annotation.Root({
  request: Annotation(),
  route: Annotation(),
  plan: Annotation(),
  composition: Annotation(),
  artwork: Annotation(),
  pdf_report: Annotation(),
  evidence: Annotation(),
  decision: Annotation(),
  history: Annotation({ reducer:(old=[],update=[])=>old.concat(update),default:()=>[] }),
});
const supervisor = async (s) => {
  if (!s.request?.id || !s.request?.artifact_type || !s.request?.source_ref)
    return {decision:"HOLD",route:"hold",history:["SUPERVISOR: missing request operands"]};
  const route = s.request.artifact_type === "pdf" ? "requirements" : "hold";
  return {route,decision:route==="hold"?"HOLD":"PENDING",history:[`SUPERVISOR: ${route}`]};
};
const requirements = async(s)=>({plan:{source_ref:s.request.source_ref,required_text:s.request.required_text||[],format:"16:9"},history:["REQUIREMENTS: planned"]});
const design = async(s)=>({composition:{component_model:"React/Puck candidate",text:s.plan.required_text},history:["DESIGN: composition specified"]});
const artwork = async(s)=>({artwork:{mode:"separate story asset",source:"NOT_ESTABLISHED"},history:["ARTWORK: source missing; image production not performed"]});
const verify = async(s)=>{
  const refs=Array.isArray(s.evidence)?s.evidence:[];
  const required=s.plan.required_text;
  const observed=s.request.observed_text||[];
  const missing=required.filter(x=>!observed.includes(x));
  const pass=refs.length>0 && missing.length===0 && s.request.pdf_path_verified===true && s.request.story_asset_verified===true;
  return {decision:pass?"REVIEW_REQUIRED":"HOLD",pdf_report:{missing,has_evidence:refs.length>0,pdf_path_verified:s.request.pdf_path_verified===true,story_asset_verified:s.request.story_asset_verified===true},history:[`VERIFICATION: ${pass?"READY_FOR_HUMAN_REVIEW":"HOLD"}`]};
};
export const graph = new StateGraph(State)
  .addNode("supervisor",supervisor)
  .addNode("requirements",requirements)
  .addNode("design",design)
  .addNode("artwork",artwork)
  .addNode("verify",verify)
  .addEdge(START,"supervisor")
  .addConditionalEdges("supervisor",s=>s.route,{requirements:"requirements",hold:END})
  .addEdge("requirements","design")
  .addEdge("design","artwork")
  .addEdge("artwork","verify")
  .addEdge("verify",END)
  .compile();
export async function run(request,evidence=[]){return graph.invoke({request,evidence});}
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
 const result=await run({id:"TRIAL-001",artifact_type:"pdf",source_ref:"DAY-ZERO-OVERVIEW-01",required_text:["From AI Consumer to Governed Operator."],observed_text:["From AI Consumer to Governed Operator."],pdf_path_verified:false,story_asset_verified:false});
 process.stdout.write(JSON.stringify({decision:result.decision,history:result.history,report:result.pdf_report},null,2)+"\n");
}
