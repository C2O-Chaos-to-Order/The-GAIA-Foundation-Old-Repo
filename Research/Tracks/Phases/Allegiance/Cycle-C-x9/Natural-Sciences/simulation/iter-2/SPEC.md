# SIM-AL-NAT-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
With IHP P62 reports a Hill n of 0.85: can an equal two-component mixture reproduce n 0.85 at P50 with a K ratio between 2 and 20, and does the slope at P50 fall monotonically with the K ratio?

## Phase operationalization tested
NAT Allegiance = apparent anti-cooperativity from heterogeneous trapped states (P62).

## Sources this run draws on
P62 (Shibayama 2025, 'Analysis of beta-C-terminal salt bridges in T-state hemoglobin by trapping tertiary conformations in silica gels', Protein Sci 34:e70193, PMC12168133, CC BY-NC; read in full in ALC): anion-free T state biphasic, two non-cooperative components K 1.2 +- 0.3 torr (18 +- 2%) and 136 +- 8 torr (82 +- 2%); with IHP Hill n 0.85 +- 0.01, P50 135 +- 4 torr; effectors alter K_T 'by up to ~60-fold'; TTS predicts an r fraction below 1% with affinity about 0.20 torr.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | no mixture has a Hill slope above 1 anywhere (heterogeneity cannot create cooperativity) |
| H2 | hypothesis | some ratio gives slope at P50 within 0.03 of 0.85 |
| H3 | hypothesis | slope at P50 decreases with the K ratio |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's equal-fraction toy; P62 does not decompose the IHP curve. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-C",
 "iteration": 2,
 "kind": "mixture_hill",
 "seed": 27102,
 "sets": {
  "ratio_2": [
   [
    0.5,
    95.4594154601839
   ],
   [
    0.5,
    190.91883092036784
   ]
  ],
  "ratio_5": [
   [
    0.5,
    60.37383539249432
   ],
   [
    0.5,
    301.8691769624716
   ]
  ],
  "ratio_10": [
   [
    0.5,
    42.690748412273116
   ],
   [
    0.5,
    426.90748412273126
   ]
  ],
  "ratio_20": [
   [
    0.5,
    30.18691769624716
   ],
   [
    0.5,
    603.7383539249432
   ]
  ]
 },
 "hyps": [
  [
   "no mixture has a Hill slope above 1 anywhere (heterogeneity cannot create cooperativity)",
   "all(v['n_max'] <= 1 + 1e-6 for v in o.values())"
  ],
  [
   "some ratio gives slope at P50 within 0.03 of 0.85",
   "any(abs(v['n_at_P50'] - 0.85) < 0.03 for v in o.values())"
  ],
  [
   "slope at P50 decreases with the K ratio",
   "o['ratio_2']['n_at_P50'] > o['ratio_5']['n_at_P50'] > o['ratio_10']['n_at_P50'] > o['ratio_20']['n_at_P50']"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
