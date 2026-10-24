# SIM-R4-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Probabilistic bias analysis: draw confounder strengths (RR_EU, RR_UD) from a prior and report how often each association is fully explained away; sweep the prior spread because the prior is our assumption.

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V0/V_* | validation | as iteration 1 |
| P1 | validation | larger E-value -> smaller fraction explained away |
| P2 | reporting | fraction explained away per estimate |
| P3 | validation | fraction explained away increases with prior spread |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
The prior |N(0, sd)| on log RR is arbitrary; results are conditional on it.

## Command
`python sim_r4.py iter-2` (run from `Report-4-Spirit/simulation/`)
