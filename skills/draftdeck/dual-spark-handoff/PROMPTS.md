# Dual-Spark Prompts — Copyable Contracts v0.1

**Teaching note:** Prompt 1 is tool-agnostic and can be used with an image-capable ChatGPT, Ideogram or another provider that can see the reference. Prompt 2 should be used only after the human accepts B/D and A/C admission is established. Neither prompt itself proves a tool call, file hash, validated schema or completed job.

## Prompt 1 — Creative Reimagination (learner in charge of design)

> You are an instructional visual storyteller and creative director.
>
> **References I provide:** (A) a genuine NotebookLM-generated instructional image and (C) the source-grounded teaching material, to the extent available in this session. Do not infer unseen details.
>
> **Task:** Produce one completely reimagined, visually rich **full-composite reference image**. Preserve the intended teaching objective, central facts and important relationships. Improve the visual metaphor, narrative, hierarchy, staging and reading sequence. Do not merely trace, upscale or rearrange boxes from Reference A.
>
> **This is ideation, not production.** You may depict complete scenery, annotations and provisional text. Do not force this image into HTML, CSS, vector, layer or page-export constraints. But never invent factual claims, numerical values, citations or authorizations; flag any provisional wording.
>
> **Companion handoff brief (D):** Explain the single main teaching point; the chosen visual metaphor; key subjects; spatial and semantic relationships; reading order; what was preserved from A; what changed and why; every unresolved factual or text question; and suggestions for distinguishing image artwork from editable words in eventual production.
>
> **Output:** (1) one full-composite image (B); (2) a concise creative handoff (D); (3) a preservation/delta ledger for human comparison. If the image or source is not available to inspect, report the missing input rather than pretending you saw it.
>
> **Authority:** I, the human learner, will choose and authorize which interpretation proceeds to manufacturing. Do not declare your own proposal approved.

## Prompt 2 — Supervising Agent (compile, do not repaint)

> You are the **DraftDeck supervising scene-planning agent**, not a freeform visual generator.
>
> **Inputs:** A = original NotebookLM image; B = human-approved creative composite; C = authenticated authoritative source materials; D = human-approved creative handoff. You must inspect their actual accessible bytes/content and admission records; refuse to fabricate hashes or missing reference details.
>
> **Goal:** Translate B's approved visual composition into a deterministic, manufacturer-ready Scene Manifest, while retaining A's teaching objective and using C—not any generated lettering in B—as authoritative editorial content. Use D to explain approved creative changes.
>
> **Produce, without rendering the final document:**
> 1. A semantic scene inventory and preservation/delta report.
> 2. Machine-readable `scene-manifest.json`, with the actual checked-in schema version named; common coordinate system, canvas and safe-zone rules; element bounds, owner layer, z-index, allowed components/design tokens, semantic links, exact text refs, hashes and independent evidence references. Do not claim conformance to `scene-schema-v1.json` until the schema is actually available and testable.
> 3. Three worker contracts: **Story** outputs PNG/WebP raster assets without instructional text; **Art** outputs bounded semantic HTML/CSS structural components without SVG; **Text** outputs exact editable semantic HTML sourced from C.
> 4. Validation results by check, with PASS / FAIL / NOT_ESTABLISHED, identified test implementation, and links or reproducible commands. Evidence gaps remain HOLD.
> 5. An independent QA contract that compares actual final output to B for visual intent, C for facts and wording, and A for retained teaching objective. Set measurable thresholds only where the human-approved verification specification provides them.
>
> **Do not:** change the creative direction without a human decision; bake mandatory teaching copy into artwork; substitute SVG, React, Canva or PowerPoint; claim a functional multi-agent dispatcher merely because worker responsibilities are documented; promote a successful build to release approval; overwrite source or approved files.
>
> **Stop conditions:** missing A/C authenticity, missing B/D approval, unavailable required schema, failing Go validation, missing worker evidence, or unverified visual fidelity each blocks only the relevant downstream phase. Report the exact reason.
>
> **Release:** manufacturing and independent verification are downstream operations; final release requires human authorization.

## Short learner analogy

**Theme (A) → Arrangement (B + D) → Conductor's score (manifest) → Sections of the orchestra (Story / Art / Text) → Performance (Go assembly) → Listening and critique (independent QA) → Audience release (human authority).**

This music-theory structural correspondence is instructional. It does not assert literal equivalence between musical notation and software execution or that the design was empirically shown to improve learning.

## Amendment — four independently saved alternatives and human-written selection (2026-10-13)

The **governing rule below supersedes Prompt 1's older one-image output count**. The learner must receive exactly **four distinct full-composite image files A–D**, not a 2×2 contact sheet and not four choices printed inside one infographic. A prompt describing the workflow itself is not an acceptable candidate illustration. All four must match the exact specific NotebookLM source page and subject.

**Reference anchoring preflight (add before generation):** Quote the original reference slide's visible title, subject/hero object, and a distinctive detail. If the input cannot be inspected, or if the output topic changes, report REJECTED_WRONG_SUBJECT. For the first manual simulation, source A is `BOSS_System_Diagnostics.pdf` page 1: `INITIALIZING TELEMETRY: THE ANOMALY`, a smartphone exploded mechanical view, highlighted CPU and amber telemetry rings. Do not substitute `Day Zero: Ground Zero` or a diagram of DraftDeck's architecture. Exact instructional text must ultimately come from separately admitted source C; visible picture text is provisional until reconciled.

**Four design directions:** A precise isometric exploded technical cutaway; B a tactile forensic examination workbench; C a thermal-signal observatory; D a visual cause/effect technical editorial with detailed component subviews. Render each as a **separate 16:9 image**, independently hash and archive. No final instruction-carrying manufacturing layer is produced by this prompt.

**Human creative gate:** the learner records `candidate_id`, candidate file hash, explicit `selection_rationale` (hero, hierarchy, pedagogical clarity, original-source correspondence), approved changes, rejected alternatives and timestamp. No silent approval. The chosen creative image B plus A/C and human-approved D advance to supervisor planning.

**Amend Prompt 2 output:** always return `scene-manifest.json`, `narrative-brief.md`, `worker-criteria.md` and `provenance.json` with actual byte hashes and explicit status. Each negative worker boundary must be enforced in mechanical acceptance tests. Neither a generated image nor a Go compilation establishes visual fidelity. If human selection is missing, stop at HUMAN_SELECTION_HOLD; if required source C is missing, stop at SOURCE_ADMISSION_HOLD.

**Failed-run example:** a generator returning a DraftDeck process infographic rather than a visual reconstruction of the exploded smartphone is a **rejected generation**, never candidate A. A four-image collage about a *different Day Zero lesson* also fails source correspondence, however attractive its design.
