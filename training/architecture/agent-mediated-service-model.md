# Agent-Mediated Service & Candidate-State Architecture

**Status:** Candidate Architecture Note  
**Program:** BOSS Operator Program  
**Purpose:** Archive and formalize the unified framing that AI work is both agent-mediated at intake and provisional at output: requests are admitted through a governed service boundary, and generated results remain candidate artifacts until consequence-appropriate adjudication establishes them for use.

## Core shift

The common public framing is roughly:

```text
USER
↓
PROMPT
↓
LLM
↓
ANSWER
```

That picture makes it feel as if the user is directly operating the model.

For BOSS, the more useful architecture is:

```text
HUMAN / SENDER
↓
REQUEST
↓
AGENT / SERVICE COUNTER
↓
PACKAGE PREPARATION
↓
ADMISSION INSPECTION
↓
ACCEPT / HOLD / REFUSE
↓
ROUTING
↓
MODEL / TOOL / RUNTIME CAPABILITY
↓
VERIFICATION
↓
DELIVERY TO HUMAN / RECEIVER
```

The end user should not reason as though they are directly commanding raw model capability. They are submitting work through an intermediary control layer.

That intermediary is where governance belongs.

## Agent as service counter

The package clerk does not manufacture the destination, drive every truck, fly the aircraft, sort every package, and personally deliver it.

The clerk represents the network at its **admission boundary**.

Their responsibility is to determine whether what the customer is trying to send is sufficiently specified and eligible to enter the system.

That maps directly to a governed AI agent.

The agent should be responsible for:

```text
UNDERSTAND THE REQUEST
↓
BOUND THE WORK
↓
IDENTIFY MISSING OPERANDS
↓
ASSEMBLE THE PACKAGE
↓
COMPLETE / VALIDATE THE SHIPPING LABEL
↓
CLASSIFY THE CARGO
↓
CHECK PERMISSION
↓
DETERMINE REQUIRED CAPABILITIES
↓
ACCEPT / HOLD / REFUSE
↓
ROUTE TO ELIGIBLE MODEL / TOOL / RUNTIME
↓
COLLECT RESULT
↓
VERIFY AGAINST ACCEPTANCE CONDITIONS
↓
RETURN DELIVERY EVIDENCE
```

A good agent may ask questions instead of immediately generating.

A counter clerk who receives “send this somewhere good” does not invent the address.

Likewise, a governed agent receiving “make this better” should not automatically turn ambiguity into execution. It should determine whether a valid package can actually be constructed.

## Request is not package

A prompt is not necessarily the package.

A prompt may only be the initial request.

Example:

```text
USER REQUEST

"Make this presentation better."
```

That is not yet the full payload.

The agent may still need to establish:

```text
SOURCE
AUDIENCE
DESTINATION FORMAT
PURPOSE
SCOPE
STYLE REQUIREMENTS
PROTECTED CONTENT
AVAILABLE TOOLS
PERMITTED DESTINATIONS
ACCEPTANCE CONDITIONS
DELIVERY LOCATION
```

Only after that can the work become a governed package.

Therefore:

> **REQUEST ≠ PACKAGE.**

This distinction belongs beside other BOSS distinctions:

```text
REQUEST ≠ PACKAGE

CAPABILITY ≠ PERMISSION

CAN PROCESS ≠ MAY RECEIVE

MOVEMENT ≠ DELIVERY

OUTPUT ≠ VERIFIED RESULT
```

## Model as capability, not cargo

The model is not what is being shipped.

The data/work package is what is being handled.

The model is a **processing capability available inside the network**.

Updated role mapping:

```text
HUMAN         = SENDER / RECEIVER

REQUEST       = SHIPPING REQUEST

DATA + TASK   = CARGO / PAYLOAD

PACKAGE       = BOUNDED UNIT OF ACCOUNTABILITY

AGENT         = COUNTER CLERK / ADMISSION AGENT /
                ROUTING COORDINATOR

MODEL         = PROCESSING CAPABILITY

TOOL          = SPECIALIZED HANDLING CAPABILITY

RUNTIME       = PROCESSING / HANDLING ENVIRONMENT

ROUTE         = AUTHORIZED EXECUTION PATH

VERIFICATION  = DELIVERY INSPECTION / PROOF

HUMAN AUTHORITY
              = FINAL RELEASE AUTHORITY
```

The model is inside the service network. The customer does not need to manually choose every internal processing surface before the shipment can be accepted.

## Requirements before model selection

AI products often encourage:

> Which model do you want?

BOSS reverses the primitive:

> **The sender's responsibility is to specify the shipment correctly. The network's responsibility is to determine eligible handling.**

This does not mean a sophisticated user can never request a specific model. It means model selection is not the primitive. Requirements are the primitive.

Instead of:

```text
USER
↓
PICK MODEL
↓
WRITE PROMPT
↓
HOPE
```

BOSS teaches:

```text
USER
↓
STATE NEED
↓
AGENT BUILDS / VALIDATES PACKAGE
↓
ADMISSION
↓
CLASSIFICATION
↓
REQUIREMENTS
↓
ELIGIBLE HANDLING OPTIONS
↓
ROUTE
↓
EXECUTION
↓
VERIFICATION
```

## Agent Counter Contract

This architecture introduces a major BOSS object:

> **Agent Counter Contract**

The agent at the interface must be able to perform at least six responsibilities:

1. **Intake** — understand what the human is asking.
2. **Package construction** — turn the request into bounded accountable work.
3. **Admission control** — determine whether required information and authorization are sufficient.
4. **Classification** — determine handling requirements before selecting capability.
5. **Routing** — select eligible models, tools, runtimes, or other agents.
6. **Delivery establishment** — return the result with the evidence necessary to know what happened.

A governed BOSS agent has authority only inside the package and routing envelope it has been granted.

When the missing decision exceeds that envelope:

```text
DO NOT INVENT
↓
HOLD
↓
CLARIFY / ESCALATE
```

## Module 01 impact

Module 01 should now include the interaction between **sender and admission agent**.

Opening scenario:

```text
HUMAN:
"I need this sent."

AGENT:
"What exactly needs to move?"

HUMAN:
"This document."

AGENT:
"Where does it need to end up?"

...

↓
PACKAGE ESTABLISHED
↓
LABEL COMPLETE
↓
ADMISSION INSPECTION
```

Module 01 teaches two perspectives:

- **Sender responsibility** — supply purpose and necessary truth.
- **Agent responsibility** — structure, test, account, and refuse to fabricate missing requirements.

Neither side should invent missing requirements.

## Day Zero impact

Day Zero should contrast the common illusion with the governed operating model.

What it feels like:

```text
YOU → MODEL
```

What BOSS teaches you to see:

```text
YOU
↓
AGENT / INTERFACE
↓
PACKAGE
↓
ADMISSION
↓
ROUTE
↓
MODEL + TOOLS + RUNTIME
↓
VERIFICATION
↓
YOU
```

This diagram becomes a primary Day Zero correction.

## DraftDeck impact

DraftDeck is a product specimen of BOSS.

The user does not conceptually tell “the model”:

> Make me 12 slides.

The DraftDeck agent receives the request and builds the package:

```text
SOURCE MATERIAL
SLIDE COUNT
AUDIENCE
CANVAS
DESIGN SYSTEM
EDITABILITY REQUIREMENTS
IMAGE POLICY
OUTPUT FORMAT
ACCEPTANCE CONDITIONS
```

Then it determines required internal capabilities:

```text
TEXT MODEL
LAYOUT ENGINE
IMAGE GENERATOR
SVG BUILDER
CANVA
PPTX GENERATOR
VALIDATOR
```

That is the carrier network. DraftDeck is the counter. The agent coordinates the shipment.

## Constitutional-level principle

> **AI capability should be approached as a governed service network, not as an intelligence endpoint.**

More precisely:

> **You do not govern AI by controlling intelligence directly. You govern the packages admitted to capable systems, the conditions under which they move, and the evidence required before their outputs are accepted.**

The user's primary question changes from:

> “What can the AI do?”

to:

> **“What am I asking to move, what must be true before it moves, and what capability is permitted to handle it?”**

This is the interface architecture for governed AI work.


---

## Candidate-state doctrine

The agent-mediated service model and the candidate-output principle are one architecture, not two unrelated ideas.

The first governs **what enters capable systems**.

The second governs **what is allowed to leave them as established work**.

The complete lifecycle is:

```text
HUMAN / SENDER
↓
REQUEST
↓
AGENT / SERVICE COUNTER
↓
PACKAGE CONSTRUCTION
↓
ADMISSION INSPECTION
↓
ACCEPT / HOLD / REFUSE
↓
CLASSIFICATION
↓
ROUTE TO ELIGIBLE CAPABILITY
↓
MODEL / TOOL / RUNTIME EXECUTION
↓
GENERATED RESULT
↓
CANDIDATE STATE
↓
CONSEQUENCE-APPROPRIATE ADJUDICATION
↓
ACCEPT / REVISE / REJECT / ESCALATE
↓
RELEASE AUTHORITY
↓
ESTABLISHED RESULT / DELIVERY
```

This yields a closed-loop control architecture:

> **Govern admission before execution. Govern adjudication before release.**

The system should not treat raw generation as authority merely because the output is fluent, complete-looking, fast, or produced by a powerful model.

## Generated output is candidate state

A generated artifact is not authoritative merely because a model, agent, tool, or workflow produced it.

Canonical candidate principle:

> **Generated output is candidate state, not authority.**

Operational corollary:

> **Generation creates a candidate. Adjudication creates an established result.**

This is broader than the word *pre-production*. In media, writing, design, analysis, and DraftDeck workflows, AI output may literally be pre-production. In live operational systems, however, the durable principle is that generated output remains **provisional until sufficient adjudication establishes fitness for its intended use**.

Therefore:

```text
AI GENERATION
↓
CANDIDATE OUTPUT
↓
ADJUDICATION
↓
ACCEPTED / RELEASED / AUTHORIZED RESULT
```

## Human-in-the-loop is not the constitutional primitive

The constitutional requirement is not that a human must manually review every output.

The requirement is that **the level of adjudication must be appropriate to consequence**.

Possible adjudication mechanisms include:

- deterministic validation;
- schema or constraint checks;
- source-grounding checks;
- independent model or evaluator review;
- simulation or test execution;
- policy verification;
- human review;
- explicit release authority;
- combinations of the above.

For low-consequence work, deterministic verification may be sufficient.

For higher-consequence work, independent review, stronger evidence, or human release authority may be required.

The architecture is therefore:

```text
AI OUTPUT
↓
CONSEQUENCE-APPROPRIATE ADJUDICATION
↓
RELEASE AUTHORITY
```

not:

```text
AI OUTPUT
↓
HUMAN MUST ALWAYS APPROVE
```

## Adjudication burden scales with consequence

Canonical candidate rule:

> **The burden of adjudication scales with consequence, not with confidence, fluency, or model capability.**

A polished answer is not automatically a trusted answer.

A trusted answer is not automatically released.

A released answer is not automatically authorized for every context.

The following distinctions remain separate:

```text
FLUENT
≠
CORRECT

CORRECT
≠
VERIFIED

VERIFIED
≠
RELEASED

RELEASED
≠
UNIVERSALLY AUTHORIZED
```

Additional candidate distinctions:

> **GENERATED ≠ ESTABLISHED.**

> **PRODUCED ≠ AUTHORIZED.**

> **OUTPUT ≠ VERIFIED RESULT.**

> **EVAL PASS ≠ RELEASE.**

## Release authority is distinct from generation capability

A model may be capable of generating a result without possessing authority to release that result into use.

An agent may be capable of routing work without possessing final release authority.

A validator may be capable of detecting errors without possessing authority to redefine the package.

This extends the existing BOSS separation:

> **BUILD_CAPABILITY ≠ REVIEW_CAPABILITY ≠ RELEASE_AUTHORITY.**

The system should make these roles explicit rather than allowing one capable component to silently inherit all three.

## Unified constitutional candidate

The two threads combine into one higher-order principle:

> **Governed AI requires control at both boundaries: what is admitted to capable systems and what is established from their outputs.**

A more compact form:

> **Admission governs input. Adjudication governs output. Capability governs neither by itself.**

And the strongest constitutional candidate is:

> **You do not govern AI by controlling intelligence directly. You govern the packages admitted to capable systems, the conditions under which they move, the adjudication applied to generated results, and the authority required before those results are established for use.**

This combines:
- REQUEST ≠ PACKAGE;
- CAPABILITY ≠ PERMISSION;
- CAN PROCESS ≠ MAY RECEIVE;
- GENERATED ≠ ESTABLISHED;
- PRODUCED ≠ AUTHORIZED;
- OUTPUT ≠ VERIFIED RESULT;
- EVAL PASS ≠ RELEASE.

## DraftDeck production interpretation

For DraftDeck, this architecture is operationally concrete:

```text
USER REQUEST
↓
DRAFTDECK AGENT / COUNTER
↓
PACKAGE CONSTRUCTION
↓
ADMISSION + REQUIREMENTS
↓
ROUTE TO ELIGIBLE CAPABILITIES
↓
NOTEBOOKLM / MODEL / CANVA / SVG / PPTX / OTHER TOOLS
↓
RAW GENERATED ARTIFACT
↓
BOSS REFINEMENT
↓
CANDIDATE PRODUCTION ARTIFACT
↓
QA / VERIFICATION
↓
RELEASE CANDIDATE
↓
AUTHORIZED REVIEW
↓
FINAL
```

NotebookLM output is therefore **raw pre-production**, not authority.

DraftDeck output is not final merely because it renders.

Canva output is not final merely because it looks polished.

The release state is earned by adjudication.

## Day Zero implication

Day Zero should now teach both halves of the governed AI interaction:

### Before execution
- request is not package;
- package must be constructed;
- admission precedes capability selection;
- classification precedes handler selection;
- capability does not create permission.

### After execution
- generation creates a candidate;
- candidate output must be adjudicated;
- verification burden scales with consequence;
- release authority remains distinct from generation capability.

This gives Day Zero a complete beginning-to-end control story:

```text
WHAT MAY ENTER?
↓
WHAT MAY HANDLE IT?
↓
WHAT WAS PRODUCED?
↓
WHAT EVIDENCE SUPPORTS IT?
↓
WHO / WHAT MAY ESTABLISH IT FOR USE?
```

## Status

This document remains a **Candidate Architecture Note** until formally adjudicated for promotion into the constitutional / kernel layer.

Its purpose is to preserve the combined architecture without prematurely declaring constitutional status.
