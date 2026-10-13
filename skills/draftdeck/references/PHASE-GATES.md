# DraftDeck Phase Gates — operational checklist

| Gate | Required | Evidence | Disposition |
| --- | --- | --- | --- |
| P1 structure | Go template, Tailwind compilation, HTML, Chromium PDF, correct 16:9, correct copy, no SVG | Actions log, source/output hashes, PDF | P1_TECHNICAL_PASS / P1_HOLD |
| P2 composition | Three isolated Story/Art/Text outputs, text-free Story PNG/WebP, Art HTML/CSS, editable Text, visible complete composite | Per-layer manifest, snapshots, independent editability/collision checks | P2_COMPOSITION_PASS / P2_HOLD |
| P3 verification | Source fidelity, reference fidelity, visual QA, hash integrity, persistent read-back, explicit human approval | QA report, diff images, hashes, release record, stable URL | P3_ACCEPTED / RELEASE_HOLD |

Rules: no skipping gates; no promoting green CI into visual acceptance; no SVG at any production stage; no automated release. Missing Story or Art is allowed in P1 and blocks P2. A failed visual comparison is a failure even if all components are editable.
