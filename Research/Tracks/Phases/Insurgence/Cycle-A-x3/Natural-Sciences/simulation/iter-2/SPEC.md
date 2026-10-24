# SIM-IN-NAT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noise and onset (NAT pass 3): with additive noise sigma = 0.005, does a seed x0 = 0.001 at r = 0.05 (P22 Eq. 8.8) break out earlier than the deterministic 77.84 (IN0-NAT-02), and how variable is the onset time?

## Phase operationalization tested
NAT Insurgence = onset from a seed; onset timing under noise.

## Sources this run draws on
P22 Eq. 8.8 (read in full in DVC); Euler-Maruyama and the reflecting boundary are the agent's modelling choices.

## Refinement from previous iteration
Follows iter-1 (bottleneck): adds noise to the transcritical onset of IN0-NAT-02.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no run censored |
| H1 | hypothesis | mean onset below deterministic by > 4 SE |
| H2 | hypothesis | CV > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Reflection at x = 0 itself pushes small x upward (reflected noise), so part of the advance is a boundary effect; noise larger than the seed. 200 replicates, dt 0.05. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-A",
 "iteration": 2,
 "kind": "transcritical_noise",
 "seed": 20102,
 "r": 0.05,
 "x0": 0.001,
 "sigma": 0.005,
 "dt": 0.05,
 "reps": 200,
 "tmax": 2000,
 "tol_se": 4,
 "h2": 0.1
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
