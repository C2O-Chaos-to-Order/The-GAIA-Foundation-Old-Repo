# SIM-R2-C4 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
How long must the delay be?

## Refinement from previous iteration
Finer delay scan than Cycle 3.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | half-life <= 20 steps |
| H8r | reporting | by tau2 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
SUBSTITUTE simulation: the carried item 'faithful Mackintosh (1975) rule' is BLOCKED (no open-access specification found; Y05 abstract only), so no Mackintosh model is run. Textbook-form PH and KF rules as in Cycle 3; delay = KF uncertainty growth (and, from iteration 9, optional PH associability recovery 'rho', our addition). Between-subject noise is Gaussian on the LI index (our assumption). No animal data fitted.

## Command
`python sim_r2.py iter-8` (run from `Report-2-Mind/simulation/`)
