# SIM-AL-APP-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P49's allegiance moderator at a wide margin (0.45): CI within +/-0.45, power >= 0.8 for 0.3?

## Phase operationalization tested
APP Allegiance = informativeness of P49's null.

## Sources this run draws on
P49 (read in full in AL0): beta -0.183, SE 0.125.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CI within (-0.45, 0.45) |
| H2 | hypothesis | power >= 0.8 for 0.3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-D",
 "iteration": 8,
 "kind": "ci_power",
 "seed": 28408,
 "coefs": {
  "allegiance_P49": [
   -0.183,
   -0.428,
   0.062
  ]
 },
 "delta_values": [
  0.2,
  0.3
 ],
 "margin": 0.45,
 "target": "allegiance_P49",
 "h1_text": "CI within (-0.45, 0.45)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 for 0.3",
 "h2_expr": "t['power']['0.3'] >= 0.8"
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
