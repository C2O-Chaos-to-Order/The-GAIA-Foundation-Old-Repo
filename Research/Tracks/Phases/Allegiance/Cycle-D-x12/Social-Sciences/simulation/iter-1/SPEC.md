# SIM-AL-SOC-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P66 back-transforms Fisher-z CIs to r: are its printed CIs symmetric on the z scale (within 0.01) for six estimates, and visibly asymmetric on the r scale for Italy (r .74)?

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
| H1 | hypothesis | all six symmetric on the z scale within 0.01 |
| H2 | hypothesis | Italy asymmetric on the r scale by more than 0.01 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Fisher-z extension of summary_audit added in ALD (smoke-tested at seed 99 on a single estimate). New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-D",
 "iteration": 1,
 "kind": "summary_audit",
 "seed": 28301,
 "hyps": [
  [
   "all six symmetric on the z scale within 0.01",
   "all(abs(v['asym_z']) < 0.01 for v in o['fisher'].values())"
  ],
  [
   "Italy asymmetric on the r scale by more than 0.01",
   "abs(o['fisher']['italy']['asym_r']) > 0.01"
  ]
 ],
 "fisher": {
  "model1": [
   0.495,
   0.461,
   0.528
  ],
  "italy": [
   0.74,
   0.66,
   0.8
  ],
  "outgroup": [
   0.62,
   0.47,
   0.73
  ],
  "verbal": [
   0.52,
   0.48,
   0.55
  ],
  "collective": [
   0.61,
   0.49,
   0.71
  ],
  "difi": [
   0.33,
   0.06,
   0.55
  ]
 }
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
