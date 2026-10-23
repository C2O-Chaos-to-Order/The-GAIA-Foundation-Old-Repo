# Universal Framework — Research Integrity and Simulation Design Addendum
## Revision 0.9.0 — Audit of Research Passes 1–12 and Simulation Specifications 1–12

**Revision date:** 2026-10-23  
**Framework:** Seven-Report Foundational Framework  
**Status:** Research addendum filed; independent disciplinary review pending  
**Change type:** Source audit, evidential calibration, simulation-design corrections, cross-report synthesis  
**Risk level:** Low  
**Repositories affected:** `KyleAlexanderSteen/The-GAIA-Foundation`  
**Applies to:** Reports 1–7; intended to supplement rather than silently overwrite prior versioned reports  
**Execution status:** No simulation code executed; no numerical outputs generated; no empirical results newly produced  
**Implementation status:** No software or broader implementation authorized

## 1. Purpose and governing rule

This addendum integrates the twelve research passes and twelve proposed simulation designs supplied for the Universal Framework. It corrects overstatements, distinguishes primary research from critique or preprint, and makes the proposed tests more operational. It is not a claim that the twelve simulations have been executed or that the theories have been adjudicated.

The framework uses five evidence labels:

- **Established observation:** directly measured or documented within the scope of a cited study.
- **Model result:** follows from a specified model under its assumptions; it is not automatically a property of the real world.
- **Interpretation:** a proposed explanation of observations.
- **Metaphysical or theological commitment:** may be meaningful within a worldview but is not established by neural, geophysical, or systems-model evidence alone.
- **Unverified source/claim:** bibliographic details or substantive assertions not independently confirmed in this audit.

A paper's publication does not make every claim in it established fact. A simulation specification is a plan, not a result. A preprint or philosophical critique should not be described as a consensus finding.

## 2. High-priority source and wording corrections

### 2.1 COGITATE: report what the experiment tested, not a total verdict

The 2025 Nature adversarial collaboration included 256 participants across fMRI, MEG, and intracranial EEG. It found sustained posterior responses reflecting stimulus duration, no sustained synchronization within posterior cortex in the predicted IIT pattern, and no general prefrontal ignition at stimulus offset in the predicted GNWT pattern. The study also found content-specific synchronization between frontal and early visual areas. These results challenge specific predictions and biological implementations; they do not by themselves falsify every possible formulation of either theory. The published article explicitly distinguishes the theories' mathematical/computational cores from their biological implementations and acknowledges that the tested predictions overlap with other theories. [R1]

**Correction to the supplied interpretation:** describe COGITATE as a substantial challenge to specified predictions of IIT and GNWT, not as a definitive verdict on either theory. Stewart's “Conceded in Advance” is a critical philosophical argument about the design and interpretation, not the consortium's official verdict or a consensus conclusion. Present its claims as an attributed critique and pair them with the primary study. [R1, R2]

The October 2026 *Neuron* perspective “Have grand theories of consciousness earned their keep?” is a relevant current framing, but the exact quotation and bibliographic details should be verified against the article before quotation in a final publication. DOI: https://doi.org/10.1016/j.neuron.2026.08.020.

### 2.2 DOM and Prediction Ledger / MCI: treat as proposals until validated

The supplied Developmental Operator Model (DOM), Prediction Ledger, and Measure Centrality Index 2.0 are potentially useful comparison frameworks. Their status must remain **proposed framework / source-specific argument** until their exact source records, methods, operational definitions, and independent reception are verified. Do not call DOM an established third theory or say it explains the COGITATE results as a fact. State that it *proposes* six organizational operators and reports five falsifiable predictions, pending independent evaluation.

The ledger should require, for each prediction: (1) a dated theory version; (2) a source quote or formal derivation; (3) core-versus-implementation/import classification; (4) operational measure; (5) rival predictions; (6) power/sensitivity analysis; (7) pre-registered pass/fail/indeterminate criteria; (8) permitted post-result revisions; and (9) a public record of all deviations. A “measure centrality” score should not be assigned until its rubric, scale, inter-rater reliability, and worked examples are published and tested. A measure's reach describes the scope of a potential failure; it does not establish theory truth.

### 2.3 IIT Φ: do not collapse a construct critique into a settled verdict

The statement that Φ is not well-defined for real physical systems and has never been computed for any real physical system is too categorical without specifying which version of IIT, which formalism, what system boundary, and what is meant by “computed.” The defensible wording is:

> Exact Φ-style quantities can be computationally intractable or underdetermined for realistic systems, and many empirical studies use proxies or related measures. The construct validity of any proxy must be evaluated separately; a proxy is not automatically Φ, and neither Φ nor a proxy score should be equated directly with the amount of consciousness.

Simulation 2 can audit proxy validity, but “no proxy passes” would challenge the current operationalization of that proxy family, not by itself falsify IIT's entire metaphysical or causal framework. The proposed five criteria also mix psychometric construct validity, mechanistic validity, scale behavior, and causal intervention. Score them as separate dimensions, not as a single pass/fail test without a pre-specified weighting rule.

### 2.4 Earth system: correct the boundary count and preserve causal distinctions

The Planetary Health Check 2025 reported **seven of nine** planetary boundaries transgressed; the 2026 edition also reports **seven of nine**. Thus “six in 2025, seven in 2026” is not supported by the cited Planetary Health Check reports and should be removed unless it explicitly refers to a different assessment or method. [R3]

The Planetary Boundaries framework documents coupled Earth-system pressures and risk; it does not, by itself, demonstrate a specific cascade sequence, planetary agency, or active inference. A model that reproduces seven boundary transgressions after tuning parameters to those same observations is not independently validated. Calibrate against one subset/time period and test on held-out data or independent scenarios.

### 2.5 Geodynamo and CMG mode: model-based mechanism, not confirmed observed mode

Aubert's long-duration geodynamo simulation is a numerical model result constrained by physical parameters and compared with geomagnetic/geodetic observations; “excellent quantitative agreement” should be attributed to that paper and bounded by its model assumptions. The proposed CMG mode is described by Dumberry as a new dynamical mode with a predicted 40–100-year period and potentially low quality factor, (Q<1), for short inner-core viscous-relaxation times. It is a theoretical geophysical mode, not a confirmed 40–100-year observed spectral peak. [R4, R5]

Simulation 4 must not assume a unique peak is already expected in observed length-of-day (LOD) data. Use a null model and compare out-of-sample spectral predictions, confounds, and uncertainty in torque, viscosity, and forcing. If (Q<1), the mode may be broad and weak rather than a stable narrow resonance. The specified torque ranges and viscosity ranges need direct source justification and dimensional checks before use.

### 2.6 Active inference and planetary “agency”

Rubin et al. present a proof-of-concept model in which a simplified biosphere–climate system behaves as if it performs active inference and maintains climate trajectories within specified bounds. This supports a model-level interpretation under stated assumptions; it does not establish phenomenal experience, conscious intention, or a planetary soul. [R6]

The phrase “removing the Markov blanket (sparsity → 0)” is mathematically ambiguous and likely reversed. In a Gaussian graphical model, conditional-independence structure is encoded by zeros in the precision matrix; **sparsity** usually means a larger proportion of zero entries, not fewer. Define the graph and its edges explicitly. Compare (a) a correctly specified sparse conditional-independence structure, (b) a misspecified/dense structure, and (c) a no-blanket baseline. Do not infer that setting a scalar “sparsity” parameter to zero removes the blanket unless the parameter is defined that way in code.

Also separate two outcomes: (i) the model's inference interpretation fits its dynamics; (ii) the system remains within a chosen homeorhetic region. A failure of regulation is not necessarily a failure of inference, and a model's statistical factorization is not evidence of a subject.

### 2.7 Neurotheology: correct scope and retain the correction notice

Husain et al. report a systematic review of 105 studies across eight traditions and seven neuroimaging/neurophysiological modalities, with heterogeneous evidence synthesized narratively rather than by meta-analysis. The authors report practice-associated neural signatures, but repeated activation of a region does not imply the same function across practices, and the evidence does not adjudicate theological truth. [R7]

A published correction removes a misleading AI-generated anatomical figure and related passages; the authors state that the correction does not affect study selection, data extraction, analysis, conclusions, or overall scientific validity. Cite the review and its correction together when discussing the review in detail. [R7, R8]

Avoid treating “meditation shows DMN suppression,” “prayer engages social cognition,” or “chanting deactivates limbic regions” as universal signatures. Use “reported tendencies in the reviewed studies,” note practice/task/population heterogeneity, and distinguish acute functional changes from long-term structural differences.

### 2.8 Soul hypothesis: formalize comparison without pretending likelihoods are known

The Bayesian relation is:

[
\frac{P(H_S\mid O)}{P(H_B\mid O)}
=
\frac{P(O\mid H_S)}{P(O\mid H_B)}
\times
\frac{P(H_S)}{P(H_B)}.
]

The likelihood ratio Λ is meaningful only when both hypotheses and the observation are specified well enough to assign defensible likelihoods. In most proposed examples (near-death experiences, anomalous information acquisition, neural dependence), reliable numerical likelihoods are not currently supplied by the framework. Therefore, Simulation 7 is currently a **qualitative hypothesis-discrimination protocol**, not a calculable likelihood-ratio model.

Before calling an observation soul-specific, specify the best competing brain-dependent models, prospective blinding, independent corroboration, expected base rates, sensory leakage controls, selection effects, and replication criteria. “Not explained yet” is not equivalent to “more expected under a separable soul.” Conversely, the lack of such evidence is not a logical proof that no soul exists.

### 2.9 Embodied learning and two-route prioritization

The likelihood-precision versus preference-reweighting distinction is a useful model hypothesis. The cited Grimbly et al. item is an arXiv preprint (arXiv:2610.18617), so its results should be labelled preliminary until peer-reviewed and independently replicated. [R9]

The equations need dimensional and identifiability checks. Normalize γ and ρ or estimate them on a common scale before combining them; otherwise α does not have a stable interpretation as a route weight. Use factorial manipulations (precision only, preference only, both, neither), held-out task layouts, and separate outcomes for survival, discrimination accuracy, policy preference, and model-learning coverage. A survival advantage alone does not establish the proposed learning mechanism.

### 2.10 Autopoietic enactivism and whole-cell simulation

The claim that only autopoietic/autonomist enactivism truly challenges all core tenets of mainstream cognitive science is a philosophical thesis, not a settled empirical finding. Attribute it to the named critical analysis and compare with alternative interpretations of 4E cognition. Do not equate “constitutive embodiment” with proof that all cognition is reducible to bodily physiology.

The cited whole-cell modeling claim needs a verified primary bibliographic record before it is used as a core evidence item. The current source check did not independently confirm the exact citation “Thornburg et al., Cell, April 2026, Bringing the genetically minimal cell to life on a computer in 4D.” Keep it marked **source verification pending** until the DOI or publisher record is located. Even if verified, a whole-cell model of JCVI-syn3A constrains claims about cellular processes in that minimal bacterium; it does not establish a “minimal substrate” for human mind or consciousness.

### 2.11 AI substrate neutrality and Orch-OR

A substrate-neutrality audit can reveal hidden biological assumptions, but its outcome depends on the selected definitions of architecture, exemplar, and exclusion. A matrix rating GNWT or Predictive Processing as “neutral” is an argument to test, not a settled classification. The Exclusion Test does not prove AI consciousness; it tests consistency of the criteria used to include or exclude systems.

Orch-OR and Self-Aware Networks should be compared symmetrically, with each theory's proponents' strongest formalized claims, shared predictions, and unique predictions. A failure to detect quantum coherence is informative only if the measurement sensitivity and physiological conditions are sufficient for the particular coherence claim being tested. Likewise, detecting coherence would not establish consciousness. The specific ∼10⁴ Hz claim, measurement target, and proposed link to objective reduction require source-level verification and operational definition before preregistration. Avoid claiming that a single null result falsifies every version of Orch-OR.

## 3. Simulation-specification corrections

All twelve specifications remain **design proposals**, not executed simulations. The following changes are required before implementation or preregistration.

1. **DOM prediction discrimination:** provide the full five DOM predictions verbatim from a verifiable source and map each to a unique operational measure. A visual masking study alone cannot identify a cortical “operator” unless each operator has independently justified indicators. TMS, lesion evidence, MEG, and intracranial EEG have different spatial, temporal, safety, and sampling constraints; do not present them as interchangeable interventions. Do not induce or seek focal lesions as an experimental manipulation.

2. **IIT proxy construct validity:** define the target construct and each proxy precisely. Separate convergent validity, discriminant validity, mechanistic correspondence, scale dependence, and intervention evidence. An intervention that changes a proxy but not a report may be confounded; phenomenal consciousness itself is not directly observable by a simple intervention criterion. State what result would count as inconclusive.

3. **Prediction Ledger / MCI:** publish a scoring rubric before scoring any theory. Record the theory's version, prediction provenance, measure sensitivity, rival overlap, analysis deviations, and an indeterminate category. Avoid assigning theory “credit” by a subjective score that combines core status and empirical success without validated weights. Treat the application to COGITATE as one critical reanalysis, not an official replacement for the paper's own verdict.

4. **CMG mode:** derive equations with consistent torque signs and units, document inertias and boundary conditions, and use parameter priors grounded in the cited literature. Include electromagnetic-only, gravitational-only, and combined models; fit one interval and predict another. A broad low-Q feature is not equivalent to a narrow spectral peak.

5. **Planetary active inference:** specify the state-space equations, units, noise, boundary conditions, and operational homeorhesis measure. Make Markov-blanket conditional independencies explicit in a graph or precision matrix. Compare with non-inference control models and test on held-out forcing trajectories. Do not define model success solely as reproducing the same outcomes used to tune it.

6. **Practice-specific neuroplasticity:** the supplied Hebbian equation is too generic to reproduce named network-level findings without a defined network, input vectors, observation model, and mappings between latent connectivity and measurable fMRI/EEG outcomes. Treat the proposed γ parameter as a model assumption, not a demonstrated biological practice-specificity coefficient. Validate on independent datasets and avoid causal claims from cross-sectional practitioner differences.

7. **Soul-specific evidence:** retain qualitative likelihood-ratio logic until empirical likelihoods can be estimated. Predefine what constitutes veridical perception, prospective timing, independent corroboration, and replication. Include sensory leakage, memory reconstruction, base-rate, and publication-bias controls. Do not insert numerical Λ values without data.

8. **IELF arbitration:** normalize route variables and predefine parameter identifiability. Compare a combined model against precision-only, preference-only, reinforcement-learning-only, predictive-processing-only, and baseline models using held-out predictions. Report calibration and uncertainty as well as survival.

9. **AI Substrate Audit:** apply criteria to a representative set of biological and non-biological systems without using “biological” as a proxy for “conscious.” Separate a theory's logical capacity to apply to AI from empirical evidence that a specific AI meets its conditions. Include undecided/ambiguous verdicts.

10. **Whole-cell model:** first verify the paper, model code, dataset, validation targets, and scope. A “doubling time more than 2× off” criterion is too permissive for a claimed validation test and is not a substitute for target-specific error bounds. Use the source's own uncertainty intervals and held-out validation data. Do not infer human cognition from a minimal bacterial cell model.

11. **Orch-OR vs. SAN:** define the exact observable and minimum detectable effect for each scale; pre-register positive and negative controls. A non-detection can challenge a specified coherence model only if sensitivity was adequate. Theories may share gamma synchrony or behavioral predictions without one uniquely explaining them. Define the decision rule for “indistinguishable” rather than treating it as proof that the theories are identical.

12. **Earth-system cascades:** estimate coupling and threshold parameters independently where possible, quantify uncertainty, and compare full, sparse, and modular networks against a null model. Do not require the model to reproduce “seven boundaries breached” if that count is already used for fitting. Use historical calibration plus held-out periods or alternative forcing scenarios. Test whether homeorhesis failure follows from the model independently of the boundary count, not by definition.

## 4. Cross-report disposition

| Report | Research addition | Defensible conclusion | Remaining limit |
|---|---|---|---|
| **1 — Body** | Autopoietic enactivism; whole-cell modeling as a possible biological constraint | Bodily regulation and sensorimotor interaction are central to many biological and cognitive processes | The exact whole-cell citation needs verification; embodiment is not one unitary claim |
| **2 — Mind** | Two-route interoceptive prioritization; IELF arbitration | Precision and preference can be modeled as distinct routes and tested factorially | Current gridworld evidence is preliminary; equations and scales require normalization |
| **3 — Soul** | Comparative burden and likelihood-ratio framework | A separable-soul hypothesis needs observations more expected under it than under strong rivals to gain empirical preference | Numerical likelihoods are not currently established; logical possibility is not empirical confirmation |
| **4 — Spirit** | Practice-specific neural correlates and neuroplasticity | Religious/spiritual practices are associated with measurable neural and physiological changes in studied contexts | Neural correlates do not determine theological truth; review is heterogeneous and has a correction notice |
| **5 — Consciousness** | Multi-theory comparison; DOM; ledger/MCI; Φ proxy audit; AI substrate audit; Orch-OR/SAN | COGITATE challenges specified IIT/GNWT predictions; theory comparison needs pre-registered reach and falsifiers | DOM/MCI source status requires checking; no single test settles phenomenal consciousness or AI consciousness |
| **6 — Earth** | Millennium-scale geodynamo modeling; proposed CMG mode; active inference; planetary boundaries | Earth systems are coupled; geodynamo and climate models provide testable mechanism-level hypotheses | CMG is proposed, not confirmed as an observed mode; planetary dynamics do not prove agency or soul |
| **7 — Unified Framework** | Twelve proposed simulation designs and cross-report regression rules | The framework can make its claims more auditable by separating mechanisms, models, interpretations, and metaphysical commitments | No simulations executed; independent review and numerical validation pending |

## 5. Regression rules to add

- A challenged implementation prediction is not automatically a falsification of every version of the underlying theory.
- A philosophical critique of an experiment is not the experiment's official verdict.
- A theory's core/import classification must be documented before outcomes are known.
- A high proxy score is not equivalent to high consciousness or a direct measurement of Φ.
- A Markov blanket is a statistical/organizational construct, not by itself a subject.
- A predicted 40–100-year mode is not a confirmed observed oscillation or a biological heartbeat.
- Practice-specific neural correlates do not settle metaphysical or theological claims.
- “Not yet explained” is not equivalent to “more likely under a soul hypothesis.”
- Substrate-neutral criteria do not prove that any AI is conscious.
- A whole-cell model of a minimal bacterium does not explain the human body–mind.
- A model fitted to the planetary-boundary count cannot independently validate that same count.
- A model design is not a simulation run; a simulation run is not external validation.
- Numerical likelihood ratios, MCI scores, parameter estimates, and pass/fail claims must not be invented or implied without data.

## 6. Source register

**R1.** Cogitate Consortium et al. (2025). “Adversarial testing of global neuronal workspace and integrated information theories of consciousness.” *Nature*. https://doi.org/10.1038/s41586-025-08888-1. Primary empirical comparison; 256 participants, fMRI/MEG/iEEG.

**R2.** Arthur Stewart (2026). “Conceded in Advance: How Cogitate Disabled Its Own Verdict.” Critical philosophical manuscript. https://philarchive.org/browse/falsification/. Use as an attributed critique, not as the study's official conclusion.

**R3.** Planetary Health Check (2025, 2026). Official annual assessments. https://www.planetaryhealthcheck.org/ and https://www.planetaryhealthcheck.org/downloads/. Both cited editions report seven of nine boundaries transgressed.

**R4.** Aubert (2026). “Geodynamo simulations spanning millennia in the physical conditions of Earth’s core.” *Journal of Studies of Earth’s Deep Interior*. https://doi.org/10.46298/jsedi.17790. Model result; interpretation remains conditional on model and comparison methods.

**R5.** Mathieu Dumberry (2026). “The core-mantle mode of gravitational oscillation.” *Journal of Studies of Earth’s Deep Interior*. https://doi.org/10.46298/jsedi.17576. Proposed 40–100-year mode and conditional low-Q estimate.

**R6.** Rubin, S. et al. (2026). “An elementary form of agency at planetary-scale.” *Scientific Reports*. https://doi.org/10.1038/s41598-026-61878-9. Proof-of-concept model; does not establish phenomenal planetary experience.

**R7.** Husain, W. et al. (2026). “The Neuroscience of Religious and Spiritual Practices: A Systematic Review of Neurotheological Evidence.” *Brain and Behavior* 16(9), e71733. https://doi.org/10.1002/brb3.71733. Narrative synthesis of 105 heterogeneous studies.

**R8.** Correction to Husain et al. (2026). *Brain and Behavior* 16(9), e71785. https://doi.org/10.1002/brb3.71785. Removes a misleading AI-generated anatomical figure and related passages; authors report no impact on results or conclusions.

**R9.** Grimbly et al. (2026). “Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference.” arXiv:2610.18617. https://arxiv.org/abs/2610.18617. Preprint; label its results preliminary.

**R10.** Owen & Goodale (2026). “Have grand theories of consciousness earned their keep?” *Neuron*. https://doi.org/10.1016/j.neuron.2026.08.020. Verify exact wording and quotations against the article before reproducing them.

**R11.** Abbatecola et al. (2026). “Protocol for IIT vs. Predictive Processing.” *PLOS ONE*. https://doi.org/10.1371/journal.pone.0340593. Protocol, not completed outcome evidence.

**R12.** Corcoran et al. (2026). “Integrated information and predictive processing theories of consciousness: An adversarial collaborative review.” *Neuroscience & Biobehavioral Reviews* 187, 106742. https://doi.org/10.1016/j.neubiorev.2026.106742. Review/comparison of frameworks, not a final adjudication.

**Source verification pending:** the exact bibliographic record for Dias's DOM source; the source records for Ziv-el's Prediction Ledger, Chis-Ciure's MCI 2.0, Stilwell's soul comparison, Mendes's 4E analysis, Thornburg et al.'s claimed 2026 whole-cell paper, the substrate-agnostic AI framework, Arıcı's Substrate Audit, and the Orch-OR/SAN comparison. Keep these items attributed and provisional until each exact record, publication status, and relevant methods are independently verified.

## 7. Readiness and next gate

- **Document delivery:** this research-integrity addendum is filed.
- **Source status:** primary sources for COGITATE, planetary boundaries, Dumberry, Rubin, and the neurotheology review/correction were verified during this pass; several supplied framework manuscripts and the whole-cell citation remain to be verified at source level.
- **Independent review:** pending.
- **Simulation execution:** not performed.
- **Numerical validation:** pending.
- **Code/implementation:** not authorized.
- **Repository changes:** this addendum only; no previous file was overwritten, moved, or deleted.

The governing conclusion is restrained but constructive: the Universal Framework is more testable when it explicitly separates empirical findings, model-dependent predictions, philosophical arguments, and spiritual interpretations. The next step is not to claim twelve successful simulations, but to verify remaining source records and convert each proposed simulation into a versioned, executable, preregistered protocol with independent validation criteria.
