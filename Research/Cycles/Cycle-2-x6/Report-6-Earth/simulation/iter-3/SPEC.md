# SIM-R6-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Test the W03 verbal argument that adaptation fast relative to environmental change removes the need for (and the fact of) regulation, by varying forcing speed (steps per luminosity increment) against adaptation rate.

## Refinement from previous iteration
Iteration 2 showed which constraints recover regulation; this iteration asks about the RATE dimension that iterations 1-2 held fixed.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| RR1 | hypothesis | Spearman rho(adaptation per forcing step, width) <= -0.8 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth. Fewer steps per luminosity increment also means the populations are less equilibrated; this confound is noted, not removed.

## Command
`python sim_r6.py iter-3` (run from `Report-6-Earth/simulation/`)
