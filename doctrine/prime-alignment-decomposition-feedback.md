# Prime Alignment, Decomposition & Feedback Doctrine

**Status:** Candidate Canonical Doctrine  
**Framework:** Logistics Framework → Prime Process  
**Repository Role:** Operating doctrine / training doctrine / package-design and feedback architecture reference  
**Purpose:** Define how ambiguous work becomes a bounded, routable, testable, parallelizable manifest through human alignment, destination definition, dependency-aware decomposition, vertical slicing, structured feedback loops, and review.

---

## 1. Doctrine Upgrade

Prime Process already establishes:

> **PRIME = Package → Route → Inspect → Move → Establish Delivery**

The handoff doctrine adds:

> **Context should be routed, not accumulated.**

This document adds a further operating layer:

> **Alignment precedes packaging.**

A system should not begin by converting a vague request directly into implementation.

It should first establish enough shared understanding to define the destination, identify unresolved assumptions, expose dependencies, and decide which parts require human judgment before the work is decomposed into packages.

The source transcript studied for this doctrine presents a complete workflow for moving from an ambiguous idea to human-aligned planning, dependency-aware work decomposition, AFK-capable implementation, automated review, human QA, and iteration.

Prime Process adopts the principles, not the speaker's specific tools or brands.

---

## 2. Human Attention Belongs Upstream

Not all work should receive the same level of automation.

The transcript distinguishes between:

- **human-in-the-loop work**;
- **AFK-capable work**.

That distinction is useful because ambiguity and judgment are not evenly distributed across a workflow.

Human attention is most valuable where there is:

- unclear intent;
- competing objectives;
- scope ambiguity;
- architectural judgment;
- taste;
- policy or authority;
- irreversible decisions;
- high consequence;
- unresolved trade-offs.

Automation becomes safer as the package becomes more bounded.

~~~text
HIGH AMBIGUITY
HIGH JUDGMENT
HIGH AUTHORITY
        ↓
HUMAN-IN-THE-LOOP

BOUNDED PACKAGE
DECLARED ACCEPTANCE
STRONG FEEDBACK LOOPS
        ↓
AFK-CAPABLE
~~~

### Human Attention Rule

> **Human attention should be concentrated where ambiguity, judgment, taste, scope, and authority are highest. Automation should increase as the package becomes more bounded.**

---

## 3. Alignment Before Packaging

The transcript's "grilling" process is best understood as an alignment protocol.

Its goal is not merely to ask many questions.

Its purpose is to reduce hidden disagreement between the human and the system before committing to a plan.

A weak workflow looks like:

~~~text
RAW REQUEST
   ↓
PLAN
   ↓
IMPLEMENT
~~~

A stronger workflow looks like:

~~~text
RAW REQUEST
   ↓
QUESTIONING
   ↓
ASSUMPTION EXPOSURE
   ↓
DEPENDENCY RESOLUTION
   ↓
SHARED DESIGN CONCEPT
   ↓
PACKAGE READY
~~~

### Alignment Rule

> **A package is not ready to route until the operator and system share the same intended destination well enough to define acceptance.**

This does not require certainty.

It requires sufficient agreement about what the work is trying to establish.

---

## 4. Destination and Journey Are Separate Artifacts

The transcript distinguishes two essential things:

1. a description of the destination;
2. a description of the journey.

Prime Process formalizes these separately.

### Destination Artifact

The destination artifact answers:

- What problem are we solving?
- For whom?
- What should exist when we are done?
- What behavior matters?
- What is explicitly out of scope?
- What counts as acceptable delivery?

A PRD is one possible implementation.

### Journey Artifact

The journey artifact answers:

- What packages must move?
- What depends on what?
- Which packages can move in parallel?
- Which packages are blocked?
- Which packages require human involvement?
- What route should each package take?

### Destination/Journey Rule

> **The destination defines done. The journey defines how packages move toward it.**

The route must not become confused with the objective.

---

## 5. From Sequential Plan to Dependency Graph

A numbered phase list often hides the actual dependency structure.

Prime Process should prefer a dependency-aware task graph where appropriate.

~~~text
MANIFEST
   ↓
DEPENDENCY GRAPH
   ↓
READY PACKAGES
   ↓
PARALLEL LANES
   ↓
BLOCKED PACKAGES WAIT
   ↓
CONSOLIDATION
~~~

This is more useful than assuming every task must happen in one linear sequence.

### Parallelism Rule

> **Parallelism should emerge from dependency independence, not from the desire to run more agents.**

The correct question is not:

> How many agents can we run?

It is:

> Which packages are truly independent enough to move at the same time?

---

## 6. Independently Grabbable Packages

A good package should be independently actionable whenever possible.

That means the package has:

- a clear objective;
- bounded scope;
- declared dependencies;
- expected output;
- acceptance conditions;
- enough context to begin;
- no hidden reliance on unresolved sibling work.

This allows a package to be assigned to one handler without requiring the entire original planning session.

### Grabbability Rule

> **A package is independently grabbable when a qualified handler can begin it without reopening the parent design conversation.**

This is a major precondition for safe parallelism.

---

## 7. Vertical Slices Over Horizontal Layers

The transcript identifies a common failure mode: agents often decompose work by technical layer.

For example:

~~~text
PHASE 1
database

PHASE 2
API

PHASE 3
frontend
~~~

That delays integrated feedback.

Prime Process prefers thin vertical packages that cross the minimum necessary layers to create an observable outcome.

~~~text
VERTICAL PACKAGE
minimal schema
+ minimal logic
+ minimal interface
+ observable behavior
~~~

The goal is not architectural neatness inside the task list.

The goal is early evidence that the system works across the path that matters.

### Vertical Slice Rule

> **Design packages around verifiable outcomes, not architectural layers.**

A package should expose enough end-to-end behavior to produce useful feedback as early as practical.

---

## 8. Feedback Early, Not Late

Horizontal decomposition often postpones feedback until multiple layers are complete.

Vertical decomposition creates earlier checkpoints.

Prime Process values early feedback because it reduces the amount of unverified work that can accumulate.

~~~text
SMALL VERTICAL SLICE
        ↓
OBSERVABLE RESULT
        ↓
INSPECTION
        ↓
ADJUST
        ↓
NEXT SLICE
~~~

### Feedback Timing Rule

> **Prefer package boundaries that create useful feedback before large amounts of dependent work accumulate.**

---

## 9. Instrument the Route Before Movement

The transcript's use of test-driven development supports a broader logistics principle.

The important idea is not that every task must use software TDD.

The important idea is that the system should define observable success and failure before high-cost execution.

Examples:

- failing test before implementation;
- validation schema before transformation;
- visual QA rubric before rendering;
- claim criteria before research synthesis;
- benchmark before optimization;
- acceptance criteria before deployment.

### Instrumentation Rule

> **Instrument the route before sending the package.**

A package should know what evidence will indicate:

- success;
- failure;
- blocked state;
- acceptable degradation;
- need for escalation.

---

## 10. Feedback Quality Sets the Practical Ceiling

The transcript repeatedly emphasizes that agent quality depends on the quality of the feedback loops around it.

Prime Process adopts that as a system principle.

A capable model operating without useful feedback may perform worse than a weaker model operating inside a well-instrumented environment.

Useful feedback can include:

- tests;
- type checks;
- runtime errors;
- lints;
- schema validation;
- visual comparison;
- source comparison;
- acceptance checks;
- code review;
- user feedback;
- human QA.

### Feedback Ceiling Rule

> **The reliability of movement is bounded by the quality of inspection signals available during movement.**

This means improving the feedback system may be more valuable than changing the model.

---

## 11. Implementation and Review Should Be Separable Packages

The transcript makes a useful point: the same long context that implemented something may be a poor environment for reviewing it.

Prime Process treats implementation and review as different packages.

~~~text
IMPLEMENTATION PACKAGE
        ↓
DELIVERED ARTIFACT
        ↓
NEW REVIEW PACKAGE
        ↓
INDEPENDENT INSPECTION
~~~

This creates cleaner separation between:

- builder assumptions;
- reviewer criteria;
- implementation history;
- acceptance evidence.

### Independent Review Rule

> **Review should be context-independent from implementation whenever practical.**

The reviewer should receive the artifact, relevant standards, acceptance conditions, and evidence — not necessarily the entire implementation conversation.

---

## 12. Push vs. Pull Context

The transcript offers a valuable distinction:

### PUSH

Information automatically injected into the active context.

Use push for constraints that must govern every relevant decision.

Examples:

- safety requirements;
- coding standards for review;
- release criteria;
- ontology prohibitions;
- hard interface contracts.

### PULL

Information available on demand.

Use pull for reference material that is only conditionally relevant.

Examples:

- specialized skills;
- optional style guides;
- library documentation;
- narrow implementation patterns;
- historical examples.

### Push/Pull Rule

> **Push constraints that must always govern the decision. Pull reference material that is only conditionally relevant.**

This reduces context waste without weakening mandatory controls.

---

## 13. Human Review Should Follow Risk

The transcript contains one workflow preference that Prime Process should not universalize: not reading a generated PRD because summarization is considered reliable.

Prime Process instead uses proportional review.

### Review Proportionality Rule

> **Review effort should be proportional to risk, novelty, consequence, and reversibility.**

A low-risk internal summary may need minimal review.

A high-impact specification may require line-by-line review.

The doctrine governs the decision, not one personal preference.

---

## 14. Deep Boundaries Improve Agent Reliability

The transcript connects software architecture to agent performance through the idea of deep modules.

A deep module:

- exposes a small interface;
- hides substantial internal complexity;
- presents a clearer testing boundary;
- reduces dependency sprawl.

Prime Process generalizes this:

> **Good boundaries improve both human comprehension and machine reliability.**

This applies beyond software.

A well-designed package, service, process, or adapter should expose:

- a clear interface;
- expected behavior;
- declared dependencies;
- acceptance conditions;
- bounded internal complexity.

---

## 15. Retain the Shape; Delegate the Interior

The transcript proposes a useful human-scaling strategy:

- retain understanding of the major system shapes;
- retain control over interfaces;
- delegate internal implementation where verification is strong.

This creates a middle ground between:

- reviewing every low-level detail;
- surrendering architecture to the agent.

### Shape Authority Rule

> **Retain authority over interfaces and system shape; delegate internal execution where verification is strong.**

The human should understand:

- what each major component does;
- how components connect;
- what contracts govern them;
- what evidence establishes acceptable behavior.

The human does not necessarily need to author every internal line.

---

## 16. Stale Context Is Active Contamination

The transcript raises a major documentation hazard: old PRDs or planning artifacts may remain in the repository after the implementation has changed substantially.

In an AI-assisted workflow, stale documentation is not passive clutter.

It may be retrieved and treated as current truth.

Prime Process therefore distinguishes:

### ACTIVE CANON

Current authoritative material.

### CLOSED RECORD

Historical material retained for provenance, clearly marked complete or superseded.

### TRANSIT ARTIFACT

Temporary routing material.

### STALE ARTIFACT

Material that no longer represents the current system and must not be treated as authority.

### Staleness Rule

> **Stale context is active contamination.**

Historical artifacts must have visible state so they cannot silently masquerade as current authority.

---

## 17. QA Generates New Packages

QA should not be treated as the final stop in a linear pipeline.

QA produces findings.

Those findings become new packages.

~~~text
IMPLEMENT
   ↓
QA
   ↓
FINDINGS
   ↓
NEW PACKAGES
   ↓
ROUTE BACK INTO MANIFEST
~~~

### QA Rule

> **QA is not merely a gate; it is a source of new packages.**

This keeps the system iterative without collapsing back into an unbounded conversation.

---

## 18. The Human Day Shift / AFK Night Shift Pattern

The transcript uses a useful operational framing:

- humans prepare and align the work;
- automation executes bounded packages later.

Prime Process can use the underlying structure without preserving the exact metaphor.

~~~text
HUMAN PREPARATION
alignment
destination
scope
dependencies
package design
acceptance conditions

        ↓

AUTOMATED EXECUTION
bounded implementation
tests
routine review
artifact production

        ↓

HUMAN RETURN
QA
taste
architecture
release
new findings
~~~

### Delegation Rule

> **Automate execution only after the human has made the package governable.**

---

## 19. Automated Review Before Human QA

The transcript recommends inexpensive automated review before the human spends time on manual QA.

Prime Process supports this layered inspection model.

~~~text
IMPLEMENT
   ↓
AUTOMATED REVIEW
   ↓
AUTOMATED CHECKS
   ↓
HUMAN QA
   ↓
RELEASE DECISION
~~~

Automated review can catch:

- obvious defects;
- standards violations;
- missing tests;
- type errors;
- schema failures;
- inconsistencies.

Human QA remains important for:

- taste;
- product fit;
- visual quality;
- architecture;
- subtle behavior;
- authority;
- release.

### Inspection Layering Rule

> **Use cheap automated inspection before expensive human inspection, but do not confuse the two.**

---

## 20. A Prime-Native End-to-End Flow

The transcript's full workflow can be translated into Prime Process as:

~~~text
IDEA
  ↓
ALIGN
  ↓
DEFINE DESTINATION
  ↓
PACKAGE
  ↓
BUILD DEPENDENCY GRAPH
  ↓
CREATE VERTICAL SLICES
  ↓
DECLARE ACCEPTANCE SIGNALS
  ↓
ROUTE READY PACKAGES
  ↓
MOVE / IMPLEMENT
  ↓
AUTOMATED REVIEW
  ↓
HUMAN QA
  ↓
GENERATE NEW PACKAGES
  ↓
ITERATE
  ↓
ESTABLISH DELIVERY
~~~

This is not a one-way pipeline.

The system may move backward whenever evidence changes the plan.

---

## 21. PRIME Mapping

### P — PACKAGE

Before packaging:

- align;
- expose assumptions;
- define destination;
- identify out-of-scope work.

Then package work as independently grabbable vertical slices.

### R — ROUTE

Build the dependency graph.

Route only ready packages.

Parallelize only independent packages.

### I — INSPECT

Define acceptance conditions before movement.

Use tests, checks, standards, automated review, and human QA.

### M — MOVE

Execute bounded work.

Allow AFK execution where the package is sufficiently governed.

### E — ESTABLISH DELIVERY

Require observable behavior, inspection evidence, destination alignment, and proper release.

QA findings may create new packages before delivery is established.

---

## 22. Canonical Rules Added by This Doctrine

> **Alignment precedes packaging.**

> **A package is not ready to route until the operator and system share the same intended destination well enough to define acceptance.**

> **The destination defines done. The journey defines how packages move toward it.**

> **Parallelism should emerge from dependency independence, not from the desire to run more agents.**

> **A package is independently grabbable when a qualified handler can begin it without reopening the parent design conversation.**

> **Design packages around verifiable outcomes, not architectural layers.**

> **Prefer package boundaries that create useful feedback before large amounts of dependent work accumulate.**

> **Instrument the route before sending the package.**

> **The reliability of movement is bounded by the quality of inspection signals available during movement.**

> **Review should be context-independent from implementation whenever practical.**

> **Push constraints that must always govern the decision. Pull reference material that is only conditionally relevant.**

> **Review effort should be proportional to risk, novelty, consequence, and reversibility.**

> **Good boundaries improve both human comprehension and machine reliability.**

> **Retain authority over interfaces and system shape; delegate internal execution where verification is strong.**

> **Stale context is active contamination.**

> **QA is not merely a gate; it is a source of new packages.**

> **Automate execution only after the human has made the package governable.**

> **Use cheap automated inspection before expensive human inspection, but do not confuse the two.**

---

## 23. Source and Provenance

This doctrine was synthesized from:

- existing DraftDeck Logistics Framework doctrine;
- existing Prime Process doctrine;
- existing Prime Process Orchestration doctrine;
- existing Prime Handoff & Context Routing doctrine;
- a user-supplied transcript of a long-form workshop covering alignment, context discipline, PRDs, dependency-aware task decomposition, vertical slicing, AFK execution, automated review, TDD, software architecture, deep modules, human QA, push/pull context, parallelization, and iterative issue generation.

The transcript is treated as a workflow reference.

This document is an original Prime Process synthesis and does not adopt any speaker-specific product, model, vendor, or tool as canonical.
