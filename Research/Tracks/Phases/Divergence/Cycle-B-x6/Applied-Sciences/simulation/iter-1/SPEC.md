# SIM-DV-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P05 reports that progressor (late, subclonal) mutations are rarely in driver genes. In a branching toy, are drivers enriched among high-CCF mutations relative to low-CCF ones?

## Phase operationalization tested
APP Divergence = intratumour branching divergence, with selection shaping which mutations become clonal (P05, P04).

## Sources this run draws on
P05 (Sottoriva-type BEP study; re-read in full in DVB): branching evolution model and the observation on progressor mutations. The toy is not P05's model (no space, no ABC).

## Refinement from previous iteration
New run family (P05 follow-up).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mutations per birth within 4 SE of u |
| H1 | hypothesis | driver share high-CCF >= 2x low-CCF |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Non-spatial, discrete-time; drivers multiply birth probability (capped 0.95); CCF from the full population (no sampling, unlike P05's multiregion data). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 1,
 "kind": "bep_drivers",
 "seed": 16401,
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
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
