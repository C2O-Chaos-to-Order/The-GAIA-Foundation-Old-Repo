# SIM-R6-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Geomagnetic spectrum (Lowes-Mauersberger) at Earth's surface and downward-continued to the core-mantle boundary for four epochs; free-decay time across the disputed conductivity range (V09 high vs V30 low, converted with Wiedemann-Franz).

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| G0 | validation | R_1 equals 2(g10^2+g11^2+h11^2) |
| G1 | hypothesis | surface spectrum steep, CMB spectrum near-flat |
| G2 | hypothesis | free decay < 1e6 yr across the whole conductivity range |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Core temperatures 4000-5000 K for Wiedemann-Franz are an assumption; free decay ignores inner core and mode structure.

## Command
`python sim_r6.py iter-3` (run from `Report-6-Earth/simulation/`)
