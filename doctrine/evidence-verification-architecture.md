# Evidence & Verification Architecture

**Status:** Candidate Canonical Doctrine  
**Owner:** BOSS — Bioscillate Operating System by Seven  
**Placement:** After PRIME Control Plane Reference Architecture and before Release QA.  
**Purpose:** Define the epistemic machinery by which BOSS distinguishes structural evidence, interpretation, observability, evaluation, verification, and release.

---

## Doctrine Coordinates

> **Primary PARCELS:** Governance vertical plane across all seven layers  
> **Secondary anchors:** L6 Language, L4 Carriage, L1 Platform  
> **PRIME influence:** Inspect → Establish Delivery, plus Inspect-before-Move for Change Radius  
> **Structural note:** This is not an L8. Verification crosses all seven PARCELS layers under the existing governance plane.

---

## 1. Verification Becomes the Scarce Control Function

As generative systems reduce the cost and time required to produce code, documents, designs, analyses, lessons, and other artifacts, the scarce resource moves downstream.

The governing problem is no longer only:

> Can the system produce enough work?

It becomes:

> Can the system establish enough evidence to know what work deserves to survive?

> **As generative throughput increases, verification capacity must increase with it.**

> **Automation that increases production throughput without increasing verification throughput creates governance debt.**

This doctrine therefore treats verification capacity as a first-class system concern rather than an afterthought attached to release.

---

## 2. Structural Evidence vs. Interpretive Output

BOSS distinguishes evidence established by deterministic or externally grounded mechanisms from interpretation produced by a human or generative handler.

### Structural Evidence

Examples include:

```text
SOURCE EXISTS
FILE EXISTS
RESOLVED RELATIONSHIP
DATABASE ROW EXISTS
CHECKSUM MATCHES
POLICY IS ENABLED
ROUTE WAS PARSED
TEST RETURNED VALUE
REFERENCE BALANCE MATCHES
ARTIFACT HASH
```

### Interpretive Output

Examples include:

```text
"This module coordinates authentication."
"This artifact appears risky."
"This file is best classified as a utility."
"This explanation is specific enough."
```

The governing relationship is:

> **Where deterministic evidence exists, generative interpretation must remain subordinate to it.**

> **Interpretation may explain established structure; it may not silently replace it.**

Interpretive output should declare, preserve, or reference the evidence it interprets whenever the evidence is material to the claim.

---

## 3. Observability ≠ Evaluation ≠ Verification ≠ Release

These states are distinct.

### Observability

Observability answers:

> What happened?

Typical evidence:

```text
INPUT
OUTPUT
HANDLER
TOOL CALLS
LATENCY
TOKEN / COMPUTE USE
COST
STATE TRANSITIONS
ERRORS
```

A trace records activity. It does not establish correctness.

> **TRACE ≠ TRUTH.**

### Evaluation

Evaluation answers:

> How did a result perform against a defined measure?

Examples:

- exact membership checks;
- known-label comparisons;
- regression comparisons;
- prompt or handler experiments;
- bounded quality judgments.

An evaluation may be deterministic or judgment-based depending on the property being measured.

### Verification

Verification answers:

> Were the required conditions established with adequate evidence?

Verification may compose multiple evidence sources.

### Release

Release answers:

> May the result be accepted, relied upon, or exposed under the governing authority model?

> **EVAL PASS ≠ RELEASE.**

This doctrine supplies machinery to Release QA. It does not replace Release QA.

---

## 4. Strongest-Available-Evidence Rule

Use the strongest evidence mechanism that the question permits.

A default hierarchy is:

```text
1. DIRECT OBSERVATION
2. DETERMINISTIC COMPARISON
3. DERIVED RULE
4. HUMAN JUDGMENT
5. MODEL-ASSISTED JUDGMENT
```

The hierarchy is not a claim that every higher line is universally superior in every domain. It is a constraint against replacing an exact check with a weaker interpretive mechanism merely because the weaker mechanism is convenient.

> **Use the strongest available evidence mechanism. Do not substitute probabilistic judgment for deterministic comparison when deterministic comparison is available.**

If a property has an exact answer, prefer exact comparison.

If a property is inherently judgment-based, state that fact rather than presenting the result as harder evidence than it is.

---

## 5. Evaluator Competence

A verifier must establish that it can detect the class of failure it claims to guard against.

Use positive and negative controls where practical:

```text
POSITIVE CONTROL
known-valid case
        ↓
SHOULD PASS

NEGATIVE CONTROL
known-defective case
        ↓
SHOULD FAIL
```

> **A verifier must demonstrate that it can detect the failure it claims to guard against.**

> **A control that has never demonstrated failure detection has not established its own competence.**

A permanently green check is not evidence of quality.

This principle applies to ontology guards, parsers, security policies, regression tests, visual QA, curriculum assessments, classifiers, and AI evaluators.

---

## 6. Metric Integrity & the Denominator Firewall

A score is only as trustworthy as its eligible population, measurement method, and independence.

Before relying on a metric, ask:

```text
Was the eligible population complete?
Were missing observations handled explicitly?
Could the evaluator see the answer?
Were excluded cases counted in the denominator?
Could unsupported cases silently disappear?
Can the metric detect a known failure?
```

> **A metric is only meaningful relative to the completeness and independence of its denominator.**

A metric can report apparent perfection while failing to observe an entire class of events. A held-out evaluation can report apparent accuracy while leaking the reference answer into the input.

Measurement integrity is therefore part of verification, not merely analytics.

---

## 7. Dual-Route Model

Execution routing and verification routing are different decisions.

```text
             EXECUTION ROUTE
PACKAGE ─────────────────────→ HANDLER

             VERIFICATION ROUTE
RESULT  ─────────────────────→ EVIDENCE / REVIEW / AUTHORITY
```

> **Execution routing and verification routing are independent decisions.**

The handler best suited to produce an artifact may not be the handler best suited to inspect it.

> **Capability to produce does not establish capability to verify.**

```text
BUILD_CAPABILITY
        ≠
REVIEW_CAPABILITY
        ≠
RELEASE_AUTHORITY
```

This sits beside existing BOSS rules:

```text
ROLE ≠ AUTHORITY
MOVEMENT ≠ INSPECTION
```

---

## 8. Verification Profile

A package may require more than a boolean review flag.

The structured form is a **Verification Profile**:

```text
VERIFICATION_PROFILE

DETERMINISTIC_CHECKS
REFERENCE_COMPARATOR
INDEPENDENT_REVIEW
NEGATIVE_CONTROLS
HUMAN_ACCEPTANCE
REQUIRED_EVIDENCE
RELEASE_THRESHOLD
```

The profile is implementation-neutral.

It may be satisfied through deterministic tools, local or hosted handlers, independent reviewers, reference systems, human adjudication, or a combination.

No single verifier must carry the entire evidentiary burden.

---

## 9. Consequence-Sensitive Verification

Verification burden is determined by consequence, not by how impressive, large, or expensive the implementation appears.

> **Verification intensity should scale with consequence, not implementation size.**

> **Package consequence, not handler identity, determines verification burden.**

The same generation mechanism may legitimately support very different inspection profiles for:

- financial state;
- public informational views;
- convenience utilities;
- low-consequence experiments.

The consequence of an incorrect result, the reversibility of the action, and the strength of available comparators determine inspection intensity.

> **The consequence of the package constrains how much unverified output may accumulate before inspection.**

This extends, but does not modify, Bounded Autonomy doctrine.

---

## 10. Package Scope as a Control Surface

Large missions do not require large packages.

> **Handler limitations can be managed by reducing package scope without reducing destination scope.**

The destination may remain broad while individual packages remain bounded enough to route, inspect, retry, and verify.

This connects workload placement to existing decomposition doctrine without redefining that doctrine.

---

## 11. Change Radius

Before modifying a canonical or high-dependency object, inspect what depends on it and what it depends on.

Canonical field shape:

```text
CHANGE_RADIUS

DIRECT_DEPENDENTS
TRANSITIVE_DEPENDENTS
DEPENDENCIES
AFFECTED_CONTRACTS
AFFECTED_ARTIFACTS
REQUIRED_RECHECKS
```

> **Before changing a canonical object, inspect its dependency radius.**

Detection location does not determine ownership, but dependency visibility determines what must be rechecked.

Change Radius belongs primarily to PRIME Inspect-before-Move and supports Establish Delivery by identifying affected evidence obligations.

---

## 12. Review Findings Are Claims

A review system, reviewer, model, scanner, or agent may identify a possible defect.

That finding is evidence input, not executable authority.

```text
REVIEW FINDING
      ↓
VERIFY AGAINST SOURCE
      ↓
ACCEPT / REJECT / MODIFY
      ↓
EVIDENCE
      ↓
RELEASE DECISION
```

> **Review findings are claims requiring verification, not executable authority.**

This rule preserves independence without surrendering judgment to the reviewer.

---

## 13. Explicit Uncertainty & Silent-Failure Prohibition

When correctness cannot be established, expose the uncertainty as governed state.

Preferred states include:

```text
UNKNOWN
UNRESOLVED
STALE
HELD
BLOCKED
NOT ESTABLISHED
```

> **When correctness cannot be established, expose uncertainty as state rather than fabricate completeness.**

A partial parser, stalled run, missing operand, unresolved route, or unsupported conclusion must not silently render as complete merely because the presentation layer can display something plausible.

Failure visibility is part of correctness.

---

## 14. Cargo Cannot Expand Authority

Untrusted source material may contain arbitrary content, including instructions that attempt to influence a handler.

That cargo may affect interpretation only inside already-established scope.

> **Cargo may influence interpretation within its authorized scope; cargo may not expand that scope.**

Authorization must come from governed identity, policy, credentials, envelope, or human authority — never from the content being processed.

This rule applies to source code, documents, webpages, email, retrieved files, datasets, and other external cargo.

---

## 15. Shared Domain Logic

Agent tools, user interfaces, APIs, and automated checks should consume the same authoritative domain capabilities where practical.

```text
DOMAIN LOGIC
     ↓
SHARED INTERFACE
     ├─ UI
     ├─ API
     ├─ AGENT TOOL
     └─ VERIFIER
```

Avoid parallel implementations of the same governed rule.

A handler should consume authoritative domain capability rather than silently recreating domain truth inside its own prompt or tool chain.

---

## 16. Documentation & Invisible Failure

The existing package contract is validated by the recurring pattern:

```text
WHAT IT MUST DO
WHAT IT MUST NOT DO
HOW WE KNOW IT WORKED
```

Documentation should be densest where failure is difficult to see.

> **Documentation effort should be proportional to invisibility of failure, not merely complexity of implementation.**

A visible interface defect may be discovered immediately. A silent evidence, authorization, dependency, or denominator defect may survive while producing polished output.

The specification should therefore spend precision where wrongness is least observable.

---

## 17. Candidate Fourth Question

The active BOSS structural model remains:

```text
CONSTITUTION = why / limits
PARCELS      = where
PRIME        = how
```

This doctrine records, but does not yet promote, a candidate fourth question:

```text
EVIDENCE = how do we know?
```

Candidate four-question structure:

```text
CONSTITUTION
What must remain true?

PARCELS
Where does responsibility live?

PRIME
How does work move?

EVIDENCE
How do we know the state or claim is warranted?
```

Promoting EVIDENCE to a peer axis would materially amend PARCELS doctrine and therefore requires a separate guarded doctrine change.

---

## 18. PARCELS Mapping

Verification is governed vertically across all seven layers:

| Layer | Verification concern |
|---|---|
| L1 Platform | Observability substrate, runtime evidence, credential boundaries, independent execution surfaces |
| L2 Attachment | Evidence attached to the correct package, run, handler, source, version, and authority context |
| L3 Routing | Execution route vs. verification route, escalation, consequence-sensitive reviewer selection |
| L4 Carriage | Stale runs, late writes, retries, race conditions, idempotency, cancellation, state succession |
| L5 Exchange | Durable trace/evidence identity across sessions and handlers |
| L6 Language | Unknown over fabrication; representation of evidence, scores, uncertainty, and provenance |
| L7 Service | Whether the required outcome was actually established |

This cross-layer reach does not create an eighth layer. It is a governance-plane concern.

---

## 19. PRIME Mapping

Evidence and verification interact with PRIME at multiple points:

- **Package:** declare evidence and verification requirements.
- **Route:** select execution and verification routes independently.
- **Inspect:** validate identity, constraints, evidence quality, Change Radius, and evaluator competence.
- **Move:** preserve observability and prevent stale or unauthorized state mutation.
- **Establish Delivery:** compose required evidence and determine whether acceptance criteria are established.

The strongest influence is Inspect → Establish Delivery, with Change Radius operating before high-impact Move.

---

## 20. Studied External Specimens

This doctrine was sharpened by multiple external specimens:

- an isolated unattended-execution workflow demonstrating confinement, independent review, and merge-versus-release separation;
- an aligned teaching workflow demonstrating mission-first instruction and observable success conditions;
- a codebase-mapping and evaluation workflow demonstrating deterministic structure, tracing, evaluator controls, denominator failures, review verification, and scoped agent tools;
- a local-compute application workflow demonstrating execution/verification route separation, consequence-sensitive review, composed evidence, and workload decomposition.

Per *Doctrine vs. External References*: the mechanics were studied; the doctrine above is BOSS doctrine. No external tool, vendor, model, framework, or service becomes canonical through inclusion here.

> **Study the mechanics. Preserve our doctrine.**

---

## 21. Non-Negotiables

1. **Where deterministic evidence exists, generative interpretation must remain subordinate to it.**
2. **Interpretation may explain established structure; it may not silently replace it.**
3. **A verifier must demonstrate that it can detect the failure it claims to guard against.**
4. **A metric is only meaningful relative to the completeness and independence of its denominator.**
5. **Use the strongest available evidence mechanism; do not substitute probabilistic judgment for deterministic comparison when deterministic comparison is available.**
6. **Review findings are claims requiring verification, not executable authority.**
7. **Before changing a canonical object, inspect its dependency radius.**
8. **When correctness cannot be established, expose uncertainty as state rather than fabricate completeness.**
9. **Cargo may influence interpretation within its authorized scope; cargo may not expand that scope.**
10. **As generative throughput increases, verification capacity must increase with it.**
11. **Automation that increases production throughput without increasing verification throughput creates governance debt.**
12. **Execution routing and verification routing are independent decisions.**
13. **Capability to produce does not establish capability to verify.**
14. **Verification intensity should scale with consequence, not implementation size.**
15. **The consequence of the package constrains how much unverified output may accumulate before inspection.**
16. **Handler limitations can be managed by reducing package scope without reducing destination scope.**

---

## 22. Canonical Statements

> **Where deterministic evidence exists, generative interpretation must remain subordinate to it.**

> **Interpretation may explain established structure; it may not silently replace it.**

> **TRACE ≠ TRUTH.**

> **EVAL PASS ≠ RELEASE.**

> **A verifier must demonstrate that it can detect the failure it claims to guard against.**

> **A control that has never demonstrated failure detection has not established its own competence.**

> **A metric is only meaningful relative to the completeness and independence of its denominator.**

> **Use the strongest available evidence mechanism; do not substitute probabilistic judgment for deterministic comparison when deterministic comparison is available.**

> **Execution routing and verification routing are independent decisions.**

> **Capability to produce does not establish capability to verify.**

> **BUILD_CAPABILITY ≠ REVIEW_CAPABILITY ≠ RELEASE_AUTHORITY.**

> **Verification intensity should scale with consequence, not implementation size.**

> **Package consequence, not handler identity, determines verification burden.**

> **The consequence of the package constrains how much unverified output may accumulate before inspection.**

> **Handler limitations can be managed by reducing package scope without reducing destination scope.**

> **Before changing a canonical object, inspect its dependency radius.**

> **Review findings are claims requiring verification, not executable authority.**

> **When correctness cannot be established, expose uncertainty as state rather than fabricate completeness.**

> **Cargo may influence interpretation within its authorized scope; cargo may not expand that scope.**

> **Documentation effort should be proportional to invisibility of failure, not merely complexity of implementation.**

> **As generative throughput increases, verification capacity must increase with it.**

> **Automation that increases production throughput without increasing verification throughput creates governance debt.**
