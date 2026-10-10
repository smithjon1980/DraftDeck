# BOSS Day Zero · The Missing Interface
## REA Investigation & Tool Readiness Lab — Candidate Lesson Integration v0.1
**Status:** PROPOSED; not approved canon. **Parent:** Solve for the Unknown. **Case:** BOSS-D0-REA-001. **Tool:** REA (optional). **Target:** examples/interactive-checklist/index.html.

### Official instructional placement
Day Zero establishes the learner's initial routing state, evidence habits, and understanding of system boundaries; Day One begins formal building and orchestration. Therefore this is an **orientation/calibration laboratory**, not mandatory reverse-engineering training. Fits *Solve for the Unknown* after IPOS and the "unknown process" / "unsatisfactory output" scenarios, before *The Missing Manual* (source-grounded response) or the Day One handoff. Order within candidate Day Zero sequence requires curriculum-owner approval.

### Learner promise
After the exercise, the learner can (1) describe the observed event without asserting a cause, (2) map Input / Process / Output / Storage, (3) classify known facts, inference, unknown, and NOT ESTABLISHED, (4) distinguish **tool configuration** from **tool capability** and **successful invocation**, (5) explain why a bounded test should produce inspectable evidence, and (6) accurately report a blocked tool route without inventing results.

### Seven-stage progression (bounded 20–30 minute candidate activity)
1. **Observe (3 min):** Show existing DraftDeck interactive checklist example and its intended behavior; identify observations vs claims.
2. **Describe (4 min):** Complete IPOS map: source HTML/JS and user checks → event handling/progress/clipboard → displayed progress/copied text → GitHub source and saved audit.
3. **Diagnose (4 min):** Choose Scenario B (process unknown) or C (unsatisfactory output); use KNOW / INFERRED / UNKNOWN / NOT ESTABLISHED correctly.
4. **Hypothesize (3 min):** State competing explanations and evidence needed to discriminate. No claim of cause without evidence.
5. **Test (4 min):** Select one of three routes: A manual source inspection (no install); B inspect genuine archived REA tool trace if validated and published; C actual REA CLI/MCP call only in approved equipped environment. For blocked environment, create boundary diagnostic rather than fake execution.
6. **Measure (4 min):** Audit **system evidence chain** (availability, retrieval, interpretation, support, uncertainty) **separately** from learner audit accuracy against human reference answer.
7. **Document (3 min):** Submit IPOS worksheet, hypothesis/test table, evidence chain audit, confidence/unknowns, next action and route taken.

### Three accessible pathways
- **A / Core:** Browser-only owned source and prepared case packet. Fully completable without REA or technical setup.
- **B / Guided observation:** Instructor-approved real REA trace, only after captured and source-verified. Not yet available; mark **NOT READY** until checked.
- **C / Optional operator lab:** Call REA from a connected MCP client; pin version and collect logs. **NOT READY** until verified by executable checks.
All pathways must assess the *same reasoning objectives*; only C supports learner claims of personally executing a tool.

### Assessment (two separate ledgers)
**S — system evidence:** source available/unavailable/not established; retrieval surfaced/partial/not surfaced/N/A; interpretation accurate/partial/inaccurate/N/A; citation/evidence support claim/partial/unsupported/no citation; uncertainty appropriate/overconfident/excessively hedged/N/A. Report applicability and reason. Do not score unperformed stages as failures.
**L — learner evidence auditing:** correctly classify facts/inferences/unknowns, select appropriate N/A, identify the actual failure boundary, specify useful next test and justify it with available evidence. Human reference key required before formal scoring. Never substitute S score for L score.

### Reference answer anchors (candidate until verified by reviewer)
Repository source existence and checklist HTML/JS observable on GitHub. The owned HTML declares event listeners, DOM progress updates, clipboard attempt/fallback, reset behavior. Source inspection alone does not prove runtime interaction passes. Gemini Web report states execution boundary blocked; no REA tool result exists to assess. Claimed REA cause diagnosis is NOT ESTABLISHED. A suitable next test: equipped runtime CLI, then separate MCP discovery/call verification. Recorded run requires artifact hash, pinned package, actual schemas, request/output, and reviewer.

### Completion criteria and governance
An accessible learner produces five artifacts: IPOS map, known/inferred/unknown ledger, hypothesis and test, Evidence Chain Audit, and boundary-aware conclusion. Passing requires a human-reviewed reference key and clear rubric, not merely a completed worksheet. No tool access is required for foundation competency. **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

### Implementation dependencies (NOT complete)
- Create a small case packet and human-reviewed reference answer from frozen repo revision.
- Collect actual CLI and MCP execution trace in a compatible environment before publishing B/C as working experiences.
- Create learner worksheet and instructor scoring guide.
- Align lesson placement with approved Day Zero curriculum sequence and update curriculum index only after approval.
- Keep candidate instructional files separate from `doctrine/`; do not silently amend canonical doctrine.

**Release rule:** CONFIG PRESENT ≠ TOOLS CONNECTED ≠ TOOL INVOKED ≠ EVIDENCE VERIFIED ≠ LEARNING ESTABLISHED.
