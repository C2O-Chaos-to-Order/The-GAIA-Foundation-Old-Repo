# SIM-IN-NAT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noise and onset, weak noise (NAT pass 3): same as iter-2 with sigma = 0.0005 (half the seed): does the advance shrink, and is onset still variable?

## Phase operationalization tested
NAT Insurgence = onset from a seed; onset timing under weak noise.

## Sources this run draws on
As iter-2.

## Refinement from previous iteration
Follows iter-2: noise reduced tenfold to separate the noise effect from the boundary effect.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no run censored |
| H1 | hypothesis | mean onset below deterministic by > 4 SE |
| H2 | hypothesis | CV > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-2; this setting was not smoke-tested. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-A",
 "iteration": 3,
 "kind": "transcritical_noise",
 "seed": 20103,
 "r": 0.05,
 "x0": 0.001,
 "sigma": 0.0005,
 "dt": 0.05,
 "reps": 200,
 "tmax": 2000,
 "tol_se": 4,
 "h2": 0.1
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
