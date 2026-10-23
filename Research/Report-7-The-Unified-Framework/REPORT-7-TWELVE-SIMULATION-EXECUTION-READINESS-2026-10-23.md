# Report 7 — Twelve Simulation Designs: Execution Readiness and Blocking Inputs

**Audit date:** 2026-10-23  
**Canonical design source:** `Research/Report-7-The-Unified-Framework/Universal-Framework-Research-Integrity-and-Simulation-Design-Addendum-Revised-0.9.0.md`  
**Status:** 0 READY FOR FULL EXECUTION; 12 DESIGN RECORDS TRIAGED  
**Change type:** Simulation execution-readiness audit  
**Risk level:** High epistemic risk if synthetic substitutes are misreported as empirical tests

## Decision rule

A design is runnable only when the target claim, model/data, operational variables, parameters, baselines, acceptance criteria, and reproducible output plan are sufficiently specified. “Run something similar” is not a valid substitute. If prerequisites are absent, record the exact blocker and next deliverable instead of inventing assumptions silently.

The existing five synthetic smoke tests are a separate bounded suite. They have now been rerun at the logic level and are documented separately; they do not clear any of these twelve study designs.

## Per-design readiness matrix

| ID | Design | Minimum missing prerequisites before a valid run | Current disposition | Next actionable step |
|---|---|---|---|---|
| S01 | DOM prediction discrimination | Verifiable primary source for all five predictions; each prediction mapped to a distinct operational measure; justified indicators; suitable dataset/protocol; preregistered alternatives and thresholds | **BLOCKED — source/operationalization** | Verify the DOM source and formal prediction ledger; do not fabricate the five predictions from summaries |
| S02 | IIT Φ proxy construct validity | Exact target construct and proxy definitions; independent datasets; convergent/discriminant/mechanistic criteria; preregistered scoring and inconclusive outcomes | **BLOCKED — construct/data** | Define each proxy separately and locate datasets capable of testing the specified validity claims |
| S03 | Prediction Ledger / MCI | Source/version provenance; published rubric; theory core/import classification; operational measures; inter-rater reliability plan; scoring weights and uncertainty | **BLOCKED — rubric/source** | Freeze rubric and provenance before scoring; treat COGITATE reanalysis as a critical reanalysis, not an official replacement |
| S04 | Core–mantle gravitational mode (CMG) | Correct equations/sign conventions and units; inertia/boundary conditions; literature-grounded parameter priors; electromagnetic-only, gravity-only, combined baselines; time series and train/test split | **BLOCKED — model specification/data** | Derive and unit-check equations, then specify held-out prediction protocol and observational series |
| S05 | Planetary active inference | State-space equations, units, noise, boundary conditions, explicit Markov-blanket graph/precision matrix, homeorhesis metric, non-inference controls, held-out forcing trajectories | **BLOCKED — formal model/data** | Publish executable equations and define a benchmark suite before coding |
| S06 | Practice-specific neuroplasticity | Defined network/input vectors/observation model; mapping to measurable fMRI/EEG outcomes; γ parameter provenance; independent datasets and controls | **BLOCKED — model/data** | Specify a reproducible network and source-grounded parameterization; do not infer causality from cross-sectional differences |
| S07 | Soul-specific comparative evidence | Operational definition of veridical perception; prospective timing and independent corroboration criteria; sensory leakage/memory/base-rate/publication-bias controls; eligible data | **BLOCKED — empirical design** | Write protocol and evidence criteria; retain qualitative likelihood ratios until empirical likelihoods can be estimated |
| S08 | IELF arbitration | Normalized route variables; parameter identifiability; precision-only, preference-only, RL-only, predictive-processing-only and baseline models; held-out predictions and calibration criteria | **BLOCKED — model comparison** | Specify model families, data-generating tasks, fitting protocol, and falsifiers before simulation |
| S09 | AI substrate audit | Representative biological and non-biological system set; independently justified criteria; system-specific evidence; ambiguous/undecided outcomes | **BLOCKED — criteria/sample** | Operationalize substrate-neutral criteria and define sampling; do not equate capacity to qualify with actual consciousness |
| S10 | Whole-cell model validation | Verified paper and model/code/data; source-specific validation targets and uncertainty intervals; held-out validation data; justified error bounds | **BLOCKED — source/code/data** | Verify exact primary record and artifacts; do not infer human cognition from a minimal bacterial model |
| S11 | Orch-OR vs. SAN | Exact observables, minimum detectable effects, positive/negative controls, power/sensitivity, preregistered decision rule for distinguishable/indistinguishable outcomes | **BLOCKED — experimental specification** | Define what measurement could discriminate the models and what would count as inconclusive |
| S12 | Earth-system cascades | Independently estimated coupling/threshold parameters; uncertainty; full/sparse/modular models; null models; historical calibration and held-out periods/forcing; non-circular homeorhesis outcome | **BLOCKED — data/model validation** | Specify data sources and held-out evaluation; do not fit and validate on the same “seven boundaries” count |

## Why none is marked executed

These are not merely missing computer runs. Several designs still lack a unique operational model, verified source definitions, appropriate empirical datasets, or acceptance criteria. Executing arbitrary code under those conditions would create a number without testing the intended claim. This is a substantive research blocker, not a reason to fill the gap with toy data.

## Reusable execution record required for each study

Before execution: design ID/version, report version/blob SHA, claim IDs, source provenance, hypotheses/rivals, model/code commit, data provenance/license, parameter sources, environment, seed plan, baselines, acceptance/failure/indeterminate criteria, planned analyses, and risk/ethics review where applicable.

After execution: exact command, timestamp, environment lock, input and output hashes, per-run seeds, logs/errors, complete numerical outputs, sensitivity/ablation results, deviations, failed runs, interpretation limited to the tested scope, and independent reproduction instructions.

## Current decision

**Full simulation execution: NOT CLEARED for S01–S12.** The designs are documented and triaged, but missing prerequisites must be resolved first. The five smoke tests are a separate suite and do not change this decision. The global research gate remains open.
