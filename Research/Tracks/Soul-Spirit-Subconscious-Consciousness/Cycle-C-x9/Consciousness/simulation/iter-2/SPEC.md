# SIM-CONS-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K32 reports that dream recall under anaesthesia was not associated with intraoperative awareness. Awareness is rare (0-2.5%). How much power did such comparisons have?

## Sources this run draws on
K32 (Sikka, Hu & Heifets 2026): awareness 0%-2.5% in the five clinical studies reporting it; clinical recall typically 3%-8%. Awareness rate .5%, recall 6%, RR 3 and N are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RR 1 FPR <= .05 + 3 MC SE |
| H1 | hypothesis | power < .5 |
| R1 | reporting | power by N |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Fisher exact test; independent patients. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 2,
 "kind": "rare_association_power",
 "seed": 812,
 "N": 2000,
 "p_recall": 0.06,
 "p_aware_nonrecall": 0.005,
 "RR": 3.0,
 "N_grid": [
  500,
  2000,
  10000
 ],
 "reps": 2000
}
```

## Command
`python sim_cons.py iter-2` (run from `Consciousness/simulation/`)
