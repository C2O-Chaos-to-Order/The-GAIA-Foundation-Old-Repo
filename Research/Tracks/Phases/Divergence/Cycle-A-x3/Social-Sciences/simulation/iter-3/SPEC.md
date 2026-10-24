# SIM-DV-SOC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Can P11's headline pattern (values diverged globally but converged regionally) arise in a simple generative panel, and do P11's two measures register it?

## Phase operationalization tested
SOC Divergence = rising SD of country means across items ('value variation', P11) together with falling within-region SD.

## Sources this run draws on
P11 (Jackson & Medvedev 2024, read in full): definitions of value variation and value distinctiveness; finding of global divergence with regional convergence.

## Refinement from previous iteration
New run family (measurement sense from P11).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | SD routine exact on a two-point case |
| H1 | hypothesis | global slope > 0 and within-region slope < 0 |
| R1 | reporting | measures by wave |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic data with a built-in regional drift: a possibility demonstration of the measures, not a test of P11's data or causes.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-A",
 "iteration": 3,
 "kind": "value_divergence",
 "seed": 15303,
 "countries": 60,
 "regions": 6,
 "items": 40,
 "waves": 7,
 "region_drift": 0.02,
 "idio_sd": 0.1,
 "pull": 0.15,
 "noise": 0.02
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
