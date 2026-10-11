# BOSS-D0-NLM-003 — A-Tier Source Transfer Receipt

Status: **SEVEN TEXT TRANSFERS MATCH / CANDIDATE SOURCE AUTHORITY ONLY / NOTEBOOKLM INGESTION HOLD**

The seven A-tier files in `feature/boss-day-zero-seven-episode-transition` were populated from connected Google Drive v2.0 source documents, without inserted new curriculum text. A separate follow-up compared each complete Google Drive connector text response with the GitHub connector read-back string using exact JavaScript string equality; all seven comparisons returned true.

| EP | Drive document ID | Git blob SHA-1 | Connector character count |
|---|---|---|---:|
| 01 | 1rXB18l10eOpxMGM4xhnXr5nYFGbZ1odKggQJwlA_g6g | 6059463f0fc24d880ef890731e8d1ba010d44aa0 | 3229 |
| 02 | 1mPj_lvsRzEggQHu1va8umCDgjd9UFW65N-JWKT4PDCw | 9b386e6c9a2bd1c4a1575c22c5b0fb4a40844a54 | 3168 |
| 03 | 1Wo5O5ppafAmLsCpo_yB0EKqxIkpzkt1ZZT8zgUPlw4g | aab10ce7986be4b0e6bb7d653806cb97ba0bc333 | 3351 |
| 04 | 1BQBV2DVkF9IrQra3j_obSThg0jgjvhEnAyPpP_Wv6-A | aacd6263b14de98a0865be8a5c1986e80450e6d0 | 3435 |
| 05 | 1S6FwhYKIkIKzlxwSwPy_QFsW35KLnthZRbFBRbfP5RQ | 6054ed00d38295588125b64ab998ada9a83e2059 | 3849 |
| 06 | 1vmQ4rVODt7zAQzJO9rhIqrGR44X2m3ybFAjqBMv1A_k | 679a7d32f14a42270f30ff4bd2c5d889c27f29ab | 3327 |
| 07 | 124hi9tX3fLhvfO_gzQvaVUFpoUyYGAuJQFW-rgPBRr0 | 6a82fb7a497e0f6a5aa84af0fec7981e22c00957 | 2998 |

**Scope qualification:** The equality is between text returned by the Google Drive connector and GitHub connector, not raw-byte equality of Google Docs internal representation. No UTF-8 file SHA-256 manifest has yet been calculated independently; the table contains Git SHA-1 blob identifiers, not SHA-256. The Drive documents mark themselves *candidate training material*, not controlled release. The B- and C-tier files remain unmodified. NotebookLM, PR #42, n8n runtime, and Google Cloud credential provisioning remain on HOLD.

Next gate: generate a SHA-256 manifest from exact committed GitHub UTF-8 bytes, reconcile the B-tier topic titles with the admitted A-tier episode names without modifying A-tier text, and seek separate NotebookLM source-admission authorization.
