# SIM-AL-APP-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P56's delivery-staff coefficient (0.11 [0.005, 0.23]): significant, and would a 0.1 effect be detected with >= 50% power?

## Phase operationalization tested
APP Allegiance = investigator-team delivery (P56).

## Sources this run draws on
P56 (Leijten et al. 2026, 'Have parenting programs for disruptive child behavior become less effective?', J Child Psychol Psychiatry 67:127-137, CC BY; read in full in ALB): Table 1 coefficients with 95% CIs (developer involvement -0.002 [-0.12, 0.11], n = 243 trials).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | p < 0.05 |
| H2 | hypothesis | power >= 0.5 for 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-B",
 "iteration": 4,
 "kind": "ci_power",
 "seed": 26404,
 "coefs": {
  "delivery_staff": [
   0.11,
   0.005,
   0.23
  ]
 },
 "delta_values": [
  0.1,
  0.2,
  0.3
 ],
 "margin": 0.15,
 "target": "delivery_staff",
 "h1_text": "p < 0.05",
 "h1_expr": "t['p'] < 0.05",
 "h2_text": "power >= 0.5 to detect 0.1",
 "h2_expr": "t['power']['0.1'] >= 0.5"
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
