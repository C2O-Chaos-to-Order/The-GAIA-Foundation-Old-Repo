# SIM-DV-APP-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P17's result: forward Euler on the simple harmonic oscillator always grows (growth factor |1 + i h w| > 1); semi-implicit Euler does not.

## Phase operationalization tested
APP Divergence = numerical divergence of a solver from the true bounded solution (method-induced instability).

## Sources this run draws on
P17 (Brorson, LibreTexts, read in full in DVB): growth factor |1 +/- i h w0|; 'the solution computed by forward Euler always grows'.

## Refinement from previous iteration
New run family (extends the DVA real-lambda euler_stability run to the oscillator).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | amplitude = (1+h^2w^2)^(n/2) within 1e-9 |
| H1 | hypothesis | growth > 1% at h = 0.001 over 10 periods |
| H2 | hypothesis | symplectic within 5% at h = 0.01 |
| R1 | reporting | amplitudes |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear oscillator only. Semi-implicit Euler is not in P17's chapter (agent's comparison). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 4,
 "kind": "euler_sho",
 "seed": 16404,
 "omega": 1.0,
 "h_values": [
  0.01,
  0.001
 ],
 "periods": 10,
 "h1": 0.01,
 "h2": 0.05
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
