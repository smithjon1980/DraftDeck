# D0-A04 — Authority & Handling Boundaries

**Status:** Candidate NotebookLM Source Script  
**Target:** 9–13 minute audio overview  
**Purpose:** Establish permission, handling state, HOLD, and restricted-cargo orientation.

## Opening

A system that knows how to move information still needs to answer a harder question:

Should this information move at all?

BOSS separates ability from permission.

Two canonical statements anchor this orientation:

**CAPABILITY ≠ PERMISSION.**

And:

**CAN PROCESS ≠ MAY RECEIVE.**

## The Case

It is easy to assume that the strongest available handler should receive the work.

A model may have excellent reasoning.

A tool may support the required file type.

A service may return the result faster.

Those are capability facts.

They do not establish permission.

## A Simple Scenario

Suppose an external service can summarize a confidential document perfectly.

Technically, it can process the file.

But the document owner has not authorized external transfer.

The service's capability does not erase the boundary.

The correct route is not “send it because it works.”

The package must remain within its permitted handling environment.

## Classification Before Handler Selection

A core rule is:

**Cargo classification precedes handler selection.**

First determine what kind of handling the cargo requires.

Then determine which handlers are eligible.

Not the other way around.

If you begin with a favorite tool and then stretch the package rules to justify using it, the system has reversed its authority.

## Five Handling States

At Day Zero depth, know these five states:

**STANDARD.**

**SENSITIVE.**

**RESTRICTED.**

**QUARANTINED.**

**PROHIBITED.**

These are handling states.

They are not quality ratings.

They do not tell you whether the content is good, bad, true, false, important, or unimportant.

They tell you how movement must be governed.

## HOLD Is Valid

One of the most important behaviors in BOSS is refusing to guess when required handling information is missing.

The rule is:

**Unknown handling requirements produce HOLD, not guessed routing.**

HOLD is not a punishment.

HOLD is not indecision.

HOLD is a governed state that protects the network while missing information is resolved.

## Sanitization

Sometimes a package contains more information than the destination needs.

Removing sensitive material may create a new, safer package.

But the sanitized extract is a new package with its own identity and handling state.

Sanitization does not retroactively authorize the original package.

That distinction prevents the system from pretending that a later transformation made an earlier unauthorized movement acceptable.

## Authorization Across Handoffs

Permission does not disappear when a package changes hands.

Authorization follows the cargo across every handoff.

A second handler does not gain broader authority merely because the first handler sent the package.

## Bottom Line

The network does not ask only:

“Can this be processed?”

It asks:

“May this package be received here, under these conditions, by this handler?”

Capability tells us what is possible.

Permission tells us what is allowed.

When required information is missing, HOLD.

In the next audio overview, we put these ideas into the five-stage movement protocol: PRIME.

**Next Route: PRIME — Package, Route, Inspect, Move, Establish Delivery.**
