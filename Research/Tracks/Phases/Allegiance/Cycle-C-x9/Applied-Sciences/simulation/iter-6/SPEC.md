# SIM-AL-APP-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P54's BDI estimate -0.12 [-0.76, 0.53]: does the CI lie within (-1, 1), and is power >= 0.8 for 1 unit?

## Phase operationalization tested
APP Allegiance = informativeness of an allegiance-balanced trial's null (P54).

## Sources this run draws on
P54 (Malkomsen et al. 2025, STPP vs CBT for depression, BMC Psychiatry, PMC11817821, CC BY; read in full in ALC): power statement 0.84 for d 0.6 with N 100; HDRS time x treatment -1.50 [-4.25, 1.26]; BDI -0.12 [-0.76, 0.53]; response OR 0.59 [0.24, 1.42]; between-group d HDRS 0.27, BDI 0.14, WSAS 0.39; 81 evaluated at 28 weeks (39 CBT, 42 STPP); balanced-allegiance steering group.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CI lies within (-1, 1) |
| H2 | hypothesis | power >= 0.8 for 1 unit |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Units as printed in P54's model (agent did not re-derive the scale).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-C",
 "iteration": 6,
 "kind": "ci_power",
 "seed": 27406,
 "coefs": {
  "BDI": [
   -0.12,
   -0.76,
   0.53
  ]
 },
 "delta_values": [
  0.5,
  1.0
 ],
 "margin": 1.0,
 "target": "BDI",
 "h1_text": "CI lies within (-1, 1)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 for 1 unit",
 "h2_expr": "t['power']['1.0'] >= 0.8"
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
