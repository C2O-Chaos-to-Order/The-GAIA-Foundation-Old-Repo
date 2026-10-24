# SIM-SPIRIT-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Stronger outcome-dependent dropout (m up to 2).

## Sources this run draws on
K45 (as iteration 2).

## Refinement from previous iteration
Iteration 2 tested m = 1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | random dropout unbiased |
| H1 | hypothesis | |shift| >= .05 at m 2 |
| R1 | reporting | by m |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 6,
 "kind": "attrition_mnar",
 "seed": 716,
 "n": 654,
 "rho": 0.2,
 "m_grid": [
  0.0,
  1.0,
  2.0
 ],
 "m_test": 2.0,
 "retain_target": 0.5795,
 "reps": 1000
}
```

## Command
`python sim_spirit.py iter-6` (run from `Spirit/simulation/`)
