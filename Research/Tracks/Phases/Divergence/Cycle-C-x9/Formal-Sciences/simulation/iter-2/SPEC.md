# SIM-DV-FOR-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
A convergent series can look divergent: p = 1.01. After a million terms, how much of zeta(1.01) has been reached?

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3). Contrast: convergence is a limit property, invisible in finite data.

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC). (p-series converge iff p > 1, Activity 8.3.6; Integral Test). zeta from scipy.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | S_1e6 inside the integral-test bracket |
| H1 | hypothesis | S_1e6 below half the limit |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's choice of p; threshold 0.5 set before running. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-C",
 "iteration": 2,
 "kind": "series_suite",
 "seed": 17202,
 "mode": "slow_p",
 "p": 1.01,
 "h1": 0.5
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
