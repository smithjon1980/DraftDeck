# Day Zero: Build a Stack, Not a Magic Button

Status: Candidate learner insert, not approved for NotebookLM production.

## Outcome
A learner can distinguish a tool from a stack, describe handoff contracts, choose a primary and fallback, and explain why installing a tool is not proof of result accuracy.

## Manual-first lab (no code or installation)
1. Choose a short recording that you are authorized to process; retain the original.
2. Draw the pipeline: MEDIA > ASR > ALIGN > SPEAKER CLUSTER > HUMAN INSPECT > EXPORT.
3. Identify each stage's output: derivative audio, raw text, aligned timestamps, acoustic segments, reviewed script, evidence receipt.
4. Put FFmpeg at media processing; Silero VAD at optional speech activity inspection; whisper.cpp at ASR; WhisperX at alignment; pyannote.audio at speaker clustering; Subtitle Edit at human review.
5. Identify faster-whisper as an alternative ASR engine and Audacity as a manual editing option. Explain that these fallback tools have different interfaces.
6. Imagine the ASR stage fails. Document the failure and how you would select the next authorized tool. Do not claim a transcript was produced.
7. Explain why timestamps do not prove speaker attribution and why two engines agreeing still does not prove exact words.
8. Compose a receipt: input, tool, observed result, what remains NOT ESTABLISHED.

## Concepts in pairs
- Tool versus stack
- Primary versus failover
- Skill versus executable engine
- Evidence receipt versus release authority
- Original versus compressed derivative
- Installation versus verification

## Reflection
What evidence would authorize the handoff? Which errors can compression introduce? When must a human re-listen? Why should historical drafts stay outside the source set for production NotebookLM artifacts?

## Assessment
Learner names eight tools, distinguishes ASR from diarization, identifies two recovery routes, preserves the original recording, and marks any untested claim NOT ESTABLISHED.

Day Zero stays conceptual and manual. Executable automation is a later lesson.
