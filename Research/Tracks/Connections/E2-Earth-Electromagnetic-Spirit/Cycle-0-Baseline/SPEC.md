# E2 Cycle-0 physical-model specification

Date: 2026-10-26. ID: GAIA-E2-C0-SPEC-002. Owner topic: The Earth and the Electromagnetic Spectrum as the Spirit of the Earth. Owner proposition: Consciousness as the Electromagnetic Spectrum.

## Status and provenance

This commit contains the specification, configuration and runnable model only. Research manuscripts, registers, results, ZIP and integration checks are not uploaded by this commit. The overall gate is INDETERMINATE.

A prior conversational execution reported the numerical results. Its temporary files were not delivered or committed. This specification reconstructs that model transparently for a fresh, separately recorded execution after this commit. It is not an outcome-blind preregistration: both adequacy hypotheses are already expected to fail. Do not backdate the reconstruction or portray it as the original execution.

## Physical source and model

Source: Simoes, Pfaff and Freudenreich, Observation of Schumann Resonances in the Earth's Ionosphere, NASA-hosted manuscript, cavity discussion and equation: https://ntrs.nasa.gov/api/citations/20120000051/downloads/20120000051.pdf

Evaluate the thin, lossless spherical-cavity approximation f_n = c * sqrt(n*(n+1)) / (2*pi*R). The source gives angular frequency; division by 2*pi converts to Hz. Radius R = 6371000 m is a declared rounded model parameter, not a new measurement. c = 299792458 m/s. Modes n = 1 through 5. Compare with the approximate average ground-mode summary 7.8, 14.3, 20.8, 27.3 and 33.8 Hz, not the different single-orbit vector in the paper. These are published summary values without supplied uncertainty, not raw observations.

Fit one scalar alpha = summary_f1 / ideal_f1, then apply it to all modes. Mode 1 is calibration, not predictive validation. Modes 2-5 are internal cross-mode comparisons, not independent empirical validation. No synthetic observations are generated.

## Fixed checks

V01: finite, positive, strictly increasing ideal modes.
V02: squared-frequency identity agrees at relative tolerance 1e-12.
V03: increasing radius by 1% divides frequencies by 1.01, relative tolerance 1e-12.
V04: fitted fundamental matches to absolute tolerance 1e-10 Hz.
H01: all five ideal modes within 5% of published summaries. Expected Not Supported.
H02: fitted modes 2-5 each within 5%. Expected Not Supported from the prior disclosed execution.

The 5% threshold is an author-chosen diagnostic, not a source standard or statistical significance test. Failed hypotheses remain findings and must not be retuned. One iteration evaluates five modes; verification reruns do not count as additional research passes.

## Boundaries

This analytic model is not a realistic lossy-ionosphere solver, consciousness simulation or test of Spirit. Frequency mismatch cannot establish a spiritual explanation. It does not test Earth-to-brain coupling, health effects or planetary experience. No human or animal experiment, field exposure, deployment or implementation is authorized.

## Execution

Python standard library only. From this cycle directory run: python tools/model.py

Outputs are iter-1/outputs/results.json and iter-1/EXECUTION_RECORD.json. Preserve the specification commit ID separately when recording the execution environment. Do not mark the research complete merely because the script runs. Canonical maps, full-tree validation, source review, ZIP integrity and independent review remain outstanding.
