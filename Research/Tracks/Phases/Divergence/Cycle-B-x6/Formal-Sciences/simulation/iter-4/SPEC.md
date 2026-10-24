# SIM-DV-FOR-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
How often does local uncertainty shrink in a chaotic map? Share of time the logistic map (r = 4) spends where |f'(x)| < 1, against the analytic invariant-measure value.

## Phase operationalization tested
FOR Divergence = average exponential separation that coexists with regions of local convergence (P09).

## Sources this run draws on
P09 (re-read in full in DVB): stretching and folding; P09 calls the idea that chaotic systems are unpredictable a 'myth'. Invariant density 1/(pi sqrt(x(1-x))) is standard.

## Refinement from previous iteration
New run family.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | orbit share within 4 SE of analytic |
| H1 | hypothesis | share > 0.1 |
| H2 | hypothesis | all finite-time exponents positive |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Floating-point orbits; finite-time exponents over 20,000 steps. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 4,
 "kind": "local_shrink",
 "seed": 16204,
 "orbits": 200,
 "burn": 100,
 "n": 20000,
 "tol_se": 4,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
