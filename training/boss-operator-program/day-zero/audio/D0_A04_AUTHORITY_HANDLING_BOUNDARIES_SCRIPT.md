# D0-A04 — Admission Before Capability

**Target:** 12–16 minute NotebookLM audio overview

A familiar mistake in AI work sounds reasonable:

“Use the most capable model.”

But there is a question that comes before capability.

May this information go there?

At a shipping counter, the carrier does not begin with the truck.

The carrier begins with admission.

Is the shipment sufficiently declared?

Are the handling requirements known?

Is the package eligible to be accepted?

Is the destination permitted?

That gives us the first inspection in BOSS:

**Admission Inspection.**

Its question is:

> **May this package enter controlled movement?**

The possible outcomes are:

**ACCEPT.**

**HOLD.**

**REFUSE.**

HOLD matters because uncertainty is not permission.

A canonical rule is:

> **Unknown handling requirements produce HOLD, not guessed routing.**

Now consider an information example.

An external AI service may be excellent at summarizing documents.

Technically, it can process a confidential file.

But suppose the file is not permitted to leave the approved environment.

The service's capability does not authorize the transfer.

That is why:

> **CAPABILITY ≠ PERMISSION.**

And:

> **CAN PROCESS ≠ MAY RECEIVE.**

The sequence is crucial.

First classify the cargo.

Then determine eligibility.

Then select among eligible handlers.

> **Cargo classification precedes handler selection.**

That leads to another important consequence:

> **Capability is downstream from admissibility.**

At orientation depth, BOSS uses five handling states:

**STANDARD.**

**SENSITIVE.**

**RESTRICTED.**

**QUARANTINED.**

**PROHIBITED.**

These labels do not tell you whether the information is true, valuable, good, or bad.

They tell you how its movement must be governed.

This is why the shipping counter is such a useful analogy.

A carrier does not say, “We own equipment capable of carrying this, therefore we are authorized to accept it.”

Ability does not create permission.

And the same is true in information systems.

A model's context window does not create authorization.

An agent's file access does not create authorization.

An API's technical compatibility does not create authorization.

Admission comes first.

Classification comes before handler choice.

Capability is evaluated only after eligibility has been established.

In the next overview, we go behind that admission boundary and look at PRIME—the protocol that governs movement once a package is eligible to move.
