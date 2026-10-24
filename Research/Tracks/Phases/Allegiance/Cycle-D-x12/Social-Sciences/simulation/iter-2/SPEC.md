# SIM-AL-SOC-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P66's PRISMA flow and effect-type counts: do the printed totals follow (434 - 252 = 182; 182 - 102 = 80; 80 - 1 = 79; 79 - 52 = 27; 27 + 28 = 55), and do the converted-effect counts 62 + 15 + 21 add to the 106 effects?

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
| H1 | hypothesis | PRISMA steps add up exactly |
| H2 | hypothesis | effect-type counts add to 106 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge from reading: 62 + 15 + 21 = 98, so H2 was expected not supported.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-D",
 "iteration": 2,
 "kind": "summary_audit",
 "seed": 28302,
 "hyps": [
  [
   "PRISMA steps add up exactly",
   "all(abs(o['sums'][k]['diff']) < 1e-9 for k in ['screened', 'sought', 'assessed', 'published', 'reports'])"
  ],
  [
   "effect-type counts add to 106",
   "abs(o['sums']['effect_types']['diff']) < 1e-9"
  ]
 ],
 "sums": {
  "screened": {
   "parts": [
    213,
    181,
    40,
    -252
   ],
   "printed": 182
  },
  "sought": {
   "parts": [
    182,
    -102
   ],
   "printed": 80
  },
  "assessed": {
   "parts": [
    80,
    -1
   ],
   "printed": 79
  },
  "published": {
   "parts": [
    79,
    -18,
    -12,
    -2,
    -1,
    -19
   ],
   "printed": 27
  },
  "reports": {
   "parts": [
    27,
    28
   ],
   "printed": 55
  },
  "effect_types": {
   "parts": [
    62,
    15,
    21
   ],
   "printed": 106
  }
 }
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
