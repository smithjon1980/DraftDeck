# Restricted Cargo Handling

**Status:** Candidate Canonical Doctrine  
**Owner:** BOSS — Bioscillate Operating System by Seven  
**Placement:** Immediately after Bioscillate PRIME Shipping Label & Classification and before PRIME Protocol Orchestration.  
**Primary PARCELS:** L3 Routing  
**Secondary PARCELS:** L2 Attachment; Governance Vertical Plane  
**PRIME Influence:** Hard gate between Package and Route  
**Purpose:** Define how BOSS identifies, holds, sanitizes, refuses, and routes information whose ownership, sensitivity, authorization, retention, or downstream consequence requires restricted handling.

---

## 1. Why This Doctrine Exists

The Shipping Label already carries sensitivity, data-boundary, locality, handler, and execution requirements. Those fields require a doctrine that defines what they protect and what the network must do when cargo is not eligible for ordinary movement.

Restricted Cargo Handling governs the gap between classification and routing.

> **Not every package that can be moved is authorized for movement.**

A handler may be technically capable of processing a package while still being unauthorized to receive it.

> **CAN PROCESS ≠ MAY RECEIVE.**

Capability and permission are independent axes.

This doctrine defines handling state and disposition. It does not judge the quality, value, truth, or morality of the cargo.

---

## 2. Dominant Failure Boundary

The dominant failure is **misrouting across a boundary**:

> cargo reaches a handler, destination, network, storage location, or service that was not authorized to receive it.

That makes L3 Routing the primary PARCELS home.

L2 Attachment is secondary because ownership, authorization context, provenance, and handling obligations must remain bound to the cargo.

The Governance Vertical Plane applies because authorization must survive every handoff.

> **Authorization follows the cargo across every handoff.**

Detection at another layer does not change canonical ownership of the failure.

---

## 3. Pre-Routing Gate

Restricted-cargo classification occurs before handler selection.

~~~text
PACKAGE
   ↓
READ / VALIDATE SHIPPING LABEL
   ↓
CLASSIFY CARGO HANDLING STATE
   ↓
CHECK OWNERSHIP / AUTHORIZATION
   ↓
CHECK DESTINATION / HANDLER ELIGIBILITY
   ↓
ROUTE / HOLD / REFUSE / SANITIZE
~~~

> **Cargo classification precedes handler selection.**

A capable handler beyond an unauthorized boundary remains ineligible.

> **Sensitive cargo must not cross a boundary merely because a capable handler exists beyond it.**

---

## 4. Five Handling States

These are handling states, not quality judgments.

### STANDARD

Cargo may move through ordinary permitted routes subject to the rest of the Shipping Label and policy.

### SENSITIVE

Cargo requires elevated handling controls, but movement remains possible when the declared boundary, handler, and policy permit it.

### RESTRICTED

Cargo may move only through explicitly authorized destinations, handlers, execution environments, and retention conditions.

### QUARANTINED

Handling requirements or authorization are unresolved, conflicting, incomplete, or not yet established. Movement is held until classification and authority are resolved.

### PROHIBITED

The package is not eligible to move through the requested route or network under current policy or authority.

~~~text
STANDARD
SENSITIVE
RESTRICTED
QUARANTINED
PROHIBITED
~~~

A state may change only through evidence, authorized policy, sanitization into a new package, or authorized adjudication.

---

## 5. Four Dispositions

Restricted Cargo Handling distinguishes state from action.

### ROUTE

The package is eligible for a permitted destination and handler under its current label.

### HOLD

Movement stops while missing, conflicting, or authority-bearing information is resolved.

### REFUSE

The requested movement is not permitted. The network does not send the package through the prohibited route.

### SANITIZE → RECLASSIFY → ROUTE

An authorized transformation may remove or reduce restricted content so that a newly bounded package becomes eligible for a different route.

~~~text
ROUTE
HOLD
REFUSE
SANITIZE → RECLASSIFY → ROUTE
~~~

Sanitization does not rewrite the history or authorization state of the original package.

> **Sanitization may change routing eligibility; it does not retroactively authorize the original package.**

The sanitized result is a new package with its own identity, provenance, label, and routing decision.

---

## 6. Quarantine as Governed Unknown

Quarantine is the operational form of explicit uncertainty.

~~~text
UNKNOWN HANDLING REQUIREMENT
        ↓
QUARANTINE / HOLD
        ↓
IDENTIFY OWNER
        ↓
ESTABLISH CLASSIFICATION
        ↓
ESTABLISH AUTHORIZED DESTINATIONS / HANDLERS
        ↓
ROUTE / RESTRICT / REFUSE
~~~

> **Unknown handling requirements produce HOLD, not guessed routing.**

This specializes the Evidence & Verification rule:

> **When correctness cannot be established, expose uncertainty as state rather than fabricate completeness.**

Restricted Cargo Handling does not redefine that rule; it applies it to movement authority.

---

## 7. Capability and Permission

The system must never infer authorization from technical capability.

~~~text
CAPABILITY = SUFFICIENT
AUTHORIZATION = NOT ESTABLISHED
ROUTE = BLOCKED
~~~

This sits beside existing BOSS separations:

~~~text
CAPABILITY ≠ PERMISSION
PLACEMENT ≠ CAPABILITY
ROLE ≠ AUTHORITY
~~~

A handler may be powerful enough to perform the work and still be disallowed from receiving the cargo.

---

## 8. Minimum Necessary Cargo

Movement should be bounded to the smallest package necessary to fulfill the authorized service.

> **The minimum necessary cargo should travel.**

This may require:

- extracting only required fields;
- redacting unrelated sensitive content;
- separating public from restricted attachments;
- creating a derived package with narrower scope;
- using an authorized local or private environment;
- refusing movement when minimum-necessary handling still exceeds policy.

Minimum-necessary scope is a routing and disclosure control, not permission to alter authoritative source silently.

---

## 9. Authorization Across Handoffs

Every handoff must preserve the cargo's applicable handling constraints.

A handoff may not silently broaden:

- destination eligibility;
- handler eligibility;
- retention duration;
- external-transfer permission;
- training-use permission;
- credential scope;
- disclosure scope.

> **Authorization follows the cargo across every handoff.**

A downstream handler receives no greater authority merely because an upstream handler forwarded the package.

---

## 10. Legitimate Work Can Still Be Unsafe to Route

A request may be valid while its requested route is not.

Examples include legitimate requests to summarize, debug, classify, compare, or transform information whose disclosure boundary does not permit the selected handler.

> **The network must protect against unauthorized disclosure even when the requested work itself is legitimate.**

The network therefore evaluates both:

~~~text
SERVICE LEGITIMACY
and
ROUTING AUTHORIZATION
~~~

One does not establish the other.

---

## 11. Shipping Label Contract

Restricted Cargo Handling consumes the Shipping Label fields that describe ownership, sensitivity, boundaries, and authorization.

The label should support at least:

~~~text
CARGO_HANDLING_CLASS
DATA_OWNER
DATA_CLASSIFICATION
PERMITTED_DESTINATIONS
PROHIBITED_DESTINATIONS
PERMITTED_HANDLERS
PROHIBITED_HANDLERS
EXTERNAL_TRANSFER_ALLOWED
RETENTION_CONSTRAINT
TRAINING_USE_ALLOWED
SANITIZATION_REQUIRED
MINIMUM_NECESSARY_SCOPE
~~~

The label declares the handling contract.

This doctrine defines the consequences of that contract.

---

## 12. PARCELS Mapping

| Coordinate | Restricted Cargo Responsibility |
|---|---|
| L2 Attachment | Bind ownership, provenance, handling obligations, and authorization context to cargo. |
| L3 Routing | Prevent movement to an unauthorized destination, handler, network, or service. |
| Governance Plane | Preserve authority and handling constraints across every handoff and state transition. |
| L4 Carriage | Enforce hold, refusal, and movement constraints during transport. |
| L7 Service | Ensure an otherwise legitimate service request does not override cargo restrictions. |

The primary home remains L3 because the dominant defect is unauthorized routing across a boundary.

---

## 13. PRIME Mapping

Restricted Cargo Handling operates primarily between Package and Route.

~~~text
PACKAGE
   ↓
SHIPPING LABEL
   ↓
RESTRICTED-CARGO GATE
   ↓
ROUTE
   ↓
INSPECT
   ↓
MOVE
   ↓
ESTABLISH DELIVERY
~~~

The gate may return:

~~~text
ROUTE
HOLD
REFUSE
SANITIZE → NEW PACKAGE → RECLASSIFY
~~~

The existence of a route does not imply the package is eligible to enter it.

---

## 14. Relationship to Existing Doctrine

### Bioscillate PRIME Shipping Label & Classification

The Shipping Label carries the fields. Restricted Cargo Handling defines the states and dispositions that make those fields operational.

### Evidence & Verification Architecture

Explicit uncertainty becomes quarantine or hold where uncertainty affects movement authority. This doctrine cross-references the evidence rule; it does not redefine it.

### Bounded Autonomy & Execution Envelopes

Execution envelopes may enforce network, filesystem, credential, locality, or runtime boundaries required by restricted cargo. This doctrine does not amend the envelope model.

### PRIME Handoff & Context Routing

Transit packages must preserve restricted-cargo constraints. Context minimization and minimum-necessary cargo are mutually reinforcing but remain distinct responsibilities.

---

## 15. Studied Reference Boundary

This doctrine was informed by a user-supplied security-training transcript describing classes of information that should not be casually uploaded to cloud-hosted AI systems, including financial records, health information, proprietary code, confidential business strategy, and sensitive legal material.

The transcript is treated as a studied reference and specimen, not as BOSS authority.

BOSS generalizes the lesson into a tool-neutral restricted-cargo control model. It does not make categorical claims that every instance of any named document type is always prohibited, because actual handling depends on ownership, policy, authorization, environment, contractual obligations, and applicable law.

---

## 16. Canonical Statements

> **Not every package that can be moved is authorized for movement.**

> **CAN PROCESS ≠ MAY RECEIVE.**

> **Cargo classification precedes handler selection.**

> **Sensitive cargo must not cross a boundary merely because a capable handler exists beyond it.**

> **Unknown handling requirements produce HOLD, not guessed routing.**

> **Sanitization may change routing eligibility; it does not retroactively authorize the original package.**

> **The minimum necessary cargo should travel.**

> **Authorization follows the cargo across every handoff.**

> **The network must protect against unauthorized disclosure even when the requested work itself is legitimate.**
