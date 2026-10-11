# DraftDeck Studio — DD-006 bootstrap

1. Install Node + PNPM. From repo root: `pnpm install`.
2. Put the verified text-free STORY image at `apps/studio/public/approved-assets/ep01-workstation.png`.
3. Run `pnpm dev`, view localhost:3000. Until asset admission the image is missing, by design.
4. Supply Plasmic Project ID and public token in `.env.local`; registration is defined in `plasmic-init.ts`, but must be loaded by an actual Plasmic editor integration before claiming components appear in Plasmic.
5. Verify 1920×1080 screenshot, text collision, asset provenance, story correspondence, exact logo and release tests before exporting.

No styling props are registered. Caveat: Plasmic can still style its outer wrappers, so the full slide composition must remain inside the governed React code and undergo independent screenshot-based release validation. **This is a source bootstrap, not a tested render.**
