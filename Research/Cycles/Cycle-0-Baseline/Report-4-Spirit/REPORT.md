# Report 4 — The Spirit

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R4 |
| Version | Baseline (Cycle 0) |
| Status | Researched (1 bounded pass); simulated (executed, see §Simulation); internally checked; **not independently reviewed** |
| Date | 2026-10-23 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing documents | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |

## Abstract
Baseline pass on spirituality as studied empirically and philosophically. A systematic review finds religion/spirituality associated with better mental health on average, with mixed and negative findings; a large cohort found >weekly service attendance associated with lower mortality (HR 0.67). Measurement of 'spirituality' is contested as partly tautological. An E-value sensitivity analysis was executed (E = 1.97 after common-outcome conversion); a Monte Carlo check failed because of a specification error, which is preserved.

## Contents
Purpose & exclusions · Research questions & definitions · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Separate subjective experience, theological interpretation, and independently verifiable claims. Excluded this pass: tradition-specific theologies of spirit (ruach, pneuma hagion, qi, prana), practices research beyond attendance.

## Research questions and definitions
Q1 What associations between R/S and health are documented? Q2 How robust are they to confounding? Q3 What is 'mystical experience' in specialist philosophy?

**Definitions.** *R/S*: religion/spirituality as operationalised in S11. *E-value*: minimum confounder strength (risk-ratio scale) with both exposure and outcome needed to explain away an association (S14). *Mystical experience*: per S15, excludes paranormal visions/voices.

## Methods
One bounded research pass (2026-10-23). Source selection: primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), official data/assessments, chosen by targeted web search and fetched directly; each fetched page was snapshotted (SHA-256 recorded; third-party text not redistributed in the repository). Claims were matched to the specific passage supporting them (locator column); where only an abstract was accessible, this is stated. Conclusions classified Supported / Mixed / Contested / Interpretive / Hypothetical / Indeterminate. Simulation specified in `simulation/SPEC.md` before execution; outputs, parameters, seeds and environment are in the execution record. No claim is made beyond what was run.

## Evidence and findings
Status counts in this report's ledger: Mixed: 1, Supported: 2, Contested: 1, Interpretive: 1, Indeterminate: 1. Findings are given claim-by-claim in the ledger below; each row is the unit of evidence.

## Competing theories and alternatives
Causal (social support, meaning, health behaviours) vs confounding/selection (healthier people attend) explanations (S12); Koenig's 'tautology' critique of spirituality scales vs its critics (S13).

## Simulation

**SIM-R4-C0** (`simulation/`) — status: executed; finished 2026-10-23T23:50:59Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **False**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | E-values > 1 | `{"rare_E": 2.35, "common_E": 1.968, "common_E_CI": 1.85}` | **Pass** |
| E2 | crude RR at E <= 0.758+0.02 | `0.851` | **Fail** |
| E3 | weak confounding crude RR > 0.9 | `0.9787` | **Pass** |

Specification: `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in EXECUTION_RECORD.json).

## Claim-to-source ledger
Machine-readable: `claims/claims.csv`; sources: `sources/sources.csv`.

| ID | Claim | Class | Status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0-R4-01 | A systematic review of quantitative studies (1872–2010) reports that religion/spirituality is related to better mental health on average, with some studies showing negative or mixed associations. | Empirical | **Mixed** | S11 | 'related to better mental health (less depression, lower stress...)'; mixed/negative counts in subsections | Medium | Single-author review; observational designs dominate; publication bias not assessed here. |
| C0-R4-02 | In the Nurses' Health Study (n = 74,534), attending religious services more than once per week vs never was associated with lower all-cause mortality (HR 0.67, 95% CI 0.62–0.71); authors note possible unmeasured and residual confounding. | Empirical | **Supported** | S12 | Abstract results; limitations paragraph | High (association) / not causal | Women, mostly white US nurses; self-reported attendance. |
| C0-R4-03 | Many 'spirituality' measures are contaminated with mental-health and positive-character items, making some spirituality–health associations tautological. | Interpretive/philosophical | **Contested** | S13 | Abstract | Medium | Critics replied in the same journal (comments listed in PubMed record); not read this pass. |
| C0-R4-04 | In the SEP's account, mystical experience is defined to exclude paranormal experiences such as visions or voices, and mysticism is best understood as practices, texts and traditions aimed at transformation, not only experiences. | Interpretive/philosophical | **Interpretive** | S15 | Definition section | High (as description) | Definitions vary across scholars and traditions. |
| C0-R4-05 | For HR 0.67 the E-value is 2.35 (rare-outcome approximation) or 1.97 after common-outcome conversion (outcome risk 18%); CI-limit E-values 2.17 / 1.85. | Mathematical/computational | **Supported** | SIM-R4-C0;S14 | Report-4-Spirit/simulation/outputs/results.json | High (arithmetic) | E-value is a bound, not evidence that confounding exists or not. |
| C0-R4-06 | The SIM-R4-C0 Monte Carlo check E2 FAILED because its confounder parameterisation did not implement the E-value's definition; no conclusion is drawn from it. | Mathematical/computational | **Indeterminate** | SIM-R4-C0 | SPEC.md result note | High | Correction deferred to a separate recorded run. |

## Relationships to other reports
R1 (mortality outcome, L05), R2 (measurement/replication, L04), R3 (pneuma, L07), R5 (mystical experience, L08).

## Ethical implications
Health associations must not be used to pressure religious practice or stigmatise non-belief, consistent with the Research README's priority on dignity, consent and non-harm. Spiritual claims are not to be presented as proven mechanisms.

## Limitations and counterevidence
Observational evidence; single cohort for mortality; S13 read as abstract only; SIM-R4-C0 E2 failed.

## Open questions and falsification criteria
Correctly parameterised confounding simulation; meta-analytic estimates across cohorts; tradition-internal definitions of spirit. **Falsification:** C0-R4-02's causal interpretation would be undermined by a measured confounder with associations ≥ E-value (≈1.85–1.97).

## Conclusion with evidence classification
R/S–mental health: **Mixed**. Attendance–mortality association: **Supported** as association; causation **Indeterminate**. Spirituality measurement: **Contested**. Simulation: executed, 2/3 checks passed, E2 **Fail** preserved.

## References
- **S11** — Koenig HG (2012). Religion, Spirituality, and Health: The Research and Clinical Implications. ISRN Psychiatry 2012:278730. doi:10.5402/2012/278730 <https://pmc.ncbi.nlm.nih.gov/articles/PMC3671693/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `f61805702ffb1ede…`)
- **S12** — Li S, Stampfer MJ, Williams DR, VanderWeele TJ (2016). Association of Religious Service Attendance With Mortality Among Women. JAMA Intern Med 176(6):777-785. doi:10.1001/jamainternmed.2016.1615 <https://pmc.ncbi.nlm.nih.gov/articles/PMC5503841/> (accessed 2026-10-23; full text (PMC author manuscript PMC5503841); snapshot SHA-256 `18defddfc9d682ea…`)
- **S13** — Koenig HG (2008). Concerns about measuring 'spirituality' in research. J Nerv Ment Dis 196(5):349-355. doi:10.1097/NMD.0b013e31816ff796 <https://pubmed.ncbi.nlm.nih.gov/18477877/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 18477877); snapshot SHA-256 `fc3281466598d24f…`)
- **S14** — VanderWeele TJ, Ding P (2017). Sensitivity Analysis in Observational Research: Introducing the E-Value. Ann Intern Med 167(4):268-274. doi:10.7326/M16-2607 <https://dash.harvard.edu/bitstreams/7312037e-0f45-6bd4-e053-0100007fdf3b/download> (accessed 2026-10-23; full text (Harvard DASH manuscript); snapshot SHA-256 `d48e725b83e30bf8…`)
- **S15** — Jones R, Gellman J. Mysticism. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/mysticism/> (accessed 2026-10-23; full text; snapshot SHA-256 `3f1ce2bd4e8ec0b9…`)

## Change history
- 2026-10-23 — Baseline (Cycle 0): first version in this folder hierarchy. Builds on the governing README and plan; the earlier GAIA-PRELIM v0.1.0 package and workbench were deleted from `main` by the owner before this work (commits 802e17a, df9a561) and never contained committed per-report files (its PACKAGE_INDEX listed 01–07 reports as not attached); nothing from them is reused or overwritten.
