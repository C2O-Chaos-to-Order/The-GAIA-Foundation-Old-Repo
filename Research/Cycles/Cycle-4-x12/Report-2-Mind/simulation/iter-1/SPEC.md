# SIM-R2-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check: the copied rules (Mackintosh branch removed) reproduce Cycle 3; the new rho option leaves weights unchanged on empty steps.

## Refinement from previous iteration
Replaces the blocked carried item (faithful Mackintosh) with a smaller PH-vs-KF robustness study; disclosed.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C3 iter-4 |
| V2 | validation | delay steps inert for weights |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
SUBSTITUTE simulation: the carried item 'faithful Mackintosh (1975) rule' is BLOCKED (no open-access specification found; Y05 abstract only), so no Mackintosh model is run. Textbook-form PH and KF rules as in Cycle 3; delay = KF uncertainty growth (and, from iteration 9, optional PH associability recovery 'rho', our addition). Between-subject noise is Gaussian on the LI index (our assumption). No animal data fitted.

## Command
`python sim_r2.py iter-1` (run from `Report-2-Mind/simulation/`)
