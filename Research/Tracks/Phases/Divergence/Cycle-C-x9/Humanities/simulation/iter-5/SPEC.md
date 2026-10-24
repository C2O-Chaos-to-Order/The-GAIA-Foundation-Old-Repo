# SIM-DV-HUM-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Null control: no change points, no drift: how often does a 'revolution' appear by chance at alpha 0.05?

## Phase operationalization tested
HUM Divergence = stylistic change in a cultural record, detected as rate discontinuities ('revolutions') (P21).

## Sources this run draws on
P21 (Mauch, MacCallum, Levy & Leroi 2015, R. Soc. Open Sci. 2:150081, PMC4453253, CC BY 4.0; read in full in DVC): 200 quarters, Foote Novelty with a checkerboard kernel, permutation cut-offs, revolutions around 1964, 1983 and 1991 (change points here placed at quarters 30, 92, 124 = 1967.5, 1983, 1991 by analogy only).

## Refinement from previous iteration
Control.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share of replicates with a significant peak within 4 binomial SE of 0.05 |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic features (4-dim), not P21's topics; about 85 songs per quarter mirrors 17,094 / 200; kernel half-width 12 quarters = P21's 3 years. Permutation null uses the maximum novelty over the series. With 40 replicates the binomial band is wide. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-C",
 "iteration": 5,
 "kind": "foote_novelty",
 "seed": 17505,
 "T": 200,
 "d": 4,
 "w": 12,
 "change_points": [],
 "reps": 40,
 "drift": 0.0,
 "jump": 1.5,
 "noise": 1.0,
 "n_per": 85,
 "perms": 99,
 "alpha": 0.05,
 "tol": 4,
 "h1": 0.8,
 "h2": 1.0,
 "tol_se": 4
}
```

## Command
`python sim_hum.py iter-5` (run from `Humanities/simulation/`)
