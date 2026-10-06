# DraftDeck Doctrine Index

**Status:** Candidate Canonical Index  
**Purpose:** Provide a one-page map of DraftDeck's doctrine stack so a fresh human or agent can understand the order, authority, and relationship of the governing files.

---

## 1. Doctrine Stack

DraftDeck doctrine is intentionally layered.

```text
PRODUCTION CONTRACT
        ↓
COMPOSITION STANDARD
        ↓
LOGISTICS FRAMEWORK
        ↓
PRIME PROCESS
        ↓
PRIME PROCESS ORCHESTRATION
        ↓
PRIME HANDOFF & CONTEXT ROUTING
        ↓
RELEASE QA
```

Each layer answers a different class of question.

---

## 2. Layer Map

| Layer | File | Governing Question | Primary Role |
|---|---|---|---|
| Contract | `production-contract.md` | What is authoritative, what is generated, and what may be edited? | Defines source → compiler/renderer → generated output ownership. |
| Composition | `composition-standard.md` | What visual grammar governs DraftDeck output? | Defines the pure-white drafting standard, typography, line hierarchy, accent discipline, and prohibited visual treatments. |
| Ontology | `logistics-framework.md` | What conceptual model governs the system? | Establishes shipping-and-receiving logistics as canonical and defines the control spine: LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY. |
| Process | `prime-process.md` | How does work move through the system? | Defines PRIME: Package → Route → Inspect → Move → Establish Delivery. |
| Orchestration | `prime-process-orchestration.md` | How does PRIME become an executable multi-step work system? | Defines bounded work packages, routing, inspection, orchestration, delivery verification, feedback, and reusable learning. |
| Routing / Handoff | `prime-handoff-context-routing.md` | How should context and side-work move between handlers or sessions? | Defines task severance, Prime Handoff Packages, return handoffs, transit artifacts, evidence-producing detours, and context routing. |
| Release | `release-qa.md` | What must be true before an artifact is considered releasable? | Defines release gates and verification expectations. |

---

## 3. Reading Order

A new contributor, agent, or adapter should read doctrine in this order:

1. `production-contract.md`
2. `composition-standard.md`
3. `logistics-framework.md`
4. `prime-process.md`
5. `prime-process-orchestration.md`
6. `prime-handoff-context-routing.md`
7. `release-qa.md`

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

### Rule 3 — PRIME before execution

Work should be packaged, routed, inspected, moved, and have delivery established.

Execution alone is not completion.

### Rule 4 — Orchestration does not replace authority

An orchestrator may classify, schedule, route, hold, compare, and report.

Human release authority remains human where the workflow requires human authorization.

### Rule 5 — Context is cargo

Context should be routed, not accumulated.

Out-of-scope work should become a new package rather than contaminating the parent workstream.

### Rule 6 — Release requires evidence

A build, test pass, commit, or deployment may be necessary but is not automatically sufficient to establish delivery or release.

---

## 5. Canonical Statements

The following statements summarize the active doctrine stack:

> **GitHub is the canonical source of truth.**

> **SOURCE → COMPILER / RENDERER → GENERATED OUTPUT**

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

> **PRIME = Package → Route → Inspect → Move → Establish Delivery.**

> **The block is the unit of operational commitment; the package is the unit of accountability.**

> **Speed of execution increases the value of restraint before execution.**

> **Movement never substitutes for inspection.**

> **TEST PASS ≠ DELIVERY ESTABLISHED.**

> **The orchestrator is a control surface, not final authority.**

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
REVIEW
        ↓
MERGE TO MAIN
```

A useful idea is not automatically doctrine.

A repeated successful behavior becomes a doctrine candidate only after inspection.

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

DraftDeck may study external systems such as:

- Amazon logistics;
- ECC;
- AI coding harnesses;
- design tools;
- workflow engines;
- development methodologies.

These sources may influence implementation patterns.

They do not become DraftDeck's ontology by default.

> **Study the mechanics. Preserve our doctrine.**

---

## 10. Repository Invariant

The permanent ontology guard protects the canonical boundary.

It exists so the Logistics Framework is enforced operationally rather than only documented.

The guard should fail when prohibited predecessor ontology re-enters protected tracked content.

Doctrine growth must therefore remain compatible with the same invariant that protects production source and generated output.

---

## 11. Fresh-Agent Boot Sequence

A fresh agent entering DraftDeck should use this order:

```text
1. Read this index.
2. Read production-contract.md.
3. Read logistics-framework.md.
4. Read prime-process.md.
5. Read the most relevant downstream doctrine for the task.
6. Inspect the active repository state.
7. Package the requested work.
8. Route it.
9. Inspect before movement.
10. Establish delivery before declaring completion.
```

For visual-production work, also read `composition-standard.md` before implementation.

For orchestration work, read `prime-process-orchestration.md`.

For cross-session delegation or context transfer, read `prime-handoff-context-routing.md`.

For release decisions, read `release-qa.md`.

---

## 12. Canonical Summary

DraftDeck doctrine is not a pile of independent Markdown files.

It is a layered operating system:

```text
CONTRACT
defines authority

COMPOSITION
defines visual grammar

ONTOLOGY
defines what the system is

PROCESS
defines how work moves

ORCHESTRATION
defines how work scales

ROUTING
defines how context and sub-work move

RELEASE
defines when delivery is established
```

> **The doctrine stack should be readable as one system, not seven unrelated documents.**
