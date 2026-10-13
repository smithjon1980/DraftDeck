---
name: bioscillate-podcast-planner
description: Governed, source-grounded editorial planning, immutable-by-approval script locking, TTS handoff and independent audio acceptance for BOSS Day Zero
version: 0.1.0-candidate
status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: PROPOSE_AND_PREPARE_ONLY
original_gemini_skill: NOT_PROVIDED
derivation: CHATGPT_RECONSTRUCTION_FROM_USER_RELAYED_GEMINI_REPORT_2026-10-13
---

# Bioscillate Podcast Planner — Candidate Workflow Skill

**Important lineage:** Gemini's reported analysis said it had “created and saved” a skill with this name. No file with this name was found on DraftDeck's inspected feature branch as of 2026-10-13. This is a **new repository candidate reconstructed from the reported design**, NOT a verbatim import or proof of Gemini's separately saved skill. Request the original Gemini file/export; diff and reconcile before declaring identity.

**Status: SPECIFIED_CANDIDATE / HUMAN_REVIEW_PENDING / NO_RUNTIME_ENFORCEMENT.** This document defines an editorial workflow, not a working TTS adapter, runtime ACL, model connection or approved public media workflow. Do not auto-register it in \`skills/metadata.json\`: that separate schema currently expects exactly 31 listed skills and needs an approved migration before a new entry can be added.

## Why this skill exists

Day Zero is teaching **constraint, discipline, human judgment, feedback and verified results**. The podcast is a medium and case study for those lessons. A NotebookLM/Gemini Audio Overview is a **private creative spark**, not authorized public narration. A human-approved exact script becomes the manufacturing authority.

### Role boundaries

| Role | Default access and responsibility | Must not assert/do |
|---|---|---|
| Source/Research | Authorized historical materials and genuine source evidence; mark authority versions | Treat an unverified summary as primary fact |
| Ideation (NotebookLM/Gemini) | Full actually provided, authorized relevant history to explore alternatives and critique | Release private spark as public final media |
| Human editorial director | Select objective, make decisions, revise, approve exact script and acceptable voices | Assume model agreement proves accuracy |
| Scribe (GPT or other model) | Approved source excerpts, editorial brief and draft/critique permission | Rewrite a LOCKED script while manufacturing |
| Script-lock reviewer | Exact script bytes + approved speaker/voice and pronunciation manifest; record human decision | Claim SHA-256 alone proves human approval |
| Speech engine | Exact approved turns and model-specific delivery instructions only | Interpret source history as license to add/remove dialogue |
| Independent audio QA | Locked script/manifest, generated audio, source evidence to verify | Approve its own public release |
| Human publisher | Verified QA packet, rights and final output | Delegate final decision to unsupervised generator |

**Research context vs production context:** Gemini the independent research critic should receive the **entire relevant history actually shared**, while the manufacturing engine should receive only the approved production contract. These are different roles with different legitimate information needs.

## States and operational steps

1. **SOURCE_INTAKE_HOLD** — identify exact authorized source versions, lesson outcome, claims needing verification and privacy restrictions. If not available, stop.
2. **SPARK_CANDIDATE** — NotebookLM/Gemini privately explores Audio Overview, critique, debate or briefing alternatives. Archive references and limitations; no automatic public use.
3. **EDITORIAL_BRIEF_CANDIDATE** — human names thesis, audience, expected length, intended learner competency and desired narrative route. Draft the **working rubric alongside the episode**, starting with the desired learner end capability. Do not demand a fully ratified external rubric before drafting.
4. **SCRIPT_DRAFT** — scribe writes sections from admitted sources with each spoken line assigned to a stable speaker/turn ID; factual claims trace to sources. Mark reconstructed dialogue as reconstructions, not invented real quotations.
5. **SCRIPT_REVIEW_HOLD** — human reviews exact words, boundaries, speaker roles, pronunciation, tone, licensed content, and whether claims are established. If changed, repeat review.
6. **SCRIPT_LOCKED** — preserve one exact UTF-8 script file with stable line/turn IDs; calculate SHA-256 over **its exact bytes**; separately bind script version, voice assignment, allowed pronunciation/delivery markup, provider/model configuration and human approval record in a lock manifest. The hash establishes byte identity **only**, not content truth or authorization. Every content edit changes the script hash; a performance-rule change versions the manufacturing manifest even if dialogue bytes stay identical.
7. **SYNTHESIS_CANDIDATE** — after explicit approved paid/provider choice and access, synthesize bounded independent turns/chunks. Never assume a library's “podcast” function can skip its internal LLM rewrite; inspect/test before paid use. Store run ID and audio segments with actual model/provider settings and usage.
8. **AUDIO_QA_HOLD** — compare generated audio with authorized words using independent ASR/forced alignment where possible plus human listening for pronunciation, prosody, missing/extra words, line bleed, clipping, joins and rights. A perfect automatic transcript is not proof of fidelity.
9. **PATCH_REVIEW** — if one line fails, determine whether audio-only regeneration with the **same locked words** suffices. Keep replacement lineage and recheck adjacent transitions. Any text change returns to SCRIPT_REVIEW_HOLD and re-lock.
10. **HUMAN_RELEASE_HOLD / APPROVED** — independent QA packet plus explicit human publishing authorization required. A successful generation is not publishing permission.

## Preferred working artifacts

- \`editorial-brief.md\` — intended lesson, sources, private inspirations and 60-minute target; no unsupported runtime promise.
- \`working-competency-crosswalk.md\` — learner performance and assessment evidence co-created with the script.
- \`script-v0.1.txt\` or stable-ordered speaker-turn source — precise, versioned, human-reviewed words.
- \`production-contract.json\` — hashes/refs, voice map, pronunciation rules, delivery metadata, human authorization, gates.
- \`segment-manifest.json\` — segment IDs, source turn IDs, input/payload hashes, audio output hash, status and generation usage.
- \`audio-qa.md\` — measured discrepancies, listening decisions, accepted corrections, linked evidence, unresolved issues.
- \`cost-ledger.csv\` — provider and local compute costs per run and accepted minute.
- \`release-attestation.md\` — final human decision only after all required evidence.
A JSON example schema-shaped *fixture* lives in [production-contract.example.json](production-contract.example.json). It is **not** a validator or locked script.

## Five-minute manual proof — required before 60-minute spend

- Use approximately five minutes of **measured** speech, not guaranteed by any fixed word count. A proposed 500-word sample may be less than five minutes at typical delivery rates; confirm actual pace and plan sufficient representative turns.
- Two approved speakers; one pause; one project-specific word such as “Bioscillate” with pronunciation chosen **by the human**, not invented from model inference.
- Human locks exact words and voice manifest. Compare at least one local/open-source and one commercial option if feasible under approved access and cost.
- Test a deliberate error in one line: can only that line be synthesized again and spliced without unrelated regeneration or an audible join?
- Track dropped/added/reordered words, speaker switches, pronunciation, pause performance, generation and correction requests, dollars, local compute and review minutes.
- PASS for word fidelity requires **zero confirmed substantive added/dropped/spoken substitutions** after human and independent-tool review, not a claim that ASR is infallible. Release still needs sound/mixing/rights/lesson checks.
- Any vendor/model feature, including SSML support and exact imported script, must be validated for the **selected** model/endpoint; do not treat product-level marketing as proof.

## Financial measurement

**Cost Per Approved Minute (CPAM)** = \`total measured equivalent-currency production cost / accepted finished audio minutes\`.

Calculate numerator in consistent money units: editorial model tokens × their prices, original TTS characters/credits/minutes × price, **incremental** TTS correction costs, local compute/electricity as measured or explicitly estimated, storage/mix/QA and optionally labor **with labor-inclusive variant labeled separately**. Avoid double-counting a correction already included in total TTS charges.

Maintain a **comparable ungoverned baseline** before saying script locking saves money. Editorial rigor may raise up-front cost while reducing downstream waste; neither result is assumed.

## Provider boundaries

Podcastfy, Open Notebook and Podcast Creator are *candidates*; exact locked-script bypass is NOT_ESTABLISHED until tested. Kokoro/Chatterbox local sound quality, model stability and hardware demands are NOT_ESTABLISHED locally. Jellypod exact-script import and edit semantics require current API evidence and test. OpenAI GPT + ElevenLabs is a **candidate paid pairing**, not a proven best provider or determinism guarantee. ElevenLabs SSML support is **model-dependent**; some newer model families use audio tags rather than SSML break tags. Preserve original spoken copy separately from provider-specific delivery markup, so adapting instructions doesn't silently change the locked words.

## Negative tests / stop conditions

- Missing human approval or full script bytes -> **LOCK_HOLD**.
- Script hash differs from approved exact bytes -> **LOCK_INVALID**.
- Voice manifest hash/config changed without authorization -> **SYNTHESIS_HOLD**.
- TTS engine adds, omits or rewrites spoken words -> **AUDIO_QA_FAIL**.
- Unverified source fact or inaccurate pedagogy -> **EDITORIAL_HOLD**.
- Unreviewed clip correction or audible join -> **PATCH_HOLD**.
- No verified vendor script-only mode -> do not claim deterministic performance.
- No independent QA or human release -> **RELEASE_HOLD**.

## Related files

- [Day Zero Audio queue and sequence](../../curriculum/day-zero/audio/README.md)
- [Shared working learner competency rubric](../../curriculum/day-zero/audio/COMPETENCY_RUBRIC_WORKING_V0.1.md)
- [Five-minute manufacturing experiment](../../curriculum/day-zero/audio/EPISODE_01_MANUFACTURING_PLAN_CANDIDATE.md)
- [Prompt Library](../../prompt-library/README.md)
- [Response & Decision Library](../../response-library/README.md)
