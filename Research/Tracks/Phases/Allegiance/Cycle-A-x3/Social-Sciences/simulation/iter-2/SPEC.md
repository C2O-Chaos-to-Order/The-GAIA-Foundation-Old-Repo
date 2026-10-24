# SIM-AL-SOC-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Fusion loop with tenfold slower decay of fusion (delta 0.005; irrevocability, P48): does the same threshold at R = 1 hold, and how long does fusion take to halve once condemnation stops?

## Phase operationalization tested
SOC Allegiance = self-reinforcing fusion with near-irrevocability.

## Sources this run draws on
P48 (read in full in AL0): labelling loop; irrevocability principle; de-fusion mechanisms not yet demonstrated.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | F_end > 0.4 for R >= 2 and < 0.01 for R < 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; parameters arbitrary.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-A",
 "iteration": 2,
 "kind": "fusion_loop",
 "seed": 25302,
 "a": 1.0,
 "beta": 0.5,
 "gamma": 0.5,
 "delta": 0.005,
 "dt": 0.05,
 "kappas": [
  0.002,
  0.01,
  0.02
 ],
 "F0": 0.01,
 "D0": 0.0,
 "T": 20000,
 "h1_text": "fused state above 0.4 when R >= 2, below 0.01 when R < 1",
 "h1_expr": "all((v['F_end'] > 0.4) if v['R'] >= 2 else (v['F_end'] < 0.01) for v in o.values() if v['R'] >= 2 or v['R'] < 1)"
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
