# SIM-IN-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Do P32's fitted negative binomial (mean 0.88, k 0.27) and its reported shares agree: zero secondary cases 67%, > 5 3%, top 17% producing 80%?

## Phase operationalization tested
APP Insurgence = emergence driven by a few superspreaders (P32).

## Sources this run draws on
P32 (McKee et al. 2024, Epidemiol Infect 152:e121, CC BY; read in full in INB): 9,591 index cases, 67% zero secondary cases, 3% > 5, negative binomial mean 0.88, k 0.27, top 17% produce 80%.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | zero share vs analytic |
| H1 | hypothesis | zero within 0.02 |
| H2 | hypothesis | > 5 within 0.02 |
| H3 | hypothesis | top-80% within 0.02 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Samples of 9,591 index cases, 200 replicates; checks P32's internal consistency, not its data. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-B",
 "iteration": 1,
 "kind": "offspring_profile",
 "seed": 21401,
 "m": 0.88,
 "k": 0.27,
 "n": 9591,
 "reps": 200,
 "tol": 0.02,
 "p_zero": 0.67,
 "p_gt5": 0.03,
 "p_top80": 0.17
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
