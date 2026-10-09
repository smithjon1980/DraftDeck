# Authority and role reconciliation
Date: 2026-10-09
Status: Proposed resolution prepared under the author's request to resolve the discrepancy. Not promoted doctrine; not empirical evidence.

## Inspected sources
- Main: 1c5c92934422cf2ed6150ccba298aca4ebb63dc8.
- Day Zero candidate: c45804e73fbb1586546f03d57dba259e24b31c70.
- Main doctrine/logistics-framework.md: models described as freight; agents as couriers; explicit human release control.
- Main doctrine/bounded-autonomy-execution-envelope.md, sections 2, 5, 7: prior scoped permission, model as capability provider, human or governed release.
- Main doctrine/evidence-verification-architecture.md: Candidate Canonical Doctrine; consequence-sensitive verification.
- Candidate training/boss-operator-program/day-zero/00_DAY_ZERO_CONTROL.md: data/task payload, agent admission and coordination, model processing capability, applicable release authority.

## Resolution selected for the proposed research architecture
Information and task specifications are the payload. A package bounds that payload with identity, scope, constraints, destination, acceptance criteria and applicable authority. Humans supply purpose and retain accountability. Agents perform admission, coordination and handling functions within granted authority; courier is one possible function, not their complete identity. Models supply processing capability; tools supply specialized capability; runtimes supply execution environments. Verifiers assess evidence within their remit. Release requires the applicable authorization for the declared intended use.

The ordinary workflow does not ship the model itself. A separate explicit model-file transfer task could make a model artifact payload; that exception does not define the normal processing role.

PRIME remains Package → Route → Inspect → Move → Establish Delivery. Admission and output adjudication are control boundaries, not extra PRIME letters. PARCELS remains seven layers with governance across them.

## Authority wording for the revised manuscript
Work proceeds within explicitly granted authority. Outputs are evaluated against stated acceptance criteria. Release requires authorization applicable to the intended use. Prior authorization must explicitly cover any routine release performed without a new approval; execution permission alone does not grant release permission. Where governing policy reserves release to a human, the handler must obtain that human decision. A passing evaluation does not itself authorize release.

## Why this resolution
The canonical bounded-autonomy role definition already supports model-as-capability. The freight mnemonic conflates what is handled with what handles it. The candidate clarifies that distinction, but its downstream status cannot override upstream doctrine silently. This record specifies a proposed upstream correction rather than claiming that the conflict disappears through interpretation.

Human accountability and a fresh approval on every output are different requirements. Bounded prior authorization can preserve accountability, but does not cancel human-only release policies.

## Repository completion requirements
Before calling the repository conflict resolved:
1. Amend logistics-framework.md role mappings, release wording and verification-as-proof wording so evidence supports scoped claims rather than automatically establishing delivery.
2. Update doctrine/README.md in the same doctrine change set, including status and the mnemonic.
3. Reconcile PARCELS introductory shorthand and inspect dependent doctrine, active training and production source for inherited role mappings.
4. Preserve explicit human-only release controls where required; do not convert them to automatic release.
5. Preserve historical manuscript v0.4; describe the reconciled architecture in v0.5 with its proposed status.
6. Inspect the candidate architecture rationale and applicable release QA before promotion. Run applicable ontology and consistency checks; retain actual results.
7. Review the resulting doctrine change through the repository's promotion path. No canonical promotion or branch merge is established by this record.

## Tests required
- Routine result released under explicit prior release authorization and required checks.
- Same result with execution permission only: release held.
- Human-only release policy: verified candidate waits for the human decision.
- Model or agent capability without handling permission: admission held or refused according to policy.
No tests were executed in creating this record.
