# SIM-AL-APP-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P49 design with K = 94 (twice as many studies): power still < 0.5?

## Phase operationalization tested
APP Allegiance = power with more studies.

## Sources this run draws on
P49 (read in full in AL0): beta -0.183, SE 0.125.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | analytic power < 0.5 |
| H2 | hypothesis | SE within 20% of 0.125 and power within 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Design values the agent's; H2 expected not supported because SE shrinks.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-C",
 "iteration": 8,
 "kind": "meta_power",
 "seed": 27408,
 "beta_rep": -0.183,
 "se_rep": 0.125,
 "p_rep": 0.144,
 "K": 94,
 "pi": 0.3,
 "tau": 0.25,
 "beta_true": -0.183,
 "b0": 0.3,
 "s_lo": 0.2,
 "s_hi": 0.4,
 "reps": 4000
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
