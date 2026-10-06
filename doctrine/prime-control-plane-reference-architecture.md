# Prime Control Plane Reference Architecture Doctrine

**Status:** Candidate Canonical Doctrine  
**Framework:** Logistics Framework → Prime Process  
**Repository Role:** Reference architecture / implementation doctrine  
**Purpose:** Define the preferred first implementation architecture for a Prime Process operational control plane while preserving server authority, explicit interfaces, replaceable adapters, doctrine-to-code traceability, and low unnecessary complexity.

---

## 1. Doctrine Upgrade

The existing canon defines:

- how work is packaged;
- how labels are created and scanned;
- how classifiers inform routing;
- how work is orchestrated;
- how context is handed off;
- how delivery is verified and released.

This document defines a preferred implementation architecture for turning that doctrine into a working operator-facing application.

The reference architecture is:

~~~text
PRIME DOMAIN
    ↓
THIN HTTP ADAPTER
    ↓
TYPED SERVER-RENDERED PRESENTATION
    ↓
LIGHTWEIGHT HYPERMEDIA INTERACTION
    ↓
REPLACEABLE PERSISTENCE / AUTH / REALTIME ADAPTER
~~~

A current candidate implementation is:

~~~text
Go
+ Chi
+ templ
+ HTMX
+ PocketBase adapter
+ owned CSS or Tailwind adapter
~~~

The technologies are replaceable.

The boundaries are not.

---

## 2. Governing Principle

The architecture should remain as simple as possible while preserving the control boundaries Prime requires.

> **Keep the system small enough to understand, but modular enough to govern.**

The browser should display governed state.

The server should remain authoritative.

### Server Authority Rule

> **The UI displays governed state. It does not become the source of governed state.**

The client may request actions.

The server validates, decides, records, and renders the resulting authoritative state.

---

## 3. Why a Hypermedia Architecture Fits Prime

A Prime operator console is primarily concerned with state transitions such as:

~~~text
CREATED
→ LABELED
→ VALIDATED
→ CLASSIFIED
→ ROUTED
→ MOVING
→ HELD / VERIFIED
→ RELEASED
~~~

These transitions do not require a duplicated client-side application state machine.

A hypermedia architecture allows the browser to submit an action and receive updated HTML representing the new server-authoritative state.

Example:

~~~text
POST /packages/{id}/scan
        ↓
validate label
        ↓
classify cargo
        ↓
compare declared vs observed
        ↓
apply routing policy
        ↓
persist result
        ↓
render updated package panel
~~~

### Hypermedia Rule

> **Prefer server-authoritative state transitions with HTML responses over duplicated client state when the workflow does not require a full client-side application model.**

---

## 4. Comparison of the Two Studied Web Patterns

Two source transcripts were studied.

### Pattern A — Structured GOTH-style stack

The first pattern emphasized:

- Go;
- Chi;
- templ;
- HTMX;
- Tailwind;
- explicit interfaces;
- dependency injection;
- middleware;
- content-security policy;
- generated-file separation;
- store abstraction;
- graceful shutdown;
- build tooling.

Its strength is architectural discipline.

### Pattern B — Minimal Go web stack

The second pattern emphasized:

- Go;
- Gin;
- standard HTML templates;
- HTMX;
- SQLite;
- minimal moving parts;
- direct request/response flow;
- PocketBase as an optional backend shortcut.

Its strength is architectural simplicity.

### Synthesis Rule

> **Use the simplicity test from the minimal stack and the structural discipline from the more modular stack.**

Prime should not copy either implementation wholesale.

It should preserve their useful mechanics inside Prime-native boundaries.

---

## 5. Domain First, Framework Second

The application must not become a framework-shaped system.

Prime domain contracts should exist independently of the HTTP router, template engine, database adapter, or frontend interaction library.

Recommended interfaces include:

~~~text
PackageStore
LabelStore
LabelValidator
Classifier
RoutingPolicy
HandlerRegistry
InspectionService
Verifier
ReleaseAuthority
~~~

Implementations may change without changing the domain contract.

### Domain Boundary Rule

> **The domain defines the interfaces. Frameworks and services implement them.**

This preserves tool independence and prevents infrastructure choices from becoming ontology.

---

## 6. Preferred HTTP Boundary

A thin HTTP layer is preferred.

A lightweight router such as Chi is currently favored because it remains close to Go's standard request/response model and makes it easier to keep framework-specific types out of domain logic.

Gin remains a valid adapter.

Neither is canonical doctrine.

### Router Rule

> **The HTTP router is an adapter, not the application architecture.**

The primary selection criteria are:

- thin abstraction;
- middleware support;
- testability;
- low framework leakage;
- stable maintenance;
- compatibility with standard Go interfaces.

---

## 7. Typed Server-Rendered Presentation

A typed rendering layer such as templ is currently preferred over unstructured template maps for Prime's operator console.

Prime concepts can map directly to typed presentation components:

~~~text
PackagePanel
ShippingLabel
ManifestView
ScanResult
ClassificationResult
RouteDecision
HoldNotice
InspectionPanel
VerificationTag
ReleaseLatch
~~~

### Presentation Rule

> **Presentation components should mirror domain concepts without owning domain authority.**

Typed components improve discoverability, interface clarity, compile-time feedback, and source-to-output traceability.

Generated render code should remain clearly separated from editable source.

---

## 8. HTMX as the Interaction Adapter

HTMX is a strong candidate for the first interaction layer because Prime primarily needs:

- request dispatch;
- partial HTML replacement;
- form submission;
- targeted state updates;
- lightweight asynchronous interaction.

A Prime action may look conceptually like:

~~~text
SCAN BUTTON
   ↓
POST /packages/P-00491/scan
   ↓
SERVER EXECUTION
   ↓
HTML FRAGMENT RESPONSE
   ↓
REPLACE #package-panel
~~~

### Interaction Rule

> **Use the lightest interaction mechanism that preserves authoritative server state and operator clarity.**

HTMX is therefore an adapter, not doctrine.

If a future interaction layer preserves the same contract more effectively, it may replace HTMX.

---

## 9. Persistence Must Remain Replaceable

Persistence is infrastructure.

It must not define the domain.

The preferred shape is:

~~~text
PRIME DOMAIN
      │
      ▼
PackageStore interface
      │
      ├── PocketBase adapter
      ├── raw SQLite adapter
      └── future Postgres adapter
~~~

### Persistence Rule

> **Prime owns persistence contracts; storage engines implement them.**

This avoids backend lock-in.

---

## 10. PocketBase as a Candidate Adapter

PocketBase is a useful first integrated adapter because it can provide a compact bundle of:

- SQLite persistence;
- authentication;
- migrations;
- administrative tooling;
- realtime capabilities;
- Go extensibility.

However, PocketBase is not permanent infrastructure doctrine.

It should be treated as:

> **Candidate Storage / Auth / Realtime Adapter**

not:

> **Prime's canonical backend**

### Adapter Rule

> **Adopt PocketBase behind interfaces, never in place of interfaces.**

If Prime later outgrows PocketBase, the domain architecture should survive unchanged.

---

## 11. Raw SQLite Remains a Valid Lower Layer

The second studied pattern demonstrates the value of a direct SQLite implementation.

This remains useful for:

- prototypes;
- tests;
- local development;
- minimal deployments;
- deterministic fixtures;
- isolated demonstrations.

### Storage Ladder

~~~text
RAW SQLITE
maximum ownership
minimum abstraction

POCKETBASE
integrated backend conveniences

LARGER DATABASE / SERVICE
greater operational scale
~~~

The correct choice depends on package requirements, not prestige.

---

## 12. Dependency Injection and Deep Boundaries

The first studied pattern's explicit dependency injection strongly aligns with existing Prime doctrine.

A handler should depend on interfaces rather than instantiate hidden global dependencies.

Example:

~~~text
ScanHandler
  receives:
    LabelValidator
    Classifier
    RoutingPolicy
    PackageStore
~~~

This enables:

- isolated tests;
- mock implementations;
- adapter replacement;
- explicit dependency graphs;
- clearer architecture.

### Dependency Rule

> **Dependencies should be explicit enough to test, replace, and inspect.**

This supports the existing doctrine:

> **Retain authority over interfaces and system shape; delegate internal execution where verification is strong.**

---

## 13. Doctrine-to-Code Isomorphism

Prime should strive for structural correspondence between doctrine and code.

For example:

~~~text
DOCTRINE CONCEPT        SOFTWARE BOUNDARY

Package                 Package model/service
Shipping Label          Label model/service
Classifier              Classifier interface
Routing Policy          RoutingPolicy interface
Handler Registry        HandlerRegistry
Inspection              InspectionService
Verification Tag        Verification record/service
Release Authority       ReleaseAuthority
~~~

### Isomorphism Rule

> **Where practical, canonical doctrine concepts should have inspectable software boundaries rather than being buried in generic utility code.**

This improves traceability and reduces semantic drift.

---

## 14. Security Belongs in the Architecture

A lightweight web stack does not remove security requirements.

The control plane should support explicit middleware and security boundaries for matters such as:

- authentication;
- authorization;
- content-security policy;
- secure cookies;
- request validation;
- CSRF protection where applicable;
- output escaping;
- secret handling;
- audit logging.

Demonstration code from external tutorials must not be treated as production security guidance.

### Security Boundary Rule

> **Simplicity does not waive security controls.**

Security remains an independent implementation concern governed by policy and risk.

---

## 15. Source vs. Generated Artifacts

The first studied stack separates editable template source from generated Go output and editable style source from generated CSS output.

This strongly aligns with DraftDeck's production contract.

### Generated Artifact Rule

> **Generated files are outputs, not authoring surfaces.**

Editable source should remain authoritative.

Generated output should be reproducible.

This mirrors:

> **SOURCE → COMPILER / RENDERER → GENERATED OUTPUT**

---

## 16. Styling Is an Adapter

Tailwind may be useful for implementation speed.

It is not Prime's visual doctrine.

Prime already has its own visual grammar.

Therefore:

~~~text
PRIME VISUAL DOCTRINE
        ↓
owned design tokens / component rules
        ↓
CSS implementation
        ↓
Tailwind optional
~~~

### Styling Rule

> **The styling tool implements the visual system; it does not define the visual system.**

Owned CSS remains equally valid.

---

## 17. The Control Plane Surface

The first Prime Control Plane should make the doctrine operational through visible surfaces such as:

~~~text
MANIFESTS
PACKAGES
SHIPPING LABELS
SCANNER
CLASSIFICATION
ROUTING
HANDLER REGISTRY
HOLDS
INSPECTIONS
VERIFICATION TAGS
PROOF OF DELIVERY
RELEASE
~~~

Each surface should correspond to an inspectable server-side state transition.

### Control Surface Rule

> **Operator actions should correspond to explicit domain operations, not hidden client-side state mutations.**

---

## 18. Example Prime Request Flow

A package scan may execute as:

~~~text
1. operator scans package
2. browser sends POST /packages/{id}/scan
3. server loads authoritative package
4. label schema is validated
5. deterministic metadata is checked
6. classifier interprets semantic cargo
7. declared vs observed values are compared
8. routing policy evaluates the evidence
9. result is persisted
10. typed HTML component is rendered
11. browser replaces the affected fragment
12. operator sees the authoritative new state
~~~

The client does not independently decide the route.

The client displays the server's governed result.

---

## 19. Handler Capability Registry

The control plane should avoid coupling labels to named models.

A handler registry may track:

~~~text
HANDLER_ID
PROVIDER
CAPABILITIES
CONTEXT_CLASS
LATENCY_CLASS
COST_CLASS
AVAILABILITY
RISK_CLEARANCE
ENABLED
~~~

The classifier declares required capabilities.

The routing policy selects a compatible handler.

### Capability Routing Rule

> **Classifiers describe requirements. Routing policy matches those requirements to available handlers.**

This directly supports the Shipping Label doctrine.

---

## 20. Realtime Is Optional, Not Foundational

Some operator views may benefit from realtime updates.

Examples:

- package queue counts;
- manifest progress;
- held items;
- verification completion;
- handler availability.

Realtime transport may use:

- server-sent events;
- WebSockets;
- backend subscriptions;
- periodic refresh.

### Realtime Rule

> **Use realtime only where changing state materially benefits the operator.**

The architecture must remain correct without making realtime transport the source of truth.

---

## 21. Control Plane Reference Stack

The current preferred candidate is:

~~~text
PRIME CONTROL PLANE

DOMAIN
Go
│
├── Package service
├── Shipping Label service
├── Label Validator
├── Classifier interface
├── Routing Policy
├── Handler Registry
├── Inspection service
├── Verification service
└── Release Authority

HTTP ADAPTER
Chi
│
├── middleware
├── authentication
├── security policy
└── route handlers

PRESENTATION
templ
│
├── PackagePanel
├── ShippingLabel
├── ScanResult
├── ClassificationResult
├── RouteDecision
├── VerificationTag
└── ReleaseLatch

INTERACTION
HTMX
│
├── requests
├── fragment replacement
└── lightweight event updates

PERSISTENCE ADAPTER
PocketBase
│
├── SQLite
├── authentication
├── migrations
├── realtime
└── administrative tooling

STYLE ADAPTER
owned CSS or Tailwind
~~~

This is a reference architecture, not a mandatory implementation lock.

---

## 22. Architecture Selection Rules

A technology may enter the reference implementation when it:

- preserves Prime domain boundaries;
- is replaceable behind an interface;
- improves testability or observability;
- reduces unnecessary complexity;
- supports server authority;
- does not redefine the ontology;
- does not own release authority;
- has an inspectable migration path.

### Selection Rule

> **Choose infrastructure according to the control boundary it must preserve, not according to framework popularity.**

---

## 23. What Is Canonical vs. What Is Candidate

### Canonical

The following architectural principles are canonical:

- server-authoritative state;
- domain-first interfaces;
- replaceable adapters;
- typed or inspectable presentation boundaries;
- explicit dependency injection;
- generated/source separation;
- doctrine-to-code traceability;
- capability-based handler selection;
- security as an independent control concern.

### Candidate

The following are current implementation candidates:

- Go;
- Chi;
- templ;
- HTMX;
- PocketBase;
- Tailwind.

### Canonicality Rule

> **Implementation candidates may change without changing the doctrine they implement.**

---

## 24. Canonical Statements

> **Keep the system small enough to understand, but modular enough to govern.**

> **The UI displays governed state. It does not become the source of governed state.**

> **Prefer server-authoritative state transitions with HTML responses over duplicated client state when the workflow does not require a full client-side application model.**

> **Use the simplicity test from the minimal stack and the structural discipline from the more modular stack.**

> **The domain defines the interfaces. Frameworks and services implement them.**

> **The HTTP router is an adapter, not the application architecture.**

> **Presentation components should mirror domain concepts without owning domain authority.**

> **Use the lightest interaction mechanism that preserves authoritative server state and operator clarity.**

> **Prime owns persistence contracts; storage engines implement them.**

> **Adopt PocketBase behind interfaces, never in place of interfaces.**

> **Dependencies should be explicit enough to test, replace, and inspect.**

> **Where practical, canonical doctrine concepts should have inspectable software boundaries rather than being buried in generic utility code.**

> **Simplicity does not waive security controls.**

> **Generated files are outputs, not authoring surfaces.**

> **The styling tool implements the visual system; it does not define the visual system.**

> **Operator actions should correspond to explicit domain operations, not hidden client-side state mutations.**

> **Classifiers describe requirements. Routing policy matches those requirements to available handlers.**

> **Use realtime only where changing state materially benefits the operator.**

> **Choose infrastructure according to the control boundary it must preserve, not according to framework popularity.**

> **Implementation candidates may change without changing the doctrine they implement.**

---

## 25. Source and Provenance

This doctrine was synthesized from:

- existing DraftDeck production, logistics, Prime Process, shipping-label, orchestration, handoff, and release doctrine;
- a user-supplied transcript describing a Go + Chi + templ + HTMX + Tailwind application structure with explicit interfaces, dependency injection, middleware, generated templates, security headers, and replaceable storage;
- a second user-supplied transcript describing a minimal Go + Gin + HTML templates + HTMX + SQLite architecture and introducing PocketBase as an optional integrated backend;
- the comparative architecture analysis performed after both transcripts were available.

The external stacks are treated as implementation references.

This document is an original Prime Process synthesis.

No named framework, database, template engine, or interaction library is granted canonical authority over the Prime domain.
