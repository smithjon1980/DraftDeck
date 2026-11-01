// Synthetic-only regression suite. NO approved manuscript, credentials, or genuine approval receipts.
import test from "node:test";
import assert from "node:assert/strict";
import crypto from "node:crypto";
import { validate } from "./validate.mjs";
const hash = s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
const copy = v=>structuredClone(v);
function fixture(stage="SOURCE_ADMISSION") {
  const paragraphs=Array.from({length:25},(_,i)=>{const text="Synthetic training paragraph "+(i+1)+"; this is not an approved manuscript.";return {id:"P"+String(i+1).padStart(3,"0"),text,sha256:hash(text)};});
  const digest=hash(paragraphs.map(x=>x.text).join("\n\n"));
  const m={
    schema:"BOSS-105/1.0",mode:"SYNTHETIC",run_id:"TEST-001",stage,
    source:{repository:"synthetic/repo",path:"test/fixture.md",commit:"a".repeat(40),blob:"b".repeat(40),raw_sha256:"c".repeat(64),canonical_sha256:digest,serialization:"BOSS-PARAGRAPHS/1.0",paragraphs},
    target:{episode:"EP00",section_id:"S01",slide_id:"P001A",profile:"SLIDE_1920x1080",composition_id:"COMPOSITION-001",medium:"PHOTOREALISM",medium_decision_ref:"synthetic/episode-zero-medium"},
    checks:{structural:"NOT_TESTED",editorial:"NOT_TESTED",visual:"NOT_TESTED",adapter:"NOT_TESTED",security:"NOT_TESTED",human_decision:"NOT_TESTED"},
    effects:{external_write:false,payment:false,deployment:false,publication:false},
    narrative:{qualified:false},
    approvals:{},
    anchors:{}
  };
  if(["ART_CANDIDATE","STORY_CANDIDATE","COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(stage))
    m.art=asset("ART","ART-001",digest);
  if(["STORY_CANDIDATE","COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(stage)) {
    m.story=asset("STORY","STORY-001",digest);
    m.approvals.art=approval("ART",m.art,m);
  }
  if(["COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(stage)) {
    m.approvals.story=approval("STORY",m.story,m);
    m.narrative={qualified:true,qualification_ref:"synthetic/narrative"};
    m.anchors={opener:"SYNTHETIC_QUALIFIED",closer:"SYNTHETIC_QUALIFIED"};
    m.composition={native_html_text:true,exact_copy_proved:true,react_tailwind:true,layout_variant:"Hero illustration + analytical rail"};
  }
  return m;
}
function asset(kind,id,digest) {
  return {id,kind,sha256:hash(kind+id),preview_sha256:hash(kind+id+"preview"),
    source_digest:digest,provenance_ref:"synthetic/asset",story_brief_ref:"synthetic/brief",
    width:1672,height:941,isolated:true,embedded_cad:false,embedded_text:false,
    embedded_logo:false,composited:false,duplicates_art:false,causal_story_visible_without_labels:true,
    photorealistic:true,represents_proposed_facility:true,implies_completed_or_authorized_facility:false};
}
function approval(kind,c,m) {
  return {test_only:true,gate:kind,candidate_id:c.id,candidate_sha256:c.sha256,
    preview_sha256:c.preview_sha256,source_digest:m.source.canonical_sha256,
    target_id:m.target.slide_id,profile:m.target.profile,composition_id:m.target.composition_id,
    event_id:"SYNTHETIC-EVENT-"+kind,ledger_ref:"test-only/"+kind,actor:"SYNTHETIC_TEST"};
}
function verify(label,stage,change,expectedStatus,code) {
  test(label,()=>{
    const m=fixture(stage);change(m);
    const result=validate(m);
    assert.equal(result.status,expectedStatus,JSON.stringify(result));
    if(code) assert.ok([...result.errors,...result.holds].includes(code),JSON.stringify(result));
  });
}
verify("synthetic source admission PASS","SOURCE_ADMISSION",()=>{},"PASS");
verify("synthetic isolated ART PASS","ART_CANDIDATE",()=>{},"PASS");
verify("synthetic independent STORY PASS","STORY_CANDIDATE",()=>{},"PASS");
verify("synthetic bounded composition PASS","COMPOSITION_CANDIDATE",()=>{},"PASS");
verify("release always requires external human authority","RELEASE_CANDIDATE",()=>{},"HOLD","HUMAN_RELEASE_AUTHORITY_EXTERNAL");
verify("real-source readback cannot self-certify","SOURCE_ADMISSION",m=>{m.mode="REAL";},"HOLD","REAL_SOURCE_READBACK_NOT_INDEPENDENTLY_VERIFIED");
verify("real ART cannot self-certify visual acceptance","ART_CANDIDATE",m=>{m.mode="REAL";},"HOLD","HUMAN_VISUAL_REVIEW_NOT_ATTESTED");
verify("late terminal P025 absent","SOURCE_ADMISSION",m=>{m.source.paragraphs.pop();},"FAIL","PARAGRAPH_COUNT");
verify("wrong paragraph numbering","SOURCE_ADMISSION",m=>{m.source.paragraphs[24].id="P026";},"FAIL","PARAGRAPH_ORDER_P025");
verify("duplicate paragraph ID","SOURCE_ADMISSION",m=>{m.source.paragraphs[1].id="P001";},"FAIL","PARAGRAPH_DUPLICATE_P001");
verify("paragraph byte change","SOURCE_ADMISSION",m=>{m.source.paragraphs[0].text+=" altered";},"FAIL","PARAGRAPH_HASH_P001");
verify("canonical digest mismatch","SOURCE_ADMISSION",m=>{m.source.canonical_sha256="0".repeat(64);},"FAIL","CANONICAL_READBACK_MISMATCH");
verify("different canonical serialization version","SOURCE_ADMISSION",m=>{m.source.serialization="unversioned";},"FAIL","SOURCE_SERIALIZATION");
verify("reject path traversal","SOURCE_ADMISSION",m=>{m.source.path="../secrets.txt";},"FAIL","SOURCE_PATH_ESCAPE");
verify("reject Windows path escape","SOURCE_ADMISSION",m=>{m.source.path="C:\\Windows\\system.ini";},"FAIL","SOURCE_PATH_ESCAPE");
verify("reject malicious paragraph CR change","SOURCE_ADMISSION",m=>{m.source.paragraphs[0].text="a\r\nb";},"FAIL","PARAGRAPH_TEXT_P001");
verify("reject wrong Git blob kind","SOURCE_ADMISSION",m=>{m.source.blob="0".repeat(64);},"FAIL","SOURCE_BLOB");
verify("reject unknown stage","SOURCE_ADMISSION",m=>{m.stage="AUTO_PUBLISH";},"FAIL","STAGE_UNKNOWN");
verify("reject unscoped profile","ART_CANDIDATE",m=>{m.target.profile="ALL_FORMATS";},"FAIL","PROFILE");
verify("reject missing episode-specific medium decision","ART_CANDIDATE",m=>{m.target.medium_decision_ref="";},"FAIL","MEDIUM_DECISION_MISSING");
verify("Episode 01 photo medium is not silently admitted","ART_CANDIDATE",m=>{m.target.episode="EP01";},"FAIL","EP01_MEDIUM_CONFLICT");
verify("reject ART mixed with CAD","ART_CANDIDATE",m=>{m.art.embedded_cad=true;},"FAIL","LAYER_CONTAMINATION");
verify("reject ART with embedded text","ART_CANDIDATE",m=>{m.art.embedded_text=true;},"FAIL","LAYER_CONTAMINATION");
verify("reject ART with embedded logo","ART_CANDIDATE",m=>{m.art.embedded_logo=true;},"FAIL","LAYER_CONTAMINATION");
verify("reject mismatched ART medium","ART_CANDIDATE",m=>{m.art.photorealistic=false;},"FAIL","MEDIUM_ART_MISMATCH");
verify("reject untraceable art","ART_CANDIDATE",m=>{m.art.provenance_ref="";},"FAIL","CANDIDATE_PROVENANCE");
verify("reject missing art source hash","ART_CANDIDATE",m=>{m.art.sha256="no-hash";},"FAIL","CANDIDATE_HASH");
verify("proposed campus must not imply construction","ART_CANDIDATE",m=>{m.art.implies_completed_or_authorized_facility=true;},"FAIL","UNSUPPORTED_CONSTRUCTION_CLAIM");
verify("STORY requires distinct human gate receipt (synthetic test only)","STORY_CANDIDATE",m=>{delete m.approvals.art;},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("STORY cannot reuse ART preview","STORY_CANDIDATE",m=>{m.story.sha256=m.art.sha256;},"FAIL","ART_STORY_SAME_ASSET");
verify("STORY must stand without labels","STORY_CANDIDATE",m=>{m.story.causal_story_visible_without_labels=false;},"FAIL","STORY_SEPARATION");
verify("STORY may not duplicate ART scene","STORY_CANDIDATE",m=>{m.story.duplicates_art=true;},"FAIL","STORY_SEPARATION");
verify("STORY source digest must match approved source","STORY_CANDIDATE",m=>{m.story.source_digest="f".repeat(64);},"FAIL","CANDIDATE_SOURCE_MISMATCH");
verify("wrong target cannot reuse ART approval","STORY_CANDIDATE",m=>{m.approvals.art.target_id="P002A";},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("wrong profile cannot reuse ART approval","STORY_CANDIDATE",m=>{m.approvals.art.profile="PRINT_SEPARATE";},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("wrong composition cannot reuse ART approval","STORY_CANDIDATE",m=>{m.approvals.art.composition_id="other";},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("replay/legacy approval cannot bind to altered candidate","STORY_CANDIDATE",m=>{m.art.sha256=hash("new-art");},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("missing story approval blocks composition","COMPOSITION_CANDIDATE",m=>{delete m.approvals.story;},"FAIL","STORY_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("narrative qualification before composition","COMPOSITION_CANDIDATE",m=>{m.narrative.qualified=false;},"FAIL","NARRATIVE_QUALIFICATION_MISSING");
verify("opener/closer anchors block interior composition","COMPOSITION_CANDIDATE",m=>{m.anchors.closer="NOT_APPROVED";},"FAIL","ANCHOR_APPROVALS_REQUIRED");
verify("native HTML editorial text required","COMPOSITION_CANDIDATE",m=>{m.composition.native_html_text=false;},"FAIL","COMPOSITION_TEXT_CONTRACT");
verify("exact narration requirement","COMPOSITION_CANDIDATE",m=>{m.composition.exact_copy_proved=false;},"FAIL","COMPOSITION_TEXT_CONTRACT");
verify("only seven versioned layouts admitted","COMPOSITION_CANDIDATE",m=>{m.composition.layout_variant="Invented layout";},"FAIL","LAYOUT_VARIANT_NOT_ADMITTED");
verify("consequential effects cannot be bundled into validation","SOURCE_ADMISSION",m=>{m.effects.external_write=true;},"FAIL","CONSEQUENTIAL_EFFECT_REQUESTED");
verify("malformed approval schema cannot infer human authority","STORY_CANDIDATE",m=>{m.approvals.art.actor="AI";},"FAIL","ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
verify("invalid check state rejected","SOURCE_ADMISSION",m=>{m.checks.visual="SURE";},"FAIL","CHECK_STATE_visual");
verify("missing human decision state is not silently passed","SOURCE_ADMISSION",m=>{delete m.checks.human_decision;},"FAIL","CHECK_STATE_human_decision");
test("manifest input immutability",()=>{const m=fixture("STORY_CANDIDATE");const before=JSON.stringify(m);validate(m);assert.equal(JSON.stringify(m),before);});

