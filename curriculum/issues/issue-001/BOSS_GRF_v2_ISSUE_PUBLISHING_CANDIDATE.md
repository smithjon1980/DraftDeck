# BOSS Guided Reasoning & Issue Publishing Specification v2

**Status:** REBUILT CANDIDATE — NOT RATIFIED / NOT A RELEASE AUTHORIZATION  
**Issue:** `BOSS-PUB-SPEC-002` · **Date:** 2026-10-13  
**Authority:** Human BOSS publishing authority; no AI author or renderer may grant its own release.  
**Source baseline:** DraftDeck `feature/book-to-skills-intake-candidate` at `843023651fff28cad3189b2b53f03b7de5c1a7b4` (inspected); inherited candidate from `training/editorial-grf-v1` at `9d144b13f7da37570ba46dfe200f29e4a8722709`. 

## 1. Rebuild record and decision boundaries

This is a coherent rebuild, not an addendum or a merge of the divergent editorial branch. It preserves the validated *design intent* of GRF v1, but does not turn prior candidate language into ratified doctrine. Git history preserves the older candidate. The active branch's Day Zero competency rubric, podcast-manufacturing plan, branding guide and logistics doctrine take precedence when scope conflicts. The v2 editorial standard governs **form** and **publication orchestration**, never BOSS constitutional doctrine, evidence admissibility, curriculum authorization, or rights.

**Not performed:** PR #24 merge, default-branch changes, approval of module doctrine, public publication, or script lock. Changing this candidate later is a fresh coherent rebuild with source provenance, not an invisible modification of generated outputs.

## 2. Publishing unit and decomposition

An **Issue** is a versioned competency-led editorial package: one organizing question, a bounded set of claims and approved source records, a terminology gateway, four editorial movements, independent article units, assessment prompts, and medium-specific release proofs. A complete issue is an aggregation, not a prerequisite for reading an individual article.

An **Article** is a stable independently publishable unit with `issue_id`, `article_id`, `canonical_slug`, GRF mode, competency IDs, claim IDs, source manifest revision, paragraph IDs, locally answered question, review checkpoints and boundary. Articles may be published serially if their source snapshot and release package are approved. A later issue collection references those article release revisions; it does not silently rewrite them.

**Artifact derivation**:

```text
ADMITTED SOURCE RECORDS + GOVERNING DOCTRINE + WORKING COMPETENCY MAP
                         ↓
       ISSUE SOURCE MANIFEST — CANDIDATE → APPROVED SNAPSHOT
                         ↓
                AUTHORIZED LEXICON GATEWAY
                  ↙                  ↘
     GRF ARTICLE SCRIBE            PODCAST SCRIBE
       paragraph IDs             host/turn IDs
                  ↘                  ↙
             CLAIM + LEXICON COMPARISON
                  ↓
     WEB / PRINT QA         SCRIPT LOCK → TTS → AUDIO QA
                  ↘                  ↙
             DISTINCT HUMAN RELEASE EVENTS
```

Source manifest identity is recorded with its exact immutable content hash **after** approval. A hash establishes file identity only; it does not prove source authenticity, claim validity, human approval, or delivery. Each article and audio release binds to its own approved manifest and lexicon versions.

## 3. Authority hierarchy and evidence states

1. **Canonical BOSS doctrine / safety and structural-correspondence limits** — authoritative only to the extent actually confirmed and version-pinned.
2. **Approved instruction and competency anchor** — human-selected observable learner capability; unapproved rubric is WORKING.
3. **Authenticated source records** — source ID, URI/path, commit SHA where applicable, statement range, admissibility decision, licensing, classification.
4. **Issue Source Manifest** — organizes approved inputs; cannot elevate an unreviewed assertion to fact.
5. **GRF v2 / visual component contracts / lexicon gateway** — presentation constraints.
6. **Scribe drafts and generated media** — proposals without authority.

For each claim, preserve `evidence_state` from `DOCTRINAL_RULE | SOURCE_SUPPORTED | ILLUSTRATIVE | HYPOTHESIS | UNKNOWN`; `verification_status` from `VERIFIED_SOURCE | PENDING_REVIEW | NOT_ESTABLISHED | REJECTED`; and `permitted_uses` for each output. **An analogy illustrates a relationship; it does not establish a measured physical or causal equivalence.** Where relevant, keep Fact, Sensation, Choice and Unknown distinct. A model-generated claim, unsupported numerical gain, predicted outcome, or two-model agreement does not become verified evidence because it appears in a polished issue.

## 4. Mandatory Issue Source Manifest schema

Required top-level fields: `schema_id`, `manifest_id`, `issue_id`, `title`, `question`, `version`, `status`, `source_branch`, `source_commit`, `competency_anchors`, `source_registry`, `claim_registry`, `lexicon_ref`, `editorial_movements`, `article_plan`, `audio_plan`, `cross_format_matrix`, `review`, `release`.

Each claim must have stable `claim_id`, exact `statement`, `source_ids`, `evidence_state`, `verification_status`, `scope`, `boundary`, `competency_ids`, `allowed_paraphrase`, and article/audio usage declarations. Claim IDs must not be renumbered to disguise a changed claim. A substantive replacement creates a new versioned claim. Provisional learning goals remain explicitly provisional until the human approves their assessment use. Missing sources, empty claim IDs, unknown status, or withheld approval fail closed.

## 5. GRF v2 reasoning discipline

Preserve GRF v1's five candidate editorial laws as the writing contract:

1. Question before conclusion.
2. Represent the strongest reasonable case before testing it.
3. Give each claim space according to available evidence, not rhetorical force.
4. Terminate an explanation in an operator move, a bounded conclusion, or an explicitly unresolved state.
5. Label established, illustrative, speculative, and unknown material so the reader need not guess.

**Voice:** short intellectual steps; one move per paragraph; questions serve a purpose; plain-before-technical; concrete-before-abstract; define before extending; demonstrate before prescribing; bounded endings. **Default paragraph grammar:** `CLAIM → WHY → CONCRETE INSTANCE → IMPLICATION` without forcing all four beats into every short paragraph.

**GRF-A · Adjudication:** `THE QUESTION → THE CASE → PRESSURE TEST → THE STANDARD → WORKED CASE → BOTTOM LINE → NEXT ROUTE`, always with an explicit evidence boundary. **GRF-B · Operator:** `THE PROBLEM → DEFINE IT → WHY IT HAPPENS → DOES THE APPROACH HOLD? → OPERATOR MOVE → BOUNDARY → PRACTICE`. A topic can use an A/B mix if the artifact clearly declares its teaching purpose. The formats are editorial modes, not alternate sources of truth.

**Stable paragraph IDs:** `ISS01-A01-P001` and onward; use rendered numbers such as `01` only when their hidden stable ID persists in the HTML and edition manifest. Do not allow print pagination to replace canonical paragraph references. A `Pause & Consider` prompt links to the preceding paragraph range and a specific learner action. Optional response collection requires accessibility, privacy and consent design, not assumed here.

## 6. GRF semantic device to instructional-component mapping

The older twelve labels are **semantic roles**, while the newer ten features are **rendered instructional components**. A role can appear in primary prose without a box, and one component may serve multiple roles. Never auto-map by label resemblance alone. The following mapping is an authoring contract, not proof of a rendered implementation.

| GRF v1 semantic device | Default v2 rendering component(s) | Audio form | Guardrail |
|---|---|---|---|
| THE QUESTION | At the Loading Dock; Pause & Consider | Lead question; focused recall | One authentic issue problem; no fabricated testimonial |
| THE CASE | At the Loading Dock; Evidence Window | Strongest plausible case | Do not pass an illustrative case as observed fact |
| PRESSURE TEST | Inspect the Payload | Host challenges a claim and names comparator | Source, candidate and finding must remain distinguishable |
| DEFINE IT | The Working Agreement | Spoken ordinary-language definition followed by controlled term | Do not invent missing schema fields |
| THE STANDARD | Evidence Window; The Working Agreement | Host cites governing statement and limits | Exact quotations only when sourced and approved |
| WORKED CASE | At the Loading Dock; Recovery Record | Clearly identified hypothetical or reported case | Outcome/observed status explicit |
| SIGNAL | Evidence Window | Spoken source/evidence note | No numeric authority without source and denominator |
| BREAK TEST | Inspect the Payload; Choose the Route | Counterexample and falsifier | UNKNOWN cannot shortcut to execution |
| OPERATOR MOVE | Try the Handoff; Choose the Route | Listener action with bounded instructions | Measurable move, not encouragement alone |
| BOUNDARY | Before You Release; Evidence Window | Explicit `what this does not establish` passage | Verification is not release authority |
| BOTTOM LINE | Carry Forward | Short bounded conclusion | No inspirational conclusion or unsupported success claim |
| NEXT ROUTE | Carry Forward; Choose the Route | Link to next exercise/article/act | No implication that it was completed |

**Other reserved components:** `Pause & Consider` is a checkpoint; `Recovery Record` documents problem/action/obtained evidence; `Before You Release` separates verification from authority. Existing ten feature names remain exact. Do not create a thirteenth semantic label or an eleventh named visual component without a revised registry, editorial review, and downstream contract update. New GRF-A/B stage headings (e.g., THE PROBLEM) are prose headings, not new registered widgets.

## 7. Authorized Lexicon Gateway (mandatory, three tiers)

An Issue Manifest references the independent machine-readable `LEXICON-GATEWAY-001.yaml`. The gateway is applied **before drafting, after each draft, after each revision, and immediately before script lock / article release**. The lint rules work at concept-and-context level as well as raw strings.

**Tier A — Mandatory Phrasing:** exact spellings linked to concept IDs, e.g., `Issue Source Manifest`, `Authorized Lexicon Gateway`, `GRF-A`, `GRF-B`, `Creative Spark`, `Dual-Spark Architecture` (the last is a *proposed controlled term pending authoritative definition*). On first use, define each technical phrase plainly. Some terms become mandatory only when that particular concept is discussed, not in every artifact.

**Tier B — Prohibited Equivalents:** forbid misleading substitute labels when the *same controlled concept* is intended. Do not blanket-ban technically correct terms in unrelated contexts, quotations, or corrective comparisons. `AI-generated image` remains a valid literal description of an image; it is not a replacement for an exploratory `Creative Spark` process. Historical terms may appear only in labeled comparison or repository citation, not as current operative vocabulary.

**Tier C — Style and claim safety:** prevent inspirational conclusions, motive attribution to models, unsupported clinical/legal/moral diagnoses, unstated causal statistics, invented source receipts, and unfounded success language. Favor observable subject/verb/object and bounded conclusions. `NOT ESTABLISHED` must be retained where measurement is absent.

**Gateway statuses:** `LEXICAL_PASS`, `LEXICAL_FAIL`, or `HUMAN_CONTEXT_REVIEW`. Automated matching alone cannot infer intended concept in every passage; uncertainty routes to a reviewer. A gateway PASS establishes only conformance to tested constraints, not source fidelity or publishing authority.

## 8. Audio manufacturing boundary

The full issue can inform multiple audio acts, but the immediate manufacturing proof uses an approximately 750-word synthetic test fixture. **A fixture is not a human-approved public script.** Public manufacture requires a distinct exact UTF-8 script, human word approval, script SHA-256 and separately approved delivery/voice/pronunciation contract. Voice names and pronunciations are not inferred from a spelling. A provider's script-import feature is not evidence that it will speak the text verbatim. Native synthesis logs prove input and transport, not necessarily audible word correctness.

Lock states: `SOURCE_INTAKE_HOLD → SCRIPT_DRAFT → SCRIPT_REVIEW_HOLD → SCRIPT_LOCKED → SYNTHESIS_CANDIDATE → AUDIO_QA_HOLD → HUMAN_RELEASE_HOLD → RELEASED`. A content change invalidates script lock; delivery parameter edits version the manufacturing manifest separately. Each segment references its exact turn IDs; segment-only repair records prior and replacement file hashes and must inspect both joins. Audio QA requires independent transcript/alignment where feasible and human listening; an ASR match is not conclusive by itself.

## 9. Web and print rendering boundary

Canonical article content is stored as accessible structured text with stable paragraph IDs. Web output uses semantic headings, keyboard-reachable prompts, useful figure descriptions and CSS responsive columns; print uses page-numbered issue collation but preserves article and paragraph IDs. Both versions must retain source caveats adjacent to the relevant claim. White `#FFFFFF` canvas and source-controlled composition apply to the existing DraftDeck visual profile; typography, imagery, logo placement and page designs remain render-review candidates until visually accepted. React and Tailwind are authoring conveniences, not evidence of native editability in Canva. No borrowed religious copy, branding, visual trade dress or graphic assets are imported.

## 10. Cross-format verifier and release gates

A cross-format build must generate a *claim occurrence ledger* containing artifact ID, claim ID, paragraph/turn ID, text excerpt, evidence state, expected source, assessment linkage and discrepancy. Check that critical claims have coverage in every intended format, and that contextualized paraphrases are semantically accurate. Different emphases are permitted; opposite propositions, scope inflation, or unsupported certainty fail. Lexicon scanning is deterministic only for its explicitly listed patterns; semantic consistency and pedagogy require human review.

**Gate ladder:**

- `G0 SOURCE_ADMISSION`: exact admitted sources and privilege boundary recorded.
- `G1 MANIFEST_REVIEW`: competencies, claim registry, source statuses and lexicon reviewed; approved snapshot is immutable by version.
- `G2 LEXICON`: per-medium mandatory, prohibited and stylistic gates run, reviewed exceptions documented.
- `G3 CROSS_FORMAT`: shared critical claims, source support and boundaries independently compared.
- `G4 MEDIUM_QA`: article editorial/links/accessibility, print layout/proof, or TTS/ASR/voice/joins as applicable.
- `G5 HUMAN_RELEASE`: explicit approval per version, medium and distribution destination.

**Outcome vocabulary:** `PASS`, `FAIL`, `NOT_TESTED`, `NOT_ESTABLISHED`, `HOLD`. Never infer `RELEASED` from a build success, a committed file, two models agreeing, a checksum, or a test fixture. A recorded `PASS` always includes time, reviewer or process, exact artifact hash and checked scope.

## 11. Pilot-to-release progression

1. Reproduce the 750-word two-voice local speech fixture and record actual duration; track script source, speech-engine metadata, and patch isolation.
2. Human evaluates voice quality, selected `Bioscillate` pronunciation, and the correctness of the benchmark selection. A paid comparison requires separately authorized credits and API access.
3. Approve or revise the Issue 01 claim registry and lexicon definitions, then approve an exact source manifest snapshot.
4. Generate GRF-A Article 01 and Podcast Act 1 from the snapshot; the currently supplied examples remain candidates until that approval.
5. Run deterministic lint plus independent claim comparison and medium-specific tests. Human decides whether each release is permitted.
6. Release standalone articles serially and aggregate approved article revisions into a complete issue; issue and audio packaging can proceed independently once their separate gates pass.

## 12. Migration disposition

- **Carry forward:** GRF five laws, short-paragraph grammar, A/B modes, seven beats, multiple reading speeds, 12 semantic editorial roles and candidate issue spine.
- **Rebuild against current sources:** visual component mapping, logistics doctrine, human accountability, status/evidence separation, competency rubric and audio script-lock semantics.
- **Deprecate as controlling for new work:** old branch's standalone statement that amendments alone govern new devices; use a whole-specification rebuild at this unpublished stage.
- **Remain unresolved:** author confirmation of `Dual-Spark Architecture` definition, human pronunciation, evidence approval for general educational efficacy, podcast vendor benchmarking, public release authority, and production render acceptance.

**Design conclusion (not release conclusion):** One issue package can generate independently consumable publications while preserving a shared evidence boundary. That cross-format promise must be evaluated against actual approved drafts and independent verification before any claim of reliable operation.