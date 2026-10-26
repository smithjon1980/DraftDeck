#!/usr/bin/env node
import fs from 'node:fs';
const file = process.argv[2];
if (!file) { console.error('usage: node scripts/check-storybook-asset-manifest.mjs manifest.json'); process.exit(2); }
let m;
try { m = JSON.parse(fs.readFileSync(file, 'utf8')); } catch(e) { console.error('HOLD: unreadable manifest',e.message); process.exit(1); }
const errors = [];
const nonempty = v => typeof v === 'string' && v.trim().length > 0;
for (const k of ['candidate_id','source_id','source_digest','story_brief_id','generation_prompt_digest','output_digest']) if (!nonempty(m[k])) errors.push('missing '+k);
if (m.source_status !== 'PINNED') errors.push('source not pinned');
if (!Array.isArray(m.reference_assets) || !m.reference_assets.length) errors.push('reference assets missing');
else for (const a of m.reference_assets) {
  if (!nonempty(a.id)||!nonempty(a.digest)||!['COMPOSITION_ONLY','STYLE_ONLY','CONTENT_APPROVED'].includes(a.approved_scope)) errors.push('invalid scoped reference');
  if (a.approved_scope === 'CONTENT_APPROVED' && (!Array.isArray(a.approved_subjects)||!a.approved_subjects.length)) errors.push('content reference lacks approved subjects');
}
for (const k of ['required_subjects','forbidden_subjects']) if (!Array.isArray(m[k])) errors.push('missing '+k);
const palette = ['#FFFFFF','#00BCEB','#E30074','#000000'];
if (!Array.isArray(m.allowed_palette)|| m.allowed_palette.some(c=>!palette.includes(String(c).toUpperCase()))) errors.push('noncanonical palette');
if (!Array.isArray(m.detected_subjects)) errors.push('detected subjects not reviewed');
else {
  const required=new Set((m.required_subjects||[]).map(x=>String(x).toLowerCase()));
  const forbidden=new Set((m.forbidden_subjects||[]).map(x=>String(x).toLowerCase()));
  for (const s of m.detected_subjects) {
    const key=String(s).toLowerCase();
    if (forbidden.has(key)) errors.push('forbidden subject: '+s);
    if (!required.has(key) && !(m.expressly_approved_extra_subjects||[]).some(x=>String(x).toLowerCase()===key)) errors.push('unapproved extra subject: '+s);
  }
}
if (m.review_status !== 'SUBJECT_REVIEWED') errors.push('subject review incomplete');
if (m.human_approval && (m.human_approval.candidate_digest!==m.output_digest || !nonempty(m.human_approval.scope))) errors.push('approval digest/scope mismatch');
if (errors.length) { for(const e of errors) console.error('HOLD: '+e); process.exit(1); }
console.log('STRUCTURAL PASS ONLY — image inspection and human release still required');
