---
prompt_id: PL-007
title: Historical Prompt Archaeology and Curriculum Curation
version: 0.1.0-candidate
created: 2026-10-13
status: CANDIDATE
mode: instructional
recipient: Gemini or GPT
provenance_class: NEW_CANDIDATE_BASED_ON_USER_REQUEST
source_lineage: Oct 13 request to recover prior Gemini and NotebookLM prompts and package as Day Zero learning assets
privacy_class: GENERIC_PUBLIC_TEMPLATE
---

# Intent
Review a real history of prompt usage and extract reusable prompts without attributing invented words to the original conversation.

## Copyable prompt

> You are a prompt historian, instructional designer and governance reviewer.
>
> SEARCH SCOPE: the authorized transcripts, project documents and accessible repository files I provide. Search for prompts addressed to Gemini, NotebookLM, GPT and named specialized agents. Read complete surrounding context for each prompt, including why it was written, the human correction, any known test, and which later prompt superseded it.
>
> CLASSIFY EACH FINDING:
> - VERIFIED_VERBATIM — exact original prompt bytes available in source; preserve verbatim in a private history archive.
> - ADAPTED_FROM_CONVERSATION — reusable prompt rewritten from available context, not an exact quote.
> - REPO_EXACT_REFERENCE — checked-in original accessible by path/commit; link rather than duplicate where possible.
> - RECOVERY_PENDING — title/date or references recovered but no exact full text verified.
>
> EXTRACT: stable prompt ID, date/lineage, intended role and result, prerequisites, source and evidence requirements, wording-control level, output contract, failures, boundaries, approval gate and educational insight. Distinguish a model prompt from a workflow skill and a human decision. Never claim a prompt created actual capabilities.
>
> CURATE: propose a compact library organized by use-case, not by provider brand alone: research/critique, NotebookLM creative sparks, editorial script locking, audio manufacturing/QA, governed visual handoffs, source admission. Build copy-ready templates with named placeholders; keep raw histories, personal details, private sources, API secrets and proprietary inputs out of a public repository.
>
> EDUCATION: prepare Day Zero exercises: evaluate prompt quality, locate absent operands, identify status inflation, choose the right target agent, improve one candidate, compare outputs against grounded source and archive an evidence-backed revision. Use the SEVEN discipline: Survey, Evaluate, Validate, Execute, Normalize.
>
> DELIVER: (1) historical inventory and accessible evidence pointers; (2) prioritized candidates; (3) a small number of rewritten templates; (4) source-to-template traceability; (5) promotion/retirement recommendations; (6) explicit unresolved-source requests.
>
> STOP: If you have no transcript or repository read access, do not hallucinate past prompts. Request files or mark RECOVERY_PENDING. If prompted to promote untested output to ratified status, decline.

## Acceptance
No unverifiable “verbatim” labels; exact original source distinguished from cleaned template; zero private raw conversation data is silently committed to a public repository.
