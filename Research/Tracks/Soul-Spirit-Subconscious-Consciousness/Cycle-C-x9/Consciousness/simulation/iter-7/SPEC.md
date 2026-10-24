# SIM-CONS-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. 200 neurologists per vignette.

## Sources this run draws on
K47 (as iteration 4).

## Refinement from previous iteration
Iteration 4 used 120 per group.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC = noncentral chi-square |
| H1 | hypothesis | power < .8 |
| R1 | reporting | power by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 7,
 "kind": "chisq_3group",
 "seed": 817,
 "props": [
  0.47,
  0.63,
  0.67
 ],
 "n_per_group": 200,
 "reps": 20000,
 "n_grid": [
  200,
  300
 ]
}
```

## Command
`python sim_cons.py iter-7` (run from `Consciousness/simulation/`)
