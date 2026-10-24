# SIM-AL-NAT-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
TTS with the tertiary t affinity raised 60-fold (K_t 1.2 instead of 0.02): does cooperativity drop below 2.3?

## Phase operationalization tested
NAT Allegiance = TTS cooperativity when T-state affinity shifts (P62).

## Sources this run draws on
P53 (Eaton 2022, read in full in ALA): MWC Eq. (4), TTS Eq. (13) and approximate values. P46 (read in full in AL0): Hb n = 2.8. P62 (Shibayama 2025, 'Analysis of beta-C-terminal salt bridges in T-state hemoglobin by trapping tertiary conformations in silica gels', Protein Sci 34:e70193, PMC12168133, CC BY-NC; read in full in ALC): anion-free T state biphasic, two non-cooperative components K 1.2 +- 0.3 torr (18 +- 2%) and 136 +- 8 torr (82 +- 2%); with IHP Hill n 0.85 +- 0.01, P50 135 +- 4 torr; effectors alter K_T 'by up to ~60-fold'; TTS predicts an r fraction below 1% with affinity about 0.20 torr.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end slopes 1 |
| H2 | hypothesis | max slope within 0.5 of 2.8 |
| H3 | hypothesis | max slope varies by > 0.1 over L |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's variant; K_t 1.2 exceeds K_r 5 / 4, so the tertiary contrast nearly vanishes.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-C",
 "iteration": 6,
 "kind": "mwc_binding",
 "seed": 27106,
 "model": "TTS",
 "params": {
  "l_T": 200,
  "l_R": 0.3,
  "K_t": 1.2,
  "K_r": 5.0
 },
 "L": 1000000.0,
 "L_values": [
  100000.0,
  1000000.0,
  10000000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
