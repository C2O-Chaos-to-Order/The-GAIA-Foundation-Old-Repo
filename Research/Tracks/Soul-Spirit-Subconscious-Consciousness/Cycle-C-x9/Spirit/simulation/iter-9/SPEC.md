# SIM-SPIRIT-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Larger trials (n = 300) with no causal ASE effect: does sample size remove the spurious correlation?

## Sources this run draws on
K39 (as iteration 1).

## Refinement from previous iteration
Iteration 1 used n = 100.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim r = analytic |
| H1 | hypothesis | r >= .30 |
| R1 | reporting | share significant |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 9,
 "kind": "mediation_confound",
 "seed": 719,
 "n": 300,
 "confound": 0.8,
 "direct_ase": 0.0,
 "reps": 2000
}
```

## Command
`python sim_spirit.py iter-9` (run from `Spirit/simulation/`)
