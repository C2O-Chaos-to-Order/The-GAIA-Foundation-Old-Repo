# SIM-R3-C2 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Tolerance: how many random cell flips can the typology absorb before its median ARI drops below 0.8, compared with the disagreement rate extrapolated to all 180 cells?

## Refinement from previous iteration
Generalises iteration 5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | extrapolated disagreements < tolerance threshold |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-6` (run from `Report-3-Soul/simulation/`)
