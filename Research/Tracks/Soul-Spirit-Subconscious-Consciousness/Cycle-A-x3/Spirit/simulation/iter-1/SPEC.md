# SIM-SPIRIT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K05 failed to reproduce several awe effects, including three direct replications at 2.5x the original samples. How strong is a run of three failures as evidence against a small true effect, and how inflated would published originals be under selection?

## Sources this run draws on
K05 (Graziosi et al. 2026, PLoS One): six studies; three online direct replications at 2.5x original N; effects of Valdesolo & Graham 2014, Piff et al. 2015, Rudd et al. 2012 not reproduced. Original Ns are not used (n0 = 50 per group is illustrative).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | unselected mean d within 0.02 of 0.5 |
| H1 | hypothesis | true d = 0.2: P(3 of 3 replications fail) < 0.10 |
| H2 | hypothesis | true d = 0: mean published d > 0.4 |
| R1 | reporting | replication power by d |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-group t-tests, normal outcomes, two-sided alpha .05, illustrative n0. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-A",
 "iteration": 1,
 "kind": "replication_runs",
 "seed": 301,
 "n0": 50,
 "mult": 2.5,
 "d_grid": [
  0.0,
  0.2,
  0.3,
  0.5
 ],
 "k_reps": 3,
 "reps": 20000
}
```

## Command
`python sim_spirit.py iter-1` (run from `Spirit/simulation/`)
