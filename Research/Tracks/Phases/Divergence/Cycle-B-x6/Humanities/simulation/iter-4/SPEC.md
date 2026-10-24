# SIM-DV-HUM-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Stemmatics with more contamination (4 of 8 copies contaminated instead of 2).

## Phase operationalization tested
HUM Divergence = manuscript divergence by copying, recovered as a stemma.

## Sources this run draws on
As DVA (P12/P13 stemmatics sources, read in full in DVA).

## Refinement from previous iteration
DVA iteration 3 used 2 contaminated copies; only cont_leaves and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | changes per copy within 4 SE |
| H1 | hypothesis | clean accuracy >= 0.95 |
| H2 | hypothesis | contamination lowers accuracy >= 0.05 |
| R1 | reporting | per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-B",
 "iteration": 4,
 "kind": "stemma_copying",
 "seed": 16504,
 "depth": 3,
 "M": 500,
 "mu": 0.02,
 "reps": 50,
 "cont_frac": 0.3,
 "cont_leaves": 4,
 "tol_se": 4,
 "h1": 0.95,
 "h2": 0.05
}
```

## Command
`python sim_hum.py iter-4` (run from `Humanities/simulation/`)
