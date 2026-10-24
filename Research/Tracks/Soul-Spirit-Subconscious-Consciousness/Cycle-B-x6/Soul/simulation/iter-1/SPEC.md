# SIM-SOUL-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Extend SIM-SOUL-A iteration 2 to all ten pairs of K03's five mind-brain positions: does any pair have to be co-endorsed by at least 10% of neuroscientists?

## Sources this run draws on
K03 (Navarro-Pena et al. 2026): five agreement marginals.

## Refinement from previous iteration
Cycle A tested only reductive physicalism + dualism.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LP = Frechet |
| H1 | hypothesis | some pair forced >= 10% |
| R1 | reporting | all pairs |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; marginals only.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 1,
 "kind": "marginals_pairs",
 "seed": 211,
 "marginals": {
  "reductive_physicalism": 0.6362,
  "dualism": 0.3668,
  "nonreductive_physicalism": 0.4294,
  "dual_aspect_monism": 0.4094,
  "functionalism": 0.3469
 },
 "pair": [
  "reductive_physicalism",
  "nonreductive_physicalism"
 ],
 "h1_threshold": 0.1
}
```

## Command
`python sim_soul.py iter-1` (run from `Soul/simulation/`)
