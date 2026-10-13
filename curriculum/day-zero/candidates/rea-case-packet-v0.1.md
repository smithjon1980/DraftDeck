# Case Packet — The Missing Interface
**Case:** BOSS-D0-REA-001 · **Version:** 0.1 candidate · **Scope:** owned DraftDeck interactive checklist and Gemini environment report
**Source anchor:** `examples/interactive-checklist/index.html` (Git blob SHA `528f8e34f2a2b27fe2c485985354877298f976a6`). This is a Git object ID, not a computed SHA-256 checksum.
**Supporting report:** `archive/day-zero/rea/2026-10-10-gemini-execution-audit-v0.1.md`. This describes Gemini's own reported capability limitations; independent shell traces were not supplied.

## Learner-facing evidence
A DraftDeck checklist page declares checkboxes, a progress indicator, Copy checklist and Clear selections buttons. Source code contains a `change` listener that calls `updateProgress`, whose function counts selected boxes and updates the progress value and label. A Copy action attempts `navigator.clipboard.writeText`; after failure, it tries a textarea plus `document.execCommand("copy")`, and provides text for manual copying if that fails. A Reset action sets boxes to unchecked and calls `updateProgress`.

A separate REA tool adapter appears in PR #39. It declares a pinned REA package and MCP server entry. In a Gemini Web session, the operator asked for a REA tool test. Gemini reported it had no shell or local stdio-MCP capability. **No REA CLI command or MCP invocation was executed in that session.**

## Boundary questions
A. If the checklist's copy button appears unresponsive, which facts and unknowns must we separate before saying why?
B. Does reading a code path prove that clipboard writing works in a particular browser?
C. Does a committed `.mcp.json` establish that REA ran?
D. What test could distinguish a missing-capability environment from a faulty REA package?
E. Which outcome is **NOT ESTABLISHED** by this case?

**Prohibited inference:** Do not claim an actual copy-button defect, a successful REA scan, or an MCP call. This is an open diagnostic exercise, not a verified-cause defect packet.
