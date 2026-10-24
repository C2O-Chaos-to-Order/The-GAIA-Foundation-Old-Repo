# SIM-DV-HUM-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Can P21's method recover three known change points of moderate size (jump 1.5 SD of per-song noise) under slow drift?

## Phase operationalization tested
HUM Divergence = stylistic change in a cultural record, detected as rate discontinuities ('revolutions') (P21).

## Sources this run draws on
P21 (Mauch, MacCallum, Levy & Leroi 2015, R. Soc. Open Sci. 2:150081, PMC4453253, CC BY 4.0; read in full in DVC): 200 quarters, Foote Novelty with a checkerboard kernel, permutation cut-offs, revolutions around 1964, 1983 and 1991 (change points here placed at quarters 30, 92, 124 = 1967.5, 1983, 1991 by analogy only).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | rates computed in [0,1] |
| H1 | hypothesis | detection rate >= 0.8 |
| H2 | hypothesis | false peaks <= 1 per replicate |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic features (4-dim), not P21's topics; about 85 songs per quarter mirrors 17,094 / 200; kernel half-width 12 quarters = P21's 3 years. Permutation null uses the maximum novelty over the series. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-C",
 "iteration": 1,
 "kind": "foote_novelty",
 "seed": 17501,
 "T": 200,
 "d": 4,
 "w": 12,
 "change_points": [
  30,
  92,
  124
 ],
 "reps": 20,
 "drift": 0.05,
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
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
