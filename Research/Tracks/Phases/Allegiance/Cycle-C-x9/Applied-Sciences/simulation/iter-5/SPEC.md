# SIM-AL-APP-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P54's HDRS time x treatment estimate -1.50 [-4.25, 1.26]: does its CI exclude differences of 3 HDRS points, and did it have 80% power for 3 points?

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
| H1 | hypothesis | CI lies within (-3, 3) |
| H2 | hypothesis | power >= 0.8 for 3 points |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal approximation (SE about 1.41). Foreknowledge by hand: power for 3 points about 0.57; 3 points is the agent's choice of a clinically relevant margin.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-C",
 "iteration": 5,
 "kind": "ci_power",
 "seed": 27405,
 "coefs": {
  "HDRS": [
   -1.5,
   -4.25,
   1.26
  ]
 },
 "delta_values": [
  1.0,
  2.0,
  3.0
 ],
 "margin": 3.0,
 "target": "HDRS",
 "h1_text": "CI lies within (-3, 3)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 for 3 points",
 "h2_expr": "t['power']['3.0'] >= 0.8"
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
