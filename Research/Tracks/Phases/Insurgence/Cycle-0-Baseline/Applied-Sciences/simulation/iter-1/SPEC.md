# SIM-IN-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P26's threshold reading (an outbreak continues if R0 > 1 and ends if R0 < 1) in a branching-process model: share of major outbreaks (1000 cases) for R0 = 0.8, 1.5, 3 vs 1 - q, and P26's point that R0 is not a rate (same R0, generation time 3 vs 15 days).

## Phase operationalization tested
APP Insurgence = emergence of an outbreak from one case when each case causes more than one new case on average (P26).

## Sources this run draws on
P26 (Delamater et al. 2019, Emerg Infect Dis 25(1):1-4, public domain; read in full in IN0). The branching model and q = exp(R0(q-1)) are standard (not from P26).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share within 4 SE of 1 - q |
| H1 | hypothesis | no major outbreak at R0 < 1 |
| H2 | hypothesis | calendar time scales with generation time |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Homogeneous Poisson offspring, fully susceptible population (the definition of R0 in P26); 20,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-0",
 "iteration": 1,
 "kind": "branching_outbreak",
 "seed": 19401,
 "R0": [
  0.8,
  1.5,
  3.0
 ],
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
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
