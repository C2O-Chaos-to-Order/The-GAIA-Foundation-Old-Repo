# N-A x12: verification

Date: 2026-10-25. Branch `research/crosswalk-x12`. Tool `tools/na.py` git blob `48687d527aae8f8f94766b511a36ec5340562483`.

## Rerun of this and every earlier N-A cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
Cycle-x12:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
Cycle-x3:
iter-1 identical=True
iter-2 identical=True
Cycle-x6:
iter-1 identical=True
iter-2 identical=True
Cycle-x9:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
```
Fresh clone of `research/crosswalk-x12` at `c5622e11`: the same command gave identical records for every iteration (GD mirror: the same blob-SHA-verified local mirror; checked by C*-1 on every run).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 PASS, X12-8 FAIL, X12-9 FAIL, X12-10 PASS, X12-11 FAIL, X12-12 PASS, X12-13 FAIL, X12-14 FAIL, X12-15 FAIL, X12-17 PASS, X12-18 PASS, X12-19 FAIL, X12-20 FAIL, X12-21 PASS, X12-22 PASS, X12-23 PASS, X12-24 FAIL, X12-25 FAIL, X12-26 PASS, X12-28 FAIL, X12-29 PASS, X12-30 PASS, X12-31 PASS | 0 |
| iter-2 | strict | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 PASS, X12-8 FAIL, X12-9 FAIL, X12-10 PASS, X12-11 FAIL, X12-12 PASS, X12-13 FAIL, X12-14 FAIL, X12-15 FAIL, X12-16 FAIL, X12-17 PASS, X12-18 PASS, X12-19 FAIL, X12-20 FAIL, X12-21 PASS, X12-22 PASS, X12-23 PASS, X12-24 FAIL, X12-25 FAIL, X12-26 PASS, X12-28 FAIL, X12-29 PASS, X12-30 PASS, X12-31 PASS | 0 |
| iter-3 | adversarial | X12-1 PASS, X12-2 PASS, X12-3 PASS, X12-4 PASS, X12-5 PASS, X12-6 PASS, X12-7 PASS, X12-8 FAIL, X12-9 FAIL, X12-10 PASS, X12-11 FAIL, X12-12 PASS, X12-13 FAIL, X12-14 FAIL, X12-15 FAIL, X12-17 PASS, X12-18 PASS, X12-19 FAIL, X12-20 FAIL, X12-21 PASS, X12-22 PASS, X12-23 PASS, X12-24 FAIL, X12-25 FAIL, X12-27 FAIL, X12-28 FAIL, X12-29 PASS, X12-30 PASS, X12-31 PASS | 0 |

## Repository checks
- Earlier work still reproduces: PC-1 cycles `iter-1: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True iter-3: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True `
- Manifests (`mancheck.sh`): manifests: 94/94
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.31s
- GAIA-Documentation: read only; no file copied (only paths, blob SHAs, sizes, extracted terms, counts and short phrases); boundary scan in every record.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded.
