---
prompt_id: PL-002
title: Gemini Podcast-First Governed Production Architecture
version: 0.1.0-candidate
created: 2026-10-13
status: CANDIDATE
mode: critique
recipient: Gemini
provenance_class: ADAPTED_FROM_CONVERSATION
source_lineage: Oct 13 "From NotebookLM Audio Inspiration to a Governed Podcast Production System" Gemini handoff
privacy_class: GENERIC_PUBLIC_TEMPLATE
---

# Intent
Evaluate the deliberate pivot from difficult visual-slide manufacturing to **controlled-script podcast production**, using NotebookLM outputs privately as creative references, never automatic public products.

## Copyable prompt

> ROLE: Gemini independent product architect, technology evaluator and editorial production critic. Review the provided authorized project history, particularly the DraftDeck failures and the reason for shifting priority to audio.
>
> SCOPE: Research and design, not execution or publishing.
>
> OPERATING ASSUMPTION: NotebookLM/Gemini provides **private initial sparks** (Audio Overview, debates, critiques, briefings, etc.). A human chooses the objective and narrows creative possibilities. GPT or another LLM helps draft *grounded, reviewable* dialogue. The human approves and hashes an exact script with assigned speaker turns. The final speech engine performs that script in replaceable segments; independent QA tests what was actually spoken. The producer alone releases.
>
> ARTIFACTS: (A) approved source/lesson brief, (B) episode outline, (C) script and speaker manifest, (D) pronunciation and pacing rules, (E) source claim ledger, (F) production and correction evidence, (G) final recording and human release decision.
>
> TOOL CANDIDATES, TO VERIFY USING CURRENT DOCS/TESTS: Podcastfy; Open Notebook; Podcast Creator; Kokoro FastAPI; Chatterbox; Jellypod; OpenAI GPT API; ElevenLabs. Distinguish open-source licenses from source-available claims, real API methods from marketing, script-import capability from autonomous dialogue generation, and local hosting from fully local data processing.
>
> EDITORIAL MODES: Deep Dive, Debate, Critical Review, Executive Briefing and Instructional Lesson should share source control and manufacturing but have different argument, narration and verification contracts. Avoid claiming feature parity with NotebookLM.
>
> PRIMARY EXPERIMENT: one human-approved five-minute, two-host script with challenging words and a mid-section correction. Produce comparable output using an eligible open-source workflow and a commercial API option. Measure transcript deviations, missing/repeated words, speaker consistency, ability to regenerate only a corrected passage, operator time, inference/API cost, cost per *approved usable minute*, and actual source fidelity.
>
> FINANCIAL HYPOTHESIS: pre-locking an editorial plan and script **might** reduce wasted regeneration and credits, but validation and upstream model calls also cost money. Require measured usage, not guaranteed savings.
>
> RETURN: (1) reasons audio-first may succeed or fail; (2) precise architecture and role permissions; (3) evidence-based provider comparison with caveats; (4) script-lock/versioning and TTS correction contract; (5) five-minute experiment and pass/fail rubric; (6) cost-accounting method; (7) 60-minute flagship episode development plan; (8) prioritized unverified assumptions and next skill candidate.
>
> RESTRICTIONS: No invented benchmark runs, price claims, model capabilities, source access, or API fidelity. Maintain slide-production pause. Do not merge or deploy changes automatically.

## Acceptance
The report must separate documented vendor capabilities from observed performance and must propose a quantitative, reproducible speech-fidelity test. Audio Overview is not public-facing final audio.

## Linkage
PL-003 = private NotebookLM audio spark; PL-005 = technical benchmark.
