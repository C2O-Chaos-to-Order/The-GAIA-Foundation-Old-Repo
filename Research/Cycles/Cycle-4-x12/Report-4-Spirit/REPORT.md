# Report 4 — The Spirit: spirituality, religion and health

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-4-X12-R4 |
| Version | Cycle 4 (x12) |
| Status | Researched (12 passes), simulated (12 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-3-x9/Report-4-Spirit/REPORT.md` (Cycle 3), Cycles 0-2 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7); Cycle-4: Report 7's own new claims excluded from its simulation inputs |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 4 takes the carried item 'negative-control designs' for the religious-attendance → mortality association. Two methods papers were read in full (Lipsitch et al. 2010, Y03; Arnold et al. 2016, Y04: E). SIM-R4-C4 (12 iterations, synthetic cohorts) shows negative controls detect **strong** confounding well (90% power, replicated 96%; false-flag 4.5%) and the ratio correction recovers a true effect (0.736 vs 0.741), but **weak** confounding of the size that could still matter (spurious OR 0.91–0.97) goes undetected even at 100,000 people, rare outcomes and imperfect controls lose power, and so a null negative-control result would not show the association is unconfounded. Disclosure: iteration 6 (selection bias) was mis-specified — its scenario contained no bias to detect — so its 'not supported' is a design error and is not cited. No real negative-control study of attendance was found in logged searches.

## What changed in Cycle 4
Pass 1 logged two queries (negative control/E-value with religiosity; attendance-mortality cohorts) — no negative-control study of attendance in top hits. Pass 2 (title 'negative controls') surfaced Y03 and Y04; pass 3 a DOI lookup for Y03 (author manuscript via NCBI). Passes 4, 6, 9 added nothing. Passes 5, 7, 8 ran iterations 1–4, 5–8, 9–12. Pass 10: 4 new claims; C0v2-R4-12 annotated. Pass 11: L14, L15 updated. Pass 12: no carried label or status changed.

Ledger: 39 claims (29 E, 6 P, 3 PS, 1 H); 4 new; 1 carried claims annotated with Cycle-4 evidence; no carried claim changed label or status (each row's `c4_change` says which).

## Methods
Twelve successive research passes (1 logged search → 2 deepen → 3 DOI/open-access lookups → 4 challenge → 5 carried agenda item (iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness (iterations 5–8) → 8 extension and challenge (iterations 9–12) → 9 retry of blocked items → 10 consolidation → 11 links → 12 diminishing-returns audit; notes in `research/pass-1..12/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and twelve chained simulation iterations (`simulation/iter-1..12`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such, not padded.

## Competing views and counter-evidence
Attendance may protect health (social support, behaviour) or merely mark health (healthy-attender confounding). Negative controls can test the second explanation only for strong confounding; weak confounding, mediation and confounding remain hard to separate (C3-R4-04).

## Simulation (12 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code check: null cohort and U-stratified recovery of a known effect. | V1: Pass, V2: Pass | 2/2 | 0/0 |
| 2 | Does a negative-control outcome (NCO) detect confounding that alone produces an apparent protective effect? | H2: Supported, H2r: Reported | 0/0 | 1/1 |
| 3 | False-flag rate when there is no confounding but a true effect. | V3: Pass | 1/1 | 0/0 |
| 4 | When can the NCO also correct the estimate (ratio OR_D/OR_N)? | H4: Not supported, H4r: Reported | 0/0 | 0/1 |
| 5 | Negative-control exposure (Y03's second type). | H5: Supported | 0/0 | 1/1 |
| 6 | Selection bias (Y04): entry into the cohort depends on attendance and health. | H6: Not supported | 0/0 | 0/1 |
| 7 | How weak a confounder can an NCO detect? | H7: Not supported, H7r: Reported | 0/0 | 0/1 |
| 8 | Sample size for the weak scenario. | H8: Not supported | 0/0 | 0/1 |
| 9 | Rare outcomes, as for cause-specific mortality. | H9: Not supported | 0/0 | 0/1 |
| 10 | Imperfect NCO (Y03 warns these are common). | H10: Not supported | 0/0 | 0/1 |
| 11 | Replication of iteration 2 with new seeds. | H11: Supported | 0/0 | 1/1 |
| 12 | Consolidation: confounding plus a true effect. | H12: Supported | 0/0 | 1/1 |

Iteration-6 design error disclosed above; the iteration was kept, not re-run or re-specified.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-4 change |
|---|---|---|---|---|---|
| C0v2-R4-01 | E | Supported | Vitality (Greek, descriptive): Stoic pneuma ('breath') comes in grades — the lowest gives cohesion to inanimate bodies, higher ones account for nature (growth) and soul. | S07 | Carried unchanged. |
| C0v2-R4-02 | E | Supported | Vitality (Hebrew Bible, descriptive): Genesis 1:2 rûaḥ is rendered 'a wind from God' in the JPS translation, which notes that others render it 'the spirit of [God]' — the word spans wind, breath and spirit. | U47 | Carried unchanged. |
| C0v2-R4-03 | E | Supported | Connection/vitality (Christian, descriptive): John 3:8 (WEB) likens being 'born of the Spirit' to the wind that blows where it wants; inspiration: 2 Timothy 3:16 calls Scripture 'God-breathed'. | U48;U49 | Carried unchanged. |
| C0v2-R4-04 | E | Supported | Vitality (Islamic, descriptive): Qur'an 15:29 describes God breathing into the human of His [created] soul (rūḥ). | U50 | Carried unchanged. |
| C0v2-R4-05 | E | Supported | Vitality (Chinese, descriptive): qi is described as 'breath-energy' from which organic being and animation emerge; the phenomena the West associates with soul are, in this view, light, refined qi. | T17 | Carried unchanged. |
| C0v2-R4-06 | PS | Interpretive | Transcendence: mystical experience is defined (SEP) to exclude visions, voices and powers; mysticism covers practices, texts and traditions associated with such experiences, which occur within all world religions. | S15 | Carried unchanged. |
| C0v2-R4-07 | PS | Interpretive | Connection: African ethics stresses humanity/brotherhood and the common good; animist traditions extend social relations to non-human persons — spirit as connection, reported as belief. | U44;U45 | Carried unchanged. |
| C0v2-R4-08 | P | Mixed | Well-being (demonstrable side): a systematic review reports that religion/spirituality is, on balance, associated with greater well-being and better mental health, with some negative or mixed findings. | S11 | Carried unchanged. |
| C0v2-R4-09 | E | Supported | In the Nurses' Health Study (n = 74,534), attending services more than once/week vs never was associated with 33% lower all-cause mortality (HR 0.67, 95% CI 0.62–0.71). | S12 | Carried unchanged. |
| C0v2-R4-10 | P | Indeterminate | A meta-analysis of prospective cohorts found religiosity/spirituality associated with reduced mortality in initially healthy populations (combined HR 0.82, 0.76–0.87) but not in diseased populations (HR 0.98, 0.94–1.01). | T08 | Carried unchanged. |
| C0v2-R4-11 | P | Contested | Many 'spirituality' measures are contaminated with mental-health and positive-character items, making some spirituality–health correlations tautological. | S13 | Carried unchanged. |
| C0v2-R4-12 | E | Supported | For HR 0.67, the E-value is 2.35 (rare-outcome) or 1.97 after common-outcome conversion (outcome risk 18%); CI-limit E-values 2.17 / 1.85. | C0:SIM-R4-C0#E1;S14 | Cycle 4 adds negative-control design analysis (C4-R4-01 to C4-R4-04): such controls detect strong but not weak confounding at typical cohort sizes; no real negative-control study of attendance was read. |
| C0v2-R4-13 | E | Supported | Corrected confounding simulation: with no causal effect and an unmeasured confounder at strength E on both associations (worst-case allocation), the crude RR was 0.760 vs observed 0.758; at 0.9·E it was 0.812 (cannot explain the association); weak confounding (1.2) gave 0.977. | C0:SIM-R4-C0#E2a;C0:SIM-R4-C0#E2;C0:SIM-R4-C0#E2b;C0:SIM-R4-C0#E3 | Carried unchanged. |
| C0v2-R4-14 | H | Hypothetical | That religious participation causally lowers mortality remains a hypothesis. Cycle 1 adds full-text cohorts with E-values of 2.04 (all-cause) and 2.35-5.70 (deaths from despair), a Swedish cohort in which the association disappeared once social participation was adjusted, and an abstract-only sibling/instrument study; simulations show both designs can still be biased (individual-level confounding; exclusion violations). | S12;S14;V12;V13;V14;V16;SIM-R4-C1/iter-3#S2;SIM-R4-C1/iter-3#S4 | Carried unchanged. |
| C0v2-R4-15 | PS | Interpretive | Spirit as vitality, transcendence, connection or inspiration is not shown or refuted by the well-being data; those data concern measurable practices and associations, kept separate per the framework. | G03;S13 | Carried unchanged. |
| C1-R4-01 | E | Supported | In pooled data from two US cohorts, weekly religious-service attendance vs never was associated with 26% lower all-cause mortality (RR 0.74, 95% CI 0.65-0.84), with an E-value of 2.04 for the point estimate, in an outcome-wide design. | V12 | Carried unchanged. |
| C1-R4-02 | E | Supported | Among US health professionals, at-least-weekly attendance vs never was associated with lower hazard of deaths from despair (drugs, alcohol, suicide): HR 0.32 (0.16-0.62) in women (NHSII) and 0.67 (0.48-0.94) in men (HPFS); the authors report E-values of 5.70 and 2.35. | V13 | Carried unchanged. |
| C1-R4-03 | E | Supported | Challenge: in a Swedish population cohort (n = 24,855), past-year attendance was associated with lower all-cause mortality until social-participation items were introduced into the model; the authors suggest a social-network pathway in a highly secularized country. | V14 | Carried unchanged. |
| C1-R4-04 | P | Mixed | A 2025 study reports that attendance was protective against diseases of despair with similar conclusions in regression (pooled β -0.031), sibling fixed-effects (β -0.013) and instrumental-variable models (β -0.064 to -0.081). | V16 | Carried unchanged. |
| C1-R4-05 | P | Contested | Using religious market density as an instrument, Gruber reports that higher density raises religious participation and is associated with better economic outcomes (education, income, lower welfare receipt and disability). | V17 | Carried unchanged. |
| C1-R4-06 | E | Supported | Leading authors of this literature caution that it would be inappropriate to universally promote service attendance solely on the grounds of its associations with health. | V15 | Carried unchanged. |
| C1-R4-07 | E | Supported | In SIM-R4-C1, recomputed E-values matched those reported by V12 (2.04) and V13 (5.70, 2.35) to within 0.01; Li 2016 after common-outcome conversion gives 1.97 and the abstract-only Chida meta-analysis 1.74. | SIM-R4-C1/iter-1#V0;SIM-R4-C1/iter-1#V_Chen2021_mortality_pooled;SIM-R4-C1/iter-1#V_Chen2020_despair_women;SIM-R4-C1/iter-1#V_Chen2020_despair_men;S14 | Carried unchanged. |
| C1-R4-08 | E | Supported | In SIM-R4-C1's probabilistic bias analysis (confounder strengths drawn from \|N(0, sd)\| on the log scale), the share of draws that fully explained away the association was 5.5% (pooled all-cause), 6.8% (Li 2016), 0% and 1.9% (despair, women/men) and 14.7% (Chida) at sd = 0.5, rising to 37%, 40%, 1.5%, 27% and 52% at sd = 1.0: the conclusion depends on the prior. | SIM-R4-C1/iter-2#P1;SIM-R4-C1/iter-2#P2;SIM-R4-C1/iter-2#P3 | Carried unchanged. |
| C1-R4-09 | E | Supported | In SIM-R4-C1's design simulation (true effect -0.1), sibling fixed effects removed family-level confounding (bias 0.008 vs naive 0.28) but individual-level confounding biased it more than the naive estimate (-0.17 vs +0.11); a valid instrument recovered the effect (bias 0.002) and an exclusion violation biased it (-0.24). | SIM-R4-C1/iter-3#S1;SIM-R4-C1/iter-3#S2;SIM-R4-C1/iter-3#S3;SIM-R4-C1/iter-3#S4 | Carried unchanged. |
| C2-R4-01 | E | Supported | In the Nurses' Health Study analysis of religious-service attendance and mortality, proportions of the association mediated (risk-difference scale) were about 11% for depressive symptoms, 22% for smoking, 9% for optimism and 23% for social integration, with alcohol, diet and phobic anxiety near zero; the methods assume measured covariates suffice to control exposure-outcome, mediator-outcome and exposure-mediator confounding. | S12 | Carried unchanged. |
| C2-R4-02 | E | Supported | With several mediators where earlier ones may affect later ones, path-specific effects can be defined counterfactually, there are many ways in which the decomposition can be done, and the effects are identified only under strong assumptions, for which a sensitivity analysis is suggested. | W09 | Carried unchanged. |
| C2-R4-03 | E | Supported | De Stavola et al. show that with intermediate (exposure-induced) confounding, structural-equation mediation models need a sensitivity parameter for unmeasured mediator-outcome confounding because some parameters are not identified (collinear). | W10 | Carried unchanged. |
| C2-R4-04 | E | Supported | In SIM-R4-C2 (synthetic data), when one mediator causes another, summing separately estimated single-mediator proportions mediated overstated the joint proportion (0.74 vs 0.49, replicated 0.73 vs 0.48); with independent mediators the sum equalled the joint proportion. | SIM-R4-C2/iter-3#V3;SIM-R4-C2/iter-3#V3b;SIM-R4-C2/iter-3#H2;SIM-R4-C2/iter-6#V3;SIM-R4-C2/iter-6#V3b;SIM-R4-C2/iter-6#H2 | Carried unchanged. |
| C2-R4-05 | E | Supported | In SIM-R4-C2, moderate unmeasured mediator-outcome confounding (coefficient 0.3 on both paths) biased the proportion mediated by 18-19% (relative) and cut 95% CI coverage from 0.96 to 0.67 at n = 2000; both effects were real but smaller than the pre-registered bars (>= 25% bias; coverage < 0.5), so those hypotheses were not supported. | SIM-R4-C2/iter-2#V2;SIM-R4-C2/iter-2#H1;SIM-R4-C2/iter-5#V4;SIM-R4-C2/iter-5#H4;SIM-R4-C2/iter-6#V2;SIM-R4-C2/iter-6#H1 | Carried unchanged. |
| C2-R4-06 | E | Supported | In SIM-R4-C2 iteration 4, the proportion mediated was scale-dependent in the opposite way to our expectation: the odds-ratio difference method departed from the risk-difference value by 0.08-0.10 for rare outcomes (3-8%) but by only 0.006-0.053 for common ones (37-78%) (both hypotheses not supported). | SIM-R4-C2/iter-4#H3;SIM-R4-C2/iter-4#H3b | Carried unchanged. |
| C3-R4-01 | P | Supported | In a population-based prospective cohort in southern Sweden (24,855 adults, 8.3-year follow-up; 13.9% attended a religious service in the past year), attendance was associated with lower all-cause mortality until social participation items were introduced in the final model. | X11 | Carried unchanged. |
| C3-R4-02 | E | Supported | VanderWeele & Ding (2017) state that when the outcome is common (more than 15%), an approximate E-value for a hazard ratio is obtained by applying RR ~ (1-0.5^sqrt(HR))/(1-0.5^sqrt(1/HR)) in the E-value formula. | S14 | Carried unchanged. |
| C3-R4-03 | E | Supported | In SIM-R4-C3, S12's reported E-value of 2.35 was reproduced, but S12 has 18% cumulative mortality, and with S14's common-outcome approximation the E-value is about 1.97 (CI limit 1.85) - this repeats Cycle 1's finding (C1-R4-07: 1.97) and is not new; new in Cycle 3, an exact proportional-hazards conversion at ~20% risk gives 2.24 (so the approximation is not within 0.1 of it: not supported). The strength of unmeasured confounding needed to explain the association away is therefore about 2.0-2.35-fold, depending on how outcome frequency is handled. | SIM-R4-C3/iter-1#V2;SIM-R4-C3/iter-1#V3;SIM-R4-C3/iter-2#H2;SIM-R4-C3/iter-2#H2r;SIM-R4-C3/iter-8#H8 | Carried unchanged. |
| C3-R4-04 | E | Supported | SIM-R4-C3 tipping-point analyses: a confounder associated 1.5-fold with attendance would need a 3.65-fold association with mortality; six independent weak confounders (1.3-fold each, worst case) would be needed (five was not enough: not supported); one extreme pre-declared 'healthy attender' scenario (residual poor health 30% vs 10%, mortality RR 3, beyond S12's adjustment) alone would suffice; and adjusting for social participation attenuated the association by 97-101% whether it was simulated as a mediator or as a confounder. | SIM-R4-C3/iter-4#H4;SIM-R4-C3/iter-5#H5;SIM-R4-C3/iter-6#H6;SIM-R4-C3/iter-7#H7 | Carried unchanged. |
| C3-R4-05 | E | Supported | In SIM-R4-C3 run 2, a synthetic S12-sized cohort with no true effect and one confounder at the E-value strength reproduced the target RR (iteration 3; replicated over 20 cohorts in iteration 9). This repeats the Cycle-0 corrected confounding simulation (C0v2-R4-13: 0.760 vs 0.758) and adds nothing new beyond a replication. Run 1 had reported both checks 'not supported' because of our coding error (confounder prevalences swapped); run 1 is preserved in simulation/superseded-run-1. | SIM-R4-C3/iter-3#H3;SIM-R4-C3/iter-9#H9 | Carried unchanged. |
| C4-R4-01 | E | Supported | Lipsitch, Tchetgen Tchetgen & Cohen (2010) argue that negative controls, routine in laboratory experiments, can help identify confounding and other errors in observational epidemiology; they distinguish negative-control exposures and negative-control outcomes and state the conditions for using them to detect confounding. | Y03 | New in Cycle 4. |
| C4-R4-02 | E | Supported | Arnold et al. (2016) extend negative controls to detect selection bias and measurement bias in observational studies and randomized trials. | Y04 | New in Cycle 4. |
| C4-R4-03 | E | Supported | In SIM-R4-C4's synthetic cohorts, a negative-control outcome sharing the unmeasured confounder flagged confounding that alone produced a spurious protective OR of about 0.80 in 90% of cohorts of 10,000 (replicated 96%; false-flag rate 4.5% without confounding), a negative-control exposure in 91%, and with confounding plus a true effect the ratio correction gave 0.736 against a true 0.741. | SIM-R4-C4/iter-1#V1;SIM-R4-C4/iter-1#V2;SIM-R4-C4/iter-2#H2;SIM-R4-C4/iter-3#V3;SIM-R4-C4/iter-5#H5;SIM-R4-C4/iter-11#H11;SIM-R4-C4/iter-12#H12 | New in Cycle 4. |
| C4-R4-04 | E | Supported | SIM-R4-C4 found practical limits: confounding weak enough to give a spurious OR near 0.97 or 0.91 was flagged in only 5% and 23% of 10,000-person cohorts (not supported), 80% power was not reached even at 100,000 (19%; not supported), rare outcomes (2%) gave 55% power at 20,000 (not supported), an imperfect control sharing one third of the confounding gave 30% (not supported), and the ratio correction was within 10% at gN = 1 and 1.5, not only when confounding acts equally (as worded, not supported). | SIM-R4-C4/iter-4#H4;SIM-R4-C4/iter-4#H4r;SIM-R4-C4/iter-7#H7;SIM-R4-C4/iter-7#H7r;SIM-R4-C4/iter-8#H8;SIM-R4-C4/iter-9#H9;SIM-R4-C4/iter-10#H10 | New in Cycle 4. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-4 status |
|---|---|---|---|---|
| L10 | R3 Soul → R4 Spirit | relationship | E | No Cycle-4 evidence targeted this link. |
| L11 | R3 Soul → R4 Spirit | distinction | PS | No Cycle-4 evidence targeted this link. |
| L14 | R4 Spirit → R1 Body | relationship | P | Retained Plausible. Negative controls could test the confounding explanation, but in our synthetic cohorts they detect strong confounding only; weak confounding (spurious OR ~0.9-0.97) goes undetected at 10,000-100,000. No negative-control study of attendance was read. |
| L15 | R4 Spirit → R1 Body | dependency | H | Remains Hypothetical: a negative control that finds nothing would not show the association is causal. |
| L16 | R4 Spirit → R4 Spirit | distinction | P | No Cycle-4 evidence targeted this link. |
| L18 | R5 Consciousness → R4 Spirit | relationship | H | Unchanged (Hypothetical): slightly subcritical dynamics are reported in animal spike data, not in altered or spiritual states; non-stationary input can mimic near-criticality. |
| L26 | R1 Body → R4 Spirit | relationship | H | No Cycle-4 evidence targeted this link. |

## Limitations
All synthetic; perfect controls by construction except iteration 10. Spiritual interpretation (vitality, transcendence) is kept separate from measured associations.

## Open questions and falsification
Is there a cohort with a credible negative-control outcome (e.g. a cause of death attendance cannot plausibly affect) and enough events? Rejection of the confounding explanation needs such a study with high power for weak confounding.

## Conclusion and gate
The association remains Plausible (L14), causality Hypothetical (L15). **Gate: Indeterminate** (internal checks pass; no independent review; Indeterminate is never Pass).

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
- **X11** — Lindström M, Pirouzifard M (2023). Religious service attendance and mortality: A population-based prospective cohort study in southern Sweden. SSM - population health 23:101492. doi:10.1016/j.ssmph.2023.101492 [full text (Europe PMC PMC10458674)] <https://europepmc.org/article/PMC/PMC10458674>
- **Y03** — Lipsitch M, Tchetgen Tchetgen E, Cohen T (2010). Negative controls: a tool for detecting confounding and bias in observational studies. Epidemiology (Cambridge, Mass.) 21:383-388. doi:10.1097/ede.0b013e3181d61eeb [full text (NCBI efetch PMC3053408, author manuscript)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/>
- **Y04** — Arnold BF, Ercumen A, Benjamin-Chung J, Colford JM (2016). Brief Report: Negative Controls to Detect Selection Bias and Measurement Bias in Epidemiologic Studies. Epidemiology (Cambridge, Mass.) 27:637-641. doi:10.1097/ede.0000000000000504 [full text (Europe PMC PMC4969055)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4969055/>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9): `../../Cycle-3-x9/`.
- Cycle 4 (x12) (2026-10-24): this version; details in `CHANGELOG.md`.
