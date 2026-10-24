# SIM-R5-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
'Anaesthesia-like' manipulation (loosely after W13): reduce between-module coupling at fixed within-module coupling; does PCI-like fall?

## Refinement from previous iteration
Uses the iteration-3 peak coupling as within-module coupling.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| D1 | hypothesis | Spearman(out_ratio, PCI-like) >= 0.8 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy Kuramoto network of our own; 'PCI-like' is only loosely modelled on PCI (W11): no source modelling, no statistical thresholding against baseline. Says nothing about consciousness. PILOT DISCLOSURE: before iteration 1 was frozen, one pilot whose numbers are not part of any result (40 units, K 0-80, dt 0.05, T 300, no sub-sampling) was run only to check run time; it showed low spontaneous LZ for all K (~0.11-0.14, i.e. oversampled smooth signals) and a flat PCI-like profile (0.08 at K=0, 0.19-0.23 for K>=2). In response we fixed sub-sampling every 10 steps and T = 600 for all iterations; no other parameter was changed after the pilot. Propofol's real mechanisms are not modelled.

## Command
`python sim_r5.py iter-5` (run from `Report-5-Consciousness/simulation/`)
