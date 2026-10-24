# SIM-IN-HUM-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
James's two types of conversion (P43): a monostable system (a = -0.5) changes gradually under a slow push; a bistable one (a = 1) jumps. Largest change between successive small steps of r.

## Phase operationalization tested
HUM Insurgence = gradual (volitional) versus sudden (self-surrender) transformation (P43).

## Sources this run draws on
P43 (Chirico et al. 2022, Front Psychol 13:790300, CC BY; main text read in full in INC): transformative experiences as brief, sudden, irreversible changes (integrated definition); James's volitional (gradual) and self-surrender (sudden) conversion; Carel & Kidd: cumulative small changes. Drift from P41 Eq. 3; the mapping to experience is the agent's (interpretive).

## Refinement from previous iteration
Iteration 2 of the x9 family for HUM; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | both change > 1 in total |
| H1 | hypothesis | jump > 0.5 vs < 0.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Foreknowledge: smoke gave 1.06 and 0.01. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-C",
 "iteration": 2,
 "kind": "kramers_switch",
 "seed": 22502,
 "mode": "gradual",
 "a_values": [
  -0.5,
  1.0
 ],
 "r0": -1.0,
 "r1": 1.0,
 "n_r": 401,
 "relax": 2000,
 "h1_text": "bistable maximum step change > 0.5 and monostable < 0.05",
 "h1_expr": "o['1.0']['max_step_change'] > 0.5 and o['-0.5']['max_step_change'] < 0.05"
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
