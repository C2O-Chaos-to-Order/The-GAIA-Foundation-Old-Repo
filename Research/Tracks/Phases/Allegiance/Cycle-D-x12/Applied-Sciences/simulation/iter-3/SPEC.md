# SIM-AL-APP-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P66's test of publication status on the main effect (.02 [-.08, .13]): CI within +/-0.15, power >= 0.8 for 0.2?

## Phase operationalization tested
APP Allegiance = publication status and theory originators in a meta-analysis (P66).

## Sources this run draws on
P66 (Varmann, Kruse, Bierwiaczonek, Gomez, Vazquez & Kunst 2023, 'How identity fusion predicts extreme pro-group orientations: A meta-analysis', Eur Rev Soc Psychol 35:162-197; free PDF on the UNED Identity Fusion project site; read in full in ALD): Model 1 r = .495 [.461, .528]; Fig. 1 PRISMA counts; effect conversions k = 62, 15, 21 of 106 effects; moderator estimates with CIs.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CI within (-0.15, 0.15) |
| H2 | hypothesis | power >= 0.8 for 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-D",
 "iteration": 3,
 "kind": "ci_power",
 "seed": 28403,
 "coefs": {
  "pub_status": [
   0.02,
   -0.08,
   0.13
  ]
 },
 "delta_values": [
  0.1,
  0.2
 ],
 "margin": 0.15,
 "target": "pub_status",
 "h1_text": "CI within (-0.15, 0.15)",
 "h1_expr": "t['excludes_margin']",
 "h2_text": "power >= 0.8 for 0.2",
 "h2_expr": "t['power']['0.2'] >= 0.8"
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
