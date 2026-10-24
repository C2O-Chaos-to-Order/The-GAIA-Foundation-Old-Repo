# SIM-DV-NAT-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P22's two pitchfork types: supercritical (Eq. 8.10) settles on two stable branches +/- sqrt(r); subcritical (Eq. 8.12) has no stable branch near zero for r > 0.

## Phase operationalization tested
NAT Divergence = symmetric splitting of one state into two (supercritical pitchfork) vs runaway (subcritical) (P22).

## Sources this run draws on
P22 (read in full): Eqs. 8.10-8.13.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | supercritical final = sqrt(r) (1e-6) |
| V2 | validation | r <= 0 decays |
| H1 | hypothesis | subcritical escapes for every r > 0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic RK4 from x0 = 0.01; cap 10. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-C",
 "iteration": 6,
 "kind": "pitchfork_types",
 "seed": 17106,
 "r_values": [
  -0.5,
  0.1,
  0.25,
  1.0
 ],
 "eps": 0.01,
 "dt": 0.01,
 "steps": 20000,
 "cap": 10,
 "tol": 1e-06
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
