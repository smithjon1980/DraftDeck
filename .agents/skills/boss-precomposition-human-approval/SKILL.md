---
name: boss-precomposition-human-approval
description: Require separate visible human approval of art and story candidate layers before React/Tailwind slide composition, regardless of structural CI or prior candidate status.
---
# BOSS precomposition art + story acceptance

This is a mandatory stop gate between isolated layer generation and combined slide composition. Read `AGENTS.md`, `.agents/skills/boss-art-asset-producer/SKILL.md`, `.agents/skills/boss-art-story-reviewer/SKILL.md`, and `.agents/skills/boss-react-art-story-submission/SKILL.md`.

## Sequence
1. Submit **art only**, without masthead, editorial copy, story labels or composited slide. Render its genuine source at the actual intended scale. Record SHA-256 of the underlying art source and screenshot; visually inspect source, people/equipment anatomy, technical fidelity, detail, medium and originality.
2. Human must respond specifically **APPROVE ART <candidate_id>** or **REJECT ART <candidate_id>**; a generic "proceed", silence, automated score, or tool-created token is not approval. Save a human-attributed evidence reference in a restricted approval ledger (not a self-signed model claim).
3. Submit **story only** as an independent storyboard with causal sequence, operational facts and teaching outcome; no composed slide. Render it separately. Require **APPROVE STORY <candidate_id>** or **REJECT STORY <candidate_id>**.
4. Reject → issue-specific correction → fresh candidate ID and hash → resubmit same layer. Approval of an older source version does not carry forward.
5. Composer may run ONLY when both approvals are valid for the identical section, slide ID, art and story hashes, both previewed versions, and the same intended composition target. A valid approval is not a release authorization. Any source change, missing/expired approval, hash mismatch, wrong slide, self-approval, private artifact leak or altered build → HOLD.
6. After composition, perform editorial/native text, React/Tailwind source, browser render, brand, PDF and human final-layout inspection. The human explicitly authorizes release separately.

## Rejection of current candidates
The previous box-based studio scenes and stick-figure Slide 05 rebuild are **REJECTED AS ART**, not accepted references. Treat new work as fresh art proposals. No previously generated slide has inferred human approval.

## Division of responsibility
OpenDots may stage and organize candidate evidence only under real granted permissions. OpenBot/BOSS gateway must enforce execution policy and audit. GitHub Actions validates manifests; CI may not mint approvals. Human review is mandatory and occurs before any art+story composition. Never put unpublished source, review recordings, credentials or approval signing secrets in public GitHub.
