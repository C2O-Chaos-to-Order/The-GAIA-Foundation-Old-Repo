# SIM-AL-NAT-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Four equal components spread over two decades (1.2, 5, 30, 136): minimum slope below 0.6?

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
| H2 | hypothesis | minimum slope below 0.6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Variant.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-D",
 "iteration": 8,
 "kind": "mixture_hill",
 "seed": 28108,
 "sets": {
  "four": [
   [
    0.25,
    1.2
   ],
   [
    0.25,
    5
   ],
   [
    0.25,
    30
   ],
   [
    0.25,
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
   "minimum slope below 0.6",
   "o['four']['n_min'] < 0.6"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-8` (run from `Natural-Sciences/simulation/`)
