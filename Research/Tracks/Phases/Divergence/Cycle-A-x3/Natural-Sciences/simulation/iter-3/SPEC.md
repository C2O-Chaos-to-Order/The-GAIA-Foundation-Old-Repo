# SIM-DV-NAT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Developmental divergence as a formal toy: when a one-valley landscape becomes two-valley (pitchfork bifurcation), do identical cells split between fates, and how sensitive is the split to a small bias?

## Phase operationalization tested
NAT Divergence = cell-fate divergence pictured as Waddington's epigenetic landscape (P10: a visual metaphor for the genetic control of embryonic differentiation) and as a physical bifurcation.

## Sources this run draws on
P10 (Henikoff 2023, read in full): the landscape is a metaphor introduced to illustrate the genetic control of embryonic differentiation. The SDE is a standard normal form, not taken from P10.

## Refinement from previous iteration
New run family in this iteration (covers the development/bifurcation sense listed as unsourced in DV0).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | bias 0: right-valley fraction = 0.5 within 4 binomial SE |
| V2 | validation | mean |x| within 10% of sqrt(a1) |
| H1 | hypothesis | bias 0.05: > 0.9 in one valley |
| R1 | reporting | fractions by bias |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-dimensional gradient system with additive noise; no gene regulatory network, no cell division. P10 is a perspective, not a model paper; the link is metaphorical. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-A",
 "iteration": 3,
 "kind": "pitchfork_landscape",
 "seed": 15103,
 "cells": 2000,
 "dt": 0.01,
 "T": 20,
 "a0": -1.0,
 "a1": 1.0,
 "sigma": 0.1,
 "biases": [
  0.0,
  0.05
 ],
 "tol_se": 4,
 "h1": 0.9
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
