# Connection x6: verification

Date: 2026-10-25. Branch `research/connection-x6`. Tool `tools/conn.py` git blob `473745fc55f5c0f2703b293d33c565e0d35e015d`.

## Rerun of this and every earlier Connection cycle with the current tool (identical EXECUTION_RECORD required)
```
Cycle-0-Baseline:
iter-1 identical=True
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
```
Fresh clone of `research/connection-x6` at `bb6ac628`: the same verify command gave identical records for every iteration of the Baseline, x3 and x6, and `conn.py maps` rebuilt v39, v40 and v41 byte-identical (`diff -r`), via `connfresh.sh` (which now takes each version's iteration from its README's reproduce line; v41 is built from iteration 3, as the SPEC states).

## Pre-registered checks
| Iteration | Rule | Checks | Integrity problems |
|---|---|---|---|
| iter-1 | as_judged | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 PASS, C6-20 PASS, C6-21 PASS | 0 |
| iter-2 | strict | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 FAIL, C6-20 PASS, C6-21 PASS | 0 |
| iter-3 | established_only | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 FAIL, C6-20 PASS, C6-21 PASS | 0 |
| iter-4 | no_method | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 PASS, C6-20 PASS, C6-21 PASS | 0 |
| iter-5 | no_tradition | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 FAIL, C6-20 PASS, C6-21 PASS | 0 |
| iter-6 | as_judged | C6-1 PASS, C6-2 PASS, C6-3 PASS, C6-4 PASS, C6-5 PASS, C6-6 PASS, C6-7 PASS, C6-8 PASS, C6-9 PASS, C6-10 PASS, C6-11 PASS, C6-12 PASS, C6-13 FAIL, C6-14 PASS, C6-15 PASS, C6-16 FAIL, C6-17 PASS, C6-18 PASS, C6-19 PASS, C6-20 PASS, C6-21 PASS | 0 |

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
- Manifests (`mancheck.sh`): manifests: 100/100
- `gaia_tools.phases validate`: {"n_cycles": 30, "n_errors": 0, "n_warnings": 0}
- pytest (`Research/tools`): 43 passed, 2 skipped in 13.16s
- The tool is identified by its git blob above, not by the cycle manifest (it evolves across cycles; each cycle's records must still reproduce with the current tool). The Baseline manifest's original line for `tools/conn.py` (blob `2a799ebe`) was removed in x3 for this reason.
- Inputs (SSSC track, Phases track, main Cycle-4-x12 reports and registers, README, Work Queue) read only; no file outside this report's folder and its new Maps version was changed.

Overall verification gate: **PASS** (reruns identical, Maps rebuild identical, manifests, validator and tests). Pre-registered check results are reported as they fell; none is re-thresholded. The Connection's content stays Proposed, gate INDETERMINATE pending independent review.
