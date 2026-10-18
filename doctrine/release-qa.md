# BOSS / DraftDeck release QA — current candidate

**Required review protocol:** `doctrine/visual-evidence-gate.md`. A review candidate without reference/render screenshots, annotated comparison and a recorded decision is **HOLD**, not visually qualified. For CAD-framed work, the visible grid, zone markers and technical title plate are visual acceptance criteria; no claim of ANSI/ISO certification is implied.

These are **separate** evidence levels, not interchangeable approvals:
1. Source admission: original reference and brand asset identity, exact copy, manifest, and approved design rules.
2. Structural build: scene, dimensions, named token use, component APIs, layers, hash, and non-raster editorial text.
3. Rendered visual review: source-story match, correct original logo, composition, typography, clipping, overlap, line contrast, and reflective question/notes.
4. Target adapter review: imported page size, independent text and artwork objects, legibility, and fidelity in the actual destination.
5. Hands-on edit test: authorized human edits, saves, and reopens the target artifact.
6. Release authorization: a separate explicit human decision with scope, evidence, and exceptions.

Each level is PASS, FAIL, or NOT_TESTED; lower-level success never implies the next level. Historical Canva evidence may guide the testing procedure but does not verify any newly imported deck. Canva import routes may change; discover and verify the actual available route.

Default instructional slide is 1920 x 1080. Responsive web and print must use their own approved layout contracts. Avoid obsolete metaphors, substituted brand assets, invented source copy, rasterized editorial text, and unsupported claims of compliance. The canonical logo binary/hash is still unverified in the design contract and is therefore a release HOLD for new brand-master approval.

A failed visual candidate is repaired and rerendered; recommendation is not selection, and selection is not final release. Save original source identities, build records, visual evidence, outstanding unknowns, and explicit approver record.
