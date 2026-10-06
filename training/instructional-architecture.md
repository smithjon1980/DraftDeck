# BOSS Instructional Architecture — The Two-Plane Fork

**Status:** Locked control document (program-level)
**Owner:** BOSS / Seven
**Governs:** The relationship between instructional design machinery and the learner-facing operational model, across all BOSS Operator Program artifacts
**Coordinates:** Sits beside `training/production-architecture.md`; subordinate to doctrine; binds the POI, Day Zero, module source packages, GRF, and all generated media

---

## 0. Why This Document Exists

Pre-production generation (NotebookLM and similar tools) exhibited a specific failure mode:

> **The teaching metaphor was promoted into the ontology.**

Generated material spoke as though learners were entering a literal logistics network — "welcome to the network," "today you become an operator moving cargo" — instead of using logistics as a disciplined way to reason about information movement.

This is not a tone problem to be patched in podcast language. It is an architectural defect: the instructional machinery and the subject being taught were allowed to blur into one plane. This document forks them permanently.

Canonical statements of this correction:

> **Instructional design governs how BOSS is taught. It is not the subject being taught.**

> **The logistics model describes information movement. It does not assert that information systems are literally parcel networks.**

> **The learner-facing anchor begins at the shipping counter: declare the package, inspect admission, then enter controlled movement.**

---

## 1. The Two Planes

```text
BOSS TRAINING SYSTEM
│
├── INSTRUCTIONAL CONTROL PLANE          (backstage — how we teach)
│   ├── Plan of Instruction
│   ├── Learning Envelope
│   ├── Learner State
│   ├── Diagnostics
│   ├── GRF (Guided Reasoning Format)
│   ├── Sequencing
│   ├── Assessment
│   ├── Remediation
│   └── Qualification
│
└── OPERATIONAL TEACHING MODEL           (frontstage — what we teach)
    ├── Sender
    ├── Request
    ├── Package
    ├── Shipping Label
    ├── Admission Inspection
    ├── Acceptance / Hold / Refusal
    ├── Classification
    ├── Route
    ├── Facility
    ├── Transfer
    ├── Transport / Handler Selection
    ├── High-Control Handling
    ├── Network Orchestration
    └── Proof of Delivery / Release
```

- The **Instructional Control Plane** is how we design and govern the course. Its movement chain is:

```text
MISSION
→ LEARNING ENVELOPE
→ DIAGNOSTIC
→ LEARNER STATE
→ INSTRUCTIONAL ROUTE
→ LESSON
→ PRACTICE
→ ASSESSMENT
→ STATE UPDATE
→ REMEDIATION / NEXT ROUTE
```

- The **Operational Teaching Model** is what the learner experiences and learns to perform: the governed movement of information packages.

**Rule:** The learner experiences primarily the Operational Teaching Model. The Instructional Control Plane determines how it is taught and must remain backstage.

---

## 2. Metaphor Discipline

The logistics model is a **structural correspondence**, not a fictional setting.

### Prohibited (metaphor promoted into reality)

- Addressing the learner as cargo, a package, or freight.
- Telling the learner they have "entered the network" or "joined the BOSS Shipping Company."
- Treating learner state as literal cargo moving through literal facilities.
- Any narration in which the training program itself is depicted as a parcel carrier employing the learner.

### Required (structural correspondence)

- The learner is a person who already moves information every day — between people, systems, models, files, and applications.
- BOSS provides a logistics model for **seeing those movements clearly**: what was actually sent, where it was allowed to go, what it needed to arrive with, and how arrival is established.
- Logistics vocabulary names **structures of reasoning about information work**. Correspondences may be drawn to familiar parcel-shipping experience because the structure genuinely matches — not because a fictional world is being built.

### Canonical Day Zero framing

> Every day you already move information between people, systems, models, files, and applications. Most failures happen because we pay attention to the work being performed and not enough attention to what was actually sent, where it was allowed to go, what it needed to arrive with, and how we know it arrived correctly. BOSS gives us a logistics model for seeing those movements clearly.

---

## 3. The Shipping Counter — Frontstage Anchor

The learner's first mental image:

> **You are standing at the shipping counter with something that needs to go somewhere. Before anybody touches the internal network, the shipment has to be specified well enough to accept.**

Most people already understand what happens when they physically ship something important:

- You do not throw a box through the loading-bay door and hope the carrier figures it out.
- You arrive with something you want moved, and you identify where it is going.
- You provide information about the shipment: who is sending, what is being sent, what handling it requires, what conditions matter, what establishes successful receipt.
- The clerk examines whether the shipment is sufficiently specified.
- Certain packages require different handling. Certain things cannot be accepted.
- If required information is missing, the carrier does not invent the missing address.
- Only after acceptance does the package enter the carrier's internal operational system.

This is the frontstage model:

```text
SENDER SPACE
─────────────────────────────────

NEED / REQUEST
↓
PACKAGE PREPARATION
↓
SHIPPING LABEL
   Who/what is sending?
   What is being sent?
   Where is it going?
   What handling it requires?
   What conditions matter?
   What establishes successful receipt?

              ↓

═════════════════════════════════
         ACCEPTANCE COUNTER
═════════════════════════════════

INSPECT DECLARATION
INSPECT PACKAGE CONDITIONS
CHECK HANDLING ELIGIBILITY
CHECK REQUIRED INFORMATION

        ┌─────────┬─────────┐
        ↓         ↓         ↓
     ACCEPT     HOLD     REFUSE

═════════════════════════════════
      CONTROLLED NETWORK ENTRY
═════════════════════════════════

CLASSIFY → ROUTE → SORT → HANDLE → TRANSFER
→ CARRY → RECEIVE → VERIFY → RELEASE
```

### Teaching lineage

PRIME's teaching lineage is **generic parcel-carrier / shipping-and-receiving operations**, anchored at the counter experience — not consumer fulfillment. Consumer fulfillment (click, warehouse, doorstep) hides the declaration step; counter shipping makes the sender actively specify the shipment before acceptance. That active specification — explicit package definition, declaration, acceptance conditions, handling eligibility, controlled admission — is exactly what BOSS cares about.

PRIME remains the proprietary protocol name. The anchor image is the counter.

---

## 4. Two Inspections, Not One

The shipping counter creates a pre-admission boundary. The first inspection happens **before** the package enters the network. This is distinct from the inspection inside PRIME.

```text
PRE-ADMISSION

PREPARE PACKAGE
↓
COMPLETE SHIPPING LABEL
↓
ADMISSION INSPECTION
↓
ACCEPT / HOLD / REFUSE

────────────────────────────────

PRIME — GOVERNED MOVEMENT

PACKAGE
↓
ROUTE
↓
INSPECT
↓
MOVE
↓
ESTABLISH DELIVERY
```

The two inspections ask different questions:

- **Admission Inspection:** *May this package enter controlled movement?*
- **PRIME INSPECT:** *Are the conditions for this particular movement satisfied?*

PRIME itself is unchanged. Admission is the gate in front of it; PRIME governs movement behind it.

### Canonical consequence

> **Capability is downstream from admissibility.**

A carrier does not say "we own a truck capable of carrying this, therefore we are authorized to accept it." This makes **CAN PROCESS ≠ MAY RECEIVE** immediately concrete at the counter.

---

## 5. Where Classification Lives

Cargo classification is an admission-time act. It precedes handler selection:

```text
SHIPPING LABEL
↓
ADMISSION INSPECTION
↓
CARGO CLASSIFICATION
↓
STANDARD / SENSITIVE / RESTRICTED / QUARANTINED / PROHIBITED
↓
ELIGIBILITY DECISION
↓
ACCEPT / HOLD / REFUSE
↓
ROUTE
```

Standing rules reaffirmed:

> **Cargo classification precedes handler selection.**

> **Unknown handling requirements produce HOLD, not guessed routing.**

Handling states describe how movement must be governed. They are not judgments about the value, truth, or quality of the cargo.

---

## 6. Module Topology Under the New Model

The module sequence follows the operational teaching model's natural progression. The metaphor follows the curriculum topology — never the reverse.

| Module | Operational Teaching Model anchor |
|---|---|
| 01 — Package Operations | The counter: bound the package, establish destination, establish required inputs, complete the shipping label, admission inspection → ACCEPT / HOLD / REFUSE |
| 02 — Route Operations | Behind the counter: the shipment is accepted — now where should it go? |
| 03 — Facility Operations | The sort facility: many packages moving safely through one environment |
| 04 — Transfer Operations | Custody transfer: identity, authority, and context preserved across handoffs |
| 05 — Transport Coordination | Service/transport selection: placement follows requirements |
| 06 — High-Control Operations | Special / restricted / high-consequence handling |
| 07 — Network Orchestration | The whole network: many packages, routes, handlers, coordinated without losing package-level accountability |

Module 01's internal arc:

```text
"I need to send this."
↓ WHAT IS IT?                    BOUND THE PACKAGE
↓ WHERE IS IT GOING?             ESTABLISH DESTINATION
↓ WHAT MUST TRAVEL WITH IT?      ESTABLISH REQUIRED INPUTS
↓ WHAT DOES THE CARRIER          COMPLETE THE SHIPPING LABEL
  NEED TO KNOW?
↓ IS IT READY TO ENTER           ADMISSION INSPECTION
  CONTROLLED MOVEMENT?
↓
ACCEPT / HOLD / REFUSE
```

---

## 7. Binding Rules for All Generated Media

1. **Plane separation.** Instructional machinery (Learning Envelope, diagnostics, learner state, remediation) must never be narrated to the learner as though it were part of the operational model. The learner is not "a package being routed"; learner state is not cargo.
2. **No literalization.** Generated media may use the counter, the label, the sort facility, and the handoff as explanatory correspondences. It may not depict a fictional BOSS carrier world in which the learner lives.
3. **Canonical statements verbatim.** CAPABILITY ≠ PERMISSION, CAN PROCESS ≠ MAY RECEIVE, and the other locked statements appear exactly, in contexts that show them operating at the counter and in the network.
4. **Admissibility before capability.** Any treatment of handler selection must establish admission and classification first.
5. **HOLD is legitimate.** Missing required information produces HOLD at the counter, exactly as a carrier refuses to invent a missing address.
6. **Audit hook.** During BOSS REFINEMENT, reviewers check every generated artifact for metaphor literalization as a named failure mode, alongside doctrine, terminology, and scope audits.

---

## 8. Boundary of This Document

- This document does not amend PRIME. It defines the pre-admission gate in front of PRIME.
- It does not amend the doctrine. It constrains how doctrine is taught and how generated media may speak.
- It binds Day Zero, all seven module source packages, the GRF, and every NotebookLM brief. Existing artifacts that violate the metaphor discipline are revised at their next controlled revision — beginning with the Day Zero source set and its seven audio scripts.

## Amendment Rule

Amendments to this document require the same guarded PR process as other controlled training material. Any amendment that would re-merge the two planes, literalize the metaphor, or move classification after handler selection is prohibited by construction.
