# DraftDeck Dual-Spark Handoff — Source Packet v0.1

**Status:** CANDIDATE · 2026-10-13 · SOURCE_ADMISSION_HOLD / MANIFEST_HOLD / RELEASE_HOLD  
**Scope:** repeatable learner-facing creative-to-manufacturing transfer; no assertion that image generation, schema execution or high-fidelity reconstruction succeeded.

## One-patch / one-NotebookLM-workspace rule
Create a new versioned source patch for each distinct NotebookLM research workspace. Never silently replace earlier source material or change the meaning of a prior hash. Archive the prior workspace, manifest, notes, acceptance decision and unresolved differences. Keep provisional experiments and authenticated material in separate folders. Do not treat a fresh notebook as an implicit authorization to overwrite canonical text.

## Identity and responsibilities

| Reference | Meaning | Required authorization | Final role |
|---|---|---|---|
| **A** | Genuine NotebookLM reference image / original instructional visual | Authentic source admitted and hashed | Meaning and initial story reference |
| **B** | Learner-selected, AI-reimagined full composite image | Human creative approval + hashed bytes | Target composition and visual hierarchy |
| **C** | Authoritative instructional source content | Authenticated, versioned, exact-copy and rights boundaries | Factual text authority |
| **D** | Brief that narrates B's creative choices and fidelity constraints | Human creative approval + revision identity | Semantic bridge from imagery to manifest |

**Order:** authenticate A/C → create B/D → explicit human approval of B/D → supervisor compiles Scene Manifest → verify manifest against implemented contract → Story/Art/Text workers → Go/Tailwind/Chromium → independent reference QA → explicit human release.

### Required packet directory for one slide

```text
dual-spark-run-001/
  00-admission/
    admission-record.md
    hashes.sha256
  01-original/
    notebooklm-reference.<png-or-webp>
  02-source/
    authoritative-text.md
  03-creative/
    human-approved-composite.<png-or-webp>
    creative-handoff.md
    creative-decision.md
  04-plan/
    scene-manifest.json
    manifest-validation.json
    worker-contracts.md
  05-production/
    story-assets/
    art-components/
    text-content/
    output.html
    output.pdf
  06-verification/
    evidence-ledger.md
    independent-qa.md
    human-release.md
```

The directory listing is a **target layout**, not evidence that these files currently exist. Naming and storage may be adapted to the approved archive policy without mixing version identities. Treat the NotebookLM generated source image and the AI creative image as two separate immutable payloads.

## Admission record fields

| Field | Purpose |
|---|---|
| `run_id`, `patch_id`, `admission_date` | Identify candidate execution and version |
| `reference_id` | A, B, C or D |
| `file_path`, `sha256`, `bytes`, `media_type` | Prove exact admitted artifact identity |
| `producer`, `generation_date`, `source_workspace` | Provenance, with UNKNOWN where necessary |
| `authority` | For source C: which copy is binding; for B/D: which human decision is binding |
| `rights_status`, `permitted_use` | Bound reuse and publication |
| `verification_method`, `verifier`, `verified_at` | Distinguish reported versus independently checked evidence |
| `state`, `issues` | ADMITTED, CANDIDATE, REJECTED, HOLD |

Do not invent byte hashes; calculate them from real received bytes. The reference and source hashes required by the candidate Go validator are not established by simply pasting filenames into the manifest.

## Compilation contract

**The supervising agent does not generate the final artwork or render the final PDF.** It interprets the approved composite B in light of A, C and D and produces a proposed manifest and bounded worker contracts. Use one coordinate origin and canvas policy. Reference the implemented `scene-manifest-001/validator.go` for currently enforced rules; `scene-schema-v1.json` is a **missing prerequisite**, not a verified installed artifact.

Every intended visual element must identify its owner (Story, Art, Text), geometrical bounds, z-order, source/creative reference, and semantic function. Claims of supported copy must resolve to C; unsupported words in B never override C. Reject dangling semantic links and out-of-bounds elements. Record any crop decisions or visual mismatches as explicit deltas.

## Gates and falsifiable checks

- **Admission gate:** authentic original A, authoritative C and hashes; source provenance and rights declared.
- **Creative gate:** a concrete B, D, and dated human approval decision; reject an ambiguous 'looks good' from an automated agent.
- **Manifest gate:** actual schema available, parsing and structural checks, linked content provenance, asset constraints and negative tests; never promote preliminary JSON into a release claim.
- **Manufacturing gate:** three isolated role outputs, executable allowed components, actual engine execution, and rendered file evidence.
- **QA gate:** image comparison with B, factual comparison with C, teaching alignment with A, verifiable hashes and independent review.
- **Release gate:** explicit human permission; never infer release from QA PASS alone.

## Present state and next test

Existing `scene-manifest-001/day-zero-manifest-001.json` uses approximated positions and null reference/source hashes; it remains **CANDIDATE_NOT_AUTHENTICATED**. The directory currently has a Go validator and tests, but no checked-in `scene-schema-v1.json`. A production input pair consisting of the genuine high-fidelity NotebookLM slide and its corresponding authoritative text has not been admitted in the inspected branch. Therefore **no end-to-end Dual-Spark reference reconstruction can be claimed**.

**Smallest next experiment:** admit A and C; hash exact files; generate one B and D; record human selection; reconcile schema/Go validation on one scene; exercise only the approved one-slide workflow; independently compare final PDF to B and copy to C. Do not launch a broad deck run before this one-slide proof.
