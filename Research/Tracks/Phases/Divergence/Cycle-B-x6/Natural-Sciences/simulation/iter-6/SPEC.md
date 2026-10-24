# SIM-DV-NAT-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Bifurcation follow-up: how small a bias already decides the fate split at the pitchfork (bias grid down to 0.005)?

## Phase operationalization tested
NAT Divergence = cell-fate divergence as a pitchfork bifurcation (P10 metaphor; standard normal form).

## Sources this run draws on
P10 (Henikoff 2023, read in full in DVA): the landscape is a metaphor. SDE is a standard normal form.

## Refinement from previous iteration
DVA iteration 3 used biases 0 and 0.05; this grid is finer. H1 is evaluated at the largest bias in the grid (0.02).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | bias 0: fraction 0.5 within 4 binomial SE |
| V2 | validation | mean |x| within 10% of sqrt(a1) |
| H1 | hypothesis | largest bias: > 0.9 in one valley |
| R1 | reporting | fractions by bias |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-dimensional gradient system; the link to P10 is metaphorical. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-B",
 "iteration": 6,
 "kind": "pitchfork_landscape",
 "seed": 16106,
 "cells": 2000,
 "dt": 0.01,
 "T": 20,
 "a0": -1.0,
 "a1": 1.0,
 "sigma": 0.1,
 "biases": [
  0.0,
  0.005,
  0.01,
  0.02
 ],
 "tol_se": 4,
 "h1": 0.9
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
