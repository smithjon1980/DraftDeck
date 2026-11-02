# 02 — BOSS Core Doctrine for Training (Compiled Excerpts)

**Document role:** Consolidated doctrine source for NotebookLM. Each excerpt is marked with its canonical source file and section. These excerpts are authority; training artifacts must not contradict them.

---

## Excerpt 1 — Canonical Ontology

SOURCE: doctrine/logistics-framework.md
SECTION: Canonical doctrine

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

The system handles packages: information is prepared, classified, routed, transported, received, checked, and released.

---

## Excerpt 2 — Control Spine

SOURCE: doctrine/logistics-framework.md
SECTION: Four-function control spine

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

1. **Location** — Identify the proposition, package, route context, and handling destination.
2. **Accounting** — Record what the package contains, where it came from, what supports it, what remains unknown, and what dependencies it carries.
3. **Adjudication** — Compare the delivered package against the relevant warrant, evidence, comparator, or ground-truth fixture. Routing and accounting do not themselves establish truth.
4. **Authority** — Release occurs only under valid human authority.

---

## Excerpt 3 — Logistics Roles

SOURCE: doctrine/logistics-framework.md
SECTION: Logistics roles

- **Sender** — originates a package or request.
- **Receiver / consignee** — intended recipient and release context.
- **Courier / agent** — transports or transforms a package under declared instructions.
- **Freight / model service** — computational capability used during transport or handling.
- **Shipping & Receiving Control Desk** — human command, handling, and release authority.
- **Verification Tag** — proof-of-delivery metadata and status.

---

## Excerpt 4 — The PRIME Protocol

SOURCE: doctrine/prime-process.md
SECTION: The PRIME Acronym

> **PRIME = Package → Route → Inspect → Move → Establish Delivery**

**P — PACKAGE.** Identify and prepare the cargo units that must move. A package is the smallest accountable unit in the process. Rule: *Undefined cargo cannot be routed reliably.*

**R — ROUTE.** Determine where the package belongs and which handling path it requires. Rule: *Route according to the job, not according to prestige.*

**I — INSPECT.** Verify identity, provenance, constraints, risk, and delivery requirements before or during movement. Rule: *Movement never substitutes for inspection.*

**M — MOVE.** Execute the route through the appropriate handlers and processing stages. Rule: *Use only as much infrastructure as the shipment requires.*

**E — ESTABLISH DELIVERY.** Confirm that the correct cargo reached the correct destination, in an acceptable state, with proof and proper release authority. Rule: *Completion is a verified state, not an activity count.*

---

## Excerpt 5 — Block vs. Package

SOURCE: doctrine/prime-process.md
SECTION: The Block Is the Commitment

> **The block is the unit of operational commitment; the package is the unit of accountability.**

The operator commits to a bounded block of work, but each package inside it still needs an accountable destination and delivery state.

---

## Excerpt 6 — Bounded Manifest

SOURCE: doctrine/prime-process.md
SECTION: The Bounded Manifest Principle

> **A manifest must be bounded before movement begins.**

A manifest may include package identifiers, type, source/provenance, destination, route, handling constraints, priority, assigned handler, verification requirement, status, and proof-of-delivery record.

Instead of "keep working until this feels done," PRIME asks: *What packages are in this block, where are they going, what handling does each require, and what will count as established delivery?*

---

## Excerpt 7 — Throughput vs. Correctness

SOURCE: doctrine/prime-process.md
SECTION: Package Accountability vs. Network Throughput

> **Throughput is a network metric. Delivery is a package claim.**

A system can process a large manifest while misrouting packages, losing provenance, skipping inspection, or marking unresolved work as complete. Neither metric substitutes for the other.

---

## Excerpt 8 — Alignment Doctrine

SOURCE: doctrine/prime-alignment-decomposition-feedback.md
SECTION: Canonical statements

> **Alignment precedes packaging.**

> **Instrument the route before sending the package.**

> **Stale context is active contamination.**

A package that moves without acceptance signals is cargo without a manifest.

---

## Excerpt 9 — Instruction Doctrine

SOURCE: doctrine/aligned-instruction-learning-envelope.md
SECTION: Canonical statements

> **Instruction begins with alignment, not content.**

> **A learner's destination, current state, constraints, and available attention govern the route.**

> **A learning goal should be expressed as an observable capability whenever practical.**

> **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**

> **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

> **Representation ≠ learning.**

---

## Excerpt 10 — Handler and Capability Rules

SOURCE: doctrine/prime-shipping-label-classification.md
SECTION: Handler and capability rules

> **Describe the handling requirement first. Select the handler second.**

> **Route according to the job, not according to prestige.**

> **Capability to produce does not establish capability to verify.**

> **Handler limitations can be managed by reducing package scope without reducing destination scope.**

---

## Excerpt 11 — Cargo Authorization

SOURCE: doctrine/restricted-cargo-handling.md
SECTION: Canonical statements

> **Not every package that can be moved is authorized for movement.**

> **CAN PROCESS ≠ MAY RECEIVE.**

> **The minimum necessary cargo should travel.**

---

## Excerpt 12 — Verification and Release

SOURCE: doctrine/evidence-verification-architecture.md and doctrine/README.md
SECTION: Canonical statements

> **TEST PASS ≠ DELIVERY ESTABLISHED.**

> **MERGE ≠ RELEASE.**

> **EVAL PASS ≠ RELEASE.**

> **When correctness cannot be established, expose uncertainty as state rather than fabricate completeness.**

---

## Excerpt 13 — Naming Hierarchy

SOURCE: doctrine/naming-architecture.md
SECTION: Naming hierarchy

```text
BOSS — the system; owner of the doctrine stack
BIOSCILLATE LOGISTICS FRAMEWORK — the governing conceptual model
PARCELS — the seven-layer structural architecture
BIOSCILLATE PRIME PROTOCOL — the governed movement protocol
DOMAIN SPECIALIZATIONS — Instruction, Agent Execution, Research, Design, Production, Verification
PRODUCTS — DraftDeck = the visual-production engine
```

> **Frameworks describe conceptual worlds; protocols govern sequences.**

> **Products implement specializations; products do not own the system.**
