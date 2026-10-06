# Bounded Autonomy & Execution Envelopes

**Status:** Canonical Doctrine
**Placement:** Between Structure and Process in the doctrine stack — `LOGISTICS FRAMEWORK → PARCELS → BOUNDED AUTONOMY & EXECUTION ENVELOPES → PRIME PROCESS`.
**Purpose:** Constrain delegation before unattended execution. Define the constitutional limit on handler autonomy and the Execution Envelope as its enforcement shape.

---

## Doctrine Coordinates

> **Primary PARCELS:** L1 Platform
> **Secondary:** L3 Routing, L4 Carriage
> **PRIME influence:** before Package routing and throughout Move
> **Constitutional role:** constrain delegation before unattended execution

---

## 1. The Missing Article

Unattended execution changes the nature of delegation. An attended handler can be interrupted, corrected, and scoped mid-task. An unattended handler must be given enough freedom to complete the work — without receiving unrestricted authority over the surrounding system.

The common framing presents a false choice:

- constant permission prompts, which defeat unattended operation; or
- unrestricted execution, which defeats governance.

Both are wrong. The correct resolution is environmental:

> **Autonomy requires confinement before delegation.**

Constitutional form:

> **The degree of unattended autonomy granted to a handler must not exceed the containment, observability, and recovery guarantees of its execution environment.**

```text
MORE AUTONOMY
     requires
MORE CONFINEMENT
+ STRONGER OBSERVABILITY
+ BETTER RECOVERY
```

This principle is broader than any specific sandboxing technology. A sandbox is one implementation. The constitutional principle is **bounded autonomy**, and it governs research handlers, design handlers, file-processing handlers, deployment handlers, and eventually networked Prime couriers alike.

Autonomy is only safe when execution authority is bounded by environment design. Unattended autonomy is fundamentally an environment-governance problem, not a prompt-engineering problem.

---

## 2. Permission Belongs in the Envelope

The goal is not to remove permission controls. It is to resolve permitted scope *before* unattended execution starts.

> **Permission should be designed into the execution envelope rather than negotiated repeatedly during execution.**

The unattended pattern:

```text
HUMAN / GOVERNANCE
defines allowed envelope
        ↓
HANDLER
operates freely inside envelope
        ↓
BOUNDARY
prevents unauthorized escape
```

Inside the envelope, the handler should not need repeated infrastructure permission for actions already authorized by the envelope. The envelope does not eliminate escalation for ambiguity, authority-bearing decisions, irreversible consequences, or release. Outside the envelope, the handler should not be able to act.

---

## 3. The Execution Envelope

A sandbox is too narrow a name for what governance actually requires. The enforcement shape of bounded autonomy is the **Execution Envelope** — the complete declaration of the environment in which a package may move:

```text
EXECUTION_ENVELOPE

PACKAGE_ID
HANDLER_ID

RUNTIME
FILESYSTEM_SCOPE
NETWORK_SCOPE
TOOL_SCOPE

CREDENTIAL_SCOPE
SECRET_SCOPE

CPU / MEMORY / TIME LIMITS
COST BUDGET

ALLOWED ACTIONS
PROHIBITED ACTIONS

RETRY_POLICY
CANCELLATION_POLICY

LOGGING
ARTIFACT_DESTINATION

RETURN_ROUTE
```

> **Every unattended package moves inside an execution envelope.**

The abstraction is implementation-independent. The same envelope concept holds whether the substrate is a container, a cloud sandbox, a virtual machine, a worktree, an isolated browser session, a remote coding environment, or a future agent runtime. Any tool that provisions such an environment is an *adapter implementing an Execution Envelope*; the envelope is doctrine, the tool is not.

### Minimum substrate

Envelopes should be tight, not generous:

> **Execution environments should expose the minimum substrate required for the package.**

This is least privilege applied at L1 Platform. The dominant Platform failure is substrate/control failure: the handler can reach something it should not, or cannot access something the task requires. Both directions are envelope defects — over-provisioned scope is a containment failure; under-provisioned scope is a capability failure.

---

## 4. Identity Before Delegation

An unattended package must never arrive as an anonymous instruction. It arrives attached to durable identifiers:

```text
TASK_ID
PACKAGE_ID
CHANGE_SET_ID
HANDLER_ID
```

> **Autonomous work must remain attributable to a durable package, task, work surface or change set, and handler identity.**

This is the L2 Attachment rule — *Identity must precede delegation* — made concrete for unattended execution. `CHANGE_SET_ID` may be implemented as a source-control branch, worktree, document revision, artifact version, workspace, or equivalent bounded modification surface. The durable backlog itself is an L5 Exchange concern: the work object must survive the disappearance of any handler, session, or terminal. The backlog's implementation (issues, database tasks, Prime packages, protocol tasks, a queue) is replaceable; durable identity is not.

---

## 5. Roles, Not Identities

The functions in an autonomous workflow are **roles**:

```text
PLANNER
IMPLEMENTER
REVIEWER
MERGER
```

A **handler** is who or what performs a role. A **model** is one possible capability provider behind a handler.

> **Role must not be coupled to provider identity.**

Any handler with the required capability may fill any role, and providers may be swapped without doctrinal change. This is an anti-lock-in rule and a direct extension of *The domain defines the interfaces. Frameworks and services implement them.*

The executable form of the Constitution approaches:

```text
run(
  package,
  handler,
  executionEnvelope,
  policy,
  acceptanceProfile
)
```

which separates what simpler primitives conflate: HANDLER, ENVIRONMENT, and INSTRUCTION are distinct choices, independently governable.

---

## 6. Parallelism Is Governed, Not Assumed

Parallel unattended execution follows a concrete pattern:

```text
              ┌→ PACKAGE A → ENVELOPE A → CHANGE SET A ┐
MANIFEST → PLAN ─→ PACKAGE B → ENVELOPE B → CHANGE SET B ├→ REVIEW → CONSOLIDATE
              └→ PACKAGE C → ENVELOPE C → CHANGE SET C ┘
```

But lane count is downstream of the dependency graph, not of available compute:

> **Parallelism should emerge from dependency independence.**

The control gate:

```text
SEVERABLE?
    ↓
DEPENDENCIES DECLARED?
    ↓
CONFLICT RISK ACCEPTABLE?
    ↓
EXECUTION ENVELOPES AVAILABLE?
    ↓
PARALLELIZE
```

> **Do not create more lanes than the manifest can govern.**

### Movement semantics belong to Carriage

Concurrent execution raises L4 questions that must be answered by policy, not left to chance: What happens when two change sets touch the same governed surface? What happens if a worker dies? Can a task retry, and could duplicate execution occur? Can a task be cancelled? How is partial completion handled?

Autonomous execution envelopes should eventually declare:

```text
RETRY_POLICY
IDEMPOTENCY_PROFILE
TIMEOUT
CANCELLATION_POLICY
CONFLICT_POLICY
MAX_ATTEMPTS
```

These are Carriage-layer fields. *Movement must define its delivery semantics* applies with full force to unattended handlers.

---

## 7. Consolidation Is a Control Boundary

Parallel movement creates a need for controlled consolidation. The **Merger** is not another implementer; it is a distinct control role.

> **Parallel movement requires both severable work and an explicit consolidation boundary.**

The Merger receives:

```text
PARENT_MANIFEST
CHILD_PACKAGES
CHANGE SETS
PACKAGE OBJECTIVES
REVIEW RESULTS
CONFLICTS
```

and produces a **consolidated candidate**.

A candidate is not a release:

> **MERGE ≠ RELEASE.**

> **CONSOLIDATED ≠ RELEASED.**

Integration proves that the parts fit together. It does not establish that the intended service was fulfilled. The consolidated candidate returns to L7 Service for acceptance, verification, and authorized release:

```text
MERGED
   ↓
acceptance criteria
   ↓
integrated tests
   ↓
artifact/state verification
   ↓
human or governed release
```

This is the unattended-execution form of *TEST PASS ≠ DELIVERY ESTABLISHED*.

---

## 8. Independent Inspection

Review of unattended work should remain context-independent from implementation whenever practical:

```text
IMPLEMENTER CONTEXT
        ↓
ARTIFACT / DIFF
        ↓
FRESH REVIEW CONTEXT
```

The reviewer inspects the artifact, not the implementer's narration of it. Provider diversity across roles is an implementation option; independent inspection is the canonical principle. *Movement never substitutes for inspection.*

---

## 9. PARCELS Validation

The observed external pattern that motivated this doctrine — backlog, eligibility filter, planner, isolated sandboxes, parallel implementers, tests, independent review, merger, main — exercises all seven PARCELS layers without forcing any structural contortion:

| Layer | Observed concern |
|---|---|
| L1 Platform | Sandbox substrate: filesystem boundary, runtime, tools, credentials |
| L2 Attachment | Task, package, change-set, and handler identity bound to the work |
| L3 Routing | Label-based admission control; dependency-aware eligibility |
| L4 Carriage | Retry, idempotency, cancellation, conflict semantics |
| L5 Exchange | Durable backlog; work survives handler disappearance |
| L6 Language | Structured planner output under declared schema, not free-form prose |
| L7 Service | Acceptance, verification, release authority |

Two observations strengthen the architecture:

1. **This specimen exercised all seven layers without requiring a new layer or collapsing an existing one.** Within this specimen, no observed concern was structurally homeless and no PARCELS layer lacked a corresponding concern. This is specimen-level structural validation of the kind the anti-bloat clause demands.
2. **The observed pattern's weakest region was Carriage.** Its retry, idempotency, and cancellation semantics were left implicit — which is exactly the failure surface Carriage exists to govern, and evidence that L4 earns its separation.

---

## 10. Relation to the Shipping Label

This doctrine establishes *why* execution requirements must exist. A follow-on doctrine change should amend the Prime Shipping Label to *carry* them — fields such as:

```text
EXECUTION_CLASS
SANDBOX_REQUIRED
NETWORK_POLICY
FILESYSTEM_POLICY
CREDENTIAL_PROFILE
TIME_LIMIT
COST_LIMIT
PARALLEL_SAFE
IDEMPOTENCY_CLASS
HUMAN_REVIEW_REQUIRED
```

With those fields declared, routing policy selects not merely *which handler* but *which handler plus which execution envelope*.

Constitutional change stays upstream of schema change: this doctrine does not modify the Shipping Label; it authorizes and constrains the amendment that will.

---

## 11. Language Discipline in Delegation

Inter-handler contracts should become increasingly structured as reliability requirements rise. Prompts may remain natural language internally, but orchestrator-to-handler and planner-to-orchestrator boundaries should prefer declared schemas over interpretive prose.

> **Machine-to-machine delegation should prefer declared schemas over interpretive prose where reliable parsing matters.**

This is L6 Language discipline applied to delegation: *Representation must not be mistaken for meaning.*

---

## 12. External References

This doctrine was sharpened by studying an external autonomous-execution tool ("Sand Castle") and its workflow: eligibility-filtered backlog, planner decomposition, isolated parallel sandboxes, independent review, and a merger role. Per *Doctrine vs. External References*: the mechanics were studied; the doctrine above is ours. The tool itself is, at most, a candidate adapter implementing Execution Envelopes.

> **Study the mechanics. Preserve our doctrine.**

---

## 13. Non-Negotiables

1. **Autonomy requires confinement before delegation.**
2. **The degree of unattended autonomy granted to a handler must not exceed the containment, observability, and recovery guarantees of its execution environment.**
3. **Permission should be designed into the execution envelope rather than negotiated repeatedly during execution.**
4. **Parallel movement requires both severable work and an explicit consolidation boundary.**
5. **MERGE ≠ RELEASE.**
6. **Role must not be coupled to provider identity.**

---

## 14. Canonical Statements

> **Autonomy requires confinement before delegation.**

> **Permission should be designed into the execution envelope rather than negotiated repeatedly during execution.**

> **Every unattended package moves inside an execution envelope.**

> **Execution environments should expose the minimum substrate required for the package.**

> **Autonomous work must remain attributable to a durable package, task, work surface or change set, and handler identity.**

> **Role must not be coupled to provider identity.**

> **Parallelism should emerge from dependency independence.**

> **Do not create more lanes than the manifest can govern.**

> **MERGE ≠ RELEASE. CONSOLIDATED ≠ RELEASED.**

> **Machine-to-machine delegation should prefer declared schemas over interpretive prose where reliable parsing matters.**
