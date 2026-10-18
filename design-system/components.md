# BOSS component registry v0.1 — CANDIDATE

Status: SPECIFIED, NOT IMPLEMENTATION-VERIFIED. A component record does not prove the component is present in React, Canva, or any other target.

Every component must record identifier, purpose, required fields, allowed states and variants, token dependencies, responsive/print behavior, accessibility tests, source reference, and render acceptance evidence.

| Component | Intended role | Required inputs | Acceptance conditions |
| --- | --- | --- | --- |
| SlideCanvas | 1920 x 1080 slide root | slide identifier, content | 16:9; fixed logical dimensions; CSS viewport scaling; no clipped required copy |
| BrandMasthead | original Bioscillate identity | verified logo asset, title, metadata | no substitute artwork; proportions preserved; original source/hash identified |
| TechnicalPanel | structured editorial content | heading, body, priority | native selectable text; grid aligns; no unsupported fill or decorative cards |
| EvidenceWindow | sourced claims | claim, source, limits, classification | candidate and verified states distinct; unsupported claims flagged |
| SequenceDiagram | process and branching | labeled nodes, directed relations | relationships preserved; accessible textual alternative; no invented steps |
| PauseAndConsider | learner reflection rail | question, optional notes area | no invented answers; visible at the intended slide scale |
| ReleaseStatus | human decision state | state, evidence record, approval identity | structural success never equates to visual approval or release |

Implementation adapters may use the same semantic contracts without sharing layout code. Website content must reflow responsively; slides retain their fixed composition. Editorial copy remains live HTML.
