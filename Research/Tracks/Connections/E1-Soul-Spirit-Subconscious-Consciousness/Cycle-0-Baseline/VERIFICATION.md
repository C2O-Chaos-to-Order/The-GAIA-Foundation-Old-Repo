# Connection 0-Baseline: verification

Date: 2026-10-25. Branch `research/connection-c0`. Tool `tools/conn.py` git blob `2a799ebeac3cbe22479acaf69ad9e2092968b3b3`.

## Rerun of this and every earlier Connection cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
```
Fresh clone of `research/connection-c0` at `ff52843f`: the same verify command gave identical records for every iteration, and `conn.py maps` rebuilt v39 byte-identical (`diff -r`), via `connfresh.sh`.

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C0-1 PASS, C0-2 PASS, C0-3 PASS, C0-4 PASS, C0-5 PASS, C0-6 PASS, C0-7 PASS, C0-8 PASS, C0-9 FAIL, C0-10 FAIL, C0-11 FAIL, C0-12 FAIL, C0-13 PASS, C0-14 PASS, C0-15 PASS | 0 |

## Repository checks
- Earlier work (N-A, the previous report) rerun at this head with its own tool:
```
Cycle-0-Baseline iter-1: identical
Cycle-x12 iter-1: differs only in metrics.repro_dependents, outputs.option_ripple.csv
Cycle-x12 iter-2: differs only in metrics.repro_dependents, outputs.option_ripple.csv
Cycle-x12 iter-3: differs only in metrics.repro_dependents, outputs.option_ripple.csv
Cycle-x3 iter-1: identical
Cycle-x3 iter-2: identical
Cycle-x6 iter-1: identical
Cycle-x6 iter-2: identical
Cycle-x9 iter-1: differs only in metrics.repro_dependents, outputs.option_ripple.csv
Cycle-x9 iter-2: differs only in metrics.repro_dependents, outputs.option_ripple.csv
Cycle-x9 iter-3: differs only in metrics.repro_dependents, outputs.option_ripple.csv
```
  N-A x9 and x12 include `repro_dependents`, a live census of every `config.json` and `*.py` under `Research/` that names `Research/README.md` or `WORK_QUEUE.md`. This report's config and tool read and hash those files, so the census now lists them too, and that metric and `option_ripple.csv` differ; every check, every other metric and every other output is identical. N-A's records reproduce identically at their own commit (N-A x12 verification, `58044d58`). N-A is not edited; pinning that census to a commit is an option for the owner.
- Manifests (`mancheck.sh`): manifests: 97/97
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.80s
- Inputs (SSSC track, Phases track, README, Work Queue) read only; no file outside this report's folder and its new Maps version was changed.

Overall verification gate: **PASS** (reruns identical, Maps rebuild identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded. The Connection's content stays Proposed, gate INDETERMINATE pending independent review.
