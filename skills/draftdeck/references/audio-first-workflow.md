# Audio-first BOSS lesson production

Use this production order for the author's BOSS lesson workflow. Preserve the selected course day. Order of operations belongs in Day Zero; round numbers describe production attempts.

## Artifact dependencies

| Stage | Required input | Output and evidence | Next permitted production step |
| --- | --- | --- | --- |
| Source preparation | Actual reviewed lesson sources, objectives, current doctrine, and approved examples | Versioned source inventory; roles distinguished from production instructions | Long-form podcast generation |
| Audio generation | Verified selected sources and recorded audio instructions | Actual downloaded audio; hash, measured runtime, source list, actual prompt/settings | Transcription of the actual recording |
| Transcription | Readable actual audio and an available transcription mechanism | Verbatim transcript with timestamps, actual coverage, provider/method, and uncertain speech | Transcript and source review |
| Transcript review | Recording, transcript, approved sources | Raw transcript retained; separate correction log and reviewed teaching text; review scope recorded | Video script and visual outline |
| Script preparation | Reviewed teaching text, correction log, sources, and objectives | Versioned narration and scene/slide map tracing claims to transcript timestamps and source sections | Video, slides, and infographic generation |
| Media inspection | Actual exported artifacts and their approved parent script/outline | Separate visual, narration, correspondence, and execution evidence | Scoped acceptance under applicable human authority |

Keep source authority intact. A transcript establishes what was spoken within its checked coverage; it does not establish that the statements are true. Do not promote generated speech into doctrine merely because the transcription is accurate. Preserve raw wording separately from editorial corrections. Do not overwrite raw speech to make the podcast appear compliant. Correct unsupported claims against approved sources before deriving the video script; regenerate affected audio when the intended audio release still contains material defects.

Record each derived artifact's parent version or hash, source sections, transcript time ranges, transformations, and review state. Map adaptations by teaching purpose rather than forcing identical sentences across media. Keep full message schemas, illustrative excerpts, shared frames, tag fields, and status namespaces distinct.

## Audio generation instructions

Use the supported NotebookLM/Gemini Notebook Audio Overview controls. For an English long-form podcast, choose Deep Dive and Longer when available; record the actual selected settings and measured export duration. Do not promise a fixed 60-minute runtime from a Longer setting. If a required duration exceeds the tool's output, identify the actual shortfall and prepare bounded episodes or a separately authored audio production path within the owner's scope.

Prompt the hosts to develop the lesson's approved reasoning, examples, practice pauses, explicit unknowns, dependency ordering, evidence scope, and human authority. Keep production directions separate from lesson facts. Preserve exact canonical statements and calculations. Exclude retired embedded plates and rejected generated artifacts from the selected lesson sources.

Official controls checked 2026-10-09: https://support.google.com/gemininotebook/answer/16212820?hl=en . Recheck changing controls rather than assuming availability.

## Transcript acquisition

Download the podcast and transcribe its actual audio with the configured backend. If no backend is configured, report the specific unavailable step; keep transcript status UNKNOWN and hold the dependent script acceptance/generation step. Do not silently install large models, send audio to a new provider, or claim a transcript exists because a podcast was generated.

NotebookLM supports transcribing imported local audio into a source. When that route is explicitly used, treat its text as a platform-generated transcript candidate; verify coverage and exact wording against the recording before claiming audio fidelity. Keep raw imported transcript candidates outside the accepted visual-production source set until reviewed. Use a separate review notebook when needed to avoid mixing unreviewed text into active production.

Official import behavior checked 2026-10-09: https://support.google.com/gemininotebook/answer/16215270?hl=en . A downloaded Audio Overview does not by itself establish a transcript or export capability.

Use speaker labels only when the voices are actually distinguishable. Preserve repetitions and uncertain speech. Record missing spans; never reconstruct them from source text, frames, or desired narration. A partial transcript may support only the specifically reviewed segment; it does not unlock the entire lesson.

## Fresh notebook transition

Preserve the first-round notebook and evidence. Prepare the reviewed source packet, then create one distinct production target after duplicate checking. Do not clone the prior notebook wholesale. Generate the podcast first in the new notebook. After transcript review, hand off the reviewed teaching text and approved video script as explicit, versioned sources; exclude raw rejected transcripts, predecessor plates, and workflow instructions from lesson generation.

Verify actual source selection and ingestion at each transition. Transport, ingestion, dispatch, generation, review, and release are separate outcomes. A reset is input isolation, not evidence of repair. If the same defect returns, inspect the source packet and settings before another reset; do not create identical notebooks indefinitely.

## Current-action rule

Choose the first unsatisfied dependency as the next action. If sources are verified but audio is absent, prepare the long-form audio prompt. If audio exists but a checked transcript does not, obtain and review the transcript. If checked transcript exists but the script does not, derive and review the script. If a video has already been generated prematurely, preserve it as a candidate and compare it later; do not require deletion or start another course day.

Continue independent permitted work, such as inventorying sources, diagnosing old exports, preparing design components, or reconstructing an explicitly requested reference. Label those results with their actual draft/reconstruction scope. Honor explicit owner exceptions without claiming that omitted evidence was verified.
