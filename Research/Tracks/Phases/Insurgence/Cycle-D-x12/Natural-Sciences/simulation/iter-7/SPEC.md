# SIM-IN-NAT-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-NAT iter-7 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
NAT Insurgence = a delayed outbreak after a period of oscillation (P38).

## Sources this run draws on
P38 (Novozhilov 2016, Sci Rep 6:29730, CC BY 4.0; read in full in INC, equations read from the article's equation images): Eq. 1 d theta/d tau = (1/delta)(theta_xixi + (m/xi) theta_xi) + exp(theta/(1 + Ar theta)), Eq. 2 theta(1, tau) = A0 sin(omega tau); delta_cr = 0.88 for the static planar case; Figs. 1-8.

## Refinement from previous iteration
Iteration 7 of the x12 family for NAT; follows iteration 6 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ran |
| H1 | hypothesis | runaway after >= 2 maxima |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-D",
 "iteration": 7,
 "kind": "thermal_explosion",
 "seed": 23107,
 "mode": "history",
 "delta": 0.6,
 "Ar": 0.0,
 "A0": 2.8,
 "omega": 10.0,
 "tmax": 100,
 "h1_text": "runaway occurs, after at least two oscillation maxima at the centre",
 "h1_expr": "boom and peaks >= 2"
}
```

## Command
`python sim_nat.py iter-7` (run from `Natural-Sciences/simulation/`)
