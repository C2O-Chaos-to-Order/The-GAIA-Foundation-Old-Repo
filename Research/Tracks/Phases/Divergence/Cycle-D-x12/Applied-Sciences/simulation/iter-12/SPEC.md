# SIM-DV-APP-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of the pooled-SE driver test (sd 0.5).

## Phase operationalization tested
APP Divergence = intratumour branching with selection (P05, P04).

## Sources this run draws on
P05 (re-read in full in DVB) for the branching-evolution picture; toy is not P05's model.

## Refinement from previous iteration
Derived from SIM-DV-APP-C iteration 1: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mutations per birth within 4 SE of u |
| H1 | hypothesis | share_high - share_low > 4 pooled SE |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB; pooled SE ignores clustering within clones (optimistic). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 12,
 "kind": "bep_drivers_pooled",
 "seed": 18412,
 "reps": 40,
 "N": 10000,
 "b0": 0.5,
 "d0": 0.3,
 "sd": 0.5,
 "u": 1.0,
 "q": 0.05,
 "hi": 0.5,
 "lo_min": 0.01,
 "lo_max": 0.3,
 "tol_se": 4,
 "h1": 2.0,
 "h1_mode": "enrich"
}
```

## Command
`python sim_app.py iter-12` (run from `Applied-Sciences/simulation/`)
