# SIM-R7-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Audit the Cycle-1 ledger (all claims, register, link register, all Cycle-1 execution records).

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| K1 | validation | fields/vocabulary/label-status/unique ids |
| K2 | validation | all source and SIM#check citations resolve |
| K3 | validation | no Established claim cites a failed validation check; cited Not-supported outcomes are stated as such |
| K4 | validation | every Established literature claim has a full-text source |
| K5 | validation | no Established claim on governing documents alone (simulation-backed claims exempt) |
| K6 | validation | link register complete; all types; all references resolve |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Checks bookkeeping, not truth.

## Command
`python sim_r7.py iter-1` (run from `Report-7-Unified/simulation/`)
