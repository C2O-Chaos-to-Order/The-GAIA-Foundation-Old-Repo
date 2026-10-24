# SIM-DV-PHI-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Properties of the Cultural Fixation Index that P15 uses to show religion is the most divergent cultural trait: recovery of a known value and sensitivity to measurement scale (continuous vs yes/no items).

## Phase operationalization tested
PHI Divergence = cross-population divergence of religious (and other) values measured by CFst (P15).

## Sources this run draws on
P15 (Bentzen et al. 2026, read in full): CFst = var_b/(var_b + var_w); religion shows the largest cross-country divergence; P15 compares only items within the same question set and scale.

## Refinement from previous iteration
New run family (religious divergence was unsourced in DV0).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | continuous CFst within max(4 SE, 0.005) of finite-sample value |
| H1 | hypothesis | dichotomising lowers CFst by >= 20% |
| R1 | reporting | means |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic normal data; the finite-sample approximation is the agent's derivation (stated in the code), allowed a 0.005 bias band in addition to 4 SE. Says nothing about which real trait diverges most. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-A",
 "iteration": 2,
 "kind": "cfst_scale",
 "seed": 15602,
 "groups": 50,
 "n": 200,
 "sb": 0.5,
 "sw": 1.0,
 "reps": 200,
 "tol_se": 4,
 "bias_allow": 0.005,
 "h1": 0.2
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
