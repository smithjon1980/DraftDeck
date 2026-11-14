# Bioscillate — Day Zero Case Research & Publication Specification v0.3 (CANDIDATE)

**Specification ID:** `BOSS-DZ-CASE-RESEARCH-v0.3`  
**Date:** 2026-11-14 (America/Chicago)  
**Status:** REVIEW CANDIDATE / NO PUBLICATION APPROVAL  
**Scope:** Candidate 009, Revision B, P001 pilot first, then P002–P250 only after human authorization  
**Governance:** HAVE — Human Authority, Verified Execution  
**Predecessor:** `docs/BIOSCILLATE_DAY_ZERO_CASE_RESEARCH_SPEC_v0.2_CANDIDATE.md` (retained unchanged)  
**Evidence pilot:** `reports/day-zero/CANDIDATE-009-2026-11-14/P001_EVIDENCE_QUALIFICATION_REPORT_v0.1.md`

## 1. Responsibilities and control

- **Perplexity is an external research assistant only:** locate original publications, extract precisely located passages, identify limitations, and propose claim-to-evidence mappings for *one supplied paragraph*. It does not control the 250-paragraph manuscript, rewrite editorial material, qualify its own outputs as independently verified, manage GitHub, change specifications, approve scaling or approve publication.
- **Bioscillate editorial/research supervision:** custody of the canonical manuscript and research companions, source screening, independent inspection, evidence classification, corrections and change logs, source-eligibility and readiness recommendations.
- **Human owner/editor:** authoritative editorial judgments, any substantive manuscript revision, scaling decision and final publication/release approval. No model output constitutes this approval.

## 2. Canonical text, counting, and non-regression

- The reference is **Candidate 009 Revision B** in `reports/day-zero/CANDIDATE-009-2026-11-14/BOSS_DAY_ZERO_CANDIDATE_009_250_PARAGRAPHS.md`, on branch `reports/day-zero-candidate-009-20261114`.
- Preserve all 250 numbered narrative paragraphs, exact punctuation and emphasis; 250 companion research packets correspond one-to-one, each reproducing the canonical paragraph verbatim.
- P001 specifically contains the unitalicized first “finished” and the later italicized `*finished*`. Never reconstruct P001 from voice transcripts or Perplexity's output. Compare byte-for-byte against repository text before accepting a packet or annotated copy.
- Scripted dialogues, exhibits, research records and citations are excluded from the 250-paragraph count. SEVEN (P016), PRIME (P052), PARCELS (P076) retain their previously recorded definitions and first anchors.
- Candidate 006 remains historically approved and untouched. Candidate 009 is a review candidate; no publication, production deployment, LMS release, or change to React/Tailwind, Windmill, n8n, Railway, or GitHub Actions follows from this specification.

## 3. Source qualification — DOI OPTIONAL, accuracy REQUIRED

**DOI is optional**, not a quality score. Source selection prioritizes: (a) accessible original publication from publisher/institution, (b) identifiable authorship/title/date or an honest undated designation, (c) specifically located relevant passage/figure/page, (d) method and population when reporting empirical claims, (e) transparent funding, conflicts, and limitations, (f) appropriate sector and claim fit, and (g) reproducible original URL or DOI when present.

Use source states **DISCOVERED → ORIGINAL INSPECTED → CLAIM MAPPED → INDEPENDENTLY VERIFIED → HUMAN ACCEPTED**. Advancement must be documented; source existence or an AI-generated citation never implies independent verification.

Evidence classes: `DIRECT SUPPORT`, `PARTIAL SUPPORT`, `CONTRADICTION`, `INSUFFICIENT EVIDENCE`; separately identify empirical result, theory/mathematical relationship, professional recommendation, and supervisor inference. A credible source can be irrelevant to a particular claim.

For each PNNN, request **up to three distinct quality sources, targeting three**. Preserve the three research positions C1–C3 but record a shortfall if fewer qualify; never invent a third. Multiple direct citations may support one claim, and research slots are not required to become published endnotes. Sources may be replaced only with traceable decisions. An original industry definition is not proof of a prevalence rate or a causal mechanism.

## 4. Research-only Perplexity packet contract

Each independently copyable prompt contains:
1. Candidate/paragraph ID and **canonical verbatim paragraph**.
2. One paragraph-specific question about evidence for real-world operational principles, *not* fictional events.
3. Up to three source targets, with author, title, issuing institution, date, original URL/DOI if any, exact passage/page/section, method/population, sponsor, sector fit, and limitations.
4. A claim-to-source table with evidence class and shortfall/contradiction notes.
5. Optional citation placement suggestions in a second exact-copy annotated version; no alteration to underlying words, order, punctuation or emphasis.
6. **PENDING INDEPENDENT SOURCE VERIFICATION** on every provisional mapping.

Perplexity returns research only. It must never be asked to rewrite the manuscript, create a 250-packet program, run GitHub, decide scaling, approve citations, or choose publication status. Use narrow follow-up tasks to fill identified gaps; do not reboot completed research.

## 5. Publication style (informed by executive research reports, original to Bioscillate)

This is an editorial design decision **inspired by** the separation of narrative, numbered notes/exhibits, and methodology found in McKinsey Global Institute research reports. It is not an endorsement, a certification, or a reproduction of McKinsey's proprietary templates or text.

**Layer 1 — Teaching publication:** readable consulting case and learning sequence; verified claims receive minimal numbered reader-facing notes or endnotes at the relevant position. Do not overload fiction with source markers. Numbered exhibits include title, units, date, source note, invented-versus-real status and caveats.

**Layer 2 — Research companion:** persistent C1/C2/C3 internal IDs, original URLs, exact supporting locations, claim-level evidence register, source snapshots/versions where rights permit, methods, caveats, and contradictions.

**Layer 3 — Methods and governance appendix:** how sources were selected, exclusion rules, access dates, population and sample, assumptions, conflicts, limitations, independent validation, editorial revisions, publication permissions, and human authorization.

Public footnotes/endnotes are generated from **human-accepted** internal IDs; internal C1/C2/C3 placeholders are never printed as approved references. No invented quotation, sample statistic, pagination, DOI or figure label.

## 6. P001 pilot acceptance (HOLD until cleared)

- Match both original and research-copy paragraph to the exact GitHub P001, including `001.`, punctuation, and the later `*finished*`.
- Review **Factory Physics** from its actual chapter text, not merely its publisher table of contents; record edition/printing precisely. Publisher lists third-edition hardcover ©2008; an asserted 2011 date needs edition-specific verification.
- Inspect NAPCO's Figure 13: buyer dissatisfaction percentages are **not** shop rework prevalence, equipment-utilization measures, or causal tests.
- Inspect ASQ's Define/Measure/Analyze/Improve content for recommended diagnostic sequencing; distinguish methodology from proven printer purchase outcomes.
- Keep a printing-industry spoilage/re-run definition available as supplemental evidence, without treating it as a survey of rework incidence.
- If a publication-relevant claim about capacity shortage versus failed handoffs still lacks direct evidence, request a targeted new source from Perplexity. Leave that claim unsupported if none qualifies.
- Produce dated verdicts for factual support, paragraph fidelity, independent verification and editorial suitability. A source audit is not publication approval.

**Initial disposition:** P001 `PARTIALLY SUPPORTED / SOURCE VERIFICATION PENDING / PUBLICATION HOLD`; see the pilot report. Do not scale research packets or change the manuscript based on a partial report.

## 7. Acceptance tests and change custody

Candidate packets must satisfy exact text identity, unique paragraph IDs 001–250, three explicit source positions with shortfall disclosure, precisely located citations, and explicit `PENDING` status until independent inspection. Track every research-lead replacement and editorial change with source, rationale, reviewer and time. Maintain fiction-versus-evidence separation.

Review branch is `reports/day-zero-candidate-009-20261114`. Only add candidate specification and pilot audit records here. Keep the v0.2 specification, approved Candidate 006, source manuscript and production systems unchanged. The owner retains the human decision on expansion and public release.

## 8. Next supervised research handoff

Perplexity may be sent **one narrowly scoped P001 gap-fill assignment** asking for exact passage-level `Factory Physics` evidence or a better accessible authoritative alternative, and empirical printing/job-shop sources that genuinely distinguish capacity, queueing, and coordination/rework effects. If full text is not lawfully accessible, disclose this limitation; use the strongest accessible original source instead of fabricating a quotation. All proposed findings return to the Bioscillate supervisor for independent review.

**Status:** REVIEW CANDIDATE. Not a verified publication standard until human accepted.