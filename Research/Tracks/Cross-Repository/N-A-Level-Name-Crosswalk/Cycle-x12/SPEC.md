# N-A x12: specification

This specification was written and pushed **before** the x12 run, together with its input `../CROSSWALK.md`. It builds on x9 at `research/crosswalk-x9` (`a9c497d8`).

## Purpose
x12 consolidates. It produces three things:
- **`../CROSSWALK.md`**, the consolidated map: all six conflicts, every option with its review verdict, the record ripple, errata to the Work Queue entry, and the diminishing-returns statement.
- **The final options register**, `../judgments/options_x12.csv`.
- **Corrections to x9**, found when the x9 report was re-read before x12:
  1. The x9 report said an appended Work Queue note avoids record drift. **That is wrong**, because any edit changes the blob that the records hash. It is corrected in the K1-C, K2-B, K2-C and K3-B consequences and in the K3-B review basis.
  2. The K5 evidence citation `vocab.canonical_home` becomes `vocab.canonical_home_gaiadoc`. The K6 citation of the v1 stage metric becomes `stage_sequence_variants_v2`.
  3. The evidence checker's false positive (dotted `.csv` names treated as metrics) is fixed behind the config key `x12`, so the x9 record still reproduces with its defect.
- **New option K3-G** (errata recorded in CROSSWALK.md, queue unchanged).
  - It arises from the x9 ripple finding.
  - **It was added after X9-27 failed for K3.** Its "survives" verdict, and any X12-27 change for K3, are therefore not independent evidence.

No GD reading is new. The crosswalk rows are carried forward unchanged.

## Pre-registered checks
- X12-1 to X12-27 carry over X9-1 to X9-27 unchanged. Iteration scoping is the same: X12-16 runs on iter-2; X12-26 on iters 1–2; X12-27 on iter-3.

| ID | Hypothesis | Metric | Test | Kind |
|---|---|---|---|---|
| X12-28 | Every ID named in CROSSWALK.md exists | doc_unknown_ids | = 0 | method |
| X12-29 | CROSSWALK.md covers every option | doc_missing_options | = 0 | method |
| X12-30 | CROSSWALK.md covers every conflict | doc_missing_conflicts | = 0 | method |
| X12-31 | x12 changes no crosswalk row against x9 | crosswalk_rows_changed_vs_previous | = 0 | diminishing returns (summary) |

**Disclosure:**
- **X12-23 is expected to pass** after the fixes above.
- **X12-24, X12-25 and X12-27 are expected to fail again.**
  - The Work Queue text is unchanged.
  - The align-foundation options still edit files that other records read.
  - K6 still has no unqualified survivor.
- **X12-31 is under my control,** since I chose not to change rows, so it records a fact about this cycle rather than testing one.

## Gate
- PASS needs:
  - the method checks X12-1 to X12-7, X12-12, X12-17, X12-21, X12-22 and X12-28 to X12-30
  - identical reruns of every N-A cycle
  - PC-1 reproduction
  - the manifests, validator and tests
- The crosswalk stays **Proposed**. Adopting it, or any option, is Kyle's decision.
