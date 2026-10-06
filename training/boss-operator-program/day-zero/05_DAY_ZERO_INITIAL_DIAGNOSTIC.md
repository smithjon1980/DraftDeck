# Day Zero Initial Diagnostic

**Status:** Candidate Assessment Instrument  
**Purpose:** Establish baseline evidence for instructional routing.

The diagnostic is not a qualification exam.

## Part A — Declared Experience

Rate familiarity from 0–3:
0 = none
1 = limited exposure
2 = working familiarity
3 = frequent practical use

- AI assistants
- structured prompting
- file/version management
- source verification
- visual production
- workflow automation
- multi-step task decomposition

These ratings are routing inputs only.

## Part B — Recognition

### 1. Which statement is correct?
A. The most capable handler should always receive the package.  
B. Capability and permission are separate.  
C. Any package can move if the task is legitimate.  
D. A completed output is automatically released.

Expected: B.

### 2. If handling requirements are unknown, what is the correct next state?
A. Guess the safest route  
B. Use the strongest available model  
C. HOLD  
D. Skip classification

Expected: C.

### 3. Put PRIME in order.
PACKAGE / ROUTE / INSPECT / MOVE / ESTABLISH DELIVERY

### 4. Which statement is correct?
A. Training completion equals qualification.  
B. Qualification equals authorization.  
C. Credentialing grants universal authority.  
D. These states remain distinct.

Expected: D.

## Part C — Demonstrated Micro-Task

Prompt:

“You receive a request: ‘Make this better.’ The source is a 40-page training document. No destination format, audience, deadline, or acceptance condition is provided.”

Ask the learner to write:
1. what is known;
2. what is unknown;
3. whether the work is ready to route;
4. the next action they would take.

### Evidence sought

Strong response:
- separates known from unknown;
- refuses to invent destination/acceptance;
- identifies need for alignment;
- uses HOLD or equivalent bounded stop if routing requirements are insufficient.

## Diagnostic Output

Record:

```text
DECLARED_STATE
OBSERVED_STATE
GAPS
STARTING_ROUTE
REMEDIATION_REQUIRED
```

Do not compute a single “ability score” from these fields.
