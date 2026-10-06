# BOSS Naming Architecture

**Status:** Candidate Canonical Doctrine  
**Owner:** BOSS — Bioscillate Operating System by Seven  
**Purpose:** Fix the naming hierarchy of the BOSS system so system, framework, architecture, protocol, specialization, and product each have one distinct referent.

---

## 1. Canonical Identity

The governing system is:

> **BOSS — Bioscillate Operating System by Seven**

**Bioscillate** is spelled **B-I-O-S-C-I-L-L-A-T-E** and combines the terms *Bio* and *Oscillate*.

The public domain associated with the system is:

> **www.bioscillate.com**

BOSS owns the doctrine stack. Products may implement BOSS doctrine; products do not own or redefine it.

---

## 2. Naming Hierarchy

The canonical hierarchy is:

```text
BOSS — BIOSCILLATE OPERATING SYSTEM BY SEVEN
the system; owner of the doctrine stack
        ↓
BIOSCILLATE LOGISTICS FRAMEWORK
the governing conceptual model
        ↓
PARCELS
the seven-layer structural architecture
        ↓
BIOSCILLATE PRIME PROTOCOL
the governed movement protocol
        ↓
DOMAIN SPECIALIZATIONS
Instruction · Agent Execution · Research · Design · Production · Verification
        ↓
PRODUCTS
DraftDeck = the visual-production engine / product
```

Each level has a different job. A lower level may implement or specialize an upper level, but may not silently replace it.

---

## 3. Term Contract

### System

A **system** is the governing whole.

Canonical referent:

> **BOSS — Bioscillate Operating System by Seven**

Do not use a product name as a synonym for the system.

### Framework

A **framework** defines the conceptual model in which the system reasons.

Canonical referent:

> **Bioscillate Logistics Framework**

The Logistics Framework defines the shipping-and-receiving ontology used by BOSS.

### Architecture

An **architecture** defines stable structural organization.

Canonical referent:

> **PARCELS**

PARCELS defines where responsibilities, concerns, and dominant failure modes live across the seven layers.

### Protocol

A **protocol** governs an ordered movement sequence with defined transitions, controls, evidence requirements, and a terminal state.

Canonical referent:

> **Bioscillate PRIME Protocol**

PRIME governs:

```text
PACKAGE → ROUTE → INSPECT → MOVE → ESTABLISH DELIVERY
```

### Specialization

A **specialization** applies BOSS doctrine to a domain without becoming the governing system.

Examples include:

- Instruction
- Agent execution
- Research
- Design
- Production
- Verification

A specialization may introduce domain-specific contracts, envelopes, or procedures, but it remains subordinate to BOSS doctrine.

### Product

A **product** is a concrete implementation offered to perform work.

Canonical product referent in the current repository:

> **DraftDeck**

DraftDeck is the visual-production engine and productized production specialization of BOSS.

> **BOSS owns the doctrine. DraftDeck implements a production specialization of that doctrine.**

---

## 4. PRIME Naming Rule

When referring to the named protocol, write:

> **Bioscillate PRIME Protocol**

Short form:

> **PRIME Protocol**

The acronym is always uppercase when referring to the protocol:

- **P — PACKAGE**
- **R — ROUTE**
- **I — INSPECT**
- **M — MOVE**
- **E — ESTABLISH DELIVERY**

The lowercase word *prime* may still be used as an ordinary adjective where grammar requires it. Ordinary adjective use does not refer to the protocol.

The existing file path `prime-process.md` may remain unchanged until a dedicated path-migration change is justified. Semantic identity precedes filename churn.

---

## 5. PARCELS Naming Rule

When referring to the named architecture, write:

> **PARCELS**

PARCELS is an architecture, not the system and not the movement protocol.

It answers:

> **Where does this concern, responsibility, or dominant failure mode live?**

---

## 6. BOSS Ownership Rule

Doctrine ownership language must refer to **BOSS**, not DraftDeck, when discussing the governing doctrine stack as a whole.

Correct:

> BOSS doctrine governs the system.

Incorrect:

> DraftDeck doctrine governs the system.

DraftDeck remains correct where the referent is specifically the product, its visual-production engine, its product contract, examples, generated artifacts, or product-specific implementation.

---

## 7. Product Demotion Is Not Product Devaluation

Moving DraftDeck below BOSS does not reduce its importance.

It clarifies its role.

DraftDeck was the first substantial workload through which much of the doctrine was developed and pressure-tested. Its correct place is therefore:

```text
BOSS DOCTRINE
        ↓
PRODUCTION SPECIALIZATION
        ↓
DRAFTDECK PRODUCT
```

A product may be the first implementation of doctrine without becoming the owner of doctrine.

---

## 8. Repository Boundary

The GitHub repository may continue to be named `DraftDeck`.

Repository location does not determine doctrine ownership.

> **Implementation location does not redefine system identity.**

A future repository split or rename is a separate implementation decision and must not be inferred from this naming doctrine.

---

## 9. Domain and Brand Boundary

The canonical public identity is:

```text
BOSS
Bioscillate Operating System by Seven
www.bioscillate.com
```

The naming architecture does not assert affiliation with any external company, platform, or logistics provider.

The Bioscillate Logistics Framework remains an original governing conceptual model inside BOSS.

---

## 10. Canonical Stack Reading

A fresh human or agent should be able to distinguish these questions immediately:

| Level | Canonical Name | Question |
|---|---|---|
| System | BOSS — Bioscillate Operating System by Seven | What is the governing whole? |
| Framework | Bioscillate Logistics Framework | What conceptual model governs reasoning? |
| Architecture | PARCELS | Where do concerns and failures live? |
| Protocol | Bioscillate PRIME Protocol | How does bounded work move? |
| Specialization | Instruction / Agent Execution / Research / Design / Production / Verification | How is doctrine applied in a domain? |
| Product | DraftDeck | What concrete product implements a specialization? |

---

## 11. Non-Negotiables

1. **BOSS is the system and owner of the doctrine stack.**
2. **The Bioscillate Logistics Framework is the governing conceptual model.**
3. **PARCELS is the seven-layer structural architecture.**
4. **The Bioscillate PRIME Protocol is the governed movement protocol.**
5. **Specializations apply doctrine; they do not replace it.**
6. **Products implement specializations; they do not become the system.**
7. **DraftDeck is a product, not the owner of BOSS doctrine.**
8. **PRIME is uppercase whenever it refers to the named protocol.**

---

## 12. Canonical Statements

> **BOSS — Bioscillate Operating System by Seven — is the governing system.**

> **BOSS owns the doctrine. DraftDeck implements a production specialization of that doctrine.**

> **The Bioscillate Logistics Framework is the governing conceptual model.**

> **PARCELS is the seven-layer structural architecture.**

> **The Bioscillate PRIME Protocol governs Package → Route → Inspect → Move → Establish Delivery.**

> **Frameworks describe conceptual worlds; protocols govern sequences.**

> **Products implement specializations; products do not own the system.**

> **Implementation location does not redefine system identity.**

> **Semantic identity precedes filename churn.**
