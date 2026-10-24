# SIM-R2-C4 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Challenge: if PH associability recovers with time, does PH also show a delay effect?

## Refinement from previous iteration
New option rho (our addition, not from a source).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | PH drop < 50% at rho 0.01 |
| H9r | reporting | drop by rho |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
SUBSTITUTE simulation: the carried item 'faithful Mackintosh (1975) rule' is BLOCKED (no open-access specification found; Y05 abstract only), so no Mackintosh model is run. Textbook-form PH and KF rules as in Cycle 3; delay = KF uncertainty growth (and, from iteration 9, optional PH associability recovery 'rho', our addition). Between-subject noise is Gaussian on the LI index (our assumption). No animal data fitted.

## Command
`python sim_r2.py iter-9` (run from `Report-2-Mind/simulation/`)
