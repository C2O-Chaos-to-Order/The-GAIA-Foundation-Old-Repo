# SIM-DV-FOR-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Two senses together: in the Lorenz system the vector-field divergence is negative everywhere (volumes contract) while nearby trajectories diverge (positive largest Lyapunov exponent).

## Phase operationalization tested
FOR Divergence = div F (operator sense) vs trajectory divergence (dynamical sense).

## Sources this run draws on
No source read for the Lorenz system in this track; div F = -(sigma+1+beta) is a direct computation. P09 (re-read) for stretching and folding in general.

## Refinement from previous iteration
New run family linking the DVA operator run to the dynamical sense.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | FD divergence = -(sigma+1+beta) within 1e-6 |
| H1 | hypothesis | lambda_max > 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
RK4 with dt 0.01, one trajectory pair, T = 500. The 0.5 threshold is the agent's choice (a commonly quoted value near 0.9 is not sourced here). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 5,
 "kind": "lorenz_div",
 "seed": 16205,
 "sigma": 10.0,
 "rho": 28.0,
 "beta": 2.6666666666666665,
 "fd_points": 200,
 "fd_h": 0.0001,
 "fd_tol": 1e-06,
 "dt": 0.01,
 "burn": 50,
 "T": 500,
 "d0": 1e-08,
 "h1": 0.5,
 "h1_dir": "gt"
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
