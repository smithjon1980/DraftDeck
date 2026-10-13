# Bioscillate / BOSS — Governed Prompt Library

**Status:** CANDIDATE COLLECTION · 2026-10-13 · Human editorial approval pending  
**Location:** DraftDeck repository feature branch; not merged to main.  
**Relationship:** Supplementary **Day Zero instructional artifact**, cross-project resource for research, podcast, NotebookLM and manufacturing workflows.

## Why this exists

A valuable prompt often emerges after many rounds of clarification, failed experiments, evidence and human feedback. Do not lose it as a transient chat message. This library converts those discoveries into reusable, teachable **prompt contracts**, without representing rewrites as verbatim history.

**Governing principle:** Constraint requires discipline, and discipline sustained over time gets results. Verification establishes whether results are the intended ones.

A **prompt** is a reusable instruction. A **skill** is a repeatable operating procedure with tools, evidence, boundaries and gates. A **source document** supplies information; it is not itself an authorization to publish. A **human decision** is not a model output. A prompt cannot enforce software permissions, actual runtime or source authenticity by itself.

## How to use

1. Locate a task and audience in [CATALOG.md](CATALOG.md).
2. Open the Markdown prompt; fill required inputs and remove none of the grounded evidence/status boundaries.
3. Supply the model with **actual authorized materials**. “Review the whole conversation” never grants access to absent messages or hidden files.
4. Receive a candidate output; check claims, scope, source alignment and status.
5. Record the prompt version and resulting decision in the private run archive. Only manufacturing packets should be minimized to need-to-know.

## Access distinction

**Gemini in a research/critique role:** may receive the full *authorized relevant* history and source bundle; broad context is desirable, but access must actually be provided.  
**NotebookLM:** receives an appropriately admitted and curated instructional source set; generated audio/video/slides/infographics are **private creative sparks**, not auto-approved final products.  
**DraftDeck downstream production supervisor:** receives only selected approved creative asset, authorized exact copy, approved requirements and approval evidence; not upstream prompt history.  
**Public GitHub:** contains reusable genericized instructions and provenance descriptors, **not personal chat transcripts, secrets, private source uploads, access tokens or unapproved source documents**.

These are project role definitions. They do not assert formal government classification or deployed access controls.

## Folder system

- [CATALOG.md](CATALOG.md): register of reusable prompts, predecessors and discovered historical candidates.
- [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md): repeatable metadata and prompt contract.
- [prompts/](prompts/): copy-ready templates (adapted from chat unless labeled otherwise).
- [RESEARCH_BACKLOG.md](RESEARCH_BACKLOG.md): older prompt candidates to recover and source-check.

## Governance

Every accepted library entry needs a stable ID, use-case, intended recipient, required inputs, authorized scope, source lineage, exactness classification, outputs, acceptance tests, and HOLD/STOP triggers. Status is CANDIDATE until the human accepts it. When revising, create a new version or an explicit historical note rather than silently rewriting a supposedly verbatim prompt. Keep prompts separate from production-engine code and from independently verified evidence.

**Next steps:** Human reviews templates; verify historical exact originals where available; add a prompt-selection lesson to Day Zero; test the five-minute approved-script audio-production route before upgrading a template to VERIFIED.

## Existing skills and source archives (links, not copies)

- [Need-to-know creative and supervising-agent prompts](../skills/draftdeck/dual-spark-handoff/PROMPTS.md)
- [DraftDeck manufacturing skill](../skills/draftdeck/SKILL.md)
- [Gemini independent code audit](../skills/draftdeck/GEMINI_INSPECTION.md)
- [NotebookLM controlled source admission and audio customization](../curriculum/day-zero/notebooklm/source-admission-v0.4/GEMINI_NOTEBOOKLM_HANDOFF_READ_FIRST.md)
- [Book-to-Skills extraction workflow](../skills/book-to-skills/SKILL.md)

**Preserve historical conflict openly:** Old DraftDeck React/Canva/SVG-era instructions in root AGENTS.md belong to an earlier workflow; current audio-first research and canonical candidate manufacturing restrictions must not be inferred from that legacy text. The active slide production initiative is paused pending a separate decision.
