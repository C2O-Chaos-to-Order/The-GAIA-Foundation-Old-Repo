# SIM-IN-APP-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-APP iter-1 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
APP Insurgence = a technical system tipping into failure: by noise (N-tipping) or by a parameter crossing a fold (B-tipping) (P41).

## Sources this run draws on
P41 (Hessler & Kamps 2025, Nat Commun 16:6246, CC BY 4.0; read in full in INC): Eq. 2 N-tipping dataset (h = nu x - x^3, noise ramp, N-tipping at t = 1386.8 in one realisation), Eq. 3 fold drift h = r + x - x^3; 1996 Western Interconnection blackout: noise level rose about 2 min before the 15:42:03 line trip; CSD indicators fail for N-tipping. The least-squares estimator is the agent's, not P41's Bayesian BLE.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | internal check of Eq. 2 |
| H1 | hypothesis | median < 1750 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-D",
 "iteration": 1,
 "kind": "ntipping",
 "seed": 23401,
 "mode": "switch",
 "reps": 200,
 "h1_text": "median switch time before t = 1750 (during the ramp)",
 "h1_expr": "r['median_switch_t'] < 1750"
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
