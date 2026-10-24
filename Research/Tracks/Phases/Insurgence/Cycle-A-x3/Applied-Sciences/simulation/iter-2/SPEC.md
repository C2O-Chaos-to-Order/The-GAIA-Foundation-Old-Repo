# SIM-IN-APP-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Superspreading (APP pass 2; P26 cautions that R0 hides heterogeneity): with negative-binomial offspring (dispersion k = 0.1) and the same R0 = 0.8, 1.5, 3, how much lower is the major-outbreak share than under Poisson (IN0-APP-02)?

## Phase operationalization tested
APP Insurgence = outbreak emergence with heterogeneous transmission.

## Sources this run draws on
P26 (read in full in IN0) for R0's limits; the negative-binomial offspring model and its extinction equation q = (1 + R0(1-q)/k)^(-k) are standard (not from P26).

## Refinement from previous iteration
Follows iter-1 (near threshold): heterogeneity of transmission.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales with generation time |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
k = 0.1 is illustrative, not an estimate for any pathogen. 20,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-A",
 "iteration": 2,
 "kind": "branching_outbreak",
 "seed": 20402,
 "R0": [
  0.8,
  1.5,
  3.0
 ],
 "k": 0.1,
 "reps": 20000,
 "K": 1000,
 "Tg": [
  3,
  15
 ],
 "tol_se": 4
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
