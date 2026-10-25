# N-A x6: verification

Date: 2026-10-25. Branch `research/crosswalk-x6`. Tool `tools/na.py` git blob `68b160e556c6f653661ede8419843531b95c241a`.

## Rerun of this and every earlier N-A cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
Cycle-x3:
iter-1 identical=True
iter-2 identical=True
Cycle-x6:
iter-1 identical=True
iter-2 identical=True
```
Fresh clone of `research/crosswalk-x6` at `5ae8ea67`: the same command gave identical records for every iteration (GD mirror: the same blob-SHA-verified local mirror; checked by C*-1 on every run).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X6-1 PASS, X6-2 PASS, X6-3 PASS, X6-4 PASS, X6-5 PASS, X6-6 PASS, X6-7 PASS, X6-8 FAIL, X6-9 FAIL, X6-10 PASS, X6-11 FAIL, X6-12 PASS, X6-13 FAIL, X6-14 FAIL, X6-15 FAIL, X6-17 PASS, X6-18 PASS, X6-19 FAIL, X6-20 FAIL | 0 |
| iter-2 | strict | X6-1 PASS, X6-2 PASS, X6-3 PASS, X6-4 PASS, X6-5 PASS, X6-6 PASS, X6-7 PASS, X6-8 FAIL, X6-9 FAIL, X6-10 PASS, X6-11 FAIL, X6-12 PASS, X6-13 FAIL, X6-14 FAIL, X6-15 FAIL, X6-16 FAIL, X6-17 PASS, X6-18 PASS, X6-19 FAIL, X6-20 FAIL | 0 |

## Repository checks
- Earlier work still reproduces: PC-1 cycles `iter-1: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True iter-3: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True `
- Manifests (`mancheck.sh`): manifests: 92/92
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 11.97s
- GAIA-Documentation: read only; no file copied (only paths, blob SHAs, sizes, extracted terms, counts and short phrases); boundary scan in every record.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded.
