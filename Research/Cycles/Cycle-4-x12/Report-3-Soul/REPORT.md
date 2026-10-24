# Report 3 — The Soul: conceptions across traditions

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-4-X12-R3 |
| Version | Cycle 4 (x12) |
| Status | Researched (12 passes), simulated (12 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-3-x9/Report-3-Soul/REPORT.md` (Cycle 3), Cycles 0-2 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7); Cycle-4: Report 7's own new claims excluded from its simulation inputs |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
An independent human coder remains impossible for this agent (disclosed; the Cycle-2 blank coding form is still available for a person to complete). Cycle 4 therefore tests a narrower question: is the Cycle-1 four-cluster soul-conception typology at least a stable feature of the single coding it came from? SIM-R3-C4 (12 iterations) says **no**: attribute bootstrap mean ARI 0.44 (replicated), flipping uncertain cells 0.34, single linkage 0.26, no stable cores; it survives dropping any one conception (0.99) and alternative distances. Cluster structure is weak (silhouette ≤ 0.28, only just above a permutation null). This concerns descriptions of doctrines only; it says nothing about whether a soul exists. A logged cross-cultural soul/afterlife search returned nothing relevant.

## What changed in Cycle 4
Pass 1 logged one cross-cultural query (top hits irrelevant) — added nothing. Passes 2, 3, 4, 6, 9 added nothing (no new source; no human coder available). Passes 5, 7, 8 ran iterations 1–4, 5–8, 9–12. Pass 10: 2 new claims; C1-R3-05, C2-R3-03, C3-R3-03 annotated (C1-R3-05 stays Indeterminate). Pass 11: links unchanged. Pass 12: no carried label or status changed.

Ledger: 33 claims (25 E, 2 P, 6 PS, 0 H); 2 new; 3 carried claims annotated with Cycle-4 evidence; no carried claim changed label or status (each row's `c4_change` says which).

## Methods
Twelve successive research passes (1 logged search → 2 deepen → 3 DOI/open-access lookups → 4 challenge → 5 carried agenda item (iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness (iterations 5–8) → 8 extension and challenge (iterations 9–12) → 9 retry of blocked items → 10 consolidation → 11 links → 12 diminishing-returns audit; notes in `research/pass-1..12/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and twelve chained simulation iterations (`simulation/iter-1..12`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such, not padded.

## Competing views and counter-evidence
Typologies of soul conceptions are a scholarly convenience; traditions resist neat partition. Weak cluster structure is consistent with a continuum of conceptions rather than four kinds.

## Simulation (12 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code check; counts of uncertain cells and cluster sizes. | V1: Pass, V2: Pass, C0: Reported | 2/2 | 0/0 |
| 2 | Attribute bootstrap. | H2: Not supported | 0/0 | 0/1 |
| 3 | Jackknife over conceptions. | H3: Supported | 0/0 | 1/1 |
| 4 | Was k = 4 a good choice? | H4: Supported | 0/0 | 1/1 |
| 5 | Linkage sensitivity. | H5: Not supported | 0/0 | 0/1 |
| 6 | Do coder A's uncertain cells drive the partition? | H6: Not supported | 0/0 | 0/1 |
| 7 | Distance sensitivity. | H7: Supported | 0/0 | 1/1 |
| 8 | Which conceptions form stable cores? | H8: Not supported | 0/0 | 0/1 |
| 9 | Is there more structure than chance? | H9: Supported | 0/0 | 1/1 |
| 10 | Coder C's partition and its stability (reporting only). | H10r: Reported | 0/0 | 0/0 |
| 11 | Replication of iteration 2. | H11: Supported | 0/0 | 1/1 |
| 12 | Consolidation. | H12: Not supported | 0/0 | 0/1 |

Stability is not reliability: all codings (A, B, coder C) are by the same research agent.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-4 change |
|---|---|---|---|---|---|
| C0v2-R3-01 | E | Supported | Greek (descriptive): ancient Greek theories of soul (psuchê) differ widely — Plato, Aristotle, Epicurus and the Stoics give the main accounts — and for some thinkers the ensouled includes plants. | S07 | Carried unchanged. |
| C0v2-R3-02 | E | Supported | Greek (descriptive): Aristotle defines soul as the first actuality of a natural body having life potentially — soul as form of the living body. | T05 | Carried unchanged. |
| C0v2-R3-03 | E | Supported | Greek (descriptive): Epicurus held the soul to be atomic and dispersed at death; the Stoics treated soul as pneuma, a breath-like material compound, with the commanding faculty located at the heart. | S07 | Carried unchanged. |
| C0v2-R3-04 | E | Supported | Hebrew Bible (descriptive): Genesis 2:7 says God formed the human from the soil and blew into his nostrils the breath of life, and the human became a 'living being' (Hebrew nefesh ḥayyah). | T07e;T07 | Carried unchanged. |
| C0v2-R3-05 | E | Supported | Christian (descriptive): Aquinas defines the soul as the first principle of life and argues that the intellectual principle is incorporeal and subsistent. | U40 | Carried unchanged. |
| C0v2-R3-06 | E | Supported | Islamic (descriptive): Qur'an 17:85 (Saheeh International) answers a question about the rūḥ: 'The soul is of the affair of my Lord. And mankind have not been given of knowledge except a little'; 15:29 speaks of God breathing into the human of His [created] soul. | U41;U50 | Carried unchanged. |
| C0v2-R3-07 | E | Supported | Islamic philosophy (descriptive): Avicenna's 'floating man' thought experiment and Averroes' doctrine of the unity of the intellect are notable contributions in the dualist tradition. | S08 | Carried unchanged. |
| C0v2-R3-08 | E | Supported | Hindu (descriptive): Bhagavad Gita 2.20 (Prabhupada translation) says the soul is unborn and eternal and is not slain when the body is slain; Advaita Vedānta identifies the individual self (ātman) with Brahman. | U43;S31 | Carried unchanged. |
| C0v2-R3-09 | E | Supported | Buddhist (descriptive): Indian Buddhist philosophy counts the lack of an abiding self (anātman) among the three marks of existence. | S32 | Carried unchanged. |
| C0v2-R3-10 | E | Supported | Chinese (descriptive): early Chinese texts speak of hun and po souls and of qi; xin ('heart-mind') originated as a picture of the heart and is credited with thinking, understanding and feeling. | T17 | Carried unchanged. |
| C0v2-R3-11 | E | Supported | African (descriptive): in African ethics as presented by Gyekye, character and moral personhood are central and morality is social rather than individualistic. | U44 | Carried unchanged. |
| C0v2-R3-12 | E | Supported | Indigenous (descriptive): animist traditions common to many Indigenous cultures treat features of the environment (trees, rivers, animals) as non-human persons and relatives; social-relational readings do not require a doctrine of interior souls. | U45 | Carried unchanged. |
| C0v2-R3-13 | PS | Contested | Identity: whether the person is a soul, an organism, or a psychologically continuous subject is contested (psychological-continuity views vs animalism vs soul views). | U13;S08 | Carried unchanged. |
| C0v2-R3-14 | E | Supported | Moral character: virtue ethics, one of three major approaches in normative ethics, emphasizes the virtues or moral character (vs duties or consequences). | T16 | Carried unchanged. |
| C0v2-R3-15 | PS | Contested | Purpose: accounts of life's meaning divide into supernaturalist (God- or soul-centred), naturalist and nihilist views; none is established. | U46 | Carried unchanged. |
| C0v2-R3-16 | PS | Contested | Independence from body: substance dualism, hylomorphic dualism and physicalism compete; dualism faces the interaction problem and causal-closure objections. | S08;T06 | Carried unchanged. |
| C0v2-R3-17 | PS | Indeterminate | In SIM-R3-C0 (14 conceptions × 12 attributes, single coder, 36 flagged-uncertain cells), the base 4-cluster partition recurred in only 0.13% of 20,000 perturbations (coding-sensitive); 17 pairs co-clustered in ≥80% of draws (e.g. Plato–Aquinas 0.99, Gita–Advaita 0.93); no attribute was shared by all 14 (max 9/14). | C0:SIM-R3-C0#E1;C0:SIM-R3-C0#E2;C0:SIM-R3-C0#E3 | Carried unchanged. |
| C0v2-R3-18 | PS | Indeterminate | No finding in this pass establishes the existence, nonexistence or ultimate nature of a soul; the framework's boundary is respected. | S08;G03 | Carried unchanged. |
| C1-R3-01 | E | Supported | Jain (descriptive): at the heart of Jainism is the belief that each living being is the transitory embodiment of a permanent divine-like self (jīva) which is unobstructed consciousness; karma is conceived as a subtle type of matter that sticks to the self and obstructs it; living beings range from one-sensed beings such as plants to five-sensed beings. | V40 | Carried unchanged. |
| C1-R3-02 | E | Supported | Death (descriptive): the SEP entry identifies Epicurus as having made perhaps the most influential case against the harm thesis (that death can harm the one who dies), and discusses the deprivationist defence as a contemporary response. | V41 | Carried unchanged. |
| C1-R3-03 | E | Supported | In SIM-R3-C1 iteration 1, the Cycle-0 soul typology was not supported as coding-robust: across 15 coding x metric variants (uncertain cells as coded / 0 / 1 / 0.5 / dropped; Jaccard, Hamming, Dice), median agreement with the base partition was ARI 0.57 and only 2 variants reproduced it. | SIM-R3-C1/iter-1#C1;SIM-R3-C1/iter-1#C2;SIM-R3-C1/iter-1#E1 | Carried unchanged. |
| C1-R3-04 | E | Supported | In SIM-R3-C1 iteration 2, alternative clustering methods at k = 4 were not supported as agreeing with the base (median ARI 0.77; single linkage 0.25), and the best silhouette was 0.27 (weighted linkage, k = 4), indicating weak cluster structure. | SIM-R3-C1/iter-2#M1;SIM-R3-C1/iter-2#M2 | Carried unchanged. |
| C1-R3-05 | PS | Indeterminate | In SIM-R3-C1 iteration 3 (15 conceptions incl. Jain jīva; 2,000 draws over codings x metrics x linkages x k), the base partition never recurred, but 7 pairs co-clustered in >= 80% of draws: Hebrew Bible–Qur'an 0.92, Aristotle–Aquinas 0.88, Plato–Jain 0.86, Gita–Advaita 0.85, Epicurus–early Chinese 0.83, Plato–Aquinas 0.83, Aristotle–Stoics 0.82; no attribute was shared by all 15 (max 10/15). | SIM-R3-C1/iter-3#K1;SIM-R3-C1/iter-3#K2;SIM-R3-C1/iter-3#K3;SIM-R3-C1/iter-3#E3 | Remains Indeterminate; Cycle 4 shows the partition is not stable even within coding A (attribute bootstrap ARI 0.44; C4-R3-01). |
| C2-R3-01 | E | Supported | In SIM-R3-C2, a codebook re-coding of a seeded random sample of 48 of the 180 Cycle-1 soul-typology cells agreed with the Cycle-1 coding in 90% of cells (Cohen's kappa 0.79, bootstrap 95% CI 0.58-0.96; Krippendorff's alpha 0.79), with no directional bias (bias index 0.02, so the 'directional disagreement' hypothesis was not supported). Both codings were made by the same research agent, so this is re-coding reliability, not inter-rater reliability. | SIM-R3-C2/iter-1#K0;SIM-R3-C2/iter-1#K00;SIM-R3-C2/iter-1#H1;SIM-R3-C2/iter-1#H1r;SIM-R3-C2/iter-2#H2;SIM-R3-C2/iter-2#H2r;SIM-R3-C2/iter-4#H4;SIM-R3-C2/iter-4#H4r | Carried unchanged. |
| C2-R3-02 | E | Supported | In the Cycle-2 re-coding, 27 of 48 sampled cells (56%) could not be decided from an explicit passage of the cited source (source silent or inference needed); agreement was kappa 0.86 where an explicit passage existed versus 0.42 where it did not. | SIM-R3-C2/iter-3#H3;SIM-R3-C2/iter-3#H3r | Carried unchanged. |
| C2-R3-03 | E | Supported | In SIM-R3-C2 iterations 5-6, substituting the re-coded values left the Cycle-1 partition unchanged (ARI 1.0), but the typology tolerated only about 4 random cell flips before its median ARI fell below 0.8, while the observed disagreement rate extrapolates to about 19 disagreements over all 180 cells: the hypothesis that the typology is robust to coding disagreement was not supported. | SIM-R3-C2/iter-5#H5;SIM-R3-C2/iter-5#H5r;SIM-R3-C2/iter-6#H6 | Consistent with Cycle 4: flipping uncertain cells gives mean ARI 0.34 (C4-R3-01). |
| C2-R3-04 | P | Contested | McHugh reports Cohen's interpretation of kappa (0.41-0.60 moderate, 0.61-0.80 substantial, 0.81-1.00 almost perfect) and argues it may be too lenient for health research because it implies that a score as low as 0.41 might be acceptable. | W07 | Carried unchanged. |
| C2-R3-05 | E | Supported | A simulation and case study of reliability coefficients for nominal data recommends Fleiss' K with a bootstrap confidence interval for complete nominal data, advises against the asymptotic interval for Fleiss' K, and recommends Krippendorff's alpha when data are missing or higher than nominal. | W08 | Carried unchanged. |
| C3-R3-01 | P | Supported | A systematic analysis of near-death-experience case reports and qualitative studies found the most frequent reported experiences were 'supernatural' ones, especially leaving the body, and that the basis and content of reported patterns were similar across reports. | X19 | Carried unchanged. |
| C3-R3-02 | E | Supported | In SIM-R3-C3, a third, mechanical lexicon coder (coder C; same agent, different method) agreed with the Cycle-1 soul coding only fairly (kappa 0.32, 70% agreement, 180 cells) and poorly with the Cycle-2 codebook coding (kappa 0.13); three-coder Fleiss kappa was 0.34 against 0.79 for A and B alone (all three 'moderate agreement' hypotheses not supported), though A-C agreement exceeded a within-attribute permutation null (95th percentile 0.19). | SIM-R3-C3/iter-1#V1;SIM-R3-C3/iter-1#V2;SIM-R3-C3/iter-1#C0;SIM-R3-C3/iter-2#H2;SIM-R3-C3/iter-3#H3;SIM-R3-C3/iter-4#H4;SIM-R3-C3/iter-9#H9 | Carried unchanged. |
| C3-R3-03 | E | Supported | In SIM-R3-C3, the Cycle-1 four-cluster typology was not recovered from coder C's coding (ARI 0.36; not supported); 7 of 12 attributes reached kappa >= 0.2, the result was robust to window size (kappa 0.32-0.36), and coder C agreed with B more on cells B had marked uncertain than on certain ones (0.74 vs 0.43; the opposite of the pre-registered expectation). | SIM-R3-C3/iter-5#H5;SIM-R3-C3/iter-6#H6;SIM-R3-C3/iter-7#H7;SIM-R3-C3/iter-8#H8 | Consistent with Cycle 4 (C4-R3-01, C4-R3-02). |
| C4-R3-01 | E | Supported | In SIM-R3-C4, the Cycle-1 four-cluster soul-conception typology was NOT a stable feature even of the single coding it came from: resampling the 12 attributes gave mean ARI 0.44 (replicated 0.44; not supported), flipping the 39 cells the coder marked uncertain gave 0.34 (not supported), single linkage gave 0.26 (not supported), and no cluster had a stable core co-clustering in >= 80% of bootstraps (not supported); it was stable to dropping any one conception (mean ARI 0.99) and to Hamming/Dice distances. | SIM-R3-C4/iter-1#V1;SIM-R3-C4/iter-1#V2;SIM-R3-C4/iter-2#H2;SIM-R3-C4/iter-3#H3;SIM-R3-C4/iter-5#H5;SIM-R3-C4/iter-6#H6;SIM-R3-C4/iter-7#H7;SIM-R3-C4/iter-8#H8;SIM-R3-C4/iter-11#H11;SIM-R3-C4/iter-12#H12 | New in Cycle 4. |
| C4-R3-02 | E | Supported | In SIM-R3-C4, the soul-conception coding has only weak cluster structure: mean silhouette 0.21-0.28 for k = 2-7 (k = 4 highest, 0.28) and only just above a within-attribute permutation null (0.280 vs 95th percentile 0.255); coder C's own partition matched coding A at ARI 0.36 and was itself unstable (bootstrap ARI 0.41). | SIM-R3-C4/iter-4#H4;SIM-R3-C4/iter-9#H9;SIM-R3-C4/iter-10#H10r | New in Cycle 4. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-4 status |
|---|---|---|---|---|
| L09 | R2 Mind → R3 Soul | competing interpretation | PS | No Cycle-4 evidence targeted this link. |
| L10 | R3 Soul → R4 Spirit | relationship | E | No Cycle-4 evidence targeted this link. |
| L11 | R3 Soul → R4 Spirit | distinction | PS | No Cycle-4 evidence targeted this link. |
| L12 | R3 Soul → R5 Consciousness | competing interpretation | PS | No Cycle-4 evidence targeted this link. |
| L13 | R3 Soul → R6 Earth | relationship | E | No Cycle-4 evidence targeted this link. |
| L23 | R6 Earth → R3 Soul | competing interpretation | PS | No Cycle-4 evidence targeted this link. |
| L27 | R3 Soul → R5 Consciousness | competing interpretation | PS | No Cycle-4 evidence targeted this link. |

## Limitations
15 conceptions; single coder; uncertain cells (39) strongly affect the partition.

## Open questions and falsification
Would an independent human coder, using the Cycle-2 codebook, produce a partition with ARI ≥ 0.5 against coding A? Rejection of the typology: ARI < 0.5 again.

## Conclusion and gate
The typology should not be relied on; the descriptive claims about individual traditions are unaffected (they rest on sources, not on the clustering). **Gate: Indeterminate** (internal checks pass; no independent review; Indeterminate is never Pass).

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S07** — Lorenz H. Ancient Theories of Soul. Stanford Encyclopedia of Philosophy (rev. 2024). [full text] <https://plato.stanford.edu/entries/ancient-soul/>
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). [full text] <https://plato.stanford.edu/entries/dualism/>
- **S31** — Vedanta, Advaita. Internet Encyclopedia of Philosophy (author not captured in snapshot). [full text] <https://iep.utm.edu/advaita-vedanta/>
- **S32** — Coseru C. Mind in Indian Buddhist Philosophy. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/mind-indian-buddhism/>
- **T05** — Aristotle. On the Soul (De Anima), Book II, trans. J. A. Smith. MIT Internet Classics Archive. [full text] <https://classics.mit.edu/Aristotle/soul.2.ii.html>
- **T06** — Stoljar D. Physicalism. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/physicalism/>
- **T07** — Genesis 2:7, Hebrew text (Miqra according to the Masorah), via Sefaria API v3. [full text (API)] <https://www.sefaria.org/Genesis.2.7>
- **T07e** — Genesis 2:7, The JPS TANAKH: Gender-Sensitive Edition, via Sefaria API v3. [full text (API)] <https://www.sefaria.org/Genesis.2.7>
- **T16** — Hursthouse R, Pettigrove G. Virtue Ethics. Stanford Encyclopedia of Philosophy (rev. 2026). [full text] <https://plato.stanford.edu/entries/ethics-virtue/>
- **T17** — Wong D. Chinese Philosophy of Mind (xin). Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/chinese-mind/>
- **U13** — Olson ET. Personal Identity. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/identity-personal/>
- **U40** — Thomas Aquinas. Summa Theologiae I, q.75 (trans. Fathers of the English Dominican Province), New Advent. [full text] <https://www.newadvent.org/summa/1075.htm>
- **U41** — Qur'an 17:85, Saheeh International translation, via AlQuran Cloud API. [full text (API)] <https://quran.com/17/85>
- **U43** — Bhagavad-gita As It Is 2.20 (A.C. Bhaktivedanta Swami Prabhupada), Vedabase. [full text] <https://vedabase.io/en/library/bg/2/20/>
- **U44** — Gyekye K. African Ethics. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/african-ethics/>
- **U45** — Smith T. Animism. Internet Encyclopedia of Philosophy. [full text] <https://iep.utm.edu/animism/>
- **U46** — Metz T. The Meaning of Life. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/life-meaning/>
- **U50** — Qur'an 15:29, Saheeh International translation, via AlQuran Cloud API. [full text (API)] <https://quran.com/15/29>
- **V40** — Stanford Encyclopedia of Philosophy, entry 'Jaina Philosophy' [full text (SEP web page)] <https://plato.stanford.edu/entries/jaina-philosophy/>
- **V41** — Stanford Encyclopedia of Philosophy, entry 'Death' [full text (SEP web page)] <https://plato.stanford.edu/entries/death/>
- **W07** — McHugh ML (2012). Interrater reliability: the kappa statistic. Biochemia medica 22:276-282 [full text (Europe PMC PMC3900052)] <https://europepmc.org/article/PMC/PMC3900052>
- **W08** — Zapf A, Castell S, Morawietz L, Karch A (2016). Measuring inter-rater reliability for nominal data - which coefficients and confidence intervals are appropriate?. BMC medical research methodology 16:93. doi:10.1186/s12874-016-0200-9 [full text (Europe PMC PMC4974794)] <https://europepmc.org/article/PMC/PMC4974794>
- **X19** — Hashemi A, Oroojan AA, Rassouli M, Ashrafizadeh H (2023). Explanation of near-death experiences: a systematic analysis of case reports and qualitative research. Frontiers in psychology 14:1048929. doi:10.3389/fpsyg.2023.1048929 [full text (Europe PMC PMC10158795)] <https://europepmc.org/article/PMC/PMC10158795>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9): `../../Cycle-3-x9/`.
- Cycle 4 (x12) (2026-10-24): this version; details in `CHANGELOG.md`.
