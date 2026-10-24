# SIM-DV-HUM-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Stemmatics with light contamination (1 of 8 copies).

## Phase operationalization tested
HUM Divergence = manuscript divergence by copying.

## Sources this run draws on
P12/P13 (read in full in DVA).

## Refinement from previous iteration
cont_leaves 4 -> 1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | changes per copy within 4 SE |
| H1 | hypothesis | clean accuracy >= 0.95 |
| H2 | hypothesis | contamination lowers accuracy >= 0.05 |
| R1 | reporting | per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-C",
 "iteration": 6,
 "kind": "stemma_copying",
 "seed": 17506,
 "depth": 3,
 "M": 500,
 "mu": 0.02,
 "reps": 50,
 "cont_frac": 0.3,
 "cont_leaves": 1,
 "tol_se": 4,
 "h1": 0.95,
 "h2": 0.05
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
