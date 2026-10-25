# Connection x12: verification

Date: 2026-10-25. Branch `research/connection-x12`. Tool `tools/conn.py` git blob `bbe071acbed23de5f3074b4c6a1be9c49b9fc01a`.

## Rerun of this and every earlier Connection cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
Cycle-x12:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
iter-4 identical=True
iter-5 identical=True
iter-6 identical=True
iter-7 identical=True
iter-8 identical=True
iter-9 identical=True
iter-10 identical=True
iter-11 identical=True
iter-12 identical=True
Cycle-x3:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
Cycle-x6:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
iter-4 identical=True
iter-5 identical=True
iter-6 identical=True
Cycle-x9:
iter-1 identical=True
iter-2 identical=True
iter-3 identical=True
iter-4 identical=True
```
Fresh clone of `research/connection-x12` at `d2737e69`: the same verify command gave identical records for every iteration of the Baseline, x3, x6, x9 and x12, and `conn.py maps` rebuilt v39 to v43 byte-identical (`diff -r`), via `connfresh.sh` (v43 is built from iteration 7, as the SPEC states).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |
| iter-2 | strict | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-3 | established_only | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-4 | no_method | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |
| iter-5 | no_tradition | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-6 | as_judged | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |
| iter-7 | reviewed | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |
| iter-8 | strict | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-9 | established_only | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-10 | no_method | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |
| iter-11 | no_tradition | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 FAIL, C12-26 PASS, C12-27 PASS | 0 |
| iter-12 | reviewed | C12-1 PASS, C12-2 PASS, C12-3 PASS, C12-4 PASS, C12-5 PASS, C12-6 PASS, C12-7 PASS, C12-8 PASS, C12-9 PASS, C12-10 PASS, C12-11 PASS, C12-12 PASS, C12-13 PASS, C12-14 PASS, C12-15 PASS, C12-16 PASS, C12-17 FAIL, C12-18 PASS, C12-19 PASS, C12-20 PASS, C12-21 PASS, C12-22 PASS, C12-23 PASS, C12-24 PASS, C12-25 PASS, C12-26 PASS, C12-27 PASS | 0 |

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
- Manifests (`mancheck.sh`): manifests: 104/104
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 12.13s
- The tool is identified by its git blob above, not by the cycle manifest (it evolves across cycles; each cycle's records must still reproduce with the current tool). The Baseline manifest's original line for `tools/conn.py` (blob `2a799ebe`) was removed in x3 for this reason.
- Inputs (SSSC track, Phases track, main Cycle-4-x12 reports and registers, README, Work Queue) read only; no file outside this report's folder, its new Maps version and the Connections index status line was changed.

Overall verification gate: **PASS** (reruns identical, Maps rebuild identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded. The Connection's content stays Proposed, gate INDETERMINATE pending independent review.
