---
record_id: RL-003
title: Gemini Podcast Architecture Review
date: 2026-10-13
status: CANDIDATE
response_origin: USER_RELAYED_GEMINI_RESPONSE
prompt_match: THEME_LINK_ONLY
original_gemini_skill: NOT_PROVIDED
execution_status: DOCUMENTATION_ONLY
---

# RL-003 — Gemini's podcast-production review and our decisions

## The reported response

The human pasted a ten-part Gemini report supporting the switch to podcast-first research. Its proposed stages were: private NotebookLM/Gemini ideation; human editorial selection; source-grounded AI Scribe; human word-for-word script lock; TTS/local synthesis; independent audio audit. It recommended a five-minute two-host proof, a SHA-256 script identity, targeted regeneration of a failed line, cost per approved minute (CPAM), and four 15-minute parts.

Gemini also stated it had saved a skill named `bioscillate-podcast-planner`. **The original skill file was not supplied, nor found in the inspected DraftDeck feature branch.** The newly committed [candidate skill](../../skills/bioscillate-podcast-planner/SKILL.md) is a reconstruction from the user-relayed report, not a verified verbatim import. Ask Gemini for its original file, storage location, version, and compare the differences.

## What happened while Gemini was out of the loop

The human and ChatGPT committed a [Prompt Library](../../prompt-library/README.md), [Response & Decision Library](../README.md), and a [shared evolving Day Zero rubric](../../curriculum/day-zero/audio/COMPETENCY_RUBRIC_WORKING_V0.1.md). The rubric begins with the learner's desired end capability and matures alongside audio editorial drafting.

The human queued the [Human-Centered AI Triad](../../curriculum/day-zero/audio/episode-02-human-centered-ai-triad/EPISODE_BRIEF.md) as Deep Dive Episode 02 immediately after *The Discipline of Constraint* (Episode 01). The triad is A=ChatGPT, B=Human, C=Gemini, with the human directing, selecting and authorizing. The emphasis is not the tools themselves: the process provides examples for teaching constraint, discipline, judgment and verified results.

The human also requires every future Gemini prompt to demand a live GitHub repository synchronization receipt, not a claim based on a pasted summary.

## Review adjustments

- Convert Gemini's CPAM quantities (tokens, TTS minutes, correction waste) into comparable actual monetary costs before division by accepted audio minutes.
- Bind a hash of exact UTF-8 script bytes to separately authorized human approval and speaker/delivery manifest; a hash alone proves only byte identity.
- The proposed 500-word five-minute test is a draft assumption; measure actual speech time.
- ElevenLabs SSML syntax is model-specific. Eleven v3/v4 do not support SSML break tags. Official reference: https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api
- Pronunciation of project names requires human confirmation.
- Vendor superiority and strict script handling remain NOT_ESTABLISHED until a fair benchmark.
- Separate podcast **manufacturing QA** (word, voice, audible quality) from **learner competency assessment** (can the learner reason, constrain, correct and prove?).

## Recorded outcomes

- [Derived podcast planner candidate](../../skills/bioscillate-podcast-planner/SKILL.md)
- [Five-minute proof and Episode 01 plan](../../curriculum/day-zero/audio/EPISODE_01_MANUFACTURING_PLAN_CANDIDATE.md)
- [Prompt Library](../../prompt-library/CATALOG.md) and [Response Library](../CATALOG.md)
- [Living competency rubric](../../curriculum/day-zero/audio/COMPETENCY_RUBRIC_WORKING_V0.1.md)

No commercial API integration, five-minute audio test, approved locked script or published podcast has been established. The source is the user's pasted report; this case study is an **edited summary**, not an authenticated full original Gemini export.

## Core teaching observation

AI critique becomes productive when the human evaluates it, sets boundaries, preserves disputed claims, and verifies the next result. A model's recommendation is not the same thing as a measured production improvement.
