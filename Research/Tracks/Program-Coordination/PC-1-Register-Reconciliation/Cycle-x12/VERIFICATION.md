# PC-1 x12: verification

Date: 2026-10-25. Branch `research/pc1-x12`. Tool `tools/pc1.py` git blob `fabe1c5fc8dcc71e6db4167e6bc84c50786475a3`.

## Rerun of this and every earlier cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1: record identical=True
Cycle-x12:
iter-1: record identical=True
iter-2: record identical=True
Cycle-x3:
iter-1: record identical=True
iter-2: record identical=True
iter-3: record identical=True
Cycle-x6:
iter-1: record identical=True
iter-2: record identical=True
Cycle-x9:
iter-1: record identical=True
iter-2: record identical=True
```
Fresh clone of `research/pc1-x12` at `b25306f5`: the same command gave identical records for every iteration.

## Pre-registered checks
| Iteration | Home rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 PASS, X12-8 PASS, X12-9 PASS, X12-10 PASS, X12-11 PASS, X12-12 PASS, X12-13 PASS, X12-14 PASS, X12-15 PASS | 0 |
| iter-2 | as_judged | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 PASS, X12-8 PASS, X12-9 PASS, X12-10 PASS, X12-11 PASS, X12-12 PASS, X12-13 PASS, X12-14 PASS, X12-15 PASS | 0 |

## Repository checks
- Manifests (`mancheck.sh`): manifests: 89/89
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 11.50s
- Adoption boundary: no file of the Totality Suite is in this branch (only derived IDs, titles, priorities and short cited phrases); register SHA-256 checked on every run.
- Boundary scan of the whole PC-1 folder (`tools/pc1.py boundary`, 80-character windows): files sharing a 80-character window with the suite: 2   Cycle-0-Baseline/TABLES.md   Cycle-0-Baseline/iter-1/data/reconciliation.csv 

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell, in the table above and in REPORT.md; none is re-thresholded.
