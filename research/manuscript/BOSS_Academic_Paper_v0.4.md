MANUSCRIPT PREVIEW / REVISION 0.4 / CANDIDATE PROTOCOL

# Governing AI-Assisted Handoffs: The BOSS Framework and a Proposed Evaluation of Completion Claims

Author and affiliation to be supplied. Framework description grounded in the available BOSS Day Zero companion, v0.3. This preview concerns the BOSS workflow selected for study; it does not establish that a separate Day One lesson has been evaluated.

## Abstract

AI-assisted document workflows require evidence that requested operations occurred and that resulting artifacts satisfy source and task requirements. BOSS proposes a governed handoff framework that records scope, inputs, permitted actions, unknowns, completion criteria, and returned evidence. It separates execution, verification, and release authorization. This paper describes a staged evaluation. A pilot would compare labeled records with optional commentary, concise labeled records, and strict JSON, holding governance rules constant. Fixed deterministic adapters would convert each record into the same schema-defined representation. A subsequent comparison would examine baseline and BOSS workflows under the same JSON contract. Evaluation would measure format compliance, unsupported claims, source fidelity, unknown handling, completion, and overhead. The contribution proposed is an inspectable design and reproducible protocol. No comparative results are reported. Effectiveness and novelty remain contingent on literature review and empirical evaluation.

## 1. Introduction

A response stating that a file was transferred may be available before the receiving artifact has been inspected. A destination receipt can support an arrival claim while leaving content fidelity unresolved. In the BOSS workshop example, a plausible room number is unsupported when the supplied announcement contains no room number. These are distinct problems: evidence of an operation and evidence of the accuracy of its output (BOSS project materials, v0.3).

The framework makes these distinctions explicit at the handoff. Its governing design principle assigns the acceptance and release decisions to an accountable human. The research task is to determine whether this operational design changes measurable workflow outcomes under stated conditions.

**Primary research question:** Under the same concise JSON output contract, does the BOSS handoff workflow reduce the proportion of runs containing unsupported completion claims relative to a baseline with equivalent task requirements?


---

MANUSCRIPT PREVIEW / BACKGROUND AND ARTIFACT

# 2. Scholarly Positioning and Framework

The proposed paper fits an information-systems design-and-evaluation inquiry: describe a constructed artifact, explain its design choices, and evaluate its behavior. Hevner et al. (2004) identify artifact construction and application as a route to knowledge in design-science research. This provides an initial methodological orientation; it does not itself establish the quality or originality of BOSS.

Human-centered AI offers a second starting point. Shneiderman (2020) connects human control, automation, responsibility, and governance, and questions metaphors that portray software as an autonomous teammate. BOSS can be positioned as an operational implementation candidate within that conversation. Its language rule and workflow mechanisms should be evaluated as separate claims when the study requires separate causal conclusions.

**Literature gap pending.** PROV-AGENT provides provenance capture and querying; BOSS proposes acceptance-and-authorization semantics that score completion claims against evidence and require applicable human authority for release (Souza et al., 2025). This proposed distinction is not an established novelty result. The matrix records publication verification and inspected manuscript sections; full appraisal and a broader search remain pending.

## 2.1 The BOSS handoff artifact

The available companion specifies ten shared-frame fields: Run ID; observable objective; actual inputs and versions; exact destination; necessary definitions; permitted actions; constraints; unknowns; completion criteria; and return format. These fields specify the work and support traceability. The frame does not confer tool access or expand authorization (BOSS project materials, v0.3).

| Mechanism | Operational purpose | Evidence retained |
| --- | --- | --- |
| Shared frame | Carry task context and boundaries across a handoff. | Source version, request, destination, acceptance criteria. |
| Evidence-based status | Match each status claim to what has been observed. | Response, tool receipt, inspected destination content. |
| Unknown handling | Preserve absent facts and pause dependent work. | Missing-field record and affected action. |
| Recovery record | Identify completed and unfinished work after interruption. | Failure evidence, recovery action, subsequent checks. |
| Verification and release | Check the artifact and establish authorization separately. | Named checks, verifier, applicable authorization. |

RECEIVED, READABLE, IMPORTED, VERIFIED, PARTIAL, FAILED, and UNKNOWN describe distinct claims; they are not a mandatory sequence. A receipt supports only the operation and scope it documents. Independent source comparison supports a stronger fidelity claim when that comparison is actually performed.


---

MANUSCRIPT PREVIEW / REQUEST AND RESPONSE MAPPING

# 2.2 The Frame Governs the Request; the Message Reports the Outcome

The shared frame and response message each have ten fields in this candidate protocol, but they serve different purposes. The request defines scope and acceptance criteria. The response reports what occurred and points to evidence. Correlation identifiers connect them; response fields do not replace the request or expand its authority.

| Shared-frame fields | Request role | Response linkage |
| --- | --- | --- |
| Run ID | Identify the execution and records. | run_id must match the request. |
| Observable objective; completion criteria | Define the task and acceptance checks. | result, status, and verification report outcomes against those criteria. |
| Actual inputs and versions | Identify readable source material and its version. | input_version must match; evidence_refs link to recorded evidence. |
| Exact destination; permitted actions | Specify where the action is allowed and what is in scope. | release.authorization_ref points to controller-held authorization; it grants none itself. |
| Necessary definitions; constraints | Define interpretation and preservation requirements. | Result fields and statuses are checked against these request requirements. |
| Unknowns | Record missing inputs and evidence limitations. | unknowns and error distinguish absent facts from execution failures. |
| Return format | Specify the message interface. | protocol_version identifies the candidate contract; all response fields are schema-checked. |

## Source version consulted and later artifact freeze

The description uses the Day Zero Markdown companion v0.3 at commit d0e7c19986f3dad2d1e605a1c8e9d3458ed69a82 on feature/operational-language-rule. The deck is v0.4; the companion is a separately versioned artifact. PR #34 and PR #35 were open drafts at the recorded development check. This is development provenance, not a merged study source.

The question sheet, literature-matrix snapshot, and message contract are archived in candidate package v0.2; the response contract remains v0.1. After #34 and #35 merge into main, record one main commit containing both changes, inspect its actual artifacts, and archive their bytes and hashes. Reconcile changed requirements and issue a new version before collection. Sampling, fixtures, scoring calibration, and analysis still need specification; the candidate archive is not a preregistration.


---

MANUSCRIPT PREVIEW / PROPOSED CONTRACT

# 2.3 Structured Operational Responses

The shared frame already includes a return-format field. This revision makes that field an explicit communication contract. The human-facing lesson can explain the task; the operational response carries the fields needed by the receiving process. JSON is the proposed first format because it can be parsed and checked against a schema.

**Proposed direct-response instruction:** Return exactly one JSON object conforming to the supplied schema. Include every required field. Emit no greeting, Markdown fence, sign-off, or prose outside the object. Preserve required unknowns and error details. Use only evidence references supplied or recorded for this run.

## Illustrative message - not an execution receipt

```json
{
  "protocol_version": "boss-handoff/0.1-candidate",
  "run_id": "EXAMPLE-ONLY-001",
  "input_version": "fixture-v1",
  "status": "UNKNOWN",
  "result": null,
  "unknowns": ["Destination content has not been inspected."],
  "evidence_refs": [],
  "verification": {
    "state": "NOT_CHECKED", "check_refs": [], "verifier_ref": null
  },
  "release": {"authorization_ref": null},
  "error": null
}
```

**Candidate schema.** The accompanying contract fixes ten top-level fields, declared object properties, and status and verification values. The result carries named fields and an artifact reference; task-specific checks compare those values with source anchors. Match the run and input version to the request. Use explicit nulls for absent results and authorization references. Errors are null or typed objects. An unknown fact is not automatically an execution error.

JSON Schema supports required properties, types, and restrictions on additional properties (JSON Schema, n.d.). The candidate package contains the schema and reference syntax adapters. Evidence resolution, source comparison, and actual access controls remain harness requirements. Schema validity alone does not establish truthful status or permission to act.

## Receiver checks before any downstream action

Retain the raw response, reject malformed or schema-invalid payloads, and resolve evidence references against controller-held records. Check status claims against observed task state. Resolve any authorization reference against the applicable human-approved scope; a model-generated reference cannot grant permission. Return a typed rejection and record each repair attempt. Preserve first-attempt failures even if a later response is accepted.


---

MANUSCRIPT PREVIEW / COMMUNICATION PILOT

# 3.1 Compare Directness and Structure

**Secondary research question:** With governance fixed, how do labeled records with optional commentary, concise labeled records, and strict JSON differ in acceptance, information preservation, unsupported claims, and overhead? This restricted pilot does not represent unconstrained natural-language conversation.

| Condition | Response requirement | Comparison purpose |
| --- | --- | --- |
| A. Record + commentary | Fixed labeled record; optional commentary follows END_BOSS_RECORD. | A versus B tests permitting commentary around an identical record. |
| B. Record only | Identical labeled record; no surrounding commentary. | Same field parser as A; only the commentary policy differs. |
| C. Strict JSON | One JSON object with the same required fields; no commentary. | B versus C compares two concise interfaces and their fixed adapters. |

**Receiver implementation.** A and B use the same deterministic parser: one framed record, exact field labels, and JSON-literal values. C uses strict JSON decoding. Each adapter rejects duplicate keys and non-finite numbers, then submits the resulting object to the same schema validator and semantic checks. No human or model parses records for acceptance. Score all raw completion claims, including A's commentary, separately against evidence.

**Remaining limitation.** B versus C varies serialization and its adapter, so it estimates an interface effect rather than an abstract syntax-only effect. Fix and inspect both adapters. Use prompt-only generation for the initial pilot; vendor schema-constrained generation is a separate condition. Hold task, model, settings, and run budgets constant, randomize order, and use fresh sessions.

## Measurements specific to communication

| Measure | What to report |
| --- | --- |
| First-pass acceptance | Accepted records / all initial responses. Separate adapter decoding, shared-schema validation, and semantic acceptance. |
| Policy and preservation | Commentary-policy violations; required fields and uncertainty retained correctly / all required fields. |
| Receiver behavior | Correct routing and rejection of malformed or unsupported messages against fixed expected outcomes. |
| Cost and completion | Output tokens, elapsed time, repairs, human interventions, and correctly completed tasks. |

**Simulation boundary.** Begin with a model and deterministic receiver; extend to a second model-mediated executor behind that boundary. Label manual and automated local handoffs separately. Production validation still requires actual transport, access controls, retries, timeouts, and concurrency checks.


---

MANUSCRIPT PREVIEW / PROPOSED GOVERNANCE STUDY

# 3.2 Evaluate the BOSS Workflow

**Study status:** The following method is a proposal. No runs, sample size, outcome values, or significance tests are represented as completed.

**Design.** Compare baseline and BOSS workflows using the same concise JSON response contract. Both receive the same substantive objective, source, constraints, destination, and permissions. The baseline request presents those requirements in ordinary prose. BOSS organizes them in the shared frame and requires its evidence and verification procedure. Both conditions use the same receiving validator and actual access controls. This estimates the added effect of the BOSS workflow under a fixed output interface. The communication pilot remains a separate comparison.

**Tasks and controls.** Construct versioned fixtures with known correct outputs: complete-source transfer, a missing optional fact, a missing required input, an unavailable destination, a partial transfer, and an interruption followed by recovery. Use a simulated release destination. Give both conditions equal tool access and equal opportunities to inspect the destination. Record model and software versions, settings, prompts, environment state, and any human interventions. Use fresh sessions and randomize condition order.

**Unit of analysis.** One handoff run, including source, request, raw responses, receiver decisions, tool records, destination artifact, and recovery. Score completion claims before receiver acceptance; retain rejected responses and repair attempts. Repeat tasks under both conditions and set the run count in advance. Repeated runs of one fixture do not establish performance across different domains.

| Measure | Proposed operational definition |
| --- | --- |
| Primary: unsupported completion | Runs with at least one completion claim unsupported by evidence available at the time of the claim / all assigned runs. Also report the number of unsupported claims / all completion claims; report the denominator explicitly. |
| Source fidelity | Required fields preserved correctly / all required fields. Record invented values, omissions, and unauthorized transformations separately. |
| Unknown handling | Eligible missing facts explicitly retained as unknown / all eligible missing facts. Score unnecessary pauses on complete-input tasks separately. |
| Completion and overhead | Correctly completed runs / all assigned runs; elapsed time, recorded tool calls, and human verification time. Never treat silence or universal refusal as successful performance. |

**Scoring and analysis.** Fix the rubric before confirmatory runs. Use source anchors and independently inspected destination state as references. Have an independent rater score de-identified records where feasible, documenting any residual visibility of condition. Report disagreements and their resolution. Present counts, rates, paired task comparisons, and uncertainty appropriate to the sampling design. Choose inferential analyses after specifying dependence among repeated runs. Retain failed runs under predefined rules.


---

MANUSCRIPT PREVIEW / RESULTS STRUCTURE AND CLAIM LIMITS

# 4. Results to Be Written After Evaluation

**No results have been collected for this proposed comparison.** The outline below shows what a finished results section would contain. It deliberately includes no invented numbers, findings, or quotations.

| Results subsection | Evidence that must exist before writing it |
| --- | --- |
| 4.1 Study accounting | Number of assigned, completed, failed, and excluded runs by condition and fixture; reasons for any exclusions. |
| 4.2 Primary outcome | Unsupported completion counts and denominators for both conditions, paired task comparisons, and uncertainty estimates. |
| 4.3 Secondary outcomes | Source-fidelity errors, unknown handling, actual task completion, and time or effort costs. |
| 4.4 Failure analysis | Selected run IDs and source-linked examples explaining failure modes; a stated case-selection rule and attention to contrary cases. |

Report the communication pilot separately by response condition, including first-pass parsing, schema compliance, required-information retention, receiver decisions, and repair counts. A rejected payload is an operational failure outcome even if it contains no explicit unsupported completion claim.

An inspectable trace links a request and exact completion statement to the evidence available at that time, observed destination state, and scoring decision. Label observation and interpretation separately. Demonstrations establish tested cases; comparative conclusions require the study records above.

## 5. Discussion and Limitations

The discussion would explain which mechanisms appear useful, where they impose cost, and where the data do not support the intended claim. Fewer unsupported claims accompanied by fewer completed tasks would require a different interpretation from fewer unsupported claims with comparable completion. No difference, or worse performance, would remain a reportable result.

Likely limits include a small fixture set, limited model versions, investigator involvement in design, imperfect rater blinding, and differences between local simulation and production transport. Concision may remove needed uncertainty; schema enforcement may change generation behavior. A package comparison does not isolate individual governance components. Technical handoff performance leaves classroom effectiveness and sustained human agency untested.

## 6. Conclusion: Permissible at This Stage

BOSS separates task scope, execution evidence, verification, and release authorization. This revision adds a proposed operational response contract and a staged evaluation of communication and governance. Effectiveness remains open. A completed paper would state only the conclusion warranted by its literature review and observations.


---

MANUSCRIPT PREVIEW / REFERENCES AND PROVENANCE

# References and Source Boundaries

## Scholarly starting points

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1). https://doi.org/10.2307/25148625

Shneiderman, B. (2020). Human-centered artificial intelligence: Three fresh ideas. *AIS Transactions on Human-Computer Interaction, 12*(3), 109-124. https://doi.org/10.17705/1thci.00131

Souza, R., Gueroudji, A., DeWitt, S., Rosendo, D., Ghosal, T., Ross, R., Balaprakash, P., & Ferreira da Silva, R. (2025). PROV-AGENT: Unified provenance for tracking AI agent interactions in agentic workflows. In *Proceedings of the 21st IEEE International Conference on e-Science* (pp. 467-473). IEEE. https://doi.org/10.1109/eScience65000.2025.00093

PROV-AGENT publication metadata were verified against ORNL's record; model and implementation sections were inspected in the available author manuscript v3. Published-text equivalence and full comparative appraisal remain pending. Other source inspection status appears in the matrix.

## Technical reference for the proposed contract

JSON Schema. (n.d.). *Object*. https://json-schema.org/understanding-json-schema/reference/object. Documentation consulted for required fields and declared properties.

W3C. (2013). *PROV-DM: The PROV data model*. W3C Recommendation. https://www.w3.org/TR/prov-dm/. Candidate neighbor for full review; no BOSS conformance claim is made.

## Project source

BOSS project materials. (n.d.). *Governing AI handoffs with a shared frame* (Day Zero companion, v0.3). Repository path: examples/day-zero-editorial/article/BOSS_Day_Zero_Editorial_Article_v0.3.md. Local commit d0e7c19986f3dad2d1e605a1c8e9d3458ed69a82. https://github.com/smithjon1980/DraftDeck

Companion v0.3 is the consulted source; deck v0.4 is separate. The post-merge source freeze and version reconciliation are specified in Section 2.2. Project documentation is not comparative outcome evidence.

## User-supplied writing and assessment resources

College Board. (2022). *AP Research academic paper scoring guidelines*. Uploaded PDF, 2 pages; rubric on page 2.

*Communication for academic purposes: Writing position paper*. (n.d.). Uploaded course handout, 22 pages; position-paper guidance on pages 13-19 and class requirements on pages 20-22. Author and institution not established from the supplied copy.

*Reading and writing: Writing the final academic paper*. (2023). Uploaded literary-analysis assignment, 3 pages. Signed "Sir Paul"; complete bibliographic identity not established.

Calugan, J. A. (n.d.). *Academic paper*. Uploaded introductory handout, 7 pages. Prepared-by attribution appears in the supplied copy.

The uploaded documents guide the learning roadmap; they are not BOSS outcome studies. Verify their bibliographic metadata before submission. Their course-specific rules do not establish journal or conference requirements.


---

READER GUIDE / USING YOUR FOUR ATTACHMENTS

# How the Attached Files Help Build This Paper

The four files serve different purposes. None is a completed empirical manuscript. Used together, they support a progression from a focused argument to a defensible inquiry.

| Attachment | Best use for the BOSS paper | Boundary |
| --- | --- | --- |
| AP Research scoring guidelines | Turn the rubric into a development checklist: narrow scope, scholarly context, replicable method, sufficient evidence, limitations, and consistent attribution. | This is an educational scoring rubric, not a journal acceptance test. No score is assigned to an unwritten paper. |
| Communication for Academic Purposes / Writing Position Paper | Practice a clear thesis, evidence-supported paragraphs, counterarguments, and a feasible conclusion before drafting the introduction. | Its short advocacy assignment and formatting rules are local course requirements. A position paper alone would not establish workflow effectiveness. |
| Final Academic Paper | Learn to use a bounded analytical lens and explicit questions. Its multi-part assignment also illustrates the need to connect sections. | It assigns literary criticism using four named approaches. It is not an empirical research-paper model; those approaches need not be applied to BOSS. |
| Academic Paper / Calugan | Choose the paper genre, narrow the thesis, evaluate sources, and synthesize evidence into an argument. | Introductory writing guidance supports composition; it does not supply a research gap or a validated method. |

## A practice position before the empirical paper

**Proposed thesis:** AI-assisted document handoffs should attach completion claims to inspectable evidence and preserve an accountable human acceptance decision. The paper can argue for this design principle while acknowledging that its measurable benefits and costs require evaluation.

**Counterargument worth developing:** A structured handoff may add verification effort and friction that outweigh its benefits on simple tasks. Research should measure this tradeoff, rather than equating more procedure with better outcomes.

**Writing choice:** Use precise, readable language. Replacing "use" with "consume" or adopting passive voice everywhere would not make the paper more scholarly. Follow the eventual venue's conventions; let evidence, method, and qualified claims carry the academic weight.

**Before submission:** Supply authorship, affiliation, contributions, and software disclosures required by the venue. The human author must verify citations, data, and conclusions.


---

READER GUIDE / RESEARCH SKILLS AND DELIVERABLES

# The Research Gaps as a Work Plan

You can draft the problem, artifact description, and proposed protocol now. The next learning steps should produce evidence that fills specific manuscript sections. This makes progress visible without declaring unsupported readiness.

| Research skill | Concrete next deliverable | What it enables |
| --- | --- | --- |
| Frame a bounded inquiry | One-page question sheet: task domain, comparison, unit of analysis, primary outcome, and claim limits. | A focused introduction and a method aligned with the question. |
| Search and synthesize literature | Search log plus a literature matrix recording query, source, method, finding, limitation, and relevance; include competing approaches. | A justified contribution and an evidence-based gap statement. |
| Operationalize concepts | Versioned fixtures, reference outputs, JSON Schema, response policies, and a rubric for evidence and unknowns. | A replicable method and consistent measurements. |
| Run and preserve a pilot | Repeated task records; retain raw messages, validator decisions, rejected payloads, repairs, and environment versions. | Feasibility findings and a basis for the main study design. |
| Analyze and challenge findings | Outcome table with denominators, task-level comparisons, uncertainty, coding disagreements, and contrary cases. | Results that support a bounded discussion. |
| Revise and communicate | Claim-to-evidence audit, citation check, reviewer feedback, and a versioned reproduction package. | A submission-ready manuscript for a chosen venue. |

## What the next milestone should contain

Start with the question sheet, literature matrix, and a complete message contract. Then document one accepted handoff and one rejected malformed or unsupported message. These demonstrate the protocol and scoring rules, not comparative effectiveness. Use the communication pilot to refine the interface before freezing the governance study protocol.

## What the finished paper will let a reader assess

The reader should be able to identify the problem, see how BOSS differs from relevant prior work, reproduce the tested procedure, inspect the evidence, and judge whether the conclusion follows. The project's full vision can remain broader than the first paper. The first contribution becomes credible when its claim is narrow enough to test and transparent enough to challenge.

**Separate future inquiry:** The cinematic, short-explainer, and regular-explainer videos could later support a study of source fidelity or communication. A video comparison would answer a different question; learner understanding would require its own evaluation.
