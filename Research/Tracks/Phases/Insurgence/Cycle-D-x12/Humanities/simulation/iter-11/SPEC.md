# SIM-IN-HUM-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Gradual-vs-sudden variant: a = -0.2 vs 0.5.

## Phase operationalization tested
HUM Insurgence = gradual (volitional) versus sudden (self-surrender) transformation (P43).

## Sources this run draws on
P43 (Chirico et al. 2022, Front Psychol 13:790300, CC BY; main text read in full in INC): transformative experiences as brief, sudden, irreversible changes (integrated definition); James's volitional (gradual) and self-surrender (sudden) conversion; Carel & Kidd: cumulative small changes. Drift from P41 Eq. 3; the mapping to experience is the agent's (interpretive).

## Refinement from previous iteration
Iteration 11 of the x12 family for HUM; follows iteration 10 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | both change > 1 in total |
| H1 | hypothesis | jump > 0.5 vs < 0.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-D",
 "iteration": 11,
 "kind": "kramers_switch",
 "seed": 23511,
 "mode": "gradual",
 "a_values": [
  -0.2,
  0.5
 ],
 "r0": -1.0,
 "r1": 1.0,
 "n_r": 401,
 "relax": 2000,
 "h1_text": "bistable maximum step change > 0.3 and monostable < 0.05",
 "h1_expr": "o['0.5']['max_step_change'] > 0.3 and o['-0.2']['max_step_change'] < 0.05"
}
```

## Command
`python sim_hum.py iter-11` (run from `Humanities/simulation/`)
