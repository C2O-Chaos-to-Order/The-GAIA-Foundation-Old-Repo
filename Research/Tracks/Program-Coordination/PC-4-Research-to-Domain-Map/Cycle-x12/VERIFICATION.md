# PC-4 x12: verification

Date: 2026-10-25. Branch `research/pc4-x12`. Tool `tools/pc4.py` git blob `7e0094248f39f9362f890b1b6fcee549b839596a`.

## Rerun of this and every earlier cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1: record identical=True outputs identical=True
Cycle-x12:
iter-1: record identical=True outputs identical=True
iter-2: record identical=True outputs identical=True
iter-3: record identical=True outputs identical=True
iter-4: record identical=True outputs identical=True
iter-5: record identical=True outputs identical=True
iter-6: record identical=True outputs identical=True
iter-7: record identical=True outputs identical=True
iter-8: record identical=True outputs identical=True
iter-9: record identical=True outputs identical=True
iter-10: record identical=True outputs identical=True
iter-11: record identical=True outputs identical=True
iter-12: record identical=True outputs identical=True
Cycle-x3:
iter-1: record identical=True outputs identical=True
iter-2: record identical=True outputs identical=True
iter-3: record identical=True outputs identical=True
Cycle-x6:
iter-1: record identical=True outputs identical=True
iter-2: record identical=True outputs identical=True
iter-3: record identical=True outputs identical=True
iter-4: record identical=True outputs identical=True
iter-5: record identical=True outputs identical=True
iter-6: record identical=True outputs identical=True
Cycle-x9:
iter-1: record identical=True outputs identical=True
iter-2: record identical=True outputs identical=True
iter-3: record identical=True outputs identical=True
iter-4: record identical=True outputs identical=True
iter-5: record identical=True outputs identical=True
iter-6: record identical=True outputs identical=True
iter-7: record identical=True outputs identical=True
iter-8: record identical=True outputs identical=True
iter-9: record identical=True outputs identical=True
```
Fresh clone of `research/pc4-x12` at `f0394859`: the same command gave identical records for every iteration.

## Pre-registered checks
| Iteration | Matcher | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | charter | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-2 | charter | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |
| iter-3 | charter | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-4 | title_purpose | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-5 | title_purpose | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |
| iter-6 | title_purpose | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-7 | title | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-8 | title | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |
| iter-9 | title | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-9 PASS, X12-10 PASS | 0 |
| iter-10 | charter | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |
| iter-11 | title_purpose | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |
| iter-12 | title | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 FAIL, X12-8 PASS, X12-9 PASS, X12-10 PASS | 0 |

## Repository checks
- Manifests (`mancheck.sh`): manifests: 84/84
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.21s
- Adoption boundary: no file of the Totality Suite is in this branch (only derived IDs, titles and priorities); register SHA-256 checked on every run.
- Boundary scan of the whole PC-4 folder (`tools/pc4.py boundary`, 120-character windows): files sharing a 120-character window with the suite: 1   Cycle-x3/PASSES.md 

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell, in the table above and in REPORT.md; none is re-thresholded.
