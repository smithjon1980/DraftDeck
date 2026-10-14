# DZ-AUDIO-01 — Governed Podcast Manufacturing and First Proof

**Status:** CANDIDATE / NO APPROVED SCRIPT / NO SYNTHESIS TEST · 2026-10-13  
**Flagship:** *The Discipline of Constraint — From a Single Note to a Governed Symphony*  
**Sequence:** Episode 01 is first. [Episode 02: the Human-Centered AI Triad](episode-02-human-centered-ai-triad/EPISODE_BRIEF.md) is queued next.

## What Gemini contributed in the user-relayed 2026-10-13 critique

Gemini recommended a private ideation system, human editorial gate, source-grounded Scribe, human script lock, TTS synthesis and audio auditor. It proposed four 15-minute editorial acts, with Act 1 validated before spending on Act 2, and an initial five-minute two-speaker proof focusing on verbatim words, distinct voices, pronunciation, targeted correction and measured cost. This was a **reported proposal**, not an executed test.

## What we accept as candidate design

**System A:** NotebookLM/Gemini as internal creative spark, including debate, critique, briefing and Deep Dive possibilities. Their outputs are not automatically public-facing transcripts or final audio.

**Human editorial authority:** define the intended learner capability at the beginning, construct working assessment criteria *with* the audio narrative, review all spoken words and source claims, approve script and performance contract.

**System B:** Scribe drafts with explicitly bounded source access → human approves an exact UTF-8 script → SHA-256 byte-identity & approved voice/delivery manifest → TTS adapter performs only approved words → independent audio QA plus human listening → human release.

Script-lock implementation, TTS model support and automated hash enforcement remain NOT_ESTABLISHED. Designing a skill is not the same as deploying a synthesizer.

## Four-act plan (editorial targets, not guaranteed synthesis length)

| Act | Approx. duration | Lesson | Intended rubric coverage |
|---|---|---|---|
| 01 | 15 min | Why we constrain: failed creative/manufacturing approaches and corrected source anchoring | C-01, C-03, C-04 |
| 02 | 15 min | Note, chord, composition, orchestration; logistics and custody | C-01, C-02, C-05 |
| 03 | 15 min | Private creative spark, human-approved script, need-to-know manufacturing | C-02, C-03, C-05 |
| 04 | 15 min | Feedback, outcome evidence, practice over time, transferable Day Zero curriculum | C-04, C-06, C-07 |

**Rubric development is concurrent with scripting:** define the terminal learner performance before drafting; map each section to a real learner action and assessment item. Do not treat “listened to an hour” as proof of competence or wait for a final external rubric to start.

## First five-minute pilot

1. Source admission: verified exact lesson sources, a concise teaching objective and two editor-defined hosts. Use a synthetic *test script* only if labeled synthetic and not mistaken for authenticated research dialogue.
2. Human-approved script: approximately 600–800 words may yield roughly five minutes depending on speaking rate and pauses; **measure instead of guaranteeing duration by word count**. Note Gemini's proposed 500 words may yield significantly less.
3. Include one intentional 2-second pause, one marked technical pronunciation chosen by the **human**, a short dialogue turn exchange, and one stable turn ID designed for targeted correction.
4. Lock: hash **exact UTF-8 bytes** of script text, record the human selection/approval event and the separately versioned voice/delivery parameters. Do not substitute hash for authorization or for source truth.
5. Run at least one feasible open/local approach and one paid API route under explicit budget permission. Candidate providers: Podcastfy+TTS, Kokoro/Chatterbox, or controlled-script Jellypod, or OpenAI GPT+ElevenLabs; verify that locked script is *not rewritten* by the chosen software.
6. Audit: independent transcript comparison to approved words, speaker mapping and listen-through of all flagged spans plus joins, cadence and factual emphasis. Reject unexpected words/omissions; measure all TTS calls.
7. Patch one intentional defect within a single line, re-run its clip, verify joining quality and hash its final audio; document whether the provider permits this economically.
8. Human reviews report. Only then decide whether to scale to a full 15-minute Act 1.

### Candidate pass/hold decisions

- Text: **zero confirmed added, dropped or substituted spoken words** (not proof of a universal TTS guarantee; automated ASR has its own errors).
- Speakers: every approved turn performed by the intended voice.
- Pronunciation: human-selected rendering of “Bioscillate” and other test terms audibly correct.
- Correction: only the designated clip regenerated, no unintended adjacent changes; if impossible mark the candidate's **segment-patch capability FAIL**, not necessarily the whole product.
- Audio: no clipped words, awkward splices, severe volume difference, copyrighted unlicensed material or unintelligible transitions.
- Data/evidence: versioned script+delivery manifest, provider/model, output clip identity, usage accounting and QA report.
- Failure in these checks means **NOT APPROVED**. Cost/performance rankings come after actual tests.

## Cost accounting (correct units)

Gemini's reported CPAM formula added raw “API tokens + TTS minutes + regeneration waste”; those quantities have incompatible units. The valid metric is expressed in a single currency:

```text
C_direct_USD =
    C_editorial_model_USD
  + C_TTS_initial_USD
  + C_TTS_regeneration_USD
  + C_local_compute_USD
  + C_mixing_storage_USD
  + C_external_QA_USD

CPAM_direct_USD = C_direct_USD / minutes_of_final_human_approved_audio

CPAM_all_in_USD =
  (C_direct_USD + C_human_labor_USD) / minutes_of_final_human_approved_audio
```

Only allocate spending actually incurred or state an estimation method. Do not double count regeneration charged inside a total invoice. Record provider pricing units separately; compare a credible baseline to test whether upfront approval reduces expensive re-runs.

## Claims needing challenge in Gemini sync

- **SSML control is model-specific.** ElevenLabs Eleven v3/v4 don't support SSML break tags; other model families may. Test specific model/endpoint and the syntax it accepts rather than assert all ElevenLabs voices behave uniformly. Official reference: https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api
- **Jellypod “strict read” is NOT ESTABLISHED** just because structured scripts or imported lines are documented; compare actual rendered speech to the imported source.
- **Local TTS zero API cost** does not mean zero compute, setup, electricity or time cost.
- **Most deterministic / unmatched** commercial-quality language should not substitute for a benchmark.
- **500 words = five minutes** is an assumption to measure, not a fact.
- **SHA-256 = lock** is incomplete unless approved source bytes, approval attestation, manifest version and runtime re-validation are all joined.
- **Teaching competency rubric vs audio production QA:** these are distinct test systems; develop both. Script fidelity is not proof that learners understood the lesson.

## Boundaries

Slide production remains paused. Gemini's claimed separately saved skill is not established as a checked-in GitHub file. We created a **new derived skill candidate**, [bioscillate-podcast-planner](../../../skills/bioscillate-podcast-planner/SKILL.md), and request the original Gemini version before treating them as identical. The repository's fixed-count skills metadata schema is unchanged.

No payment, API invocation, locked script, learner test or production release is asserted here.
