# SIM-DV-FOR-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
p = 0.999: divergent, yet is S_1e6 still below 20?

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3).

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC).

## Refinement from previous iteration
Derived from SIM-DV-FOR-C iteration 3: only p and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | S_1e6 within integral bounds |
| H1 | hypothesis | S_1e6 below 20 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Threshold 20 set by the agent before running (about 1.4 x H_1e6). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-D",
 "iteration": 3,
 "kind": "series_suite",
 "seed": 18203,
 "mode": "slow_p",
 "p": 0.999,
 "h1": 20.0
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
