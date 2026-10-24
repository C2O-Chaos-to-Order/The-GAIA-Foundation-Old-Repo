# SIM-IN-NAT-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Barrier height and waiting time (P37): for B = 0.8, 1.0, 1.2, 1.5 (G* = 6.25 to 1.78 kT) is ln MFPT linear in G* with slope near 1?

## Phase operationalization tested
NAT Insurgence = rare onset over a free-energy barrier.

## Sources this run draws on
P37 (Tokmakoff, Concepts in Biophysical Chemistry, LibreTexts section 19.2, CC BY-NC-SA 4.0; read in full in INB): dG_n = gamma alpha n^(2/3) - d_eps V0 n, n*, G*. Kinetics (attachment rate 1, detailed-balance detachment) and the birth-death MFPT formula are the agent's (standard, not from P37).

## Refinement from previous iteration
Iteration 2 of the x6 family for NAT; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MFPT increases with barrier |
| H1 | hypothesis | slope within 0.3 of 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exact birth-death sums (deterministic); end point 2 n*; small barriers, so prefactors matter. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-B",
 "iteration": 2,
 "kind": "nucleation",
 "seed": 21102,
 "mode": "scaling",
 "A": 3.0,
 "B_values": [
  0.8,
  1.0,
  1.2,
  1.5
 ],
 "end_factor": 2,
 "h1": 0.3
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
