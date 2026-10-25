# SYNTHESIS — six phase reports across six fields of knowledge

Status: **Proposed; gate INDETERMINATE (independent review pending).** Written 2026-10-25 on `research/phase-synthesis`, stacked on `research/phase-transcendence-x12` @ 3ae9bf57, as `PLAN.md` §7 (amended by §9) asks: one cross-phase, cross-field synthesis after Transcendence x12.

**What this document is.** A reading of what is already in the repository: the 30 cycle ledgers (six phases x Baseline, x3, x6, x9, x12), 1,116 simulation records, the research passes, the source and link registers and Maps v38. It reads no new source, runs no new model of the world and adds **no new claim**: every substantive statement points to an existing claim (ID with its ledger label in brackets), link (`PL-nn` with its label), source (`Pnn`) or record. Method, pre-registered checks and limits: `Synthesis/SPEC.md`; aggregation, rendering and checks: `Synthesis/tools/synth.py`; numbers: `Synthesis/data/`; check results: `Synthesis/EXECUTION_RECORD.json`. Labels are the Seven-Report framework's four: Established, Plausible, Philosophical/Spiritual, Hypothetical. Indeterminate is never Pass.

## 1. What was done (all six phases)
Each phase ran the plan's five cycles in all six fields: 31 research passes and 31 simulation iterations per field, 186 runs per phase, **1,116 runs** in all, every SPEC written before its run and every run re-executed identically in its cycle's verification. Totals per cycle, recomputed from the ledgers, EXECUTION_RECORDs and PASSES.md files (`data/cycle_totals.csv`):

{{TABLE:cycle_totals}}

Validation checks passed 1,176 of 1,182 times; the six failures are in Divergence (one in DV0, two in DVC) and Allegiance (one in ALB, two in ALC), all reported in their cycles and none since ALC. Pre-registered hypotheses were supported 1,456 times and not supported 333 times (0.81); no hypothesis result was recorded as anything else. "Not supported" results are findings, kept in the ledgers, not failures to be hidden.

Final (x12) ledgers hold **512 claims** (Divergence 132, Insurgence 89, Allegiance 88, Convergence 80, Ascendence 60, Transcendence 63). Across all 30 ledgers 936 of 1,498 claim rows are of class Simulation: most of what the track established is about the agent's own models and recomputations, not new facts about the world.

## 2. How the phases connect
### 2.1 The explicit phase-relation links
Each phase's Baseline recorded one link of type "phase relation" to an earlier phase; Divergence has the framework link PL-05 [Philosophical/Spiritual]. All six phase relations are labelled **Hypothetical**, so no phase-to-phase relation in the track is more than a hypothesis (`data/phase_links.csv`):

{{TABLE:phase_links}}

Read together, the links do not form one sequence. They describe a threshold shared by splitting and rising (PL-22 [Hypothetical]), resistance to or joining of an uprising by loyal groups (PL-33 [Hypothetical]), convergence as the reverse of divergence on the same objects (PL-50 [Hypothetical]), loyalty and convergence of inquiry as rivals in one text (PL-53 [Hypothetical]), ascent as convergence seen from the objective (PL-64 [Hypothetical]) and transcendence as moving the feasible set rather than climbing within it (PL-76 [Hypothetical]). That is a web of pairwise contrasts, each resting on Baseline toys or one text. README §12 Q4 (fixed sequence, recurring states, or something else) therefore stays **open**: nothing in the ledgers supports a fixed order, and the links were written by the agent at each Baseline, so their existence reflects the plan's order of work, not evidence of an order in the world.

### 2.2 Threads that recur across phases
Three threads appear in several phases. They are method or formal parallels, labelled as such in the link register; none shows that the phases share a mechanism.

- **Thresholds and multiplication.** Sensitive dependence and solver instability share one mechanism, a factor of magnitude above one applied each step (PL-11 [Established]; basis DVB-APP-11 [Plausible], DVB-FOR-12 [Plausible]). The giant-component equation of a random graph is the survival equation of a branching outbreak (PL-20 [Plausible]; IN0-FOR-01 [Established]), and abrupt onset at a critical connection probability recurs in percolation and simple contagion (PL-29 [Plausible]; IND-FOR-11 [Established], IND-SOC-15 [Plausible]). In Ascendence, where an ascent ends depends on where it starts (PL-67 [Hypothetical]) and a minority variant rises only above a start-share threshold (PL-72 [Hypothetical]). Transcendence's formal reading has the same shape: what separates Liouville numbers is super-linear lookahead, a long-run rate (PL-73 [Established]), and in TRD that rate proved to depend on the base (TRD-FOR-06 [Established], TRD-FOR-08 [Plausible]).
- **Convergence of chains, ascent by gradients.** The strongest cross-field results in the track are mathematical: P74's null model of molecular convergence is the same object as P73's regular Markov chains (PL-51 [Established]), P78's mixing time measures how long that null chain needs (PL-54 [Established]; CVB-FOR-08 [Established]), and adaptive walks are discrete hill climbing toward the optimum that a contracting gradient flow reaches (PL-61 [Established]; ASD-FOR-01 [Established]).
- **Printed numbers need recomputing.** From Allegiance on, the cheapest and most productive method was to recompute a source's statistics from its own printed summaries (PL-35 [Plausible], PL-36 [Plausible], PL-40 [Plausible]). It found a transposed table in P52 (ALD-SOC-07 [Plausible]), headline numbers in P87 and P88 that need care (PL-62 [Plausible]; ASD-SOC-02 [Established], ASD-APP-02 [Established]), and slips in every audited self-transcendence study (PL-74 [Plausible], PL-77 [Established]; TRD-APP-04 [Established], TRD-APP-11 [Established]). The same method showed that researcher allegiance can reach a meta-analysis (PL-44 [Plausible]; ALD-SOC-14 [Plausible], ALD-APP-13 [Plausible]) and that small studies cannot give strong evidence at moderate t while large samples make p near .05 weak evidence (PL-80 [Established], PL-83 [Plausible]; TRD-HUM-05 [Established], TRD-HUM-07 [Established]). This is the track's most transferable result, and it concerns the reliability of sources rather than any phase.

### 2.3 One topic that crosses three phases: mystical experience
The question whether experiences across traditions share a "common core" runs from Convergence (perennialism, P81; chanting survey, P83; critique of measures, P84) to Transcendence (P102, P105, P107, P108). Reports agree across traditions in P83 (CVD-PHI-09 [Plausible]), but its null across traditions had low power (CVD-PHI-12 [Established]), and an instrument that measures only some dimensions can miss differences (CVD-PHI-14 [Hypothetical]; PL-59 [Hypothetical]). Contact can produce similarity that mimics common origin (PL-57 [Hypothetical]). In Transcendence the dispute is stated (TRD-PHI-01 [Philosophical/Spiritual]), the measures are argued to descend from Stace's common-core view (TRD-PHI-04 [Philosophical/Spiritual]), P107's universality reading goes beyond its configural evidence (TRD-PHI-06 [Plausible]) and a factor pattern shared across countries is a property of measures (PL-81 [Hypothetical]). The empirical part that did hold is narrower: ego-dissolution is graded with dose in a laboratory meta-regression and a retrospective survey (PL-84 [Plausible]; TRD-PHI-08 [Plausible]). The toys say what would distinguish the readings (TRD-PHI-09 [Hypothetical]); no source in the track settles the dispute.

### 2.4 Competing definitions
Every phase kept a `DEFINITIONS.md` with one working reading per field and its rivals. The readings are this track's choices: no repository document defines the phases, and the same word names different things in different fields (for Transcendence: transitions in individuality, transcendental numbers, self-transcendence values and scales, the sublime, mystical experience). A shared word is not a shared mechanism (Phases `README.md`, Honest scope), and the synthesis finds no claim that would license treating any phase as one phenomenon across fields.

## 3. Where the evidence is strong and where it is thin
Per phase and field in the x12 ledgers (`data/field_footprint.csv`):

{{TABLE:field_footprint}}

Across the six phases (`data/field_track.csv`):

{{TABLE:field_track}}

**Strong.** The Formal-Sciences ledgers of Convergence (15 of 15 Established), Ascendence (10 of 10) and Transcendence (8 of 9) rest on mathematics that the runs reproduce exactly or to stated tolerance (CVD-FOR-02 [Established], CVD-FOR-08 [Established], ASD-FOR-03 [Established], TRD-FOR-06 [Established]). The recomputation audits in Social, Applied and Humanities are Established where they rest only on a source's printed numbers (TRD-APP-04 [Established], TRD-HUM-06 [Established]). Empirical claims from large primary studies stand as their sources report them (DVD-NAT-01 [Established]; DVD-PHI-05 [Established], 640,110 respondents in 117 countries).

**Thin.**
- **Philosophy-Spirituality.** PHI has the most source IDs (22) and the lowest Simulation share (0.55), but per phase it rests on one to five sources, and the sources are narrow: 10 of the 22 are encyclopedia entries (mostly the Stanford Encyclopedia; one Wikipedia article, P81), two pairs are the same work registered twice (P51 and P59, Kleinig's "Loyalty"; P84 and P105, Mosurinjohn et al. 2023), and the only primary texts are Peirce (P75) and Ruth in the KJV (P67). Ascendence PHI rests on a single source (P90) and has no Established or Plausible claim (ASD-PHI-01 [Philosophical/Spiritual]; ASD-PHI-02 [Hypothetical] and seven more toys); Allegiance PHI likewise has none (Maps v38 flags both cells UNDER-RESEARCHED). The unresolved lists repeat the same gap: no second non-Western tradition (DVD), no non-Abrahamic primary text (ALD), no Neoplatonic or non-Platonic ascent source (ASD), Stace, Katz, Forman and Taves not read (TRD). Interpretive claims are labelled Philosophical/Spiritual and are not evidence (DVD-PHI-03 [Philosophical/Spiritual], IND-PHI-08 [Philosophical/Spiritual], ALD-PHI-12 [Philosophical/Spiritual]).
- **Single-source fields.** In the later phases many fields rest on one or two sources: Convergence SOC on P69 alone, Ascendence FOR on P86, Transcendence FOR on P98 and HUM on P101. Claims there are as good as one reading of one source plus the agent's runs.
- **Toys.** 145 of 1,498 claim rows are Hypothetical, nearly all agent-built toys (instrument, ladder, exit-voice, copying). They show what a model does, not what the world does (ASD-PHI-02 [Hypothetical], TRD-PHI-09 [Hypothetical]).
- **Foreknowledge.** Ascendence x12 and all Transcendence cycles smoke-tested every configuration before its SPEC (disclosed in each cycle), and many runs are replications by design. Their high support rates (0.83 and 0.87) therefore measure consistency, not predictive success.
- **Links above their basis.** Seven of 84 links carry a label stronger than their weakest cited claim (PL-06 [Established], PL-11 [Established], PL-42 [Plausible], PL-51 [Established], PL-54 [Established], PL-61 [Established], PL-73 [Established]; `data/registry_checks.json`). For PL-51 [Established], PL-54 [Established], PL-61 [Established] and PL-73 [Established] the link states a mathematical identity that can be stronger than an empirical premise; the others should be reviewed.

## 4. The owner's level-to-phase pattern (Hypothetical)
The owner (Kyle Alexander Steen) states a pattern mapping upgrade levels to phases: **Base = Divergence, Meta (Metaphysical) = Insurgence, Super (Superphysical) = Allegiance, Hyper (Hyperphysical) = Convergence, Ultra (Ultraphysical) = Ascendence, Magic = Transcendence** (recorded in each phase README and DEFINITIONS file; `PLAN.md` §9). Label: **Hypothetical (owner's claim)**. It was not tested by any cycle, no ledger claim depends on it, and the methods were not changed by it. The synthesis cannot test it either: no ledger defines "Metaphysical", "Superphysical", "Hyperphysical", "Ultraphysical" or "Magic" operationally, and README §11 requires definitions and disconfirmation criteria before a mapping can be evaluated. What the ledgers can say is limited to the observation in §2.1: the phase-relation links are pairwise and Hypothetical, so they neither support nor contradict a ladder.

**Quantum: role unconfirmed.** The owner has named Quantum as a further level after Magic. The repository records no phase, level, axis value or definition for it, and the README warns against reading ordinary coupling as physical quantum entanglement. Whether Quantum is a seventh phase, a level applied across all six phases, or a separate report series is **not confirmed** and is listed as an owner decision (§7). Nothing here assigns it a role.

## 5. Saturation across phases
- **New sources fall in every phase.** Baselines added three to nine sources; x12 cycles added one to four (DV 1, IN 3, AL 4, CV 2, AS 1, TR 1). Divergence added the most sources (23) and Ascendence and Transcendence the fewest (12 each).
- **Most passes read nothing new.** At x12, 65 to 71 of 72 passes per phase recorded "Read: nothing new". The track as a whole read something new in 138 of 1,116 passes.
- **"Added nothing" was not recorded consistently.** Divergence to Convergence marked a pass that read nothing and only ran a replication as "Added nothing" (DVD 71 of 72); Ascendence and Transcendence credited such passes with the claim the run produced, so they report 0 empty passes. The two conventions are not comparable; the "Read: nothing new" column is the comparable measure.
- **Claims grow by carrying.** x12 ledgers are mostly carried claims (TRD: 50 carried, 13 new). Divergence x12 says returns are strongly diminishing and recommends closing the phase or targeting the listed gaps; Convergence x12 says FOR, APP and two PHI lines are saturated on their sources; Insurgence and Allegiance say the same of most fields.
- **Reading.** On their current sources all six phases are saturated: further cycles of the same design would mostly replicate. New primary sources aimed at the listed gaps, not more cycles, are what the ledgers ask for.

## 6. The matrix: what the Phase axis adds to the 625 grid (README §12 Q6, §10)
Maps v38 places all 512 x12 phase-track claims on the Phase axis, by report scope (an organisational placement, not evidence that a claim instantiates a phase). Claims per phase and field (E/P/PS/H; † = flagged UNDER-RESEARCHED, no E/P claim):

{{TABLE:phase_field}}

Claims per phase and lens (Maps v38 lens rules):

{{TABLE:phase_lens}}

- **No cell is populated by placement.** No phase-track claim has an Alchemy mode (the Alchemy axis is undefined), so none is placed exactly in any of the 625 intersections; 550 are UNPLACED, 50 UNDER-RESEARCHED and 25 EMPTY. Only 2 of 512 phase claims sit on the Being axis, CVD-PHI-06 [Philosophical/Spiritual] (Spirit) and CVD-PHI-09 [Plausible] (Consciousness).
- **Justice is empty.** The Justice lens has 6 claims in Divergence and none in the other five phases.
- **Answer to Q6 on present evidence.** The Phase axis organises 512 claims and shows where they are thin, which is useful; it does not yet add populated intersections, because Alchemy is undefined and phase placement is by report scope.
- **README §10 arithmetic** recomputes exactly (`data/arithmetic.json`): M = a b^T + 1 with a = (0, 1, 3, 5, 0), b = (3, 6, 9, 12) gives the printed 5 x 4 table; 5^4 = 625 and 5 x 5 x 6 x 5 = 750 (125 added cells). The later pattern does **not** reproduce as SPEC check V3 read it: the element-wise product A * B * C is (0, 18, 90, 252, 0), and multiplying by D = 1 leaves it unchanged; the all-zero vector README §10 reports follows only if the scalar is E = 0. README does not say which scalar it means, so V3 is recorded as Fail and the ambiguity is carried (§8). The outer-product arithmetic holds; the semantics stay open. The vector a has five entries, and README §10 says not to add a weight silently, so a six-phase reading of a needs an owner definition.
- **Transcendence** is recorded only in the overlay files (`phase_track_transcendence_*.csv`), and all 125 overlay cells are marked pending; none has a phase claim in its projection.

## 7. Open owner decisions
1. **Matrix 625 -> 750.** Approve or decline re-dimensioning the canonical matrix to six phases (5 x 5 x 6 x 5 = 750). Until then the canonical files keep five phases and Transcendence stays in overlay files. If approved, also define whether README §10's vector a gains a sixth value, and what that value means.
2. **Quantum.** Confirm Quantum's role: a seventh phase, a level applied across the six phases, or a separate series. Give it an operational definition that keeps it distinct from physical quantum entanglement (README §9.2).
3. **Reviewers.** Name independent reviewers, at least one per domain plus an ethics reviewer (GOVERNANCE audit UR-L3-04, UR-L4-02). Every phase cycle gate, and this synthesis, stays INDETERMINATE until review records exist in `Research/Reviews/`.
4. **Source register hygiene.** Allow a correction cycle to mark P59 as a duplicate of P51 and P105 as a duplicate of P84. This synthesis does not edit registers (SPEC check C4).
5. **Next work.** Choose between closing the phases as saturated and a targeted source cycle aimed at the gaps (§3, §8).
6. **Level definitions.** If the level-to-phase pattern is to be tested, give operational definitions of Meta, Super, Hyper, Ultra and Magic and say what would disconfirm the mapping (README §11).

## 8. Carried issues
Unresolved at x12, per phase (from each x12 report's unresolved list; abbreviated):
- **Divergence:** speciation literature beyond P01/P02 not read; divergence in visual art and literature unsourced; no second non-Western tradition; P19's 1870 ratio unexplained; P24 is a single-author methods proposal with fictive examples.
- **Insurgence:** nucleation kinetics unsourced (one planned source never read, another unread and uncited); the site-percolation value 0.5927 is the agent's knowledge, not a source; P39's and P40's supplements not read.
- **Allegiance:** P62 and P64 not reconciled on haemoglobin's T state; OSF data for P56 and P66 not fetched (98 vs 106 effects unexplained); Ruth read in the KJV only; no non-Abrahamic primary text.
- **Convergence:** chaos at N = 4 not shown; P69's count (678 or 582) and P83's group sizes and df unresolved; Pahnke 1963, Stace 1960 and Taves not read; no non-Wikipedia quadrature source.
- **Ascendence:** P94's large-L decline not reproduced; P87's 78.8% vs 77.8% unexplained; no non-PMC or non-Platonic ascent source; the ladder toy's absorbing top rung is an assumption.
- **Transcendence:** P104's equations unavailable (the agent's reconstruction is used); base dependence of lookahead is the agent's reading, without proof or source; P108's p and z discrepancies unexplained; Stace, Katz, Forman and Taves not read.

Cross-cutting:
- No independent review of any cycle; CI paused; all checks local and by the agent.
- Reference lists and supplements were mostly not read; several standard results were used from the agent's knowledge (labelled).
- The pass-recording convention changed between Convergence and Ascendence (§5).
- Duplicate source registrations (P51/P59, P84/P105), and six numbers between P01 and P108 that no register assigns (`data/registry_checks.json`).
- Seven links are labelled above their weakest basis claim (§3).
- Attribution record: the Divergence x12 disclosure says its commits carry a Co-authored-by: Grok Bot trailer, but the commits on `research/phase-divergence-x12` are authored by Grok Bot with a Co-authored-by: Kyle Steen trailer, like later phases; the disclosure text is wrong and the trailer's e-mail address changed between Insurgence and Ascendence (UR-L5-03, attributable agent actions).
- README §10's later pattern: the reported all-zero vector follows only from multiplying by E = 0, not D = 1 (§6); which scalar is meant is undefined.

## 9. Verification of this synthesis
`Synthesis/EXECUTION_RECORD.json` records the pre-registered checks in `Synthesis/SPEC.md`: V1, x12 ledger label counts equal Maps v38 (36 rows); V2, 1,116 records, 186 per phase; V3, README §10 arithmetic; C1, every claim ID here resolves in its cycle ledger with the label shown; C2, every link ID resolves with its label; C3, every source ID resolves; C4, no claims, link or source register changed against the base. Results: V1, V2, C1, C2, C3 and C4 Pass; **V3 Fail** (the later-pattern reading, §6), kept and reported. No Maps version is made: `PLAN.md` §6 and §9 assign Maps versions to cycles only (v9-v38). Gate: **INDETERMINATE** (independent review pending).
