# SIM-SOUL-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K03 reports agreement shares for five mind-brain positions that sum to 219% (items were rated separately). What do these marginals force about how many neuroscientists agree with both reductive physicalism and dualism?

## Sources this run draws on
K03 (Navarro-Pena et al. 2026, PNAS; 2,657 neuroscientists): 63.62% reductive physicalism, 36.68% dualism, 42.94% nonreductive physicalism, 40.94% dual-aspect monism, 34.69% functionalism.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LP pair bounds = Frechet bounds |
| H1 | hypothesis | marginals force >= 10% co-endorsing reductive physicalism and dualism |
| H2 | hypothesis | marginals force >= 25% endorsing two or more positions |
| R1 | reporting | co-endorsement if independent |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic linear programme over the 32 agreement patterns; uses only published marginals (K03's cross-tabulations were not read).

## Parameters
```json
{
 "sim_id": "SIM-SOUL-A",
 "iteration": 2,
 "kind": "marginals_bounds",
 "seed": 202,
 "marginals": {
  "reductive_physicalism": 0.6362,
  "dualism": 0.3668,
  "nonreductive_physicalism": 0.4294,
  "dual_aspect_monism": 0.4094,
  "functionalism": 0.3469
 },
 "pair": [
  "reductive_physicalism",
  "dualism"
 ]
}
```

## Command
`python sim_soul.py iter-2` (run from `Soul/simulation/`)
