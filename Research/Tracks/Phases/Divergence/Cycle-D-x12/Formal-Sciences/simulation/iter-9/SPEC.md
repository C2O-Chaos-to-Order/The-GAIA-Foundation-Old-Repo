# SIM-DV-FOR-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Lorenz exponent with d0 = 1e-8 and a new seed (compare DVC 1e-10).

## Phase operationalization tested
FOR Divergence = div F vs trajectory divergence.

## Sources this run draws on
Direct computation; P09 for stretching and folding.

## Refinement from previous iteration
Derived from SIM-DV-FOR-C iteration 9: d0 and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | FD divergence = -(sigma+1+beta) within 1e-6 |
| H1 | hypothesis | lambda_max > 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-D",
 "iteration": 9,
 "kind": "lorenz_div",
 "seed": 18209,
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
`python sim_for.py iter-9` (run from `Formal-Sciences/simulation/`)
