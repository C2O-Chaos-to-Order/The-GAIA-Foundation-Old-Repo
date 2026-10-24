# SIM-IN-NAT-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Oscillating ambient temperature (P38 Fig. 7: delta = 0.2, Ar = 0.04, omega = 1): is the critical amplitude near P38's value (bounded at A0 = 1.931802, runaway at 2.0)?

## Phase operationalization tested
NAT Insurgence = ignition triggered by fluctuations in a system that is stable on average (P38).

## Sources this run draws on
P38 (Novozhilov 2016, Sci Rep 6:29730, CC BY 4.0; read in full in INC, equations read from the article's equation images): Eq. 1 d theta/d tau = (1/delta)(theta_xixi + (m/xi) theta_xi) + exp(theta/(1 + Ar theta)), Eq. 2 theta(1, tau) = A0 sin(omega tau); delta_cr = 0.88 for the static planar case; Figs. 1-8.

## Refinement from previous iteration
Iteration 2 of the x9 family for NAT; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | inside bracket |
| H1 | hypothesis | within 0.05 of 1.93 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge: a smoke run showed runaway at A0 = 2.0 and none at 1.8 for these values. tau* = 100. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-C",
 "iteration": 2,
 "kind": "thermal_explosion",
 "seed": 22102,
 "mode": "acrit",
 "vary": "om",
 "values": [
  1.0
 ],
 "delta": 0.2,
 "Ar": 0.04,
 "lo": 1.5,
 "hi": 2.5,
 "iters": 12,
 "tmax": 100,
 "h1_text": "critical amplitude within 0.05 of 1.93 (P38 Fig. 7)",
 "h1_expr": "abs(a[0] - 1.93) <= 0.05"
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
