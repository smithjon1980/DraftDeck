# BOSS Open Tool Trial — execution evidence

**Trial run:** [GitHub Actions #39249523036](https://github.com/smithjon1980/DraftDeck/actions/runs/39249523036)  
**State:** ACTUAL SYNTHETIC TEST EXECUTED / HUMAN VISUAL REVIEWED AS CANDIDATE / NO PRODUCTION APPROVAL.  
**Audience:** DraftDeck maintainers; these are narrowly scoped operational findings, not platform rankings.

## Penpot token compatibility

**Result: STATIC STRUCTURAL PASS / REAL APP IMPORT NOT TESTED.**

The offline Python check compared the proposed Penpot/W3C DTCG-compatible `penpot-boss-tokens.json` values against DraftDeck's actual `design-system/tokens/tokens.css`.

- Exact palette: ground `#FFFFFF`, ink `#000000`, cyan `#00BCEB`, magenta `#E30074`.
- Exact 1920×1080 dimension candidate.
- Negative tests reject wrong cyan, invalid slide width and missing magenta.
- No Penpot account sign-in, actual import, token export, UI-edit, CSS export, or React JSX handoff occurred.

**Next gate:** Open Penpot with a synthetic design, import token JSON, inspect resulting values, export tokens, compare values/hashes and capture proof. No private narration or unapproved logo should be uploaded.

## Excalidraw Mermaid conversion

**Result: EDITABLE ELEMENT CONVERSION PASS / BOSS VISUAL FIT FAIL / RELEASE HOLD.**

Browser test took `sample-msc.mmd` through official `@excalidraw/mermaid-to-excalidraw@2.2.2` and `@excalidraw/excalidraw@0.18.1`. A mounted React editor was inspected through its Excalidraw scene API.

Verified results:

- **17 mounted scene elements** exactly match conversion output.
- **4 rectangles, 1 diamond, 5 arrows, 7 text objects**.
- The synthetic **HOLD** label remains present.
- React editor API is callable and no unhandled browser exceptions were observed.
- A 1600×900 screenshot is included in the CI artifact `boss-open-tool-excalidraw-smoke` alongside `proof/evidence.json` and generated npm lockfile.

Human visual inspection of the screenshot found **text crossing or clipping the border** for the request, HOLD clarification, work-order and production labels. The handwritten type and loose technical alignment also **do not match** the BOSS Tesla-screen/CAD/ISO editorial hierarchy. These flaws are **not detected** by the current API/structural smoke test and must not be masked by its green status.

**Decision:** Excalidraw may be useful as a separate learner storyboard/idea sketchpad, particularly for sketching Mermaid-derived concepts. It is **not promoted to the master Episode 01 slide compositor**, and must not replace PR #77's React native-text Diagram Composer. A targeted visual fix could be attempted later if actual student exercises demand it.

## Follow-on decision

- **Penpot:** Recommend one hands-on DTCG import/export and component handoff test, no paid hosting.
- **Excalidraw:** Tested compatibility; **defer production integration**, optional educational sketchpad.
- **NocoDB, n8n licensing:** flag redistribution/external builder rights before LMS integration.
- **PostHog, Coolify, Supabase, Cal.com, Documenso, Immich:** no service deployment or live capability test authorized here. The ten-tool README records why each is deferred or has a role.

No course data, brand-master replacement, credentials, persistent service, Baseten inference, or paid cloud resources were touched. Run success is **not** permission to merge an unapproved UX into production or migrate architecture.
