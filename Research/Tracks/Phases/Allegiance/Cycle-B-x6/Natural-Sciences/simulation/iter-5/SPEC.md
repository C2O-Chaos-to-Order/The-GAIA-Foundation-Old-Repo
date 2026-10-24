# SIM-AL-NAT-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
MWC with a weaker affinity contrast (K_T 0.01, K_R 1; c = 0.01) and L = 1e4 = 1/c^2: is the maximal slope lower than with c = 0.001?

## Phase operationalization tested
NAT Allegiance = MWC cooperativity versus affinity contrast.

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
| H3 | hypothesis | max slope varies by > 0.1 over L = 1e2, 1e4, 1e6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's parameter choice; not haemoglobin values.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-B",
 "iteration": 5,
 "kind": "mwc_binding",
 "seed": 26105,
 "model": "MWC",
 "params": {
  "K_T": 0.01,
  "K_R": 1.0
 },
 "L": 10000.0,
 "L_values": [
  100.0,
  10000.0,
  1000000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5
}
```

## Command
`python sim_nat.py iter-5` (run from `Natural-Sciences/simulation/`)
