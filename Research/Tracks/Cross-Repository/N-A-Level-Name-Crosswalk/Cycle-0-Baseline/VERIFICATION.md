# N-A 0-Baseline: verification

Date: 2026-10-25. Branch `research/crosswalk-c0`. Tool `tools/na.py` git blob `798e533c3a54b3ed58b3180e8d7b3caade4ca94e`.

## Rerun of this and every earlier N-A cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
```
Fresh clone of `research/crosswalk-c0` at `dffdd4c6`: the same command gave identical records for every iteration (GD mirror: the same blob-SHA-verified local mirror; checked by C*-1 on every run).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C0-1 PASS, C0-2 PASS, C0-3 PASS, C0-4 PASS, C0-5 PASS, C0-6 PASS, C0-7 PASS, C0-8 FAIL, C0-9 FAIL, C0-10 PASS, C0-11 FAIL, C0-12 PASS | 0 |

## Repository checks
- Earlier work still reproduces: PC-1 cycles `iter-1: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True iter-3: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True `
- Manifests (`mancheck.sh`): manifests: 90/90
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.00s
- GAIA-Documentation: read only; no file copied (only paths, blob SHAs, sizes, extracted terms, counts and short phrases); boundary scan in every record.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded.
