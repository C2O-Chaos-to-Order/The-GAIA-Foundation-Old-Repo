# SIM-DV-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as opinion fragmentation: does bounded confidence split a population into several clusters while wide confidence yields consensus?

## Phase operationalization tested
SOC Divergence = fragmentation/polarisation of opinions into separated clusters (P03, bounded-confidence agent-based model).

## Sources this run draws on
P03 (bounded assimilative influence: opinions fragment into two or more converging clusters; noisy and event-driven variants).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean opinion conserved (noise 0) |
| H1 | hypothesis | eps 0.5 -> consensus in every replicate |
| H2 | hypothesis | eps 0.15 -> mean clusters in [2, 4] |
| R1 | reporting | clusters per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Classic noise-free Deffuant model; no network structure, no external events (P03's mechanism is not yet modelled; planned for x3). Cluster count depends on the gap/min-share rule.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-0",
 "iteration": 1,
 "kind": "deffuant",
 "seed": 1503,
 "agents": 500,
 "eps_values": [
  0.15,
  0.5
 ],
 "mu": 0.5,
 "steps": 100000,
 "reps": 10,
 "noise": 0.0,
 "gap": 0.02,
 "min_share": 0.02,
 "h2": [
  2,
  4
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
