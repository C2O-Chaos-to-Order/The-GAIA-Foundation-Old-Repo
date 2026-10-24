# SIM-DV-FOR-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Reproduce P23's printed partial sums (harmonic S_1000 = 7.485470861; S_10 of 1/k^2 = 1.549767731) and show that the harmonic divergence is logarithmic (H_n - ln n approaches Euler's gamma).

## Phase operationalization tested
FOR Divergence = a series whose partial sums do not converge (P23 Definition 8.3.3).

## Sources this run draws on
P23 (Boelkins, Austin & Schlicker, Active Calculus 1st ed., section 8.3 'Series of Real Numbers', activecalculus.org; read in full in DVC). Euler's gamma is standard (not from P23).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | S_1000 = 7.485470861 (1e-9) |
| V2 | validation | S_10 = 1.549767731 (1e-9) |
| H1 | hypothesis | H_1e6 - ln 1e6 within 1e-3 of gamma |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Floating-point sums (reverse order). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-C",
 "iteration": 1,
 "kind": "series_suite",
 "seed": 17201,
 "mode": "source_values",
 "h1": 0.001
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
