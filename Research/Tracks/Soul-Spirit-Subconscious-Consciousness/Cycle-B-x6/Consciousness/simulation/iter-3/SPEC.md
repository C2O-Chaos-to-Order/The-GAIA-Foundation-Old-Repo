# SIM-CONS-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K27 argues that posterior decoding reported as support for IIT in the adversarial collaboration could arise from non-conscious processes. Does a model with stimulus coding on every trial decode unseen trials above chance?

## Sources this run draws on
K27 (Naccache et al. 2025, Neuroscience of Consciousness).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | signal 0 at chance |
| H1 | hypothesis | unseen accuracy >= .6 |
| R1 | reporting | by signal |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Nearest-centroid decoder; awareness independent of the code by construction. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 3,
 "kind": "decoding_nonconscious",
 "seed": 413,
 "trials": 400,
 "channels": 50,
 "p_seen": 0.5,
 "signal_grid": [
  0.0,
  0.1,
  0.2
 ],
 "signal_test": 0.2,
 "reps": 300
}
```

## Command
`python sim_cons.py iter-3` (run from `Consciousness/simulation/`)
