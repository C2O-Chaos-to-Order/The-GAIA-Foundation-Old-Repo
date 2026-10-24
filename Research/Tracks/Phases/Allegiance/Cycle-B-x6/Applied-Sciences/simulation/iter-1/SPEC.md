# SIM-AL-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P56 found no association between developer involvement (a form of researcher allegiance) and effect size (-0.002 [-0.12, 0.11], 243 trials). Unlike P49's null, is this null informative: does its CI exclude effects larger than 0.15 and does it have >= 80% power for an effect of 0.2?

## Phase operationalization tested
APP Allegiance = developer involvement in trials (P56).

## Sources this run draws on
P56 (Leijten et al. 2026, 'Have parenting programs for disruptive child behavior become less effective?', J Child Psychol Psychiatry 67:127-137, CC BY; read in full in ALB): Table 1 coefficients with 95% CIs (developer involvement -0.002 [-0.12, 0.11], n = 243 trials).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CI excludes |effect| > 0.15 |
| H2 | hypothesis | power >= 0.8 for 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal approximation to P56's robust-variance CIs.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-B",
 "iteration": 1,
 "kind": "ci_power",
 "seed": 26401,
 "coefs": {
  "developer_involvement": [
   -0.002,
   -0.12,
   0.11
  ],
  "active_control": [
   0.17,
   0.07,
   0.27
  ],
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
 "target": "developer_involvement",
 "h1_text": "developer-involvement CI lies within (-0.15, 0.15)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 to detect 0.2",
 "h2_expr": "t['power']['0.2'] >= 0.8"
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
