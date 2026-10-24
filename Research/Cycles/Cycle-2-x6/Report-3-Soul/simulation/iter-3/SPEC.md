# SIM-R3-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Is disagreement concentrated where the cited source is silent (coder B 'uncertain')?

## Refinement from previous iteration
Splits iteration 1-2 agreement by B's certainty flag.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | kappa(certain) >= kappa(uncertain) + 0.2 |
| H3r | reporting | share of uncertain cells |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-3` (run from `Report-3-Soul/simulation/`)
