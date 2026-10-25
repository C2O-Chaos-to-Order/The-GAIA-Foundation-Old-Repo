# PC-1 0-Baseline: verification

Date: 2026-10-25. Branch `research/pc1-c0`. Tool `tools/pc1.py` git blob `4f8e3273ed54a95050fbe2cbbf5f0f4dfa779fd6`.

## Rerun of this and every earlier cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1: record identical=True
```
Fresh clone of `research/pc1-c0` at `a82cd665`: the same command gave identical records for every iteration.

## Pre-registered checks
| Iteration | Home rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C0-1 PASS, C0-2 PASS, C0-3 PASS, C0-4 PASS, C0-5 PASS, C0-6 PASS, C0-7 PASS, C0-8 PASS, C0-9 PASS | 0 |

## Repository checks
- Manifests (`mancheck.sh`): FAIL ./Research/Tracks/Program-Coordination/PC-1-Register-Reconciliation/Cycle-0-Baseline/MANIFEST.sha256
manifests: 85/86
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.30s
- Adoption boundary: no file of the Totality Suite is in this branch (only derived IDs, titles, priorities and short cited phrases); register SHA-256 checked on every run.
- Boundary scan of the whole PC-1 folder (`tools/pc1.py boundary`, 80-character windows): files sharing a 80-character window with the suite: 2   Cycle-0-Baseline/TABLES.md   Cycle-0-Baseline/iter-1/data/reconciliation.csv 

Overall verification gate: **FAIL** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell, in the table above and in REPORT.md; none is re-thresholded.
