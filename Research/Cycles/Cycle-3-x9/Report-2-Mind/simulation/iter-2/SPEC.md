# SIM-R2-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Would a parametric pre-exposure design (LI vs number of pre-exposures) separate PH from KF?

## Refinement from previous iteration
Adds the Mackintosh-type model as a third account.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | PH and KF curves differ by >= 0.15 |
| H2b | hypothesis | MK LI grows with pre-exposure |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-2` (run from `Report-2-Mind/simulation/`)
