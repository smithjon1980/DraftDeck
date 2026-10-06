# PARCELS Layer Architecture

**Status:** Canonical Doctrine
**Placement:** Between Ontology and Process in the doctrine stack — `ONTOLOGY → PARCELS LAYER ARCHITECTURE → PRIME PROCESS`.
**Purpose:** Define where a concern lives in the system, so that doctrine, defects, and design decisions can be located precisely instead of argued about globally.

---

## 1. Why PARCELS Exists

The Logistics Framework defines *what the system is* (cargo, couriers, freight, proof of delivery).
PRIME defines *how work moves* (Package → Route → Inspect → Move → Establish Delivery).

Neither answers a prior question:

> **Where does a given concern, rule, or failure live in the system?**

Without a locating model, every defect becomes a global argument: is a retry bug a routing problem, a process problem, or a transport problem? PARCELS answers with seven layers, each owning a distinct responsibility, a distinct governance boundary, and a distinct dominant failure mode.

PARCELS uses the seven-layer OSI structure as **mnemonic scaffolding**, not as literal networking identity. (See the Structural-Correspondence Clause, §7.)

---

## 2. The Three-Axis Model

PARCELS does not stand alone. DraftDeck doctrine operates on three axes:

| Axis | Answers | Scope |
|---|---|---|
| **CONSTITUTION** | Why the system exists and what it may never do | Limits, prohibitions, invariants |
| **PARCELS** | Where a concern lives | Structural location |
| **PRIME** | How work moves | Operational sequence |

> **CONSTITUTION = why/limits × PARCELS = where × PRIME = how.**

Every doctrine file should be locatable on all three axes. A complete doctrine answers three locating questions:

1. **Where** does this doctrine's primary concern live in PARCELS?
2. **How** does it act in the PRIME sequence?
3. **What** constitutional limits constrain it?

### Worked coordinates

| Doctrine | Primary PARCELS layer | Secondary layers | PRIME coordinate |
|---|---|---|---|
| Shipping Label & Classification | L2 Attachment | L6 Language, L3 Routing | Package → Route boundary |
| Handoff & Context Routing | L5 Exchange | L3 Routing, L4 Carriage | Route → Move, across sessions |
| Verification & release | L7 Service | L4 Carriage | Inspect → Establish Delivery |

---

## 3. Layer Ownership ≠ Layer Exclusivity

A concern has exactly one **canonical home**, but it may produce effects in, and be detected at, other layers. These are three different things:

- **Canonical home** — the layer whose failure most directly explains the defect.
- **Cross-layer effect** — where the damage propagates.
- **Discovery location** — where someone happened to notice.

**Example — checksum mismatch.** A payload integrity check fails.
- *Canonical home:* **L2 Attachment** — identity and integrity of the package are its responsibility.
- *Cross-layer effect:* **L4 Carriage** — movement is interrupted or must be retried.
- *Discovery location:* **L7 Service** — the receiver may be the one who first reports the failure.

Assigning the defect to Service because it was discovered there, or to Carriage because movement stalled, mislocates the fix. The integrity rule belongs to Attachment.

---

## 4. The Seven Layers

Read bottom-up: each lower layer supplies capability the layer above relies on.

```text
┌─────────────────────────────────────┐
│ L7  SERVICE    — intent, acceptance, release      │
│ L6  LANGUAGE   — encoding, schema, semantics      │
│ L5  EXCHANGE   — durable work identity, sessions  │
│ L4  CARRIAGE   — movement semantics, retries      │
│ L3  ROUTING    — destination, policy, capability  │
│ L2  ATTACHMENT — identity, integrity, association │
│ L1  PLATFORM   — execution substrate              │
└─────────────────────────────────────┘
║ GOVERNANCE — a vertical plane across all seven    ║
```

### L1 — Platform

The execution substrate: compute, storage, runtimes, credentials, network reach, budgets.

- **Responsibility:** make work physically possible.
- **Dominant failure mode:** capability absence — the substrate cannot run the work at all (missing runtime, exhausted quota, unreachable store).
- **Governance boundary:** substrate provisioning and capacity, not work semantics.

> **Capability begins with available substrate.**

### L2 — Attachment

Identity, integrity, and association of the package: what it is, who sent it, that it is unaltered, that it is bound to the right context.

- **Responsibility:** establish that the package is what it claims to be, intact, and correctly associated.
- **Dominant failure mode:** identity/integrity failure — forged labels, tampered payloads, mis-associated context.
- **Governance boundary:** proof of identity and integrity, not permission.

> **Identity must precede delegation.**
> **Association ≠ authorization.**

A forged label is an Attachment failure even when it is discovered at Service.

### L3 — Routing

Destination, policy, and capability matching: where the package should go, which rules govern the choice, which handler can receive it.

- **Responsibility:** select a lawful destination and path.
- **Dominant failure mode:** misrouting — correct package, wrong destination; or a lawful destination the chosen handler cannot serve.
- **Governance boundary:** route selection and routing policy, not movement itself.

### L4 — Carriage

Movement semantics: retries, idempotency, ordering, flow control, delivery guarantees.

- **Responsibility:** define and enforce what *delivered* means for a movement: `AT_MOST_ONCE`, `AT_LEAST_ONCE`, `EFFECTIVELY_ONCE`.
- **Dominant failure mode:** movement-semantics failure — duplicates from retry, lost messages, reordered effects, unbounded re-delivery.
- **Governance boundary:** how movement behaves, not what the work means.

> **Movement must define its delivery semantics.**

A retry duplicate is a Carriage failure even when it corrupts an Exchange session.

### L5 — Exchange

Durable work identity and session continuity: `TASK_ID`, `CONTEXT_ID`, conversation spans, handoff linkage.

- **Responsibility:** keep work addressable and continuous across messages, sessions, and handlers.
- **Dominant failure mode:** identity-continuity failure — work that cannot be referenced after the conversation ends; context severed from its task.
- **Governance boundary:** continuity and reference, not content correctness.

> **Material work must have durable identity independent of the conversation that created it.**

### L6 — Language

Encoding, schema, and semantics: how meaning is represented, declared, and interpreted.

- **Responsibility:** ensure artifacts are interpretable under a declared schema and that representation maps to meaning.
- **Dominant failure mode:** representation failure — unparseable artifacts, schema violations, encoding drift.
- **Governance boundary:** interpretability, not business correctness.

> **Representation must not be mistaken for meaning.**

An artifact that cannot be interpreted under its declared schema is a Language failure. A correctly parsed artifact with the wrong business meaning is not — that is a Service failure.

### L7 — Service

Intent, acceptance, and release authority: what the work is *for*, whether the outcome fulfills that intent, and who may release it.

- **Responsibility:** establish that delivered output constitutes fulfilled service.
- **Dominant failure mode:** fulfillment failure — technically delivered, operationally wrong; correct artifact, wrong business meaning; release without authority.
- **Governance boundary:** acceptance and release, not transport correctness.

> **Technical delivery does not establish service fulfillment.**

---

## 5. The Dominant Failure Mode Rule

> **Assign each concern to the layer whose failure mode dominates. A concern may affect several layers, but its canonical home is the layer whose failure most directly explains the defect. Detection location does not determine layer ownership.**

Examples:

- A retry duplicate is a **Carriage** failure, even when it corrupts an Exchange session.
- A forged label is an **Attachment** failure, even when discovered at Service.
- A correctly parsed artifact with the wrong business meaning is a **Service** failure.
- An artifact that cannot be interpreted under its declared schema is a **Language** failure.

When a defect appears to implicate two layers, apply the tie-break: ask *which layer's rule, if correct, would have prevented the defect?* That layer owns it.

---

## 6. Governance Is a Vertical Plane, Not a Layer

There is no L8.

Governance — verification, release authority, audit, constitutional limits — does not sit above the stack. It crosses every layer:

- L1: capacity and credential governance.
- L2: identity and integrity verification.
- L3: routing-policy review.
- L4: delivery-semantics enforcement.
- L5: session audit and handoff traceability.
- L6: schema versioning and deprecation policy.
- L7: acceptance criteria and human release authority.

Promoting governance to a layer would imply some work happens *outside* it. Nothing does.

---

## 7. The Structural-Correspondence Clause (Anti-Bloat)

> **PARCELS uses the seven-layer OSI structure as mnemonic scaffolding, not as literal networking identity. Each layer must justify itself through a distinct responsibility, governance boundary, and dominant failure mode. The seven-layer form is subordinate to explanatory usefulness; structural correspondence does not authorize importing unrelated networking semantics into Prime.**

Conservative merge clause:

> **If two PARCELS layers can no longer demonstrate materially distinct failure modes or governance boundaries, their separation must be formally re-evaluated through the doctrine-change process rather than preserved merely to maintain seven layers.**

Seven is a scaffold, not a sacred number. A layer that cannot state its distinct dominant failure mode is a candidate for formal re-evaluation — not casual merging, and not preservation by inertia.

---

## 8. Relation to A2A

Agent-to-agent protocols fit *inside* PARCELS rather than competing with it.

- A2A-style message and task primitives map primarily onto **L5 Exchange** (durable task identity) and **L6 Language** (declared schemas for artifacts and messages), with transport concerns at **L4 Carriage**.
- PARCELS' largest additions beyond an A2A-style model are **L4 Carriage** (explicit delivery semantics) and **L1 Platform** (the substrate and its capability limits) — the two layers that protocol specifications often leave beneath their primary abstraction boundary.

External protocol adoption is an implementation choice; layer ownership is doctrine. (See the index: *Doctrine vs. Implementation*.)

---

## 9. Non-Negotiables

1. **PARCELS is structural correspondence, not literal networking identity.**
2. **Layer ownership ≠ layer exclusivity.**
3. **Assign canonical ownership by dominant failure mode, not by where the problem happened to be detected.**
4. **CONSTITUTION = why/limits × PARCELS = where × PRIME = how.**

---

## 10. Canonical Statements

> **Capability begins with available substrate.**

> **Identity must precede delegation. Association ≠ authorization.**

> **Movement must define its delivery semantics.**

> **Material work must have durable identity independent of the conversation that created it.**

> **Representation must not be mistaken for meaning.**

> **Technical delivery does not establish service fulfillment.**

> **Governance is a vertical plane across all seven layers; there is no L8.**

> **Detection location does not determine layer ownership.**
