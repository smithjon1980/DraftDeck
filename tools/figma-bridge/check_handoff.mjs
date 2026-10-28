#!/usr/bin/env node
// BOSS-FIGMA-BRIDGE-V2: public-safe STRUCTURAL GATE ONLY.
// References, approvals and Figma frame IDs must be independently authenticated.
// No pixel inspection, human attestation, art quality, or release authorization.
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {plans} from '../../experiments/episode-zero-seven-phase1/scripts/layouts.mjs';

const contractUrl = new URL('../../design-system/boss-design-contract.json', import.meta.url);
const cssUrl = new URL('../../design-system/tokens/tokens.css', import.meta.url);
const contract = JSON.parse(fs.readFileSync(contractUrl, 'utf8'));
export const PALETTE = Object.freeze({
  white: contract.brand.ground,
  ink: contract.brand.ink,
  cyan: contract.brand.cyan,
  magenta: contract.brand.magenta,
});
export const SEVEN = Object.freeze(plans.map(p => p.name));
export const CONTRACT = 'BOSS-FIGMA-BRIDGE-V2';
const SHA = /^[a-f0-9]{64}$/i;
const MODES = ['LAYOUT_STUDY', 'COMPOSITION_HANDOFF', 'WEB_COMPONENT_SPEC'];
const PROFILES = ['SEVEN_PRINT_17X11', 'SLIDE_1920X1080', 'WEB_RESPONSIVE'];
const NONBLANK = v => typeof v === 'string' && v.trim().length > 0;
const FIELD = ['kind','section_id','target_id','composition_id','profile','layout_variant','source_digest'];
const SECTION = 'BOSS.EP00.A01.S01';
const HAS = (obj, key) => Object.prototype.hasOwnProperty.call(obj || {}, key);
function referenceIdentityMatches(a, b) {
  return !!a && !!b && FIELD.every(k => a[k] === b[k]) &&
    Array.isArray(a.paragraph_ids) && Array.isArray(b.paragraph_ids) &&
    a.paragraph_ids.length === b.paragraph_ids.length &&
    a.paragraph_ids.every((p, i) => p === b.paragraph_ids[i]);
}
function auditTrail(record) {
  return record && NONBLANK(record.human_record_ref);
}
function reportSourceDrift(errors) {
  const css = fs.readFileSync(cssUrl, 'utf8');
  const vars = {white:'--boss-color-ground',ink:'--boss-color-ink',cyan:'--boss-color-brand-cyan',magenta:'--boss-color-brand-magenta'};
  for (const [name, variable] of Object.entries(vars)) {
    const v = css.match(new RegExp('(?:^|\\n)\\s*' + variable + '\\s*:\\s*(#[0-9A-Fa-f]{6})\\s*;', 'm'));
    if (!v || v[1] !== PALETTE[name]) errors.push('authoritative CSS/design contract drift: ' + name);
  }
  if (SEVEN.length !== 7 || new Set(SEVEN).size !== 7) errors.push('SEVEN source must expose exactly seven distinct layout names');
}
function webAudit(m, fail) {
  const vp = m.web_viewports;
  if (!Array.isArray(vp) || vp.length !== 3) { fail('three distinct web breakpoint ranges required'); return; }
  const names = ['mobile','tablet','desktop'];
  const seenNodes = new Set();
  for (let i = 0; i < names.length; i++) {
    const v = vp[i];
    if (!v || v.name !== names[i]) { fail('viewport order must be mobile, tablet, desktop'); continue; }
    const min = v.min_width_px, max = v.max_width_exclusive_px;
    if (!Number.isInteger(min) || min < 0 ||
       (i < 2 && (!Number.isInteger(max) || max <= min)) ||
       (i === 2 && max !== null)) fail('invalid distinct breakpoint range: '+names[i]);
    if (i === 0 && min > 320) fail('mobile range must cover width 320px');
    if (i > 0 && vp[i - 1]?.max_width_exclusive_px !== min) fail('web breakpoint gap or overlap');
    if (!Number.isInteger(v.tested_width_px) || v.tested_width_px < min ||
        (max !== null && v.tested_width_px >= max)) fail('web test width outside breakpoint: '+names[i]);
    if (!NONBLANK(v.frame_node_id) || seenNodes.has(v.frame_node_id)) fail('duplicate/missing viewport Figma frame');
    else if (!Array.isArray(m.figma?.frame_nodes) || !m.figma.frame_nodes.includes(v.frame_node_id))
      fail('viewport Figma frame not declared in figma.frame_nodes: ' + names[i]);
    seenNodes.add(v.frame_node_id);
  }
  // These prove evidence declarations at design-spec stage, not actual browser accessibility.
  for (const name of ['responsive_reflow','keyboard_navigation','focus_visibility',
                      'accessibility_review','english_expansion','spanish_expansion','interaction_states']) {
    const check = m.web_design_evidence?.[name];
    if (!check || check.status !== 'PASS' || !NONBLANK(check.evidence_ref))
      fail('missing web design evidence: ' + name);
  }
}

export function inspect(m) {
  const errors = [];
  const fail = s => errors.push(s);
  if (!m || typeof m !== 'object' || Array.isArray(m)) return ['manifest not an object'];
  reportSourceDrift(errors);
  if (m.contract !== CONTRACT) fail('V1 manifests cannot be promoted; migrate to BOSS-FIGMA-BRIDGE-V2');
  if (!NONBLANK(m.candidate_id)) fail('candidate_id missing');
  if (!MODES.includes(m.mode)) fail('invalid mode');
  if (!['CANDIDATE','REJECTED','HANDOFF_READY'].includes(m.status)) fail('invalid status');
  if (!PROFILES.includes(m.profile)) fail('invalid profile');
  if (m.mode === 'WEB_COMPONENT_SPEC' && m.profile !== 'WEB_RESPONSIVE') fail('web mode needs responsive profile');
  if (m.mode !== 'WEB_COMPONENT_SPEC' && m.profile === 'WEB_RESPONSIVE') fail('slide mode cannot use web profile');
  if (!NONBLANK(m.source?.id) || !NONBLANK(m.source?.revision) || !SHA.test(m.source?.digest || '')) fail('source ID, revision, digest missing');
  if (!Array.isArray(m.references) || m.references.length === 0) fail('scoped reference hashes missing');
  else {
    const ids = new Set();
    for (const r of m.references) {
      if (!NONBLANK(r?.id) || !SHA.test(r?.sha256 || '') || !['COMPOSITION_ONLY','STYLE_ONLY','CONTENT_APPROVED'].includes(r?.scope)) fail('invalid reference identity, digest or scope');
      if (ids.has(r?.id)) fail('duplicate reference id');
      ids.add(r?.id);
    }
  }
  for (const [name, hex] of Object.entries(PALETTE)) if (m.tokens?.[name] !== hex) fail('brand token mismatch: ' + name);
  if (m.mode !== 'WEB_COMPONENT_SPEC' && ![...SEVEN,'ANCHOR'].includes(m.layout_variant)) fail('SEVEN source layout does not match');
  if (m.release_authorized !== false) fail('Figma manifest may not authorize release');
  if (m.paid_generation_requested && m.paid_generation_authorized !== true) fail('paid generation not authorized');

  const t = m.target;
  if (!t || FIELD.some(k => !NONBLANK(t[k])) || !Array.isArray(t?.paragraph_ids)) fail('exact target binding missing');
  else {
    if (!t.target_id.startsWith(m.source?.id + '.')) fail('target ID must be within its declared source');
    if (t.section_id !== m.source?.id || t.source_digest !== m.source?.digest ||
        t.profile !== m.profile || t.layout_variant !== m.layout_variant) fail('target != source/profile/layout');
    if (m.mode === 'WEB_COMPONENT_SPEC' && t.kind !== 'WEB_SCREEN') fail('web target kind mismatch');
    if (m.mode !== 'WEB_COMPONENT_SPEC' && t.kind !== 'SLIDE') fail('slide target kind mismatch');
    if (m.mode === 'WEB_COMPONENT_SPEC' && t.paragraph_ids.length !== 0) fail('web cannot inherit slide paragraph IDs');
    if (m.mode !== 'WEB_COMPONENT_SPEC' && t.section_id === SECTION) {
      const anchored = t.target_id === SECTION + '.OPEN' || t.target_id === SECTION + '.CLOSE';
      const paragraphMatch = /^BOSS\.EP00\.A01\.S01\.P(\d{3})$/.exec(t.target_id);
      const interior = !!paragraphMatch && Number(paragraphMatch[1]) >= 1 && Number(paragraphMatch[1]) <= 25;
      if (!anchored && !interior) fail('unknown section slide target');
      if (anchored && t.paragraph_ids.length !== 0) fail('anchor must not masquerade as paragraph slide');
      if (interior && (t.paragraph_ids.length !== 1 || t.paragraph_ids[0] !== t.target_id.split('.').at(-1))) fail('paragraph ID does not match slide target');
      if (!m.rollout || !['ANCHORS','INTERIOR'].includes(m.rollout.phase)) fail('section rollout phase missing');
      else if (anchored && m.rollout.phase !== 'ANCHORS') fail('anchor must be first qualification stage');
      else if (interior) {
        if (m.rollout.phase !== 'INTERIOR') fail('interior slide cannot start anchor qualification');
        const refs=m.rollout.anchor_approvals;
        if (!Array.isArray(refs) || refs.length !== 2 ||
           ![SECTION+'.OPEN',SECTION+'.CLOSE'].every(id=>refs.some(a=>a?.target_id===id && a?.source_digest===m.source.digest && a?.status==='APPROVED_FOR_NEXT_GATE' && NONBLANK(a.human_record_ref))))
          fail('opener and closer acceptance records required before P001–P025');
        if (Array.isArray(refs) && refs.length === 2 &&
            NONBLANK(refs[0]?.human_record_ref) && refs[0].human_record_ref === refs[1]?.human_record_ref)
          fail('opener and closer must have distinct human approval records');
      }
    }
  }
  if (m.status !== 'HANDOFF_READY') return errors;
  if (!NONBLANK(m.figma?.file_key) || !Array.isArray(m.figma?.frame_nodes) ||
      !m.figma.frame_nodes.length || m.figma.frame_nodes.some(n=>!NONBLANK(n))) fail('exact Figma file/frame nodes missing');
  for (const k of ['token_parity','reference_comparison','source_copy_parity']) {
    const v=m.tests?.[k];
    if (v?.status !== 'PASS' || !NONBLANK(v.evidence_ref)) fail('handoff test+evidence missing: ' + k);
  }
  const design = m.approvals?.design;
  if (!auditTrail(design) || !referenceIdentityMatches(design?.binding, t) ||
      design?.composition_candidate_id !== m.candidate_id || design?.status !== 'APPROVED_FOR_NEXT_GATE')
      fail('design review not bound to this candidate and target');
  if (m.mode === 'COMPOSITION_HANDOFF') {
    for (const layer of ['art','story']) {
      const a=m.approvals?.[layer]; const src=m.layers?.[layer];
      if (!auditTrail(a) || a.status !== 'APPROVED' || !SHA.test(a.sha256 || '') ||
          !SHA.test(a.preview_sha256 || '') ||
          a.sha256 !== src?.sha256 || a.preview_sha256 !== src?.preview_sha256 ||
          a.layer_candidate_id !== src?.candidate_id ||
          a.composition_candidate_id !== m.candidate_id ||
          !referenceIdentityMatches(a.binding, t)) fail(layer + ' approval/preview binding mismatch');
    }
    if (m.approvals?.art?.human_record_ref === m.approvals?.story?.human_record_ref) fail('art and story require distinct human review records');
  }
  if (m.mode === 'WEB_COMPONENT_SPEC') webAudit(m, fail);
  return errors;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === fileURLToPath(new URL(process.argv[1], 'file://'))) {
  try {
    const manifest=JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
    const errors=inspect(manifest);
    console.log(errors.length ? 'FAIL: '+errors.join('; ') : 'PASS: STRUCTURAL HANDOFF ONLY; approval authenticity, Figma pixels, React/browser parity and release NOT VERIFIED');
    process.exitCode=errors.length?1:0;
  } catch(e) { console.error('FAIL:',e.message); process.exitCode=2; }
}
