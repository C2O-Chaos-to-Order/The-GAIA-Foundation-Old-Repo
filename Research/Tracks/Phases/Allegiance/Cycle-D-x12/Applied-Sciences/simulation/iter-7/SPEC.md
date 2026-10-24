# SIM-AL-APP-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P56's developer-involvement null at a tighter margin (0.1): CI within +/-0.1?

## Phase operationalization tested
APP Allegiance = developer involvement (P56).

## Sources this run draws on
P56 (Leijten et al. 2026, 'Have parenting programs for disruptive child behavior become less effective?', J Child Psychol Psychiatry 67:127-137, CC BY; read in full in ALB): Table 1 coefficients with 95% CIs (developer involvement -0.002 [-0.12, 0.11], n = 243 trials).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CI within (-0.1, 0.1) |
| H2 | hypothesis | power >= 0.8 for 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-D",
 "iteration": 7,
 "kind": "ci_power",
 "seed": 28407,
 "coefs": {
  "developer_involvement": [
   -0.002,
   -0.12,
   0.11
  ]
 },
 "delta_values": [
  0.1,
  0.2
 ],
 "margin": 0.1,
 "target": "developer_involvement",
 "h1_text": "CI within (-0.1, 0.1)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 for 0.2",
 "h2_expr": "t['power']['0.2'] >= 0.8"
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
