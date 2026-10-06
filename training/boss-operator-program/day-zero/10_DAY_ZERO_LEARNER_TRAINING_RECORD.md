# Day Zero Learner Training Record

**Status:** Candidate Record Schema  
**Purpose:** Preserve durable learner state from entry through Module 01 handoff.

## Required fields

```text
LEARNER_ID
ENTRY_STATUS
PREBOARDING_STATUS
DAY_ZERO_STATUS
LEARNING_MISSION
TIME_ENVELOPE
LEARNING_CONSTRAINTS
AVAILABLE_TOOLS
DECLARED_EXPERIENCE
OBSERVED_BASELINE
KNOWN_GAPS
REMEDIATION_ITEMS
ORIENTATION_CLEARANCE
INITIAL_ROUTE
MODULE_01_ENTRY_STATE
RECORD_VERSION
UPDATED_AT
UPDATED_BY
```

## State rules

- Self-report and demonstrated evidence remain separate fields.
- Unknowns remain unknown; do not fill them by inference.
- A learner can be accepted while Day Zero remains on HOLD.
- A learner can be cleared with remediation without being qualified.
- Authorization is not recorded as implied by training status.

## Handoff to Module 01

The record passed into Module 01 should contain only what Module 01 needs for instructional routing.

Learning continuity depends on durable learner state, not conversational memory.
