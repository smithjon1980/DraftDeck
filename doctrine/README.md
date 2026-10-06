# BOSS Doctrine Index

**Status:** Canonical Index
**Purpose:** Provide a one-page map of the BOSS doctrine stack so a fresh human or agent can understand the order, authority, ownership, and relationship of the governing files.

---

## 1. Doctrine Stack

BOSS doctrine is intentionally layered.

```text
NAMING ARCHITECTURE
        ↓
BIOSCILLATE LOGISTICS FRAMEWORK
        ↓
PARCELS LAYER ARCHITECTURE
        ↓
BOUNDED AUTONOMY & EXECUTION ENVELOPES
        ↓
BIOSCILLATE PRIME PROTOCOL
        ↓
PRIME ALIGNMENT, DECOMPOSITION & FEEDBACK
        ↓
ALIGNED INSTRUCTION & LEARNING ENVELOPES
        ↓
PRIME SHIPPING LABEL & CLASSIFICATION
        ↓
PRIME PROTOCOL ORCHESTRATION
        ↓
PRIME HANDOFF & CONTEXT ROUTING
        ↓
PRIME CONTROL PLANE REFERENCE ARCHITECTURE
        ↓
EVIDENCE & VERIFICATION ARCHITECTURE
        ↓
DRAFTDECK PRODUCTION CONTRACT
        ↓
DRAFTDECK COMPOSITION STANDARD
        ↓
RELEASE QA
```

Each layer answers a different class of question.

---

## 2. Layer Map

| Layer | File | Governing Question | Primary Role |
|---|---|---|---|
| Naming | `naming-architecture.md` | What is the system, and what do framework, architecture, protocol, specialization, and product mean? | Establishes BOSS ownership, the Bioscillate naming hierarchy, PRIME typography, and DraftDeck's role as a productized production specialization. |
| Ontology | `logistics-framework.md` | What conceptual model governs the system? | Establishes shipping-and-receiving logistics as canonical and defines the control spine: LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY. |
| Structure (Canonical) | `parcels-layer-architecture.md` | Where does a concern, rule, or failure live in the system? | Defines the seven PARCELS layers (Platform, Attachment, Routing, Carriage, Exchange, Language, Service), canonical ownership by dominant failure mode, governance as a vertical plane, and the three-axis model: CONSTITUTION × PARCELS × PRIME. |
| Delegation Limits | `bounded-autonomy-execution-envelope.md` | What limits govern delegation before unattended execution? | Defines bounded autonomy, the Execution Envelope, envelope-scoped permission, roles vs. handlers vs. providers, the parallelism gate, the consolidation boundary, and MERGE ≠ RELEASE. |
| Protocol | `prime-process.md` | How does bounded work move through the system? | Defines the Bioscillate PRIME Protocol: Package → Route → Inspect → Move → Establish Delivery. The existing filename is retained pending any dedicated path migration. |
| Alignment / Decomposition / Feedback | `prime-alignment-decomposition-feedback.md` | What must be aligned, decomposed, and instrumented before and during execution? | Defines alignment before packaging, destination vs journey artifacts, dependency graphs, vertical slices, route instrumentation, feedback quality, review proportionality, and stale-context handling. |
| Aligned Instruction / Learning Envelopes | `aligned-instruction-learning-envelope.md` | What limits govern instruction before teaching begins? | Specializes alignment doctrine into the instructional domain: defines the Learning Envelope, mission vs. curriculum vs. lesson, declared vs. observed learner state, the learning loop, Day Zero's constitutional responsibility, and CONTENT DELIVERED ≠ LEARNING ESTABLISHED. |
| Shipping Label / Classification | `prime-shipping-label-classification.md` | What metadata must accompany a package before routing, and how may classifiers influence execution, placement, escalation, and verification policy without acquiring authority? | Defines the PRIME Shipping Label, declared/derived/classified fields, scan validation, declared-vs-observed comparison, execution-envelope requirements, capability and locality requirements, Verification Profiles, review independence, escalation policy, route selection, label versioning, and separation from the Verification Tag. |
| Orchestration | `prime-process-orchestration.md` | How does PRIME become an executable multi-step work system? | Defines bounded work packages, routing, inspection, orchestration, delivery verification, feedback, and reusable learning. |
| Routing / Handoff | `prime-handoff-context-routing.md` | How should context and side-work move between handlers or sessions? | Defines task severance, Prime Handoff Packages, return handoffs, transit artifacts, evidence-producing detours, and context routing. |
| Control Plane Reference Architecture | `prime-control-plane-reference-architecture.md` | How should PRIME doctrine map into an operator-facing web application without surrendering domain authority to implementation tools? | Defines server-authoritative state, domain-first interfaces, replaceable adapters, typed server-rendered presentation, lightweight hypermedia interaction, PocketBase as a candidate adapter, and doctrine-to-code traceability. |
| Evidence & Verification | `evidence-verification-architecture.md` | How does BOSS know whether a state, claim, evaluation, or release condition is warranted? | Defines structural evidence vs. interpretation, observability/evaluation/verification/release separation, evaluator competence, denominator integrity, dual execution/verification routing, Verification Profiles, consequence-sensitive inspection, Change Radius, explicit uncertainty, and candidate EVIDENCE axis language. |
| DraftDeck Product Contract | `production-contract.md` | What is authoritative, what is generated, and what may be edited in the DraftDeck product? | Defines source → compiler/renderer → generated output ownership for DraftDeck. |
| DraftDeck Composition | `composition-standard.md` | What visual grammar governs DraftDeck output? | Defines the pure-white drafting standard, typography, line hierarchy, accent discipline, and prohibited visual treatments. |
| Release | `release-qa.md` | What must be true before an artifact is considered releasable? | Defines release gates and verification expectations. |

---

## 3. Reading Order

A new contributor, agent, or adapter should read doctrine in this order:

1. `naming-architecture.md`
2. `logistics-framework.md`
3. `parcels-layer-architecture.md`
4. `bounded-autonomy-execution-envelope.md`
5. `prime-process.md`
6. `prime-alignment-decomposition-feedback.md`
7. `aligned-instruction-learning-envelope.md`
8. `prime-shipping-label-classification.md`
9. `prime-process-orchestration.md`
10. `prime-handoff-context-routing.md`
11. `prime-control-plane-reference-architecture.md`
12. `evidence-verification-architecture.md`
13. `production-contract.md`
14. `composition-standard.md`
15. `release-qa.md`

The order matters.

A downstream layer may specialize an upstream rule, but it must not silently redefine it.

---

## 4. Authority Rules

### Rule 1 — Contract before implementation

Generated output is subordinate to canonical source.

If a generated artifact conflicts with the production contract, the generated artifact is wrong.

### Rule 2 — Ontology before metaphor

The Logistics Framework is canonical.

Predecessor aviation-era ontology is prohibited in current production source, generated output, user-facing documentation, and active training doctrine except where a meta-doctrine file explicitly names the prohibition.

### Rule 3 — Structure before argument

Locate a concern before debating it.

PARCELS assigns every concern a canonical home by dominant failure mode; detection location does not determine layer ownership.

### Rule 4 — Confinement before delegation

Autonomy requires confinement before delegation.

The degree of unattended autonomy granted to a handler must not exceed the containment, observability, and recovery guarantees of its execution environment.

### Rule 5 — PRIME before execution

Work should be packaged, routed, inspected, moved, and have delivery established.

Execution alone is not completion.

### Rule 6 — Alignment before packaging

Alignment precedes packaging.

Instrument the route before sending the package; a package that moves without acceptance signals is cargo without a manifest.

### Rule 7 — Labels and classifiers do not replace authority

A label declares. A classifier interprets. A routing policy assigns.

Classification informs routing; classification does not grant release authority.

### Rule 8 — Orchestration does not replace authority

An orchestrator may classify, schedule, route, hold, compare, and report.

Human release authority remains human where the workflow requires human authorization.

### Rule 9 — Context is cargo

Context should be routed, not accumulated.

Out-of-scope work should become a new package rather than contaminating the parent workstream.

Stale context is active contamination: in an agentic system, obsolete documentation is retrieved and acted upon as if it were current authority.

### Rule 10 — Implementation serves doctrine

The domain defines the interfaces. Frameworks and services implement them.

Implementation candidates may change without changing the doctrine they implement.

### Rule 11 — Release requires evidence

A build, test pass, commit, merge, or deployment may be necessary but is not automatically sufficient to establish delivery or release.

---

## 5. Canonical Statements

The following statements summarize the active BOSS doctrine stack:

> **BOSS — Bioscillate Operating System by Seven — is the governing system.**

> **BOSS owns the doctrine. DraftDeck implements a production specialization of that doctrine.**

> **The Bioscillate Logistics Framework is the governing conceptual model.**

> **PARCELS is the seven-layer structural architecture.**

> **The Bioscillate PRIME Protocol governs Package → Route → Inspect → Move → Establish Delivery.**

> **Where deterministic evidence exists, generative interpretation must remain subordinate to it.**

> **TRACE ≠ TRUTH.**

> **EVAL PASS ≠ RELEASE.**

> **Execution routing and verification routing are independent decisions.**

> **BUILD_CAPABILITY ≠ REVIEW_CAPABILITY ≠ RELEASE_AUTHORITY.**

> **Automation that increases production throughput without increasing verification throughput creates governance debt.**

> **GitHub is the canonical source of truth.**

> **SOURCE → COMPILER / RENDERER → GENERATED OUTPUT**

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

> **CONSTITUTION = why/limits × PARCELS = where × PRIME = how.**

> **Layer ownership ≠ layer exclusivity.**

> **Detection location does not determine layer ownership.**

> **Governance is a vertical plane across all seven layers; there is no L8.**

> **Autonomy requires confinement before delegation.**

> **Permission should be designed into the execution envelope rather than negotiated repeatedly during execution.**

> **Every unattended package moves inside an execution envelope.**

> **Execution environments should expose the minimum substrate required for the package.**

> **Role must not be coupled to provider identity.**

> **Parallelism should emerge from dependency independence.**

> **Do not create more lanes than the manifest can govern.**

> **MERGE ≠ RELEASE. CONSOLIDATED ≠ RELEASED.**

> **PRIME = Package → Route → Inspect → Move → Establish Delivery.**

> **The block is the unit of operational commitment; the package is the unit of accountability.**

> **Speed of execution increases the value of restraint before execution.**

> **Alignment precedes packaging.**

> **Instruction begins with alignment, not content.**

> **A learner's destination, current state, constraints, and available attention govern the route.**

> **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**

> **Learning continuity should depend on durable learner state, not conversational memory.**

> **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

> **Day Zero establishes the learner's initial routing state before curriculum movement begins.**

> **Instrument the route before sending the package.**

> **Stale context is active contamination.**

> **Movement never substitutes for inspection.**

> **TEST PASS ≠ DELIVERY ESTABLISHED.**

> **The orchestrator is a control surface, not final authority.**

> **A reliable courier network requires both observable routes and trustworthy manifests.**

> **A label declares. A classifier interprets. A routing policy assigns. A handler executes. Verification establishes delivery. Human authority releases where required.**

> **ENCODED ≠ PROTECTED.**

> **PACKAGE = what is being shipped. LABEL = how it should be interpreted and handled. VERIFICATION TAG = what actually happened to it.**

> **Classification informs routing. Classification does not grant release authority.**

> **Placement follows requirements.**

> **PLACEMENT ≠ CAPABILITY.**

> **Execution routing and verification routing are independent decisions.**

> **Capability to produce does not establish capability to verify.**

> **Handler limitations can be managed by reducing package scope without reducing destination scope.**

> **The UI displays governed state. It does not become the source of governed state.**

> **Keep the system small enough to understand, but modular enough to govern.**

> **The domain defines the interfaces. Frameworks and services implement them.**

> **Context should be routed, not accumulated.**

> **COMPACT preserves one package. HANDOFF creates another.**

> **Carry the operational delta; reference the authority.**

> **Skills should be extracted from repeated successful behavior, not invented merely to fill a catalog.**

---

## 6. How New Doctrine Enters the Stack

New doctrine should not be added casually.

The preferred path is:

```text
OBSERVED REPEATED BEHAVIOR
        ↓
PATTERN IDENTIFIED
        ↓
PATTERN INSPECTED
        ↓
CANDIDATE DOCTRINE
        ↓
BRANCH
        ↓
ONTOLOGY GUARD
        ↓
REVIEW (INCLUDING INDEX UPDATE)
        ↓
MERGE TO MAIN
```

A useful idea is not automatically doctrine.

A repeated successful behavior becomes a doctrine candidate only after inspection.

### Doctrine Index Invariant

> **Every PR that adds, renames, supersedes, or materially changes a canonical doctrine file must update `doctrine/README.md` in the same change set. A doctrine change is incomplete until the index reflects the new canonical state.**

The index is a maintained registry of the canon, not a passive table of contents.

---

## 7. Doctrine vs. Implementation

Doctrine files define stable operating rules.

Implementation may change.

For example:

```text
DOCTRINE
"Context should be routed, not accumulated."

IMPLEMENTATION A
Markdown handoff file

IMPLEMENTATION B
Structured JSON handoff object

IMPLEMENTATION C
Native agent-to-agent transport
```

The implementation may evolve while the doctrine remains stable.

This distinction prevents tool or vendor lock-in.

---

## 8. Doctrine vs. Training Material

Training material may explain doctrine using examples, exercises, analogies, diagrams, or case studies.

Training material must not redefine doctrine.

If a lesson conflicts with doctrine:

> **Doctrine wins.**

If a training example introduces a new rule that deserves permanence, that rule should be promoted into doctrine through the normal guarded review path.

---

## 9. Doctrine vs. External References

BOSS may study external systems such as:

- Amazon logistics;
- ECC;
- AI coding harnesses;
- design tools;
- workflow engines;
- development methodologies.

These sources may influence implementation patterns.

They do not become BOSS ontology by default.

> **Study the mechanics. Preserve our doctrine.**

---

## 10. Repository Invariant

The permanent ontology guard protects the canonical boundary.

It exists so the Logistics Framework is enforced operationally rather than only documented.

The guard should fail when prohibited predecessor ontology re-enters protected tracked content.

Doctrine growth must therefore remain compatible with the same invariant that protects production source and generated output.

---

## 11. Fresh-Agent Boot Sequence

A fresh agent entering BOSS should use this order:

```text
1. Read this index.
2. Read naming-architecture.md.
3. Read logistics-framework.md.
4. Read parcels-layer-architecture.md.
5. Read bounded-autonomy-execution-envelope.md.
6. Read prime-process.md as the Bioscillate PRIME Protocol.
7. Read the most relevant downstream doctrine for the task.
8. For DraftDeck work, read production-contract.md and composition-standard.md.
9. Inspect the active repository state.
10. Package the requested work.
11. Route it.
12. Inspect before movement.
13. Establish delivery before declaring completion.
```

For visual-production work, also read `composition-standard.md` before implementation.

For locating a defect, doctrine, or design decision within the system, read `parcels-layer-architecture.md`.

For unattended execution, sandboxing, parallelism, or delegation limits, read `bounded-autonomy-execution-envelope.md`.

For planning, decomposition, or feedback design, read `prime-alignment-decomposition-feedback.md`.

For curriculum design, instructional systems, learner routing, or Day Zero work, read `aligned-instruction-learning-envelope.md`.

For package labeling, scan classification, execution/placement requirements, capability routing, escalation policy, or verification-profile selection, read `prime-shipping-label-classification.md`.

For orchestration work, read `prime-process-orchestration.md`.

For cross-session delegation or context transfer, read `prime-handoff-context-routing.md`.

For operator-console, web-control-plane, persistence-adapter, or HTMX/templ implementation work, read `prime-control-plane-reference-architecture.md`.

For evidence design, evaluation, verifier competence, Change Radius, consequence-sensitive inspection, or Verification Profiles, read `evidence-verification-architecture.md`.

For release decisions, read `release-qa.md`.

---

## 12. Canonical Summary

BOSS doctrine is not a pile of independent Markdown files.

It is a layered operating system:

```text
NAMING ARCHITECTURE
defines system identity and the naming hierarchy

ONTOLOGY
defines the governing conceptual model

PARCELS
defines where concerns live

BOUNDED AUTONOMY
defines what limits govern delegation

BIOSCILLATE PRIME PROTOCOL
defines how bounded work moves

ALIGNMENT / DECOMPOSITION / FEEDBACK
defines what must be true before and during movement

ALIGNED INSTRUCTION
defines what limits govern teaching

SHIPPING LABEL / CLASSIFICATION
defines what metadata accompanies cargo and how pre-routing interpretation is governed

ORCHESTRATION
defines how work scales

ROUTING
defines how context and sub-work move

CONTROL PLANE REFERENCE ARCHITECTURE
defines how doctrine maps into replaceable implementation boundaries

EVIDENCE & VERIFICATION ARCHITECTURE
defines how BOSS establishes warranted state before release

DRAFTDECK PRODUCT CONTRACT
defines source and generated-output authority for the DraftDeck product

DRAFTDECK COMPOSITION
defines the DraftDeck visual grammar

RELEASE
defines when delivery is established
```

> **The doctrine stack should be readable as one system, not fifteen unrelated documents.**
