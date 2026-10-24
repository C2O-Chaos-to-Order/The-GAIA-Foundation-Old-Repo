# SIM-R2-C4 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
What does the two-model comparison do with data that are neither model (a 50/50 mixture)?

## Refinement from previous iteration
New: mixture generators.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | 50/50 share KF in 0.2-0.8 |
| H7r | reporting | share by mixture |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
SUBSTITUTE simulation: the carried item 'faithful Mackintosh (1975) rule' is BLOCKED (no open-access specification found; Y05 abstract only), so no Mackintosh model is run. Textbook-form PH and KF rules as in Cycle 3; delay = KF uncertainty growth (and, from iteration 9, optional PH associability recovery 'rho', our addition). Between-subject noise is Gaussian on the LI index (our assumption). No animal data fitted.

## Command
`python sim_r2.py iter-7` (run from `Report-2-Mind/simulation/`)
