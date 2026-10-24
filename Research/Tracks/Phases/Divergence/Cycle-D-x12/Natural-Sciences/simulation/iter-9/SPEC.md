# SIM-DV-NAT-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of the linkage island at m = 0.02.

## Phase operationalization tested
NAT Divergence = locus-specific differentiation decaying with recombination distance (P01, toy).

## Sources this run draws on
P01 (re-read in full in DVB).

## Refinement from previous iteration
Derived from SIM-DV-NAT-C iteration 8: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral mean frequency 0.5 within 4 SE |
| H1 | hypothesis | Fst(c=0) - Fst(c=0.5) > 4 SE |
| H2 | hypothesis | monotone in c |
| H3 | hypothesis | Fst(c=0.01) below midpoint |
| R1 | reporting | Fst by c |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-D",
 "iteration": 9,
 "kind": "wf_linked",
 "seed": 18109,
 "m": 0.02,
 "s": 0.1,
 "N": 200,
 "reps": 60,
 "generations": 400,
 "per_c": 8,
 "c_values": [
  0.0,
  0.001,
  0.01,
  0.05,
  0.5
 ],
 "c_mid": 0.01,
 "tol_se": 4,
 "mono_tol": 0.02
}
```

## Command
`python sim_nat.py iter-9` (run from `Natural-Sciences/simulation/`)
