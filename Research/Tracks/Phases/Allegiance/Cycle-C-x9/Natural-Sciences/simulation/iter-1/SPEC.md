# SIM-AL-NAT-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Hill plot of P62's two-component anion-free T state versus the TTS-predicted component set: is the slope <= 1 everywhere, does P62's mixture dip below 0.6, and do the two sets have P50 within 10% of each other?

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
| H2 | hypothesis | P62 mixture minimum slope below 0.6 |
| H3 | hypothesis | P50 of the two sets within 10% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-component sum as P62 fitted; the TTS set uses P62's quoted prediction (< 1% at about 0.20 torr), taken as 1%. Smoke test (seed 99, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); thresholds were not changed after it. Smoke showed H1 and H2 supported.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-C",
 "iteration": 1,
 "kind": "mixture_hill",
 "seed": 27101,
 "sets": {
  "P62_anion_free": [
   [
    0.18,
    1.2
   ],
   [
    0.82,
    136
   ]
  ],
  "TTS_pred": [
   [
    0.01,
    0.2
   ],
   [
    0.99,
    136
   ]
  ]
 },
 "hyps": [
  [
   "no mixture has a Hill slope above 1 anywhere (heterogeneity cannot create cooperativity)",
   "all(v['n_max'] <= 1 + 1e-6 for v in o.values())"
  ],
  [
   "P62 mixture minimum slope below 0.6",
   "o['P62_anion_free']['n_min'] < 0.6"
  ],
  [
   "P50 of the two sets within 10%",
   "abs(o['P62_anion_free']['P50'] / o['TTS_pred']['P50'] - 1) < 0.1"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
