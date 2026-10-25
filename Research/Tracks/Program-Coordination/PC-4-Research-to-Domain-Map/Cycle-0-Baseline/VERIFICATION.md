# PC-4 0-Baseline: verification

Date: 2026-10-25. Branch `research/pc4-c0`. Tool `tools/pc4.py` git blob `57c26eb47497f09d6377313fd1cad793071a3386`.

## Rerun (identical EXECUTION_RECORD required)
```
iter-1: record identical=True outputs identical=True
```
Fresh clone of `research/pc4-c0` at `911ee779`: the same command gave identical records for every iteration.

## Pre-registered checks
| Iteration | Matcher | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | charter | C0-1 PASS, C0-2 PASS, C0-3 PASS, C0-4 PASS, C0-5 PASS, C0-6 PASS, C0-7 PASS | 0 |

## Repository checks
- Manifests (`mancheck.sh`): manifests: 81/81
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 11.80s
- Adoption boundary: no file of the Totality Suite is in this branch (only derived IDs, titles and priorities); register SHA-256 checked on every run.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell, in the table above and in REPORT.md; none is re-thresholded.
