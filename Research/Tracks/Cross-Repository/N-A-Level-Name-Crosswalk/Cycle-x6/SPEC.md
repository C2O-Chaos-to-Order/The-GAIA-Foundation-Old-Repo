# N-A x6: specification

This specification was written and pushed **before** the x6 run. It builds on x3 at `research/crosswalk-x3` (`cdc3aa2c`).

## New reading, checked against blob SHAs (`../ledger/ledger_x6.csv`, `read_x6`)
The remaining 12 tablets were read in full: Amber, Amethyst, Aqua, Celestial, Lapis, Obsidian, Rose, Ruby, Sapphire, Shadow, Silver and Solar. All 26 Tablets files have now been read in full. No GAIA-Documentation file was written; the mirror is read-only.

## Tool changes, all behind the config key `x6`, so the Baseline and x3 records stay identical
- **Stage extractor v2.** x3's extractor ran past the sentence end (the X3-3 failure). v2 takes only (a) arrow chains bounded by ':' or '.', and (b) the first sentence after a sequence marker. D-ST4 and D-ST5 now use the v2 extractors `stage_albedo` and `stage_citrine`. The v1 functions stay in the tool, unchanged, so x3 still reproduces.
- **Stage census v2.** Also reads plain "Governing Stage:" lines. x3 missed these in five tablets.
- **Phase senses.** `../judgments/phase_senses_x6.csv` compares each Tablets phase gloss with a Foundation working reading.
  - The tool re-extracts the gloss from MATRIX-COMBINED "How to read".
  - It checks that each anchor phrase is present in `Research/Tracks/Phases/<phase>/Cycle-D-x12/DEFINITIONS.md`.
  - The relations are judgments, all labelled Plausible.
  - The Foundation's own definitions say that no repository document defines these phase terms. The anchors are therefore the Foundation tracks' working readings, not definitions.
- **Meta-sense census.** Counts reflexive meta- markers (meta-level, meta-cognition, meta-knowledge and so on) and metaphysic- terms across the listing, and per level of the 32 reports.
- **Position and numbering claims.** "Tablet 0", "Zeroth Tablet" and "X, position 0", plus "The N-th Hermetic Law of GAIA" headings.

## Judgment changes
- **Schemes:** new scheme D-ST5E, Ruby's arc: Nigredo, Albedo, Citrinitas, Ember, Rubedo.
- **Crosswalk:**
  - X46–X55 move from Hypothetical to Plausible. Divergence, Allegiance and Convergence are same-sense. Insurgence and Ascendence become partial-overlap.
  - X56 changes from no-counterpart to partial-overlap: Foundation Transcendence against Tablets Ascendence.
  - X94–X98 are new (D-ST5E).
- **Conflicts and options:** K3 and K6 are extended. New options K3-F and K6-F, both "open (Kyle)".

## Pre-registered checks
- X6-1 to X6-16 carry over X3-1 to X3-16 with the same thresholds.
- Exception: X6-14 now reads `stage_sequence_variants_v2`. The v1 value was contaminated by the extractor defect.

| ID | Hypothesis | Metric | Test | Kind |
|---|---|---|---|---|
| X6-17 | Judged glosses equal the source; Foundation anchors resolve | phase_sense_mismatches | = 0 | method |
| X6-18 | In the 8 Meta-level reports, reflexive markers outnumber metaphysic- terms | meta_reports_reflexive_minus_metaphysical | ≥ 1 | open |
| X6-19 | Exactly one tablet holds position 0 | position0_claimants | = 1 | GD consistency |
| X6-20 | Stated Hermetic Law numbers have no gaps from 1 | hermetic_law_gaps | = 0 | GD consistency |

**Disclosure (what I knew before the run):**
- Reading showed that X6-14, X6-19 and X6-20 are likely to fail.
  - Ruby's doctrine adds Ember. Citrine adds Celestial.
  - Terra is "Tablet 0", while Obsidian gives Emerald "position 0".
  - The stated laws are First (Obsidian), Third (Silver) and Fourth (Amber).
- The v2 extractor was tried on 7 tablets while it was being written. Those tablets gave three sequences.
- X6-18 has not been computed.
- **Caveat on X6-19.** Terra's position is a tablet position and Emerald's is a law position. A failure may therefore mean two numbering schemes rather than a contradiction. The REPORT will say which reading the text supports, and that it remains Kyle's call.

## Gate
- **Gate change, stated before the run.** X6-16 (strict sensitivity) leaves the gate. x3 showed it measures how strong the judgments are, not the method. It is still reported.
- **PASS needs:**
  - the method checks: X6-1 to X6-7, X6-12 and X6-17
  - identical reruns of Baseline, x3 and x6
  - PC-1 reproduction
- The crosswalk stays Proposed, and every option stays "open (Kyle)".
