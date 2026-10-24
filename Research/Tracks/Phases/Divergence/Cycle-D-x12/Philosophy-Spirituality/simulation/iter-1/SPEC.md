# SIM-DV-PHI-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of text consolidation at u = 0.1.

## Phase operationalization tested
PHI Divergence = textual divergence of a classic's transmission lines followed by consolidation toward a received text (P18).

## Sources this run draws on
P18 (Chan, SEP 'Laozi', rev. 2025; read in full, end to end, in DVC): Guodian (c. 300 BCE), Mawangdui and Beida manuscripts; 'different collections of sayings ... overlapping to some extent'; 'The demand for textual uniformity rose ... the different textual traditions eventually gave way to the received text'. The model is the agent's formal analogue, not a reconstruction of the Laozi's history.

## Refinement from previous iteration
Derived from SIM-DV-PHI-C iteration 1: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | divergence-phase distance within 4 SE of (1-(1-2mu)^(2t1))/2 |
| H1 | hypothesis | standardisation lowers distance by > 30% |
| R1 | reporting | distances |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Binary sites, independent lineages from one archetype, majority over lineages. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-D",
 "iteration": 1,
 "kind": "text_consolidation",
 "seed": 18601,
 "lineages": 6,
 "M": 1000,
 "reps": 200,
 "t1": 20,
 "t2": 20,
 "mu": 0.01,
 "u": 0.1,
 "tol_se": 4,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
