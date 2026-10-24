# SIM-IN-HUM-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Degree of suddenness: near the cusp (a = 0.1) is the jump much smaller than at a = 1?

## Phase operationalization tested
HUM Insurgence = transformations of varying abruptness (P43: TEs need not be sudden).

## Sources this run draws on
P43 (Chirico et al. 2022, Front Psychol 13:790300, CC BY; main text read in full in INC): transformative experiences as brief, sudden, irreversible changes (integrated definition); James's volitional (gradual) and self-surrender (sudden) conversion; Carel & Kidd: cumulative small changes. Drift from P41 Eq. 3; the mapping to experience is the agent's (interpretive).

## Refinement from previous iteration
Iteration 3 of the x9 family for HUM; follows iteration 2 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | both change > 1 in total |
| H1 | hypothesis | jump at a = 0.1 less than half |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; not smoke-tested at a = 0.1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-C",
 "iteration": 3,
 "kind": "kramers_switch",
 "seed": 22503,
 "mode": "gradual",
 "a_values": [
  0.1,
  1.0
 ],
 "r0": -1.0,
 "r1": 1.0,
 "n_r": 401,
 "relax": 2000,
 "h1_text": "maximum step change at a = 0.1 less than half that at a = 1",
 "h1_expr": "o['0.1']['max_step_change'] < o['1.0']['max_step_change'] / 2"
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
