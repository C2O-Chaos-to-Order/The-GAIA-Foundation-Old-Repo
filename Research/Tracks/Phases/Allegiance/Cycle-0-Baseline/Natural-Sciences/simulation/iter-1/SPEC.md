# SIM-AL-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Cooperative binding (P46): does a 4-site binding model with affinity rising as sites fill give a curved Hill plot whose ends approach slope 1 and whose slope is greatest (between 1 and 4) near half-saturation, while independent sites give slope 1 throughout?

## Phase operationalization tested
NAT Allegiance = binding: partners associating so that each bond makes the next one more likely (cooperative binding, P46).

## Sources this run draws on
P46 (Jakubowski, 'C3. Mathematical Analysis of Cooperative Binding - Hill Plot', Chemistry LibreTexts, CC BY-NC-SA 4.0; read in full in AL0): Hill equation, Kd = P50^n, Hill plot; Hb Hill plot curvilinear with end slopes 1 and slope 2.8 in the middle.

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
Deterministic. The Adair constants (0.02, 0.05, 0.2, 2.0) are the agent's choice, not haemoglobin data, and were set before the smoke test, which gave a maximum slope of 3.63 and end slopes 1.000 (one earlier smoke with steeper constants gave 3.88; the milder set was then chosen, disclosed). Adair binding polynomial is standard theory, not in P46. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-0",
 "iteration": 1,
 "kind": "hill_binding",
 "seed": 24101,
 "K_coop": [
  0.02,
  0.05,
  0.2,
  2.0
 ],
 "k_site": 1.0,
 "n_hill": 2.8,
 "P50": 26.0
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
