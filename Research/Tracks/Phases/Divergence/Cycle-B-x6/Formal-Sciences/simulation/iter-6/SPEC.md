# SIM-DV-FOR-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Control: at rho = 14 (below the chaotic regime) the same negative field divergence should accompany converging trajectories (largest exponent < 0).

## Phase operationalization tested
As iteration 5.

## Sources this run draws on
As iteration 5.

## Refinement from previous iteration
Only rho, the hypothesis direction and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | FD divergence = -(sigma+1+beta) within 1e-6 |
| H1 | hypothesis | lambda_max < 0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 5. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 6,
 "kind": "lorenz_div",
 "seed": 16206,
 "sigma": 10.0,
 "rho": 14.0,
 "beta": 2.6666666666666665,
 "fd_points": 200,
 "fd_h": 0.0001,
 "fd_tol": 1e-06,
 "dt": 0.01,
 "burn": 50,
 "T": 500,
 "d0": 1e-08,
 "h1": 0.0,
 "h1_dir": "lt"
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
