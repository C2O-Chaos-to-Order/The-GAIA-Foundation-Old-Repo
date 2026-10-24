# SIM-IN-APP-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Vaccination (APP pass 3): with a share v = 0.6 immune, offspring Poisson(R0 (1 - v)) for R0 = 2, 3, 4 (R = 0.8, 1.2, 1.6): is there no major outbreak at R = 0.8 and does the share follow 1 - q at the reduced R?

## Phase operationalization tested
APP Insurgence = outbreak emergence suppressed by immunity (effective reproduction number).

## Sources this run draws on
P26 (read in full in IN0): R0 assumes a fully susceptible population; the reduction R0 (1 - v) for random immunity is standard (not from P26).

## Refinement from previous iteration
Follows iter-2: immunity lowers the reproduction number.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales with generation time |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Random, perfect immunity; homogeneous mixing. 20,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-A",
 "iteration": 3,
 "kind": "branching_outbreak",
 "seed": 20403,
 "R0": [
  2.0,
  3.0,
  4.0
 ],
 "v": 0.6,
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
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
