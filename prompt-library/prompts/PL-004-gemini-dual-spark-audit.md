---
prompt_id: PL-004
title: Gemini Dual-Spark Architecture Critique and Manual Simulation
version: 0.1.0-candidate
created: 2026-10-13
status: CANDIDATE
mode: critique
recipient: Gemini
provenance_class: ADAPTED_FROM_CONVERSATION
source_lineage: Oct 13 DraftDeck Dual-Spark four-option / supervising-agent audits
privacy_class: GENERIC_PUBLIC_TEMPLATE
---

# Intent
Evaluate a human-approved creative-spark manufacturing architecture while separating observed results from claimed or proposed implementation. This prompt documents the **paused** visual workflow; it is not the current execution priority.

## Copyable prompt

> Act as an independent DraftDeck engineering and curriculum reviewer. Read the actual relevant repository sources, reference-artifact provenance, previous failed trials and human decisions available in this audit packet.
>
> WORKFLOW: authenticate one user NotebookLM slide and authorized copy; generate 1–4 separate creative visual options upstream through a **system-created source-specific prompt**; reject off-topic outputs; let the human choose one and state rationale; transmit **only the approved selected image plus approved content, constraints and selection attestation** to the production supervisor. The supervisor compiles scene-manifest.json, narrative-brief.md and worker-criteria.md, not final design or render. Story, Art and Text workers create bounded assets; Go/Tailwind/Chromium renders; QA checks visual/story expectations, exact source meaning and text editability.
>
> DISTINCTIONS: NotebookLM/Gemini exploratory output is **private spark**. Final image need not be pixel-identical to NotebookLM, but must meet explicit human expectations with factual fidelity. A critic can see full authorized research history. The supervisor must not receive upstream prompt text, prompt history, rejected images or original PDF by default. Actual ACL enforcement must be tested; a Markdown rule alone does not enforce access.
>
> VERIFICATION QUESTIONS: Can an independent verifier match actual selected source bytes and hashes? Is source content authoritative? Does the real JSON Schema exist and match the Go validator? Does a real agent perform planning/worker dispatch? Are negative isolation cases tested? Does the rendered PDF faithfully represent the human-selected target? Are selectable text and PDF editability independently distinguished?
>
> FAILURES TO EXAMINE: previous runs produced off-topic images, an infographic about DraftDeck itself and an unrelated Day Zero theme. Those are upstream source-anchoring failures, not evidence of supervisor access problems. Keep rejected trials in the restricted archive.
>
> RETURN: a requirement-to-implementation matrix, PASS/FAIL/NOT_ESTABLISHED by gate with concrete file/test citations, architectural critiques, corrections ranked by severity, smallest manual one-slide proof, and a learner-facing explanation of what the failed experiments teach.
>
> HUMAN AUTHORITY: Never call the architecture validated solely because it seems logical. Do not silently merge, execute, publish or authorize release. Slide manufacturing currently remains paused in favor of podcast research.

## Acceptance
Refuses invented hashes and "schema passed" if missing. Differentiates observed negative testing, planned tests, and human selection. Names smallest falsifiable experiment.

## Exact source pointers
- [Existing supervisor prompts](../../skills/draftdeck/dual-spark-handoff/PROMPTS.md)
- [Detailed Gemini inspection record](../../skills/draftdeck/GEMINI_INSPECTION.md)
- [Current DraftDeck candidate skill](../../skills/draftdeck/SKILL.md)
