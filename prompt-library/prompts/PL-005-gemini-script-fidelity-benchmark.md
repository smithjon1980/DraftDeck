---
prompt_id: PL-005
title: Gemini Controlled-Script Podcast Tool Benchmark
version: 0.1.0-candidate
created: 2026-10-13
status: CANDIDATE
mode: research
recipient: Gemini
provenance_class: ADAPTED_FROM_CONVERSATION
source_lineage: Oct 13 research of open-source NotebookLM podcast alternatives, GPT APIs and commercial production
privacy_class: GENERIC_PUBLIC_TEMPLATE
---

# Intent
Compare potential **word-for-word script manufacturing** systems, rather than comparing the storytelling of automatically invented podcasts.

## Copyable prompt

> You are an independent audio-tool researcher and benchmark designer. We want to **lock a human-approved, source-grounded two-speaker script** before purchasing audio generation. A NotebookLM/Gemini podcast remains a private creative spark. Production must use fixed approved text with reproducible speaker labels and scoped corrections.
>
> RESEARCH THESE CANDIDATES with current official documentation, repository license files, reproducible code examples and pricing where available: Open Notebook, Podcastfy, Podcast Creator, Kokoro FastAPI, Chatterbox, Jellypod, OpenAI GPT API and ElevenLabs. You may identify better-supported alternatives, but distinguish actual evidence from proposals.
>
> VALIDATE PER TOOL: genuine open-source license and terms; can ingest existing script without auto-rewriting? Exact speaker-turn mappings? Public/personal API? Model choice or external GPT pairing? Batch/audio length and per-request chunk limits? Segment regeneration? Voice quality and consistency? Local GPU/CPU requirements? Data sent to third parties? Pricing, rate limits, credits and commercial rights? Active maintenance?
>
> DESIGN ONE FIVE-MINUTE TEST: An approved two-host script containing specific unusual terms, numbers, punctuation, intentional pauses, a speaker switch and a single sentence later amended by the human. Supply script bytes/hash and count actual accepted audio minutes. Use identical editorial content across one open-source and one paid candidate if feasible.
>
> MEASURE: word error rate or carefully defined verbatim-difference rate with punctuation separately checked; transcript confidence limitations; missing/duplicated words; wrong speaker; pronunciation, prosody and breath quality; edit/re-run scope; total generation calls, dollar costs, operator labor and **cost per accepted usable minute**. Human listens to flagged regions; independent ASR is a diagnostic, not an oracle.
>
> PROVIDE: (1) current provider evidence matrix with sources; (2) concrete reproducible minimal scripts and setup prerequisites; (3) privacy and licensing caveats; (4) falsifiable test protocol; (5) total-cost model; (6) recommendation for five-minute test and 60-minute scale-up; (7) all unknown or untested claims marked NOT ESTABLISHED.
>
> No claims that GPT is embedded inside a service when it is merely an external integration. No assumed 60-minute one-click generation. Do not launch paid production or assert observed quality without actually running the experiment and receiving permission.

## Acceptance
Benchmark clearly separates GPT script composition, speech synthesis and audio editing; current vendor claims are sourced and findings are not presented as local performance tests.

## Linkage
PL-002 is the full product architecture brief; PL-003 is the NotebookLM private creative brief.
