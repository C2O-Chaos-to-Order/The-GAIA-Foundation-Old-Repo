# Report 6 — Life as the Soul of the Earth; the Core as Its Heart

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R6 |
| Version | Baseline (Cycle 0) |
| Status | Researched (1 bounded pass); simulated (executed, see §Simulation); internally checked; **not independently reviewed** |
| Date | 2026-10-23 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing documents | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |

## Abstract
Part A: microbial life is documented by ≥3.4 Ga; ~1 million species are threatened; Daisyworld demonstrates how biota–environment coupling can regulate temperature in a toy, while Kirchner argues real biological feedbacks are on net amplifying. Part B: the core (outer radius ~3480 km, inner ~1220 km) sustains a geomagnetic field; IGRF-14 shows a 7.6% dipole decline 1900–2025, and free ohmic decay (~10⁴–10⁵ yr) is far shorter than the ≥3.3 Gyr record, consistent with continual dynamo regeneration. 'Soul' and 'heart' are metaphors.

## Contents
Purpose & exclusions · Research questions & definitions · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Separate ecological/geophysical mechanism from symbolic interpretation. Excluded: biogeochemical cycle quantification, origin-of-life chemistry, mantle/plate dynamics, reversal statistics.

## Research questions and definitions
Q1 When is life first securely evidenced? Q2 Does Daisyworld-style regulation describe Earth? Q3 What sustains the geomagnetic field and how is it changing?

**Definitions.** *Gaia hypothesis* variants (homeostatic, optimizing; S22). *Geodynamo*: self-sustaining field generation by core fluid motion. *Dipole moment*: from IGRF degree-1 Gauss coefficients.

## Methods
One bounded research pass (2026-10-23). Source selection: primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), official data/assessments, chosen by targeted web search and fetched directly; each fetched page was snapshotted (SHA-256 recorded; third-party text not redistributed in the repository). Claims were matched to the specific passage supporting them (locator column); where only an abstract was accessible, this is stated. Conclusions classified Supported / Mixed / Contested / Interpretive / Hypothetical / Indeterminate. Simulation specified in `simulation/SPEC.md` before execution; outputs, parameters, seeds and environment are in the execution record. No claim is made beyond what was run.

## Evidence and findings
Status counts in this report's ledger: Supported: 6, Contested: 2, Interpretive: 1. Findings are given claim-by-claim in the ledger below; each row is the unit of evidence.

## Competing theories and alternatives
Strong vs weak Gaia; Kirchner's critique (S22). Early-dynamo timing from Jack Hills zircons (S28) vs later critiques (not fetched; flagged).

## Simulation

**SIM-R6-C0** (`simulation/`) — status: executed; finished 2026-10-23T23:52:02Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | life band width >= 3x lifeless | `[0.82, 0.24]` | **Pass** |
| E2 | hysteresis: alive ranges differ up vs down | `[[0.72, 1.54], [0.63, 1.21]]` | **Pass** |
| E3 | dipole moment decreases 1900->latest | `-7.592` | **Pass** |
| E4 | tau <= 1e6 yr for all sigma | `{"500000.0": 24431, "1000000.0": 48861, "1500000.0": 73292}` | **Pass** |

Specification: `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in EXECUTION_RECORD.json).

## Claim-to-source ledger
Machine-readable: `claims/claims.csv`; sources: `sources/sources.csv`.

| ID | Claim | Class | Status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0-R6-01 | Microbial life is documented in the rock record by at least 3.4 billion years ago; earlier claims are disputed because abiotic processes and contamination can mimic biosignatures. | Empirical | **Supported** | S23 | Abstract | High |  |
| C0-R6-02 | IPBES estimates around 1 million animal and plant species are threatened with extinction and that the current extinction rate is at least tens to hundreds of times higher than the 10-million-year average. | Empirical | **Supported** | S24 | SPM key messages (A, B sections) | Medium-High | Estimate extrapolated; insect figures tentative (per SPM). |
| C0-R6-03 | Daisyworld shows that a coupled biota–temperature model with a peaked growth curve stabilises temperature; it was offered as a parable, not a model of Earth. | Mathematical/computational | **Supported** | S21b | Abstract; §1 | High |  |
| C0-R6-04 | Kirchner argues available evidence suggests biologically mediated feedbacks will on net amplify, not reduce, Earth's sensitivity to anthropogenic climate change, contrary to strong homeostatic Gaia. | Empirical | **Contested** | S22 | Abstract/summary; Vostok discussion | Medium | Gaia proponents dispute framing; not read this pass. |
| C0-R6-05 | In SIM-R6-C0, re-implemented Daisyworld kept T_e within 22.5±10 °C over luminosity 0.72–1.54 (width 0.82) vs 0.83–1.07 (0.24) without life, with hysteresis between up and down sweeps. | Mathematical/computational | **Supported** | SIM-R6-C0;S21b | Report-6-Earth/simulation/outputs/results.json | High (re-implementation) | Seed-area floor and integration scheme are our assumptions. |
| C0-R6-06 | Earth's outer core radius is ~3480 km and inner core radius ~1220 km; Lehmann inferred the inner core in 1936 from seismic waves and its solidity was later argued (e.g. Birch 1952). | Empirical | **Supported** | S25;S26 | S25 Fig.1 text; S26 | High |  |
| C0-R6-07 | Zircons 3.3–4.2 Gyr old record fields 0.12–1.0× recent equatorial strength, implying a geodynamo by 4.2 Ga. | Empirical | **Contested** | S28 | Abstract | Medium | Reliability of Jack Hills zircon magnetisation has been challenged in later literature (not fetched this pass). |
| C0-R6-08 | IGRF-14 dipole moment fell from 8.32×10²² A·m² (1900) to 7.69×10²² A·m² (2025), −7.6%; free ohmic decay time for the core is ~2.4–7.3×10⁴ yr for σ = 0.5–1.5×10⁶ S/m (assumed), ≥4.5×10⁴ times shorter than the paleomagnetic record — consistent with continual regeneration. | Mathematical/computational | **Supported** | SIM-R6-C0;S27;S25;S28 | Report-6-Earth/simulation/outputs/results.json | High (arithmetic) / σ assumed | Conductivity value assumed; decay estimate ignores inner-core and mode structure. |
| C0-R6-09 | Describing life as Earth's 'soul' or the core as its 'heart' is metaphor; no evidence in this pass supports Earth being conscious or ensouled. | Interpretive/philosophical | **Interpretive** | S21b;S22;G02 | — | High |  |

## Relationships to other reports
R1 (homeostasis analogy, L01; heart metaphor, L11), R3 (soul metaphor, L10), R7 (stewardship, L09).

## Ethical implications
Biodiversity decline (S24) supports stewardship as a premise; the normative conclusion requires ethical argument, not only data. Avoid sacralising metaphors displacing evidence in policy.

## Limitations and counterevidence
S23, S28, S29 abstract only; conductivity assumed; Daisyworld implementation assumptions (seed floor, Euler).

## Open questions and falsification criteria
Fetch critiques of Jack Hills paleointensity; compute decay with modern conductivity values; add Daisyworld variants (many species, mutation). **Falsification:** E4 would fail if σ were ≳2×10⁷ S/m (τ ≥ 10⁶ yr) — far above published estimates, but checkable.

## Conclusion with evidence classification
Early life ≥3.4 Ga: **Supported**. Biodiversity threat: **Supported**. Daisyworld regulation (toy): **Supported**. Strong Gaia for Earth: **Contested**. Dynamo regeneration required: **Supported** (order of magnitude). Earth ensouled/conscious: **Interpretive** (metaphor). Simulation: executed, 4/4 checks passed.

## References
- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md> (accessed 2026-10-23; full text (GitHub connector); snapshot SHA-256 `…`)
- **S21b** — Watson AJ, Lovelock JE (1983). Biological homeostasis of the global environment: the parable of Daisyworld. Tellus 35B:284-289. <https://b.tellusjournals.se/articles/1857/files/submission/proof/1857-1-15588-1-10-20221123.pdf> (accessed 2026-10-23; full text (Tellus B PDF); snapshot SHA-256 `a4c7825fa16f1da9…`)
- **S22** — Kirchner JW (2003). The Gaia Hypothesis: Conjectures and Refutations. Climatic Change 58:21-45. doi:10.1023/A:1023494111532 <https://courses.seas.harvard.edu/climate/eli/Courses/EPS281r/Sources/Gaia/more/Kirchner-2003.pdf> (accessed 2026-10-23; full text (Harvard course PDF); snapshot SHA-256 `70bbb9e30efe3502…`)
- **S23** — Javaux EJ (2019). Challenges in evidencing the earliest traces of life. Nature 572:451-460. doi:10.1038/s41586-019-1436-4 <https://pubmed.ncbi.nlm.nih.gov/31435057/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 31435057); snapshot SHA-256 `a9af9f5102d2134f…`)
- **S24** — IPBES (2019). Global Assessment Report on Biodiversity and Ecosystem Services: Summary for Policymakers. <https://files.ipbes.net/ipbes-web-prod-public-files/ipbes_global_assessment_report_summary_for_policymakers.pdf> (accessed 2026-10-23; full text PDF; snapshot SHA-256 `baa39de770154c47…`)
- **S25** — Waszek L, Irving J, Pham T-S, Tkalcic H (2023). Seismic insights into Earth's core. Nat Commun. doi:10.1038/s41467-023-41725-5 <https://www.nature.com/articles/s41467-023-41725-5> (accessed 2026-10-23; full text; snapshot SHA-256 `8e72a13616a2db11…`)
- **S26** — Boatman L (2023). September 1936: Seismologist Inge Lehmann Concludes That Earth Has an Inner Core. APS News. <https://www.aps.org/apsnews/2023/08/seismologist-lehmann-earth-inner-core> (accessed 2026-10-23; full text; snapshot SHA-256 `0aef630cab2bd156…`)
- **S27** — IAGA Working Group V-MOD / NOAA NCEI. IGRF-14 coefficient file igrf14coeffs.txt. <https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf14coeffs.txt> (accessed 2026-10-23; full file; snapshot SHA-256 `8f8d88403028fc4e…`)
- **S28** — Tarduno JA, Cottrell RD, Davis WJ, Nimmo F, Bono RK (2015). A Hadean to Paleoarchean geodynamo recorded by single zircon crystals. Science 349:521-524. doi:10.1126/science.aaa9114 <https://pubmed.ncbi.nlm.nih.gov/26228145/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 26228145); snapshot SHA-256 `e0a764578d3dfdf1…`)

## Change history
- 2026-10-23 — Baseline (Cycle 0): first version in this folder hierarchy. Builds on the governing README and plan; the earlier GAIA-PRELIM v0.1.0 package and workbench were deleted from `main` by the owner before this work (commits 802e17a, df9a561) and never contained committed per-report files (its PACKAGE_INDEX listed 01–07 reports as not attached); nothing from them is reused or overwritten.
