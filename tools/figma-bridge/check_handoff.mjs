#!/usr/bin/env node
// Static, public-safe structural checker. Does NOT inspect actual Figma pixels,
// authenticate human approvers, certify React parity, or authorize release.
import fs from 'node:fs';

export const EXACT_PALETTE = Object.freeze({
  white: '#FFFFFF', ink: '#000000', cyan: '#00BCEB', magenta: '#E30074'
});
export const SEVEN = Object.freeze([
  'Hero illustration + analytical rail',
  'Cinematic split + lower process band',
  'Narrative column + MECE dashboard',
  'Executive quadrant + story margins',
  'Integrated story + swimlane',
  'Three-tier evidence lab',
  'Story sequence + systems atlas'
]);
const SHA = /^[a-f0-9]{64}$/i;
const modes = ['LAYOUT_STUDY','COMPOSITION_HANDOFF','WEB_COMPONENT_SPEC'];
const profiles = ['SEVEN_PRINT_17X11','SLIDE_1920X1080','WEB_RESPONSIVE'];

export function inspect(m) {
  const problems = [];
  const fail = message => problems.push(message);
  if (!m || typeof m !== 'object' || Array.isArray(m)) return ['manifest not an object'];
  if (m.contract !== 'BOSS-FIGMA-BRIDGE-V1') fail('wrong contract');
  if (!m.candidate_id || typeof m.candidate_id !== 'string') fail('candidate identity missing');
  if (!modes.includes(m.mode)) fail('unknown mode');
  if (!['CANDIDATE','HANDOFF_READY','REJECTED'].includes(m.status)) fail('invalid status');
  if (!profiles.includes(m.profile)) fail('invalid profile');
  if (m.mode === 'WEB_COMPONENT_SPEC' && m.profile !== 'WEB_RESPONSIVE') fail('web needs responsive profile');
  if (m.mode !== 'WEB_COMPONENT_SPEC' && m.profile === 'WEB_RESPONSIVE') fail('slides cannot use web profile');
  if (!m.source || !m.source.id || !m.source.revision || !SHA.test(m.source.digest || '')) fail('source id/revision/digest missing');
  const refs = m.references;
  if (!Array.isArray(refs) || !refs.length) fail('actual scoped reference assets required');
  else {
    const ids = new Set();
    refs.forEach((r, i) => {
      if (!r || !r.id || !SHA.test(r.sha256 || '') ||
          !['COMPOSITION_ONLY','STYLE_ONLY','CONTENT_APPROVED'].includes(r.scope))
        fail('reference scope/hash invalid at index ' + i);
      if (r?.id && ids.has(r.id)) fail('duplicate reference id');
      if (r?.id) ids.add(r.id);
    });
  }
  for (const [k,v] of Object.entries(EXACT_PALETTE)) if (m.tokens?.[k] !== v) fail('brand token mismatch ' + k);
  if (m.mode !== 'WEB_COMPONENT_SPEC' && ![...SEVEN,'ANCHOR'].includes(m.layout_variant)) fail('unapproved SEVEN layout');
  if (m.release_authorized !== false) fail('Figma bridge must never authorize release');
  if (m.paid_generation_requested === true && m.paid_generation_authorized !== true) fail('paid Figma generation lacks explicit permission');
  if (m.status === 'HANDOFF_READY') {
    if (!m.figma?.file_key || !Array.isArray(m.figma?.frame_nodes) || !m.figma.frame_nodes.length)
      fail('verified Figma file/frame ids missing');
    if (m.tests?.token_parity !== 'PASS' || m.tests?.reference_comparison !== 'PASS' ||
        m.tests?.source_copy_parity !== 'PASS') fail('handoff requires source/reference/token tests');
    if (!m.approvals?.human_design_review_ref) fail('human design selection record missing');
    if (m.mode === 'COMPOSITION_HANDOFF') {
      for (const layer of ['art','story']) {
        const a=m.approvals?.[layer];
        if (!a || a.status !== 'APPROVED' || !SHA.test(a.sha256 || '') || !a.human_record_ref)
          fail(layer + ' separate scoped human approval missing');
      }
    }
    if (m.mode === 'WEB_COMPONENT_SPEC') {
      if (!Array.isArray(m.web_viewports) || m.web_viewports.length < 3) fail('responsive viewport design set missing');
      if (m.tests?.interaction_states !== 'PASS') fail('web interaction specification not examined');
    }
  }
  return problems;
}

if (process.argv[1] && process.argv[1].endsWith('check_handoff.mjs')) {
  try {
    const m=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
    const errors=inspect(m);
    console.log(errors.length ? 'FAIL: ' + errors.join('; ') : 'PASS: structural Figma handoff only; visual/human release NOT TESTED');
    process.exitCode=errors.length ? 1 : 0;
  } catch (err) { console.error('FAIL:',err.message); process.exitCode=2; }
}
