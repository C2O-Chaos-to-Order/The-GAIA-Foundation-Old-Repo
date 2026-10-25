# PC-1 x3: verification

Date: 2026-10-25. Branch `research/pc1-x3`. Tool `tools/pc1.py` git blob `377bf77a16852e1ebb1b0c86522db10bf3e58264`.

## Rerun of this and every earlier cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1: record identical=True
Cycle-x3:
iter-1: record identical=True
iter-2: record identical=True
iter-3: record identical=True
```
Fresh clone of `research/pc1-x3` at `1e799858`: the same command gave identical records for every iteration.

## Pre-registered checks
| Iteration | Home rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X3-1 PASS, X3-2 PASS, X3-3 PASS, X3-4 PASS, X3-5 PASS, X3-6 FAIL, X3-7 FAIL, X3-8 PASS, X3-9 PASS, X3-10 PASS, X3-11 PASS, X3-14 PASS | 0 |
| iter-2 | always_new | X3-1 PASS, X3-2 PASS, X3-3 PASS, X3-4 PASS, X3-5 PASS, X3-6 FAIL, X3-7 FAIL, X3-8 PASS, X3-9 PASS, X3-10 PASS, X3-11 PASS, X3-12 PASS | 0 |
| iter-3 | no_planned | X3-1 PASS, X3-2 PASS, X3-3 PASS, X3-4 PASS, X3-5 PASS, X3-6 FAIL, X3-7 FAIL, X3-8 PASS, X3-9 PASS, X3-10 PASS, X3-11 PASS, X3-13 PASS | 0 |

## Repository checks
- Manifests (`mancheck.sh`): manifests: 86/86
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.27s
- Adoption boundary: no file of the Totality Suite is in this branch (only derived IDs, titles, priorities and short cited phrases); register SHA-256 checked on every run.
- Boundary scan of the whole PC-1 folder (`tools/pc1.py boundary`, 80-character windows): files sharing a 80-character window with the suite: 2   Cycle-0-Baseline/TABLES.md   Cycle-0-Baseline/iter-1/data/reconciliation.csv 

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell, in the table above and in REPORT.md; none is re-thresholded.
