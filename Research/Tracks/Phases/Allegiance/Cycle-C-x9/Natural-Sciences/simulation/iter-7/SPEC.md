# SIM-AL-NAT-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
MWC with P53's values over a narrow L range around 1/c^2 (1e5, 1e6, 1e7): does the maximal slope still vary by more than 0.1?

## Phase operationalization tested
NAT Allegiance = MWC cooperativity near the optimum L.

## Sources this run draws on
P53 (Eaton 2022, read in full in ALA): MWC Eq. (4), TTS Eq. (13) and approximate values. P46 (read in full in AL0): Hb n = 2.8.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end slopes 1 |
| H2 | hypothesis | max slope within 0.5 of 2.8 |
| H3 | hypothesis | max slope varies by > 0.1 over L |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by reasoning: near the optimum the slope is flat in L, so H3 may fail.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-C",
 "iteration": 7,
 "kind": "mwc_binding",
 "seed": 27107,
 "model": "MWC",
 "params": {
  "K_T": 0.001,
  "K_R": 1.0
 },
 "L": 1000000.0,
 "L_values": [
  100000.0,
  1000000.0,
  10000000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5
}
```

## Command
`python sim_nat.py iter-7` (run from `Natural-Sciences/simulation/`)
