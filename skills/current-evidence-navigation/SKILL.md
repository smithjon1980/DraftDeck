---
name: current-evidence-navigation
description: Before recommending a new technical or educational approach, establish the human operator's starting state and intended outcome, scout recent demonstrations and practitioner evidence, and compare feasible paths under explicit constraints. Use for REA explorations, emerging tools, new stacks, and Bioscillate research. Never treat video popularity, tool availability, or inferred feasibility as execution proof.
---

# Current-Evidence Navigation — The Human Crystal Ball

**Status:** CANDIDATE v0.1 · 2026-10-13 · human review required  
**Scope:** Research and route planning. No permission to implement, publish, install, access accounts, or release anything without the authorization appropriate to that operation.

## Constitutional proposition
The human may have observations acquired after a model's training period. Those observations provide a **new evidence lead**, not a retroactive model-training update or automatically trusted fact. The operator supplies direction and context; the agent locates and inspects current information, reconciles competing evidence, proposes bounded paths, and returns uncertainties for human judgment.

**Teaching lens:** A constraint helps locate the agent *inside the problem*, not merely restrict it. First establish position A and destination B. Then select the shortest **verified, authorized, adequate** route—not necessarily the smallest number of clicks, cheapest prototype, or fastest untested shortcut. When A or B is unknown, discover before optimizing.

## Trigger
Use when exploring a technology, workflow, methodology, integration, library, architecture, unfamiliar topic, or newly emergent practice where current sources could change the recommendation. Also use when the human says “here's what I've seen on YouTube,” supplies a source, or asks to “get up to speed” before design.

Do not launch unrequested recurring monitoring or background work. Run this research during the currently authorized task; schedule repeat searches only when the user explicitly requests scheduling.

## Step 1: Fix the navigation contract
Record:
- **A / current state:** actual skills, installed tools, demonstrated capabilities, evidence on hand, observed blockers; mark UNKNOWN where unconfirmed.
- **B / destination:** a user-observable deliverable, explicit acceptance criteria, and intended beneficiaries.
- **Operating terrain:** domain, risk, urgency, allowed external services, budget, data restrictions, time budget, user expertise.
- **Hard constraints:** permissions, data protection, legal/ethical requirements, rights/licenses, accepted technology boundaries, required human gates, declared exclusions.
- **Soft preferences:** UI choices, speed, convenience, aesthetic preferences that the user may negotiate.
- **Decision rule:** distinguish research approval, implementation approval, verification, and final release.
Ask for one missing detail only when essential; otherwise proceed with explicit assumptions that are safe and reversible.

## Step 2: Human-supplied horizon scan
Accept curated videos, repository links, practitioner comments, personal observations, articles, or examples the human has encountered. State who contributed each observation and when, if known. Do not confuse *the user has seen a demo* with *this agent has independently inspected that demo*.

Use “crystal ball” as an educational metaphor for a human's timely awareness, never for literal prediction or complete access to present events.

## Step 3: Scout live evidence in an order fitted to the territory
Available evidence channels include:
1. **Official documentation and changelogs** — APIs, compatibility, versions, limitations, licenses, security notices.
2. **Public code and test artifacts** — actual repository, commit, version, running example, issue reports, reproduction instructions.
3. **YouTube and other demonstrations** — scope of the build, dates, versions, narrated claims versus observable behavior, links to runnable code. Video *title/description/transcript only* is not the same as directly watching and inspecting a demonstration.
4. **Practitioner reports** — Reddit, technical forums, blog posts, Medium articles, issue discussions: useful for failure cases and tradeoffs, not automatically objective.
5. **Fast-moving signals** — X/Twitter, release announcements, trending posts: leads requiring further verification, not decision-grade proof on their own.
Choose channels that materially help; there is no mandatory search across every platform. Prefer recent evidence and check **publication date, actual event/date, version, and source authenticity**. Preserve the exact URL, author, date, checked-on date, and relevant claim.

## Step 4: Evidence ledger
For each significant assertion log:
- ID, A/B question, URL, author/publisher, publication/event date, access date, version/commit;
- Evidence type: official doc, executable code, observed demo, accessible transcript, user report, community experience, independent test;
- Status: **SOURCE REPORTS**, **REVIEWED**, **LOCALLY REPRODUCED**, **INDEPENDENTLY VERIFIED**, **CONTRADICTED**, **UNKNOWN**;
- What it actually establishes; what it does *not* establish; conflicting evidence; reproducible test to close the gap.
No silent promotions between states. A successful test of one predicate does not establish others. Avoid fabricated quotations, video timestamps, demos viewed, receipts, results, benchmarks, or CI statuses. See [evidence-record.md](references/evidence-record.md).

## Step 5: Chart viable routes
Generate 2–3 materially different routes when meaningful (reuse, adapt, build). For each show:
- prerequisites and dependencies;
- distance from A to B, estimated in *work*, not imaginary certainty;
- hard-constraint compliance and user-facing value;
- maintainability, control, interoperability, licensing, data stewardship and rollback;
- evidence strength and the smallest discriminating experiment.
Reject routes violating hard constraints. Prefer the path with the least **total justified effort and risk** that can satisfy the acceptance tests, not simply the least code. Mark estimates as estimates.

## Step 6: Run a minimum decisive experiment
Choose one representative test that would change the recommendation. Capture environment, versions, exact instructions, expected behavior, observed result, failure logs and reproducibility conditions. A documented plan is **NOT RUN**. A source commit is **NOT EXECUTED**. A working local route is **NOT PRODUCTION VERIFIED**. Negative results and contradictory evidence are valuable.

## Step 7: Deliver a navigation brief
Return, in order:
1. **Position A:** established facts and unknowns.
2. **Destination B:** acceptance standard.
3. **Recent evidence:** dated source links and distinctions among reports, inspected material and demonstrated function.
4. **Route options:** tradeoffs and disqualifying constraints.
5. **Recommended next bounded step:** smallest meaningful test, objective pass/fail checks, responsible reviewer.
6. **Human release state:** CANDIDATE / HOLD / APPROVED as supported by actual human decision.

## First exercise: Bioscillate adaptive assessment
**A:** Proposed Go + HTMX + PocketBase prototype; no verified end-to-end learner flow yet. Earlier notebook source sets and research frameworks exist but are not production systems.  
**B:** One self-assessment captures answers and time availability, generates an explainable competency-based pathway, stores learner state, and applies the **same rubric** to different learners. A 15-minute pathway must not falsely imply equivalence to 15 hours of practice or passing competency.  
**Constraints:** Open-source/license review, learner privacy, testable branching, documented question versions and outcomes, GitHub source authority, no unsupported scientific efficacy claims, explicit human approval for release.  
**Experiment:** Verify whether a version-pinned PocketBase-as-Go-framework route serves a server-rendered HTML question via HTMX, safely records a response, selects a next item deterministically, and produces auditable scoring against a fixed rubric. Evaluate authentication, validation and data-access boundaries. A direct HTMX request to PocketBase's JSON API should not be assumed equivalent.  
**RESEARCH HOLD:** no app behavior, license review, security review or learner outcomes are confirmed by this skill text alone.

## Rules for updating the skill
Keep this skill vendor-neutral. Update examples, tests, and sources via versioned patches; never rewrite the rule to claim a previously unobserved test occurred. Human authority remains separate from agent suggestion. When a newly found practice contradicts an older tutorial, preserve both and date the difference before updating the recommendation.
