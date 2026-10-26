# BOSS Storybook — Layout Selection and Variant Archive Protocol

**Status:** PROPOSED V1 — candidate for human review  
**Scope:** Episode Zero, planned 250 pages at 17 × 11 inches landscape  
**Authority:** Locked manuscript, existing BOSS provenance guard, human release approval

## Principle
**The manuscript determines the layout; the layout never determines or rewrites the manuscript.** Each page evaluates seven structurally distinct candidates derived from the same authoritative paragraph. Recommend one and retain the other six with reviewable evidence. A high score does not grant publication authority.

## Non-negotiable gates (fail closed)
1. Exact authoritative paragraph ID, source version, and SHA-256; no changed text, invented characters, setting, claim, or quotation.
2. Spark/reference assets document origin, usage rights, and allowed visual attributes. Inspiration grants *no* content authority.
3. Exact 17 × 11-inch landscape page; white background; approved cyan, magenta, black identity, logo, and required instructional components.
4. No clipping, unreadable text, off-page content, or unacceptable print/export fidelity. Preserve editable text and diagrams where feasible; raster story art is permitted only where authorized.
5. Provenance and verification evidence recorded. Any failure, uncertainty, or unavailable source yields `HOLD`, never a recommendation.

## Scoring rubric
Rate each dimension 0–5 with evidence. `weighted_points = weight * rating / 5`. Sum to 100; never score a candidate that fails a gate.

| Dimension | Max points | Evaluation question |
|---|---:|---|
| Manuscript compatibility | 30 | Does panel structure serve this paragraph without forcing new content? |
| Instructional effectiveness | 20 | Does it support understanding, process, causal links, and reflection? |
| Visual hierarchy and readability | 20 | Is reading order clear, text legible, spacing generous? |
| Editorial storytelling quality | 15 | Does it meet the premium illustrated Storybook standard? |
| Sequence diversity | 10 | Does it vary neighboring layouts appropriately? |
| Production reliability | 5 | Is the result reproducible, printable, and maintainable? |
| **Total** | **100** | |

Rating anchors: 0 absent/unacceptable, 1 poor, 2 weak, 3 adequate, 4 strong, 5 exemplary. Missing evidence is `UNSCORED`, not zero or a guessed value.

Provisional bands: 90–100 excellent; 80–89 strong; 70–79 acceptable; 60–69 weak; below 60 poor. Calibrate thresholds and weights against human-reviewed samples.

## Selection procedure
1. Lock source paragraph and digest; profile narrative/process/analysis/inquiry/evidence/exercise/balanced characteristics (each 0–5).
2. Render all seven layouts from the **identical** locked paragraph; change composition, not story or subjects.
3. Evaluate gates; quarantine failed candidates and document precise failure reasons.
4. Score eligible candidates with criterion ratings, rationales, and source-to-render checks.
5. Rank by score. Candidates within **3 points** of the leader become an **editorial tie**, requiring human comparison. For display ordering only, prefer higher manuscript fit, then instructional effectiveness, then stable variant ID.
6. Apply diversity only within its 10-point allotment; never demand equal utilization of layout families.
7. Present a recommendation and evidence bundle; publish only after a human approves the **exact candidate/version**.
8. Retain every candidate as an audit record. The six unselected candidates are archived, not deleted.

## Archive states
- `APPROVED_FOR_PAGE`: the one explicitly approved candidate tied to the specified page and digest.
- `ARCHIVED_UNAPPROVED_FOR_REUSE`: unselected, gate-passing candidate available for later consideration only.
- `QUARANTINED_FAILED_GUARD`: noncompliant candidate retained for audit, **not** reusable until corrected and retested.
- `HOLD`: incomplete evidence, tie awaiting review, or other unresolved gate.

For 250 completed pages × seven rendered candidates: **1,750 candidate records**, **250 selected**, **1,500 nonselected**, assuming exactly one page approval and seven outputs per page. Quarantined records do not count as reusable assets.

## Required archive manifest
`episode_id`, `section_id`, `paragraph_id`, `manuscript_version`, `manuscript_sha256`, `spark_asset_id`, `spark_source`, `spark_allowed_properties`, `variant_id`, `layout_family`, `candidate_version`, `candidate_sha256`, `source_file_uri`, `preview_uri`, `print_uri`, `validation_status`, `gate_results`, `score_breakdown`, `total_score`, `ranking`, `selection_reason`, `approval_actor`, `approval_time`, `reuse_tags`, `rights_status`, `archive_status`.

Store shared media by immutable digest to avoid duplication, and retain versioned manifests. Repurposing any design for another Storybook page, website, textbook, or presentation requires a new source binding, rights/provenance verification, hard-gate tests, and new human approval; approvals cannot be inherited.

## Calibration and safeguards
Start with Episode Zero / Section 1 / Paragraph 001 using verified exact text. Score all seven layouts and compare blinded human rankings, inter-reviewer agreement, text fidelity, and print inspection. Record weight/threshold changes as versioned reviewable proposals. **No automated merge, publishing, or production release.** Do not modify React/Tailwind, Windmill, n8n, Railway, or GitHub Actions solely to adopt this rubric.

## Acceptance tests proposed (not yet executed)
- Source paragraph mutated → `HOLD`.
- Unauthorized café/cat or other introduced subject → quarantine.
- Spark image promoted to content authority → quarantine.
- Wrong 17 × 11-inch page box or wrong palette → `HOLD`.
- Absent manifest field or missing rights record → `HOLD`.
- Two variants within 3 points → flag human editorial tie.
- Six valid unselected variants → six searchable archive records, never silently discarded.
- Reuse from archive without new approval → blocked.
