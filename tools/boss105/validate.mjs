#!/usr/bin/env node
// BOSS-105 synthetic gate validator. No writes, external calls, or authority grants.
// Node.js 24+; stdlib only. This checks structure, NOT human authenticity or image quality.
import fs from "node:fs";
import crypto from "node:crypto";
import path from "node:path";
import { pathToFileURL } from "node:url";

const HEX64 = /^[0-9a-f]{64}$/;
const HEX40 = /^[0-9a-f]{40}$/;
const STATES = new Set(["PASS", "FAIL", "HOLD", "NOT_TESTED"]);
const STAGES = new Set(["SOURCE_ADMISSION", "NARRATIVE_QUALIFICATION", "ART_CANDIDATE", "STORY_CANDIDATE", "COMPOSITION_CANDIDATE", "RELEASE_CANDIDATE"]);
const PROFILES = new Set(["SLIDE_1920x1080", "WEB_REFLOW", "PRINT_SEPARATE"]);
const sha256 = (value) => crypto.createHash("sha256").update(Buffer.from(value, "utf8")).digest("hex");
const isHex64 = (v) => typeof v === "string" && HEX64.test(v);
const isNonempty = (v) => typeof v === "string" && v.trim().length > 0;
function safeRelative(p) {
  if (!isNonempty(p) || p.includes("\\") || p.includes("\0") || /[\r\n]/.test(p)) return false;
  if (p.startsWith("/") || /^[A-Za-z]:/.test(p)) return false;
  const parts = p.split("/");
  return parts.every((x) => x !== ".." && x !== "." && x !== "");
}
function validCandidate(c, kind, digest, errors) {
  if (!c || typeof c !== "object") { errors.push("CANDIDATE_MISSING"); return; }
  if (!isNonempty(c.id) || !/^[A-Z0-9][A-Z0-9._-]+$/.test(c.id)) errors.push("CANDIDATE_ID");
  if (c.kind !== kind) errors.push("CANDIDATE_KIND");
  if (!isHex64(c.sha256) || !isHex64(c.preview_sha256)) errors.push("CANDIDATE_HASH");
  if (c.source_digest !== digest) errors.push("CANDIDATE_SOURCE_MISMATCH");
  if (!isNonempty(c.provenance_ref) || !isNonempty(c.story_brief_ref)) errors.push("CANDIDATE_PROVENANCE");
  if (!Number.isInteger(c.width) || c.width < 100 || !Number.isInteger(c.height) || c.height < 100) errors.push("CANDIDATE_DIMENSIONS");
  if (c.isolated !== true || c.embedded_cad === true || c.embedded_text === true || c.embedded_logo === true || c.composited === true) errors.push("LAYER_CONTAMINATION");
  if (kind === "STORY" && (c.duplicates_art === true || c.causal_story_visible_without_labels !== true)) errors.push("STORY_SEPARATION");
  if (c.represents_proposed_facility === true && c.implies_completed_or_authorized_facility === true) errors.push("UNSUPPORTED_CONSTRUCTION_CLAIM");
}
function checkSyntheticApproval(a, kind, manifest, candidate) {
  const t = manifest.target;
  return a && a.test_only === true && a.gate === kind
    && a.candidate_id === candidate?.id && a.candidate_sha256 === candidate?.sha256
    && a.preview_sha256 === candidate?.preview_sha256
    && a.source_digest === manifest.source.canonical_sha256
    && a.target_id === t.slide_id && a.profile === t.profile
    && a.composition_id === t.composition_id && isNonempty(a.event_id)
    && isNonempty(a.ledger_ref) && a.actor === "SYNTHETIC_TEST";
}
export function validate(m) {
  const errors = [], holds = [];
  const add = (condition, code) => { if (!condition) errors.push(code); };
  if (!m || typeof m !== "object" || Array.isArray(m)) return { status:"FAIL", errors:["MALFORMED_MANIFEST"], holds:[] };
  add(m.schema === "BOSS-105/1.0", "SCHEMA_VERSION");
  add(m.mode === "SYNTHETIC" || m.mode === "REAL", "RUN_MODE");
  add(STAGES.has(m.stage), "STAGE_UNKNOWN");
  add(isNonempty(m.run_id), "RUN_ID");
  const s = m.source || {};
  add(isNonempty(s.repository), "SOURCE_REPOSITORY");
  add(safeRelative(s.path), "SOURCE_PATH_ESCAPE");
  add(typeof s.commit === "string" && HEX40.test(s.commit), "SOURCE_COMMIT");
  add(typeof s.blob === "string" && HEX40.test(s.blob), "SOURCE_BLOB");
  add(isHex64(s.raw_sha256), "SOURCE_RAW_HASH");
  add(s.serialization === "BOSS-PARAGRAPHS/1.0", "SOURCE_SERIALIZATION");
  add(isHex64(s.canonical_sha256), "SOURCE_CANONICAL_HASH");
  const paragraphs = Array.isArray(s.paragraphs) ? s.paragraphs : [];
  add(paragraphs.length === 25, "PARAGRAPH_COUNT");
  const seen = new Set();
  paragraphs.forEach((p, i) => {
    const id = "P" + String(i + 1).padStart(3, "0");
    if (!p || p.id !== id) errors.push("PARAGRAPH_ORDER_" + id);
    if (seen.has(p?.id)) errors.push("PARAGRAPH_DUPLICATE_" + String(p?.id));
    seen.add(p?.id);
    if (!isNonempty(p?.text) || /[\r]/.test(p?.text || "")) errors.push("PARAGRAPH_TEXT_" + id);
    if (!isHex64(p?.sha256) || (typeof p?.text === "string" && p.sha256 !== sha256(p.text))) errors.push("PARAGRAPH_HASH_" + id);
  });
  if (paragraphs.length === 25 && paragraphs.every(p => typeof p?.text === "string")) {
    if (s.canonical_sha256 !== sha256(paragraphs.map(p=>p.text).join("\n\n"))) errors.push("CANONICAL_READBACK_MISMATCH");
  }
  const t = m.target || {};
  add(["EP00", "EP01"].includes(t.episode), "EPISODE");
  add(isNonempty(t.section_id), "SECTION");
  add(isNonempty(t.slide_id), "TARGET_ID");
  add(PROFILES.has(t.profile), "PROFILE");
  add(isNonempty(t.composition_id), "COMPOSITION_ID");
  add(isNonempty(t.medium_decision_ref), "MEDIUM_DECISION_MISSING");
  if (t.episode === "EP01" && t.medium !== "EDITORIAL_ILLUSTRATION") errors.push("EP01_MEDIUM_CONFLICT");
  if (t.episode === "EP00" && !["PHOTOREALISM", "EDITORIAL_ILLUSTRATION"].includes(t.medium)) errors.push("EP00_MEDIUM_UNRESOLVED");
  if (t.episode === "EP00" && !/^P(00[1-9]|01[0-9]|02[0-5])[A-Z]?$/.test(t.slide_id) && !["OPENER","CLOSER"].includes(t.slide_id)) errors.push("EP00_SLIDE_ID");
  const checks = m.checks || {};
  ["editorial","visual","structural","adapter","security","human_decision"].forEach(k=>add(STATES.has(checks[k]), "CHECK_STATE_"+k));
  if (m.effects && Object.values(m.effects).some(x => x === true)) errors.push("CONSEQUENTIAL_EFFECT_REQUESTED");
  if (m.mode === "REAL") {
    holds.push("REAL_SOURCE_READBACK_NOT_INDEPENDENTLY_VERIFIED");
    if (["STORY_CANDIDATE","COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(m.stage)) holds.push("HUMAN_LEDGER_AUTHENTICITY_UNVERIFIED");
  }
  if (["ART_CANDIDATE","STORY_CANDIDATE","COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(m.stage)) {
    const a = m.art;
    validCandidate(a, "ART", s.canonical_sha256, errors);
    if (t.episode === "EP00" && a && a.photorealistic !== (t.medium === "PHOTOREALISM")) errors.push("MEDIUM_ART_MISMATCH");
  }
  if (["STORY_CANDIDATE","COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(m.stage)) {
    if (m.mode === "SYNTHETIC" && !checkSyntheticApproval(m.approvals?.art, "ART", m, m.art)) errors.push("ART_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
    validCandidate(m.story, "STORY", s.canonical_sha256, errors);
    if (m.art?.sha256 === m.story?.sha256) errors.push("ART_STORY_SAME_ASSET");
  }
  if (["COMPOSITION_CANDIDATE","RELEASE_CANDIDATE"].includes(m.stage)) {
    if (m.mode === "SYNTHETIC" && !checkSyntheticApproval(m.approvals?.story, "STORY", m, m.story)) errors.push("STORY_APPROVAL_MISSING_OR_SCOPE_MISMATCH");
    if (m.narrative?.qualified !== true || !isNonempty(m.narrative.qualification_ref)) errors.push("NARRATIVE_QUALIFICATION_MISSING");
    if (t.episode === "EP00" && t.slide_id !== "OPENER" && t.slide_id !== "CLOSER") {
      if (m.anchors?.opener !== "SYNTHETIC_QUALIFIED" || m.anchors?.closer !== "SYNTHETIC_QUALIFIED") errors.push("ANCHOR_APPROVALS_REQUIRED");
    }
    if (m.composition?.native_html_text !== true || m.composition?.exact_copy_proved !== true || m.composition?.react_tailwind !== true) errors.push("COMPOSITION_TEXT_CONTRACT");
    if (!m.composition || !["Hero illustration + analytical rail","Cinematic split + lower process band","Narrative column + MECE dashboard","Executive quadrant + story margins","Integrated story + swimlane","Three-tier evidence lab","Story sequence + systems atlas"].includes(m.composition.layout_variant)) errors.push("LAYOUT_VARIANT_NOT_ADMITTED");
  }
  if (m.stage === "RELEASE_CANDIDATE") holds.push("HUMAN_RELEASE_AUTHORITY_EXTERNAL");
  if (m.mode === "REAL" && m.stage !== "SOURCE_ADMISSION" && m.stage !== "NARRATIVE_QUALIFICATION") holds.push("HUMAN_VISUAL_REVIEW_NOT_ATTESTED");
  return {status: errors.length ? "FAIL" : holds.length ? "HOLD" : "PASS", errors:[...new Set(errors)], holds:[...new Set(holds)],
    dimensions: {structural:errors.length?"FAIL":"PASS", editorial:checks.editorial||"NOT_TESTED",visual:checks.visual||"NOT_TESTED",adapter:checks.adapter||"NOT_TESTED",security:checks.security||"NOT_TESTED",human_decision:checks.human_decision||"NOT_TESTED"},
    note:"A structural PASS on synthetic data does not authenticate human approval, validate visual quality, admit real source or authorize release."};
}
const invoked = process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href;
if (invoked) {
  const file = process.argv[2];
  if (!file) { console.error("Usage: node tools/boss105/validate.mjs MANIFEST.json"); process.exit(2); }
  let manifest;
  try { manifest = JSON.parse(fs.readFileSync(file, "utf8")); }
  catch (err) { console.log(JSON.stringify({status:"FAIL",errors:["INPUT_READ_OR_PARSE"],message:String(err)})); process.exit(2); }
  const result = validate(manifest);
  console.log(JSON.stringify(result, null, 2));
  process.exit(result.status === "PASS" ? 0 : result.status === "HOLD" ? 3 : 2);
}
