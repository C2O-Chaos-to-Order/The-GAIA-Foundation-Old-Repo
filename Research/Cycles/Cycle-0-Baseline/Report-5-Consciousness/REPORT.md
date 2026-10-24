# Report 5 — Consciousness

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R5 |
| Version | Baseline (Cycle 0) |
| Status | Researched (1 bounded pass); simulated (executed, see §Simulation); internally checked; **not independently reviewed** |
| Date | 2026-10-23 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing documents | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |

## Abstract
Baseline pass on concepts and theories of consciousness. Phenomenal ('what it is like') and access senses are distinct; at least four theory families compete; a preregistered adversarial test (n = 256) challenged key tenets of both IIT and GNWT. A toy recurrent 'ignition' model was executed and shows all-or-none sustained activity only with strong recurrence — a generic dynamical property that does not bear on phenomenal experience.

## Contents
Purpose & exclusions · Research questions & definitions · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Distinguish established findings about neural/cognitive processes from disputed interpretations of experience. Excluded: altered states, anaesthesia/coma measures (e.g. PCI), animal and machine consciousness.

## Research questions and definitions
Q1 What concepts of consciousness are in use? Q2 What do leading theories predict and how have they fared? Q3 What does an ignition-like dynamic require minimally?

**Definitions.** *Phenomenal consciousness*; *access consciousness* (S16). *Ignition*: sudden, self-sustaining large-scale activation proposed as a marker of conscious access (S20).

## Methods
One bounded research pass (2026-10-23). Source selection: primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), official data/assessments, chosen by targeted web search and fetched directly; each fetched page was snapshotted (SHA-256 recorded; third-party text not redistributed in the repository). Claims were matched to the specific passage supporting them (locator column); where only an abstract was accessible, this is stated. Conclusions classified Supported / Mixed / Contested / Interpretive / Hypothetical / Indeterminate. Simulation specified in `simulation/SPEC.md` before execution; outputs, parameters, seeds and environment are in the execution record. No claim is made beyond what was run.

## Evidence and findings
Status counts in this report's ledger: Supported: 4, Contested: 1, Indeterminate: 1. Findings are given claim-by-claim in the ledger below; each row is the unit of evidence.

## Competing theories and alternatives
Higher-order, global workspace, re-entry/predictive processing, integrated information (S19). Cogitate results (S18).

## Simulation

**SIM-R5-C0** (`simulation/`) — status: executed; finished 2026-10-23T23:51:27Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | w=8 transition 10%->90% within <=2 units | `[1.8, 2.8000000000000003]` | **Pass** |
| E2 | w=2 no sustained trials | `0.0` | **Pass** |
| E3 | w=8, a=0 spontaneous ignition <10% | `0.0` | **Pass** |

Specification: `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in EXECUTION_RECORD.json).

## Claim-to-source ledger
Machine-readable: `claims/claims.csv`; sources: `sources/sources.csv`.

| ID | Claim | Class | Status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0-R5-01 | Consciousness is studied under several distinct concepts, including Nagel's 'what it is like' (phenomenal) sense and an access sense concerning availability of states to other mental processes. | Interpretive/philosophical | **Supported** | S16 | §§ on 'What it is like' and 'Access consciousness' | High |  |
| C0-R5-02 | Major neuroscientific theories include higher-order, global workspace, re-entry/predictive-processing and integrated information theories, which differ in explanatory targets and neural commitments. | Empirical | **Supported** | S19 | Abstract | High |  |
| C0-R5-03 | Global Neuronal Workspace research proposes late amplification, long-range synchronization and prefronto-parietal 'ignition' as markers of conscious access. | Empirical | **Contested** | S20;S18 | S20 abstract; S18 abstract | Medium | S18 reports a general lack of ignition at stimulus offset. |
| C0-R5-04 | A preregistered adversarial test (n = 256; fMRI, MEG, iEEG) found results aligned with some predictions of IIT and GNWT while substantially challenging key tenets of both. | Empirical | **Supported** | S18 | Abstract | High | Single paradigm (suprathreshold visual stimuli). |
| C0-R5-05 | In SIM-R5-C0, a single recurrent rate unit showed all-or-none sustained activity under strong recurrence (ignition fraction rose from <10% to >90% between amplitudes 1.8 and 2.8) and none under weak recurrence; this is a dynamical toy and says nothing about phenomenal experience. | Mathematical/computational | **Supported** | SIM-R5-C0 | Report-5-Consciousness/simulation/outputs/results.json | High (toy only) | Bistability is generic to many non-conscious systems. |
| C0-R5-06 | No theory has been shown to resolve the phenomenal ('hard') aspect of consciousness. | Interpretive/philosophical | **Indeterminate** | S16;S18;S19 | Survey-level judgement | Medium |  |

## Relationships to other reports
R2 (prediction error, L03), R3 (dualism, L06), R4 (mystical experience, L08), R1 (embodiment, L02).

## Ethical implications
Do not infer consciousness or sentience from behaviour or from model dynamics (Research README §7). Ignition in a toy is not evidence of experience in any system, including AI.

## Limitations and counterevidence
S20 abstract only; S19 via third-party-hosted accepted manuscript. Toy model has one unit; no anatomy.

## Open questions and falsification criteria
Measurement problem: which markers survive adversarial tests? **Falsification:** C0-R5-03's 'ignition marker' status is weakened further if replications confirm lack of offset ignition (S18).

## Conclusion with evidence classification
Plural concepts: **Supported**. Specific theories' adequacy: **Contested**. Hard problem resolved: **Indeterminate** (no). Simulation: executed toy, 3/3 checks passed, interpretation limited to access-like dynamics.

## References
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/consciousness/> (accessed 2026-10-23; full text; snapshot SHA-256 `9e814583974e4f21…`)
- **S18** — Cogitate Consortium, Ferrante O, et al. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. Nature. doi:10.1038/s41586-025-08888-1 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/> (accessed 2026-10-23; full text (PMC12137136); snapshot SHA-256 `f5c54592f2db384a…`)
- **S19** — Seth AK, Bayne T (2022). Theories of consciousness. Nat Rev Neurosci 23:439-452. doi:10.1038/s41583-022-00587-4 <https://michaelpollan.com/wp-content/uploads/2026/02/SethBayne_NRN_accepted.pdf> (accessed 2026-10-23; accepted manuscript PDF (third-party host); snapshot SHA-256 `52d364e4a87b0354…`)
- **S20** — Dehaene S, Changeux JP (2011). Experimental and theoretical approaches to conscious processing. Neuron 70(2):200-227. doi:10.1016/j.neuron.2011.03.018 <https://pubmed.ncbi.nlm.nih.gov/21521609/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 21521609); snapshot SHA-256 `86ed373bf452594e…`)

## Change history
- 2026-10-23 — Baseline (Cycle 0): first version in this folder hierarchy. Builds on the governing README and plan; the earlier GAIA-PRELIM v0.1.0 package and workbench were deleted from `main` by the owner before this work (commits 802e17a, df9a561) and never contained committed per-report files (its PACKAGE_INDEX listed 01–07 reports as not attached); nothing from them is reused or overwritten.
