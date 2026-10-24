# Report 5 — Consciousness: the foundation of subjective experience and awareness

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R5 |
| Version | Baseline v2 (Cycle 0, framework-aligned) |
| Status | Researched (1 bounded pass, framework-aligned); simulated (executed, see §Simulation); internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; organizing principle: GAIA Is the Motherthread) |
| Integrity rules | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |
| Conclusion labels | Established / Plausible / Philosophical/Spiritual / Hypothetical (mapping to repository statuses: `../FRAMEWORK.md` appendix) |

## Abstract
Awareness, subjective experience, attention, self-awareness, perception and altered states, and the open question of how consciousness arises and what it is. No theory is treated as having solved consciousness. Established: phenomenal vs access concepts; attention-network research; a perturbational complexity index that tracks the level of consciousness across wake, sleep, anaesthesia and coma recovery; an adversarial test that challenged key tenets of both global workspace and integrated information theories. Contested or hypothetical: posterior 'hot zone' vs fronto-parietal ignition; entropy accounts of psychedelic states. Toy ignition model executed (all checks passed); it says nothing about experience itself.

## Contents
Purpose & exclusions · Research questions & definitions · Framework scope coverage · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Scope (framework, Report 5): awareness, subjective experience, attention, self-awareness, perception, altered states, and the open question of origin and nature; domains neuroscience, philosophy of mind, consciousness studies. Boundary: no theory has solved consciousness.

## Research questions and definitions
1. What concepts of consciousness are in use? 2. How do attention and consciousness relate? 3. What is self-awareness and how is it studied? 4. Where are the neural correlates of perception? 5. What do altered states reveal? 6. What do current theories claim about origin and nature?

## Framework scope coverage
Every scope item the framework lists for this report, with the claims that address it.

| Framework scope item | Claims | Labels |
|---|---|---|
| Awareness / subjective experience | C0v2-R5-01 | Established |
| Attention | C0v2-R5-02; C0v2-R5-03 | Established, Plausible |
| Self-awareness | C0v2-R5-04 | Philosophical/Spiritual |
| Perception & neural correlates | C0v2-R5-05; C0v2-R5-09 | Plausible |
| Altered states | C0v2-R5-06; C0v2-R5-07 | Established, Hypothetical |
| Theories / origin and nature | C0v2-R5-08; C0v2-R5-10; C0v2-R5-11; C0v2-R5-12 | Established, Philosophical/Spiritual |

## Methods
One bounded, framework-aligned research pass (2026-10-23/24) that reuses valid v1 sources and adds new ones. Sources were primary texts, primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), open textbooks and official assessments, found by targeted search and fetched directly. Each fetched page was snapshotted and its SHA-256 recorded; third-party text is not redistributed. Each claim is tied to the passage that supports it (locator) and labelled with a framework label plus a repository class/status. Where only an abstract or excerpt was accessible, the access mode says so. Every Established literature claim carries a verification phrase that was re-checked against a fresh fetch of its source (see `../Verification/VERIFICATION.md`). Simulations were specified in `simulation/SPEC.md` before execution and re-run fresh for v2.

## Evidence and findings
Label counts in this report's ledger: Established: 6, Plausible: 3, Philosophical/Spiritual: 2, Hypothetical: 1.

**Concepts.** Phenomenal ('what it is like') vs access consciousness (01, Established).

**Attention.** Attention-network research (orienting, executive) is a mature framework (02, Established). Whether attention is necessary or sufficient for consciousness is controversial (03, Plausible).

**Self-awareness.** Self-awareness is awareness of oneself *as oneself*; mirror self-recognition and metacognition serve as contested markers (04, Philosophical).

**Perception and correlates.** One review places correlates of specific percepts in a posterior hot zone (05, Plausible/contested). The global workspace view proposes prefronto-parietal ignition (09, Plausible/contested).

**Altered states.** PCI discriminates the level of consciousness across wakefulness, sleep, anaesthesia and coma recovery (06, Established). Entropy accounts of psychedelic states are a hypothesis (07).

**Theories.** Four theory families exist (08). An adversarial test challenged key tenets of both IIT and GNWT (10). The toy model shows generic ignition-like bistability (11). How consciousness arises and what it is remains open (12, Philosophical/Spiritual).

## Competing theories and alternatives
Global neuronal workspace (prefrontal ignition, access) vs integrated information theory (posterior complexity) vs higher-order theories vs re-entry/predictive processing (S19). Metaphysically: physicalism vs dualism vs others (S08, S16). The Cogitate results (S18) did not crown any theory.

## Simulation
**SIM-R5-C0** — status: executed; run finished 2026-10-24T00:24:45Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | w=8 transition 10%->90% within <=2 units | `[1.8, 2.8000000000000003]` | **Pass** |
| E2 | w=2 no sustained trials | `0.0` | **Pass** |
| E3 | w=8, a=0 spontaneous ignition <10% | `0.0` | **Pass** |

Specification (written before execution, incl. v2 changes and recorded deviations): `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in `simulation/EXECUTION_RECORD.json`). Simulation results are labelled Established only for the model itself, never for the real-world system.

## Claim-to-source ledger
Machine-readable: `claims/claims.csv` (includes verification phrases); sources: `sources/sources.csv`.

| ID | Claim | Framework label | Repo class / status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0v2-R5-01 | Awareness/subjective experience: consciousness is studied under distinct concepts, including phenomenal ('what it is like') consciousness and access consciousness. | **Established** | Interpretive/philosophical / Supported | S16 | Concepts sections | High (as description) |  |
| C0v2-R5-02 | Attention: Petersen & Posner's attention-network framework (1990, updated 2012) has been elaborated with orienting and executive networks, developmental changes and genetic contributions to individual differences. | **Established** | Empirical / Supported | U20 | Abstract | High | Abstract-level access only. |
| C0v2-R5-03 | Attention and consciousness are closely related, but whether attention is necessary, sufficient, both or neither for consciousness is controversial. | **Plausible** | Interpretive/philosophical / Contested | U22 | Opening; §3.1 | High (as description) |  |
| C0v2-R5-04 | Self-awareness: self-consciousness is awareness of oneself as oneself (expressed by 'I', 'me', 'my'); mirror recognition, episodic memory and metacognition are studied as markers in infants and animals. | **Philosophical/Spiritual** | Interpretive/philosophical / Interpretive | U23 | Opening; §5 | High (as description) | Markers are contested proxies. |
| C0v2-R5-05 | Perception and the neural correlates: a review locates the anatomical correlates of specific conscious percepts primarily in a posterior cortical 'hot zone' rather than a fronto-parietal network. | **Plausible** | Empirical / Contested | T11 | Abstract | Medium | Authors include IIT proponents; GNWT proponents dispute this (S20). |
| C0v2-R5-06 | Altered states: the perturbational complexity index (TMS-evoked EEG compressibility) discriminated the level of consciousness during wakefulness, sleep, anaesthesia and in patients emerging from coma. | **Established** | Empirical / Supported | T10 | Abstract | High | Measures level, not content, of consciousness. |
| C0v2-R5-07 | Altered states: the 'entropic brain' hypothesis proposes that psychedelic states show elevated entropy of brain dynamics and that normal waking consciousness operates just below criticality. | **Hypothetical** | Empirical / Hypothetical | U21 | Abstract | Low-Medium | Proposal built on limited psilocybin imaging data. |
| C0v2-R5-08 | Origin/nature: prominent theories include higher-order, global workspace, re-entry/predictive-processing and integrated-information theories; how they relate and whether they can be empirically distinguished is unclear. | **Established** | Interpretive/philosophical / Supported | S19 | Abstract | High (as description) |  |
| C0v2-R5-09 | Global Neuronal Workspace research proposes late amplification, long-range synchronization and prefronto-parietal 'ignition' as markers of conscious access. | **Plausible** | Empirical / Contested | S20;S18 | S20 abstract; S18 abstract | Medium | S18 reports a general lack of ignition at stimulus offset. |
| C0v2-R5-10 | A preregistered adversarial test (n = 256; fMRI, MEG, iEEG) found results aligned with some predictions of IIT and GNWT while substantially challenging key tenets of both. | **Established** | Empirical / Supported | S18 | Abstract | High | Single paradigm (suprathreshold visual stimuli). |
| C0v2-R5-11 | In SIM-R5-C0, a recurrent rate unit showed all-or-none sustained activity under strong recurrence (ignition rose from <10% to >90% between input 1.8 and 2.8) and none under weak recurrence; a dynamical toy with no bearing on phenomenal experience. | **Established** | Mathematical/computational / Supported | SIM-R5-C0#E1;SIM-R5-C0#E2;SIM-R5-C0#E3 | outputs/results.json | High (toy only) | Bistability is generic to many non-conscious systems. |
| C0v2-R5-12 | How consciousness arises and what it ultimately is remain open: no theory has resolved the phenomenal ('hard') aspect; physicalist, dualist and other metaphysical answers persist. | **Philosophical/Spiritual** | Interpretive/philosophical / Indeterminate | S16;S18;S08 | Survey-level judgement | Medium |  |

## Relationships to other reports
R1: level of consciousness depends on bodily brain states (L17). R2: predictive processing and access vs phenomenal (L07, L08). R3: subject of experience (L12). R4: altered and mystical states (L18). GAIA motherthread: awareness as part of Earth's living whole is a Philosophical/Spiritual framing; nothing here attributes consciousness to Earth or its core.

## Ethical implications
Consciousness measures such as PCI bear on clinical decisions for unresponsive patients; theory disputes should not be overstated in that context.

## Limitations and counterevidence
Several sources are abstract-only (U20, U21, T10, T11, S20). The toy model is not a consciousness model. Animal consciousness and the meditation literature were not covered. Not independently reviewed.

## Open questions and falsification criteria
- Which theory, if any, survives adversarial tests? *Reject* a theory when its preregistered predictions fail (as partly happened in S18).
- Is attention necessary for consciousness? *Test:* no-report paradigms with tightly controlled attention.
- Hard problem: no agreed test; recorded as open.

## Conclusion with evidence classification
Established: concepts, attention networks, PCI across altered states, adversarial-test outcome, toy behaviour. Plausible: attention–consciousness relation, hot zone vs ignition. Hypothetical: entropic brain. Philosophical/Spiritual: self-awareness markers' meaning; origin and nature of consciousness.

## References
- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md> (accessed 2026-10-23; full text (GitHub connector))
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md> (accessed 2026-10-24; full text (owner-supplied file); snapshot SHA-256 `2bad2984fe2109de…`)
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). <https://plato.stanford.edu/entries/dualism/> (accessed 2026-10-23; full text; snapshot SHA-256 `ab916c4bcb92e362…`)
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/consciousness/> (accessed 2026-10-23; full text; snapshot SHA-256 `9e814583974e4f21…`)
- **S18** — Cogitate Consortium, Ferrante O, et al. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. Nature. doi:10.1038/s41586-025-08888-1 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/> (accessed 2026-10-23; full text (PMC12137136); snapshot SHA-256 `f5c54592f2db384a…`)
- **S19** — Seth AK, Bayne T (2022). Theories of consciousness. Nat Rev Neurosci 23:439-452. doi:10.1038/s41583-022-00587-4 <https://michaelpollan.com/wp-content/uploads/2026/02/SethBayne_NRN_accepted.pdf> (accessed 2026-10-23; accepted manuscript PDF (third-party host); snapshot SHA-256 `52d364e4a87b0354…`)
- **S20** — Dehaene S, Changeux JP (2011). Experimental and theoretical approaches to conscious processing. Neuron 70(2):200-227. doi:10.1016/j.neuron.2011.03.018 <https://pubmed.ncbi.nlm.nih.gov/21521609/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 21521609); snapshot SHA-256 `86ed373bf452594e…`)
- **T10** — Casali AG, Gosseries O, Rosanova M, et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med 5(198):198ra105. doi:10.1126/scitranslmed.3006294 <https://pubmed.ncbi.nlm.nih.gov/23946194/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 23946194); snapshot SHA-256 `eff85683c74ad77f…`)
- **T11** — Koch C, Massimini M, Boly M, Tononi G (2016). Neural correlates of consciousness: progress and problems. Nat Rev Neurosci 17(5):307-321. doi:10.1038/nrn.2016.22 <https://pubmed.ncbi.nlm.nih.gov/27094080/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 27094080); snapshot SHA-256 `117bb7cece1d8719…`)
- **U20** — Petersen SE, Posner MI (2012). The attention system of the human brain: 20 years after. Annu Rev Neurosci 35:73-89. doi:10.1146/annurev-neuro-062111-150525 <https://pubmed.ncbi.nlm.nih.gov/22524787/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 22524787); snapshot SHA-256 `f82a961064ed3cc3…`)
- **U21** — Carhart-Harris RL, Leech R, Hellyer PJ, et al. (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. Front Hum Neurosci 8:20. doi:10.3389/fnhum.2014.00020 <https://pubmed.ncbi.nlm.nih.gov/24550805/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 24550805); snapshot SHA-256 `61708a188f0a924a…`)
- **U22** — Mole C. Attention. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/attention/> (accessed 2026-10-24; full text; snapshot SHA-256 `b78a4e33bf1ba6ef…`)
- **U23** — Smith J. Self-Consciousness. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/self-consciousness/> (accessed 2026-10-24; full text; snapshot SHA-256 `7ce6a963f7578826…`)

## Change history
- **2026-10-24 — Baseline v2 (Cycle 0, framework-aligned).** Rewritten against FRAMEWORK.md. Added attention (02, 03), self-awareness (04), perception/NCC (05), altered states (06, 07). v1 claims C0-R5-01…06 map to C0v2-R5-01, 08, 09, 10, 11, 12. Simulation re-run unchanged and identical to v1. Sources added: T10, T11, U20–U23.
- 2026-10-23 — Baseline (Cycle 0) v1: first version, built mainly on Research/README.md and RESEARCH_PLAN_EXTENSION.md (v1 files are superseded in place; the full v1 text remains in this branch's git history, commits before the v2 push). The earlier GAIA-PRELIM v0.1.0 package was deleted from `main` by the owner (commits 802e17a, df9a561) and never contained committed per-report files; nothing from it is reused.
