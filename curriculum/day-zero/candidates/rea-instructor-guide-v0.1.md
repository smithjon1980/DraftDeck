# Instructor Guide — The Missing Interface
**Status:** Candidate · **Parent:** Solve for the Unknown · **Time:** approximately 25 minutes
**Use with:** `rea-case-packet-v0.1.md`, `rea-learner-worksheet-v0.1.md`, `rea-reference-answer-v0.1.md`.

## Mission and accessibility
Teach *how to discover a system boundary and audit evidence*, not decompilation. No software installation is needed for core competency. Optional live REA demonstration is embargoed until actual CLI and MCP traces are verified. Do not grade a learner down for lacking local technical tooling.

## Seven-stage facilitation
1. **Observe (3m):** Provide source/excerpts. Ask what was observed versus what is merely described in code.
2. **Describe (4m):** Elicit IPOS and record actual vs possible output.
3. **Diagnose (4m):** Compare Scenario B (unknown process) and C (unsatisfactory output)—C is hypothetical until a defect is observed.
4. **Hypothesize (3m):** Ask for two plausible explanations and one test that discriminates.
5. **Test (4m):** Route A is always available. Routes B/C require approved real trace/client capability, respectively.
6. **Measure (4m):** Separate S system evidence from L learner assessment. Unexecuted stages use N/A; uncertain access uses NOT ESTABLISHED.
7. **Document (3m):** Verify learner recorded claims, limitations, next action, and source version.

## Learner rubric — dimension scores 0–3, independently scored
| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| IPOS and boundary recognition | No usable map | Major misclassification | Most boundaries valid | Accurate, explicitly qualified |
| Evidence classification | Fabricates or reverses facts | Regularly confuses inferred/known | Mostly distinguishes | Consistently separates claims and unknowns |
| Hypothesis and test | No useful test | Vague step | Test is executable but not discriminating | Test predicts distinguishable outcomes |
| Audit calibration | Claims execution with no trace | Some overclaims | Reports most N/A correctly | Faithfully distinguishes reported/observed, S/L and N/A |

Do not compute a course pass threshold or claim a validated rubric until piloted. Record each reviewer independently; audit agreement after pilot.

## Assessment safeguards
- **S system output** describes what tool/source actually yielded. It is not the learner score.
- **L learner competence** measures accurate evaluation of available S. A blocked tool may be audited expertly.
- Do not give automatic high marks for hedging. Require evidence-linked reasons and useful next test.
- A citation to a source is not proof of support.
- Classify missing downstream execution as **N/A**, not an execution failure or zero quality.
- Source inspection proves declared logic; only execution/test proves observed browser behavior.

## Instructor preflight
Confirm case-packet version and reference source blob match, verify learner can open the supplied materials, verify route A works with browser only. If offering B/C, produce command outputs, artifact hashes, real MCP tool name/schema and tool response, approval record, and accessibility alternative. Remove identifiers/secrets and do not execute untrusted software.

## Release gate
Obtain human approval of packet, key, worksheet and rubric; trial with a learner; inspect accessibility and assessment validity; record version and change radius. Preserve doctrine unchanged. **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**
