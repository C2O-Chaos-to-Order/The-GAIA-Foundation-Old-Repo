# SIM-AL-NAT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Adair variant with mild cooperativity (stepwise constants 0.1, 0.2, 0.4, 1.0): does the Hill plot keep end slopes 1 and a central maximum between 1 and 4?

## Phase operationalization tested
NAT Allegiance = cooperative binding (mild).

## Sources this run draws on
P46 (read in full in AL0): Hill plot ends approach slope 1, maximal cooperativity in the middle.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end slopes within 0.05 of 1 |
| H2 | hypothesis | max slope in (1, 4) within 0.5 log units of P50 |
| H3 | hypothesis | independent sites slope 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent-chosen constants.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-A",
 "iteration": 3,
 "kind": "hill_binding",
 "seed": 25103,
 "K_coop": [
  0.1,
  0.2,
  0.4,
  1.0
 ],
 "k_site": 1.0,
 "n_hill": 1.5,
 "P50": 5.0
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
