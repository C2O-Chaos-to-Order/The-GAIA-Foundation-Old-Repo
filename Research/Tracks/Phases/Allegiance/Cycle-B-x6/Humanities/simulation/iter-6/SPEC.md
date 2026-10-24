# SIM-AL-HUM-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Equalizing the minority's prestige to the majority's (s1 = s2 = majority value).

## Phase operationalization tested
HUM Allegiance = language loyalty under prestige.

## Sources this run draws on
P50 (read in full in AL0): Eq. 4.4 and reported rates. P30 (read in full in INA): exponent form.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | minority equilibrium > 0.01 |
| H2 | hypothesis | minority-to-majority rate larger |
| H3 | hypothesis | P30 form: coexistence a < 1, extinction a >= 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Counterfactual.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-B",
 "iteration": 6,
 "kind": "language_markov",
 "seed": 26506,
 "T": 3000,
 "T2": 3000,
 "a_values": [
  0.0,
  0.5,
  1.0,
  1.31
 ],
 "dt": 0.01,
 "u_x": 0.4,
 "cases": {
  "Canada": [
   0.5477,
   0.5477,
   0.2343,
   0.1662
  ],
  "USA": [
   1.2553,
   1.2553,
   0.1067,
   0.1716
  ],
  "Wales": [
   0.1939,
   0.1939,
   0.2137,
   0.0599
  ],
  "Scotland": [
   0.9655,
   0.9655,
   0.0113,
   0.0009
  ]
 }
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
