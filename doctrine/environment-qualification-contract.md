# Environment Qualification Contract — Candidate

**Order:** BOSS-ARCH-BRANCH-001  
**Status:** CANDIDATE / NOT RATIFIED  
**Authority:** Subordinate to `bounded-autonomy-execution-envelope.md`, Shipping Label requirements, Evidence & Verification Architecture, and existing release gates.  
**Purpose:** Establish how BOSS determines whether a specific execution environment can safely and reproducibly perform a bounded package.

## 1. Boundary and ownership

- **Execution Envelope:** declares permitted autonomy and required environmental guarantees.
- **Shipping Label:** carries the package's declared capability, placement, handling, and verification requirements.
- **Environment Qualification:** tests the proposed runtime against those requirements and records evidence.
- **Execution Receipt:** records actual behavior of an individual attempt, whether it passes or fails.
- **Release Authority:** remains independent of acquisition, environment readiness, job success, and verification.

Environment selection and execution routing may use qualification evidence. They may never bypass required human authorization or restricted-cargo handling. PARCELS retains its seven-layer ownership. This contract is a specialization, not an eighth layer or a new governing framework.

## 2. Minimum environment qualification record

| Field | Requirement |
|---|---|
| QUALIFICATION_ID | Stable identifier with version |
| PACKAGE_ID / RUN_ID | Bounded work reference and attempt ID |
| SOURCE_URI / SOURCE_REVISION | Exact public or authorized source and resolved immutable revision when supported |
| SOURCE_LICENSE / ADMISSION | Applicable rights and source-admission disposition |
| ENVIRONMENT_ID | Provider, runtime profile, image/build identifier, architecture |
| EXECUTION_ENVELOPE_ID | Versioned envelope/permission basis |
| SHIPPING_LABEL_ID | Linked package label and required capabilities |
| JOB_OR_SESSION | Bounded job or resumable session classification |
| TOOLCHAIN / DEPENDENCY_LOCK | Executable, package versions, ABI/runtime dependencies and build inputs |
| NETWORK / FS / PORTS / HARDWARE | Declared and observed accessible resources, including optional GPU |
| CREDENTIAL_BOUNDARY | Identity, least privilege, proxy policy, redaction and expiry |
| LIMITS | CPU, memory, time, filesystem, output and cost ceilings as applicable |
| CONTINUITY | Durable artifacts, checkpoints, expiry, resume preconditions and reconciliation, or NOT_APPLICABLE |
| TEST_FIXTURE / ACCEPTANCE | Source and expected checks for workload-representative execution |
| EVIDENCE_LINKS / SHA256 | Logs, artifact locations, integrity values and verifier |
| RESULTS / UNKNOWNS | Per-stage dispositions; deviations and missing evidence |
| RELEASE_GATE | Explicit HOLD unless separately authorized |

Do not imply fields are independently verified when populated solely by the producing runtime. A digest proves byte consistency against the stated digest, not independent source authenticity.

## 3. Lifecycle and gate states

```text
SOURCE_IDENTIFIED
  -> SOURCE_ADMITTED
  -> ACQUIRED
  -> BUILT
  -> ENVIRONMENT_QUALIFIED
  -> TASK_EXECUTED
  -> OUTPUT_VERIFIED
  -> DELIVERY_ESTABLISHED
  -> RELEASE_AUTHORIZED (separate authority)
```

Each arrow requires appropriate evidence; failed, missing, stale, or unauthorized evidence produces HOLD / RECONCILE / REFUSE as governed by existing doctrine. A job's green status does not skip intermediate stages. For a session, checkpoint restore must also revalidate current authorization and state.

## 4. Required acceptance tests

1. **Identity:** Record and verify source revision, executable identity and architecture.
2. **Compatibility:** Prove required tools, dependencies and hardware are present for the stated workload.
3. **Boundary enforcement:** Demonstrate least-privilege filesystem/network/credential restrictions appropriate to consequence. Use an authorization broker that validates requested action and destination, not merely a token-hiding proxy.
4. **Execution:** Run a deterministic or explicitly scored representative fixture, record exit status and output.
5. **Evidence custody:** Hash artifacts; record provenance and retention; enable independent reconstruction/checking.
6. **Failure isolation:** Exercise timeout and error reporting without invalidating authoritative orchestration state.
7. **Continuity where required:** Demonstrate suspend/checkpoint/restore/reconcile on a new worker and identify when resume must HOLD.
8. **Drift and startup:** Report reproducibility and cold-start metrics where material; do not promote performance claims from an unmeasured test.
9. **Independent verification:** Separate production of the output from its acceptance according to the Verification Profile.

For a short-lived acquisition job, session-resume tests may be NOT_APPLICABLE with a reason; for a background agent session they cannot be silently omitted.

## 5. BOSS-SOURCE-ACQ evidence mapping

**001 — Public Whisper configuration transport:** GitHub Actions run `38239098210` reported success; its public `openai/whisper-tiny/config.json` fixture was acquired, hashed, schema-checked, packaged and uploaded. This qualifies the observed **bounded transport path only**. It does not qualify speech-to-text accuracy, offline runtime compatibility, or general model acquisition.

**002 — Whisper CPU executable/model/transcription:** `.github/workflows/hf-whisper-cpu-bundle.yml` is a separate workload. Its build, model acquisition, CPU transcription, dependencies, and ZIP receipt require evidence from the actual run, independently inspected before an admission claim. A moving source tip is recorded at acquisition time and must be reviewed; it is not intrinsically pre-approved.

## 6. Implementation neutrality and minimum sufficient architecture

Use existing bounded runners where appropriate (for example GitHub Actions for finite tests). Consider warm dev boxes, session snapshots, specialized hardware, or orchestration services only when the package demonstrates those needs. Modal and other studied platforms remain references or candidate adapters, never implied dependencies.

Environment state is not governing state. Runtime destruction must not destroy authoritative progress; a saved filesystem is not proof that resumed authority remains valid.

## 7. Change and teaching rules

A change to this candidate affecting canonical doctrine must update `doctrine/README.md` and pass the existing ontology guard. Day Zero NotebookLM source-admission packages and historical HOLD records must not be overwritten. A new instructional unit requires a separately admitted candidate and must distinguish observed transport success from not-yet-verified execution.

**Non-negotiable:** DECLARED CAPABILITY ≠ QUALIFIED ENVIRONMENT ≠ VERIFIED EXECUTION ≠ AUTHORIZED RELEASE.
