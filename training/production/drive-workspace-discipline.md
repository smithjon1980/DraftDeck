# BOSS Operator Program — Drive Workspace Discipline

**Status:** Locked (operational)
**Owner:** BOSS / Seven
**Governing architecture:** training/production-architecture.md
**Governs:** the Google Drive production workspace for the BOSS Information Logistics Operator Program. GitHub remains the canonical system of record for doctrine and controlled text; Google Drive is the production workspace and NotebookLM staging environment.

---

## 1. The Three States

```text
BOSS_OPERATOR_PROGRAM/
├── 01_SOURCE/
├── 02_WIP/
└── 03_FINALS/
```

> **SOURCE = what we are allowed to build from. WIP = what we are currently transforming. FINALS = what has passed review and is ready to use.**

The state discipline behind the folder names:

> **Never modify the source. Never confuse a draft with a deliverable. Never put something in Finals until it has earned that state.**

## 2. The Movement Rule

```text
SOURCE
   │
   │ copy / compile
   ▼
WIP
   │
   │ adjudicate + refine + verify
   ▼
FINALS
```

And never WIP → SOURCE, unless the artifact is formally adopted as a new controlled reference through the GitHub process (branch → guarded PR → review → merge). Otherwise yesterday's generated idea quietly becomes tomorrow's "source."

**NotebookLM output is always WIP.** So are Canva drafts, DraftDeck builds, rough podcast scripts, and generated infographics. None become SOURCE merely because an AI created them.

## 3. Filename Convention

```text
BOSS_M01_SRC_PACKAGE_v1.0
BOSS_M01_WIP_DECK_v0.4
BOSS_M01_WIP_PODCAST_SCRIPT_v0.7
BOSS_M01_FINAL_DECK_v1.0
BOSS_M01_FINAL_PODCAST_v1.0
```

- **SRC** = approved input
- **WIP** = production state
- **FINAL** = approved output

Folder and filename both declare the artifact's state. Program-level files carry no module segment (`BOSS_SRC_...` / `BOSS_FINAL_...`).

## 4. Structure

### 01_SOURCE (approved inputs and reference only)

```text
00_PROGRAM_CONTROL/          production-architecture, plan-of-instruction,
                             guided-reasoning-format, source-authority,
                             visual-and-terminology-standard
01_DOCTRINE/                 compiled doctrine references for training
02_SHARED_TRAINING_REFERENCE/ operator-glossary, resource-capability-reference,
                             qualification-standard, composition-standard
10_MODULE_01_PACKAGE_OPERATIONS/ … 70_MODULE_07_NETWORK_ORCHESTRATION/
                             per-module curated source packages
                             (MODULE_SOURCE, PODCAST_BRIEF, SLIDE_DECK_BRIEF,
                             WORKBOOK_AND_QUIZ_BRIEF, INFOGRAPHIC_BRIEF)
```

01_SOURCE is the only tree used when feeding NotebookLM.

### 02_WIP (per module, by medium)

```text
{XX}_MODULE_*/
├── 01_NOTEBOOKLM_OUTPUT/
├── 02_EDITORIAL_REFINEMENT/
├── 03_SLIDES/
├── 04_INFOGRAPHICS/
├── 05_AUDIO/
├── 06_STUDENT_MATERIAL/
├── 07_INSTRUCTOR_MATERIAL/
├── 08_WORKBOOK/
├── 09_ASSESSMENT/
└── 10_QA/
```

Subfolders for a module are instantiated when that module enters production; empty module slots hold only the module directory.

### 03_FINALS (released or release-ready only)

```text
00_PROGRAM/                  Instructor_Guide, Student_Operator_Manual, Workbook,
                             Operator_Glossary, Qualification_Standard,
                             Final_Integrated_Simulation
{XX}_MODULE_*/               Podcast, Slides, Infographics (Square/Portrait/Landscape),
                             Workbook, Quiz, Student_Guide, Instructor_Guide,
                             Release_Ledger
```

No exploratory NotebookLM output, no rough drafts, no alternative images, no version-suffix sprawl. Finals means released or release-ready.

## 5. NotebookLM Staging Rule

For a module: select its curated files from `01_SOURCE/{XX}_MODULE_*` plus required shared source documents. NotebookLM generates against that set. Outputs land in `02_WIP/{XX}_MODULE_*/01_NOTEBOOKLM_OUTPUT/`, are refined through the remaining WIP lanes, and reach `03_FINALS/` only after cross-media QA and a release-ledger entry.

> **NotebookLM is the spark, not the authority.**

## 6. Relationship to GitHub

Controlled text (doctrine, program control documents, module sources, canonical scripts) lives in GitHub and moves by guarded PR. Drive mirrors approved controlled text into 01_SOURCE for production use; it never originates controlled text. If a WIP artifact earns adoption as a reference, it enters GitHub first, then returns to 01_SOURCE.
