# Report 4 — The Spirit: spirituality, religion and health

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-2-X6-R4 |
| Version | Cycle 2 (x6) |
| Status | Researched (6 passes), simulated (6 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-1-x3/Report-4-Spirit/REPORT.md` (Cycle 1) and `../../Cycle-0-Baseline/` |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule (Report 7) |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 2 carries the Cycle-1 agenda item *mediation designs*. From the Nurses' Health Study (S12, full text), proportions of the attendance–mortality association mediated were about 11% (depressive symptoms), 22% (smoking), 9% (optimism) and 23% (social integration), each analysed separately and under no-unmeasured-confounding assumptions. Methods sources (W09, W10, full text) show that with several ordered mediators there are many decompositions and that intermediate confounding needs a sensitivity parameter. Six iterations on synthetic data quantify the traps: summing single-mediator proportions overstates the joint proportion when one mediator causes another (0.74 vs 0.49, replicated 0.73 vs 0.48, **supported**); moderate unmeasured mediator–outcome confounding biased the proportion by 18–19% and cut 95% CI coverage from 0.96 to 0.67 — real but below the pre-registered bars, so those hypotheses were **not supported**; and the odds-ratio method departed from the risk-difference proportion more for *rare* outcomes than for common ones, the opposite of our expectation (**not supported**).

## What changed in Cycle 2
Pass 1 ran logged searches (attendance and mortality; VanderWeele mediation). Pass 2 re-read S12 for mediation results. Pass 3 widened to multiple-mediator methods (W09). Pass 4 (challenge) searched for unmeasured confounding in mediation (W10) and for mediation studies of religion and health (title-restricted retry; no further source selected). Pass 5 executed the mediation simulations. Pass 6 filled empty limits fields and re-assessed labels (none changed). Causation remains Hypothetical.

Ledger: 30 claims (21 E, 5 P, 3 PS, 1 H); 6 new; 6 carried claims had their empty limits field filled; 3 carried claims annotated with Cycle-2 evidence; no carried claim changed label or status (each row's `c2_change` says which).

## Methods
Six successive research passes (1 logged systematic search → 2 deepen → 3 widen → 4 challenge → 5 carried agenda item → 6 consolidation; notes in `research/pass-1..6/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and six chained simulation iterations (`simulation/iter-1..6`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
- **Mediation in S12 (E; C2-R4-01).** Separate analyses; not additive.
- **Methods (E; W09, W10).**
- **Summing proportions misleads (E, simulation; C2-R4-04).**
- **Confounding bias and coverage (E, simulation; C2-R4-05)** — both hypotheses not supported at the pre-registered bars.
- **Scale dependence (E, simulation; C2-R4-06)** — direction opposite to expectation; not supported.

## Competing views and counter-evidence
Observational associations of attendance with lower mortality (Cycle 1) remain open to residual confounding (E-values ~2; bias analysis prior-dependent). Mediation estimates do not establish mechanism; they inherit the same assumptions.

## Simulation (6 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Carried agenda (C1 R4: mediation designs). Baseline: under the no-unmeasured-confounding assumption S12 states, the product-of-coefficients method recovers the indirect effect and proportion mediated (PM). | V1: Pass, V1b: Pass | 2/2 | 0/0 |
| 2 | Violate the mediator-outcome no-confounding assumption with an unmeasured U and measure the bias in PM. | V2: Pass, H1: Not supported | 1/1 | 0/1 |
| 3 | W09: with causally ordered mediators there are many decompositions. Does summing separately estimated single-mediator PMs (as a reader might do with S12 Table 4) overstate the joint PM? | V3: Pass, V3b: Pass, H2: Supported | 2/2 | 1/1 |
| 4 | Scale dependence: S12 computed PM on the risk-difference scale. How far does a PM from the odds-ratio difference method depart when the outcome is common vs rare? | H3: Not supported, H3b: Not supported | 0/0 | 0/2 |
| 5 | Inference: at a realistic sample size, does the usual (Sobel) 95% CI keep its coverage, and how much does moderate unmeasured M-Y confounding destroy it? | V4: Pass, H4: Not supported | 1/1 | 0/1 |
| 6 | Consolidation: replicate iterations 2 and 3 with a new seed. | V2: Pass, H1: Not supported, V3: Pass, V3b: Pass, H2: Supported | 3/3 | 1/2 |

Iterations: (1) baseline recovery under no confounding; (2) unmeasured M–Y confounding; (3) ordered mediators and summed proportions; (4) scale dependence (risk difference vs odds ratio); (5) CI coverage under confounding; (6) replication of 2 and 3 with a new seed (same conclusions).

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-2 change |
|---|---|---|---|---|---|
| C0v2-R4-01 | E | Supported | Vitality (Greek, descriptive): Stoic pneuma ('breath') comes in grades — the lowest gives cohesion to inanimate bodies, higher ones account for nature (growth) and soul. | S07 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R4-02 | E | Supported | Vitality (Hebrew Bible, descriptive): Genesis 1:2 rûaḥ is rendered 'a wind from God' in the JPS translation, which notes that others render it 'the spirit of [God]' — the word spans wind, breath and spirit. | U47 | Carried unchanged. |
| C0v2-R4-03 | E | Supported | Connection/vitality (Christian, descriptive): John 3:8 (WEB) likens being 'born of the Spirit' to the wind that blows where it wants; inspiration: 2 Timothy 3:16 calls Scripture 'God-breathed'. | U48;U49 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R4-04 | E | Supported | Vitality (Islamic, descriptive): Qur'an 15:29 describes God breathing into the human of His [created] soul (rūḥ). | U50 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R4-05 | E | Supported | Vitality (Chinese, descriptive): qi is described as 'breath-energy' from which organic being and animation emerge; the phenomena the West associates with soul are, in this view, light, refined qi. | T17 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R4-06 | PS | Interpretive | Transcendence: mystical experience is defined (SEP) to exclude visions, voices and powers; mysticism covers practices, texts and traditions associated with such experiences, which occur within all world religions. | S15 | Carried unchanged. |
| C0v2-R4-07 | PS | Interpretive | Connection: African ethics stresses humanity/brotherhood and the common good; animist traditions extend social relations to non-human persons — spirit as connection, reported as belief. | U44;U45 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R4-08 | P | Mixed | Well-being (demonstrable side): a systematic review reports that religion/spirituality is, on balance, associated with greater well-being and better mental health, with some negative or mixed findings. | S11 | Carried unchanged. |
| C0v2-R4-09 | E | Supported | In the Nurses' Health Study (n = 74,534), attending services more than once/week vs never was associated with 33% lower all-cause mortality (HR 0.67, 95% CI 0.62–0.71). | S12 | Carried unchanged. |
| C0v2-R4-10 | P | Indeterminate | A meta-analysis of prospective cohorts found religiosity/spirituality associated with reduced mortality in initially healthy populations (combined HR 0.82, 0.76–0.87) but not in diseased populations (HR 0.98, 0.94–1.01). | T08 | Carried unchanged. |
| C0v2-R4-11 | P | Contested | Many 'spirituality' measures are contaminated with mental-health and positive-character items, making some spirituality–health correlations tautological. | S13 | Carried unchanged. |
| C0v2-R4-12 | E | Supported | For HR 0.67, the E-value is 2.35 (rare-outcome) or 1.97 after common-outcome conversion (outcome risk 18%); CI-limit E-values 2.17 / 1.85. | C0:SIM-R4-C0#E1;S14 | Carried unchanged. |
| C0v2-R4-13 | E | Supported | Corrected confounding simulation: with no causal effect and an unmeasured confounder at strength E on both associations (worst-case allocation), the crude RR was 0.760 vs observed 0.758; at 0.9·E it was 0.812 (cannot explain the association); weak confounding (1.2) gave 0.977. | C0:SIM-R4-C0#E2a;C0:SIM-R4-C0#E2;C0:SIM-R4-C0#E2b;C0:SIM-R4-C0#E3 | Carried unchanged. |
| C0v2-R4-14 | H | Hypothetical | That religious participation causally lowers mortality remains a hypothesis. Cycle 1 adds full-text cohorts with E-values of 2.04 (all-cause) and 2.35-5.70 (deaths from despair), a Swedish cohort in which the association disappeared once social participation was adjusted, and an abstract-only sibling/instrument study; simulations show both designs can still be biased (individual-level confounding; exclusion violations). | S12;S14;V12;V13;V14;V16;SIM-R4-C1/iter-3#S2;SIM-R4-C1/iter-3#S4 | Carried unchanged. |
| C0v2-R4-15 | PS | Interpretive | Spirit as vitality, transcendence, connection or inspiration is not shown or refuted by the well-being data; those data concern measurable practices and associations, kept separate per the framework. | G03;S13 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C1-R4-01 | E | Supported | In pooled data from two US cohorts, weekly religious-service attendance vs never was associated with 26% lower all-cause mortality (RR 0.74, 95% CI 0.65-0.84), with an E-value of 2.04 for the point estimate, in an outcome-wide design. | V12 | Carried unchanged. |
| C1-R4-02 | E | Supported | Among US health professionals, at-least-weekly attendance vs never was associated with lower hazard of deaths from despair (drugs, alcohol, suicide): HR 0.32 (0.16-0.62) in women (NHSII) and 0.67 (0.48-0.94) in men (HPFS); the authors report E-values of 5.70 and 2.35. | V13 | Carried unchanged. |
| C1-R4-03 | E | Supported | Challenge: in a Swedish population cohort (n = 24,855), past-year attendance was associated with lower all-cause mortality until social-participation items were introduced into the model; the authors suggest a social-network pathway in a highly secularized country. | V14 | Carried unchanged. |
| C1-R4-04 | P | Mixed | A 2025 study reports that attendance was protective against diseases of despair with similar conclusions in regression (pooled β -0.031), sibling fixed-effects (β -0.013) and instrumental-variable models (β -0.064 to -0.081). | V16 | Carried unchanged. |
| C1-R4-05 | P | Contested | Using religious market density as an instrument, Gruber reports that higher density raises religious participation and is associated with better economic outcomes (education, income, lower welfare receipt and disability). | V17 | Carried unchanged. |
| C1-R4-06 | E | Supported | Leading authors of this literature caution that it would be inappropriate to universally promote service attendance solely on the grounds of its associations with health. | V15 | Carried unchanged. |
| C1-R4-07 | E | Supported | In SIM-R4-C1, recomputed E-values matched those reported by V12 (2.04) and V13 (5.70, 2.35) to within 0.01; Li 2016 after common-outcome conversion gives 1.97 and the abstract-only Chida meta-analysis 1.74. | SIM-R4-C1/iter-1#V0;SIM-R4-C1/iter-1#V_Chen2021_mortality_pooled;SIM-R4-C1/iter-1#V_Chen2020_despair_women;SIM-R4-C1/iter-1#V_Chen2020_despair_men;S14 | Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06). |
| C1-R4-08 | E | Supported | In SIM-R4-C1's probabilistic bias analysis (confounder strengths drawn from \|N(0, sd)\| on the log scale), the share of draws that fully explained away the association was 5.5% (pooled all-cause), 6.8% (Li 2016), 0% and 1.9% (despair, women/men) and 14.7% (Chida) at sd = 0.5, rising to 37%, 40%, 1.5%, 27% and 52% at sd = 1.0: the conclusion depends on the prior. | SIM-R4-C1/iter-2#P1;SIM-R4-C1/iter-2#P2;SIM-R4-C1/iter-2#P3 | Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06). |
| C1-R4-09 | E | Supported | In SIM-R4-C1's design simulation (true effect -0.1), sibling fixed effects removed family-level confounding (bias 0.008 vs naive 0.28) but individual-level confounding biased it more than the naive estimate (-0.17 vs +0.11); a valid instrument recovered the effect (bias 0.002) and an exclusion violation biased it (-0.24). | SIM-R4-C1/iter-3#S1;SIM-R4-C1/iter-3#S2;SIM-R4-C1/iter-3#S3;SIM-R4-C1/iter-3#S4 | Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06). |
| C2-R4-01 | E | Supported | In the Nurses' Health Study analysis of religious-service attendance and mortality, proportions of the association mediated (risk-difference scale) were about 11% for depressive symptoms, 22% for smoking, 9% for optimism and 23% for social integration, with alcohol, diet and phobic anxiety near zero; the methods assume measured covariates suffice to control exposure-outcome, mediator-outcome and exposure-mediator confounding. | S12 | New in Cycle 2. |
| C2-R4-02 | E | Supported | With several mediators where earlier ones may affect later ones, path-specific effects can be defined counterfactually, there are many ways in which the decomposition can be done, and the effects are identified only under strong assumptions, for which a sensitivity analysis is suggested. | W09 | New in Cycle 2. |
| C2-R4-03 | E | Supported | De Stavola et al. show that with intermediate (exposure-induced) confounding, structural-equation mediation models need a sensitivity parameter for unmeasured mediator-outcome confounding because some parameters are not identified (collinear). | W10 | New in Cycle 2. |
| C2-R4-04 | E | Supported | In SIM-R4-C2 (synthetic data), when one mediator causes another, summing separately estimated single-mediator proportions mediated overstated the joint proportion (0.74 vs 0.49, replicated 0.73 vs 0.48); with independent mediators the sum equalled the joint proportion. | SIM-R4-C2/iter-3#V3;SIM-R4-C2/iter-3#V3b;SIM-R4-C2/iter-3#H2;SIM-R4-C2/iter-6#V3;SIM-R4-C2/iter-6#V3b;SIM-R4-C2/iter-6#H2 | New in Cycle 2. |
| C2-R4-05 | E | Supported | In SIM-R4-C2, moderate unmeasured mediator-outcome confounding (coefficient 0.3 on both paths) biased the proportion mediated by 18-19% (relative) and cut 95% CI coverage from 0.96 to 0.67 at n = 2000; both effects were real but smaller than the pre-registered bars (>= 25% bias; coverage < 0.5), so those hypotheses were not supported. | SIM-R4-C2/iter-2#V2;SIM-R4-C2/iter-2#H1;SIM-R4-C2/iter-5#V4;SIM-R4-C2/iter-5#H4;SIM-R4-C2/iter-6#V2;SIM-R4-C2/iter-6#H1 | New in Cycle 2. |
| C2-R4-06 | E | Supported | In SIM-R4-C2 iteration 4, the proportion mediated was scale-dependent in the opposite way to our expectation: the odds-ratio difference method departed from the risk-difference value by 0.08-0.10 for rare outcomes (3-8%) but by only 0.006-0.053 for common ones (37-78%) (both hypotheses not supported). | SIM-R4-C2/iter-4#H3;SIM-R4-C2/iter-4#H3b | New in Cycle 2. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-2 status |
|---|---|---|---|---|
| L10 | R3 Soul → R4 Spirit | relationship | E | Unchanged in Cycle 2. |
| L11 | R3 Soul → R4 Spirit | distinction | PS | Typology-based support weakened: the typology tolerates only ~4 random cell flips (C2-R3-03). The distinction itself rests on descriptive claims and is kept. |
| L14 | R4 Spirit → R1 Body | relationship | P | Mediation estimates added (C2-R4-01); simulations show they move with unmeasured confounding (C2-R4-05). Label unchanged. |
| L15 | R4 Spirit → R1 Body | dependency | H | Still Hypothetical: mediation shares cannot be added up (C2-R4-04) and depend on scale and confounding. |
| L16 | R4 Spirit → R4 Spirit | distinction | P | Downgraded Established -> Plausible by the strict rule (basis includes C0v2-R4-15, Philosophical/Spiritual, and C0v2-R4-11, Plausible). Procedural: the separation of spiritual interpretation from well-being data is unchanged. |
| L18 | R5 Consciousness → R4 Spirit | relationship | H | Unchanged in Cycle 2. |

## Limitations
Linear/logistic synthetic models; confounder strength is our choice; nothing is re-estimated from S12's data.

## Open questions and falsification
How strong would mediator–outcome confounding need to be to remove S12's social-integration share? Falsification: a sensitivity analysis on real data showing robustness to plausible confounding would strengthen L14.

## Conclusion and gate
Report 4 now says *how* its mediation numbers can mislead. Gate: **Indeterminate**.

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S07** — Lorenz H. Ancient Theories of Soul. Stanford Encyclopedia of Philosophy (rev. 2024). [full text] <https://plato.stanford.edu/entries/ancient-soul/>
- **S11** — Koenig HG (2012). Religion, Spirituality, and Health: The Research and Clinical Implications. ISRN Psychiatry 2012:278730. doi:10.5402/2012/278730 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3671693/>
- **S12** — Li S, Stampfer MJ, Williams DR, VanderWeele TJ (2016). Association of Religious Service Attendance With Mortality Among Women. JAMA Intern Med 176(6):777-785. doi:10.1001/jamainternmed.2016.1615 [full text (PMC author manuscript PMC5503841)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC5503841/>
- **S13** — Koenig HG (2008). Concerns about measuring 'spirituality' in research. J Nerv Ment Dis 196(5):349-355. doi:10.1097/NMD.0b013e31816ff796 [abstract only (NCBI E-utilities PMID 18477877)] <https://pubmed.ncbi.nlm.nih.gov/18477877/>
- **S14** — VanderWeele TJ, Ding P (2017). Sensitivity Analysis in Observational Research: Introducing the E-Value. Ann Intern Med 167(4):268-274. doi:10.7326/M16-2607 [full text (Harvard DASH manuscript)] <https://dash.harvard.edu/bitstreams/7312037e-0f45-6bd4-e053-0100007fdf3b/download>
- **S15** — Jones R, Gellman J. Mysticism. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/mysticism/>
- **T08** — Chida Y, Steptoe A, Powell LH (2009). Religiosity/spirituality and mortality. A systematic quantitative review. Psychother Psychosom 78(2):81-90. doi:10.1159/000190791 [abstract only (NCBI E-utilities PMID 19142047)] <https://pubmed.ncbi.nlm.nih.gov/19142047/>
- **T17** — Wong D. Chinese Philosophy of Mind (xin). Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/chinese-mind/>
- **U44** — Gyekye K. African Ethics. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/african-ethics/>
- **U45** — Smith T. Animism. Internet Encyclopedia of Philosophy. [full text] <https://iep.utm.edu/animism/>
- **U47** — Genesis 1:2, The JPS TANAKH: Gender-Sensitive Edition, via Sefaria API v3. [full text (API)] <https://www.sefaria.org/Genesis.1.2>
- **U48** — John 3:8, World English Bible (public domain), via bible-api.com. [full text (API)] <https://bible-api.com/John%203:8>
- **U49** — 2 Timothy 3:16, World English Bible (public domain), via bible-api.com. [full text (API)] <https://bible-api.com/2%20Timothy%203:16>
- **U50** — Qur'an 15:29, Saheeh International translation, via AlQuran Cloud API. [full text (API)] <https://quran.com/15/29>
- **V12** — Chen Y, Kim ES, VanderWeele TJ (2020). Religious-service attendance and subsequent health and well-being throughout adulthood: evidence from three prospective cohorts. Int J Epidemiol 49(6):2030-2040. doi:10.1093/ije/dyaa120 [full text (Europe PMC PMC7825951)] <https://europepmc.org/article/PMC/PMC7825951>
- **V13** — Chen Y, Koh HK, Kawachi I, Botticelli M, VanderWeele TJ (2020). Religious service attendance and deaths related to drugs, alcohol, and suicide among US health care professionals. JAMA Psychiatry 77(7):737-744. PMC7203669 [full text (Europe PMC PMC7203669)] <https://europepmc.org/article/PMC/PMC7203669>
- **V14** — Lindström M, Pirouzifard M, et al. (2023). Religious service attendance and mortality: a population-based prospective cohort study in southern Sweden. SSM Popul Health (article 101492). doi:10.1016/j.ssmph.2023.101492 [full text (Europe PMC PMC10458674)] <https://europepmc.org/article/PMC/PMC10458674>
- **V15** — VanderWeele TJ, Balboni TA, Koh HK (2022). Invited commentary: religious service attendance and implications for clinical care, community participation, and public health. Am J Epidemiol 191(1). doi:10.1093/aje/kwab134 [full text (Europe PMC PMC8751781)] <https://europepmc.org/article/PMC/PMC8751781>
- **V16** — Lebenbaum M, Fletcher J (2025). Religious service attendance is protective against the diseases of despair: evidence from regression, sibling-fixed effects, and instrumental variables analyses. Am J Epidemiol 194(4):1002-1011. doi:10.1093/aje/kwae289 [abstract only (NCBI E-utilities)] <https://doi.org/10.1093/aje/kwae289>
- **V17** — Gruber J (2005). Religious market structure, religious participation, and outcomes: is religion good for you? NBER Working Paper 11377 [full text (NBER PDF)] <https://www.nber.org/papers/w11377>
- **W09** — Daniel RM, De Stavola BL, Cousens SN, Vansteelandt S (2015). Causal mediation analysis with multiple mediators. Biometrics 71:1-14. doi:10.1111/biom.12248 [full text (Europe PMC PMC4402024)] <https://europepmc.org/article/PMC/PMC4402024>
- **W10** — De Stavola BL, Daniel RM, Ploubidis GB, Micali N (2015). Mediation analysis with intermediate confounding: structural equation modeling viewed through the causal inference lens. American journal of epidemiology 181:64-80. doi:10.1093/aje/kwu239 [full text (Europe PMC PMC4383385)] <https://europepmc.org/article/PMC/PMC4383385>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6) (2026-10-24): this version; details in `CHANGELOG.md`.
