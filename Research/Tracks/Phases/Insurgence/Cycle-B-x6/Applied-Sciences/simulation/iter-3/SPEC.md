# SIM-IN-APP-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Outbreak emergence with P32's dispersion k = 0.27 at R0 = 0.88 (P32's mean), 1.5, 2.5: major-outbreak share vs 1 - q.

## Phase operationalization tested
APP Insurgence = emergence with observed heterogeneity.

## Sources this run draws on
P32 (McKee et al. 2024, Epidemiol Infect 152:e121, CC BY; read in full in INB): 9,591 index cases, 67% zero secondary cases, 3% > 5, negative binomial mean 0.88, k 0.27, top 17% produce 80%. Branching model standard (not from P32).

## Refinement from previous iteration
Iteration 3 of the x6 family for APP; follows iteration 2 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
20,000 replicates; mixing of P32's k with other R0 values is the agent's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-B",
 "iteration": 3,
 "kind": "branching_outbreak",
 "seed": 21403,
 "R0": [
  0.88,
  1.5,
  2.5
 ],
 "k": 0.27,
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
