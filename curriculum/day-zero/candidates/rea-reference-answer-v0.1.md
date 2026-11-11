# Instructor Reference Answer — The Missing Interface
**Version:** v0.1 candidate, *human review required before scored use*. **Packet:** `rea-case-packet-v0.1.md`. Do not show to learners during independent assessment.

## Frozen evidence anchors
- Checklist `examples/interactive-checklist/index.html`, Git blob SHA `528f8e34f2a2b27fe2c485985354877298f976a6`.
- The source `form.addEventListener("change", ...)` calls `updateProgress`; `updateProgress` counts checked inputs and sets `progress.max`, `progress.value`, and `progressLabel.textContent`.
- Clipboard handler first awaits `navigator.clipboard.writeText(output)`; catch branch uses textarea and `document.execCommand("copy")`, then a manual-copy display if necessary.
- Reset handler sets each checkbox's `checked` to false and calls `updateProgress`.
- Gemini environment audit states REA CLI/MCP commands were not executed; its environmental conclusions are self-reported, with no direct shell logs included.
- PR #39 declares the pinned REA adapter; source configuration is verifiable but actual agent connection and invocation are not demonstrated.

## Expected IPOS
- **Input:** owned HTML/JS code, checkbox selections or click actions, optional REA target and invocation inputs.
- **Process:** source-declared DOM construction/event listeners/progress or clipboard handling; for REA path, proposed install → registration → discovery → invocation, which did not run in Gemini Web.
- **Output:** source-declared progress-label updates and clipboard status (runtime success unknown); Gemini's ENVIRONMENT_BLOCKED report, not REA findings.
- **Storage:** committed GitHub HTML and adapter; Gemini report archived as text; **no REA execution artifact**.

## Expected claim classification
1. Source declares checkbox-change listener — **KNOWN** (source fact).
2. REA completed MCP invocation in Gemini Web — **not established as success; explicitly not executed according to report**. Learner may label the success claim *false per supplied report*, or mark successful invocation *NOT ESTABLISHED* if explicitly distinguishing reported absence from independent logs.
3. Browser permissions caused a failure — **INFERRED as a possible explanation**; actual occurrence **NOT ESTABLISHED**. No browser failure is shown.
4. PR contains tool config — **KNOWN**, verified by repository files.
5. Copy button has a confirmed defect — **NOT ESTABLISHED**.
6. REA installation itself is broken — **NOT ESTABLISHED**.

## Acceptable leading hypotheses and tests
- If a **hypothetical** clipboard failure occurs, compare secure-context/permission outcomes versus absence of user gesture; inspect browser console, API availability, and fallback outcomes. Predict which branch would execute. Since no failure was observed, a request for runtime reproduction is also acceptable.
- For Gemini **environment block**, compare current Gemini Web with an authorized equipped runtime: verify terminal, supported Node, npm, then successful CLI `--help`; only afterwards attempt static REA scan and separately MCP discovery+call. Missing shell blocks execution before package behavior can be judged.
- If tool is configured but invisible, check client-specific config discovery, trust/permissions, server startup logs and client tool list. Do not equate CLI run with MCP invocation.

## System-vs-learner scoring
**System S:** Source availability is **available** to this source-based exercise; REA output retrieval **N/A** because no REA invocation occurred. Interpretation accuracy/citation support for an imaginary REA result are **N/A / no citation to assess**. For Gemini's written environment report, evaluate its claims separately; no independent shell trace was provided. Calibration appropriate only insofar as it declines to claim tool success; do not award automatic full accuracy.
**Learner L:** Assess the learner's evidence reasoning independently. A learner can correctly recognize an unavailable tool result and receive strong audit marks even when the system operation was blocked.

## Excluded conclusions
Do not infer a universal cloud prohibition on shell/MCP; do not infer REA failed; do not claim the checklist was executed in a browser; do not claim downstream route B/C evidence exists.

## Verification and review gate
Reference key must be reviewed by curriculum owner/instructor and checked against frozen source/prompt before scored deployment. Preserve changes as a new version, do not overwrite original audit.
