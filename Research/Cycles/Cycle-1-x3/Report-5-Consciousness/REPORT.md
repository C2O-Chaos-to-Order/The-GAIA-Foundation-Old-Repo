# Report 5 — Consciousness: awareness, attention, self-awareness, altered states, origin

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-1-X3-R5 |
| Version | Cycle 1 (x3) |
| Status | Researched (3 passes), simulated (3 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-0-Baseline/Report-5-Consciousness/REPORT.md` (Baseline v2) |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Cycle-1 access rule | Established literature claims need at least one full-text (or textbook) source; abstract-only claims are capped at Plausible |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 1 upgrades the attention-network and PCI claims to full text (PCI cutoff validated on 150 subjects; 94.7% sensitivity for minimally conscious patients; 9 of 43 vegetative-state patients with high complexity) and widens the theory set with higher-order theories and the global-workspace vs recurrent-processing dispute over phenomenal consciousness without access. Toy simulations map where an ignition unit is bistable (42% of a parameter grid), show bimodal near-threshold activity under masking, and show that 'local recurrence without global ignition' and global ignition are dissociable in a two-area toy — a structural point that cannot say which state accompanies experience.

## What changed in Cycle 1
Pass 1: C0v2-R5-02 → V01, C0v2-R5-06 → V07 (full text). Pass 2: V18 (HOT), V19 (GNW/RPT/no-report). Pass 3: V35 (predictive-processing critique) and the access dispute (C1-R5-02). A preprint calling IIT pseudoscience was identified but not fetched; it is not used.

Ledger: 17 claims (10 E, 4 P, 2 PS, 1 H); 5 new, 2 revised; the rest carried forward unchanged from Cycle 0 (each row's `c1_change` says which).

## Methods
Three successive research passes (consolidate → widen → challenge; notes in `research/pass-1..3/NOTES.md`) and three chained simulation iterations (`simulation/iter-1..3`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iterations 2 and 3 read the previous iteration's results). Sources were fetched directly, snapshotted, hashed (`../Provenance/SOURCE_REGISTER.csv`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (substantive; Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
**Concepts and measures.** Phenomenal vs access concepts (C0v2-R5-01); attention networks (C0v2-R5-02, full text); PCI as a level-of-consciousness index (C0v2-R5-06, full text); adversarial test results (C0v2-R5-10) — Established.

**Theories.** Higher-order theories (C1-R5-01, Established as description); GNW vs RPT on access (C1-R5-02, Plausible/Contested); attention–consciousness relation (C0v2-R5-03) and hot zone vs ignition (C0v2-R5-09) remain Plausible; entropic brain (C0v2-R5-07) Hypothetical.

**Origin and nature** — unresolved (C0v2-R5-12, Philosophical/Spiritual).

## Competing views and counter-evidence
GNW, RPT, HOT, IIT and predictive processing; no theory is established. The two-area toy shows the GNW-like and RPT-like signatures can come apart, which is what no-report paradigms try to exploit.

## Simulation (3 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Phase diagram of the C0 ignition unit over recurrence w and threshold theta: where is it bistable? | P1: Pass, P2: Pass | 2/2 | 0/0 |
| 2 | Backward-masking toy: near threshold, is late activity bimodal (all-or-none) in the bistable unit and absent in the weak unit? (an ignition-style signature, V19 GNW). | K1: Supported, K2: Supported, K3: Pass | 1/1 | 2/2 |
| 3 | Two-area toy (local sensory area L with recurrence, global area G): does 'local recurrence without global ignition' (an RPT-like state, V19) occur for coupling > 0, and how does global ignition depend on coupling? | A1: Supported, A2: Pass | 1/1 | 1/1 |

Iteration 1 phase diagram → iteration 2 masking signatures → iteration 3 two-area local vs global. All hypotheses supported; the bimodality coefficient proved a weak discriminator (also high when ignitions were rare), recorded as a limit.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-1 change |
|---|---|---|---|---|---|
| C0v2-R5-01 | E | Supported | Awareness/subjective experience: consciousness is studied under distinct concepts, including phenomenal ('what it is like') consciousness and access consciousness. | S16 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-02 | E | Supported | Attention: Petersen & Posner's attention-network framework (1990, updated 2012) has been elaborated with orienting and executive networks, developmental changes and genetic contributions to individual differences. | V01;U20 | Upgraded to full text V01. |
| C0v2-R5-03 | P | Contested | Attention and consciousness are closely related, but whether attention is necessary, sufficient, both or neither for consciousness is controversial. | U22 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-04 | PS | Interpretive | Self-awareness: self-consciousness is awareness of oneself as oneself (expressed by 'I', 'me', 'my'); mirror recognition, episodic memory and metacognition are studied as markers in infants and animals. | U23 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-05 | P | Contested | Perception and the neural correlates: a review locates the anatomical correlates of specific conscious percepts primarily in a posterior cortical 'hot zone' rather than a fronto-parietal network. | T11 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-06 | E | Supported | Altered states: the perturbational complexity index (TMS-evoked EEG compressibility) discriminates level of consciousness; in a validation on 150 benchmark subjects an empirical cutoff separated conscious from unconscious conditions with 100% sensitivity and specificity, then detected 94.7% of minimally conscious patients and flagged 9 of 43 vegetative-state patients with high complexity. | V07;T10 | Upgraded to full text V07 (Casarotto 2016); T10 kept as secondary. |
| C0v2-R5-07 | H | Hypothetical | Altered states: the 'entropic brain' hypothesis proposes that psychedelic states show elevated entropy of brain dynamics and that normal waking consciousness operates just below criticality. | U21 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-08 | E | Supported | Origin/nature: prominent theories include higher-order, global workspace, re-entry/predictive-processing and integrated-information theories; how they relate and whether they can be empirically distinguished is unclear. | S19 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-09 | P | Contested | Global Neuronal Workspace research proposes late amplification, long-range synchronization and prefronto-parietal 'ignition' as markers of conscious access. | S20;S18 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-10 | E | Supported | A preregistered adversarial test (n = 256; fMRI, MEG, iEEG) found results aligned with some predictions of IIT and GNWT while substantially challenging key tenets of both. | S18 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R5-11 | E | Supported | In SIM-R5-C0, a recurrent rate unit showed all-or-none sustained activity under strong recurrence (ignition rose from <10% to >90% between input 1.8 and 2.8) and none under weak recurrence; a dynamical toy with no bearing on phenomenal experience. | C0:SIM-R5-C0#E1;C0:SIM-R5-C0#E2;C0:SIM-R5-C0#E3 | Carried forward; cites the Cycle-0 run. Extended by C1-R5-03..05. |
| C0v2-R5-12 | PS | Indeterminate | How consciousness arises and what it ultimately is remain open: no theory has resolved the phenomenal ('hard') aspect; physicalist, dualist and other metaphysical answers persist. | S16;S18;S08 | Carried forward unchanged from Cycle 0 (v2). |
| C1-R5-01 | E | Supported | Higher-order theories explain the difference between unconscious and conscious mental states by a relation between the conscious state and a higher-order representation of it (a higher-order perception or thought). | V18 | New in Cycle 1. |
| C1-R5-02 | P | Contested | Global workspace and recurrent processing theories disagree on access: some views (e.g. global workspace) hold that attention is necessary for access, which entails phenomenal consciousness, whereas recurrent processing theory holds there can be phenomenal states that are not accessible; many scientists take the evidence to show no phenomenal consciousness without access. | V19 | New in Cycle 1. |
| C1-R5-03 | E | Supported | In SIM-R5-C1 iteration 1, the C0 ignition unit was bistable in 42% of a recurrence x threshold grid (77 cells); simulated bistability matched the fixed-point count in every cell, and the C0 weak (w = 2) and strong (w = 8) settings fall on opposite sides. | SIM-R5-C1/iter-1#P1;SIM-R5-C1/iter-1#P2 | New in Cycle 1. |
| C1-R5-04 | E | Supported | In SIM-R5-C1 iteration 2 (backward-masking toy), near-threshold late activity of the bistable unit was bimodal (bimodality coefficient 0.94-0.97 in all 20-80% ignition cells) while the weak unit never ignited. | SIM-R5-C1/iter-2#K1;SIM-R5-C1/iter-2#K2;SIM-R5-C1/iter-2#K3 | New in Cycle 1. |
| C1-R5-05 | E | Supported | In SIM-R5-C1 iteration 3 (two-area toy), a 'local recurrence without global ignition' state occurred for coupling 0-2.5, and global ignition rose steeply from 0.5% of trials at coupling 2 to 97% at 3: the two signatures are dissociable in the toy, which says nothing about which accompanies experience. | SIM-R5-C1/iter-3#A1;SIM-R5-C1/iter-3#A2 | New in Cycle 1. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-1 status |
|---|---|---|---|---|
| L07 | R2 Mind → R5 Consciousness | relationship | P | Basis now contested by V35; label Plausible retained. |
| L08 | R2 Mind → R5 Consciousness | distinction | E | The conceptual distinction is retained as Established; whether phenomenal consciousness exists without access is the contested question (C1-R5-02). |
| L12 | R3 Soul → R5 Consciousness | competing interpretation | PS | Unchanged. |
| L17 | R5 Consciousness → R1 Body | dependency | E | Basis upgraded to full text; Established retained. |
| L18 | R5 Consciousness → R4 Spirit | relationship | H | Unchanged (Hypothetical). |

## Limitations
Rate-unit toys; parameters illustrative; no claim about experience.

## Open questions and falsification
Can no-report paradigms find phenomenal signatures without access (testable)? Do PCI-high unresponsive patients later show covert awareness?

## Conclusion and gate
Measures of the level of consciousness are well supported; theories of its nature remain contested. Gate: **Indeterminate**.

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). [full text] <https://plato.stanford.edu/entries/dualism/>
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/consciousness/>
- **S18** — Cogitate Consortium, Ferrante O, et al. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. Nature. doi:10.1038/s41586-025-08888-1 [full text (PMC12137136)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/>
- **S19** — Seth AK, Bayne T (2022). Theories of consciousness. Nat Rev Neurosci 23:439-452. doi:10.1038/s41583-022-00587-4 [full text (accepted manuscript PDF, third-party host)] <https://michaelpollan.com/wp-content/uploads/2026/02/SethBayne_NRN_accepted.pdf>
- **S20** — Dehaene S, Changeux JP (2011). Experimental and theoretical approaches to conscious processing. Neuron 70(2):200-227. doi:10.1016/j.neuron.2011.03.018 [abstract only (NCBI E-utilities PMID 21521609)] <https://pubmed.ncbi.nlm.nih.gov/21521609/>
- **T10** — Casali AG, Gosseries O, Rosanova M, et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med 5(198):198ra105. doi:10.1126/scitranslmed.3006294 [abstract only (NCBI E-utilities PMID 23946194)] <https://pubmed.ncbi.nlm.nih.gov/23946194/>
- **T11** — Koch C, Massimini M, Boly M, Tononi G (2016). Neural correlates of consciousness: progress and problems. Nat Rev Neurosci 17(5):307-321. doi:10.1038/nrn.2016.22 [abstract only (NCBI E-utilities PMID 27094080)] <https://pubmed.ncbi.nlm.nih.gov/27094080/>
- **U20** — Petersen SE, Posner MI (2012). The attention system of the human brain: 20 years after. Annu Rev Neurosci 35:73-89. doi:10.1146/annurev-neuro-062111-150525 [abstract only (NCBI E-utilities PMID 22524787)] <https://pubmed.ncbi.nlm.nih.gov/22524787/>
- **U21** — Carhart-Harris RL, Leech R, Hellyer PJ, et al. (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. Front Hum Neurosci 8:20. doi:10.3389/fnhum.2014.00020 [abstract only (NCBI E-utilities PMID 24550805)] <https://pubmed.ncbi.nlm.nih.gov/24550805/>
- **U22** — Mole C. Attention. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/attention/>
- **U23** — Smith J. Self-Consciousness. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/self-consciousness/>
- **V01** — Petersen SE, Posner MI (2012). The attention system of the human brain: 20 years after. Annu Rev Neurosci 35:73-89. PMC3413263 (NIH author manuscript) [full text (PMC author manuscript via NCBI E-utilities)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3413263/>
- **V07** — Casarotto S, et al. (2016). Stratification of unresponsive patients by an independently validated index of brain complexity. Ann Neurol 80(5):718-729. doi:10.1002/ana.24779 [full text (Europe PMC PMC5132045)] <https://europepmc.org/article/PMC/PMC5132045>
- **V18** — Stanford Encyclopedia of Philosophy, entry 'Higher-Order Theories of Consciousness' (substantive revision 9 Jan 2026) [full text (SEP web page)] <https://plato.stanford.edu/entries/consciousness-higher/>
- **V19** — Stanford Encyclopedia of Philosophy, entry 'The Neuroscience of Consciousness' [full text (SEP web page)] <https://plato.stanford.edu/entries/consciousness-neuroscience/>

## Change history
- Cycle 0 Baseline v2 (2026-10-24): see `../../Cycle-0-Baseline/`.
- Cycle 1 (x3) (2026-10-24): this version; details in `CHANGELOG.md`.
