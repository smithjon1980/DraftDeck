# Bioscillate Response & Decision Library

**Status:** 2026-10-13 · CANDIDATE RESEARCH ARTIFACT · HUMAN CURRICULUM REVIEW PENDING

**Companion:** [Prompt Library](../prompt-library/README.md) | [Day Zero lesson](../curriculum/day-zero/RESPONSE_LIBRARY.md)

## Educational purpose before process

This library is **not** a gallery of impressive AI replies. It documents the central lesson:
**"Constraint requires discipline, and discipline sustained over time gets results."**
The process is the case study through which the learner observes the lesson. The underlying concepts are constraint choice, disciplined practice, human judgment, feedback, verification, and the transfer of knowledge.

Our project narrowed its technology, providers, permissions, acceptable source claims and output contracts as we learned. In the *DraftDeck candidate pipeline*, SVG-heavy generation was excluded after recurring low-fidelity results; that is a documented **scope-specific architectural decision**, not proof that SVG is universally defective. Today's podcast-first direction pauses slide production rather than deleting prior evidence.

## What a response teaches

A prompt alone does not show what happened. The reusable unit of research is:

\`\`\`text
PROMPT / HYPOTHESIS
  → MODEL RESPONSE (record original, version and access status)
  → HUMAN INTERPRETATION / REJECTION / CORRECTION
  → CHATGPT + GEMINI CRITIQUE OR RECONCILIATION
  → APPROVED PLAN (if any)
  → EXECUTION OR HOLD
  → EVIDENCE / OUTCOME
  → TEACHABLE CONSTRAINT / NEXT ITERATION
\`\`\`

**A/B/C triad (candidate teaching concept):**
A = ChatGPT (formalization, proposed workflow, execution when tools permit);
B = Human learner/operator (real-world context, constraints, approval/rejection, final authority);
C = Gemini (independent critique, alternative perspectives, review of authorized complete history).
These are **roles**, not ranked authorities. The order of conversation can cycle A↔B↔C↔B↔A; the human is not merely a passive relay. A model's agreement does not verify a claim.

## Distinguish public reusable study from private original evidence

- **Prompt library:** reusable, genericized prompt contracts.
- **Response library:** analyzed outcomes, actual feedback/decisions, supported GitHub links, and what remains unverified.
- **Restricted research archive:** verbatim chat transcripts and Gemini full-text responses, exact prompts/attachments, source/payload bytes and hashes when available, credentials excluded or protected.

The response library is on a GitHub feature branch and should be treated as potentially public. **Do not commit complete private conversations, personal details, unpublished source documents, keys, or raw Gemini responses without a deliberate publication decision.** A public case record can summarize an originally private response, preserving a source pointer and access status. A user-pasted passage is not independent verification of model origin or an automatically authenticated complete transcript.

## Records and trust labels

[CATALOG.md](CATALOG.md) lists cases. [RESPONSE_TEMPLATE.md](RESPONSE_TEMPLATE.md) governs additions.

Use clear evidence/status:
- USER_RELAYED_RESPONSE — Gemini text/analysis supplied by the human in conversation; not independently verified against a Gemini export.
- REPOSITORY_VERIFIED — committed file or commit actually fetched/verified from GitHub.
- ADAPTED_CASE_STUDY — edited research interpretation, not an exact reproduced Gemini output.
- NOT_ESTABLISHED — claim, result, timestamp, hash or test lacking evidence.
- HUMAN_AUTHORIZATION_PENDING — proposed curriculum/production release not yet approved.

A plan and a real-world result are different objects. Record whether a response led to (a) a proposed next step, (b) a human decision, (c) a GitHub documentation patch, or (d) an actually executed technical proof. Don't label any one as another.

## Scope and later expansion

Begin with the Gemini Dual-Spark audit and Gemini audio-methodology audit supplied during the October 13 conversation, paired with relevant prompt-library candidates **by theme**, not by falsely asserting exact prompt-byte provenance.

Future eligible modes: response-to-plan traceability, Debate, Critical Review, Executive Briefing, NotebookLM Audio Overview, podcast script/voice QA, source admissions, and experiments across model providers. Gemini/NotebookLM generated media remains **private ideation sparks** until separately scripted, manufactured, verified and human-released.

**Pinned, not started:** a possible separate podcast about the ChatGPT–Human–Gemini triad. See [TOPIC_PINS.md](TOPIC_PINS.md).
