# Need-to-Know Creative Spark Handoff — Candidate v0.2

**Status:** CANDIDATE · 2026-10-13 · ACCESS_BOUNDARY_NOT_ESTABLISHED / MANIFEST_HOLD / RELEASE_HOLD  
**Principle:** The learner provides a NotebookLM reference. The **upstream system creates the prompt and candidate images**, the **human selects one**, and the **supervising agent manufactures a specification from the one approved image**. The supervisor never needs the creative-generation prompt. Apply U.S.-style *need-to-know* as an architectural analogy; this is **not a government classification system**.

## System roles, responsibilities and inputs

| Stage | Action | Permitted material | Produced material |
|---|---|---|---|
| 0. Intake / reference admission | Verify NotebookLM file/page, teaching purpose, underlying instructional source | Original PDF; source content | Source identity, exact hashes, validated teaching objective |
| 1. Upstream creative director | Compose the image prompt internally; invoke external/native image model | Scoped reference page and learning objective | Versioned prompt; 1–4 separate candidate raster images |
| 2. Creative correspondence check | Catch missing source, wrong subject, lost meaning, prohibited changes | Source, prompt if needed, all candidates | Accept/reject decision for each option |
| 3. Human authority | Inspect acceptable candidates, choose one or request regeneration; give rationale | Source context; candidates; approved objective | Signed/recorded creative decision and approved spark ID/hash |
| 4. Production handoff builder | Assemble **positive-allowlisted** minimal payload | Selected image, approved requirements, authorized source excerpts, approval attestation | Sealed supervisor packet with hash and archive reference |
| 5. Supervising agent | Compile the selected scene into a manufacturing contract | **Only sealed production packet** | Scene Manifest, Narrative Brief, Worker Acceptance Criteria |
| 6. Specialized workers & Go compositor | Build scoped assets; assemble to PDF | Worker-specific bounded contracts | Text-free Story PNG/WebP; Art HTML/CSS; exact Text HTML; PDF |
| 7. QA / auditor | Independently verify meaning, layout, bytes, rights and release status | Scoped full-reference/audit evidence as granted | QA evidence and final human decision request |

## Two physically and logically separate archives

The upstream creative/audit archive preserves full provenance; production receives only a minimal derivative. Access should be controlled by storage/connector permissions and programmatic allowlists, **not just by naming folders**.

```text
RUN-001/
  upstream-creative-audit/              # restricted; not mounted in supervisor runtime
    source-notebooklm.pdf                # original genuine slide/deck
    source-page.png                      # extraction of explicitly chosen page
    authoritative-content.md             # exact source material
    generated-prompt.txt                 # human-visible exact dispatched prompt
    generator-metadata.json              # reported generator, model, version, datetime, uncertainty
    candidates/
      candidate-01.webp
      candidate-02.webp
      candidate-03.webp
      candidate-04.webp                  # only for actual four-option runs
    candidate-evaluations.json
    selection-rationale.md               # full human-written reasoning
    provenance.json                     # complete verified hashes, processing IDs, rejection history
  sealed-production-handoff/             # only files in this folder may reach supervisor
    approved-spark.webp                  # approved exact selected bytes
    approved-brief.json                  # teaching objective, selected visual expectations/deltas
    source-copy.json                     # authorized exact strings + stable provenance IDs
    selection-attestation.json           # approved ID, selected image hash, decision/time, role
    handoff-manifest.json                # hashes and restricted audit join reference
  supervisor-outputs/
    scene-manifest.json
    narrative-brief.md
    worker-criteria.md
  production/
    story-assets/
    art-components/
    text-content/
    output.html
    output.pdf
  verification/
    independent-qa.md
    output-hashes.sha256
    human-release.md
```

Paths are **target architecture**, not assertions that these artifacts already exist. A run with fewer options archives exactly the count requested; do not create blank candidates and pretend they were generated.

## Supervisor input allowlist

Only the fields below are approved for the sealed payload:

```json
{
  "contract_version": "draftdeck-handoff-candidate-v0.2",
  "run_id": "RUN-001",
  "spark": {"file": "approved-spark.webp", "sha256": "CALCULATE_FROM_BYTES"},
  "learning_objective": "APPROVED_OBJECTIVE",
  "visual_acceptance": ["APPROVED_SCOPED_CRITERION"],
  "approved_deltas": ["ALLOWED_SOURCE_TO_SPARK_CHANGE"],
  "source_copy": {"file": "source-copy.json", "sha256": "CALCULATE_FROM_BYTES"},
  "selection_attestation": {"file": "selection-attestation.json", "sha256": "CALCULATE_FROM_BYTES"},
  "provenance_join_id": "AUDIT_RECORD_ID_WITH_NO_RAW_ACCESS"
}
```

Placeholders are not legitimate production manifests or hashes. In particular, the supervisor must **not** receive `generation_prompt`, `prompt_history`, `rejected_candidates`, `raw_notebooklm_pdf`, `complete_source_archive`, personal reflections, or broadly scoped Drive/GitHub credentials.

## Selection decision
In the upstream archive preserve (1) the candidate chosen, (2) the *actual* byte hash, (3) a human-written rationale for better communication of the lesson, (4) approved deviations from NotebookLM, (5) rejections and uncertainties, and (6) approval timestamp and authorizing principal.

In the supervisor handoff transmit only the actionable and approved consequences: e.g. **“exploded CPU must remain visual focal point, anomalous telemetry visually distinct, keep full diagnostic hierarchy, no invented data.”** There is no obligation for the supervising agent to inspect creative prompts or infer why other images were rejected.

## Creative fidelity versus factual fidelity
The user has explicitly rejected mandatory 1:1 reproduction. The operative standard is **meets or exceeds the learner's articulated visual and instructional expectations**, assessed independently against bounded criteria, not subjective AI praise. The generated image is a **target composition**, not a new source of factual claims. The authorized instructional source is still binding for exact words, numbers and qualifications. Any generated label in an illustration that conflicts with authoritative copy must be rejected or replaced in the Text layer.

## Tests to perform before deployment
1. Inject `generation_prompt`, rejected option bytes, an original PDF, or broad Drive URL into a would-be supervisor payload; the handoff schema/build process must reject all. A mere prompt “ignore these” is insufficient.
2. Log what the supervisor can *actually retrieve* using its own credentials and tools; it must not open the upstream audit area. This cannot be verified from repository Markdown.
3. Tamper with the approved spark; the checksum validation must fail.
4. Remove human selection authorization; supervisory work must not start.
5. Supply a lovely image with the wrong NotebookLM subject; the upstream creative stage must reject it before supervisor admission.
6. Author a Scene Manifest for one approved image and prove it can drive the real Go/Tailwind/Chromium renderer; passing the older wireframe benchmark does not establish this.
7. Audit separately: human-approved visual acceptance, exact source copy, logical correctness, and real PDF editability in the requested editor. Selectable text alone is not sufficient proof of editability.

## Current readiness
The candidate branch already contains `scene-manifest-001/validator.go` for partial checks, but an end-to-end automated creative system, real enforced compartment permissions, authoritative-schema conformance and aesthetic final output are **NOT ESTABLISHED**. Earlier image generation produced off-subject images; that failure happened **upstream** of the supervisor and is not automatically repaired by withholding prompt history. Archive all failed attempts and repeat a single-slide manual simulation with this boundary.
