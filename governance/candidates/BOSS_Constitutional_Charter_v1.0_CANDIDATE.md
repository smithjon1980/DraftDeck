# BOSS Constitution of Command, Skills, Research and Release
## Proposed Founding Charter v0.1 · 10 October 2026
> **DRAFT FOR RATIFICATION.** A project-governance instrument expressed in statutory form; not a claim of public-law force, legal incorporation, democratic representation, or constitutional status under any nation. Nothing here replaces applicable law, contracts, privacy duties, institutional research review, or licenses.
### Preamble
We establish a human-accountable system for the creation, movement, inspection, teaching, and release of work accomplished with computational agents. Authority shall not arise from confidence, verbosity, model identity, possession of a key, a tool connection, or a successful build. All acts shall remain bounded by purpose, evidence, consent, and accountable human release.
## Article I — Supremacy and scope
**§1.** This Constitution states BOSS-wide constraints. Derivative constitutions for skills, research projects, and products may strengthen, but shall not weaken, those constraints.
**§2.** The structural formula is **Constitution = why/limits; PARCELS = where; PRIME = how**. The seven layers of PARCELS are Platform, Attachment, Routing, Carriage, Exchange, Language and Service. PRIME means Package, Route, Inspect, Move, Establish Delivery.
**§3.** These systems are pedagogical and organizational analogies. Humans are not CPUs; AI models are not political subjects; layers are not literal OSI networking functions.
## Article II — Human command and professional boundaries
**§1.** Every released artifact must have a named accountable human or institution with actual delegated authority.
**§2.** The Academy may define learner progression from novice to qualified Commander only by demonstrable capability in selecting tools, setting limits, interpreting evidence and governing release.
**§3.** Tool fluency confers neither software-engineering credentials nor authority to make clinical, legal, financial or high-impact judgments beyond competence.
**§4.** Developers, security practitioners, artists and subject experts retain professional authorship and attribution; the Commander coordinates rather than appropriates their expertise.
## Article III — Two chambers of review
**§1. Human Review Chamber:** learner welfare, consent, accessibility, fairness, licensing, educational assessment, commercial representations and mission alignment.
**§2. Systems Review Chamber:** tool readiness, code, interface schema, dependencies, reproducibility, provenance, performance, security and verification sufficiency.
**§3.** A review chamber may be implemented as a documented review function; no claim of electoral representation is implied. Learners may submit feedback directly; voting or delegated representation is not established until separate rules are ratified.
**§4.** Neither chamber alone gains release authority merely by approving a review. A properly designated human release authority accepts, rejects or holds the resulting recommendation.
```mermaid
flowchart TB
  K[BOSS Constitution] --> H[Human Review Chamber]
  K --> S[Systems Review Chamber]
  H --> J[Joint recommendation / conflicting findings recorded]
  S --> J
  J --> RA{Designated human release authority}
  RA -->|approve with evidence| RELEASE[Release and version]
  RA -->|hold| HOLD[Repair / collect evidence]
```
## Article IV — Constitutional rights and duties of participants
**§1.** Learners are entitled to intelligible learning goals, accessible baseline routes, honest capability disclosures, meaningful assessment feedback and notice of uses of submitted work.
**§2.** Learners may decline optional data contribution or marketplace activity without automatic loss of educational credit.
**§3.** Humans shall receive credit for attributable creative or development contributions under applicable agreements.
**§4.** Human privacy, licenses, safety and retention obligations supersede experimentation convenience.
## Article V — Skills as governed instruments
**§1.** Each skill shall possess a **Skill Constitution** recording scope, exclusions, required inputs, permitted tools, authorization boundaries, environment checks, evidence contract, fallback behavior, tests, failure states, external dependencies, versions, approvers and amendment procedure.
**§2.** Skills shall not silently install software, access secrets, publish content or grant themselves permissions outside an approved execution envelope.
**§3.** Each substantive capability must pass readiness stages: Environment → Dependency → Registration → Discovery → Invocation → Evidence verification.
**§4.** A tool configuration is not evidence of connection. Tool connection is not evidence of invocation. Invocation is not evidence of task correctness.
```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Inspected
  Inspected --> Verified: relevant tests + evidence
  Inspected --> Held: missing evidence
  Verified --> Released: human authorization
  Held --> Inspected: corrected scope
  Released --> Retired: new version or revocation
```
## Article VI — Data, source, provenance and verification
**§1.** Originals shall be preserved unchanged, with digest, origin, version and rights status; derived outputs shall retain source linkages.
**§2.** Missing facts must be marked UNKNOWN or NOT ESTABLISHED, not filled by plausible invention.
**§3.** Evidence of transfer, receipt, format compliance, destination fidelity, approval and release shall be recorded as separate claims.
**§4.** Reproducible tests, negative controls, independent review and appropriate denominators should be used where warranted.
## Article VII — Research Integrity Constitution
**§1. Intention.** Research shall evaluate specified claims rather than promote BOSS through untested success statements.
**§2. Construction.** Every academic document shall distinguish theoretical model, system implementation, demonstration, pilot, and comparative study.
**§3. Pre-specification.** Research questions, outcomes, eligible populations, denominators, fixtures, randomization, settings, exclusions, and review procedures shall be fixed before any confirmatory analysis.
**§4. Provenance.** Retain raw prompts, sources, run IDs, tool versions, provider/model identifiers, complete errors and evidence digests where permitted. Raw evidence shall not be overwritten by interpretation.
**§5. Fair comparisons.** Compare models against the same frozen evidence packet, report exposure/settings differences, distinguish execution quality from a model's judgment, and separate human learner assessment from tool success.
**§6. Claim discipline.** No speculative sample size, statistical significance, novelty, efficacy, superior performance or verified editability shall be published as an observed result.
**§7. Review.** Require source check, diagram review, bibliographic audit, relevant ethics/rights review, and recorded human approval before research release.
**§8. Corrections.** Revisions shall append or version corrections; never erase contradictory runs.
### Academic document construction control
```mermaid
flowchart LR
  RQ[Research question] --> PRO[Protocol / frozen measures]
  PRO --> FIX[Versioned fixtures]
  FIX --> EXEC[Actual executions]
  EXEC --> RAW[Immutable evidence + failures]
  RAW --> EVAL[Independent scoring]
  EVAL --> CLAIM[Bounded interpretation]
  CLAIM --> REVIEW[Human/research review]
  REVIEW --> PUB[Versioned manuscript]
```
## Article VIII — Visual representation and diagrams
**§1.** Mermaid and PlantUML are permitted as editable semantic source. A rendered diagram is supplementary, not a replacement for its source.
**§2.** Each figure must carry a figure number, title, descriptive caption, version and status (Observed / Proposed / Illustration).
**§3.** Diagrams may not imply deployment, causality, authorization, or efficacy where unverified.
**§4.** BOSS identity shall use approved branding; visual polish does not supersede evidence or accessibility.
## Article IX — Releases, amendments, and retirement
**§1.** Each proposal records scope, source references, change radius, reviewer, decision and effective version.
**§2.** Amendments require review through both functions where relevant, human approval, and versioned release; unapproved drafts remain drafts.
**§3.** Retirement means displaced from active use, **not deletion**. Original records remain accessible under applicable retention policy.
**§4.** Emergency holds may prevent harm; they shall be documented and reviewed afterwards.
## Schedule A — Skill constitution template
```yaml
skill_id: CANDIDATE
purpose: UNKNOWN
owner: UNASSIGNED
parcels_primary_layer: UNKNOWN
prime_stages: []
inputs_and_source_rights: []
permitted_tools: []
forbidden_operations: []
capability_preflight: []
response_and_evidence_schema: UNKNOWN
fallback_path: UNKNOWN
verification_profile: UNKNOWN
release_authority: UNASSIGNED
amendment_review: UNASSIGNED
```
## Constitutional gap register
| ID | Unsettled matter | Required ratification |
|---|---|---|
| C01 | Who appoints human reviewers, terms, conflicts of interest | Governance role charter |
| C02 | Learner direct participation or representative system | Consultation and rights policy |
| C03 | Human Commander qualification and appeal | Academy credential standard |
| C04 | Distinct professional developer relationship | Authorship/credit and contracting policy |
| C05 | Data consent, deletion, private source material and IP | Privacy and licensing controls |
| C06 | Which skills require higher-risk safety review | Risk-tier matrix |
| C07 | Actual research ethics oversight and institutional status | Named reviewer/institution; avoid claiming IRB approval |
| C08 | Final ratifier and formal effective date | Signed approval record |
**Ratification block:** Proposed by: BOSS project team / Human ratifier: __________ / Date: __________ / Accepted version: __________ / Dissent or reservations: __________.
---
# v1.0 CANDIDATE — CONSOLIDATED CONSTITUTIONAL ARTICLES
Date: 10 October 2026. Status: REVIEW DRAFT; NOT LEGAL CERTIFICATION; NOT PRODUCTION RATIFICATION.
This addendum takes precedence as a proposed revision wherever earlier v0.1 candidate wording conflicts. Prior sections are retained for historical comparison. BOSS is an operating system that creates and governs subordinate systems; it does not independently confer legal authority.
## Article I — Definitions and Jurisdiction
“Kernel” means the BOSS mandatory policy and verification layer; “Subordinate System” means a governed workflow, skill, service, or application; “Commander” means an authorized human operator, not a licensed professional by virtue of rank; “Verified” requires evidence appropriate to the claimed operation. Applicable law supersedes this private charter. CONSTITUTION governs why/limits; PARCELS locates responsibility; PRIME sequences work; IPOS defines input, processing, output, and storage correspondence.
## Article C01 — Boundary
BOSS specifies design, authorization boundaries and audits. Practitioners and organizations retain responsibilities according to actual conduct, contracts and law; the Charter cannot assign all liability by declaration.
## Article C02 — Misuse
Knowingly bypassing mandatory logging, fabricating evidence, concealing external-state changes or exceeding authority is prohibited. Pre-authorized, bounded automation is permitted where risks, permissions, stop conditions, logs and escalation are defined.
## Article C03 — Amendment
Constitutional changes require a recorded proposal, impact and risk analysis, evidence appropriate to the change, independent review where necessary, and approval by a designated human constitutional authority. Emergency fixes may be expedited but require subsequent review and version documentation. Telemetry alone is not always necessary or sufficient.
## Article C04 — Engineering Referral
A Commander shall initiate documented qualified-specialist review when actual implementation introduces security-critical primitives, custom cryptography, production infrastructure complexity, regulated data processing or comparable engineering hazards outside approved competence. Handoff records shall include trigger, owner, technical acceptance, evidence and sign-off. Neither routine code generation nor job title alone determines competence.
## Article C05 — Adjudication
Decisions shall weigh preserved traces, source and configuration records, independent verification and relevant human evidence. Absent logging requires UNKNOWN or NOT ESTABLISHED classification and investigation; it does not alone prove misconduct.
## Article C06 — Enforcement
Control failures trigger proportionate findings, restricted privileges or remediation as justified. Credible urgent threats permit immediate temporary containment under predefined authority, followed by documented review and restoration criteria; ordinary cases include notice and appeal.
## Article C07 — Research and Human Protection
Technical telemetry is not evidence of educational efficacy. Research involving learner behavior or identifiable participant records shall receive applicable ethics and privacy review, purpose-specific information, and voluntary consent where required. Ordinary assessment is not automatically human-subject research. Research access and commercial participation shall not be improperly coupled. No internal body shall claim IRB equivalence without authority.
## Article C08 — Independence
The BOSS kernel shall be portable and vendor-agnostic. Proprietary adapters are allowed where authorized, justified and disclosed; core instructional outcomes must not depend on unnecessary paid lock-in.
## Article C09 — Academy Credentials
Qualifications require defined, verifiable competence assessed against published criteria, potentially using safe fixtures. Credential restrictions ordinarily permit notice and appeal. A credential does not itself establish engineering licensure or production deployment rights.
## Article C10 — Data Protection and Security
Every subordinate system shall have a data inventory, defined purpose, minimization rules, role-based access, proportionate security, verified retention/deletion schedule, breach detection/escalation and processes for applicable individual rights. Pseudonymization is not anonymization. Source archives and audit evidence are protected according to rights, lawful retention and preservation holds. External processors require appropriate safeguards. Texas law supplies drafting inspiration, not blanket applicability or legal certification.
### Section C10.06 — Unified Incident Response
A designated **Human Incident Lead**, identified before production deployment, receives escalations from Academy, Design Exchange, DraftDeck, DraftGraph, Windmill and research infrastructure. Each event shall receive an incident ID, reporter, observed facts, scope, severity, affected data/services, containment decision, available evidence, notification review and closure authority. A separate technical lead, data custodian and qualified privacy/legal reviewer shall participate when risk requires; one person may hold multiple low-risk roles subject to conflicts and independent-review requirements. Automated systems may detect, alert, and perform preauthorized bounded containment only. External notification duties are determined by qualified humans under applicable law. No system shall automatically declare a legal breach or reinstate its own suspended production rights.
## Article C11 — Risk and Data Protection Assessment
An authorized human shall document context-specific risk before deployment, reassessing material scope changes. Candidate tiers: T1 local low-consequence; T2 bounded connected/sensitive-source operations; T3 material external-state or participant-impact operations; T4 restricted high-consequence or regulated operations. Determine tier from impact, reversibility, sensitivity, privilege and affected persons—not labels alone. Conduct a documented data protection assessment where warranted by processing and applicable law; higher-risk work requires specialist or independent review as indicated.
## Article X — Kernel Supremacy and Independence
Subordinate systems inherit mandatory IPOS mapping, evidence discipline, privacy, security, risk assessment, human-authorized scopes and verifiable release controls. Implementations may differ without lowering protection. Only authorized human operators may approve purpose, risk, allowed spend, automation bounds and production release within higher applicable constraints. Tamper-evident records are preferred over promises of permanent immutability. Neither a tool nor an LLM may certify its own compliance by assertion.
## Governance Structure — Review Without Simulated Representation
Human Review Chamber examines people, learning, participant rights and accountable purpose. Systems Review Chamber examines evidence, interfaces, privacy and risk controls. The chambers perform independent advisory review; designated human authorities ratify policy and authorize release. Learners may submit proposals, comments and appeals without assuming political representation.
```mermaid
flowchart TD
  LAW["Applicable law and obligations"] --> K["BOSS Constitutional Kernel"]
  K --> HR["Human Review Chamber"]
  K --> SR["Systems Review Chamber"]
  HR --> AR["Independent reconciled review"]
  SR --> AR
  AR --> AUTH{"Authorized human decision"}
  AUTH -->|Approved within scope| REL["Release or amended policy"]
  AUTH -->|Hold| REM["Remediation and evidence"]
  K --> IR["Unified Incident Response / C10.06"]
  IR --> STOP["Bounded containment and qualified review"]
```
## Constitutional Gap Register
| ID | Gap | Closure evidence |
|---|---|---|
| CON-01 | Named amendment ratifier and chamber membership not established | Adopted role register and conflict rules |
| CON-02 | Incident lead and backups not appointed | Human role assignment and drill |
| CON-03 | Tier thresholds and statutory jurisdiction unresolved | Approved risk matrix and legal applicability analysis |
| CON-04 | Rights, retention and secure-disposal details not operational | Documented schedules, audited rights workflow |
| CON-05 | Specialist competence criteria and referrals untested | Referral template and completed pilot |
| CON-06 | Constitutional control tests not yet executed | Independent cross-document and technical verification |
NO IMPLEMENTATION OR LEGAL COMPLIANCE CLAIMED.