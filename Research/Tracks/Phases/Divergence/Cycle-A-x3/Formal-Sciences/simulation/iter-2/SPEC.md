# SIM-DV-FOR-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence of a series: harmonic partial sums grow without bound (like ln n) while p = 2 and alternating harmonic series converge.

## Phase operationalization tested
FOR Divergence = divergent series (partial sums have no finite limit).

## Sources this run draws on
No source read in this track; analytic bounds are standard (Euler-Mascheroni asymptotics, integral test, alternating-series bound).

## Refinement from previous iteration
New run family (series sense).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | |H_n - ln n - gamma| <= 1/(2n) |
| V2 | validation | p=2 tail <= 1/n |
| V3 | validation | alternating bound |
| H1 | hypothesis | H_n > 10 needs > 10,000 terms |
| R1 | reporting | first n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic floating-point sums; H1 was pre-registered by the agent from general knowledge (not a discovery).

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-A",
 "iteration": 2,
 "kind": "series_divergence",
 "seed": 15202,
 "n_values": [
  10,
  100,
  1000,
  10000,
  100000
 ],
 "target": 10,
 "h1": 10000
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
