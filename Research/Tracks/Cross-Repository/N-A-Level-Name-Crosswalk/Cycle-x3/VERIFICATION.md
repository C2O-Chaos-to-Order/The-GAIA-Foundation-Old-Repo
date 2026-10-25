# N-A x3: verification

Date: 2026-10-25. Branch `research/crosswalk-x3`. Tool `tools/na.py` git blob `6574b7f570463ea1d7c864b6dc7367dea06990f3`.

## Rerun of this and every earlier N-A cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
Cycle-x3:
iter-1 identical=True
iter-2 identical=True
```
Fresh clone of `research/crosswalk-x3` at `3a22b4e4`: the same command gave identical records for every iteration (GD mirror: the same blob-SHA-verified local mirror; checked by C*-1 on every run).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X3-1 PASS, X3-2 PASS, X3-3 FAIL, X3-4 PASS, X3-5 PASS, X3-6 PASS, X3-7 PASS, X3-8 FAIL, X3-9 FAIL, X3-10 PASS, X3-11 FAIL, X3-12 PASS, X3-13 FAIL, X3-14 FAIL, X3-15 FAIL | 0 |
| iter-2 | strict | X3-1 PASS, X3-2 PASS, X3-3 FAIL, X3-4 PASS, X3-5 PASS, X3-6 PASS, X3-7 PASS, X3-8 FAIL, X3-9 FAIL, X3-10 PASS, X3-11 FAIL, X3-12 PASS, X3-13 FAIL, X3-14 FAIL, X3-15 FAIL, X3-16 FAIL | 0 |

## Repository checks
- Earlier work still reproduces: PC-1 cycles `iter-1: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True iter-3: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True `
- Manifests (`mancheck.sh`): manifests: 91/91
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.45s
- GAIA-Documentation: read only; no file copied (only paths, blob SHAs, sizes, extracted terms, counts and short phrases); boundary scan in every record.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded.
