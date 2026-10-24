# SIM-SUBC-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Reproduce K09's power argument: awareness tests in implicit-learning studies (median N 16) are too small to detect a real awareness effect of dz = 0.31, so 'chance-level awareness' is a weak basis for 'unconscious' learning.

## Sources this run draws on
K09 (Vadillo, Konstantinidis & Shanks 2016): dz = 0.31, median N = 16, power ~.21, 84 participants for 80% power two-tailed; 181 awareness tests.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic power at n=16 within 0.02 of 0.21 |
| V2 | validation | simulated power within 0.015 of analytic |
| V3 | validation | n80 within 2 of 84 |
| H1 | hypothesis | >= 75% of n=16 awareness tests non-significant although awareness is real |
| H2 | hypothesis | pooling 181 tests detects awareness in >= 95% of literatures |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-sample t-tests on normal difference scores; fixed-effect pooling; Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-A",
 "iteration": 1,
 "kind": "awareness_power",
 "seed": 101,
 "dz": 0.31,
 "alpha": 0.05,
 "n_list": [
  8,
  16,
  32,
  66,
  84
 ],
 "reps": 20000,
 "n_tests": 181,
 "n_median": 16,
 "lit_reps": 2000
}
```

## Command
`python sim_subc.py iter-1` (run from `Subconscious/simulation/`)
