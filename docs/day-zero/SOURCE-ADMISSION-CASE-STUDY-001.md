# Day Zero — The book that wasn't a book
Status: INSTRUCTIONAL CANDIDATE / NOT TESTED
Topic: source integrity, human–agent trust, manual-first workflow, source admission and why a file hash does not establish truth.

## Opening question
A PDF arrives with the title of a respected business book. The filename looks right and you can calculate its SHA-256. **Do you know what the book says?**

## The actual DraftDeck case
During intake 06 a 180-page PDF labeled `100m Offers Alex Hormozi` included a third-party bookstore cover and many unrelated book passages rather than coherent subject matter. Source digest `4d213ca1dc9a7762261004ff5108e1e71fb311d7e88be17171e85151ddbf2869`. It was **rejected for extraction**, and no skills were added.
The rejection file is `sources/INTAKE-006-CONTAMINATED-100M-OFFERS/source-integrity-hold.md`.

## Student exercise: manual first (15–25 minutes)
1. Inspect the *actual* file, not just its name. Record claimed title, cover and publisher attribution.
2. Read or inspect several substantive pages from opening, middle and end. Compare chapters, topics and vocabulary.
3. Describe three **observable** congruence or mismatch clues with page anchors.
4. Explain why a cryptographic checksum identifies bytes but does not establish author authenticity, correctness, rights or relevance.
5. Choose PASS, HOLD or FAIL for content congruence. State what would change the decision.
6. Role exchange: the human challenges one agent statement; agent records corrected interpretation, changes its candidate workpaper and retains the original reasoning as superseded.
7. Repeat with a known coherent permitted document. A source can pass content congruence and still remain pending human authentication.

## People–Agents–Skills–Tools quadrant
People: learner/instructor supplies intent and confirms source identity.
Agents: assistants inspect, explain and flag contradictions without asserting admission.
Skills: source-content-congruence plus book-to-skills governs repeatable decisions.
Tools: PDF reader, file hash command and later optional software.
Workflow: matches roles, permissions, observations, and a decision with a repair path.

## Observable assessment
- Pass: cites concrete contradictory pages, rejects contaminated sample, preserves source record, generates zero source-derived skills, distinguishes source hash from authentication.
- Fail: accepts cover or hash as authenticity proof, invents chapters, publishes extracted instructions from unrelated text, or obscures human correction.

## Teaching transition
Day Zero: manual inspection and human–agent interpretation.
Day One: repeatable intake checklist and source log.
Day Two: optional automated congruence sampling with human review; machine classification is advisory, not authoritative.

All records synthetic or citation-only for classroom use; do not redistribute the contaminated file. No production execution or repository promotion.
