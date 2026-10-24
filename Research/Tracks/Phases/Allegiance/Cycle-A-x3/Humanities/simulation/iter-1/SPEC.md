# SIM-AL-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Counterfactual equal prestige: if each case's two prestige values were replaced by their mean (as P50 found for Montreal and Catalonia), does the flow still run minority-to-majority in every case?

## Phase operationalization tested
HUM Allegiance = language loyalty without a prestige gap.

## Sources this run draws on
P50 (Yang et al. 2025, read in full in AL0): Eq. 4.4, reported s1, s2, r12, r21; equal prestige in Montreal and Catalonia attributed to language policy. P30 (read in full in INA): exponent form.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | minority equilibrium > 0.01 |
| H2 | hypothesis | minority-to-majority rate larger in every case |
| H3 | hypothesis | P30 form as AL0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by arithmetic: with equal prestige the flow direction is set by r12 vs r21, and P50's USA case has r12 < r21, so H2 was expected not to hold for the USA.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-A",
 "iteration": 1,
 "kind": "language_markov",
 "seed": 25501,
 "dt": 0.01,
 "T": 3000,
 "T2": 2000,
 "cases": {
  "Canada": [
   0.36234999999999995,
   0.36234999999999995,
   0.2343,
   0.1662
  ],
  "USA": [
   0.6622,
   0.6622,
   0.1067,
   0.1716
  ],
  "Wales": [
   0.10345,
   0.10345,
   0.2137,
   0.0599
  ],
  "Scotland": [
   0.8783000000000001,
   0.8783000000000001,
   0.0113,
   0.0009
  ]
 },
 "u_x": 0.4,
 "a_values": [
  0.0,
  0.5,
  1.0,
  1.31
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
