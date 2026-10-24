# SIM-IN-FOR-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Branching-process approximation (FOR pass 2; P27 Definition 2.4): does the share of Poisson(c) Galton-Watson processes reaching 1,000 individuals match s = 1 - exp(-cs) for c = 1.1, 1.5, 2, 3?

## Phase operationalization tested
FOR Insurgence = a lineage escaping extinction; P27 links component sizes to branching processes.

## Sources this run draws on
P27 (read in full in IN0), section 2.4 'Component Sizes and the Branching Process Approximation'.

## Refinement from previous iteration
Follows iter-1 (critical window): checks the branching-process link behind P27's Eq. 2.2.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares are probabilities |
| H1 | hypothesis | within 4 SE + 0.01 of s for every c |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Reaching K = 1000 is a proxy for survival; near c = 1 finite K inflates the share (bias allowance 0.01 set before running). 5,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-A",
 "iteration": 2,
 "kind": "gw_survival",
 "seed": 20202,
 "c_values": [
  1.1,
  1.5,
  2.0,
  3.0
 ],
 "reps": 5000,
 "K": 1000,
 "tol_se": 4,
 "bias": 0.01
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
