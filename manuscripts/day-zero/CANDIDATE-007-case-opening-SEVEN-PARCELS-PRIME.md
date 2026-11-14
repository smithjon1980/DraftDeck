# Day Zero — Solve for the Unknown
## Consulting-case manuscript · distributed-framework revision

**Candidate:** 007, revision B · November 14, 2026  
**Status:** Editorial working candidate; human approval pending.  
**Scope:** Revised opening paragraphs 001–002 and provisional insertion passages for later narrative beats. These are **not** a completed 250-paragraph manuscript.  
**Comparison baseline:** `manuscripts/day-zero/CANDIDATE-006-100-paragraphs.txt`, retained unchanged on `main`.

### Scene 01 — The Order Everyone Thought Was Finished

**001.** The owner of Main Street Copy had a convincing argument for buying another printer. Orders were arriving, employees were working late, and customers were calling about jobs that should have been finished. Yet every new piece of equipment seemed to create one more place where the owner had to intervene. When a consultant visited the shop, the owner opened a spreadsheet showing an increase in daily transactions and said, “Demand isn't our problem. We just need more capacity.” The consultant studied the figures without agreeing. More orders might explain the pressure, but they could not explain why finished jobs kept returning for corrections. Before recommending equipment, staffing, or automation, the consultant needed to understand what the shop meant by *finished*, where the delays actually occurred, and what evidence would distinguish a capacity shortage from a failure of coordination.

**002.** Together they selected a recent order that looked ordinary: a customer had submitted a document for printing, binding, packing, and shipment. The job ticket was marked complete, the shipping label existed, and the owner remembered approving the work. Yet the customer had received a different document version and could not confirm delivery of the replacement. The consultant did not announce a solution. Instead, the consultant asked to see the original request, the approved file, the production record, and the receiving evidence. Each record described a different part of the same job, and some were missing. The lesson begins with that gap: a persuasive status report is not necessarily an accurate account of what happened. The learner's first assignment is to identify what can be established, what remains unknown, and which additional record would actually change the next decision.

### Placement decisions for the full 250-paragraph sequence

These positions are **proposed anchors**, subject to reconciling the continuous narrative and auditing the actual 250 paragraphs. Do not insert acronym explanations into paragraph 001 or 002.

| Framework | Provisional anchor | Narrative reason | Governing distinction |
|---|---|---|---|
| **SEVEN** — Survey, Evaluate, Validate, Execute, Normalize | **016** (first diagnostic meeting) | The learner has encountered a real problem and is ready to see how a consultant proceeds | Governs the full consulting inquiry |
| **PRIME** — Package, Route, Inspect, Move, Establish Delivery | **052** (walk one job through its handoffs) | A traceable order makes the movement protocol concrete | Governs bounded movement and evidence of delivery |
| **PARCELS** — Platform, Attachment, Routing, Carriage, Exchange, Language, Service | **076** (classify recurring failures) | Multiple observed defects create a reason to locate structural responsibility | Maps where responsibilities and failures belong |

### Provisional insertion passage — SEVEN (target paragraph 016)

**016.** At the next meeting, the owner asked when the consultant would present a proposal. “After we know what we are proposing to fix,” the consultant answered. The work would follow **SEVEN: Survey, Evaluate, Validate, Execute, Normalize**. Survey establishes the client's objective and the actual records; Evaluate compares the plausible causes and the cost of leaving them unresolved; Validate tests the explanation against the available evidence; Execute is confined to changes the owner has authorized; and Normalize establishes an inspected, repeatable procedure rather than a one-time rescue. These stages are not a promise that every investigation ends in a software sale. They provide a disciplined way to discover when a manual correction, a process redesign, a small automation, or no intervention at all is justified.

### Provisional insertion passage — PRIME (target paragraph 052)

**052.** The consultant placed the job ticket beside the production and shipping records and traced the order from one handoff to the next. The sequence followed **PRIME: Package, Route, Inspect, Move, Establish Delivery**. Package identified the correct customer request, approved file, and required metadata. Route selected the appropriate handling destination and conditions. Inspect checked the version, instructions, permissions, and condition before movement. Move covered the authorized processing and handoffs. Establish Delivery required evidence that the intended receiver accepted the correct result. A shipping label alone proved neither carrier custody nor customer receipt. The learner could now see why completing an activity and establishing an outcome are separate claims.

### Provisional insertion passage — PARCELS (target paragraph 076)

**076.** After tracing several orders, the consultant could separate failures that had previously been reported as a single complaint: “Our workflow is broken.” The **PARCELS** architecture names seven responsibility layers: **Platform, Attachment, Routing, Carriage, Exchange, Language, and Service**. A printer or network outage belongs primarily to Platform; a wrong or altered source file points to Attachment; an unsuitable destination points to Routing; a failed retry or movement rule points to Carriage; a lost handoff record points to Exchange; ambiguous job specifications point to Language; and unmet acceptance conditions point to Service. These are structural homes, not seven stations through which every order must travel. The same incident may affect several layers, but locating its primary cause prevents the team from treating every symptom as a reason to replace the whole system.

### Sample scripted exchange (excluded from paragraph count)

**Owner:** “Can you just tell me which software we should buy?”

**Consultant:** “Not yet. We have evidence that jobs are returning, but we haven't established whether the cause is capacity, instructions, handoffs, or acceptance.”

**Owner:** “So what would you recommend first?”

**Consultant:** “A bounded review of one order, with a record of what actually happened and a decision about what deserves testing.”

### Editorial and counting controls

1. The five numbered prose passages are **candidate replacements or insertions**, not a contiguous manuscript. The numbers 016, 052, and 076 reserve proposed locations only.
2. The governing requirement remains **250 substantive instructional paragraphs** in the eventual complete Day Zero manuscript. Scripted dialogue, reflection prompts, quote callouts, tables, citations, research prompts, and exhibits are **outside** that count.
3. New prose must resolve continuity and paragraph counts when assembled; do not claim that the old 100 and new 150 have already been integrated.
4. Every paragraph will have its own research prompt and target of 1–3 **claim-verified** citations; verification is not established by this candidate. The Main Street Copy conversation is **fictional instruction**, not observed client data.
5. The source hierarchy is unchanged. **SEVEN is the consulting discipline; PRIME is the movement protocol; PARCELS is the structural architecture.** IPOS and the evidence chain remain distinct teaching lenses. HAVE governs human authorization and verified execution.
6. No approved manuscript, production workflow, or publication release is changed by this review candidate.

### Repository sources

- `skills/draftdeck/SKILL.md` — SEVEN
- `doctrine/prime-process.md` — PRIME
- `doctrine/parcels-layer-architecture.md` — PARCELS
- `doctrine/main-street-copy-case-model.md` — reference case
- `doctrine/BOSS_V4_CONSULTING_AGENCY_ARCHITECTURE_CANDIDATE.md` — candidate consulting architecture
