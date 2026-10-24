# SIM-DV-FOR-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
p = 1.001: after a million terms, how little of zeta(1.001) is reached?

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3). Contrast: convergence is a limit property, invisible in finite data.

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC). (p-series converge iff p > 1, Activity 8.3.6; Integral Test). zeta from scipy.

## Refinement from previous iteration
Derived from SIM-DV-FOR-C iteration 2: only p and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | S_1e6 inside the integral-test bracket |
| H1 | hypothesis | S_1e6 below half the limit |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's choice of p; threshold 0.5 set before running. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-D",
 "iteration": 1,
 "kind": "series_suite",
 "seed": 18201,
 "mode": "slow_p",
 "p": 1.001,
 "h1": 0.5
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
