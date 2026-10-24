# SIM-AL-SOC-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Do P66's printed moderator estimates lie inside their own CIs (published difference .24 [.14, .33], unpublished -.01 [-.14, .12], publication status .02 [-.08, .13], matched-subset moderation .09 [-.20, .01], gender x age -.002 [-.004, -.001])?

## Phase operationalization tested
SOC Allegiance = auditing the identity-fusion meta-analysis (P66).

## Sources this run draws on
P66 (Varmann, Kruse, Bierwiaczonek, Gomez, Vazquez & Kunst 2023, 'How identity fusion predicts extreme pro-group orientations: A meta-analysis', Eur Rev Soc Psychol 35:162-197; free PDF on the UNED Identity Fusion project site; read in full in ALD): Model 1 r = .495 [.461, .528]; Fig. 1 PRISMA counts; effect conversions k = 62, 15, 21 of 106 effects; moderator estimates with CIs.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | all estimates inside their CIs |
| H2 | hypothesis | all but the matched-subset moderation inside |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge from reading: .09 lies outside [-.20, .01] (likely a sign slip).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-D",
 "iteration": 3,
 "kind": "summary_audit",
 "seed": 28303,
 "hyps": [
  [
   "all estimates inside their CIs",
   "all(v['inside'] for v in o['sign_ci'].values())"
  ],
  [
   "all but the matched-subset moderation inside",
   "all(v['inside'] for k, v in o['sign_ci'].items() if k != 'matched_mod')"
  ]
 ],
 "sign_ci": {
  "published": [
   0.24,
   0.14,
   0.33
  ],
  "unpublished": [
   -0.01,
   -0.14,
   0.12
  ],
  "pub_status": [
   0.02,
   -0.08,
   0.13
  ],
  "matched_mod": [
   0.09,
   -0.2,
   0.01
  ],
  "gender_age": [
   -0.002,
   -0.004,
   -0.001
  ]
 }
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
