#!/usr/bin/env node
import assert from 'node:assert/strict';
import {inspect,PALETTE,SEVEN,CONTRACT} from './check_handoff.mjs';
const h=c=>c.repeat(64), s=h('a'),art=h('b'), story=h('c'),pv1=h('d'),pv2=h('e');
const SECTION='BOSS.EP00.A01.S01';
const target = {kind:'SLIDE',section_id:SECTION,target_id:SECTION+'.OPEN',
 composition_id:'S01-OPEN-COMPOSITION-01',profile:'SLIDE_1920X1080',
 layout_variant:'ANCHOR',source_digest:s,paragraph_ids:[]};
const approved=(layer,digest,pvdigest,t,candidate)=>({
 status:'APPROVED',layer_candidate_id:layer,sha256:digest,preview_sha256:pvdigest,
 human_record_ref:'restricted-ledger/'+layer,composition_candidate_id:candidate,
 binding:structuredClone(t)
});
const base={contract:CONTRACT,candidate_id:'S01-OPEN-FIGMA-A',mode:'LAYOUT_STUDY',status:'CANDIDATE',
 profile:'SLIDE_1920X1080',source:{id:SECTION,revision:'v0.7',digest:s},
 references:[{id:'ref-five',sha256:h('f'),scope:'COMPOSITION_ONLY'}],tokens:{...PALETTE},
 layout_variant:'ANCHOR',target:structuredClone(target),rollout:{phase:'ANCHORS'},
 figma:{file_key:null,frame_nodes:[]},layers:{},approvals:{},tests:{},
 release_authorized:false,paid_generation_requested:false};
const clone=()=>structuredClone(base);
const ready=()=>{
 const o=clone();o.status='HANDOFF_READY';o.mode='COMPOSITION_HANDOFF';
 o.figma={file_key:'test-figma-file',frame_nodes:['1:2']};
 o.layers={art:{candidate_id:'A-1',sha256:art,preview_sha256:pv1},
 story:{candidate_id:'S-1',sha256:story,preview_sha256:pv2}};
 o.approvals={art:approved('A-1',art,pv1,o.target,o.candidate_id),
 story:approved('S-1',story,pv2,o.target,o.candidate_id),
 design:{status:'APPROVED_FOR_NEXT_GATE',human_record_ref:'restricted-ledger/composition',
 composition_candidate_id:o.candidate_id,binding:structuredClone(o.target)}};
 o.tests=Object.fromEntries(['token_parity','reference_comparison','source_copy_parity'].map(k=>[k,{status:'PASS',evidence_ref:'test-only/'+k}]));
 return o;
};
let assertions=0;
function passes(label,obj){assert.deepEqual(inspect(obj),[],label);assertions++;}
function fails(label,obj){const findings=inspect(obj);assert.ok(findings.length,label);assertions++;}
function failsWith(label,obj,needle){const findings=inspect(obj);assert.ok(findings.some(f=>f.includes(needle)),label+': '+JSON.stringify(findings));assertions++;}
function mutation(f){const m=ready();f(m);return m;}
passes('uncomposed anchor study does not need art approval',base);
passes('structurally coherent composed anchor candidate',ready());
fails('V1 cannot be promoted',mutation(m=>m.contract='BOSS-FIGMA-BRIDGE-V1'));
fails('mismatched art target',mutation(m=>m.approvals.art.binding.target_id=SECTION+'.CLOSE'));
fails('mismatched story composition',mutation(m=>m.approvals.story.binding.composition_id='other'));
fails('mismatched art source digest',mutation(m=>m.approvals.art.binding.source_digest=h('f')));
fails('mismatched story candidate',mutation(m=>m.approvals.story.composition_candidate_id='other'));
fails('mismatched art candidate ID',mutation(m=>m.approvals.art.layer_candidate_id='other'));
fails('mismatched art asset hash',mutation(m=>m.layers.art.sha256=h('f')));
fails('mismatched story preview',mutation(m=>m.layers.story.preview_sha256=h('f')));
fails('missing approver evidence',mutation(m=>delete m.approvals.story.human_record_ref));
fails('reused art/story approval ref',mutation(m=>m.approvals.story.human_record_ref=m.approvals.art.human_record_ref));
fails('mismatched target profile',mutation(m=>m.target.profile='SEVEN_PRINT_17X11'));
fails('missing source digest',mutation(m=>m.source.digest='unknown'));
fails('palette drift',mutation(m=>m.tokens.cyan='#00B0FF'));
fails('invented layout',mutation(m=>{m.layout_variant='MYSTERY';m.target.layout_variant='MYSTERY';}));
fails('missing reference',mutation(m=>m.references=[]));
fails('self-authorized release',mutation(m=>m.release_authorized=true));
fails('unapproved paid generation',mutation(m=>m.paid_generation_requested=true));
fails('missing test evidence reference',mutation(m=>m.tests.source_copy_parity.evidence_ref=''));
const anchorApproved=()=>[
 {target_id:SECTION+'.OPEN',source_digest:s,status:'APPROVED_FOR_NEXT_GATE',human_record_ref:'restricted-ledger/anchor-open'},
 {target_id:SECTION+'.CLOSE',source_digest:s,status:'APPROVED_FOR_NEXT_GATE',human_record_ref:'restricted-ledger/anchor-close'}
];
const interior=()=>{let m=ready();m.target.target_id=SECTION+'.P001';m.target.paragraph_ids=['P001'];m.target.composition_id='P001-COMP-A';m.target.layout_variant=SEVEN[0];m.layout_variant=SEVEN[0];m.rollout={phase:'INTERIOR',anchor_approvals:anchorApproved()};for(const l of ['art','story','design'])m.approvals[l].binding=structuredClone(m.target);return m;};
passes('interior can proceed after both explicit anchors',interior());
let x=interior();delete x.rollout.anchor_approvals[1].human_record_ref;fails('no P001 before both anchors approved',x);
x=interior();x.target.paragraph_ids=['P002'];fails('incorrect paragraph target',x);
x=interior();x.rollout.phase='ANCHORS';fails('interior cannot masquerade as anchor qualification',x);
const web=()=>{const m=ready();m.figma.frame_nodes=['1:1','1:2','1:3'];m.mode='WEB_COMPONENT_SPEC';m.profile='WEB_RESPONSIVE';m.layout_variant='WEB_NATIVE';m.rollout={phase:'WEB'};
 m.target={kind:'WEB_SCREEN',section_id:'BOSS.WEB.MAIN_STREET_COPY',target_id:'BOSS.WEB.MAIN_STREET_COPY.ORDER_INTAKE',composition_id:'MSC-ORDER-IN-A',profile:'WEB_RESPONSIVE',layout_variant:'WEB_NATIVE',source_digest:s,paragraph_ids:[]};m.source.id=m.target.section_id;
 m.approvals.design.binding=structuredClone(m.target);
 m.web_viewports=[
 {name:'mobile',min_width_px:0,max_width_exclusive_px:768,tested_width_px:390,frame_node_id:'1:1'},
 {name:'tablet',min_width_px:768,max_width_exclusive_px:1200,tested_width_px:1024,frame_node_id:'1:2'},
 {name:'desktop',min_width_px:1200,max_width_exclusive_px:null,tested_width_px:1440,frame_node_id:'1:3'}
 ];
 m.web_design_evidence=Object.fromEntries(['responsive_reflow','keyboard_navigation','focus_visibility','accessibility_review','english_expansion','spanish_expansion','interaction_states'].map(k=>[k,{status:'PASS',evidence_ref:'private/test/'+k}]));return m;};
passes('3 breakpoint ranges + bilingual/keyboard/focus evidence declared',web());
x=web();x.web_viewports[1].min_width_px=780;fails('web gap/overlap',x);
x=web();x.web_viewports[2].frame_node_id='1:2';fails('duplicate frames',x);
x=web();x.web_viewports[1].tested_width_px=700;fails('out of range viewport test',x);
x=web();x.web_design_evidence.spanish_expansion.status='NOT_TESTED';fails('Spanish expansion not demonstrated',x);
x=web();delete x.web_design_evidence.focus_visibility;fails('keyboard focus gate missing',x);
x=web();x.web_design_evidence.accessibility_review.evidence_ref='';fails('accessibility evidence missing',x);
// Three v0.3 regression probes. Keep ALL unrelated approval bindings valid so
// each negative test isolates its intended fail-closed rule.
x=interior();
x.target.target_id=SECTION+'.P999';x.target.paragraph_ids=['P999'];
for(const layer of ['art','story','design'])x.approvals[layer].binding=structuredClone(x.target);
failsWith('P999 outside Section 01 P001-P025 must fail',x,'unknown section slide target');
x=web();x.figma.frame_nodes=['1:2'];
failsWith('web viewport nodes must all belong to declared Figma frames',x,'viewport Figma frame not declared');
x=interior();x.rollout.anchor_approvals[1].human_record_ref=x.rollout.anchor_approvals[0].human_record_ref;
failsWith('opener and closer require distinct human approval records',x,'opener and closer must have distinct');
console.log(`PASS: ${assertions} synthetic structural assertions. Human authentication, pixel fidelity, browser functionality and release NOT TESTED.`);
