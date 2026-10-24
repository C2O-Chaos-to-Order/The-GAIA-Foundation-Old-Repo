# SIM-AL-SOC-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Critical slowing: at R = 1.02 does the toy converge to F* = 0.0196 within T = 3000?

## Phase operationalization tested
SOC Allegiance = slow dynamics at the fusion threshold.

## Sources this run draws on
P48 (read in full in AL0): labelling loop.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | F_end > 0.01 at R = 1.02 and < 0.01 at R = 0.98 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; V1 (within 0.01 of the fixed point) may hold even if convergence is incomplete because the fixed point is small.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-B",
 "iteration": 6,
 "kind": "fusion_loop",
 "seed": 26306,
 "beta": 0.5,
 "gamma": 0.5,
 "delta": 0.05,
 "dt": 0.01,
 "kappas": [
  0.049,
  0.051
 ],
 "T": 3000,
 "a": 1.0,
 "F0": 0.01,
 "D0": 0.0,
 "h1_text": "F_end > 0.01 at R = 1.02 and < 0.01 at R = 0.98",
 "h1_expr": "o['0.051']['F_end'] > 0.01 and o['0.049']['F_end'] < 0.01"
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
