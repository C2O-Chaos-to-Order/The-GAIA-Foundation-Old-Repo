# Report 1 — The Body: the physical foundation of life

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-3-X9-R1 |
| Version | Cycle 3 (x9) |
| Status | Researched (9 passes), simulated (9 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-2-x6/Report-1-Body/REPORT.md` (Cycle 2), Cycles 0-1 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7) |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 3 carries the Cycle-2 open problem that a single learn-and-forget state does not reproduce fast re-acclimation (C2-R1-04). It adds a two-state memory taken from motor learning (Smith et al. 2006, X22, full text, P: a fast process that learns and forgets quickly and a slow one that learns slowly and retains well). Nine chained iterations test it in the Cycle-2 toy loop: the single-state result was reproduced exactly; on the pre-declared coarse grid 0 of 144 settings met both W05 anchors (decay ~1:2 and 8–12× faster re-induction; **not supported**), and on a finer grid only 2 of 180 did. The result is fragile: the ratio is quantised by whole days to re-induction, 1 of 20 noise seeds kept it in range, and ±20% parameter changes moved it from 2.2 to 11.3 (both **not supported**). The two-state memory does make testable predictions (decay decelerates with longer absence; the two memories are distinguishable by BIC from nine test days at 5–10% noise). Literature widened to social relationships and survival (X08, meta-analysis of 148 studies, E), deprivation and allostatic load (X25, P), interoception and emotion regulation (X20, P) and heat-acclimation retention (X09, P, n = 8).

## What changed in Cycle 3
Pass 1 logged two Europe PMC searches (broad, then title-restricted) and one exact-title query that located X22. Pass 2 read X22 in full. Pass 3 widened to allostatic load (X25) and logged an OpenAlex open-access lookup for T01 (no new full text). Pass 4 (challenge) read X09, a small study in which adaptations were largely retained 7 days after acclimation. Pass 5 built the two-state model (iterations 1–4). Pass 6 targeted the empty Body×Love and Body×Justice cells of Maps v2: X08 (surfaced by Report 7's pass-1 query) fills Body×Love by keyword; X20 came from a logged interoception/allostasis query; Body×Justice stays empty (X25 is about deprivation but its wording did not trigger the Justice keywords). Pass 7 ran robustness (iterations 5–9). Pass 8 consolidated claims (8 new; 2 carried claims annotated). Pass 9 audited: no carried label or status changed.

Ledger: 34 claims (26 E, 7 P, 1 PS, 0 H); 8 new; 2 carried claims annotated with Cycle-3 evidence; no carried claim changed label or status (each row's `c3_change` says which).

## Methods
Nine successive research passes (1 logged search → 2 deepen → 3 widen and open-access full-text upgrades → 4 challenge → 5 carried agenda item (simulation design, iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness and sensitivity (iterations 5–9) → 8 consolidation → 9 diminishing-returns audit; notes in `research/pass-1..9/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and nine chained simulation iterations (`simulation/iter-1..9`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such.

## Competing views and counter-evidence
The re-acclimation anchor itself (W05, 8 studies) is weak, so failure to reproduce it may say more about the anchor than the model. X09 found adaptations largely kept after 7 days, which is compatible with a slow memory. Social-relationship effects (X08) are observational and open to confounding by health.

## Simulation (9 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code check before new work: the copied Cycle-2 session model and single-state learner must reproduce the Cycle-2 result, and the new two-state code must collapse to it. | V1: Pass, V2: Pass | 2/2 | 0/0 |
| 2 | Can a fast-plus-slow memory meet BOTH W05 anchors (about 1 HA day lost per 2 decay days, and 8-12x faster re-induction) that a single state could not? | H2: Not supported, H2r: Reported | 0/0 | 0/1 |
| 3 | Mechanism check: is the re-induction advantage carried by the slow state's retention? | H3: Supported | 0/0 | 1/1 |
| 4 | Distinguishing prediction: does decay slow down with longer absence more in the two-state model than in a single exponential? | H4: Supported | 0/0 | 1/1 |
| 5 | Could a realistic study design tell the two memories apart? Model recovery with peak temperatures on 9 test days. | H5: Supported, H5r: Reported | 0/0 | 1/1 |
| 6 | Robustness of the selected setting to day-to-day load noise. | H6: Not supported | 0/0 | 0/1 |
| 7 | Sensitivity analysis: one-at-a-time +-20% perturbation of the four memory parameters and two loop parameters. | H7: Not supported | 0/0 | 0/1 |
| 8 | Second distinguishing prediction: do savings accumulate over repeated acclimation/decay cycles (e.g. seasons)? | H8: Supported, H8r: Reported | 0/0 | 1/1 |
| 9 | Consolidation: replicate the iteration-2 answer on an independent, finer grid. | H9: Supported | 0/0 | 1/1 |

Iterations: (1) reproduce Cycle 2 and validate the two-state code; (2) coarse grid against both W05 anchors; (3) mechanism (slow-state retention); (4) decay deceleration; (5) BIC identifiability; (6) load-noise seeds; (7) ±20% sensitivity; (8) savings over three cycles (trivial by construction); (9) finer grid. Diminishing returns: iteration 9 confirmed the fragility seen in 2, 6 and 7 rather than adding a new kind of result.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-3 change |
|---|---|---|---|---|---|
| C0v2-R1-01 | E | Supported | Human body structure is described in textbook anatomy as levels of organization of increasing complexity (chemical → cells → tissues → organs → organ systems → organism), with eleven organ systems. | U04 | Carried unchanged. |
| C0v2-R1-02 | E | Supported | The nervous system is divided anatomically into the central nervous system (brain and spinal cord) and the peripheral nervous system (everything else); its basic functions are sensation, integration and response. | U01 | Carried unchanged. |
| C0v2-R1-03 | E | Supported | Functionally, the somatic nervous system governs conscious perception and voluntary motor responses, the autonomic nervous system governs involuntary responses (smooth/cardiac muscle, glands), and the enteric nervous system handles a set of gastrointestinal functions. | U01 | Carried unchanged. |
| C0v2-R1-04 | E | Supported | Sensory receptors convert (transduce) stimuli of different kinds into the electrochemical signals of the nervous system; sensory systems include exteroceptors, interoceptors and proprioception. | U05;U02 | Carried unchanged. |
| C0v2-R1-05 | E | Supported | Sensory receptors show adaptation (declining firing to a constant stimulus) and modality specificity via labeled lines; what is perceived depends on where the nerve fibre terminates in the CNS. | U02 | Carried unchanged. |
| C0v2-R1-06 | E | Supported | Homeostasis is treated as a central unifying concept of physiology: a self-regulating process that maintains internal stability while adjusting to changing external conditions. | S01 | Carried unchanged. |
| C0v2-R1-07 | E | Supported | Homeostatic regulation involves multiple interacting feedback systems and feedforward control, not a single negative-feedback cycle. | S01 | Carried unchanged. |
| C0v2-R1-08 | E | Supported | A generic negative-feedback mechanism comprises sensor, error detector comparing the signal with a set point, controller and effector; 'set point' does not imply a fixed value. | S02 | Carried unchanged. |
| C0v2-R1-09 | E | Supported | The body keeps core temperature at about 36.5–37.5 °C by thermoregulation, which the textbook gives as an example of negative feedback, with the hypothalamus working as a thermostat; about 60% of the energy produced in ATP production appears as heat used to maintain body temperature. | V06;U03 | Carried unchanged. |
| C0v2-R1-10 | E | Supported | Interoception is the nervous system's sensing, interpretation and integration of signals from within the body, contributing to homeostatic functioning; interoceptive dysfunction is increasingly recognized in several mental-health conditions. | T02 | Carried unchanged. |
| C0v2-R1-11 | P | Contested | Allostasis (Sterling) argues that the primary goal of regulation is anticipatory adjustment, not constancy, and that feedback error-correction is inherently inefficient; this competes with homeostasis-centred accounts (S01) that include feedforward within homeostasis. | T01;S01 | Carried unchanged. |
| C0v2-R1-12 | E | Supported | In SIM-R1-C0 (toy loop), PI control restored the set point after a step load (tail mean 0.001), P-only left the analytic residual 0.476, degraded gains raised peak deviation (1.79 vs 0.36) and slowed recovery (10.99 vs 4.49), and a load beyond effector capacity was not corrected. | C0:SIM-R1-C0#E2;C0:SIM-R1-C0#E3;C0:SIM-R1-C0#E4;C0:SIM-R1-C0#E5 | Carried unchanged. |
| C0v2-R1-13 | E | Supported | In SIM-R1-C0, adding anticipatory (feedforward) control cut the peak deviation from 0.360 to 0.086, while feedforward alone with a 20% estimation error left a residual of 1.987 — in this linear toy, anticipation and feedback are complementary. | C0:SIM-R1-C0#E6;C0:SIM-R1-C0#E7 | Carried unchanged. |
| C0v2-R1-14 | PS | Contested | Embodied cognition holds that the body and body–environment interaction contribute to or constitute cognition; whether the role is constitutive or merely causal is disputed. | S03 | Carried unchanged. |
| C0v2-R1-15 | P | Indeterminate | The principle that disruption of homeostatic mechanisms is what leads to disease is asserted by S01; its generality was not tested in this pass. | S01 | Carried unchanged. |
| C0v2-R1-16 | E | Supported | Where biological explanation currently ends: how physical/neural processes give rise to phenomenal ('what it is like') experience — the 'hard problem' — remains without an accepted explanation; the origin of life is also unresolved (earliest traces disputed). | S16;S23 | Carried unchanged. |
| C1-R1-01 | E | Supported | Revised estimates for a 70 kg reference man give about 3.0·10^13 human cells and 3.8·10^13 bacteria, a bacteria:human cell ratio of about 1.3 rather than the often-quoted 10:1. | V36 | Carried unchanged. |
| C1-R1-02 | E | Supported | In SIM-R1-C1 (toy regulation loop), proportional-only control left the analytic residual D/(kl+kp) (max error 0.2%), every stable PI setting returned to set point, the numerical critical feedback delay matched the analytic value within 2.4%, and stronger PI gains tolerated less delay (critical delay 1.13 at gains (1, 0.5) down to 0.19 at (8, 2)). | SIM-R1-C1/iter-1#G1;SIM-R1-C1/iter-1#G2;SIM-R1-C1/iter-2#D1;SIM-R1-C1/iter-2#D2 | Carried unchanged. |
| C1-R1-03 | E | Supported | In SIM-R1-C1 iteration 2, across 200 draws of uncertain plant leak, gains and delay, adding an imperfect feedforward (20% estimation error) to feedback never prevented restoration of the set point (100% of runs with and without it) and cut the median peak deviation to 0.22 of feedback alone (5-95%: 0.04-0.49). | SIM-R1-C1/iter-2#M1;SIM-R1-C1/iter-2#M2 | Carried unchanged. |
| C1-R1-04 | E | Supported | In SIM-R1-C1 iteration 3 (core/shell thermal toy), using the shell (skin) signal as feedforward lowered peak core deviation from 0.053 to 0.046 at nominal parameters, but the benefit was not supported as robust: under ±50% parameter perturbation it held in only 55% of draws (worst case 2.7x worse). | SIM-R1-C1/iter-3#T1;SIM-R1-C1/iter-3#T2;SIM-R1-C1/iter-3#T3 | Carried unchanged. |
| C2-R1-01 | E | Supported | Daily exposure to moderate-intensity work under sub-lethal heat stress for up to 14 days enhances heat-dissipation mechanisms so that body temperature is lower under the same workload; these adaptations reverse with prolonged absence of heat (heat acclimatization as slow, reversible adaptation). | W04 | Carried unchanged. |
| C2-R1-02 | P | Supported | A systematic review and meta-analysis of heat-acclimation decay concludes that the available literature suggests 1 day of acclimation is lost per 2 days without heat, and that re-acclimation induced heart-rate and core-temperature adaptations 8-12 times faster than they decayed (no difference established for sweat rate); only eight studies investigated re-acclimation. | W05 | Context added in Cycle 3: a small cross-over study found adaptations generally maintained 7 days after HA (C3-R1-02). |
| C2-R1-03 | E | Supported | In SIM-R1-C2 (our toy loop), a learned, bounded-effector feedforward term updated once per daily exposure lowered peak core deviation by 81% after 14 days (half of the final adaptation by day 3), and the reduction replicated across 20 seeds of 20% day-to-day load noise (79-88%). | SIM-R1-C2/iter-1#V1;SIM-R1-C2/iter-1#V2;SIM-R1-C2/iter-1#H1;SIM-R1-C2/iter-1#H1b;SIM-R1-C2/iter-6#H6 | Carried unchanged. |
| C2-R1-04 | E | Supported | In SIM-R1-C2 iteration 2, calibrating forgetting to W05's 1:2 decay heuristic (forgetting rate 0.025/day) made re-induction only 2.1 times faster than decay, so W05's 8-12x re-acclimation ratio was not supported by a single learning-and-forgetting state; reproducing it would need e.g. a slower-decaying memory component (untested). | SIM-R1-C2/iter-2#C1cal;SIM-R1-C2/iter-2#H2 | Remedy tested in Cycle 3: a two-state memory meets both W05 anchors only in 2 of 180 fine-grid settings and the result is fragile (C3-R1-06 to C3-R1-08). |
| C2-R1-05 | E | Supported | In SIM-R1-C2 iterations 3 and 5, anticipation had a cost: when the cue came without the load, the learned feedforward cooled the core below set point in proportion to its gain (0.46 at gain 0.01 up to 1.85 unbounded), so no gain bound met the pre-registered goal (undershoot <= 0.2 with >= 70% of the benefit): not supported; and across 27 settings with noisy loads none combined >= 20% benefit with acceptable undershoot (not supported; that run fell back to the unbounded learner because no safe bound existed). | SIM-R1-C2/iter-3#H3;SIM-R1-C2/iter-3#H3r;SIM-R1-C2/iter-5#H5 | Carried unchanged. |
| C2-R1-06 | E | Supported | In SIM-R1-C2 iteration 4 (R6 analogue), letting the set point itself drift toward the prevailing temperature raised the sustained-load peak by 57-198% when unbounded, while bounds of 0.1-0.25 left the peak unchanged; the bounded result is partly trivial because the effector was saturated. | SIM-R1-C2/iter-4#H4;SIM-R1-C2/iter-4#H4b | Carried unchanged. |
| C3-R1-01 | P | Supported | In motor adaptation, Smith, Ghazizadeh & Shadmehr (2006) propose and test a two-state learning model in which one process responds weakly to error but retains information well and the other responds strongly but retains poorly; the interaction explains savings, anterograde interference, spontaneous recovery and rapid unlearning. | X22 | New in Cycle 3. |
| C3-R1-02 | P | Supported | In a balanced cross-over study of eight trained males, heat-acclimation adaptations were not notably affected by permissive dehydration and were generally maintained 7 days after acclimation; the authors conclude trained individuals require more than 5 days to optimise heat acclimation. | X09 | New in Cycle 3. |
| C3-R1-03 | P | Supported | A systematic review of eight studies concludes that awareness of one's own bodily feelings (interoception) and vagal activation seem to be of central importance for effective regulation of emotional responses, while noting that the small number of studies limits the conclusion. | X20 | New in Cycle 3. |
| C3-R1-04 | E | Supported | A meta-analysis of 148 prospective studies (308,849 participants) found a random-effects average OR of 1.50 (95% CI 1.42-1.59) for survival with stronger social relationships, and concluded that the influence of social relationships on mortality risk is comparable with well-established risk factors. | X08 | New in Cycle 3. |
| C3-R1-05 | P | Supported | A scoping review of 14 mostly cross-sectional US studies found that most (12) reported a significant association between neighbourhood socioeconomic deprivation and allostatic load, a marker of physiological 'wear and tear'. | X25 | New in Cycle 3. |
| C3-R1-06 | E | Supported | In SIM-R1-C3 (toy loop), a two-state (fast + slow) acclimation memory could, on a fine grid, meet both W05 anchors (about 1 HA day lost per 2 decay days and 8-12x faster re-induction) in only 2 of 180 settings, and in 0 of 144 settings on the pre-declared coarse grid (not supported); the single-state Cycle-2 result was reproduced exactly. The answer is fragile: the ratio is quantised by whole days to 95% re-induction (re-induction took 1-2 days), which caps most settings at 7.0. | SIM-R1-C3/iter-1#V1;SIM-R1-C3/iter-1#V2;SIM-R1-C3/iter-2#H2;SIM-R1-C3/iter-2#H2r;SIM-R1-C3/iter-9#H9 | New in Cycle 3. |
| C3-R1-07 | E | Supported | SIM-R1-C3 makes two distinguishing, testable predictions for a two-state memory: decay decelerates with longer absence (per-day loss at 40 vs 7 days falls to 0.20x, versus 0.69x for a single exponential), and the two memories are distinguishable by BIC from nine realistic test days (98% correct at 5% noise, 90% at 10%, 77% at 20%; generators on the fitting grid, which flatters recovery). | SIM-R1-C3/iter-3#H3;SIM-R1-C3/iter-4#H4;SIM-R1-C3/iter-5#H5;SIM-R1-C3/iter-5#H5r | New in Cycle 3. |
| C3-R1-08 | E | Supported | SIM-R1-C3's selected two-state setting was not robust: with 20% day-to-day load noise only 1 of 20 seeds kept the ratio in 8-12, and +-20% parameter changes moved it from 2.2 to 11.3 (both not supported); savings over three acclimation/decay cycles did occur (days to 95% re-induction 2, 1, 1) but trivially, because the slow state kept the gain above the first-cycle level after decay. | SIM-R1-C3/iter-6#H6;SIM-R1-C3/iter-7#H7;SIM-R1-C3/iter-8#H8;SIM-R1-C3/iter-8#H8r | New in Cycle 3. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-3 status |
|---|---|---|---|---|
| L01 | R1 Body → R6 Earth | relationship | P | Retained as analogy only. Daisyworld from published equations reproduces W01 and shows unbounded adaptation removes regulation; the body-side two-timescale memory is a different mechanism (learning), so the parallel is structural, not mechanistic. |
| L02 | R1 Body → R6 Earth | distinction | P | Under pressure but not rejected: X15 argues for selection among ecosystems/nutrient cycles (a proposal, not a demonstrated planetary-scale selection mechanism). |
| L03 | R1 Body → R6 Earth | humans within Earth | E | No Cycle-3 evidence targeted this link. |
| L04 | R1 Body → R2 Mind | dependency | P | No Cycle-3 evidence targeted this link. |
| L05 | R1 Body → R2 Mind | feedback loop | P | Strengthened modestly by a small systematic review (X20); remains Plausible. |
| L06 | R1 Body → R2 Mind | competing interpretation | PS | No Cycle-3 evidence targeted this link. |
| L14 | R4 Spirit → R1 Body | relationship | P | Retained Plausible. E-value ~2.0-2.35; a Swedish cohort's association disappears after adjusting for social participation, which cannot be read as confounding vs mediation from attenuation alone. |
| L15 | R4 Spirit → R1 Body | dependency | H | Remains Hypothetical: an extreme residual 'healthy attender' scenario alone could explain the association. |
| L17 | R5 Consciousness → R1 Body | dependency | E | Strengthened: full text of the original PCI paper and a rodent validation. |
| L25 | R1 Body → R2 Mind | relationship | P | New in Cycle 3. |
| L26 | R1 Body → R4 Spirit | relationship | H | New in Cycle 3. |

## Limitations
Toy loop in arbitrary units; nothing fitted to human data. Whole-day quantisation dominates the ratio metric. The savings metric is trivially satisfied. X08/X25/X20 are associations.

## Open questions and falsification
Would a continuous re-induction metric (time to 95%, interpolated) change the grid result? Do human decay series at several absence lengths decelerate as predicted? Falsification: decay that is a single exponential across 7–40 days would count against the two-state account.

## Conclusion and gate
Report 1 now has a concrete, falsifiable proposal for acclimation memory and an honest record that it does not robustly reproduce the anchor. Gate: **Indeterminate**.

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S01** — Billman GE (2020). Homeostasis: The Underappreciated and Far Too Often Ignored Central Organizing Principle of Physiology. Front Physiol 11:200. doi:10.3389/fphys.2020.00200 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/>
- **S02** — Modell H, Cliff W, Michael J, et al. (2015). A physiologist's view of homeostasis. Adv Physiol Educ 39(4):259-266. doi:10.1152/advan.00107.2015 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4669363/>
- **S03** — Shapiro L, Spaulding S (2021). Embodied Cognition. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/embodied-cognition/>
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/consciousness/>
- **S23** — Javaux EJ (2019). Challenges in evidencing the earliest traces of life. Nature 572:451-460. doi:10.1038/s41586-019-1436-4 [abstract only (NCBI E-utilities PMID 31435057)] <https://pubmed.ncbi.nlm.nih.gov/31435057/>
- **T01** — Sterling P (2012). Allostasis: a model of predictive regulation. Physiol Behav 106(1):5-15. doi:10.1016/j.physbeh.2011.06.004 [abstract only (NCBI E-utilities PMID 21684297)] <https://pubmed.ncbi.nlm.nih.gov/21684297/>
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 [full text (PMC6054486)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/>
- **U01** — OpenStax (2022). Anatomy and Physiology 2e, §12.1 Basic Structure and Function of the Nervous System. Rice University. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/12-1-basic-structure-and-function-of-the-nervous-system>
- **U02** — Marzvanyan A, Alhawaj AF (2019). Physiology, Sensory Receptors. StatPearls (UCL Discovery copy). [full text (PDF)] <https://www.ncbi.nlm.nih.gov/books/NBK539861/>
- **U03** — Osilla EV, Marsidi JL, Shumway KR, Sharma S (2023). Physiology, Temperature Regulation. StatPearls (PMID 29939615). [excerpt (NCBI E-utilities; Bookshelf page blocked by bot check)] <https://www.ncbi.nlm.nih.gov/books/NBK507838/>
- **U04** — OpenStax (2022). Anatomy and Physiology 2e, §1.2 Structural Organization of the Human Body. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body>
- **U05** — OpenStax (2022). Anatomy and Physiology 2e, §14.1 Sensory Perception. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception>
- **V06** — OpenStax, Anatomy and Physiology 2e, section 24.6 'Energy and Heat Balance' (CC BY) [full text (OpenStax web page)] <https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance>
- **V36** — Sender R, Fuchs S, Milo R (2016). Revised estimates for the number of human and bacteria cells in the body. PLoS Biol 14(8):e1002533. doi:10.1371/journal.pbio.1002533 [full text (Europe PMC PMC4991899)] <https://europepmc.org/article/PMC/PMC4991899>
- **W04** — Lim CL (2020). Fundamental Concepts of Human Thermoregulation and Adaptation to Heat: A Review in the Context of Global Warming. International journal of environmental research and public health 17:E7795. doi:10.3390/ijerph17217795 [full text (Europe PMC PMC7662600)] <https://europepmc.org/article/PMC/PMC7662600>
- **W05** — Daanen HAM, Racinais S, Périard JD (2018). Heat Acclimation Decay and Re-Induction: A Systematic Review and Meta-Analysis. Sports medicine (Auckland, N.Z.) 48:409-430. doi:10.1007/s40279-017-0808-x [full text (Europe PMC PMC5775394)] <https://europepmc.org/article/PMC/PMC5775394>
- **X08** — Holt-Lunstad J, Smith TB, Layton JB (2010). Social relationships and mortality risk: a meta-analytic review. PLoS medicine 7:e1000316. doi:10.1371/journal.pmed.1000316 [full text (Europe PMC PMC2910600)] <https://europepmc.org/article/PMC/PMC2910600>
- **X09** — Neal RA, Massey HC, Tipton MJ, Young JS, Corbett J (2016). Effect of Permissive Dehydration on Induction and Decay of Heat Acclimation, and Temperate Exercise Performance. Frontiers in physiology 7:564. doi:10.3389/fphys.2016.00564 [full text (Europe PMC PMC5120118)] <https://europepmc.org/article/PMC/PMC5120118>
- **X20** — Pinna T, Edwards DJ (2020). A Systematic Review of Associations Between Interoception, Vagal Tone, and Emotional Regulation: Potential Applications for Mental Health, Wellbeing, Psychological Flexibility, and Chronic Conditions. Frontiers in psychology 11:1792. doi:10.3389/fpsyg.2020.01792 [full text (Europe PMC PMC7419655)] <https://europepmc.org/article/PMC/PMC7419655>
- **X22** — Smith MA, Ghazizadeh A, Shadmehr R (2006). Interacting adaptive processes with different timescales underlie short-term motor learning. PLoS biology 4:e179. doi:10.1371/journal.pbio.0040179 [full text (Europe PMC PMC1463025)] <https://europepmc.org/article/PMC/PMC1463025>
- **X25** — Ribeiro AI, Amaro J, Lisi C, Fraga S (2018). Neighborhood Socioeconomic Deprivation and Allostatic Load: A Scoping Review. International journal of environmental research and public health 15:E1092. doi:10.3390/ijerph15061092 [full text (Europe PMC PMC6024893)] <https://europepmc.org/article/PMC/PMC6024893>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9) (2026-10-24): this version; details in `CHANGELOG.md`.
