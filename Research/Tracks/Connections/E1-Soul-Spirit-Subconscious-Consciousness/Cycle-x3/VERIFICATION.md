# Connection x3: verification

Date: 2026-10-25. Branch `research/connection-x3`. Tool `tools/conn.py` git blob `e2d52737f92d879129da71b0f633de263e530fd2`.

## Rerun of this and every earlier Connection cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
Cycle-x3:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
```
Fresh clone of `research/connection-x3` at `a79d93b1`: the same verify command gave identical records for every iteration of the Baseline and x3, and `conn.py maps` rebuilt v39 and v40 byte-identical (`diff -r`), via `connfresh.sh`.

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C3-1 PASS, C3-2 PASS, C3-3 PASS, C3-4 PASS, C3-5 PASS, C3-6 PASS, C3-7 PASS, C3-8 PASS, C3-9 PASS, C3-10 FAIL, C3-11 PASS, C3-12 PASS, C3-13 FAIL, C3-14 PASS, C3-15 PASS, C3-16 PASS, C3-17 PASS | 0 |
| iter-2 | strict | C3-1 PASS, C3-2 PASS, C3-3 PASS, C3-4 PASS, C3-5 PASS, C3-6 PASS, C3-7 PASS, C3-8 PASS, C3-9 PASS, C3-10 FAIL, C3-11 PASS, C3-12 PASS, C3-13 FAIL, C3-14 PASS, C3-15 FAIL, C3-16 PASS, C3-17 PASS | 0 |
| iter-3 | established_only | C3-1 PASS, C3-2 PASS, C3-3 PASS, C3-4 PASS, C3-5 PASS, C3-6 PASS, C3-7 PASS, C3-8 PASS, C3-9 PASS, C3-10 FAIL, C3-11 PASS, C3-12 PASS, C3-13 FAIL, C3-14 PASS, C3-15 FAIL, C3-16 PASS, C3-17 PASS | 0 |

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
- Manifests (`mancheck.sh`): manifests: 98/98
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 11.90s
- The tool is identified by its git blob above, not by the cycle manifest (it evolves across cycles; each cycle's records must still reproduce with the current tool). The Baseline manifest's original line for `tools/conn.py` (blob `2a799ebe`) was removed in x3 for this reason.
- Inputs (SSSC track, Phases track, README, Work Queue) read only; no file outside this report's folder and its new Maps version was changed.

Overall verification gate: **PASS** (reruns identical, Maps rebuild identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded. The Connection's content stays Proposed, gate INDETERMINATE pending independent review.
