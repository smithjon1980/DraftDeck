/**
 * BOSS -> OpenBot governance policy feasibility pilot.
 * Imports UNMODIFIED upstream source files pinned by workflow SHA and Git blob hashes.
 * No external tools, files, credentials, or real user data are executed.
 * Scope: PURE POLICY/AUTHORIZATION DECISIONS, not gateway DB audit or worker recovery.
 */
import { writeFileSync } from "node:fs";
import { evaluateActionPolicy, type ActionPolicy, type PolicyContext } from
  "./upstream/server/src/computer/policy.ts";
import { decideAction } from "./upstream/server/src/approvals/policy.ts";

const PIN="bd4dc94943a9d62aefd05e5e99073ba58919c9c6";
const cases: {name:string; status:"PASS"|"FAIL"; observed?:unknown; detail?:string}[]=[];
let violations=0;
async function run(name:string, fn:()=>boolean|Promise<boolean>, detail="") {
  try {
    const ok=await fn();
    cases.push({name,status:ok?"PASS":"FAIL",detail});
    if(!ok) violations++;
  } catch(e){
    violations++;
    cases.push({name,status:"FAIL",detail:String(e)});
  }
}
function makeContext(extra:Partial<PolicyContext>={}):PolicyContext{
  return {
    tool:{name:"computer_snapshot"},
    bot:{id:"boss-story-producer"},
    actor:{id:"human-reviewer"},
    page:{url:"",host:""},
    element:{ref:"",role:"",name:""},
    file:{path:"",name:"",extension:""},
    mcp:{server:"",tool:"",effect:""},
    command:"",
    key:"",
    intent:"read",
    initiator:{kind:"person",id:""},
    ...extra
  };
}
const bPolicy:ActionPolicy={
  mode:"enforce",
  deny:[
    'intent == "write_tool"',
    'intent == "run_command"',
    'intent == "activate"',
    'intent == "navigate"',
    'contains(file.path, "approved")',
    'contains(file.path, ".env")',
    'initiator.kind == "routine" && intent == "write_file"'
  ],
  allow:[
    'intent == "read"',
    'intent == "read_file" && file.path == "source/public-brief.txt"',
    'intent == "write_file" && file.path == "candidates/slide02.jsx" && bot.id == "boss-story-producer" && actor.id == "human-reviewer"'
  ]
};
const p=(ctx:Partial<PolicyContext>, policy:ActionPolicy|undefined=bPolicy)=>
 evaluateActionPolicy(policy,makeContext(ctx));
function makeCandidate(
  extra:Partial<{toolRef:string;effect:string;scope:string;args:unknown}>={}
){
  return {
    actorId:"human-reviewer",botId:"boss-story-producer",
    toolRef:"mcp/github/update_file",effect:"write",scope:"DraftDeck/main",
    args:{sample:true},...extra,
  };
}
function makeTeam(behaviour:"allow"|"ask"|"hand_off"|"pre_approved",toolRef:string){
  return {
    id:"boss-team-rule",botId:"boss-story-producer",toolRef,
    scope:"*",effect:"*",behaviour,createdBy:"human-reviewer",
    createdAt:new Date("2026-10-23T00:00:00Z"),revokedAt:null,
  };
}
function makePersonal(behaviour:"allow"|"ask"|"hand_off"|"pre_approved",toolRef:string){
  return {...makeTeam(behaviour,toolRef),id:"boss-personal-rule",ownerUserId:"human-reviewer"};
}
async function approval(
  cand=makeCandidate(),extra:Record<string,unknown>={}
){
  return decideAction({
    candidate:cand,team:[],personal:[],autoReview:false,
    customRulesEnabled:true,askBeforeChanges:true,...extra
  } as Parameters<typeof decideAction>[0]);
}

await run("01_allow_public_spec_read",()=>{
 const d=p({intent:"read",tool:{name:"computer_snapshot"}});
 return d.allowed && d.forward && d.source==="allow";
});
await run("02_allow_exact_candidate_jsx_in_sandbox",()=>{
 const d=p({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"candidates/slide02.jsx",name:"slide02.jsx",extension:"jsx"}});
 return d.allowed && d.forward;
});
await run("03_deny_approved_narration_mutation",()=>{
 const d=p({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"approved/ep01-v6.md",name:"ep01-v6.md",extension:"md"}});
 return !d.allowed&&!d.forward&&d.source==="deny";
});
await run("04_deny_env_secret_file",()=>{
 const d=p({intent:"write_file",file:{path:"candidates/.env",name:".env",extension:"env"}});
 return !d.forward&&d.source==="deny";
});
await run("05_deny_shell_commands",()=>{
 const d=p({intent:"run_command",tool:{name:"computer_run_command"},command:"echo harmless"});
 return !d.forward&&d.source==="deny";
});
await run("06_deny_external_mcp_write_even_if_marked_allowed",()=>{
 const d=p({intent:"write_tool",tool:{name:"mcp__github__merge"},mcp:{server:"github",tool:"merge",effect:"write"}});
 return !d.forward&&d.source==="deny";
});
await run("07_deny_browser_publish_click",()=>{
 const d=p({intent:"activate",tool:{name:"computer_click"},element:{ref:"e22",role:"button",name:"Publish"}});
 return !d.forward&&d.source==="deny";
});
await run("08_deny_enter_key_activation_bypass",()=>{
 const d=p({intent:"activate",tool:{name:"computer_key"},key:"Enter"});
 return !d.forward&&d.source==="deny";
});
await run("09_deny_scheduled_candidate_write",()=>{
 const d=p({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"candidates/slide02.jsx",name:"slide02.jsx",extension:"jsx"},initiator:{kind:"routine",id:"nightly"}});
 return !d.forward&&d.source==="deny";
});
await run("10_allow_scheduled_read",()=>{
 const d=p({intent:"read",initiator:{kind:"routine",id:"nightly"}});
 return d.allowed && d.forward;
});
await run("11_missing_policy_default_deny",()=>{
 const d=evaluateActionPolicy(undefined,makeContext({intent:"read"}));
 return !d.forward&&!d.allowed&&d.source==="default";
});
await run("12_broken_deny_expression_fails_closed",()=>{
 const d=p({intent:"read"},{mode:"enforce",allow:["true"],deny:["invalid CEL ((("]});
 return !d.forward&&!d.allowed&&d.source==="deny";
});
await run("13_deny_rule_overrides_allow_everything",()=>{
 const d=p({intent:"write_tool"},{mode:"enforce",allow:["true"],deny:['intent == "write_tool"']});
 return !d.forward&&!d.allowed&&d.source==="deny";
});
await run("14_unknown_action_default_denied",()=>{
 const d=p({intent:"list_files",tool:{name:"computer_list_files"}});
 return !d.forward&&!d.allowed&&d.source==="default";
});
await run("15_DRY_RUN_IS_NOT_ENFORCEMENT",()=>{
 const d=p({intent:"write_tool"},{...bPolicy,mode:"dry-run"});
 return !d.allowed && d.forward && d.mode==="dry-run";
},"PASS means detected risky dry-run forwarding; NEVER use dry-run for production stop.");
await run("16_approval_team_handoff_for_merge",async()=>{
 const d=await approval(makeCandidate({toolRef:"mcp/github/merge_pull_request"}),{
   team:[makeTeam("hand_off","mcp/github/merge_pull_request")],
   personal:[makePersonal("allow","mcp/github/merge_pull_request")]
 });
 return d.behaviour==="hand_off"&&d.source==="team_rule";
});
await run("17_approval_ask_before_write",async()=>{
 const d=await approval();
 return d.behaviour==="ask"&&d.source==="default";
});
await run("18_preapproved_without_review_model_requires_approval",async()=>{
 const d=await approval(makeCandidate({toolRef:"mcp/github/update_file"}),{
   team:[makeTeam("pre_approved","mcp/github/update_file")],
   askBeforeChanges:false
 });
 return d.behaviour==="ask";
});
await run("19_builtin_payment_requires_person",async()=>{
 const d=await approval(makeCandidate({toolRef:"mcp/shop/checkout",effect:"write",scope:"checkout"}),{
   team:[makeTeam("allow","mcp/shop/checkout")],askBeforeChanges:false
 });
 return d.behaviour==="hand_off"&&d.source==="safety";
});
await run("20_stricter_team_ask_defeats_personal_allow",async()=>{
 const d=await approval(makeCandidate({toolRef:"mcp/github/update_file"}),{
   team:[makeTeam("ask","mcp/github/update_file")],
   personal:[makePersonal("allow","mcp/github/update_file")],
   askBeforeChanges:false
 });
 return d.behaviour==="ask"&&d.source==="team_rule";
});
await run("21_approval_missing_model_fails_closed_on_auto_review",async()=>{
 const d=await approval(makeCandidate({toolRef:"mcp/github/update_file"}),{
   autoReview:true,askBeforeChanges:false
 });
 return d.behaviour==="ask"&&d.source==="auto_review";
});
await run("22_unknown_tool_does_not_inherit_candidate_write_grant",()=>{
 const d=p({intent:"write_file",tool:{name:"computer_write_file"},file:{path:"candidates/other.jsx",name:"other.jsx",extension:"jsx"}});
 return !d.forward&&!d.allowed;
});

const result={
 status:violations===0?"POLICY_ISOLATED_PASS":"POLICY_ISOLATED_FAIL",
 upstream:{repository:"https://github.com/CopilotKit/OpenBot",commit:PIN,
       policy:"server/src/computer/policy.ts",approval:"server/src/approvals/policy.ts"},
 dataset:"SYNTHETIC_BOSS_SLIDE_ONLY",cases,total:cases.length,passed:cases.length-violations,
 failed:violations,
 scope:{
  upstream_policy_functions_executed:true,
  approval_decision_functions_executed:true,
  database_audit_records_tested:false,
  real_computer_gateway_tested:false,
  isolated_worker_restart_tested:false,
  live_approval_roundtrip_tested:false,
  real_deployment_made:false,
  production_credentials_used:false,
  OpenDots_evaluated:false
 },
 decision:"EVALUATE_ONLY_NO_ADOPTION"
};
writeFileSync("openbot_governance_results.json",JSON.stringify(result,null,2));
console.log(JSON.stringify({status:result.status,passed:result.passed,total:result.total,failed:result.failed,
  tests:cases.map(c=>({name:c.name,status:c.status,detail:c.detail}))},null,2));
if(violations)process.exitCode=1;
