# Prime Handoff & Context-Routing Doctrine

**Status:** Candidate Canonical Doctrine  
**Framework:** Logistics Framework → Prime Process  
**Repository Role:** Operating doctrine / training doctrine / context-management reference  
**Purpose:** Define how context, out-of-scope work, temporary routing artifacts, prototypes, and return paths are packaged and moved between sessions or handlers without contaminating the parent workflow.

---

## 1. Doctrine Upgrade

Prime Process already establishes:

> **PRIME = Package → Route → Inspect → Move → Establish Delivery**

This document extends that doctrine with a specific operational primitive:

> **Context should be routed, not accumulated.**

The triggering insight came from a user-supplied transcript describing a handoff skill for AI coding sessions. The speaker's recurring problem was simple: useful work often appears inside a session that does not belong to that session's current scope.

Instead of expanding the original session until its context becomes diluted, the speaker packages the relevant slice of context into a small Markdown handoff document, routes it to another session, and allows both workstreams to proceed independently.

That pattern maps directly into Prime Process.

---

## 2. The Core Problem: Context Accumulation

Long-running AI sessions accumulate:

- user instructions;
- tool calls;
- file reads;
- edits;
- errors;
- retries;
- side discussions;
- speculative branches;
- debugging history;
- resolved questions;
- unresolved questions.

A larger context window does not mean that every token remains equally useful.

The operational risk is not merely a hard context limit.

The larger risk is **context dilution**: the active task must compete with increasingly irrelevant history.

Prime Process therefore rejects the assumption that more accumulated context is automatically better.

> **Context should be curated, not merely accumulated.**

---

## 3. Compaction and Handoff Are Different Operations

The transcript distinguishes two useful operations.

### COMPACT

Compaction preserves the same task while reducing accumulated context.

~~~text
SAME PACKAGE
SAME OBJECTIVE
SAME ROUTE
SAME WORKSTREAM
REDUCED CONTEXT PAYLOAD
~~~

Compaction is appropriate when the work should continue as one long-running job.

### HANDOFF

Handoff creates a new bounded task from a relevant slice of the current context.

~~~text
NEW PACKAGE
NEW OBJECTIVE
NEW ROUTE
NEW WORKSTREAM
PARENT RELATIONSHIP PRESERVED
~~~

A handoff is not merely a compressed conversation.

It is a routing event.

### Canonical Distinction

> **COMPACT preserves one package. HANDOFF creates another.**

---

## 4. Context-Preserving Task Severance

The strongest pattern in the transcript is **task severance**.

A session encounters work that is valid but out of scope.

Instead of contaminating the original task, the operator severs that work into a new package.

~~~text
PRIMARY SESSION
     │
     │ discovers out-of-scope work
     ↓
SEVER TASK
     ↓
CREATE HANDOFF PACKAGE
     ↓
ROUTE TO NEW SESSION
     ↓
SPECIALIZED WORK
     ↓
CREATE RETURN HANDOFF
     ↓
PARENT SESSION RESUMES
~~~

This keeps the parent workstream pure while preserving the value of the discovered task.

### Task Severance Rule

> **Out-of-scope work becomes a new package rather than contaminating the parent package.**

This rule is especially important in planning, research, debugging, design, and architecture sessions where many useful side paths can emerge.

---

## 5. The Prime Handoff Package

A handoff should contain the minimum sufficient context required for the next handler to begin useful work.

A Prime-native handoff package should be tool-neutral and transportable across agent systems.

Recommended fields:

~~~text
HANDOFF_ID
PARENT_PACKAGE_ID
PURPOSE
NEXT_OBJECTIVE
CURRENT_STATE
KNOWN_FACTS
OPEN_QUESTIONS
CONSTRAINTS
DECISIONS_ALREADY_MADE
FILES_OR_ARTIFACT_REFERENCES
WHAT_NOT_TO_REDO
EXPECTED_DELIVERABLE
SUGGESTED_SKILLS_OR_HANDLERS
SECURITY_REDACTIONS
RETURN_ROUTE
~~~

### Handoff Rule

> **A handoff package should contain the minimum sufficient context plus stable references to authoritative artifacts.**

The purpose is not to recreate the original session.

The purpose is to prepare the next handler.

---

## 6. References Beat Duplication

The transcript emphasizes that handoff documents should not repeat material already captured in stable artifacts.

If the relevant information already exists in:

- a PRD;
- issue;
- commit;
- branch;
- source file;
- test result;
- doctrine file;
- design specification;
- manifest;
- research note;

the handoff should point to it.

~~~text
BAD HANDOFF
copies entire document
copies entire issue
copies entire code diff
copies entire research history

GOOD HANDOFF
states purpose
states unresolved work
states decisions
links authoritative sources
identifies next action
~~~

### Pointer Rule

> **Carry the operational delta; reference the authority.**

This preserves source-of-truth discipline and prevents stale copies from becoming accidental documentation.

---

## 7. Handoff as a PRIME Operation

The handoff pattern maps cleanly into the Prime Process.

### P — PACKAGE

Extract only the context relevant to the new task.

### R — ROUTE

Define where the package is going and why.

### I — INSPECT

Remove duplication, irrelevant context, sensitive information, and unsupported assumptions.

### M — MOVE

Transfer the package to the next session, agent, tool, or human handler.

### E — ESTABLISH DELIVERY

Confirm that the requested work was completed and that useful results were returned to the originating workflow when required.

The handoff is therefore not outside Prime Process.

It is one of its most important package-routing operations.

---

## 8. The Return Handoff

One-way delegation is incomplete when the parent workflow depends on what the child learns.

The transcript describes a recurring pattern:

1. planning session identifies uncertainty;
2. uncertainty is handed to a prototype session;
3. prototype produces evidence;
4. child session creates a distilled handoff back to the planner;
5. planning resumes with new evidence.

~~~text
PARENT PACKAGE
     ↓
CHILD HANDOFF
     ↓
SPECIALIZED WORK
     ↓
OBSERVATION / EVIDENCE
     ↓
RETURN HANDOFF
     ↓
PARENT PACKAGE UPDATED
~~~

### Return Handoff Rule

> **A child package returns conclusions, evidence, and unresolved risks — not its entire working history.**

This is the practical equivalent of a controlled sub-workstream without requiring one vendor's native sub-agent implementation.

---

## 9. Evidence-Producing Detours

Some planning questions cannot be answered reliably through discussion alone.

The transcript shows a strong pattern: when a planning session reaches a question that requires direct evidence, the operator routes that uncertainty into a prototype.

Prime Process generalizes this.

~~~text
PLAN
 ↓
UNRESOLVED QUESTION
 ↓
EVIDENCE-PRODUCING PACKAGE
 ↓
PROTOTYPE / TEST / RESEARCH / BENCHMARK
 ↓
OBSERVATION
 ↓
RETURN HANDOFF
 ↓
PLAN UPDATED
~~~

Suitable evidence-producing detours include:

- prototype;
- benchmark;
- test;
- research task;
- user interview;
- visual mockup;
- data sample;
- API experiment;
- code spike;
- comparative evaluation.

### Evidence Detour Rule

> **When a planning question cannot be resolved by reasoning alone, route the uncertainty to an evidence-producing task.**

This reduces speculative planning and converts unknowns into measurable work.

---

## 10. Transit Artifacts vs. Canonical Artifacts

The transcript recommends saving handoff files in a temporary operating-system directory rather than permanently inside the project.

That distinction is valuable.

### CANONICAL ARTIFACT

A canonical artifact is:

- persistent;
- reviewed;
- versioned;
- source-of-truth;
- expected to remain meaningful over time.

Examples:

- doctrine;
- PRD;
- release manifest;
- source file;
- approved specification;
- verified test fixture.

### TRANSIT ARTIFACT

A transit artifact is:

- temporary;
- purpose-specific;
- routing-oriented;
- disposable after delivery;
- not intended to become long-term documentation.

Examples:

- handoff note;
- temporary route summary;
- session bridge;
- short-lived scratch manifest.

### Transit Artifact Rule

> **Temporary routing artifacts should not become permanent documentation by default.**

A shipping wrapper is not the cargo authority.

---

## 11. Security and Minimal Context

A handoff should carry only information necessary for the destination task.

The transcript explicitly calls for redaction of:

- API keys;
- passwords;
- secrets;
- credentials;
- unnecessary personally identifiable information;
- unrelated sensitive context.

Prime Process strengthens this into a broader handling rule.

> **Transit packages carry only the minimum necessary operational data.**

Security review belongs inside **Inspect**, not as an afterthought.

---

## 12. Purpose Must Be Declared

A handoff cannot be written well without knowing what the next handler is expected to do.

The transcript repeatedly emphasizes describing the purpose of the handoff.

That means a handoff is destination-aware.

~~~text
HANDOFF PURPOSE:
prototype difficult interaction

HANDOFF PURPOSE:
investigate defect

HANDOFF PURPOSE:
create issue

HANDOFF PURPOSE:
perform adversarial review

HANDOFF PURPOSE:
research unresolved dependency
~~~

### Purpose Rule

> **Every handoff must declare why the package is leaving and what the next handler must establish.**

Without this, the handoff becomes a generic summary rather than an operational package.

---

## 13. Suggested Skills as Routing Metadata

The transcript includes a useful addition: the handoff can recommend which skills the next agent should invoke.

Prime Process interprets this as routing metadata.

~~~text
PACKAGE
  ↓
DESTINATION
  ↓
SUGGESTED HANDLING CLASS
  ↓
SUGGESTED SKILLS / TOOLS
~~~

This is not equivalent to final routing authority.

The receiving system may inspect the package and choose a different lane.

### Routing Metadata Rule

> **A handoff may recommend handlers, but routing remains inspectable and revisable.**

---

## 14. Cross-Harness Portability

One of the strongest properties of a Markdown handoff is that it is not tied to one vendor.

A package can move between:

- Claude-based environments;
- Codex;
- Copilot CLI;
- other coding agents;
- human reviewers;
- future tools.

This matters because the stable interface is the **document contract**, not the harness.

Prime Process therefore prefers:

> **Tool-neutral package semantics with adapter-specific execution.**

The transport format may be Markdown today, but the doctrine should survive any particular interface.

---

## 15. Context Routing vs. Context Hoarding

A common failure mode is to keep every related task inside one session because the history is already there.

That feels efficient but creates a hidden cost.

~~~text
MORE TASKS
   ↓
MORE HISTORY
   ↓
MORE CROSS-TALK
   ↓
LESS TASK PURITY
   ↓
HARDER REVIEW
   ↓
MORE REWORK
~~~

Prime Process prefers:

~~~text
DISCOVER SIDE TASK
   ↓
SEVER
   ↓
PACKAGE
   ↓
ROUTE
   ↓
RETURN ONLY WHAT MATTERS
~~~

### Context Routing Rule

> **Context is not a warehouse to fill. It is cargo to route.**

---

## 16. Skill Extraction From Repeated Behavior

The speaker describes repeatedly creating handoff documents manually before deciding the behavior deserved a reusable skill.

That is a strong doctrine pattern.

Skills should not be invented merely because a catalog can contain them.

They should emerge from repeated, useful operator behavior.

~~~text
REPEATED FRICTION
      ↓
REPEATED MANUAL BEHAVIOR
      ↓
PATTERN IDENTIFIED
      ↓
PATTERN INSPECTED
      ↓
SKILL EXTRACTED
      ↓
REUSED
      ↓
RE-EVALUATED
~~~

### Skill Extraction Rule

> **Skills should be extracted from repeated successful behavior, not invented merely to fill a catalog.**

This aligns with the existing Prime Process Orchestration rule:

> **A repeated success may become doctrine only after it survives inspection.**

---

## 17. A Prime-Native Handoff Workflow

A minimal operational sequence:

~~~text
1. DETECT
   Identify work that should leave the current session.

2. SEVER
   Define the new task boundary.

3. PACKAGE
   Create a purpose-specific handoff.

4. INSPECT
   Remove duplication, secrets, irrelevant context, and stale assumptions.

5. ROUTE
   Select the receiving session, handler, or tool.

6. MOVE
   Transfer the handoff.

7. EXECUTE
   Complete the specialized task.

8. RETURN
   Package relevant findings for the parent workflow.

9. ESTABLISH DELIVERY
   Confirm the parent received and incorporated the needed result.

10. DISPOSE
   Remove the temporary transit artifact when it no longer serves an operational purpose.
~~~

---

## 18. Recommended Prime Handoff Template

~~~markdown
# PRIME HANDOFF

## Identity
- HANDOFF_ID:
- PARENT_PACKAGE_ID:
- CREATED_FROM:
- DESTINATION:

## Purpose
Why this work is leaving the parent workflow.

## Next Objective
What the receiving handler must establish or produce.

## Current State
Only the context necessary to begin.

## Known Facts
Established information relevant to the task.

## Open Questions
Unknowns the receiving handler should resolve.

## Constraints
Boundaries, prohibitions, budgets, compatibility rules, or deadlines.

## Decisions Already Made
Do not reopen these unless new evidence invalidates them.

## Authoritative References
Pointers to source files, issues, commits, doctrine, PRDs, tests, or other canonical artifacts.

## What Not to Redo
Completed work that should not be repeated.

## Expected Deliverable
The package the receiver must return.

## Suggested Skills / Handlers
Optional routing hints.

## Security Redactions
Sensitive information intentionally omitted.

## Return Route
Where the result goes when this package is complete.
~~~

---

## 19. Training Implication

This doctrine gives the curriculum a practical way to teach context discipline.

A learner should understand that advanced AI operation is not about keeping one enormous conversation alive forever.

It is about knowing when to:

- continue;
- compact;
- sever;
- route;
- prototype;
- return;
- discard.

The learner should eventually be able to operate several bounded workstreams without losing the identity, provenance, or purpose of any package.

This is logistics behavior, not chat behavior.

---

## 20. Canonical Statements

> **Context should be routed, not accumulated.**

> **Context should be curated, not merely accumulated.**

> **COMPACT preserves one package. HANDOFF creates another.**

> **Out-of-scope work becomes a new package rather than contaminating the parent package.**

> **A handoff package should contain the minimum sufficient context plus stable references to authoritative artifacts.**

> **Carry the operational delta; reference the authority.**

> **A child package returns conclusions, evidence, and unresolved risks — not its entire working history.**

> **When a planning question cannot be resolved by reasoning alone, route the uncertainty to an evidence-producing task.**

> **Temporary routing artifacts should not become permanent documentation by default.**

> **Transit packages carry only the minimum necessary operational data.**

> **Every handoff must declare why the package is leaving and what the next handler must establish.**

> **A handoff may recommend handlers, but routing remains inspectable and revisable.**

> **Tool-neutral package semantics with adapter-specific execution.**

> **Context is not a warehouse to fill. It is cargo to route.**

> **Skills should be extracted from repeated successful behavior, not invented merely to fill a catalog.**

---

## 21. Source and Provenance

This doctrine was synthesized from:

- existing DraftDeck Logistics Framework doctrine;
- existing Prime Process doctrine;
- existing Prime Process Orchestration doctrine;
- a user-supplied transcript describing a reusable handoff skill, session compaction, context routing, temporary Markdown handoff artifacts, prototype detours, cross-agent portability, redaction, and repeated-skill extraction.

This document is an original Prime Process synthesis. The source transcript is treated as a workflow reference, not as DraftDeck's canonical vocabulary or implementation dependency.
