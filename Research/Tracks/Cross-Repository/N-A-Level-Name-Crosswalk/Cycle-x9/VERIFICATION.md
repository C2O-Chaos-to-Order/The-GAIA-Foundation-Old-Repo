# N-A x9: verification

Date: 2026-10-25. Branch `research/crosswalk-x9`. Tool `tools/na.py` git blob `96a6e00582a9ea48b33f1053cc3897dc1daed845`.

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
Cycle-x9:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
```
Fresh clone of `research/crosswalk-x9` at `b04b05b2`: the same command gave identical records for every iteration (GD mirror: the same blob-SHA-verified local mirror; checked by C*-1 on every run).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | X9-1 PASS, X9-2 PASS, X9-3 PASS, X9-4 PASS, X9-5 PASS, X9-6 PASS, X9-7 PASS, X9-8 FAIL, X9-9 FAIL, X9-10 PASS, X9-11 FAIL, X9-12 PASS, X9-13 FAIL, X9-14 FAIL, X9-15 FAIL, X9-17 PASS, X9-18 PASS, X9-19 FAIL, X9-20 FAIL, X9-21 PASS, X9-22 PASS, X9-23 FAIL, X9-24 FAIL, X9-25 FAIL, X9-26 PASS | 0 |
| iter-2 | strict | X9-1 PASS, X9-2 PASS, X9-3 PASS, X9-4 PASS, X9-5 PASS, X9-6 PASS, X9-7 PASS, X9-8 FAIL, X9-9 FAIL, X9-10 PASS, X9-11 FAIL, X9-12 PASS, X9-13 FAIL, X9-14 FAIL, X9-15 FAIL, X9-16 FAIL, X9-17 PASS, X9-18 PASS, X9-19 FAIL, X9-20 FAIL, X9-21 PASS, X9-22 PASS, X9-23 FAIL, X9-24 FAIL, X9-25 FAIL, X9-26 PASS | 0 |
| iter-3 | adversarial | X9-1 PASS, X9-2 PASS, X9-3 PASS, X9-4 PASS, X9-5 PASS, X9-6 PASS, X9-7 PASS, X9-8 FAIL, X9-9 FAIL, X9-10 PASS, X9-11 FAIL, X9-12 PASS, X9-13 FAIL, X9-14 FAIL, X9-15 FAIL, X9-17 PASS, X9-18 PASS, X9-19 FAIL, X9-20 FAIL, X9-21 PASS, X9-22 PASS, X9-23 FAIL, X9-24 FAIL, X9-25 FAIL, X9-27 FAIL | 0 |

## Repository checks
- Earlier work still reproduces: PC-1 cycles `iter-1: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True iter-3: record identical=True iter-1: record identical=True iter-2: record identical=True iter-1: record identical=True iter-2: record identical=True `
- Manifests (`mancheck.sh`): manifests: 93/93
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 11.88s
- GAIA-Documentation: read only; no file copied (only paths, blob SHAs, sizes, extracted terms, counts and short phrases); boundary scan in every record.

Overall verification gate: **PASS** (reruns identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded.
