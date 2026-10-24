# SIM-R3-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consequence for the Cycle-1 typology: substitute coder B's values on the 48 cells and compare the jaccard/average/k=4 partition with the C1 base (ARI); null = same number of random flips.

## Refinement from previous iteration
Turns agreement statistics into an effect on the Cycle-1 result.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | ARI >= 0.8 |
| H5r | reporting | null ARI distribution |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-5` (run from `Report-3-Soul/simulation/`)
