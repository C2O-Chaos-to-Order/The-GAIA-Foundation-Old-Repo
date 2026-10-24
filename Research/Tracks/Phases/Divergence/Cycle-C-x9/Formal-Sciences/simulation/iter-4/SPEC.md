# SIM-DV-FOR-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P23 Activity 8.3.9 / Ratio Test: 2^k/(3^k - k) has successive-term ratio approaching 2/3, so it converges.

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3).

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC). (Ratio Test).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ratio within 1e-3 of 2/3 at k = 25 |
| H1 | hypothesis | partial sums settle (1e-3) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-C",
 "iteration": 4,
 "kind": "series_suite",
 "seed": 17204,
 "mode": "ratio"
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
