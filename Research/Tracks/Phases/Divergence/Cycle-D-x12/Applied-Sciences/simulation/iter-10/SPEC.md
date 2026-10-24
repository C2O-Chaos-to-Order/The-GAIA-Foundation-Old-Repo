# SIM-DV-APP-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same with noisier times (noise 6).

## Phase operationalization tested
APP Divergence = divergent thinking, the generation of many ideas to an open-ended problem, measured by fluency, originality and flexibility (P24); its scores are design-process measures.

## Sources this run draws on
P24 (Barbot 2018, 'The Dynamics of Creative Ideation: Introducing a New Assessment Paradigm', Frontiers in Psychology 9:2529, CC BY; read in full in DVD).

## Refinement from previous iteration
Only noise and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean originality-cost estimate unbiased within 4 SE |
| H1 | hypothesis | per-person estimates correlate with true cost > 0.8 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy; P24 proposes the growth model but reports no data (its subjects are fictive). 18 trials as in P24 Figure 2. Time units arbitrary. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 10,
 "kind": "mtci_growth",
 "seed": 18410,
 "trials": 18,
 "persons": 300,
 "b0": 10,
 "sd_b0": 3,
 "b1": 0.2,
 "sd_b1": 0.1,
 "c": 8,
 "sd_c": 3,
 "noise": 6,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_app.py iter-10` (run from `Applied-Sciences/simulation/`)
