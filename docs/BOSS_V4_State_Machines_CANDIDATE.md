# BOSS V4 — Proposed state machines

**Status:** `CANDIDATE_PENDING_HUMAN_REVIEW`. The diagrams illustrate proposed lifecycle states in architecture §5. They do not implement authorization, release permissions, revocation, concurrency, or idempotent recovery. Every material action needs policy enforcement and an audited decision outside model-generated text.

## Engagement

```mermaid
stateDiagram-v2
    [*] --> DRAFT
    DRAFT --> ADMISSION_REVIEW: Submit intake
    ADMISSION_REVIEW --> DECLINED: Decline
    ADMISSION_REVIEW --> HOLD: Requirements unresolved
    ADMISSION_REVIEW --> AUTHORIZED: Human authorizes scope
    HOLD --> ADMISSION_REVIEW: Resolve admission questions
    HOLD --> REVIEW_REQUIRED: Resolve active review hold
    AUTHORIZED --> ACTIVE: Start authorized work
    ACTIVE --> REVIEW_REQUIRED: Dossier / exception
    ACTIVE --> HOLD: Missing prerequisites or risk
    REVIEW_REQUIRED --> ACTIVE: Authorized revision
    REVIEW_REQUIRED --> HOLD: Insufficient evidence
    REVIEW_REQUIRED --> COMPLETED: Human accepts scoped outcome
    COMPLETED --> CLOSED: Record closure
    DRAFT --> CANCELLED: Cancel
    AUTHORIZED --> CANCELLED: Authorized cancellation
    ACTIVE --> CANCELLED: Authorized cancellation
    HOLD --> CANCELLED: Authorized cancellation
    DECLINED --> [*]
    CLOSED --> [*]
    CANCELLED --> [*]
```

**Review requirement:** `HOLD` can originate during admission or active work. Resuming must retain the interrupted phase and cannot manufacture authority. `COMPLETED` must bind a human decision to exact scope and artifact identity.

## Work Commission

```mermaid
stateDiagram-v2
    [*] --> DRAFT
    DRAFT --> READY: Contract and authority checked
    READY --> ASSIGNED: Select registered practice
    ASSIGNED --> RUNNING: Start scoped operation
    RUNNING --> DELIVERED_UNINSPECTED: Receipt verified
    RUNNING --> INSPECTION_HOLD: Missing output / unknown result
    DELIVERED_UNINSPECTED --> INSPECTED_ACCEPTABLE: Receiver inspects and accepts
    DELIVERED_UNINSPECTED --> INSPECTED_REJECTED: Receiver rejects
    DELIVERED_UNINSPECTED --> INSPECTION_HOLD: Evidence incomplete
    INSPECTION_HOLD --> ASSIGNED: Authorized retry
    INSPECTION_HOLD --> ESCALATED: Scope/permission question
    INSPECTED_REJECTED --> ASSIGNED: Authorized rework
    INSPECTED_REJECTED --> ESCALATED: Material dispute
    INSPECTED_ACCEPTABLE --> CLOSED: Record closure
    ESCALATED --> INSPECTION_HOLD: Await decision
    ESCALATED --> ASSIGNED: Human-authorized revision
    DRAFT --> CANCELLED: Cancel
    READY --> CANCELLED: Cancel
    ASSIGNED --> CANCELLED: Cancel
    RUNNING --> CANCELLED: Authorized abort + cleanup
    INSPECTION_HOLD --> CANCELLED: Authorized cancellation
    INSPECTED_REJECTED --> CANCELLED: Authorized cancellation
    CLOSED --> [*]
    CANCELLED --> [*]
```

**PRIME boundary:** `DELIVERED_UNINSPECTED` requires actual receipt; transfer confirmation is not a test pass. `INSPECTED_ACCEPTABLE` describes the *commission receiver's review*, not client approval or public release. Approval requires a distinct authenticated decision record.

These are candidate transitions requiring negative tests and human ratification. They are not a deployed state machine.
