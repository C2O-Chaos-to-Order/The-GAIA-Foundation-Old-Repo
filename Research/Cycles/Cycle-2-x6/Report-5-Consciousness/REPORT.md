# Report 5 — Consciousness: awareness, attention and subjective experience

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-2-X6-R5 |
| Version | Cycle 2 (x6) |
| Status | Researched (6 passes), simulated (6 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-1-x3/Report-5-Consciousness/REPORT.md` (Cycle 1) and `../../Cycle-0-Baseline/` |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule (Report 7) |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 2 follows up the GNW–IIT adversarial collaboration (preregistered protocol, W12, E) and turns to complexity measures. Full-text sources: spontaneous EEG complexity decreases under propofol (W13, P, single study), and proponents argue that complexity measures converge as markers of consciousness and describe the perturbational complexity index (W11, P). A challenge source shows rats under sevoflurane whose wakefulness was not restored but whose cortical complexity rose to wake-like levels (W15, P, contested). A toy Kuramoto network (six iterations) shows why perturbation matters: spontaneous Lempel-Ziv complexity was highest for uncoupled noisy units (Spearman −0.98 with coupling), whereas a PCI-like measure was low for them (0.22) and peaked at intermediate coupling (2.7× both ends). The peak was **not supported** as robust (6 of 9 size–seed settings; it failed at 64 units with a fixed 10-unit kick), and reducing between-module coupling lowered PCI-like mostly but not monotonically (**not supported**).

## What changed in Cycle 2
Pass 1 ran logged searches (GNW and IIT; perturbational complexity) and selected W12. Pass 2 read W11 and W13 in full. Pass 3 widened to PCI validation (broad query, ~19,500 hits, not screened beyond the top results; no additional source selected). Pass 4 (challenge) used a title-restricted query and selected W15 (dissociation of consciousness from EEG complexity). Pass 5 executed the complexity simulations; a small pilot used to set the coupling range is disclosed in the SPEC. Pass 6 filled four empty limits fields and re-assessed labels (none changed).

Ledger: 23 claims (13 E, 7 P, 2 PS, 1 H); 6 new; 4 carried claims had their empty limits field filled; 0 carried claims annotated with Cycle-2 evidence; no carried claim changed label or status (each row's `c2_change` says which).

## Methods
Six successive research passes (1 logged systematic search → 2 deepen → 3 widen → 4 challenge → 5 carried agenda item → 6 consolidation; notes in `research/pass-1..6/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and six chained simulation iterations (`simulation/iter-1..6`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
- **Adversarial protocol (E; W12)**; outcomes remain as in Cycle 1 (neither theory fully supported).
- **Complexity markers (P; W11, W13)** — proponent synthesis and a single study.
- **Dissociation (P, contested; W15).**
- **Spontaneous vs perturbational complexity (E, simulation; C2-R5-04).**
- **PCI-like peak not robust; disconnection not monotone (E, simulation; C2-R5-05).**

## Competing views and counter-evidence
Complexity may index arousal or drug effects rather than consciousness (W15). Measures of the 'level' of consciousness do not address the phenomenal question (C0v2-R5-12, PS, Indeterminate).

## Simulation (6 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Validate the Lempel-Ziv (LZ76, Kaspar-Schuster) implementation used for both spontaneous and perturbational complexity. | Z1: Pass, Z2: Pass, Z3: Pass | 3/3 | 0/0 |
| 2 | Spontaneous complexity vs coupling: is it simply maximal for independent (uncoupled) units? (The known confound that motivates perturbational measures.) | S1: Supported | 0/0 | 1/1 |
| 3 | Perturbational (PCI-like) complexity vs coupling: does it peak at intermediate coupling (integrated AND differentiated responses)? | P1: Supported | 0/0 | 1/1 |
| 4 | Dissociation: an uncoupled, very noisy network vs the network at the PCI-like peak found in iteration 3. | N1: Supported | 0/0 | 1/1 |
| 5 | 'Anaesthesia-like' manipulation (loosely after W13): reduce between-module coupling at fixed within-module coupling; does PCI-like fall? | D1: Not supported | 0/0 | 0/1 |
| 6 | Consolidation: does the iteration-3 inverted-U replicate across network sizes and seeds? | R1: Not supported | 0/0 | 0/1 |

Iterations: (1) LZ76 validation; (2) spontaneous complexity vs coupling; (3) PCI-like vs coupling; (4) dissociation; (5) between-module disconnection; (6) replication over sizes and seeds (fails at N = 64; perturbation not scaled — a design limit).

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-2 change |
|---|---|---|---|---|---|
| C0v2-R5-01 | E | Supported | Awareness/subjective experience: consciousness is studied under distinct concepts, including phenomenal ('what it is like') consciousness and access consciousness. | S16 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R5-02 | E | Supported | Attention: Petersen & Posner's attention-network framework (1990, updated 2012) has been elaborated with orienting and executive networks, developmental changes and genetic contributions to individual differences. | V01;U20 | Carried unchanged. |
| C0v2-R5-03 | P | Contested | Attention and consciousness are closely related, but whether attention is necessary, sufficient, both or neither for consciousness is controversial. | U22 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R5-04 | PS | Interpretive | Self-awareness: self-consciousness is awareness of oneself as oneself (expressed by 'I', 'me', 'my'); mirror recognition, episodic memory and metacognition are studied as markers in infants and animals. | U23 | Carried unchanged. |
| C0v2-R5-05 | P | Contested | Perception and the neural correlates: a review locates the anatomical correlates of specific conscious percepts primarily in a posterior cortical 'hot zone' rather than a fronto-parietal network. | T11 | Carried unchanged. |
| C0v2-R5-06 | E | Supported | Altered states: the perturbational complexity index (TMS-evoked EEG compressibility) discriminates level of consciousness; in a validation on 150 benchmark subjects an empirical cutoff separated conscious from unconscious conditions with 100% sensitivity and specificity, then detected 94.7% of minimally conscious patients and flagged 9 of 43 vegetative-state patients with high complexity. | V07;T10 | Carried unchanged. |
| C0v2-R5-07 | H | Hypothetical | Altered states: the 'entropic brain' hypothesis proposes that psychedelic states show elevated entropy of brain dynamics and that normal waking consciousness operates just below criticality. | U21 | Carried unchanged. |
| C0v2-R5-08 | E | Supported | Origin/nature: prominent theories include higher-order, global workspace, re-entry/predictive-processing and integrated-information theories; how they relate and whether they can be empirically distinguished is unclear. | S19 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R5-09 | P | Contested | Global Neuronal Workspace research proposes late amplification, long-range synchronization and prefronto-parietal 'ignition' as markers of conscious access. | S20;S18 | Carried unchanged. |
| C0v2-R5-10 | E | Supported | A preregistered adversarial test (n = 256; fMRI, MEG, iEEG) found results aligned with some predictions of IIT and GNWT while substantially challenging key tenets of both. | S18 | Carried unchanged. |
| C0v2-R5-11 | E | Supported | In SIM-R5-C0, a recurrent rate unit showed all-or-none sustained activity under strong recurrence (ignition rose from <10% to >90% between input 1.8 and 2.8) and none under weak recurrence; a dynamical toy with no bearing on phenomenal experience. | C0:SIM-R5-C0#E1;C0:SIM-R5-C0#E2;C0:SIM-R5-C0#E3 | Carried unchanged. |
| C0v2-R5-12 | PS | Indeterminate | How consciousness arises and what it ultimately is remain open: no theory has resolved the phenomenal ('hard') aspect; physicalist, dualist and other metaphysical answers persist. | S16;S18;S08 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C1-R5-01 | E | Supported | Higher-order theories explain the difference between unconscious and conscious mental states by a relation between the conscious state and a higher-order representation of it (a higher-order perception or thought). | V18 | Carried unchanged. |
| C1-R5-02 | P | Contested | Global workspace and recurrent processing theories disagree on access: some views (e.g. global workspace) hold that attention is necessary for access, which entails phenomenal consciousness, whereas recurrent processing theory holds there can be phenomenal states that are not accessible; many scientists take the evidence to show no phenomenal consciousness without access. | V19 | Carried unchanged. |
| C1-R5-03 | E | Supported | In SIM-R5-C1 iteration 1, the C0 ignition unit was bistable in 42% of a recurrence x threshold grid (77 cells); simulated bistability matched the fixed-point count in every cell, and the C0 weak (w = 2) and strong (w = 8) settings fall on opposite sides. | SIM-R5-C1/iter-1#P1;SIM-R5-C1/iter-1#P2 | Carried unchanged. |
| C1-R5-04 | E | Supported | In SIM-R5-C1 iteration 2 (backward-masking toy), near-threshold late activity of the bistable unit was bimodal (bimodality coefficient 0.94-0.97 in all 20-80% ignition cells) while the weak unit never ignited. | SIM-R5-C1/iter-2#K1;SIM-R5-C1/iter-2#K2;SIM-R5-C1/iter-2#K3 | Carried unchanged. |
| C1-R5-05 | E | Supported | In SIM-R5-C1 iteration 3 (two-area toy), a 'local recurrence without global ignition' state occurred for coupling 0-2.5, and global ignition rose steeply from 0.5% of trials at coupling 2 to 97% at 3: the two signatures are dissociable in the toy, which says nothing about which accompanies experience. | SIM-R5-C1/iter-3#A1;SIM-R5-C1/iter-3#A2 | Carried unchanged. |
| C2-R5-01 | P | Supported | In spontaneous high-density EEG, three complexity measures (Lempel-Ziv, amplitude coalition entropy, synchrony coalition entropy) showed a robustly measurable decrease during propofol-induced general anaesthesia; Kuramoto simulations indicated the measures capture distinct 'flavours' of complexity. | W13 | New in Cycle 2. |
| C2-R5-02 | P | Supported | A review by developers of perturbational complexity argues that complexity-related measures have converged as markers of consciousness across sleep, anaesthesia, hallucinatory states, coma and related disorders, and describes the perturbational complexity index (PCI) as assessing the brain's causal structure by perturbation. | W11 | New in Cycle 2. |
| C2-R5-03 | E | Supported | The adversarial collaboration between global neuronal workspace and integrated information theory preregistered two experiments testing contrasting predictions about the location and timing of correlates of visual consciousness, run by six theory-impartial laboratories with fMRI, M-EEG and iEEG. | W12 | New in Cycle 2. |
| C2-R5-04 | E | Supported | In SIM-R5-C2 (toy Kuramoto network), spontaneous Lempel-Ziv complexity fell as coupling rose (Spearman -0.98) and was highest for uncoupled noisy units, whereas a perturbational (PCI-like) measure was low for them (0.22) and highest at intermediate coupling (0.72): in this toy, spontaneous complexity alone cannot tell noise from integrated-and-differentiated dynamics. | SIM-R5-C2/iter-1#Z1;SIM-R5-C2/iter-1#Z2;SIM-R5-C2/iter-1#Z3;SIM-R5-C2/iter-2#S1;SIM-R5-C2/iter-4#N1 | New in Cycle 2. |
| C2-R5-05 | E | Supported | In SIM-R5-C2, the PCI-like measure peaked at intermediate coupling (2.7x both ends at 40 units), but the peak was not supported as robust (6 of 9 size-seed settings; it failed at 64 units, where the fixed 10-unit perturbation is a smaller share of a module), and removing between-module coupling lowered it mostly but not monotonically (Spearman 0.7; not supported). | SIM-R5-C2/iter-3#P1;SIM-R5-C2/iter-5#D1;SIM-R5-C2/iter-6#R1 | New in Cycle 2. |
| C2-R5-06 | P | Contested | Challenge: in rats under continuous sevoflurane, animals whose wakefulness was not restored nevertheless showed increased cortical (spontaneous EEG) complexity similar to wakefulness, while higher-gamma connectivity stayed reduced even when wakefulness was restored; the authors conclude that the level of consciousness can be dissociated from cortical connectivity, oscillations and complexity. | W15 | New in Cycle 2. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-2 status |
|---|---|---|---|---|
| L07 | R2 Mind → R5 Consciousness | relationship | P | Unchanged; complexity markers are relevant context but do not test this link, and W15 reports a dissociation between consciousness and EEG complexity. |
| L08 | R2 Mind → R5 Consciousness | distinction | P | Downgraded Established -> Plausible by the strict rule (basis C1-R5-02 is Plausible). Procedural. |
| L12 | R3 Soul → R5 Consciousness | competing interpretation | PS | Unchanged in Cycle 2. |
| L17 | R5 Consciousness → R1 Body | dependency | E | Unchanged in Cycle 2. |
| L18 | R5 Consciousness → R4 Spirit | relationship | H | Unchanged in Cycle 2. |

## Limitations
Toy network; results describe measures, not consciousness. The pilot used to set the coupling range is disclosed. Perturbation size was not scaled with network size.

## Open questions and falsification
Does scaling the perturbation with network size restore the peak? Falsification: a PCI-like measure that is high in a network with no integration would undercut the toy's interpretation.

## Conclusion and gate
Report 5 is more cautious about complexity markers than proponent reviews. Gate: **Indeterminate**.

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
- **W11** — Sarasso S, Casali AG, Casarotto S, Rosanova M, Sinigaglia C, Massimini M (2021). Consciousness and complexity: a consilience of evidence. Neuroscience of consciousness 2021:niab023. doi:10.1093/nc/niab023 [full text (Europe PMC PMC10941977)] <https://europepmc.org/article/PMC/PMC10941977>
- **W12** — Melloni L, Mudrik L, Pitts M, Bendtz K, Ferrante O, Gorska U, Hirschhorn R, Khalaf A, Kozma C, Lepauvre A, Liu L, Mazumder D, Richter D, Zhou H, Blumenfeld H, Boly M, Chalmers DJ, Devore S, Fallon F, de Lange FP, Jensen O, Kreiman G, Luo H, Panagiotaropoulos TI, Dehaene S, Koch C, Tononi G (2023). An adversarial collaboration protocol for testing contrasting predictions of global neuronal workspace and integrated information theory. PloS one 18:e0268577. doi:10.1371/journal.pone.0268577 [full text (Europe PMC PMC9916582)] <https://europepmc.org/article/PMC/PMC9916582>
- **W13** — Schartner M, Seth A, Noirhomme Q, Boly M, Bruno MA, Laureys S, Barrett A (2015). Complexity of Multi-Dimensional Spontaneous EEG Decreases during Propofol Induced General Anaesthesia. PloS one 10:e0133532. doi:10.1371/journal.pone.0133532 [full text (Europe PMC PMC4529106)] <https://europepmc.org/article/PMC/PMC4529106>
- **W15** — Pal D, Li D, Dean JG, Brito MA, Liu T, Fryzel AM, Hudetz AG, Mashour GA (2020). Level of Consciousness Is Dissociable from Electroencephalographic Measures of Cortical Connectivity, Slow Oscillations, and Complexity. The Journal of neuroscience : the official journal of the Society for Neuroscience 40:605-618. doi:10.1523/jneurosci.1910-19.2019 [full text (Europe PMC PMC6961988)] <https://europepmc.org/article/PMC/PMC6961988>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6) (2026-10-24): this version; details in `CHANGELOG.md`.
