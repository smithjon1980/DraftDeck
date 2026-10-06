# 01 — BOSS Operator Program: Plan of Instruction (POI)

**Status:** Candidate Controlled Document (v1 draft)
**Authority chain:** DOCTRINE > POI > MODULE SOURCE > GENERATED MEDIA
**Governing architecture:** training/production-architecture.md
**Governs:** the BOSS Information Logistics Operator Program — curriculum structure, assessment architecture, and qualification requirements. Subordinate to BOSS doctrine in all conflicts.

> **Generated material may explain the source. It may not redefine the source.**

---

## 1. Program Identity

**BOSS Information Logistics Operator Program** — the instructional specialization of BOSS (Bioscillate Operating System by Seven).

The program produces operators who move bounded packages of information through a governed logistics network: packaging, routing, inspection, movement, and established delivery.

> **You are not learning how to carry one AI package. You are learning how to operate a logistics network for information.**

## 2. Program Chain (Learner Journey)

```text
ENTITY IDENTIFIES NEED
↓
ROLE DEFINED
↓
OPPORTUNITY PUBLISHED
↓
APPLICATION / SCREENING / SELECTION
↓
OFFER → ACCEPTANCE
↓
PRE-BOARDING
↓
DAY ZERO ORIENTATION
↓
SEVEN-MODULE TRAINING
↓
FINAL INTEGRATED SIMULATION
↓
QUALIFICATION
↓
AUTHORIZED OPERATION
```

Day Zero is orientation and calibration; the seven-module system begins after Day Zero.

> **Day Zero establishes the learner's initial routing state before curriculum movement begins.**

## 3. Seven-Module Sequence

| Module | Podcast | Deck | System Question |
|---|---|---|---|
| 01 | The Package | Package Operations | What exactly is being moved? |
| 02 | The Route | Route Operations | Where should this package go, and under what conditions may it move? |
| 03 | The Facility | Facility Operations | How do we safely control many packages moving through one operational environment? |
| 04 | The Transfer | Transfer Operations | How does work change custody without losing meaning, authority, or evidence? |
| 05 | The Transport Decision | Transport Coordination | What kind of handling does this package require? |
| 06 | When Consequence Increases | High-Control Operations | What additional controls are required when the consequence of failure increases? |
| 07 | The Network | Network Orchestration | How do we govern many packages, routes, handlers, and dependencies as one accountable system? |

Modules are sequenced: each module's bridge section hands the learner's state to the next. No module may be skipped on the basis of self-reported proficiency.

## 4. Module ABI (Application Binary Interface)

Every module source package exposes the same contract. Any module conforming to this ABI can be compiled into the full artifact family without structural invention.

```text
MODULE_SOURCE :=
  MODULE IDENTITY
  SYSTEM QUESTION
  TERMINAL OBJECTIVE
  ENABLING OBJECTIVES
  DOCTRINE DEPENDENCIES
  CANONICAL VOCABULARY
  CANONICAL STATEMENTS
  SCOPE
  OUT OF SCOPE
  FAILURE MODES
  WORKED EXAMPLES
  NEXT-MODULE BRIDGE
```

Companion briefs per module: PODCAST_BRIEF, SLIDE_DECK_BRIEF, WORKBOOK_AND_QUIZ_BRIEF, INFOGRAPHIC_BRIEF. Briefs govern a single artifact family for one module; the module source governs content.

## 5. Terminal Objectives

**Module 01 (locked):** At the conclusion of Module 1, the learner will be able to convert an operational request into a bounded work package with an established destination, scope, required inputs, and acceptance conditions.

**Modules 02–07 (candidate, to be locked with each module source):**

- **M02:** Given a bounded package, select a route and declare the conditions under which the package is authorized to move.
- **M03:** Given many packages moving through one operational environment, apply facility controls that keep packages separable, observable, and recoverable.
- **M04:** Given a custody change between handlers, execute a transfer that preserves meaning, authority, and evidence.
- **M05:** Given a package and a set of candidate handlers, select transport according to the job's handling requirements.
- **M06:** Given a package whose failure consequence is elevated, apply the additional controls required for high-control operations.
- **M07:** Given many packages, routes, handlers, and dependencies, operate them as one accountable network with release authority intact.

## 6. Enabling Objectives

Defined per module in the module source. Rule (applies to all):

> **A learning goal should be expressed as an observable capability whenever practical.**

Module 01 enabling objectives (locked, seven): distinguish mission from package; identify package boundaries; identify required inputs; establish destination; establish acceptance conditions; recognize over-broad packages; reduce package scope without reducing destination scope.

## 7. Doctrine Dependencies

| Module | Primary doctrine dependencies |
|---|---|
| 01 | Logistics framework ontology; PRIME protocol (Package); alignment doctrine ("Alignment precedes packaging"); bounded manifest; minimum necessary cargo |
| 02 | PRIME protocol (Route); shipping label classification; "Route according to the job, not according to prestige"; restricted cargo authorization |
| 03 | Bounded autonomy / execution envelope; span of control; facility-level observability and recovery |
| 04 | Custody and handoff; provenance; "Stale context is active contamination"; evidence preservation |
| 05 | Capability routing (CAPABILITY_CLASS); "Capability to produce does not establish capability to verify"; PLACEMENT ≠ CAPABILITY |
| 06 | Restricted cargo handling; "CAN PROCESS ≠ MAY RECEIVE"; verification profiles; escalation |
| 07 | Evidence & verification architecture; control spine (LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY); "Throughput is a network metric. Delivery is a package claim."; release authority |

## 8. Artifact Matrix

Per module, exactly:

| Artifact | Instructional job | Governing brief |
|---|---|---|
| Deep-Dive podcast | Carries story and reasoning | PODCAST_BRIEF |
| Slide deck (16:9) | Shows the architecture | SLIDE_DECK_BRIEF |
| Workbook exercise set | Owns performance | WORKBOOK_AND_QUIZ_BRIEF |
| Module quiz | Produces evidence | WORKBOOK_AND_QUIZ_BRIEF |
| Instructor guide section | Governs facilitation | Instructor Guide master |
| Student manual section | Governs reference | Student Manual master |
| Infographic ×3 (square / portrait / landscape) | Compresses; one concept, three jobs | INFOGRAPHIC_BRIEF |

Program-wide: Instructor Guide master, Student Operator Manual master, Workbook master, Operator Glossary, Resource/Capability Reference, Qualification Standard, Final Integrated Simulation, Visual & Terminology Standard, this POI, Source Authority.

> **Every artifact teaches the same seven-module progression, but each medium performs a different instructional job.**

Production status note: NotebookLM Deep Dives and generated visuals are pre-production prototypes. Final decks and infographics are rebuilt in DraftDeck/Canva under the composition standard; final audio is synthesized from canonical scripts under a controlled TTS stack.

## 9. Competency Crosswalk

| Program competency | Built in | Evidenced by |
|---|---|---|
| Bound operational requests into packages | M01 | Workbook M01; Quiz 01 (applied) |
| Select and authorize routes | M02 | Workbook M02; Quiz 02 (applied) |
| Control multi-package environments | M03 | Workbook M03; facility scenario |
| Execute custody-preserving transfers | M04 | Workbook M04; handoff exercise |
| Select handlers by requirement | M05 | Workbook M05; routing cases |
| Apply high-control measures | M06 | Workbook M06; high-consequence scenario |
| Operate the network end-to-end | M07 + Final Simulation | Final Integrated Simulation (observed) |

## 10. Assessment Architecture

Per module:

```text
INSTRUCTION
↓
KNOWLEDGE CHECK
↓
CLASSIFICATION TASK
↓
WORKBOOK PERFORMANCE
↓
MODULE QUIZ
↓
LEARNER-STATE UPDATE
```

Quiz structure: Recall / Classification / Application, with applied items carrying the greatest weight.

After Module 7:

```text
FINAL INTEGRATED SIMULATION
↓
OBSERVED PERFORMANCE
↓
VERIFICATION
↓
QUALIFICATION DECISION
```

> **QUIZ PASS ≠ OPERATOR QUALIFICATION.**

> **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**

## 11. Qualification Requirements

Qualification requires all of:

1. Completion of Modules 01–07 (TRAINED).
2. Demonstrated capability on the Final Integrated Simulation, on novel material, unprompted (QUALIFIED).
3. Attestation by program authority (CERTIFIED).
4. Durable binding of identity to qualification (CREDENTIALED).
5. Context-specific grant of permission (AUTHORIZED).

```text
TRAINED ≠ QUALIFIED ≠ CERTIFIED ≠ CREDENTIALED ≠ AUTHORIZED
```

> **CAPABILITY ≠ PERMISSION.**

## 12. Instructor Requirements

- Instructors must hold current operator qualification and be authorized to instruct by program authority.
- Instructors must teach to the module source, not to personal preference; deviations are surfaced, not silently absorbed.
- Instructors score applied evidence highest and feed observed gaps back as learner-state updates.
- Instructor-guide sections govern teaching sequence, timing, discussion prompts, misconceptions, activity directions, scoring, remediation, and module bridges.

## 13. Release Requirements

A training artifact is releasable only when:

1. It traces to the module source and this POI (no orphan content).
2. Doctrine audit: every canonical statement matches doctrine wording verbatim.
3. Terminology audit: glossary-conformant; no prohibited vocabulary.
4. Visual normalization: composition standard applied (where visual).
5. Script control: final audio synthesized from the canonical script, verbatim canonical lines intact (where audio).
6. Cross-media QA: the module family is internally consistent across podcast, deck, workbook, quiz, and infographics.
7. Entry recorded in the cross-media release ledger (81).

> **EVAL PASS ≠ RELEASE.**

## 14. Scaling Rule

The operational structure taught expands as the operating problem expands:

- Beginner: PACKAGE → ONE HANDLER → VERIFY
- Intermediate: MANIFEST → MULTIPLE HANDLERS → CONSOLIDATE → VERIFY
- Advanced: MULTIPLE MANIFESTS → MULTIPLE ROUTES → RESOURCE ALLOCATION → CONTROL PLANE → INDEPENDENT VERIFICATION → RELEASE

> **Use only the operational structure the workload requires.**

---

## Amendment Rule

Amendments to this POI ride a guarded change set. The POI remains Candidate until the Module 01 vertical slice (all seven artifacts for Module 01) validates the Module ABI end-to-end; it then flips to Controlled.
