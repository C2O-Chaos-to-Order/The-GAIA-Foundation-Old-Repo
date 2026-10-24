# Report 1 — The Body

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R1 |
| Version | Baseline (Cycle 0) |
| Status | Researched (1 bounded pass); simulated (executed, see §Simulation); internally checked; **not independently reviewed** |
| Date | 2026-10-23 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing documents | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |

## Abstract
Baseline pass on the physical foundation of life, focused on homeostasis as physiology's organising concept and on the embodied-cognition debate. Sources support homeostasis as multi-loop feedback plus feedforward regulation; the embodied-cognition constitution claim is contested. A toy negative-feedback model was executed and behaved as control theory predicts, including failure under degraded gain and effector saturation.

## Contents
Purpose & exclusions · Research questions & definitions · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Establish what is well-supported about bodily regulation and where biological explanation is open. Excluded this pass: anatomy and nervous-system detail, sensory perception, recovery and health interventions (scheduled for later cycles).

## Research questions and definitions
Q1 What is homeostasis and how is it regulated? Q2 Is 'set point' a fixed value? Q3 Does the body constitute or only cause cognition? Q4 What does a minimal feedback model show and not show?

**Definitions.** *Homeostasis*: self-regulating process maintaining internal stability while adjusting to external conditions (S01). *Negative feedback*: a disturbance is countered by effector output restoring the regulated variable toward its set point (S02). *Embodied cognition*: research program holding the body or body–environment interaction constitutes or contributes to cognition (S03).

## Methods
One bounded research pass (2026-10-23). Source selection: primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), official data/assessments, chosen by targeted web search and fetched directly; each fetched page was snapshotted (SHA-256 recorded; third-party text not redistributed in the repository). Claims were matched to the specific passage supporting them (locator column); where only an abstract was accessible, this is stated. Conclusions classified Supported / Mixed / Contested / Interpretive / Hypothetical / Indeterminate. Simulation specified in `simulation/SPEC.md` before execution; outputs, parameters, seeds and environment are in the execution record. No claim is made beyond what was run.

## Evidence and findings
Status counts in this report's ledger: Supported: 4, Contested: 1, Indeterminate: 1. Findings are given claim-by-claim in the ledger below; each row is the unit of evidence.

## Competing theories and alternatives
Classical single-loop set-point models vs hierarchical, redundant multi-loop regulation with feedforward (S01). For embodiment: computational cognitivism vs embedded, extended and enactive views; Adams & Aizawa's coupling–constitution objection (S03).

## Simulation

**SIM-R1-C0** (`simulation/`) — status: executed; finished 2026-10-23T23:49:18Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | no-control x(T) = analytic 9.933 (tends to 10.0) | `9.9328` | **Pass** |
| E2 | P steady error 0.4762 | `0.4762` | **Pass** |
| E3 | |PI tail mean|<0.02 | `0.001` | **Pass** |
| E4 | degraded peak > intact peak and slower recovery | `[1.790515460146184, 0.3600061867586858, 10.99, 4.49]` | **Pass** |
| E5 | saturated PI final |x| > 0.05 | `9.9014` | **Pass** |

Specification: `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in EXECUTION_RECORD.json).

## Claim-to-source ledger
Machine-readable: `claims/claims.csv`; sources: `sources/sources.csv`.

| ID | Claim | Class | Status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0-R1-01 | Homeostasis is widely treated as a central unifying concept of physiology: a self-regulating process maintaining internal stability while adjusting to external change. | Empirical | **Supported** | S01 | Abstract: 'central unifying concept of physiology' | High | Essay-format review by one author; 'central' is a disciplinary judgement. |
| C0-R1-02 | Homeostatic regulation involves multiple interacting feedback systems plus feedforward control, not a single negative-feedback loop. | Empirical | **Supported** | S01 | Abstract: 'not merely the product of a single negative feedback cycle'; feedforward section | High |  |
| C0-R1-03 | A generic negative-feedback homeostatic mechanism can be described as sensor, error detector comparing to a set point, controller and effector; 'set point' does not imply a fixed value. | Empirical | **Supported** | S02 | 'error detector that compares the signal ... with the set point'; set point 'not meant to imply ... a fixed value' | High | Pedagogical model; real systems may lack an explicit set-point representation. |
| C0-R1-04 | Embodied cognition holds that the body or body–environment interaction constitutes or contributes to cognition; whether the role is constitutive or merely causal is disputed. | Interpretive/philosophical | **Contested** | S03 | Sections 2.1, 5 (coupling–constitution fallacy, Adams & Aizawa) | High | Replicability concerns for some embodied-cognition findings (S03 §7). |
| C0-R1-05 | In SIM-R1-C0, PI control restored the set point after a step disturbance, P-only control left the analytic residual error 0.476, degraded gains increased peak deviation (1.79 vs 0.36) and slowed recovery (10.99 vs 4.49 time units), and effector saturation prevented restoration. | Mathematical/computational | **Supported** | SIM-R1-C0 | Report-1-Body/simulation/outputs/summary.json | High (for the toy only) | Toy model; says nothing about specific physiology. |
| C0-R1-06 | The claim that disruption of homeostatic mechanisms is what leads to disease is stated by S01 as a general principle; this pass did not test its generality. | Interpretive/philosophical | **Indeterminate** | S01 | Abstract: 'disruption of homeostatic mechanisms is what leads to disease' | Medium | Not all disease is plausibly framed as homeostatic failure (e.g. some genetic or traumatic conditions); not checked this pass. |

## Relationships to other reports
R6 (homeostasis ↔ Daisyworld, analogy only), R2 and R5 (embodied cognition), R7 (cross-domain map L01, L02).

## Ethical implications
Framing all disease as 'homeostatic failure' (C0-R1-06) can misdirect blame or care if applied uncritically; keep it a hypothesis. Model outputs must not be presented as clinical guidance.

## Limitations and counterevidence
Three literature sources only; S01 is an essay-review by one author. The simulation is generic and parameter-free of physiology. Embodied-cognition findings face replication concerns (S03 §7; S05).

## Open questions and falsification criteria
Which regulated variables lack an explicit set-point representation? Under what conditions does the constitution thesis make different predictions from the causal thesis? **Falsification:** C0-R1-02 would be weakened by well-characterised homeostatic systems shown to operate with a single loop and no higher control; SIM-R1-C0 would be falsified by any pre-registered check failing on rerun.

## Conclusion with evidence classification
Homeostasis as multi-loop feedback/feedforward regulation: **Supported**. Constitutive embodiment: **Contested**. 'Disease = homeostatic disruption' as a universal principle: **Indeterminate**. Simulation: executed, all 5 pre-registered checks passed (E1 with a documented substituted check).

## References
- **S01** — Billman GE (2020). Homeostasis: The Underappreciated and Far Too Often Ignored Central Organizing Principle of Physiology. Front Physiol 11:200. doi:10.3389/fphys.2020.00200 <https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `01b91f81929856e9…`)
- **S02** — Modell H, Cliff W, Michael J, et al. (2015). A physiologist's view of homeostasis. Adv Physiol Educ 39(4):259-266. doi:10.1152/advan.00107.2015 <https://pmc.ncbi.nlm.nih.gov/articles/PMC4669363/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `60a3d718d7c987f5…`)
- **S03** — Shapiro L, Spaulding S (2021). Embodied Cognition. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/embodied-cognition/> (accessed 2026-10-23; full text; snapshot SHA-256 `406f421bebc61f3e…`)

## Change history
- 2026-10-23 — Baseline (Cycle 0): first version in this folder hierarchy. Builds on the governing README and plan; the earlier GAIA-PRELIM v0.1.0 package and workbench were deleted from `main` by the owner before this work (commits 802e17a, df9a561) and never contained committed per-report files (its PACKAGE_INDEX listed 01–07 reports as not attached); nothing from them is reused or overwritten.
