# N-A Level-Name Crosswalk — x6 report

**Status:** researched (x6). The crosswalk is still **Proposed**. Every resolution is an option for Kyle, and all are recorded "open (Kyle)".

**Inputs:**
- `config.json`
- `../judgments/*_x6.csv`
- ledger `../ledger/ledger_x6.csv`. All 22 tablets plus INDEX and the three matrices (26 Tablets files) have now been read in full. The 12 tablets read in x6 are marked `full (x6)`.

The tables are in `TABLES.md`. The run records are in `iter-1/` (rule `as_judged`) and `iter-2/` (rule `strict`).

## What x6 adds

**1. Tool defect fixed (X6-3 PASS, method).** The v2 extractor stops at the sentence or arrow-chain boundary. Every judged scheme, D-ST4 and D-ST5 included, now equals its extraction. The x3 records still reproduce with the v1 code, and the x3 failure stays on record.

**2. Stage sequences (X6-14 FAIL, a finding; Established).** With the corrected extractor, the tablets state three sequences:
- Nigredo > Albedo > Citrinitas > Rubedo. Stated in Albedo, Celestial, Solar and Ruby's own header.
- The same, plus Celestial after Rubedo. Stated in Citrine.
- Nigredo > Albedo > Citrinitas > Ember > Rubedo. Stated in Ruby's Canon Doctrine, so Ruby gives two sequences.

Ruby also calls Rubedo "the Fourth and Final Stage", while Celestial is "Post-Rubedo". The governing-stage census (v2) finds a stated stage in 21 of 22 tablets; Terra states none. Further variants appear only as governing stages:
- Cauda Pavonis (Amethyst)
- Calcination (Ember)
- Proliferatio (Viriditas)
- Solutio (Aqua)
- Soft Rubedo (Rose)
- non-stage labels: All Stages, Cross-stage, Transition, Perception Layer, Akashic, Embodiment

This is a GD-internal vocabulary. No Foundation counterpart is claimed (X80–X83, different-kind).

**3. Phase senses (X6-17 PASS, method; relations Plausible).**
- The Tablets "How to read" glosses were compared with the Foundation phase tracks' working readings. Those readings are not definitions: each DEFINITIONS file says no repository document defines its term.
- Same sense: Divergence (splitting / separation), Allegiance (committing / persistent attachment), Convergence (coming together / approach to a common estimate).
- Partial overlap:
  - Insurgence: "rising" lacks the threshold sense the Foundation reading turns on.
  - Ascendence: "rising beyond" exceeds ascent toward a peak and reaches into the Foundation's Transcendence ("going beyond a level, limit or frame").
- X56 is therefore changed from no-counterpart to partial-overlap (Foundation Transcendence against Tablets Ascendence). The Celestial tablet, placed at Spirit × Ascendence and described as transcending its own design, is consistent with this reading.
- X46–X55 move from Hypothetical to Plausible.

**4. The senses of Meta (X6-18 PASS, open check; Established counts, Plausible reading).**

| Report level | reflexive meta- markers | metaphysic- terms |
|---|---|---|
| Meta (8 reports) | 386 | 17 |
| Original | 64 | 46 |
| Magic | 27 | 11 |
| Super | 18 | 4 |

- GD's Meta level is overwhelmingly reflexive (meta-knowledge, meta-cognition, meta-level and so on).
- "Metaphysical" occurs more in the Original reports, mainly in the Soul reports and partly as a `metaphysical_claim` field.
- This supports K2: GD's "Meta" is the reflexive sense, and the Foundation's §B/§C gloss "Metaphysical" is a different sense that shares the name.
- Caveat: the reflexive pattern also matches database names such as "Meta-Knowledge Database". Those are reflexive in sense too, but they inflate the count.

**5. Position and numbering (X6-19 and X6-20 FAIL, findings).**
- Position 0 is given to Terra ("Tablet 0", beneath the five gem tablets) and to Emerald ("position 0, the universal law", in Obsidian).
- The text reads most naturally as **two numbering schemes**, a gem-ground position and a law sequence, rather than one contradiction (Plausible). Neither file refers to the other's scheme.
- The stated Hermetic Law numbers are First (Obsidian), Third (Silver) and Fourth (Amber). No tablet calls itself the Second.

**6. Sealing (K6, confirmed; Established).**
- All 12 newly read tablets carry an editorial "Sealing note". Each says the verse metadata reads "Sealed: <July 2026 date>" while the source registry marks the tablet unsealed, "Preserved and flagged. Not resolved."
- The x3 discrepancy types D1–D9 stand, and no new type was found. Reading in full therefore confirms the census rather than changing it.

**7. Strict sensitivity (X6-16 FAIL, reported outside the gate).**
- 19 terms lose their only mapping, against 25 in x3.
- **The drop is a rule artefact, not stronger evidence.** The strict rule prunes only same-sense rows. The six terms recovered (Insurgence and Ascendence in D-TP, F-93P and F-B) were demoted to partial-overlap, which the rule keeps.
- The remaining 19 include three phase names, four Being terms, reflexive Meta, and README §2 Magic Power.

## Changes to the conflicts and options
- K3 and K6 are extended (`conflicts_x6.csv`).
- Two options are new, both "open (Kyle)":
  - K3-F: sense-qualified citation of the Tablets phase names.
  - K6-F: Kyle states the intended stage sequence and position numbering in GAIA-Documentation, as his own act.

## Gate
- **x6 gate: PASS (method), subject to `VERIFICATION.md`.**
  - X6-1 to X6-7, X6-12 and X6-17 PASS.
- Findings that FAIL: X6-8, -9, -11, -13, -14, -15, -19 and -20, plus X6-16 outside the gate. None was re-thresholded.

## Limitations
- The sense judgments rest on short glosses ("rising", "rising beyond") and on the Foundation tracks' own working readings. Both are thin.
- The Meta census is lexical.
- Option review (x9) has not been done.
