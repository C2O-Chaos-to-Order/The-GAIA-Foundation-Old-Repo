# SIM-DV-FOR-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P23 Exercise 7: two divergent series can sum term by term to a convergent one (a_n = 1 + 2^-n, b_n = -1).

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3). Divergence is not preserved under addition.

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC). (Exercise 7).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sum of (a+b) = 2 - 2^-(n-1) (1e-9) |
| H1 | hypothesis | components exceed n/2 while sum < 2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic, n = 10,000 terms. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-C",
 "iteration": 5,
 "kind": "series_suite",
 "seed": 17205,
 "mode": "sum_of_divergent",
 "n": 10000
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
