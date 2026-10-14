---
name: draftdeck
description: Governed source-to-spark production using compartmentalized, need-to-know creative generation, human-approved images, supervising-agent scene planning and Go/Tailwind/Chromium deterministic manufacturing. No SVG, React, Canva or PowerPoint in the canonical production route.
---

# DraftDeck — Need-to-Know Spark Handoff

**Status: CANDIDATE · 2026-10-13 · RELEASE_HOLD.** The process below is an approved *candidate specification* for implementation; it does not prove that role-based access controls, the creative generator, a supervisor, or a worker dispatcher are running.

## Core distinction
**The system generates the spark upstream. The human authorizes a candidate. Only the approved visual and the minimum manufacturing instructions go to the supervising agent.**

The original NotebookLM presentation and all prompts used for reimagination remain in a **creative provenance/audit compartment**, not in the ordinary supervisor input. The supervisor is a scene-contract compiler, not a visual prompt interpreter or a second creative director. It cannot require the hidden creative prompt to do its job. This is a structural correspondence with **need-to-know compartmentalization**, not a claim of U.S. government classified status or accredited clearance.

This corrects the earlier four-reference supervisor-packet design. The full A/B/C/D relationship is preserved in the privileged **archive**, but the production supervisor no longer receives all four raw sources.

## Upstream → downstream contract

1. **Ingest and authenticate (Source/Ingestion compartment).** The learner chooses a NotebookLM PDF or slide. The system verifies exact bytes, source identity, specific page, provenance/usage rights and the intended teaching objective, and associates authorized instructional text. No creative prompt is written or exposed by the supervisor.
2. **Internal prompt synthesis (Creative compartment).** The same upstream system uses the ingested reference and stated learner expectations to compose a **source-specific visual-generation prompt**, record its exact operator-visible text and hash, and execute the connected image-capable generator. The human can choose a candidate count supported by the tool (one to four; **four is the manual-trial default**, not a universal mandate). Each image must be a separate candidate asset, not one collage/contact sheet; do not claim an inaccessible hidden tool prompt was recorded.
3. **Source correspondence preflight (Creative compartment).** The upstream verifier checks generated candidates against the chosen slide's subject, hero/objects, instructional meaning and hard constraints. Reject images about the wrong lesson or mere diagrams of the DraftDeck workflow. A creative candidate need not be pixel-identical to NotebookLM; exact image-to-image reproduction is **not the objective**.
4. **Human decision (Approval compartment).** Present accepted candidates. The operator selects one or rejects all and may iterate. Archive the full written selection rationale and candidates. The operator approves **what is to be made and why**, not how the prompt was worded.
5. **Minimal production handoff (Supervisor compartment).** Send **only** the approved creative raster asset, its ID and verified hash, a bounded teaching objective, authorized exact copy/excerpts, required visual/manufacturing constraints, allowed deltas, and a signed/recorded approval attestation (including selection ID). **Do not include the source PDF by default, creative-generation prompt, prompt history, unselected options, private review notes, or whole evidence ledger.** A production supervisor may request *specific additional approved context* through a logged authorization gateway when actually necessary. An auditor/QA reviewer with appropriate access can independently inspect original references and archives.
6. **Compile (Supervisor).** Produce the tripartite contract: `scene-manifest.json` (geometry and material ownership), `narrative-brief.md` (source-grounded intent and desired composition) and `worker-criteria.md` (bounded positive and negative acceptance tests). No further artistic redesign and no rendering performed by the supervisor.
7. **Manufacture (Workers/Go).** Story creates text-free PNG/WebP, Art creates registered HTML/CSS components without instructional text, Text emits exact sourced semantic HTML. The Go/Tailwind/Chromium engine assembles the approved manifest; no SVG, React, Canva, PowerPoint or flattened teaching text.
8. **Independently verify and request release.** Manufacturing QA compares actual output to the *selected creative asset for meaningful visual/story correspondence*, to the authorized source for instructional accuracy, and to the implementation contract for geometry, typography and isolation. Outcome is **meets/exceeds the human's declared expectations** only if recorded acceptance criteria are satisfied. Exceeding expectations does **not** authorize changing facts, adding uncontrolled elements, or claiming pixel parity. Human release authorization remains distinct.

## Compartment map

| Compartment / role | May access by default | Must not receive by default |
|---|---|---|
| Source ingestion | Original NotebookLM reference; original authorized content; source credentials under separate security policy | Production-worker write rights |
| Creative generation | Necessary source page/excerpts, tool-specific synthesis prompt, its own candidates | Unrelated learner private data; release permission |
| Human approver | Source context, accepted candidate options, creative intent, selection rationale | Secret service credentials and engine internals |
| Production supervisor | Selected approved image, approved content/copy, operational/visual constraints, approval verification token | Generation prompts, rejected options, entire source PDF or raw archive |
| Story worker | Allowed image crop/visual spec; permitted raster asset input | Creative prompt; entire original PDF; mandatory instructional text |
| Art worker | Allowed component spec, bounds and registered tokens | Creative prompt; unapproved editorial text; arbitrary styling/code |
| Text worker | Exact authorized strings, source identifiers and semantic hierarchy | Creative prompt; raw unapproved visual text; layout/CSS instructions |
| Independent QA/auditor | Necessary immutable evidence for its explicitly authorized review, potentially including original and prompt archive | Authority to approve its own release |

Need-to-know is a **data minimization objective**. GitHub folders and prose do not enforce permissions. Enforce file/connector ACLs, separate scoped identities, manifest data-schema allowlists, runtime checks, retrieval logging, immutable hashes and least-privilege secrets. Audit privilege is explicit, not universal.

## What crosses the supervisor boundary

```text
production-handoff/
  approved-spark.webp          # selected, exact bytes; PNG also permitted
  approved-brief.json          # objective, visual expectations, explicit delta permissions
  source-copy.json             # authorized strings/excerpts + source IDs, not full private corpus
  selection-attestation.json   # selected candidate ID, hash, decision/time, approver reference
  handoff-manifest.json        # checksums, versioned contract ID, minimum provenance join ID
```

**What stays upstream:** original NotebookLM PDF, prompt text and prompt versions, all generated/rejected candidates, complete human discussion/rationale, generator metadata and the full `provenance.json` audit sidecar. The downstream attestation can carry a hashed ledger reference and permission-scoped verification result, never a link that grants unbounded raw access. Hashes prove byte identity, not truthfulness or actual access control.

**Human selection rationale:** preserve the full rationale in the audit archive. Put only **actionable, approved design requirements** distilled from it in `approved-brief.json` (e.g. “CPU remains hero; telemetry ring remains visually legible; no invented statistics”). The supervisor does not need the human's entire dialogue either.

## Acceptance contracts
- **Source gate:** reference is a real accessible NotebookLM asset; source text and permissions have a verified identity; actual SHA-256 is calculated, not invented. Failure → SOURCE_ADMISSION_HOLD.
- **Creative gate:** selected slide was truly observed; each candidate matches its specific topic and meaning; candidates are distinct assets. A wrong-topic output → REJECTED_WRONG_SUBJECT, not a passing candidate.
- **Human gate:** documented choice, rationale, approved image hash and decision. Failure → HUMAN_SELECTION_HOLD.
- **Boundary gate:** the supervisor payload is constructed by a positive allowlist and rejected if it contains raw prompt history, unselected-image bytes/URLs, raw source PDF, privileged archive credentials or unapproved instructions. Test negative cases. Failure → HANDOFF_CLEARANCE_HOLD.
- **Manifest gate:** Go validator and an actual versioned JSON Schema must both pass as implemented, including failure tests. The `scene-manifest-001/validator.go` already checks some bounds, IDs/links, layer bands, component tokens and file hashes; it is not a complete schema or visual validator. The requested `scene-schema-v1.json` was not present at the prior audit. Failure → MANIFEST_HOLD.
- **Manufacturing gate:** verify actual role separation, allowed asset types, exact copy, HTML/CSS allowlists, renderer output, source/asset hashes, no SVG and no unauthorized elements. Failure → ASSEMBLY_HOLD.
- **QA/release gate:** demonstrable visual and instructional acceptability, real rendered evidence, independent review and final human permission. Failure → RELEASE_HOLD.

## Manual validation milestone
Choose one recovered, authentic NotebookLM slide, associate genuine instructional source text, let the upstream generator build its **own source-specific prompt**, generate four separate alternatives (or fewer if the user explicitly chooses), human-select one with rationale, **strip creative provenance from production payload**, manually compile a scene + narrative brief + worker criteria, then run the existing Go stack for one page. Conduct tests that prove the supervisor cannot see `generation_prompt`, `prompt_history`, `candidates_unselected`, or original PDF bytes through the production route.

Prior failed image trials drifted into DraftDeck-process infographics or another Day Zero topic **during generation**, before any real supervisor handoff. Those errors establish a need for source anchoring upstream; prompt isolation alone does not repair image generator behavior. No image fidelity, live role isolation or finished rendering is newly claimed by this skill patch.

## Historic technical evidence
The older **Phase 1 WIREFRAME** was a prior structural run, not the current manual scene-planning milestone or a visual master. The only current candidate renderer is `skills/draftdeck/engine/` plus `.github/workflows/draftdeck-canonical.yml`. Existing agent definitions do not show an implemented multi-agent dispatcher. Never treat a green workflow, successful PDF signature, or model confidence as a release decision.

Read [compartmentalized handoff](dual-spark-handoff/README.md), [role-specific prompts](dual-spark-handoff/PROMPTS.md), and [Gemini inspection brief](GEMINI_INSPECTION.md). New work stays on the candidate branch until verified and authorized; do not merge or release automatically.
