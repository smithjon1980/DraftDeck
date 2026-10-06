# Prime Process Orchestration Doctrine

**Status:** Candidate Canonical Doctrine  
**Framework:** Logistics Framework → Prime Process  
**Repository Role:** Operating architecture / training doctrine / orchestration reference  
**Purpose:** Define how Prime Process becomes an executable work system by combining bounded work packages, routing, inspection, orchestration, delivery verification, and reusable learning.

---

## 1. Doctrine Upgrade

Prime Process began as a logistics model:

> **PRIME = Package → Route → Inspect → Move → Establish Delivery**

This document extends PRIME from a teaching metaphor into an executable operating architecture.

The upgrade is based on a simple observation:

> **Modern AI systems become more useful when repeatable work is converted from free-form prompting into bounded, inspectable, reusable workflows.**

The external reference studied for this upgrade is the open-source **ECC** repository by Affaan Mustafa (affaan-m/ECC). ECC is MIT licensed and demonstrates a system of planning, specialized skills, orchestration, test-driven development, review, verification, persistent artifacts, and reusable learning.

ECC is **not** adopted as the Prime Process ontology. It is used as an implementation reference.

> **We study ECC's mechanics. Prime Process remains our doctrine.**

---

## 2. The Core Architectural Insight

The most important lesson from the ECC workflow is not "run many agents."

The important lesson is to move from:

~~~text
IDEA
  ↓
PROMPT
  ↓
OUTPUT
~~~

to:

~~~text
CONTEXT / KNOWLEDGE
        ↓
IDEA
        ↓
RESEARCH
        ↓
SPECIFICATION / PRD
        ↓
PLAN
        ↓
BOUNDED WORK PACKAGES
        ↓
ROUTE TO SPECIALIZED SKILLS / AGENTS
        ↓
TEST-FIRST OR CONTROLLED EXECUTION
        ↓
REVIEW / VERIFY
        ↓
SHIP
        ↓
OUTSIDE FEEDBACK
        ↓
ITERATE
        ↓
CAPTURE REUSABLE LEARNING
~~~

That sequence matters because rapid execution changes the location of the bottleneck.

When implementation becomes cheap and fast, the cost of a bad mission increases because a bad idea can now be built, polished, and distributed quickly.

Therefore:

> **Speed of execution increases the value of restraint before execution.**

The upstream questions become more important:

- What are we trying to accomplish?
- Who is this for?
- What evidence supports the need?
- What assumptions remain unproven?
- What exactly is in scope?
- What counts as successful delivery?
- What must be verified before release?

Prime Process treats these as logistics questions, not prompt-writing questions.

---

## 3. PRIME as an Executable Workflow

### P — PACKAGE

Convert an idea, request, or problem into a bounded work package.

A package is not "something the agent should work on." It is a defined operational unit with identity, contents, requirements, and acceptance criteria.

A mature package should be able to carry fields such as:

~~~text
PACKAGE_ID
OBJECTIVE
SOURCE_CONTEXT
REQUIREMENTS
CONSTRAINTS
ACCEPTANCE_CRITERIA
DEPENDENCIES
RISK_CLASS
DESTINATION
HANDLING_REQUIREMENTS
OWNER
STATUS
~~~

A PRD, implementation plan, research brief, defect report, slide specification, or dataset evaluation may all function as work packages.

### Package Rule

> **Undefined cargo cannot be routed reliably.**

A free-form request is not yet a package merely because it is understandable.

The packaging step creates the stable artifact that downstream workers can inspect without relying on conversational memory.

---

### R — ROUTE

Assign the package to the appropriate handling path.

Routing determines:

- which workflow should handle the package;
- which skill or specialist is appropriate;
- whether the work should remain human-led;
- whether parallel handling is useful;
- whether the package needs additional inspection before execution;
- whether the work should be held rather than moved.

In the ECC reference architecture, routing may target planning, research, TDD, security review, market research, frontend work, backend work, documentation, media generation, deployment, or specialized domain skills.

Prime Process generalizes that behavior.

~~~text
PACKAGE
   ↓
CLASSIFY
   ↓
ROUTE
   ├── RESEARCH LANE
   ├── BUILD LANE
   ├── DATA LANE
   ├── REVIEW LANE
   ├── MEDIA LANE
   ├── DELIVERY LANE
   └── HUMAN HOLD / ESCALATION
~~~

### Routing Rule

> **Route according to the job, not according to prestige.**

The most capable model, largest agent system, or most expensive service is not automatically the correct route.

---

### I — INSPECT

Inspect the package before and during movement.

Inspection prevents fluent execution from becoming false confidence.

Inspection may include:

- requirements review;
- provenance review;
- assumption labeling;
- risk assessment;
- test creation;
- expected-output definition;
- code review;
- visual QA;
- security review;
- evidence checks;
- diff review;
- source comparison;
- acceptance testing.

The ECC reference is especially valuable here because it treats testing and review as structural parts of work rather than optional cleanup.

ECC contains planning gates and TDD-oriented workflows where tests can be written before implementation and used to constrain subsequent execution.

Prime Process translates this into a larger rule:

> **Movement never substitutes for inspection.**

A package that moved quickly through many systems is not necessarily a valid package.

---

### M — MOVE

Execute the route.

Movement is the stage where tools, models, agents, scripts, people, and infrastructure perform the actual work.

Movement may be:

- sequential;
- parallel;
- multi-stage;
- branch-based;
- human-assisted;
- model-assisted;
- fully automated within declared limits.

The ECC reference demonstrates orchestration where multiple workers may execute in separate panes or worktrees while a higher-level orchestrator monitors progress.

This is useful because Prime Process does not require the human operator to watch every low-level action.

The correct model is closer to a logistics control surface:

~~~text
                 ┌── WORKER A
PACKAGE → SORT ──┼── WORKER B
                 ├── WORKER C
                 └── WORKER D
                      ↓
                 CONSOLIDATE
                      ↓
                    REVIEW
~~~

### Movement Rule

> **Use only as much infrastructure as the shipment requires.**

Parallelism is not success by itself.

The purpose of orchestration is controlled throughput, not spectacle.

---

### E — ESTABLISH DELIVERY

Determine whether delivery is actually complete.

This is where Prime Process intentionally goes beyond a narrow software-development definition of done.

These may all be useful signals:

~~~text
TESTS PASS
BUILD SUCCEEDS
COMMIT EXISTS
PR CREATED
DEPLOYMENT COMPLETES
~~~

But Prime Process does not equate those signals with established delivery.

The stronger question is:

> **Did the correct package reach the correct receiver, in an acceptable state, with evidence and proper release authority?**

Delivery may require:

- artifact exists;
- required tests pass;
- review passes;
- source and output remain aligned;
- destination is correct;
- acceptance criteria are satisfied;
- required human approval is recorded;
- proof of delivery exists;
- unresolved items remain explicitly unresolved;
- user/customer feedback is captured where relevant.

### Delivery Rule

> **Completion is a verified state, not an activity count.**

And:

> **TEST PASS ≠ DELIVERY ESTABLISHED**

---

## 4. The Manifest Model

Prime Process should prefer persistent artifacts over conversational memory.

A package manifest may contain:

| Field | Function |
|---|---|
| PACKAGE_ID | Stable identity |
| OBJECTIVE | Intended outcome |
| SOURCE_CONTEXT | Inputs and grounding |
| REQUIREMENTS | Required contents or behavior |
| CONSTRAINTS | Boundaries that must not be crossed |
| ACCEPTANCE_CRITERIA | Conditions for successful delivery |
| DEPENDENCIES | Required upstream packages |
| RISK_CLASS | Handling / verification level |
| ROUTE | Assigned workflow |
| HANDLER | Current person, skill, model, or agent |
| STATUS | Current package state |
| POD | Proof-of-delivery reference |

This extends the existing Prime Process distinction:

> **The block is the unit of operational commitment; the package is the unit of accountability.**

A workflow block may contain many packages.

A successful block does not excuse a failed package.

---

## 5. Planning Before Movement

One of the strongest ECC patterns is the separation between requirements and implementation planning.

ECC documentation distinguishes:

- PRD / specification work: **why and what**;
- implementation planning: **how**.

This separation is valuable because it prevents the mission from collapsing into execution details too early.

Prime Process therefore recognizes at least three planning layers:

~~~text
MISSION
What outcome are we trying to establish?

        ↓

PACKAGE
What bounded work must exist to advance the mission?

        ↓

ROUTE PLAN
How will this package move through the network?
~~~

This creates a stable chain:

~~~text
MISSION
  ↓
PACKAGE MANIFEST
  ↓
ROUTE PLAN
  ↓
EXECUTION
  ↓
INSPECTION
  ↓
DELIVERY
~~~

A package must not enter movement merely because a system can act on it.

---

## 6. Test-Driven Handling

ECC's use of test-driven development provides a useful general principle:

> **Define observable failure and success before asking the system to produce the final result.**

In software this may mean writing failing tests first.

In other domains the equivalent may be:

- validation checklist before data transformation;
- visual QA criteria before slide generation;
- evidence criteria before research synthesis;
- schema before extraction;
- rubric before evaluation;
- acceptance test before deployment;
- claim comparator before adjudication.

Prime Process generalizes TDD into:

> **Acceptance conditions should exist before high-cost movement begins.**

This does not mean every task requires literal software tests.

It means the package should know what "good" means before execution attempts to satisfy it.

---

## 7. The Orchestrator Is a Control Surface

The ECC demonstration shows an orchestrator monitoring multiple worker panes rather than requiring the user to manually follow every worker.

That is a useful pattern.

The orchestrator should answer questions such as:

- What packages are active?
- Which handler owns each package?
- Which packages are blocked?
- Which tests or inspections have failed?
- Which work is ready for consolidation?
- Which package needs human review?
- Which package has established delivery?
- Which package requires re-routing?

The orchestrator is not final authority.

It is a network control surface.

~~~text
ORCHESTRATOR
   │
   ├── observes
   ├── routes
   ├── schedules
   ├── reports
   ├── holds
   └── escalates

HUMAN AUTHORITY
   │
   └── releases where required
~~~

This preserves the Logistics Framework semantic firewall:

> **Systems may classify, account, route, hold, compare, and report. Human authority retains release where the process requires human authorization.**

---

## 8. Parallel Work Without Context Collapse

Running multiple agents is only useful when the work has been packaged correctly.

Without bounded packages, parallel agents multiply ambiguity.

A Prime-native orchestration system should therefore prefer:

~~~text
ONE MANIFEST
    ↓
SEVERABLE PACKAGES
    ↓
DECLARED DEPENDENCIES
    ↓
PARALLEL ROUTES
    ↓
CONTROLLED CONSOLIDATION
~~~

Parallelism is appropriate only when packages can be independently handled without corrupting each other's assumptions or outputs.

### Parallelism Rule

> **Do not create more lanes than the manifest can govern.**

---

## 9. External Feedback Is Part of Delivery

The ECC demonstration includes a product being built rapidly and then presented to real people for feedback.

That matters.

Modern tooling can reduce time-to-prototype dramatically, but prototype creation is not the same as product validation.

Therefore Prime Process distinguishes:

~~~text
ARTIFACT DELIVERY
        ↓
USER / MARKET CONTACT
        ↓
FEEDBACK PACKAGE
        ↓
RE-INSPECTION
        ↓
ITERATION
~~~

This protects the operator from a closed loop where the human and agents repeatedly validate one another without outside evidence.

### Feedback Rule

> **Agent agreement is not market evidence.**

And:

> **Internal completion does not establish external usefulness.**

---

## 10. Continuous Learning as Network Improvement

ECC contains continuous-learning machinery intended to capture observations from completed work and convert repeated useful patterns into reusable knowledge.

Prime Process should adopt the principle, not blindly inherit the implementation.

A Prime-native learning cycle should look like:

~~~text
DELIVERY
   ↓
AUDIT
   ↓
OBSERVATION
   ↓
PATTERN
   ↓
CONFIDENCE
   ↓
REUSABLE RULE / SKILL / TEMPLATE
   ↓
FUTURE ROUTING IMPROVEMENT
~~~

This transforms completed deliveries into better future logistics.

The system should not "learn" simply because something happened once.

Reusable patterns should require evidence across repeated deliveries or deliberate human promotion.

### Learning Rule

> **A repeated success may become doctrine only after it survives inspection.**

---

## 11. ECC as an Upstream Reference, Not a Dependency Identity

The official ECC repository is:

~~~text
affaan-m/ECC
~~~

It is MIT licensed.

That license permits reuse, modification, redistribution, merging, publication, sublicensing, and commercial use subject to the license conditions.

However, Prime Process should not vendor the entire ECC repository into DraftDeck by default.

Reasons:

1. **Ontology integrity** — DraftDeck has its own canonical Logistics Framework and Prime Process vocabulary.
2. **Dependency control** — ECC contains a broad surface of agents, skills, hooks, commands, adapters, runtime assumptions, and integrations.
3. **Security surface** — Hooks, shell commands, credentials, MCP configuration, external APIs, and agent permissions require deliberate review.
4. **Maintenance ownership** — Vendoring the whole project would make DraftDeck responsible for tracking upstream changes that may not matter to its mission.
5. **Training clarity** — The framework should teach stable principles rather than make one external project the curriculum.

Therefore:

> **ECC should be treated as an upstream pattern library and research specimen, not as Prime Process itself.**

---

## 12. Recommended Adoption Model

Use a three-layer relationship:

~~~text
ECC
External reference implementation
        ↓
PATTERN STUDY
Identify useful mechanisms
        ↓
PRIME-NATIVE IMPLEMENTATION
Rewrite under Logistics Framework doctrine
~~~

The highest-value ECC patterns to study first are:

1. planning / PRD separation;
2. test-driven workflow;
3. orchestrator + worker pattern;
4. continuous-learning / pattern extraction;
5. skill chaining.

Prime Process does not need hundreds of skills to begin.

A minimal executable Prime stack could begin with:

~~~text
prime-package
prime-route
prime-inspect
prime-move
prime-delivery
~~~

These skills can later be expanded into specialized handlers.

---

## 13. Skill Chaining Under PRIME

A chained workflow should preserve package identity across every handoff.

Example:

~~~text
PACKAGE: Create a production-ready training lesson

prime-package
   ↓
research-handler
   ↓
curriculum-planner
   ↓
draft-handler
   ↓
fact-inspector
   ↓
visual-spec-handler
   ↓
release-inspector
   ↓
prime-delivery
~~~

The orchestration layer should not treat those as isolated prompts.

They are stages in one shipment.

Every stage should know:

- package identity;
- current version;
- prior handler;
- inputs received;
- changes made;
- unresolved issues;
- next destination.

---

## 14. Prime Process and DraftDeck

DraftDeck is a strong early application of this doctrine because it already has:

- canonical source;
- generated output;
- doctrine;
- adapters;
- verification levels;
- release QA;
- GitHub as source of truth;
- branch / PR workflows;
- semantic CI guards.

This can be expressed through PRIME:

~~~text
PACKAGE
Slide/deck specification

ROUTE
DraftDeck skill + renderer + target adapter

INSPECT
Reference fidelity + source contract + visual QA + adapter verification

MOVE
Build HTML/CSS/SVG → import → regenerate → revise

ESTABLISH DELIVERY
Verified editable artifact + preserved composition + release evidence
~~~

The same structure can later govern research, coding, data, media, and training workflows.

---

## 15. Training Implication

Prime Process can now serve two roles at once.

### Instructional doctrine

It teaches a learner how to think about work:

~~~text
Package it.
Route it.
Inspect it.
Move it.
Establish delivery.
~~~

### Executable architecture

It defines how software should actually organize work:

~~~text
manifest
→ router
→ inspector
→ handlers / agents
→ verification
→ proof of delivery
→ audit
→ reusable learning
~~~

This is the major framework upgrade.

The curriculum no longer has to stop at analogy.

The learner can eventually build the system they were taught to think with.

---

## 16. Canonical Statements

> **PRIME = Package → Route → Inspect → Move → Establish Delivery.**

> **The block is the unit of operational commitment; the package is the unit of accountability.**

> **Speed of execution increases the value of restraint before execution.**

> **Movement never substitutes for inspection.**

> **Route according to the job, not according to prestige.**

> **TEST PASS ≠ DELIVERY ESTABLISHED.**

> **Agent agreement is not market evidence.**

> **The orchestrator is a control surface, not final authority.**

> **Do not create more lanes than the manifest can govern.**

> **A repeated success may become doctrine only after it survives inspection.**

> **We study ECC's mechanics. Prime Process remains our doctrine.**

> **The learner does not become a bigger vehicle. The learner becomes capable of operating a larger logistics network.**

> **You are not learning how to carry one AI package. You are learning how to operate a logistics network for information.**

---

## 17. Source and Provenance

This doctrine was developed from:

- the Prime Process doctrine already established in DraftDeck;
- a user-supplied transcript of an ECC demonstration covering orchestration, planning, test-driven development, skill chaining, market feedback, and reusable workflows;
- direct inspection of the official public ECC repository;
- ECC's MIT license;
- ECC documentation covering planning, orchestration, TDD, continuous learning, Codex support, and multi-harness installation.

External upstream reference:

**ECC — affaan-m/ECC**  
GitHub: https://github.com/affaan-m/ECC  
License: MIT

This document is an original Prime Process doctrine synthesis. ECC terminology and implementation details are treated as reference material, not as DraftDeck's canonical ontology.
