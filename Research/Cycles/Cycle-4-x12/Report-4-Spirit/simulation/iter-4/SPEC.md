# SIM-R4-C4 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
When can the NCO also correct the estimate (ratio OR_D/OR_N)?

## Refinement from previous iteration
Varies how strongly U acts on N.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | within 10% only at gN = gD |
| H4r | reporting | corrected ORs |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic cohorts with one binary unmeasured confounder and logistic outcomes; crude 2x2 odds ratios. Real negative controls are never perfect (Y03); the design numbers are illustrations, not estimates for any study.

## Command
`python sim_r4.py iter-4` (run from `Report-4-Spirit/simulation/`)
