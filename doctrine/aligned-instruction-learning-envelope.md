# Aligned Instruction & Learning Envelopes

**Status:** Candidate Canonical Doctrine
**Placement:** After Alignment / Decomposition / Feedback in the doctrine stack — a downstream specialization of *Alignment precedes packaging* into the instructional domain.
**Purpose:** Define the constitutional limit on instruction and the Learning Envelope as its enforcement shape, so that teaching is governed by the learner's destination, state, and constraints rather than by the content available.

---

## Doctrine Coordinates

> **Primary PARCELS:** L7 Service
> **Secondary:** L3 Routing, L4 Carriage, L5 Exchange
> **PRIME influence:** Package / Route boundary and Establish Delivery
> **Constitutional role:** instruction begins with alignment, not content

---

## 1. The Missing Contract

Execution doctrine already says: *define the envelope before delegation.*

Instruction requires the symmetrical rule: **define the learning envelope before teaching.**

The recurring failure in teaching systems is beginning with content:

```text
TEACH ME ITALIAN
      ↓
ITALIAN LESSON
```

The governed form is:

```text
TEACH ME ITALIAN
      ↓
ALIGN
      ↓
LEARNING ENVELOPE
      ↓
INSTRUCTION PLAN
      ↓
LESSON
```

> **Instruction begins with alignment, not content.**

Stronger form:

> **The amount, sequence, and form of instruction should be governed by the learner's destination, current state, constraints, and available attention.**

The first artifact of instruction is not the lesson. The first artifact is the **learning mission**.

---

## 2. The Learning Envelope

The Learning Envelope is the educational counterpart to the Execution Envelope — the complete declaration of who is learning, why, from where, under what constraints, and toward what observable outcome:

```text
LEARNING_ENVELOPE

LEARNER_ID
MISSION
WHY
TARGET_OUTCOME

CURRENT_LEVEL
KNOWN_CAPABILITIES
KNOWN_GAPS

TIME_AVAILABLE
SESSION_LENGTH
PACE

INTEREST_CONTEXT
WORKING_LANGUAGE
ACCESSIBILITY_REQUIREMENTS

TEACHING_PREFERENCES
PRACTICE_MODE
ASSESSMENT_MODE

SUCCESS_CRITERIA
STOP_CONDITION
NEXT_CHECKPOINT
```

> **A learner's destination, current state, constraints, and available attention govern the route.**

An instructional system that teaches without an established envelope is the educational equivalent of an unattended handler without an execution envelope: movement without governed scope.

---

## 3. Mission ≠ Curriculum ≠ Lesson

Three distinct objects must not be conflated:

- **MISSION** — where the learner wants to arrive.
- **CURRICULUM** — the sequence of packages currently believed to get them there.
- **LESSON** — the bounded movement happening now.

```text
MISSION
   ↓
LEARNING ROUTE
   ↓
CURRICULUM
   ↓
LESSON PACKAGE
   ↓
PRACTICE
   ↓
EVIDENCE
```

A fixed schedule is an *implementation* of a learning route. It must be changeable when learner state changes. This is *Implementation serves doctrine* applied to curriculum: the mission governs destination; the schedule is implementation.

### Observable capability

Vague intent is ungovernable. "Learn Italian" is not a package; it is a direction. A governable objective is bounded and observable:

> **A learning goal should be expressed as an observable capability whenever practical.**

Bad package: `LEARN ITALIAN`.
Governable package: *Recognize and pronounce common Italian menu terms, within a 15-minute session, for a total beginner* — with success expressed as something like *read a real Italian menu aloud and roughly understand what is being ordered.*

---

## 4. Declared vs. Observed Learner State

This doctrine inherits the Shipping Label rule — *declared metadata is evidence, not unquestionable truth* — and applies it to the learner:

- **DECLARED LEARNER STATE** — what the learner reports: goals, self-assessed level, preferences, available time.
- **OBSERVED LEARNER STATE** — what performance demonstrates: diagnostic results, recall, error patterns, demonstrated capability.

> **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**

A learner who reports "intermediate" may demonstrate beginner performance in one subdomain and advanced performance in another. The system routes from evidence, not from identity labels.

This yields the complete learning loop:

```text
MISSION
   ↓
LEARNING ENVELOPE
   ↓
INITIAL DIAGNOSTIC
   ↓
LEARNER STATE
   ↓
ROUTE
   ↓
LESSON PACKAGE
   ↓
PRACTICE
   ↓
ASSESS
   ↓
UPDATE LEARNER STATE
   ↓
REROUTE
   ↓
NEXT PACKAGE
```

Alignment is not a one-time intake. It is continuously re-established from evidence.

---

## 5. Delivery Establishment

Completing a lesson is movement, not delivery.

> **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

This is the educational form of *TEST PASS ≠ DELIVERY ESTABLISHED*. In PRIME terms:

```text
LESSON COMPLETED
       ≠
LEARNING ESTABLISHED
```

Establish Delivery in instruction means: determine whether the learner can actually perform the target capability — recall, application, pronunciation, transfer — under the envelope's declared assessment mode.

A beautifully rendered lesson is an L6 artifact. It is not evidence of L7 fulfillment:

> **Representation ≠ learning.**

---

## 6. PARCELS Mapping

Instructional concerns locate cleanly across all seven layers:

| Layer | Instructional responsibility | Rule |
|---|---|---|
| L1 Platform | Learner's substrate: device, audio availability, tools, time | **Instruction may not assume a learning substrate that has not been established.** A pronunciation lesson cannot assume audio exists. |
| L2 Attachment | Learner profile and mission bound to the correct learner: `LEARNER_ID`, `MISSION_ID`, `COURSE_ID`, `SESSION_ID` | One learner's assumptions, constraints, or progress must not contaminate another learning package. |
| L3 Routing | What this learner encounters next, from current state + mission + prerequisites + available time + observed performance | Adaptive instruction is a routing function, not a content property. |
| L4 Carriage | Delivery cadence: session length, pacing, repetition, retries, spaced practice, missed-session handling, overload prevention | Missed-session and recovery protocols live here structurally. |
| L5 Exchange | Persistent learning continuity: durable mission, notes, learner profile, teaching preferences | **Learning continuity should depend on durable learner state, not conversational memory.** |
| L6 Language | Representation: text, audio, exercises, vocabulary, visual explanation, chosen per learner and subject | Representation must not be mistaken for understanding. |
| L7 Service | The actual learning outcome: demonstrated capability | Content delivered ≠ learning established. |

The L5 rule is the educational form of *Context should be routed, not accumulated*: a later session resumes from durable learner state, not from reconstructing a conversation.

---

## 7. PRIME Mapping

The instructional workflow maps onto PRIME without strain:

- **P — Package.** The subject is not the package. The bounded learning objective is the package.
- **R — Route.** Route the learner to the correct lesson from goal, level, prerequisites, interest, and available time.
- **I — Inspect.** Check prerequisite knowledge, comprehension, recall, pronunciation, errors — before and during movement.
- **M — Move.** Deliver instruction, examples, practice, feedback.
- **E — Establish Delivery.** Determine whether the learner can perform the target capability.

The loop in §4 is PRIME with feedback: each package's Establish Delivery updates the learner state that governs the next package's Route.

---

## 8. Day Zero

This doctrine explains why Day Zero exists and what it is constitutionally responsible for.

Day Zero is not a lesson. It is orientation and calibration — the establishment of initial routing state:

> **Day Zero establishes the learner's initial routing state before curriculum movement begins.**

Formal responsibility:

```text
DAY ZERO

ESTABLISH:
MISSION
MOTIVATION
CURRENT STATE
TIME ENVELOPE
LEARNING CONSTRAINTS
SUCCESS CONDITION
INITIAL ROUTE
RECOVERY RULES
```

Only after Day Zero has established these does Day 1 begin instruction. Diagnostic placement, time expectations, operating rules, missed-day handling, and path routing are Day Zero's native mechanics — this doctrine names their structural home (L4 Carriage for cadence and recovery, L3 Routing for initial path selection) rather than altering their content.

Per *Doctrine vs. Training Material*: this doctrine defines Day Zero's **responsibility**. Curriculum authors define Day Zero's **content**. Where a lesson conflicts with doctrine, doctrine wins; doctrine does not author lessons.

---

## 9. The Three-Axis Correspondence

The instructional architecture reuses the full operating model:

| Axis / Layer | Execution domain | Instructional domain |
|---|---|---|
| CONSTITUTION | Autonomy requires confinement | Instruction begins with alignment |
| Envelope | Execution Envelope | Learning Envelope |
| PARCELS | Where concerns live | Where learning responsibilities live |
| PRIME | How work moves | How learning packages move |
| Evidence | Verification, test results | Demonstrated capability |
| Service | Delivery established | Learning established |

The structural correspondence survives across domains. Teaching and software execution are not the same thing — but governed transformation has the same shape in both: align, bound, route, move, establish.

---

## 10. External References

This doctrine was sharpened by studying an external language-instruction transcript whose workflow independently arrives at envelope-first teaching: motivation, current level, available time, interests, working language, success definition, teaching approach, learner profile — before any lesson content. Per *Doctrine vs. External References*: the mechanics were studied; the doctrine above is ours.

> **Study the mechanics. Preserve our doctrine.**

---

## 11. Non-Negotiables

1. **Instruction begins with alignment, not content.**
2. **The amount, sequence, and form of instruction should be governed by the learner's destination, current state, constraints, and available attention.**
3. **A learning goal should be expressed as an observable capability whenever practical.**
4. **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**
5. **Learning continuity should depend on durable learner state, not conversational memory.**
6. **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

---

## 12. Canonical Statements

> **Instruction begins with alignment, not content.**

> **A learner's destination, current state, constraints, and available attention govern the route.**

> **The first artifact of instruction is the learning mission, not the lesson.**

> **Mission governs destination; curriculum is implementation.**

> **A learning goal should be expressed as an observable capability whenever practical.**

> **Self-reported proficiency informs routing; demonstrated performance provides the primary evidence for instructional state.**

> **Learning continuity should depend on durable learner state, not conversational memory.**

> **Instruction may not assume a learning substrate that has not been established.**

> **Representation ≠ learning.**

> **CONTENT DELIVERED ≠ LEARNING ESTABLISHED.**

> **Day Zero establishes the learner's initial routing state before curriculum movement begins.**
