# Report 5 — Consciousness: awareness, attention and subjective experience

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-3-X9-R5 |
| Version | Cycle 3 (x9) |
| Status | Researched (9 passes), simulated (9 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-2-x6/Report-5-Consciousness/REPORT.md` (Cycle 2), Cycles 0-1 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7) |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 3 carries the item *perturbation scaled with network size*. With the kick scaled to one module (N/4 units), the intermediate-coupling peak of the PCI-like measure became robust (8/9 size–seed settings, 9/9 with new seeds, at N = 96 and 128, and for all binarisation thresholds), so Cycle 2's non-robustness (C2-R5-05) was a design artefact. Other expectations failed: the peak moved with kick size, a synchrony-susceptibility criticality proxy peaked at zero coupling and predicted PCI-like weakly (ρ 0.37), and halving coupling lowered PCI-like by 29% (just short of 30%) — all **not supported**. Literature: criticality predicts PCI across anaesthesia (X12, P), PCI compatible with GNW (X13, P), PCIst in rodents (X14, E), Casali 2013 now in full text (X05, E), the attention-network review now in full text (X03), and three sources filling empty lens cells: loving-kindness meditation fMRI (X23, P), disorders-of-consciousness ethics (X24, P), metacognition (X26, E).

## What changed in Cycle 3
Pass 1 logged two PCI queries and selected X12, X13, X14. Pass 2 read them in full. Pass 3 logged OpenAlex open-access lookups (T10 → X05 full text; U21 → X02 full text; S20 → X06 failed, no HTTP response; T11) and five lens-targeted Europe PMC queries (DoC ethics, metacognition ×2, loving-kindness), selecting X23, X24, X26. Pass 4 (challenge) is carried by the simulations (criticality proxy fails). Pass 5 built the scaled perturbation (iterations 1–4). Pass 6 confirmed the Consciousness×Love/Justice/Wisdom gaps targeted in pass 3. Pass 7 ran robustness (iterations 5–9). Pass 8 consolidated (9 new claims; 3 carried claims annotated, two with full texts). Pass 9: no carried label or status changed; C2-R5-05 reinterpreted (label unchanged).

Ledger: 32 claims (18 E, 11 P, 2 PS, 1 H); 9 new; 4 carried claims annotated with Cycle-3 evidence; no carried claim changed label or status (each row's `c3_change` says which).

## Methods
Nine successive research passes (1 logged search → 2 deepen → 3 widen and open-access full-text upgrades → 4 challenge → 5 carried agenda item (simulation design, iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness and sensitivity (iterations 5–9) → 8 consolidation → 9 diminishing-returns audit; notes in `research/pass-1..9/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and nine chained simulation iterations (`simulation/iter-1..9`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such.

## Competing views and counter-evidence
Complexity may index arousal rather than consciousness (W15, Cycle 2). X12 and X13 are interpretations by proponents. Measures of level do not address phenomenal experience.

## Simulation (9 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code check against Cycle 2. | V1: Pass, V2: Pass | 2/2 | 0/0 |
| 2 | Redo the failed Cycle-2 robustness test (C2-R5-05) with the perturbation scaled to one module. | H2: Supported | 0/0 | 1/1 |
| 3 | Do larger networks keep the peak? | H3: Supported | 0/0 | 1/1 |
| 4 | Sensitivity to perturbation strength. | H4: Not supported | 0/0 | 0/1 |
| 5 | Sensitivity to the response binarisation threshold. | H5: Supported | 0/0 | 1/1 |
| 6 | Criticality link (X12): does the PCI-like peak sit where a criticality proxy peaks? | H6: Not supported | 0/0 | 0/1 |
| 7 | Can spontaneous dynamics predict perturbational complexity (X12's claim, in toy form)? | H7: Not supported | 0/0 | 0/1 |
| 8 | Anaesthesia-like coupling reduction: do spontaneous and perturbational complexity dissociate? | H8: Not supported | 0/0 | 0/1 |
| 9 | Consolidation: replicate iteration 2 with new seeds. | H9: Supported | 0/0 | 1/1 |

Iterations: (1) reproduce Cycle 2 and validate; (2) scaled kick over sizes and seeds; (3) N = 96, 128; (4) kick-size sensitivity; (5) thresholds; (6) criticality proxy; (7) proxy vs PCI-like; (8) disconnection; (9) new seeds.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-3 change |
|---|---|---|---|---|---|
| C0v2-R5-01 | E | Supported | Awareness/subjective experience: consciousness is studied under distinct concepts, including phenomenal ('what it is like') consciousness and access consciousness. | S16 | Carried unchanged. |
| C0v2-R5-02 | E | Supported | Attention: Petersen & Posner's attention-network framework (1990, updated 2012) has been elaborated with orienting and executive networks, developmental changes and genetic contributions to individual differences. | V01;U20;X03 | Petersen & Posner 2012 now read in full text (X03): the three-network framework is confirmed. Source X03 and its phrase added. |
| C0v2-R5-03 | P | Contested | Attention and consciousness are closely related, but whether attention is necessary, sufficient, both or neither for consciousness is controversial. | U22 | Carried unchanged. |
| C0v2-R5-04 | PS | Interpretive | Self-awareness: self-consciousness is awareness of oneself as oneself (expressed by 'I', 'me', 'my'); mirror recognition, episodic memory and metacognition are studied as markers in infants and animals. | U23 | Carried unchanged. |
| C0v2-R5-05 | P | Contested | Perception and the neural correlates: a review locates the anatomical correlates of specific conscious percepts primarily in a posterior cortical 'hot zone' rather than a fronto-parietal network. | T11 | Carried unchanged. |
| C0v2-R5-06 | E | Supported | Altered states: the perturbational complexity index (TMS-evoked EEG compressibility) discriminates level of consciousness; in a validation on 150 benchmark subjects an empirical cutoff separated conscious from unconscious conditions with 100% sensitivity and specificity, then detected 94.7% of minimally conscious patients and flagged 9 of 43 vegetative-state patients with high complexity. | V07;T10 | Casali et al. 2013 now read in full text (X05; C3-R5-04). |
| C0v2-R5-07 | H | Hypothetical | Altered states: the 'entropic brain' hypothesis proposes that psychedelic states show elevated entropy of brain dynamics and that normal waking consciousness operates just below criticality. | U21;X02 | Full text now read (X02): the 'just below criticality' wording is confirmed in the full text; label unchanged (Hypothetical). Source X02 and its phrase added. |
| C0v2-R5-08 | E | Supported | Origin/nature: prominent theories include higher-order, global workspace, re-entry/predictive-processing and integrated-information theories; how they relate and whether they can be empirically distinguished is unclear. | S19 | Carried unchanged. |
| C0v2-R5-09 | P | Contested | Global Neuronal Workspace research proposes late amplification, long-range synchronization and prefronto-parietal 'ignition' as markers of conscious access. | S20;S18 | Carried unchanged. |
| C0v2-R5-10 | E | Supported | A preregistered adversarial test (n = 256; fMRI, MEG, iEEG) found results aligned with some predictions of IIT and GNWT while substantially challenging key tenets of both. | S18 | Carried unchanged. |
| C0v2-R5-11 | E | Supported | In SIM-R5-C0, a recurrent rate unit showed all-or-none sustained activity under strong recurrence (ignition rose from <10% to >90% between input 1.8 and 2.8) and none under weak recurrence; a dynamical toy with no bearing on phenomenal experience. | C0:SIM-R5-C0#E1;C0:SIM-R5-C0#E2;C0:SIM-R5-C0#E3 | Carried unchanged. |
| C0v2-R5-12 | PS | Indeterminate | How consciousness arises and what it ultimately is remain open: no theory has resolved the phenomenal ('hard') aspect; physicalist, dualist and other metaphysical answers persist. | S16;S18;S08 | Carried unchanged. |
| C1-R5-01 | E | Supported | Higher-order theories explain the difference between unconscious and conscious mental states by a relation between the conscious state and a higher-order representation of it (a higher-order perception or thought). | V18 | Carried unchanged. |
| C1-R5-02 | P | Contested | Global workspace and recurrent processing theories disagree on access: some views (e.g. global workspace) hold that attention is necessary for access, which entails phenomenal consciousness, whereas recurrent processing theory holds there can be phenomenal states that are not accessible; many scientists take the evidence to show no phenomenal consciousness without access. | V19 | Carried unchanged. |
| C1-R5-03 | E | Supported | In SIM-R5-C1 iteration 1, the C0 ignition unit was bistable in 42% of a recurrence x threshold grid (77 cells); simulated bistability matched the fixed-point count in every cell, and the C0 weak (w = 2) and strong (w = 8) settings fall on opposite sides. | SIM-R5-C1/iter-1#P1;SIM-R5-C1/iter-1#P2 | Carried unchanged. |
| C1-R5-04 | E | Supported | In SIM-R5-C1 iteration 2 (backward-masking toy), near-threshold late activity of the bistable unit was bimodal (bimodality coefficient 0.94-0.97 in all 20-80% ignition cells) while the weak unit never ignited. | SIM-R5-C1/iter-2#K1;SIM-R5-C1/iter-2#K2;SIM-R5-C1/iter-2#K3 | Carried unchanged. |
| C1-R5-05 | E | Supported | In SIM-R5-C1 iteration 3 (two-area toy), a 'local recurrence without global ignition' state occurred for coupling 0-2.5, and global ignition rose steeply from 0.5% of trials at coupling 2 to 97% at 3: the two signatures are dissociable in the toy, which says nothing about which accompanies experience. | SIM-R5-C1/iter-3#A1;SIM-R5-C1/iter-3#A2 | Carried unchanged. |
| C2-R5-01 | P | Supported | In spontaneous high-density EEG, three complexity measures (Lempel-Ziv, amplitude coalition entropy, synchrony coalition entropy) showed a robustly measurable decrease during propofol-induced general anaesthesia; Kuramoto simulations indicated the measures capture distinct 'flavours' of complexity. | W13 | Carried unchanged. |
| C2-R5-02 | P | Supported | A review by developers of perturbational complexity argues that complexity-related measures have converged as markers of consciousness across sleep, anaesthesia, hallucinatory states, coma and related disorders, and describes the perturbational complexity index (PCI) as assessing the brain's causal structure by perturbation. | W11 | Carried unchanged. |
| C2-R5-03 | E | Supported | The adversarial collaboration between global neuronal workspace and integrated information theory preregistered two experiments testing contrasting predictions about the location and timing of correlates of visual consciousness, run by six theory-impartial laboratories with fMRI, M-EEG and iEEG. | W12 | Carried unchanged. |
| C2-R5-04 | E | Supported | In SIM-R5-C2 (toy Kuramoto network), spontaneous Lempel-Ziv complexity fell as coupling rose (Spearman -0.98) and was highest for uncoupled noisy units, whereas a perturbational (PCI-like) measure was low for them (0.22) and highest at intermediate coupling (0.72): in this toy, spontaneous complexity alone cannot tell noise from integrated-and-differentiated dynamics. | SIM-R5-C2/iter-1#Z1;SIM-R5-C2/iter-1#Z2;SIM-R5-C2/iter-1#Z3;SIM-R5-C2/iter-2#S1;SIM-R5-C2/iter-4#N1 | Carried unchanged. |
| C2-R5-05 | E | Supported | In SIM-R5-C2, the PCI-like measure peaked at intermediate coupling (2.7x both ends at 40 units), but the peak was not supported as robust (6 of 9 size-seed settings; it failed at 64 units, where the fixed 10-unit perturbation is a smaller share of a module), and removing between-module coupling lowered it mostly but not monotonically (Spearman 0.7; not supported). | SIM-R5-C2/iter-3#P1;SIM-R5-C2/iter-5#D1;SIM-R5-C2/iter-6#R1 | Reinterpreted in Cycle 3 (label and status unchanged): with a perturbation scaled to network size the peak is robust (C3-R5-05), so the Cycle-2 non-robustness was a design artefact. |
| C2-R5-06 | P | Contested | Challenge: in rats under continuous sevoflurane, animals whose wakefulness was not restored nevertheless showed increased cortical (spontaneous EEG) complexity similar to wakefulness, while higher-gamma connectivity stayed reduced even when wakefulness was restored; the authors conclude that the level of consciousness can be dissociated from cortical connectivity, oscillations and complexity. | W15 | Carried unchanged. |
| C3-R5-01 | P | Supported | Maschke et al. (2024) report that dynamical properties of resting-state EEG associated with criticality predicted individual subjects' PCI values with considerably high accuracy across anaesthetic-induced loss of consciousness, and interpret this as a firm link between perturbational complexity and criticality. | X12 | New in Cycle 3. |
| C3-R5-02 | P | Supported | Farisco & Changeux (2023) argue that although PCI was introduced within integrated information theory, it is fundamentally compatible with the global neuronal workspace theory, with some partial disagreements. | X13 | New in Cycle 3. |
| C3-R5-03 | E | Supported | A perturbational complexity measure (PCIst) validated in freely moving rats and mice was higher in wake than in NREM sleep and almost always higher in REM than in NREM sleep. | X14 | New in Cycle 3. |
| C3-R5-04 | E | Supported | In Casali et al. (2013), now read in full text (previously abstract only, T10), PCI values ranged from 0.44 to 0.67 in 32 awake healthy people but fell to 0.18-0.28 during NREM sleep. | X05;T10 | New in Cycle 3. |
| C3-R5-05 | E | Supported | In SIM-R5-C3, scaling the perturbation with network size (one module, N/4 units) made the intermediate-coupling peak of the PCI-like measure robust: 8 of 9 size-seed settings (including N = 64, where Cycle 2 failed), 9 of 9 with new seeds, at N = 96 and 128, and for all four binarisation thresholds. The Cycle-2 non-robustness (C2-R5-05) was a design artefact of the fixed 10-unit kick. | SIM-R5-C3/iter-1#V1;SIM-R5-C3/iter-1#V2;SIM-R5-C3/iter-2#H2;SIM-R5-C3/iter-3#H3;SIM-R5-C3/iter-5#H5;SIM-R5-C3/iter-9#H9 | New in Cycle 3. |
| C3-R5-06 | E | Supported | In SIM-R5-C3, the peak location was not stable across kick sizes (at kick 0.5 it moved to the strongest coupling; not supported); a synchrony-susceptibility criticality proxy peaked at zero coupling rather than at the PCI-like peak and predicted PCI-like only weakly (Spearman 0.37), so the toy did not reproduce X12's criticality link (both not supported); halving coupling lowered PCI-like by 29% while spontaneous LZ rose (0.41 to 0.56), just short of the pre-registered 30%. | SIM-R5-C3/iter-4#H4;SIM-R5-C3/iter-6#H6;SIM-R5-C3/iter-7#H7;SIM-R5-C3/iter-8#H8 | New in Cycle 3. |
| C3-R5-07 | P | Supported | In an fMRI study, expert and novice meditators generating a loving-kindness-compassion state showed greater insula and cingulate activation to emotional sounds during meditation than rest, more so in experts for negative sounds; the authors interpret this as support for limbic circuitry in emotion sharing. | X23 | New in Cycle 3. |
| C3-R5-08 | P | Supported | An ethics commentary on the 2018 disorders-of-consciousness practice guideline argues that implementing it raises ethical challenges in weighing benefits, harms, feasibility and cost, and that cost considerations are fundamentally questions of distributive justice. | X24 | New in Cycle 3. |
| C3-R5-09 | E | Supported | A review of metacognition describes it as reflective monitoring and control processes, with confidence judgements about one's own decisions as the standard second-order measure. | X26 | New in Cycle 3. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-3 status |
|---|---|---|---|---|
| L07 | R2 Mind → R5 Consciousness | relationship | P | Unchanged. |
| L08 | R2 Mind → R5 Consciousness | distinction | P | No Cycle-3 evidence targeted this link. |
| L12 | R3 Soul → R5 Consciousness | competing interpretation | PS | Unchanged (Philosophical/Spiritual): reports of leaving the body describe experiences, not their cause. |
| L17 | R5 Consciousness → R1 Body | dependency | E | Strengthened: full text of the original PCI paper and a rodent validation. |
| L18 | R5 Consciousness → R4 Spirit | relationship | H | Unchanged (Hypothetical); criticality-PCI link reported empirically for anaesthesia (X12), not for spiritual states. |
| L27 | R3 Soul → R5 Consciousness | competing interpretation | PS | New in Cycle 3. |

## Limitations
Toy network; measures, not consciousness. Proxy choice is ours.

## Open questions and falsification
Would a better criticality measure (e.g. avalanche statistics) track the PCI-like peak? Falsification: a high PCI-like value in a network with no integration would undercut the interpretation.

## Conclusion and gate
Report 5 corrected a Cycle-2 artefact and widened to the lens gaps. Gate: **Indeterminate**.

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
- **X02** — Carhart-Harris RL, Leech R, Hellyer PJ, Shanahan M, Feilding A, Tagliazucchi E, Chialvo DR, Nutt D (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. Frontiers in human neuroscience 8:20. doi:10.3389/fnhum.2014.00020 [full text (Europe PMC PMC3909994)] <https://europepmc.org/article/PMC/PMC3909994>
- **X03** — Petersen SE, Posner MI (2012). The attention system of the human brain: 20 years after. Annual review of neuroscience 35:73-89. doi:10.1146/annurev-neuro-062111-150525 [full text (PMC OAI-PMH PMC3413263)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3413263/>
- **X05** — Casali AG, Gosseries O, Rosanova M, Boly M, Sarasso S, Casali KR, Casarotto S, Bruno MA, Laureys S, Tononi G, Massimini M (2013). A theoretically based index of consciousness independent of sensory processing and behavior. Science translational medicine 5:198ra105. doi:10.1126/scitranslmed.3006294 [full text (submitted version PDF, ORBi repository via OpenAlex)] <https://orbi.uliege.be/bitstream/2268/171542/1/A%20theoretically%20based%20index%20of%20consciousness%20independent%20of%20sensory%20processing%20and%20behavior.pdf>
- **X12** — Maschke C, O'Byrne J, Colombo MA, Boly M, Gosseries O, Laureys S, Rosanova M, Jerbi K, Blain-Moraes S (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. Communications biology 7:946. doi:10.1038/s42003-024-06613-8 [full text (Europe PMC PMC11300875)] <https://europepmc.org/article/PMC/PMC11300875>
- **X13** — Farisco M, Changeux JP (2023). About the compatibility between the perturbational complexity index and the global neuronal workspace theory of consciousness. Neuroscience of consciousness 2023:niad016. doi:10.1093/nc/niad016 [full text (Europe PMC PMC10279414)] <https://europepmc.org/article/PMC/PMC10279414>
- **X14** — Cavelli ML, Mao R, Findlay G, Driessen K, Bugnon T, Tononi G, Cirelli C (2023). Sleep/wake changes in perturbational complexity in rats and mice. iScience 26:106186. doi:10.1016/j.isci.2023.106186 [full text (Europe PMC PMC9988678)] <https://europepmc.org/article/PMC/PMC9988678>
- **X23** — Lutz A, Brefczynski-Lewis J, Johnstone T, Davidson RJ (2008). Regulation of the neural circuitry of emotion by compassion meditation: effects of meditative expertise. PloS one 3:e1897. doi:10.1371/journal.pone.0001897 [full text (Europe PMC PMC2267490)] <https://europepmc.org/article/PMC/PMC2267490>
- **X24** — Peterson A, Young MJ, Fins JJ (2022). Ethics and the 2018 Practice Guideline on Disorders of Consciousness: A Framework for Responsible Implementation. Neurology 98:712-718. doi:10.1212/wnl.0000000000200301 [full text (Europe PMC PMC9071367)] <https://europepmc.org/article/PMC/PMC9071367>
- **X26** — Fleming SM, Dolan RJ, Frith CD (2012). Metacognition: computation, biology and function. Philosophical transactions of the Royal Society of London. Series B, Biological sciences 367:1280-1286. doi:10.1098/rstb.2012.0021 [full text (Europe PMC PMC3318771)] <https://europepmc.org/article/PMC/PMC3318771>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9) (2026-10-24): this version; details in `CHANGELOG.md`.
