# ToG 1 — Constitutional Commitments: intake record

**Filed:** 2026-10-25 by Grok Bot (agent) for the owner, Kyle Alexander Steen · **Branch:** `research/tog1-filed` off `main` @ `fdec378a` · **PR:** PR_PLACEHOLDER

## What this is

The owner supplied ToG 1 (Baseline, x3, x6, x9 and x12) as five zip files on 2026-10-25. They were produced **outside this repository**. Provenance is as the files state: every cycle says it was prepared by **Perplexity (AI assistant)** as producer and recorder, with **KyleAlexanderSteen** as owner and decision authority, against charter GAIA-GOV-TOG-001 v0.1.0 §4.1–§4.11 at repository snapshot `fdec378a`. Grok Bot did not write, edit or re-run any of it. Each zip was unpacked into its folder below and the files are **byte-identical** to the zip contents (checked with `diff -r` against a separate extraction; every zip also passed `unzip -t`).

| Cycle | Folder | Zip SHA-256 | Zip bytes | Files | Unpacked bytes |
|---|---|---|---|---|---|
| Baseline | `Baseline/` | `a28520bedbe86d000805dfb4e318d2cc4e153b8a6730aecb830ad482b3dbd4e7` | 504,424 | 40 | 4,438,083 |
| x3 | `x3/` | `a16e2f16d9876150ecaea6d4551bf01cc3e6b16d97a3e751b0d1206410a79f28` | 543,653 | 70 | 6,448,120 |
| x6 | `x6/` | `e2102fa2063aa0f15fd7b3ecc1006dc89c637550add85d32b059c05aaf09e9b1` | 485,264 | 105 | 5,348,536 |
| x9 | `x9/` | `da74dad7cd0f6ff0c17fe28b671dfa7bd3a4ac80437150f8094f95eeb5ac77d2` | 607,541 | 137 | 11,617,835 |
| x12 | `x12/` | `41e11245ddf57dbc37ff16d168d5a69e16cd7248eb86cc8932002bb79449c004` | 739,832 | 167 | 7,810,438 |

## Manifest results (run 2026-10-25)

Each cycle's own `Verification/check_manifest.py` and `sha256sum --check --strict Provenance/MANIFEST.sha256` were both run from the cycle folder. Every file in each folder except the manifest itself is listed in its manifest.

| Cycle | Entries | `check_manifest.py` | `sha256sum --check` |
|---|---|---|---|
| Baseline | 39 | PASS ("Manifest PASS: 39 files") | PASS |
| x3 | 69 | PASS | PASS |
| x6 | 104 | PASS | PASS |
| x9 | 136 | PASS | PASS |
| x12 | 166 | PASS | PASS |

The repository check `bash .github/scripts/check_manifests.sh .` picks up all five new manifests and passes: 111 manifests, result PASS (105 on `main`, plus these 5 and Maps v44). A manifest PASS only shows the delivered bytes are intact; as the packages say themselves, it is not evidence that the content is true or approved.

## Summary, as the files record it

### Claims by label

| Cycle | Established | Plausible | Philosophical/Spiritual | Hypothetical | Total (all IDs unique) |
|---|---|---|---|---|---|
| Baseline (`claims/CLAIMS.csv`) | 21 | 13 | 11 | 0 | 45 |
| x3 (`claims/CLAIMS_X3.csv`) | 23 | 3 | 14 | 1 | 41 |
| x6 (`claims/CLAIMS_X6.csv`) | 28 | 7 | 17 | 2 | 54 |
| x9 (`claims/CLAIMS_X9.csv`) | 38 | 10 | 20 | 3 | 71 |
| x12 (`claims/CLAIMS_X12.csv`) | 46 | 13 | 23 | 3 | 85 |

Claim IDs are cycle-local. The packages state that earlier ledgers were **not** imported from one cycle to the next (later cycles were built from conversation records of the earlier ones because the original archives were unavailable to the producer at the time).

### Gate status (not upgraded here)

| Cycle | Overall research gate | Owner decision | Independent review | Ethics review | Scoped results recorded as FAIL / NOT SUPPORTED |
|---|---|---|---|---|---|
| Baseline | INDETERMINATE (`REPORT.md`, `metadata.json`; no `GATE_RECORD.json` in this cycle) | not recorded | none | none | — |
| x3 | INDETERMINATE (`GATE_RECORD.json`) | NOT RECORDED | NONE | NONE | — |
| x6 | INDETERMINATE | NOT RECORDED | NONE | NONE | — |
| x9 | INDETERMINATE | NOT RECORDED | NONE | NONE | **External-input validator reuse gate: FAIL.** Hypotheses H4 and H6: NOT SUPPORTED |
| x12 | INDETERMINATE | NOT RECORDED | NONE | NONE | **Predeclared specification-count conformance: FAIL** (iteration 6 check A1: declared 5,346 cases, actual factor product 1,782). **Legacy reconstructed verification-label criterion: FAIL** (kept). Candidate known-boundary criterion: PASS within the specified tests only. Canonical corpus integration: NOT COMPLETE. H8 and H10: NOT SUPPORTED |

Authorization is NONE in every gate record. The charter itself stays Proposed.

### Checks, failures and build errors, as recorded

- **Baseline:** 14/14 structural checks PASS; 12/12 pre-execution specification checks PASS. One process launch failed at parse time (SyntaxError) before any model state ran; it is kept in `simulation/DEVELOPMENT_DISCLOSURE.md`. 2 launches, 1 successful execution, no independent rerun.
- **x3:** 20/20 structural checks PASS; 25 predefined model predicates PASS in original and same-author reproduction (6 successful executions, 0 failed). Full-paper arXiv HTML fetch failed; abstract only was used (`Provenance/DEVELOPMENT_DISCLOSURES.md`).
- **x6:** 43 model predicates PASS (12 executions). Final artifact checks 26/26 PASS; the **initial** run was 25 PASS / 1 FAIL (A25, a locator formatting mismatch), corrected without changing the predicate. The initial failure is kept in `Verification/INITIAL_ARTIFACT_CHECKS.csv` and `ARTIFACT_CORRECTION.md`.
- **x9:** 64 in-domain predicates PASS (18 executions). Three post-run robustness probes **FAIL**: the delivered record-assessment function accepted `UNRECOGNIZED`, `None` and `True` as verification labels (`Verification/OUT_OF_DOMAIN_PROBES.json`, `ROBUSTNESS_FINDING.md`). No late patch. **Document build error:** `Provenance/DOCUMENT_BUILD_ERROR.md` records a documentation cell that failed at Python parse time (a colon instead of a comma); no model ran in it and no result changed. 35 artifact checks PASS.
- **x12:** 74 predefined predicates: **73 PASS / 1 FAIL** (A1 above; `Verification/CARDINALITY_FINDING.md`, `PREDEFINED_CHECK_SUMMARY.json`). 24 successful executions, 0 failed launches, 0 independent. 36 artifact checks PASS. A candidate v0.2.0 helper closes the x9 enum/type defect within its tested boundary only; the legacy FAIL stays recorded.

### Remaining gaps (x12)

`CLOSURE_AND_REMAINING_GAPS.csv` lists 6 items: the x9 enum/type defect (legacy FAIL; candidate PASS within scope; broader INDETERMINATE), the x12 cardinality FAIL (future approved correction pending; do not rethreshold), reviewer truth and hidden conflicts (H8 NOT SUPPORTED), lease and global freshness (H10 NOT SUPPORTED), actual remedy (none), and prior archives and global maps (NOT COMPLETE). `UNRESOLVED_QUESTIONS.csv` lists **33** open items, none closed: for example B01 independent content/rights review NONE, B02 ethics review NONE, B06 independent reproduction NOT PERFORMED, B07 canonical all-work integration NOT PERFORMED, B08 legal applicability NOT DETERMINED, X301 original prior artifacts UNAVAILABLE, X1201 predeclared case count FAIL.

## What this filing does and does not change

- B11 (GitHub/Work Queue disposition, "NOT WRITTEN") is addressed only in the narrow sense that the owner asked for the files to be filed and the checklist updated on 2026-10-25. The Work Queue ticks the ToG 1 cycles one by one; it does not tick the ToG series.
- B07 is **not** closed. Maps v44 (`Research/Maps-and-Matrix/v44-cycles-0-4-mr-track-abcd-phases-x12-conn0abcd-tog1/`) adds ToG 1's claims, clause–domain map, crosswalk and links as an overlay, and records the 625 local tuples by name as **UNPLACED / UNRESOLVED**, as the package states. It does not assign canonical placements.
- Nothing here is independent review. Grok Bot's checks are intake checks of bytes, counts and labels.

## Discrepancies noted

1. **Producer:** the packages name Perplexity (AI assistant) as producer and recorder, not Grok Bot and not the owner personally. The owner supplied them. Recorded as stated.
2. **Prior-cycle continuity:** x3–x12 each say the earlier archives were unavailable when they were written (X301 "UNAVAILABLE"). All five are now in one place, so byte continuity could be checked later. That check was **not** done here.
3. **Snapshot formatting:** x6, x9 and x12 write the snapshot as `fdec378a859f2 accdc7e2d9 cfe11040a0c34545d` (with spaces); Baseline, x3 and every `metadata.json` use the unbroken hash. Same commit; files left unedited.
4. **Baseline has no `GATE_RECORD.json`**; its gate is stated in `REPORT.md`, `metadata.json` and `Verification/VERIFICATION.md`.
5. **Domains:** each cycle's DOMAIN_MAP labels its TOT domains Plausible with approval NOT RECORDED and says the primary Totality Suite was not inspected. Seven clause–domain pairs appear in Baseline only.
6. **Compressed text:** several x6–x12 files have words run together (for example "Localdocumentary/finite-modelx9research"). Left as delivered.
