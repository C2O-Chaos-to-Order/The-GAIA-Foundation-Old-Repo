# SIM-IN-NAT-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Critical amplitude versus frequency (P38 Fig. 1: delta = 0.4, Ar = 0): does it rise with omega, nearly linearly (omega = 2 to 10)?

## Phase operationalization tested
NAT Insurgence = ignition threshold depends on how fast conditions fluctuate (P38).

## Sources this run draws on
P38 (Novozhilov 2016, Sci Rep 6:29730, CC BY 4.0; read in full in INC, equations read from the article's equation images): Eq. 1 d theta/d tau = (1/delta)(theta_xixi + (m/xi) theta_xi) + exp(theta/(1 + Ar theta)), Eq. 2 theta(1, tau) = A0 sin(omega tau); delta_cr = 0.88 for the static planar case; Figs. 1-8.

## Refinement from previous iteration
Iteration 3 of the x9 family for NAT; follows iteration 2 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | inside bracket |
| H1 | hypothesis | increasing and r^2 > 0.95 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-C",
 "iteration": 3,
 "kind": "thermal_explosion",
 "seed": 22103,
 "mode": "acrit",
 "vary": "om",
 "values": [
  2.0,
  4.0,
  6.0,
  8.0,
  10.0
 ],
 "delta": 0.4,
 "Ar": 0.0,
 "lo": 0.0,
 "hi": 10.0,
 "iters": 12,
 "tmax": 100,
 "h1_text": "critical amplitude increases with omega and is nearly linear (r^2 > 0.95)",
 "h1_expr": "all(np.diff(a) > 0) and np.corrcoef(v, a)[0, 1] ** 2 > 0.95"
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
