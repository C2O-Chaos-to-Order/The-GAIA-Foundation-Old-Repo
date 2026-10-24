# SIM-IN-PHI-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Sub-threshold exposure (a = 1.2, peak utility only 0.6): does the episode leave no lasting trace (< 0.1)?

## Phase operationalization tested
PHI Insurgence = a conversion that does or does not survive the end of the conditions that produced it.

## Sources this run draws on
P30 (read in full in INA) Eq. 1 with u ramped up and back (agent's experiment); P43 for irreversibility as a mark of transformative experience (interpretive).

## Refinement from previous iteration
Iteration 4 of the x9 family for PHI; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | x in [0, 1] |
| H1 | hypothesis | see text |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Not tried in advance. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-C",
 "iteration": 4,
 "kind": "abrams_groups",
 "seed": 22604,
 "a": 1.2,
 "h1_text": "stance < 0.1 after the hold",
 "h1_expr": "res['x_after_hold'] < 0.1",
 "mode": "ramp",
 "c": 1.0,
 "u": 0.5,
 "dt": 0.01,
 "x0": 0.2,
 "u0": 0.45,
 "u1": 0.6,
 "T_ramp": 20,
 "T_hold": 200
}
```

## Command
`python sim_phi.py iter-4` (run from `Philosophy-Spirituality/simulation/`)
