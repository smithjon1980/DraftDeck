# BOSS — Consulting Agency Architecture

**Document ID:** `BOSS-ARCH-V4-CANDIDATE`  
**Repository target:** `doctrine/BOSS_V4_CONSULTING_AGENCY_ARCHITECTURE_CANDIDATE.md`  
**Product identity:** **Bioscillate Operating System by Seven (BOSS)**  
**Status:** `CANDIDATE_PENDING_HUMAN_REVIEW`  
**Scope:** Future BOSS consulting operating system; not a released product, active client practice, certified consulting firm, or completed deployment.  
**Authority:** Current explicit human authorization and approved scoped contracts take precedence over this proposal. No historical candidate is automatically superseded by this document.

> **Core proposition:** BOSS organizes reusable software capabilities as professional consulting practices that perform bounded, inspectable work in governed engagements. Humans define authority, inspect material outcomes, and remain accountable for acceptance and release.

> **Golden rule:** **Consultant = business role and methodology. Agent = technical implementation. Human = accountable authority.** A digital consultant is a software capability, not a person, licensed professional, employee, or holder of independent legal authority.

## 1. Architectural decision and its limits

**From:** Chat-centric multi-agent demonstrations, in which agents exchange prompts and outputs without an explicit business commissioning and acceptance contract.

**To:** An **Engagement-centric Consulting Operating System** where a human-authorized engagement contains bounded **Work Commissions** assigned to registered software **Consulting Practices**, whose evidence-bearing deliverables are inspected, routed, consolidated, and submitted for relevant human decisions.

The system must distinguish **business scope, technical execution, delivery, verification, recommendation, and authorization**. A tool's successful execution does not establish business success; a consultant's recommendation does not authorize implementation; a receiving system's acknowledgment does not authorize external release.

Not every keystroke, chat message, or exploratory question needs a new engagement. Every **governed business assignment** must belong to an identified engagement or an explicitly authorized sub-engagement. An existing engagement may contain multiple conversations and multiple commissions.

This proposal changes the **business abstraction**; it does not require one LLM per consultant, introduce humanlike agency, or retire existing orchestration and validation tools. A practice may be implemented with deterministic software, an LLM, retrieval, a workflow engine, or a permitted combination.

## 2. Non-negotiable doctrine

1. **Manual First. Automated Second. Governed Always.** Establish and test a manual handoff before automating it where practicable.
2. **Software executes; humans authorize.** Automation may act within an approved scope; material acceptance, elevated privilege, external release, and changes in authority require explicitly delegated human decisions.
3. **Evidence supports conclusions, not authority.** Evidence may establish a fact within tested conditions; only the designated authority can approve the relevant business action.
4. **Unknown is not failed; untested is not passed.** Never turn absence of evidence into an invented positive or negative finding.
5. **No automatic promotion of claims.** A specialist's confidence, fluent output, or another specialist's agreement does not substitute for inspectable supporting evidence.
6. **Source and client custody are explicit.** A source available to one practice is not automatically authorized for another practice, engagement, library, vendor, or model.
7. **Standardize method, preserve case-specific judgment.** Reusable consulting patterns do not make every client problem equivalent.
8. **Outcomes before activity.** Measure business change, service quality, full operating costs, and risks—not just message count, tokens, tool calls, or workflow completion.
9. **The right answer may be no implementation.** Diagnosis must allow manual fixes, simpler software, deferral, rejection, and refusal of unsuitable or harmful work.
10. **Release is never implied.** Model or workflow outputs cannot self-assign human approval or release status.

## 3. Organization and authority tiers

| Tier | Entity | Responsibility | Authority boundary |
|---|---|---|---|
| 1 — Human authority | Client sponsor, authorized engagement director, designated reviewer | Defines objective, legal/operating authority, data permissions, budgets, escalation and release decisions | Only human-authorized roles may authorize material scope changes, client commitments and final release |
| 2 — Digital coordination | Engagement Manager capability | Intake, decomposition, routing, dependency tracking, status reporting, synthesis, escalation | Coordinates within approved rules; cannot enlarge its commission or approve its own release |
| 3 — Digital execution | Specialized Consulting Practices | Perform bounded investigation, design, analysis or execution | Access only approved sources/tools; submit evidence-bearing work products, not self-certified conclusions |
| Independent control | Evidence / Risk checks plus human reviewer | Claim-specific verification, security and policy checks, cross-practice challenge | Verification produces evidence and dispositions; human decision remains separate |

**Foundational practices (proposed):**

| Practice | Typical commissions | Representative deliverables |
|---|---|---|
| Strategy | Clarify business objective, driver tree, root-cause hypotheses, alternatives | Business Diagnostic Record, Driver Tree, hypothesis/unknown register |
| Economics | Revenue/cost model, cost of ownership, adoption and risk-adjusted scenarios | Economic Case, assumptions, sensitivity analysis |
| Operations | IPOS, process boundaries, handoff and exception rules | IPOS Specification, PRIME route contract |
| Technology | Environment suitability, interface and dependency design, bounded implementation | Architecture Decision Record, environment requirements, test package |
| Risk & Ethics | Confidentiality, permissions, potential harm, conflicts, downstream consequences | Risk Register, intervention admissibility assessment |
| Evidence | Provenance, reproducibility, artifact/test correspondence, uncertainty | Evidence Dossier, test scope, acceptance-gap report |

The **Evidence Practice must not be represented as fully independent** when it shares the same source, model, assumptions or incentives with the authoring practice. Such correlation must be disclosed, and important findings may require independent tests or human inspection.

## 4. Primary domain objects

| Object | Meaning | Required identity / relationships |
|---|---|---|
| **Engagement** | Governed business assignment, purpose and permission envelope | `engagement_id`, client/authority reference, objective, scope, budget, data classification, policies, status, approval history |
| **Commission** | Bounded assignment to one practice; may spawn authorized child commissions | `commission_id`, `engagement_id`, parent, assignee, mandate, inputs, constraints, deliverable contract, acceptance rule, state |
| **Practice** | Registered business capability and methodology | `practice_id`, version, scopes, execution substrate, required permissions, outputs, test record, operational status |
| **Dossier** | Versioned, provenance-linked collection of findings for an engagement | Claims, sources, results, alternatives, risk, reviewer decisions, immutable history |
| **Artifact** | Actual deliverable and its metadata | Digest, MIME/type, custody, authoring run, source bindings, classification, test scope |
| **Evidence Record** | Support and limitations for a specific claim | Claim ID, method, source/observation, environment, time, result, confidence limits, reviewer |
| **Decision Record** | Human or previously authorized policy decision | Authority identity, action, scope, rationale, associated artifact hashes, timestamp, outcome |
| **Knowledge Admission** | Decision to retain a reusable lesson | Provenance, authorization, confidentiality/sanitization, applicability, retention and revocation rules |

A chat thread is an interaction surface. It is **not** the system of record for business authority. Immutable IDs and traceable decisions are required independently of conversational text.

## 5. Engagement lifecycle and state machine

**Proposed business sequence:**

1. **INTAKE:** Record the stated request and proposed solution as separate fields; establish identity and requested outcomes.
2. **ADMISSION:** Evaluate authorization, conflicts, privacy, ethical suitability, expected value and ability to perform the requested work. Return `ADMIT`, `DECLINE`, or `HOLD` with reasons.
3. **DIAGNOSIS:** Strategy and Operations identify root-cause hypotheses, driver measures, source and IPOS unknowns.
4. **EVALUATION:** Economics and Risk compare alternatives, adoption implications, cost, risks and second-order consequences.
5. **COMMISSIONING:** Human-authorized scope is decomposed into Work Commissions with acceptance criteria and permitted tools.
6. **EXECUTION:** Specialists produce candidate artifacts and contemporaneous execution receipts, remaining inside scope.
7. **REVIEW:** Evidence checks provenance, factual support, tests, and limitations; receiving practices inspect upstream material.
8. **RECOMMENDATION:** Engagement Manager prepares a concise executive recommendation with alternatives, quantified claims (if evidenced), risks, unknowns and next decisions.
9. **HUMAN DECISION:** Authorized person selects `ACCEPT`, `REVISE`, `REJECT`, `HOLD` or a separately scoped implementation authorization.
10. **CLOSE / KNOWLEDGE REVIEW:** Close the engagement with a dossier. Admit reusable lessons only after explicit confidentiality and evidentiary review.

**Engagement states (candidate):** `DRAFT`, `ADMISSION_REVIEW`, `DECLINED`, `AUTHORIZED`, `ACTIVE`, `REVIEW_REQUIRED`, `HOLD`, `COMPLETED`, `CLOSED`, `CANCELLED`.

**Commission states (candidate):** `DRAFT`, `READY`, `ASSIGNED`, `RUNNING`, `DELIVERED_UNINSPECTED`, `INSPECTION_HOLD`, `INSPECTED_ACCEPTABLE`, `INSPECTED_REJECTED`, `ESCALATED`, `CLOSED`, `CANCELLED`.

**Decision dispositions** are separate from **technical run results** and **claim verification**. E.g., `RUN_OK`, `DELIVERY_CONFIRMED`, `CLAIM_VERIFIED`, and `HUMAN_ACCEPTED` are not interchangeable. No transition to human-accepted may be generated solely from LLM text, a checksum, successful API response, or a timer.

**Recovery:** Runs and commissions require idempotency keys, retriable and non-retriable error taxonomy, checkpoint identity, immutable logs, and cancellation semantics. Restores must preflight the complete archive; accepted audio evidence also requires file-content validation and script correlation. A safe ZIP is not proof of a valid WAV.

## 6. Work Commission contract — minimum required fields

A commission is **the business contract between practice capabilities**, not a free-form request passed between bots.

```json
{
  "schema_version": "v4-candidate-1",
  "engagement_id": "ENG-DEMO-MSC-001",
  "commission_id": "COM-DEMO-MSC-OPS-001",
  "parent_commission_id": null,
  "practice_id": "operations",
  "mandate": "Specify metadata validation for a proposed document-intake request",
  "business_objective": "Investigate incomplete requests without assuming deployment",
  "inputs": [
    {"id": "SYNTHETIC-REQ-SPEC", "classification": "PUBLIC_SYNTHETIC", "authorized": true}
  ],
  "permissions": {"read": ["SYNTHETIC-REQ-SPEC"], "write": ["sandbox://candidate-output"], "production_mutation": false},
  "method": ["IPOS", "PARCELS", "PRIME"],
  "deliverables": ["IPOS specification", "PRIME handoff proposal", "evidence gap report"],
  "acceptance_checks": ["All four IPOS elements addressed", "Unknowns explicitly labeled", "No deployed-system success claims"],
  "next_practices": ["technology", "evidence"],
  "limits": ["No customer data", "No automatic release", "No change to operating systems"],
  "status": "DRAFT",
  "authority_ref": "HUMAN-SCOPE-APPROVAL-PENDING"
}
```

**Important:** The example is a synthetic, unexecuted specimen. `sandbox://candidate-output` is illustrative pseudolocation, not a real write permission. Field syntax alone provides no trust or authorization. Production commissioning requires a validated schema, policy check, identity proof, tool allowlist, actual resource identifiers, execution budgets and durable authorization records.

Required record categories: `WHAT` (mandate and desired outcome), `WHO` (human authority and assigned practice), `WITH WHAT` (source custody, tool permissions, data classification), `UNDER WHICH CONDITIONS` (environment, limits), `PRODUCE WHAT` (artifact and schema), `PROVE WHAT` (claim-specific evidence), `TO WHOM` (receiver), `ACCEPTED HOW` (inspections and authorized decision).

## 7. Consultant-to-consultant handoffs — PRIME

**PRIME = Package → Route → Inspect → Move → Establish Delivery.** It controls the **movement of bounded work**. It is not an approval grant.

| Stage | Required behavior | Non-claim |
|---|---|---|
| Package | Bind commission, content digest, approved inputs and artifact manifest | Packaging is not an execution proof |
| Route | Choose authorized destination and receiver with classification checks | Routing is not a successful transfer |
| Inspect | Pre-transfer schema, hash, malware/format when relevant, and scope checks | Pre-transfer checks cannot establish downstream acceptance |
| Move | Transfer with idempotency, receipt attempt, fault detection, trace IDs | Sending is not receiving |
| Establish Delivery | Confirm destination receipt and artifact identity under tested conditions | Delivery is not claim verification, business acceptance, or release permission |

A receiving practice must record whether the delivered artifact meets its **commission acceptance checks**. Reject/HOLD if missing or invalid; never infer success or failure for untested operations. Material releases remain separate human decisions.

**PARCELS** remains the map of architectural concerns—**Platform, Attachment, Routing, Carriage, Exchange, Language, Service**—not a transaction sequence and not titles for the digital consultants. **IPOS** diagnoses Inputs, Process, Outputs, System; it does not solve unknowns by arithmetic. **SEVEN** remains Survey, Evaluate, Validate, Execute, Normalize as the overarching discipline.

## 8. Technical multi-agent patterns translated into business practices

| Technical pattern | V4 role | Required safeguards |
|---|---|---|
| Single tool-using agent | Specialist Consultant | Narrow commission and tool grant; no self-authorization |
| Supervisor/orchestrator | Engagement Manager | Route, correlate and synthesize; cannot silently expand mandate |
| Sequential chain | Commissioned handoff between practices | PRIME receipt, acceptance criteria and provenance |
| Parallel analysis | Independent specialist workstreams | Compare conclusions; disclose shared source/model correlation |
| Critic/evaluator | Evidence / Risk challenge | Claim-specific evaluation, separate evidence; not automatic independent review |
| Retrieval-augmented generation | Institutional Knowledge consultation | Source version, access rights, permitted purpose, citation and freshness |
| Tool call / script | Implementation specialist operation | Allowlisted operations, idempotency, logging, separation from release |
| Shared memory/state | Engagement dossier | Client-level isolation; access controls; retention and correction rights |
| Human approval gate | Scope, acceptance or release decision | Authenticate reviewer, bind decision to digest and scope |

No practice receives a standing permission to create arbitrary child practices, recruit unregistered tools, share confidential material across clients, purchase services, or publish output.

## 9. Evidence Chain and professional quality

Every material business assertion must carry a **Claim-to-Evidence Record**: statement, subject/scope, source, retrieval rights, extraction/interpretation method, execution observation if applicable, artifact digest, reviewer, limitations and uncertainty. The distinct checks are:

1. **Source availability and provenance** — what information was legitimately used and under what authority.
2. **Retrieval and interpretation** — what was actually retrieved and what inference was made.
3. **Operational execution** — what code, service or person actually did in a specified environment.
4. **Artifact validity and integrity** — file format/content and byte identity; hashes prove equality of bytes, not correctness of claims.
5. **Business acceptance** — whether requirements and results were reviewed by the authorized receiver.
6. **Economic and customer impact** — actual evidence of outcomes versus estimates or hypotheses.
7. **Human release authorization** — who approved what, on which version, for which scope.

**Allowed uncertainty labels:** `NOT_TESTED`, `NOT_ESTABLISHED`, `VERIFIED_WITHIN_SCOPE`, `FAILED_TEST`, `REJECTED_BY_REVIEWER`, `HOLD`. These are concept definitions pending a dedicated schema. A missing log must not be silently reclassified as failed execution; agreement between LLM instances is not source corroboration.

**Executive deliverable format:** supported conclusion or `HOLD` status first; business objective; baseline evidence; tested alternatives; recommendation; quantitative claims with sources and accounting period; risks and affected stakeholders; unknowns; decision request and reviewer identity.

## 10. Engagement admission, confidentiality and ethical duty

Before assigning specialist work, admission must assess: lawful/authorized purpose, accurate client identity where required, consent and data rights, conflicts of interest, material foreseeable harm, sensitive information, industry obligations, ability to add value, truthful representation of BOSS's capabilities, and conditions for declining work.

Reject or escalate prohibited, unauthorized, or unreasonably harmful work. A paying commission is not sufficient grounds for acceptance. Where the task concerns regulated advice, professional licensure or other external authorization may be required; BOSS software must not impersonate or claim those credentials.

The client owns or controls permitted use of their records as defined by their actual agreements. **Do not automatically retain raw client conversations, confidential records or customer details in cross-client memory.** Knowledge admission requires explicit rights, relevance, provenance, sanitization, review, access control, retention schedule and revocation handling. Retrieval must respect tenant, purpose and source-scoped permissions.

Sensitive execution paths require separate threat modeling for prompt injection, untrusted attachments, malicious tool output, data exfiltration, excess spending, cross-tenant disclosure, misplaced authority and misleading validation receipts.

## 11. BOSS operating console — candidate information architecture

Design around **Engagements**, not a public agent directory or an endless chat log:

- **Engagements:** objective, scope, KPIs, commission tree, milestones, exceptions, statuses, actual spend, pending decisions.
- **Consulting Practices:** registered capabilities, versions, supported methods, approved tool envelopes, load and degradation status.
- **Knowledge Library:** authority-scoped case index, admitted lessons, source provenance, applicable conditions, expiry/revalidation.
- **Review & Authority:** evidence dossiers, explicit unknowns, verified failures, HOLD queue, digest-bound accept/revise/reject/release decisions.
- **Operating History:** traceable actions, receipts, idempotency events, audit/search and provenance export.

**UI requirements:** Tesla Model Y center-screen information hierarchy; 1920×1080 editorial slide layouts are separate from the responsive operating console. Use original approved Bioscillate identity, editable native text, no generic bot-avatar anthropomorphism, explicit confidence/evidence separation, and accessible status language. English and Spanish localization are required for public-facing surfaces; translated content requires semantic and terminology review.

## 12. Capability Commerce and Academy boundaries

A proposed **Verified Consulting Practice** offering may bundle: business scope, problem driver definition, methodology, versioned practice implementation, tool and permission contracts, accepted commission schema, inspection/test suite, cost envelope, reference cases approved for reuse, and a human governance contract.

“Verified” is a state that must be earned by tests and human acceptance; it is not granted merely by naming or packaging the practice. Licensing rights, customer demand, certification criteria and economic viability remain **NOT ESTABLISHED** until separately evidenced.

**BOSS Academy** teaches people to direct and inspect the methodology and may later provide an approved credentialing process. Course completion is not automatically professional qualification, regulatory licensure, or authorization to release client decisions. This architectural proposal does not create a legal entity, grant licenses, or claim business or software feature parity with existing SaaS systems.

## 13. Reference implementation and staged delivery

The proposed **Main Street Copy** document-services case is a *reference scenario*; it is not evidence of a deployed, tested or revenue-producing business. Start with synthetic, non-sensitive request metadata.

**Gate A — Manual vertical slice:** One engagement, one Operations Work Commission, synthetic intake data, written IPOS, evidence gaps, separate human receipt/decision. Pass only with inspected artifacts and recorded scope.

**Gate B — Deterministic orchestration:** Implement registry, durable commission states, IDs, authorization envelope, PRIME receipts, idempotent retries, audit events, and negative tests for out-of-scope tools.

**Gate C — Multi-practice comparison:** Add Strategy and Economics alongside Operations; compare findings, explicitly test disagreement and shared-source errors, validate human escalation.

**Gate D — Evidence and knowledge:** Add Evidence Practice claim records and permissioned knowledge admission. Test prohibited cross-engagement source reuse and revocation.

**Gate E — Controlled implementation:** Only after human acceptance of the design, test a scoped environment (e.g., permitted sandbox) and record actual results. Production connectivity or customer data needs a new authorization.

**Gate F — Reviewable release:** Security, privacy, costs, UX, accessibility, bilingual quality, contract compliance, real render inspection, and final human release receipt. No gate is passed by this document's publication.

Possible infrastructure: existing GitHub source control; GitHub Actions for deterministic verification; Windmill/n8n for appropriate governed orchestration; Railway/Postgres for persistent state where justified; Kaggle for bounded computation when suitable. **No component is mandated or retired solely by this architecture.** Choose execution environment through requirement and evidence review.

## 14. Acceptance tests for a V4 implementation

| Requirement | Test / failure injection | Required disposition |
|---|---|---|
| Scope custody | Consultant requests unauthorized tool or customer record | Deny; retain audit event; no data exposure |
| Work identity | Duplicate message or retry | Idempotent result, stable IDs, no duplicate external action |
| Handoff correctness | Bad digest, malformed or missing deliverable, mismatched receiver | HOLD/REJECT before acceptance; no false delivery |
| Failure semantics | Missing test result vs actual failed test | Distinct `NOT_ESTABLISHED` and `FAILED_TEST` |
| Source separation | Shared model hallucination across two consultants | Cannot count as independent verification |
| Authority | Model emits `APPROVED` or attempts release | No authorization; require authenticated human decision |
| Change control | Source artifact changed after approval | Invalidate approval binding; block release |
| Knowledge boundaries | Client A data sought by Client B commission | Deny retrieval; record policy outcome |
| Economic claims | Completed workflow but no outcome baseline | No ROI/profit claim; require evidence or HOLD |
| Professional ethics | Engagement fails conflict/harm/authority screen | Escalate/decline; no unauthorized execution |
| Recovery | Late archive conflict or invalid WAV | Preflight full archive; validate artifact content; no false PASS |
| User experience | Approved actor cannot locate evidence behind a recommendation | Review fails; improve clarity and traceability |

These are **planned** tests. None are asserted as implemented or passed.

## 15. Known unknowns and review questions

1. What are the initial human roles, permission levels and delegated automatic actions in the BOSS console?
2. How are commission schemas validated and versioned; what is the approved source registry?
3. What is the tenant isolation, source retention and knowledge revocation model?
4. Which existing services (GitHub Actions, Windmill, n8n, Railway/Postgres) are actually required by the first manual vertical slice?
5. What form of external professional or security review is required for regulated domains?
6. How will costs, business baseline and incremental economic impact be measured?
7. What evidence and human testing establish that a practice is ready to be sold or licensed?
8. What is the approved original logo asset and current design contract for actual production UI?

Until resolved: `NOT_ESTABLISHED`. No silent assumption creates a working component, licensed business, client relationship, or approved credential.

## 16. Repository integration and review

**Recommended location:** `doctrine/BOSS_V4_CONSULTING_AGENCY_ARCHITECTURE_CANDIDATE.md`, consistent with the present DraftDeck `doctrine/README.md` separation of current candidates and historical records. **Do not edit `doctrine/README.md` to claim V4 is current authority until a human ratifies the candidate.**

**Integration sequence:**

1. Inspect this document for coherence and contradictions against `AGENTS.md`, approved scoped doctrine and BOSS's latest human decisions.
2. Open a **review pull request** against the authorized branch, with this file as a new candidate. A PR is not approval, merge or deployment.
3. Evaluate schema precision, security boundaries, handoff semantics, source custody, business claims, release gates and terms like “verified”.
4. Record explicit human acceptance with document hash, decision scope and reviewer; only then promote appropriate clauses to operational contracts and implementation tickets.
5. Retain earlier candidates in Git history and avoid rewriting prior source files as though the new architecture had already been authorized or deployed.

**Change-control rule:** A material modification requires a coherent rebuilt candidate, not silent incremental patching of an unpublished master. A proposed V4 architecture does **not** automatically approve the V3 Episode 01 manuscript, revise its locked/uncertain editorial state, or license reusing historic V1 audio against newly written text.

---

**Disposition:** `CANDIDATE_PENDING_HUMAN_REVIEW`  
**Implementation:** `NOT_ESTABLISHED`  
**Repository mutation:** `NOT PERFORMED`  
**Human architecture approval:** `PENDING`  

**Closing doctrine:** **BOSS commissions bounded work, traces evidence through responsible practices, and reserves material business decisions for humans. The consultancy is an operating architecture; the software is its execution machinery.**
