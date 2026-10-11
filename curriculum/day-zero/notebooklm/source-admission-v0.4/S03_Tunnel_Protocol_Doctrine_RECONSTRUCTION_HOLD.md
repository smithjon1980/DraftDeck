# The Tunnel Protocol Doctrine
## Source-admission reconstruction · candidate v0.4

**Authority warning:** This document is a clean consolidated *reconstruction* based on the available BOSS project lineage, earlier Day Zero handoff materials, and the current authorized Information Supply Chain framing. It is not a verbatim authentication of the historical Tunnel Protocol PDFs. Its operational controls remain proposed until the originals are compared and an accountable human approves the consolidation.

### Purpose
The Tunnel Protocol governs how an identified information package crosses from a source context into another operational context without silently changing its authority, provenance, or acceptable meaning. The tunnel is an instructional model of controlled passage, not a promise of physical security, encryption, unidirectional network topology, or actual software isolation. Technical security must be separately specified and tested.

### Invariants
1. A source must be identifiable, actually readable, appropriately authorized, and version-classified before admission.
2. The sender may transfer only declared payloads using declared transformations and destinations.
3. A manifest accompanies each substantive movement and distinguishes source from annotations.
4. No receiving system acquires hidden sender state, keys, capabilities, or independent authorization merely by receiving text.
5. The receiving system must report missing operands, unexpected content, and unavailable capabilities.
6. Movement, receipt, verification, factual correctness, and human release are separate evidence predicates.
7. Contradictions create explicit HOLD or NOT ESTABLISHED states; confidence cannot heal conflicting records.
8. Original historical or deprecated sources may be quarantined for research, but cannot silently govern current output.
9. Provenance is retained through every derivative and the original remains unchanged.
10. Qualified review is required where operations exceed the operator's competence or risk envelope.

### The six-stage operational sequence
**1 · Intake.** Identify owner, source location, exact file, version, content boundaries, rights, destination, and intended task. If source content is unavailable, report not established.

**2 · Discovery and classification.** Inventory headings, embedded instructions, competing versions, deprecated terms, potential privacy or rights limitations, and contradictions. Mark material as governing, supporting, historical, administrative, or excluded.

**3 · Tunnel boundary.** Define an admission contract: authorized payloads, forbidden source classes, transformation limits, data-handling requirements, and exit conditions. Reject unapproved material. This is a conceptual custody gate and requires actual platform controls for software enforcement.

**4 · Package and route.** Build a clean payload plus manifest, state its receiving location, retain version identifiers, and avoid mixing source text with administrative instructions. Do not replace source authority during formatting or compression.

**5 · Inspect and verify.** Confirm completeness, content fidelity, prohibited-terminology absence, and any required digest comparison. Distinguish verification of bytes from verification of interpretation or factual correctness. Record exceptions without erasure.

**6 · Authorize and establish.** Obtain accountable human admission decision; record admitted, rejected, or held status and evidence. Only after explicit clearance should the destination treat it as authorized source material. Later generated media requires its own independent verification.

### Relationship to PRIME
PRIME is the larger operational movement framework: **Package → Route → Inspect → Move → Establish Delivery**. The Tunnel Protocol specifies a tighter admission-and-custody boundary. These models overlap in function but are not one-to-one equivalences. Intake and classification precede PRIME packaging; the Tunnel boundary influences routing and permitted movement; final authorization governs when establishment can be accepted. A package can move successfully while its interpretation remains unverified.

### Relationship to PARCELS
PARCELS (Platform, Attachment, Routing, Carriage, Exchange, Language, Service) allocates architectural responsibilities. A custody boundary can appear at multiple layers. A process mnemonic does not turn these categories into literal network layers.

### NotebookLM case study
The four source candidates S01–S04 must each be assigned an identifier, classification, version, checksum, authority, and allowed role. A superseded lesson or aviation-era historical slide is **not** an admitted current teaching authority. The Gemini operator may stage the files but must not infer approval from their possession. If a source contains an unreconciled contradiction, stop ingestion of that source, report the issue, and preserve the other sources unchanged. No generation should be marked verified merely because NotebookLM accepted an upload.

### Evidence record
For each source record: SOURCE_ID, title, version, origin, SHA-256, rights statement, status, approved-by, accepted-at, target notebook, destination receipt, semantic review, and remaining issues. Record `NOT ESTABLISHED` where evidence is unavailable rather than inventing values.