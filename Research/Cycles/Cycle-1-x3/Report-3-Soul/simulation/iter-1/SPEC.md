# SIM-R3-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
C0 typology recurred in 0.13% of perturbations. Test alternative codings of the 36 uncertain cells and alternative distance metrics against the C0 base partition.

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| E1 | validation | coding matrix complete and every row sourced |
| E3 | hypothesis | no attribute is shared by all conceptions |
| C1 | reporting | variants reproducing the base partition |
| C2 | hypothesis | coding-robust only if median ARI vs base >= 0.8 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Single coder; ARI and silhouette implemented in-house (sklearn not installed).

## Command
`python sim_r3.py iter-1` (run from `Report-3-Soul/simulation/`)
