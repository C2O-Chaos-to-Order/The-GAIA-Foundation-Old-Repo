# Report 2 — The Mind: cognition, perception, memory, emotion and identity

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-4-X12-R2 |
| Version | Cycle 4 (x12) |
| Status | Researched (12 passes), simulated (12 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-3-x9/Report-2-Mind/REPORT.md` (Cycle 3), Cycles 0-2 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7); Cycle-4: Report 7's own new claims excluded from its simulation inputs |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
The carried item 'faithful Mackintosh (1975) rule' is **blocked by access**: no open-access text giving the rule's specification was found (Esber & Haselgrove 2011, Y05, abstract only; Avraham et al. 2022 and Krasne et al. 2011 were read but give no specification), and we did not implement it from memory. SIM-R2-C4 is therefore a smaller, disclosed substitute: robustness and design power of the Cycle-3 delay design separating Pearce-Hall-type (PH) and Kalman-filter (KF) accounts of latent inhibition. The design holds up (delay-only 92%, curve-only 90%, combined 93% recovery at noise 0.1; 20 subjects per group for 80% power), but has a limit: if PH associability recovers during the delay, PH mimics the KF delay signature (94% drop at rho 0.05). New literature: Sbarra et al. 2023 (Y06, full text) report bidirectional causal (Mendelian randomization) evidence between loneliness and depression (P; exploratory by the authors' statement).

## What changed in Cycle 4
Pass 1 logged two Mackintosh/associability queries; pass 2 one more (open-access Mackintosh + LI); pass 3 a DOI lookup for Y05 (abstract only). Y07 and Y08 were read in full and gave no usable specification (recorded, not registered). Pass 4 (challenge) was carried by simulation (iterations 7, 9). Pass 6 added Y06 (surfaced by Report 7's logged queries). Passes 5, 7, 8 ran iterations 1–4, 5–8, 9–12. Pass 9 retried the Mackintosh item: still blocked. Pass 10: 4 new claims, 3 annotated; pass 11: new link L28; pass 12: no carried label or status changed.

Ledger: 32 claims (18 E, 11 P, 3 PS, 0 H); 4 new; 3 carried claims annotated with Cycle-4 evidence; no carried claim changed label or status (each row's `c4_change` says which).

## Methods
Twelve successive research passes (1 logged search → 2 deepen → 3 DOI/open-access lookups → 4 challenge → 5 carried agenda item (iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness (iterations 5–8) → 8 extension and challenge (iterations 9–12) → 9 retry of blocked items → 10 consolidation → 11 links → 12 diminishing-returns audit; notes in `research/pass-1..12/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and twelve chained simulation iterations (`simulation/iter-1..12`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such, not padded.

## Competing views and counter-evidence
Mackintosh-type (predictiveness) and Pearce-Hall-type (uncertainty) theories compete; Y05 proposes a reconciliation (abstract only). A two-model comparison always picks one model (60% of 50/50 mixtures went to KF), so a 'neither' outcome needs a third model or a goodness-of-fit test.

## Simulation (12 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code check: the copied rules (Mackintosh branch removed) reproduce Cycle 3; the new rho option leaves weights unchanged on empty steps. | V1: Pass, V2: Pass | 2/2 | 0/0 |
| 2 | Design power: how many subjects per group would detect the KF delay effect in a real experiment? | H2: Supported, V3: Pass | 1/1 | 1/1 |
| 3 | Which part of the design discriminates? Delay arms only. | H3: Supported | 0/0 | 1/1 |
| 4 | Ablation: pre-exposure curve only. | H4: Supported | 0/0 | 1/1 |
| 5 | Noise ceiling of the combined design. | H5: Supported | 0/0 | 1/1 |
| 6 | Mis-specification: KF generators with tau2 far outside the fitting grid. | H6: Supported | 0/0 | 1/1 |
| 7 | What does the two-model comparison do with data that are neither model (a 50/50 mixture)? | H7r: Reported, H7: Supported | 0/0 | 1/1 |
| 8 | How long must the delay be? | H8: Supported, H8r: Reported | 0/0 | 1/1 |
| 9 | Challenge: if PH associability recovers with time, does PH also show a delay effect? | H9: Supported, H9r: Reported | 0/0 | 1/1 |
| 10 | Recovery when PH may recover during the delay. | H10: Supported | 0/0 | 1/1 |
| 11 | Replication of iteration 3 (delay-only) with new seed and 2x replicates. | H11: Supported | 0/0 | 1/1 |
| 12 | Consolidation across iterations 3-11. | H12: Supported | 0/0 | 1/1 |

SUBSTITUTE simulation (disclosed). The rho option (PH associability recovery during delay) is our addition, not from a source.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-4 change |
|---|---|---|---|---|---|
| C0v2-R2-01 | E | Supported | Memory: Ebbinghaus' savings-based forgetting curve was replicated in a single-subject study (about 70 h of learning; retention intervals 20 min to 31 days). | S04 | Carried unchanged. |
| C0v2-R2-02 | E | Supported | Learning: the Rescorla–Wagner model explains Kamin blocking through a shared prediction error; attention-related phenomena require extensions beyond RW. | S06 | Carried unchanged. |
| C0v2-R2-03 | E | Supported | Learning: a meta-analysis of 839 assessments of distributed practice (317 experiments, 184 articles) found that the inter-study interval producing maximal retention increases as the retention interval increases. | T03 | Carried unchanged. |
| C0v2-R2-04 | E | Supported | Reasoning/thought: judgments under uncertainty rely on heuristics (representativeness, availability, anchoring and adjustment) that are economical and usually effective but produce systematic, predictable errors. | V04;U10 | Carried unchanged. |
| C0v2-R2-05 | P | Contested | Perception/thought: predictive-processing accounts treat brains as hierarchical prediction machines minimizing prediction error; Clark judges this the best clue yet to a unified science of mind and action while setting out evidential and conceptual challenges. | U11 | Carried unchanged. |
| C0v2-R2-06 | PS | Contested | Perception (philosophy): illusion and hallucination generate the 'problem of perception'; sense-datum, adverbial, intentionalist and naive-realist/disjunctivist theories compete. | U15 | Carried unchanged. |
| C0v2-R2-07 | P | Contested | Emotion: theories fall into feeling, evaluative (incl. appraisal) and motivational traditions (incl. basic-emotion and constructionist views) that still compete; no single definition is settled. | U12 | Carried unchanged. |
| C0v2-R2-08 | PS | Contested | Identity: there is no single problem of personal identity; psychological-continuity views and animalism (we are biological organisms) are leading competing answers to the persistence question. | U13 | Carried unchanged. |
| C0v2-R2-09 | PS | Contested | Mind–body: the identity theory holds that mental states and processes are identical to brain states and processes; physicalism and dualism remain competing positions. | U14;T06;S08 | Carried unchanged. |
| C0v2-R2-10 | P | Mixed | Mind–body: interoceptive signalling links bodily state to feelings, drives and cognitive/emotional experience; its causal role in specific mental-health conditions is plausible but not settled. | T02 | Carried unchanged. |
| C0v2-R2-11 | E | Supported | Reliability of the evidence base: in 100 replications of psychology studies, 36% had significant results and effects were about half the original size. | S05 | Carried unchanged. |
| C0v2-R2-12 | E | Supported | Across Many Labs 2, variability in observed effect sizes was attributable more to the effect studied than to the sample or setting. | V05;T04 | Carried unchanged. |
| C0v2-R2-13 | E | Supported | In SIM-R2-C0, Rescorla–Wagner reproduced blocking (V_X 0.0004 vs 0.50 control); on Ebbinghaus' data power (AIC −50.7) and log (−45.1) fit better than exponential (−29.6); on the replication data log fit best (−43.4). | C0:SIM-R2-C0#E1;C0:SIM-R2-C0#E3;C0:SIM-R2-C0#E4 | Carried unchanged. |
| C1-R2-01 | P | Mixed | A replication of 21 social-science experiments published in Nature and Science (2010-2015) found a significant effect in the same direction for 13 (62%), with replication effect sizes on average about 50% of the originals. | V37 | Carried unchanged. |
| C1-R2-02 | P | Contested | Counter-view to heuristics-as-error: the recognition-heuristic programme argues that recognition is often an ecologically valid cue and can produce a less-is-more effect, in which less recognition knowledge yields more accurate inferences; the extent of its use is debated. | V34 | Carried unchanged. |
| C1-R2-03 | P | Contested | Emotion: proponents of the theory of constructed emotion argue that it and basic emotion theory are intrinsically irreconcilable because they rest on incommensurate assumptions. | V11 | Carried unchanged. |
| C1-R2-04 | P | Contested | Challenge to predictive processing: Litwin & Miłkowski argue that presenting predictive processing as a unifying account of perception, action and cognition is premature, because it fails to deliver general, simple, homogeneous and systematic explanations. | V35 | Carried unchanged. |
| C1-R2-05 | E | Supported | In SIM-R2-C1, Rescorla–Wagner blocking (blocked-cue strength < 0.1 of control) occurred in only 20% of the learning-rate x pretraining grid; it failed whenever pretraining was weak (e.g. learning rate 0.1 with 10 pretraining trials gave ratio 0.35). | SIM-R2-C1/iter-1#W1;SIM-R2-C1/iter-1#W2 | Carried unchanged. |
| C1-R2-06 | E | Supported | In SIM-R2-C1, Rescorla–Wagner predicted no latent inhibition (acquisition ratio exactly 1), reproducing a known limitation, while a Pearce–Hall-type associability model gave ratio 0.89. | SIM-R2-C1/iter-2#L1;SIM-R2-C1/iter-2#L2 | Carried unchanged. |
| C1-R2-07 | E | Supported | In SIM-R2-C1, refitting the S04 forgetting data with leave-one-out cross-validation agreed with AIC: power fit best for Ebbinghaus (LOOCV MSE 0.0014 vs exponential 0.022) and logarithmic for the Murre & Dros replication; power won 220 and log 171 of 271 usable bootstrap resamples for the respective datasets. | SIM-R2-C1/iter-3#F1;SIM-R2-C1/iter-3#F3;S04 | Carried unchanged. |
| C2-R2-01 | P | Supported | A review of novelty and surprise in learning notes that a Bayesian account of increases in the rate of animal learning accomplishes what the Pearce-Hall model does via an explicit measure of surprise (prediction-error magnitude). | W06 | Carried unchanged. |
| C2-R2-02 | E | Supported | In SIM-R2-C2, both a Pearce-Hall-type hybrid and a Kalman-filter (Bayesian) learner produced latent inhibition and blocking at default parameters (PH: LI 0.27, blocking 0.95; KF: 0.52, 0.99) and in 58% and 71% of their parameter grids, with latent inhibition growing monotonically with pre-exposure; Rescorla-Wagner never produced latent inhibition. | SIM-R2-C2/iter-1#V1;SIM-R2-C2/iter-1#V2;SIM-R2-C2/iter-1#V3;SIM-R2-C2/iter-1#H_PH;SIM-R2-C2/iter-1#H_KF;SIM-R2-C2/iter-2#S1;SIM-R2-C2/iter-2#S2;SIM-R2-C2/iter-2#S3;SIM-R2-C2/iter-3#D_PH;SIM-R2-C2/iter-3#D_KF | Carried unchanged. |
| C2-R2-03 | E | Supported | In SIM-R2-C2 model-recovery tests, a design combining acquisition, latent inhibition and blocking recovered the generating model in 100% (noise 0.05, replicated with 40 replicates), 98% (0.1) and 88% (0.2) of cases versus 97%, 73% and 65% for acquisition only; the pre-registered advantage of >= 0.2 was not supported at low noise (ceiling) but held at higher noise. | SIM-R2-C2/iter-4#MR_0.05;SIM-R2-C2/iter-4#MG_0.05;SIM-R2-C2/iter-5#MR_0.1;SIM-R2-C2/iter-5#MG_0.1;SIM-R2-C2/iter-5#MR_0.2;SIM-R2-C2/iter-5#MG_0.2;SIM-R2-C2/iter-6#MR_0.05 | Carried unchanged. |
| C3-R2-01 | E | Supported | Graham et al. (2011) developed the Moral Foundations Questionnaire from a model of five universally available but variably developed sets of moral intuitions (Harm/care, Fairness/reciprocity, Ingroup/loyalty, Authority/respect, Purity/sanctity) and report evidence for its internal and external validity. | X21 | Carried unchanged. |
| C3-R2-02 | P | Supported | An early systematic review of compassion-focused therapy (14 studies, three randomised) found results mostly favourable, particularly for people high in self-criticism, but concluded that more large-scale, high-quality trials are needed before it can be considered evidence-based practice. | X18 | Carried unchanged. |
| C3-R2-03 | E | Supported | In SIM-R2-C3, two designs separate a Pearce-Hall-type hybrid from a Kalman-filter learner: a context change between pre-exposure and conditioning cut KF latent inhibition by 89% but raised it in the PH hybrid (so 'both context-specific' was not supported), and a delay before conditioning removed 98% of KF latent inhibition while leaving PH unchanged (0%); LI-by-pre-exposure curves also differed (max 0.30). | SIM-R2-C3/iter-1#V1;SIM-R2-C3/iter-1#V2;SIM-R2-C3/iter-2#H2;SIM-R2-C3/iter-3#H3;SIM-R2-C3/iter-4#H4 | Cycle 4 adds a limit: if PH associability recovers during the delay, PH also shows a delay effect (C4-R2-04). |
| C3-R2-04 | E | Supported | In SIM-R2-C3, a combined parametric pre-exposure + delay design recovered PH vs KF in 93% of datasets at noise 0.1 with default generators and in 98% with generators drawn off the fitting grid (replicated at 95% with a new seed and 120 replicates); the KF delay signature held in 84% of a tau2 x sigma2 grid. | SIM-R2-C3/iter-5#H5;SIM-R2-C3/iter-6#H6;SIM-R2-C3/iter-7#H7;SIM-R2-C3/iter-9#H9 | Extended in Cycle 4 (ablations, power, mis-specified range; C4-R2-03) with a limit (C4-R2-04). |
| C3-R2-05 | E | Supported | SIM-R2-C3's simplified Mackintosh-type rule produced no latent inhibition at any pre-exposure level in the parametric pre-exposure design (H2b not supported) and three-way recovery fell to 63% at noise 0.1 (not supported); the zero-LI result is an artefact of our simplification (its associability decline was coded only for single-cue trials), not a test of Mackintosh's theory. | SIM-R2-C3/iter-2#H2b;SIM-R2-C3/iter-8#H8 | Faithful Mackintosh (1975) rule still BLOCKED by access in Cycle 4 (Y05 abstract only; C4-R2-02); not re-tested. |
| C4-R2-01 | P | Supported | Sbarra et al. (2023), using bidirectional two-sample Mendelian randomization with data from three large genome-wide association studies, report robust evidence for a bidirectional causal relationship between loneliness and major depression, with estimates that remained significant across sensitivity analyses including models for horizontal pleiotropy; the authors state the analyses were not preregistered and should be considered largely exploratory. | Y06 | New in Cycle 4. |
| C4-R2-02 | P | Supported | Esber & Haselgrove (2011) put forward a formal attentional model of associative learning that reconciles predictiveness-driven and uncertainty-driven changes in cue salience (the two classes of theory behind Mackintosh-type and Pearce-Hall-type accounts). | Y05 | New in Cycle 4. |
| C4-R2-03 | E | Supported | In SIM-R2-C4 (a smaller substitute study, because the faithful Mackintosh rule could not be obtained), the delay design that separates Pearce-Hall-type (PH) from Kalman-filter (KF) latent inhibition held up: with off-grid generators at noise 0.1, delay arms alone recovered the generating model in 92% (replicated 93%), the pre-exposure curve alone in 90% and the combined design in 93% (82% at noise 0.3); 80% power to detect the KF delay effect needed 20 subjects per group at between-subject SD 0.3; KF tau2 generators 3x outside the grid still gave 95%. | SIM-R2-C4/iter-1#V1;SIM-R2-C4/iter-1#V2;SIM-R2-C4/iter-2#H2;SIM-R2-C4/iter-2#V3;SIM-R2-C4/iter-3#H3;SIM-R2-C4/iter-4#H4;SIM-R2-C4/iter-5#H5;SIM-R2-C4/iter-6#H6;SIM-R2-C4/iter-11#H11;SIM-R2-C4/iter-12#H12 | New in Cycle 4. |
| C4-R2-04 | E | Supported | SIM-R2-C4 found a limit of the delay design: if PH associability recovers toward its starting value during the delay (rho, our addition), PH also loses latent inhibition with delay (45% at rho 0.01, 94% at rho 0.05, versus 86% for KF), so a delay effect alone does not identify a Bayesian learner; with rho included in the fit, recovery was still 85% at noise 0.1, and a two-model fit assigned 60% of 50/50 PH-KF mixtures to KF (it cannot say 'neither'). | SIM-R2-C4/iter-7#H7;SIM-R2-C4/iter-7#H7r;SIM-R2-C4/iter-9#H9;SIM-R2-C4/iter-9#H9r;SIM-R2-C4/iter-10#H10 | New in Cycle 4. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-4 status |
|---|---|---|---|---|
| L04 | R1 Body → R2 Mind | dependency | P | No Cycle-4 evidence targeted this link. |
| L05 | R1 Body → R2 Mind | feedback loop | P | No Cycle-4 evidence targeted this link. |
| L06 | R1 Body → R2 Mind | competing interpretation | PS | No Cycle-4 evidence targeted this link. |
| L07 | R2 Mind → R5 Consciousness | relationship | P | Unchanged (Plausible); new criticality evidence concerns network dynamics, not prediction-error processing. |
| L08 | R2 Mind → R5 Consciousness | distinction | P | No Cycle-4 evidence targeted this link. |
| L09 | R2 Mind → R3 Soul | competing interpretation | PS | No Cycle-4 evidence targeted this link. |
| L25 | R1 Body → R2 Mind | relationship | P | Unchanged (Plausible). Context: genetic-instrument evidence that loneliness and depression influence each other (a mental-side pathway, see L28); L25's body-survival association itself was not re-tested. |
| L28 | R2 Mind → R2 Mind | feedback loop | P | New in Cycle 4. |

## Limitations
Mackintosh comparison not done (blocked). Y06 is one exploratory MR study; MR depends on instrument validity. Both loneliness and depression are within Report 2, so Y06 does not by itself link Mind to another report.

## Open questions and falsification
Does associability recover with time in real animals (a delay test that could reject the PH-no-recovery assumption)? Does the loneliness-depression MR replicate with independent instruments?

## Conclusion and gate
Report 2 gains a plausible causal (MR) link inside the Mind, a robust but conditional design result, and an honestly blocked item. It still has no Established link to another report. **Gate: Indeterminate** (internal checks pass; no independent review; Indeterminate is never Pass).

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S04** — Murre JMJ, Dros J (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. PLoS ONE 10(7):e0120644. doi:10.1371/journal.pone.0120644 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/>
- **S05** — Open Science Collaboration (2015). Estimating the reproducibility of psychological science. Science 349:aac4716. doi:10.1126/science.aac4716 [full text (PDF hosted by Reed College)] <https://www.reed.edu/psychology/scalp/assets/journal-articles/OSC_RP_2015_Science.pdf>
- **S06** — Holland PC, Schiffino FL (2016). Mini-Review: Prediction errors, attention and associative learning. Neurobiol Learn Mem (PMC4862921). [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4862921/>
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). [full text] <https://plato.stanford.edu/entries/dualism/>
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 [full text (PMC6054486)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/>
- **T03** — Cepeda NJ, Pashler H, Vul E, Wixted JT, Rohrer D (2006). Distributed practice in verbal recall tasks: a review and quantitative synthesis. Psychol Bull 132(3):354-380. doi:10.1037/0033-2909.132.3.354 [full text (author-hosted PDF)] <https://www.yorku.ca/ncepeda/publications/CPVWR2006.pdf>
- **T04** — Klein RA, Vianello M, Hasselman F, et al. (2018). Many Labs 2: Investigating Variation in Replicability Across Samples and Settings. Adv Methods Pract Psychol Sci 1(4):443-490. doi:10.1177/2515245918810225 [abstract only (APS journal page)] <https://www.psychologicalscience.org/journals/ampps/2515245918810225/>
- **T06** — Stoljar D. Physicalism. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/physicalism/>
- **U10** — Tversky A, Kahneman D (1974). Judgment under Uncertainty: Heuristics and Biases. Science 185(4157):1124-1131. doi:10.1126/science.185.4157.1124 [abstract only (NCBI E-utilities PMID 17835457)] <https://pubmed.ncbi.nlm.nih.gov/17835457/>
- **U11** — Clark A (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. Behav Brain Sci 36(3):181-204. doi:10.1017/S0140525X12000477 [abstract only (NCBI E-utilities PMID 23663408)] <https://pubmed.ncbi.nlm.nih.gov/23663408/>
- **U12** — Scarantino A, de Sousa R. Emotion. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/emotion/>
- **U13** — Olson ET. Personal Identity. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/identity-personal/>
- **U14** — Smart JJC. The Mind/Brain Identity Theory. Stanford Encyclopedia of Philosophy (rev. 2007). [full text] <https://plato.stanford.edu/entries/mind-identity/>
- **U15** — Crane T, French C. The Problem of Perception. Stanford Encyclopedia of Philosophy (rev. 2021). [full text] <https://plato.stanford.edu/entries/perception-problem/>
- **V04** — Tversky A, Kahneman D (1974). Judgment under uncertainty: heuristics and biases. Science 185(4157):1124-1131 (JSTOR scan hosted on a UC Irvine course page) [full text (PDF, third-party course host)] <https://sites.socsci.uci.edu/~bskyrms/bio/readings/tversky_k_heuristics_biases.pdf>
- **V05** — Klein RA, et al. (2018). Many Labs 2: Investigating variation in replicability across samples and settings. Adv Methods Pract Psychol Sci 1(4):443-490. doi:10.1177/2515245918810225 [full text (PDF, UvA-DARE repository)] <https://pure.uva.nl/ws/files/32817291/2515245918810225.pdf>
- **V11** — Barrett LF, et al. (2025). The theory of constructed emotion: more than a feeling. Perspect Psychol Sci. doi:10.1177/17456916251319045 [full text (Europe PMC PMC12164598)] <https://europepmc.org/article/PMC/PMC12164598>
- **V34** — Pachur T, Todd PM, Gigerenzer G, Schooler LJ, Goldstein DG (2011). The recognition heuristic: a review of theory and tests. Front Psychol 2:147. doi:10.3389/fpsyg.2011.00147 [full text (Europe PMC PMC3132682)] <https://europepmc.org/article/PMC/PMC3132682>
- **V35** — Litwin P, Miłkowski M (2020). Unification by fiat: arrested development of predictive processing. Cogn Sci 44(7):e12867. doi:10.1111/cogs.12867 [full text (Europe PMC PMC7378938)] <https://europepmc.org/article/PMC/PMC7378938>
- **V37** — Camerer CF, et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. Nat Hum Behav 2(9):637-644. doi:10.1038/s41562-018-0399-z [abstract only (NCBI E-utilities)] <https://doi.org/10.1038/s41562-018-0399-z>
- **W06** — Barto A, Mirolli M, Baldassarre G (2013). Novelty or surprise?. Frontiers in psychology 4:907. doi:10.3389/fpsyg.2013.00907 [full text (Europe PMC PMC3858647)] <https://europepmc.org/article/PMC/PMC3858647>
- **X18** — Leaviss J, Uttley L (2015). Psychotherapeutic benefits of compassion-focused therapy: an early systematic review. Psychological medicine 45:927-945. doi:10.1017/s0033291714002141 [full text (Europe PMC PMC4413786)] <https://europepmc.org/article/PMC/PMC4413786>
- **X21** — Graham J, Nosek BA, Haidt J, Iyer R, Koleva S, Ditto PH (2011). Mapping the moral domain. Journal of personality and social psychology 101:366-385. doi:10.1037/a0021847 [full text (PMC OAI-PMH PMC3116962)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3116962/>
- **Y05** — Esber GR, Haselgrove M (2011). Reconciling the influence of predictiveness and uncertainty on stimulus salience: a model of attention in associative learning. Proceedings. Biological sciences 278:2553-2561. doi:10.1098/rspb.2011.0836 [abstract only (NCBI efetch PMC3136838; metadata and abstract returned)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3136838/>
- **Y06** — Sbarra DA, Ramadan FA, Choi KW, Treur JL, Levey DF, Wootton RE, Stein MB, Gelernter J, Klimentidis YC (2023). Loneliness and depression: bidirectional mendelian randomization analyses using data from three large genome-wide association studies. Molecular psychiatry 28:4594-4601. doi:10.1038/s41380-023-02259-w [full text (NCBI efetch PMC11406447, author manuscript)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11406447/>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9): `../../Cycle-3-x9/`.
- Cycle 4 (x12) (2026-10-24): this version; details in `CHANGELOG.md`.
