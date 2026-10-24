# SIM-AL-APP-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P61 Study 2 pairwise (24 per group): power for d 0.5 and 0.8 at alpha 0.05?

## Phase operationalization tested
APP Allegiance = power of an allegiance-balanced head-to-head trial (P54).

## Sources this run draws on
P54 (Malkomsen et al. 2025, STPP vs CBT for depression, BMC Psychiatry, PMC11817821, CC BY; read in full in ALC): power statement 0.84 for d 0.6 with N 100; HDRS time x treatment -1.50 [-4.25, 1.26]; BDI -0.12 [-0.76, 0.53]; response OR 0.59 [0.24, 1.42]; between-group d HDRS 0.27, BDI 0.14, WSAS 0.39; 81 evaluated at 28 weeks (39 CBT, 42 STPP); balanced-allegiance steering group.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | power for d 0.8 >= 0.8 |
| H2 | hypothesis | power for d 0.5 below 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pairwise two-sample t; P61 powered an omnibus F.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-C",
 "iteration": 3,
 "kind": "t_power",
 "seed": 27403,
 "designs": [
  {
   "label": "P61_pair",
   "n1": 24,
   "n2": 24,
   "d_values": [
    0.5,
    0.8
   ]
  }
 ],
 "hyps": [
  [
   "power for d 0.8 >= 0.8",
   "o['P61_pair']['power']['0.8'] >= 0.8"
  ],
  [
   "power for d 0.5 below 0.5",
   "o['P61_pair']['power']['0.5'] < 0.5"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
