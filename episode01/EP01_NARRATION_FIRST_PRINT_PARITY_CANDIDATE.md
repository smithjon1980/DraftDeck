# Episode 01 — narration-first editorial + 11 × 17 print production contract

**Status:** PROPOSED / REVIEW REQUIRED / NO RELEASE  
**Change date:** 2026-10-18 (America/Chicago)  
**Scope:** New BOSS Episode 01 opening and the illustrated print-magazine adaptation.  
**Repository authority:** Candidate supplement to `AGENTS.md`, `doctrine/production-contract.md`, `design-system/boss-design-contract.json`, and `doctrine/release-qa.md`; it does **not** automatically ratify or supersede those files.  
**Human direction:** The current conversation authorizes preparing a new opening manuscript, variable narration-led compositions, and repository parity review. It does **not** authorize merging, public release, or treating candidate artwork as final.

## 1. Source of truth and editorial states

We are **writing a new Episode 01 solo narration script**, not transcribing the old solo audio and not silently editing the historical teleprompter.

Keep three evidence states distinct:
1. `NEW_SCRIPT_CANDIDATE`: newly authored proposed spoken wording, derived from the current opening direction. Not recorded, not a verbatim transcript of an existing recording.
2. `SCRIPT_APPROVED`: human-approved, versioned narration text. For print production, display its exact words in source order, with no silent rewriting, shortening, manufactured quotations, or substituted summary.
3. `RECORDED_TRANSCRIPT_VERIFIED`: wording compared with an actual new recording (word-level exceptions recorded). Only at this stage may the manuscript be described as a verified transcript of the new recording.

Before approval, page proofs may use candidate script passages but must label them `SCRIPT_CANDIDATE`. Any editorial heading, footnote, reflection prompt, or image annotation not spoken in the script must be marked `EDITORIAL_APPARATUS`, not passed off as quoted narration. Do not insert old logistics/aviation/parcel framing simply because archival media contain it. Cite and preserve historical material separately where required.

## 2. New opening / narrative direction

**Opening working title:** *AI Is Art Imitating Life*. The distinction is between fluent representation, knowledge of a procedure, the conditions required to execute, and evidence that work actually occurred. The illustration *The Right Procedure, the Wrong Environment* is one downstream teaching example, **not** the whole editorial story.

Editorial order: establish the new manuscript's argument and exact spoken words → map the teaching beats → select an artwork concept for each beat → compose the typography with the artwork → render and inspect. The artwork supports the specific passage; neither the story nor its words are invented to fill a predetermined grid.

**Writing gate:** Finish and review the new complete solo script before claiming that the 48-page issue faithfully represents it. Its length and the number of illustrations may be adjusted after the full manuscript is known; do not add padding to reach a page count.

## 3. Print profile — separate from the 16:9 slide profile

- **Target deliverable:** one coherent Episode 01 PDF, provisionally **48 pages**, each **17 × 11 inches landscape** (`MediaBox = 1224 × 792 pt`). That is a target, not a source-text quota or proof of final printer acceptance.
- Keep existing 1920 × 1080 presentation slides as a separate profile; **do not stretch or recycle the slide grid** to simulate print design.
- Different spreads intentionally have different proportions of narrative and art. Text-dominant, art-dominant, integrated-caption, and full-bleed/concept compositions are available when required by the teaching beat. **Do not force the narration into a fixed text box or partition every page into equal rectangles.**
- Where narrative text must occupy most of the page, let it do so; where technical art carries the explanation, allow the image prominence to increase. Use editorial spacing, flow, alignment, text wrap, scale, and quiet whitespace to make both inhabit the same visual world.
- CAD drafting conventions are **secondary structural accents**: restrained hairlines, zones, select callouts, and compact title-plate metadata. Do not render them as big unrelated SVG-looking boxes surrounding the prose. No implied standards certification.
- Repeated artwork must reveal new information (whole assembly → component → different condition), not repeat stock panels to fill pages.
- Publication, narration, art, and CAD/annotation elements remain separately managed in source. **Narrative stays selectable text** in the PDF. No rasterized full pages or image-baked article text.

## 4. Illustration standard and brand

- Fine-line, black-ink mechanical/engineering-journal illustrations; cross-hatching, cutaways, mounted assemblies, and physically coherent relationships as appropriate.
- **Reject photorealistic floating gears**, scenic photo renders, generic wireframe placeholders, and unrelated technical illustrations.
- Original Bioscillate Operating System by Seven brand identity; white ground, black ink, canonical cyan/magenta logo accents. Use verified original logo assets; do not regenerate a replacement.
- Artwork may have its own underlying construction, but words essential to the story must be authored as live typesetting above or alongside the image, not baked into it.
- Avoid scene-making where it does not help the point. Neither technical density nor visual realism is a proxy for teaching quality.

## 5. Production sequence and gates

1. **Manuscript:** create a complete new solo script; mark status/copyright/provenance and obtain explicit wording review.
2. **Beat map:** record each sequential source passage, exact-copy range, point, required visual evidence, and any optional editorial apparatus.
3. **Art masters:** develop a coherent, limited illustration family (approximately 12 masters is a planning estimate, not an absolute requirement). Reject imagery failing art/story fidelity.
4. **Two-page proof:** produce at least one text-dominant and one art-forward 17 × 11 page using actual proposed script passages. Show them together; specifically inspect text/art integration and boxiness.
5. **Full issue:** assemble in sequence. Maintain a copy map: source script version + exact ordered passages + page assignments; detect omissions, replacements, repeated filler, and accidental additions.
6. **QA:** verify PDF page count; page `MediaBox` dimensions; selectable text; text-to-source fidelity; layout/clipping; artwork provenance; original logo; line contrast; inspection records. Visual review and a physical print test are separate.
7. **Human selection/release:** share qualified PDF and evidence for review; **no merge, publication, or production/master claim without an explicit human release decision**.

## 6. Current evidence, decisions, and unresolved items

| Item | Current disposition |
|---|---|
| Existing Episode 01 two-page v0.1/v0.2 editorial proofs | Historical experiments only, **NOT ACCEPTED AS VISUAL MASTER**. Page 2 is comparatively stronger, but the narration remains boxed and the copy is rewritten. |
| Previously recovered 3,487-word solo script/audio | **Historical, different opening/source**, not the governing new Episode 01 solo script. Preserve with its original QA state. |
| Desired opening | *AI Is Art Imitating Life* and a representation-versus-execution argument; **new final wording not yet approved**. |
| Print layout | User-directed 17 × 11 landscape and one-file issue; page count 48 target, subject to actual unabridged manuscript and print review. |
| Visual treatment | Fine-line engineering-journal art and dynamic text/art integration; the approved illustration *style direction* must not be confused with approval of a complete page. |
| New manuscript audio | NOT RECORDED / NOT VERIFIED. |
| Print proof / physical print | NEW PROOF NOT GENERATED / PRINTER ACCEPTANCE NOT TESTED. |
| Canonical logo repository hash | Follow current design-contract identity verification; do not claim a release-pinned hash without evidence. |

## 7. Parity rule

This contract is **the proposed reconciliation of the October 18 voice decisions with repository documentation**, not a substitute for a human-approved script. Until reviewed, report `REPO_PARITY_PROPOSED`, not `REPO_PARITY_APPROVED`. Do not rewrite or erase archival source, silently change the 16:9 design rules, merge this proposal, or assert that old PDF proofs are now approved.
