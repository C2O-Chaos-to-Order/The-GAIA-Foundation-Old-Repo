# SIM-R2-C4 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Mis-specification: KF generators with tau2 far outside the fitting grid.

## Refinement from previous iteration
Generators 3x beyond the grid on each side (log-uniform).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | >= 70% at noise 0.1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
SUBSTITUTE simulation: the carried item 'faithful Mackintosh (1975) rule' is BLOCKED (no open-access specification found; Y05 abstract only), so no Mackintosh model is run. Textbook-form PH and KF rules as in Cycle 3; delay = KF uncertainty growth (and, from iteration 9, optional PH associability recovery 'rho', our addition). Between-subject noise is Gaussian on the LI index (our assumption). No animal data fitted.

## Command
`python sim_r2.py iter-6` (run from `Report-2-Mind/simulation/`)
