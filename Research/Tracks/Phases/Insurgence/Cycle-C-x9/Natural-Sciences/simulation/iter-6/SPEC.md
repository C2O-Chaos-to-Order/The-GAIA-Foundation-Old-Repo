# SIM-IN-NAT-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Low-frequency limit (P38: as omega -> 0 the critical amplitude becomes independent of frequency): omega = 0.05, 0.1, 0.2 at delta = 0.4, Ar = 0.

## Phase operationalization tested
NAT Insurgence = slow fluctuations act like a static shift (P38).

## Sources this run draws on
P38 (Novozhilov 2016, Sci Rep 6:29730, CC BY 4.0; read in full in INC, equations read from the article's equation images): Eq. 1 d theta/d tau = (1/delta)(theta_xixi + (m/xi) theta_xi) + exp(theta/(1 + Ar theta)), Eq. 2 theta(1, tau) = A0 sin(omega tau); delta_cr = 0.88 for the static planar case; Figs. 1-8.

## Refinement from previous iteration
Iteration 6 of the x9 family for NAT; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | inside bracket |
| H1 | hypothesis | within 10% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Runs last at least two periods. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-C",
 "iteration": 6,
 "kind": "thermal_explosion",
 "seed": 22106,
 "mode": "acrit",
 "vary": "om",
 "values": [
  0.05,
  0.1,
  0.2
 ],
 "delta": 0.4,
 "Ar": 0.0,
 "lo": 0.0,
 "hi": 6.0,
 "iters": 12,
 "tmax": 100,
 "h1_text": "critical amplitudes within 10% of each other",
 "h1_expr": "max(a) / min(a) - 1 <= 0.1"
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
