# SIM-R5-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Validate the Lempel-Ziv (LZ76, Kaspar-Schuster) implementation used for both spontaneous and perturbational complexity.

## Refinement from previous iteration
New simulation line in Cycle 2 (C1 R5 modelled access/ignition thresholds); motivated by W11 and W13.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| Z1 | validation | random sequence normalised LZ in [0.9, 1.1] |
| Z2 | validation | periodic < 0.05 |
| Z3 | validation | textbook example = 6 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy Kuramoto network of our own; 'PCI-like' is only loosely modelled on PCI (W11): no source modelling, no statistical thresholding against baseline. Says nothing about consciousness. PILOT DISCLOSURE: before iteration 1 was frozen, one pilot whose numbers are not part of any result (40 units, K 0-80, dt 0.05, T 300, no sub-sampling) was run only to check run time; it showed low spontaneous LZ for all K (~0.11-0.14, i.e. oversampled smooth signals) and a flat PCI-like profile (0.08 at K=0, 0.19-0.23 for K>=2). In response we fixed sub-sampling every 10 steps and T = 600 for all iterations; no other parameter was changed after the pilot.

## Command
`python sim_r5.py iter-1` (run from `Report-5-Consciousness/simulation/`)
