# Report 2 — The Mind

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R2 |
| Version | Baseline (Cycle 0) |
| Status | Researched (1 bounded pass); simulated (executed, see §Simulation); internally checked; **not independently reviewed** |
| Date | 2026-10-23 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing documents | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |

## Abstract
Baseline pass on memory and associative learning, plus the reproducibility problem that conditions all psychological claims. The Ebbinghaus forgetting curve has been replicated (single subject); Rescorla–Wagner explains blocking via prediction error; only 36% of 100 replicated psychology studies reached significance. Two bounded models were executed: RW blocking and a three-function fit to published savings data.

## Contents
Purpose & exclusions · Research questions & definitions · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Identify well-supported findings about learning/memory and the evidential standard psychology currently meets. Excluded this pass: perception, attention, emotion, language, self-concept, bias, social cognition, development (C0-R2-05).

## Research questions and definitions
Q1 Is the classic forgetting curve reproducible? Q2 What does prediction-error learning explain? Q3 How reliable are published psychological effects?

**Definitions.** *Savings*: reduction in relearning time relative to original learning (S04). *Blocking*: prior training of cue A reduces learning about X when AX is paired with the outcome (S06). *Replication*: an independent repetition of a study's procedure (S05).

## Methods
One bounded research pass (2026-10-23). Source selection: primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), official data/assessments, chosen by targeted web search and fetched directly; each fetched page was snapshotted (SHA-256 recorded; third-party text not redistributed in the repository). Claims were matched to the specific passage supporting them (locator column); where only an abstract was accessible, this is stated. Conclusions classified Supported / Mixed / Contested / Interpretive / Hypothetical / Indeterminate. Simulation specified in `simulation/SPEC.md` before execution; outputs, parameters, seeds and environment are in the execution record. No claim is made beyond what was run.

## Evidence and findings
Status counts in this report's ledger: Supported: 4, Indeterminate: 1. Findings are given claim-by-claim in the ledger below; each row is the unit of evidence.

## Competing theories and alternatives
Forgetting: power, logarithmic, exponential, summed-exponential and Memory-Chain models (S04). Learning: RW vs attention-based accounts (S06). Replication metrics: significance, effect-size ratio, subjective assessments (S05).

## Simulation

**SIM-R2-C0** (`simulation/`) — status: executed; finished 2026-10-23T23:49:42Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | V_X blocking < 0.1*V_X control | `[0.00039896132710136594, 0.49999999450244187]` | **Pass** |
| E2 | sum V on AX -> lambda | `[0.9999999999912268, 0.9999999890048837]` | **Pass** |
| E3 | Ebbinghaus: power or log AIC < exponential AIC | `{"exponential": -29.552, "power": -50.659, "log": -45.073}` | **Pass** |
| E4 | Dros: report only | `{"exponential": -37.279, "power": -38.441, "log": -43.385}` | **Pass** |

Specification: `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in EXECUTION_RECORD.json).

## Claim-to-source ledger
Machine-readable: `claims/claims.csv`; sources: `sources/sources.csv`.

| ID | Claim | Class | Status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0-R2-01 | Ebbinghaus' savings-based forgetting curve was replicated in a single-subject study (70 h of learning; intervals 20 min–31 days). | Empirical | **Supported** | S04 | Abstract; Table 3 | High | n = 1 subject; 31-day savings anomalously low (0.041). |
| C0-R2-02 | The Rescorla–Wagner model explains Kamin blocking through a shared prediction error (λ − ΣV); associative-learning research also documents attention-based phenomena RW does not capture alone. | Empirical | **Supported** | S06 | Section on RW and blocking; discussion of attention/prediction-error variants | High | RW is one of several learning models; known failures noted in S06. |
| C0-R2-03 | In a large multi-site replication of 100 psychology studies, 36% of replications had statistically significant results and replication effects were about half the magnitude of originals. | Empirical | **Supported** | S05 | Abstract/summary: 'Thirty-six percent of replications had statistically significant results' | High | Replication success metrics are debated; field-specific rates vary. |
| C0-R2-04 | In SIM-R2-C0, RW produced blocking (V_X 0.0004 vs 0.50 control); on Ebbinghaus data power (AIC −50.7) and log (−45.1) fit better than exponential (−29.6); on Dros data log fit best (−43.4). | Mathematical/computational | **Supported** | SIM-R2-C0 | Report-2-Mind/simulation/outputs/results.json | High (computation) | 7 data points; AIC comparison among 2-parameter forms only; S04's own fits use other models. |
| C0-R2-05 | Perception, attention, emotion, language, self-concept, bias, social cognition and development were NOT researched in this baseline pass. | Interpretive/philosophical | **Indeterminate** | G02 | RESEARCH_PLAN_EXTENSION §2 Report 2 scope | High | Scope gap; scheduled for later cycles. |

## Relationships to other reports
R5 (prediction-error/predictive-processing theories, L03), R4 (measurement validity, L04), R1 (embodiment, L02).

## Ethical implications
Low replication rates (S05) mean GAIA must not encode single-study psychological effects as facts about persons. Avoid using learning models to justify manipulative design.

## Limitations and counterevidence
n = 1 in S04; 7 data points per fit; AIC among 2-parameter forms only. S06 is a mini-review. Large parts of the Report 2 scope are not yet researched.

## Open questions and falsification criteria
Does the 1-day 'jump' in savings (S04) reflect sleep consolidation? **Falsification:** C0-R2-04's ranking would change if fits on the raw OSF data (osf.io/6kfrp) differ materially from Table 3 values.

## Conclusion with evidence classification
Forgetting-curve replication: **Supported** (with n = 1 caveat). RW explains blocking: **Supported** as a model result. Psychology reproducibility concern: **Supported**. Unresearched Report 2 domains: **Indeterminate**. Simulation: executed, 4/4 checks passed; one pre-run rationale was withdrawn as unverified.

## References
- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md> (accessed 2026-10-23; full text (GitHub connector); snapshot SHA-256 `…`)
- **S04** — Murre JMJ, Dros J (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. PLoS ONE 10(7):e0120644. doi:10.1371/journal.pone.0120644 <https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `4d690164934877ea…`)
- **S05** — Open Science Collaboration (2015). Estimating the reproducibility of psychological science. Science 349:aac4716. doi:10.1126/science.aac4716 <https://www.reed.edu/psychology/scalp/assets/journal-articles/OSC_RP_2015_Science.pdf> (accessed 2026-10-23; full text (PDF hosted by Reed College); snapshot SHA-256 `4387db34aa0a2633…`)
- **S06** — Holland PC, Schiffino FL (2016). Mini-Review: Prediction errors, attention and associative learning. Neurobiol Learn Mem (PMC4862921). <https://pmc.ncbi.nlm.nih.gov/articles/PMC4862921/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `8596bd21fea7f671…`)

## Change history
- 2026-10-23 — Baseline (Cycle 0): first version in this folder hierarchy. Builds on the governing README and plan; the earlier GAIA-PRELIM v0.1.0 package and workbench were deleted from `main` by the owner before this work (commits 802e17a, df9a561) and never contained committed per-report files (its PACKAGE_INDEX listed 01–07 reports as not attached); nothing from them is reused or overwritten.
