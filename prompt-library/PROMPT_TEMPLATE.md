# Prompt Library Entry Template v0.1

Copy this file to a new stable slug under prompts/. Update metadata; do not invent a source reference.

---
prompt_id: PL-000
title: Replace with specific operation
version: 0.1.0-candidate
created: YYYY-MM-DD
status: CANDIDATE
mode: research | critique | creative | manufacturing | QA | instructional
recipient: Gemini | NotebookLM | GPT | Other
audience: learning-author | supervising-agent | researcher
provenance_class: ADAPTED_FROM_CONVERSATION | REPO_EXACT_REFERENCE | VERIFIED_VERBATIM
source_lineage: identify actual date/title and accessible repository files
privacy_class: GENERIC_PUBLIC_TEMPLATE
release_authority: HUMAN
---

## Intent
One narrow decision or artifact this instruction supports.

## Before use
Actual inputs needed; identify which source bytes were inspected. If source is absent, stop.

## Copyable prompt

> ROLE: ...
>
> TASK: ...
>
> INPUTS: ...
>
> FACTUAL AUTHORITY: ...
>
> PERMITTED REASONING: ...
>
> PROHIBITIONS / NEGATIVE CONSTRAINTS: ...
>
> OUTPUT ARTIFACTS: ...
>
> ACCEPTANCE / VERIFICATION: ...
>
> STOP CONDITIONS: ...

## Output review
Measurable tests, permission checks, independent QA and a release decision. Do not say “validated” when only drafted.

## Archival record for a real execution
Run ID, exact prompt UTF-8 bytes/hash, inputs/versions/hashes, model/tool name, invocation timestamp, result hashes, cost if measurable, decision, rejected alternatives and caveats. Keep private values in access-controlled run storage, not in a public template.

## Change log
v0.1 — extracted/adapted. Human review pending.

**Terminology:** “verbatim archive” only if the exact original text is actually preserved and compared; “adapted template” for improved, condensed or reorganized prompts; “historical candidate” for prompts found by reference but not yet recovered in full.
