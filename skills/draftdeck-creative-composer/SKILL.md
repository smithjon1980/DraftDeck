---
name: draftdeck-creative-composer
description: Governs seven-stage creative recomposition of an admitted NotebookLM Spark into original, instructionally faithful, editable DraftDeck presentation slides and infographics.
---

# DraftDeck Creative Composer

**Project:** Bioscillate / BOSS · DraftDeck
**Status:** CANDIDATE · EXPERIMENTAL BRANCH ONLY · IMPLEMENTATION_NOT_VALIDATED · RELEASE_HOLD
**Method:** Dual-Spark / Creative Recomposition
**Purpose:** Manufacture new instructional visual experiences from approved ideas; do not reconstruct NotebookLM pixels.

## Authority and precedence

For builds explicitly designated **Creative Recomposition Trial**, this candidate replaces the reconstruction-oriented requirements identified in [SUPERSESSION_CROSSWALK.md](SUPERSESSION_CROSSWALK.md). The new composition route is **React + Tailwind CSS** with actual independent DOM text. SVG is allowed only as a discrete artwork asset. A PNG/WebP artwork asset is equally valid. **Chromium remains a browser renderer and QA instrument**; the legacy Go composition builder is not a mandatory stage of this route. Neither this document nor its commit modifies or ratifies other repository files, or authorizes publication.

The NotebookLM Spark is *creative input*, not a source of factual or visual authority. The original's pixels, placement, and design may be replaced. What must survive is the **approved instructional meaning** and accepted copy/expression, not pixel parity. Use the authenticated Issue Source Manifest and separately logged human editorial decisions to determine claims. An exploratory metaphor must never be elevated to a fact.

Respect Charter §6.04 structural-correspondence boundary and §6.05 Pick-and-Pull; distinguish verified propositions, untested ideas, and expressive choices. A verified hash establishes file identity, not doctrinal truth or editorial approval. All approvals require actual human decision records, not synthetic stand-ins.

## Seven-stage operating contract

### 01 — Admit
Accept a **real** NotebookLM page, image, PDF, or narrative Spark, with file identity, observed content, rights/permissions, issue identifier and relevant approved sources. Record exact byte digests when accessible; otherwise **SOURCE_ADMISSION_HOLD**, not a fabricated digest. Ingest only required material.

**Output:** admitted Spark locator and provenance record; teaching objective and authenticated source references.

### 02 — Discover
Describe the Spark's visual story, claims, expressions, teaching intent, learner competency, and useful visual possibilities. Keep proposition ledger and expression ledger distinct. Record uncertainty and source addresses. OCR is advisory only; it is not authority for authored text.

**Output:** source-addressed candidate propositions, expressions, and visual directions.

### 03 — Pick-and-Pull
Use **Pick → Pull → Inspect → Fit → Install → Authorize** with explicit human **ACCEPT / REJECT / AMEND** decisions. Treat rejected material as unavailable for production. Preserve rationale, source relationship, and rights. No silent canon promotion or rewrite-percentage quota.

**Output:** approved creative input list and editorial decision receipts.

### 04 — Direct · Approval Gate 1
Populate the upstream [Slide Creative Contract](schemas/slide_creative_contract.yaml), including:
- Teaching Claim and its exact source/decision locator and state.
- Spark Inspiration (descriptive only; no pixel-parity requirement).
- Creative Treatment: **RETELL** (conserve narrative setting) or **REIMAGINE** (new metaphor, same authorized lesson).
- Narrative Direction and **text-free** Artwork Brief.
- Approved **Editable Copy** with provenance.
- Visual Standard and measurable Acceptance Criteria.

**Human must explicitly approve the creative treatment and instructional direction.** Permission here authorizes bounded candidate creation, **not** selection, manufacturing, or public release. Record Gate 1 decision ID/time/scope.

### 05 — Create · Approval Gate 2
Generate original **separate** text-free artwork alternatives according to the approved brief. Candidate count follows actual tool capability and operator choice; do not fabricate variants. Inspect for wrong subject, unsupported symbolism, hallucinated measurements, unwanted text and image-generation artifacts. Preserve prompt, candidate files and generator metadata in the **restricted upstream creative/audit archive**.

**Human selects an actual candidate or rejects all.** Record selection ID, selected file SHA-256 from bytes, allowed design deltas and rationale. Gate 2 authorizes only the selected asset's downstream manufacturing.

### 06 — Manufacture
Build a **positive-allowlisted** restricted payload conforming to [restricted handoff JSON Schema](schemas/restricted_manufacturing_handoff.schema.json) and the [sample carrier](schemas/restricted_manufacturing_handoff.yaml). **Do not copy the upstream Creative Contract into the manufacturing packet.** It contains the generation prompt and Spark provenance that are not authorized manufacturing inputs. The packet may carry only:
- selected approved artwork path, its verified digest and permissible usage scope;
- approved exact copy and source/decision IDs;
- required geometry, brand profile, typography and manufacturing restrictions;
- Gate 1 + Gate 2 approval receipts and a non-browsable provenance join ID.

Never include original NotebookLM PDF, creative prompt, prompt history, rejected candidates, raw private conversation, complete editorial ledgers, or unbounded source links. The supervisor compiles a bounded scene manifest and component plan from this packet. The scene is assembled from independent **React/Tailwind semantic text** and text-free artwork assets; illustrations may be SVG, PNG or WebP. Do not assume a generated image is actually text-free until inspected.

Record reproducible build inputs and render via Chromium. Do not claim that an SVG import is an independently editable HTML text layer.

### 07 — Verify · Approval Gate 3
Independent QA must inspect and document:
1. **Instructional fidelity** to accepted teaching claims and approved literal copy; preserve UNKNOWN / NOT ESTABLISHED where applicable.
2. **Creative quality** and meaningful correspondence to the **new human-approved creative treatment**, not the NotebookLM pixels; actual image/layout evidence required.
3. **Technical editability**, including DOM inspection of separate instructional text **and an actual edit → save → reopen/refresh → persist demonstration** in the declared target authoring format. Presence of text nodes alone is not a pass.
4. Constraints: 16:9 scene where specified, no hidden rasterized copy, brand profile, clipping/overflow, rights, runtime/test record, and handoff isolation.

No test result, model claim, or passed workflow creates publication authority. Present QA evidence for **distinct human release authorization**; otherwise **RELEASE_HOLD**.

## Visual and manufacturing boundaries

Follow the declared BOSS visual profile, authentic logo colors (cyan/magenta/black where the approved asset requires), pure white slide ground unless a separately approved profile says otherwise, CAD/ISO linework, information-dense Tesla Model Y center-screen influence, and controlled whitespace. Do not silently override approved typography or source copy with generic tool defaults. The effective profile and exact tokens must be source-addressed at Gate 1; unverified exact font/color values remain unresolved. Presentation layout and infographic layout may have different geometry while sharing scene/brand components.

**VTracer:** optional raster-to-SVG utility for an isolated approved artwork feature only; never the default Spark-to-slide engine. **REA:** optional tool for investigating permitted software behavior or a failed workflow, not an editorial decision maker. **Chromium:** rendering/verification, not a replacement for the editable authoring model.

## Fail-closed states

SOURCE_ADMISSION_HOLD · EDITORIAL_DECISION_HOLD · CREATIVE_CONTRACT_HOLD · ARTWORK_SELECTION_HOLD · HANDOFF_CLEARANCE_HOLD · MANUFACTURING_HOLD · EDITABILITY_HOLD · RELEASE_HOLD.

Any absent required operand remains NOT ESTABLISHED; do not invent human decisions, vector quality, provenance, tool results, or authorizations. Do not push changes to main or the curriculum branch via this skill.

## Trial milestone

Run **one authentic NotebookLM Spark → human-adjudicated teaching claim/expressions → Gate 1 approved Retell/Reimagine contract → candidate artwork → Gate 2 human selection → restricted React/Tailwind slide build → Chromium render → independent real-text edit/persistence QA → Gate 3 release decision**. The current repository commit only stages the candidate specification and test plan; it does **not** demonstrate execution of the seven-stage workflow.

Read [VALIDATION_PLAN.md](VALIDATION_PLAN.md), [SUPERSESSION_CROSSWALK.md](SUPERSESSION_CROSSWALK.md) and existing Dual-Spark handoff procedures before implementation.
