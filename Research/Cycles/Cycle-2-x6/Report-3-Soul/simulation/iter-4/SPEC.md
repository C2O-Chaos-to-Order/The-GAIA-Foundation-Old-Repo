# SIM-R3-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Direction of disagreement: does one coding systematically assign 1 more often (bias), and how does prevalence affect kappa?

## Refinement from previous iteration
Diagnoses the iteration-1 kappa.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | bias index >= 0.1 |
| H4r | reporting | 2x2 table, PABAK, indices |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-4` (run from `Report-3-Soul/simulation/`)
