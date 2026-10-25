# N-A x3: specification

This specification was written and pushed **before** the x3 run. It builds on the Baseline at `research/crosswalk-c0` (`db6973b3`).

## New reading, all checked against blob SHAs (`../ledger/ledger_x3.csv`, `read_x3`)
These 10 tablets were read in full:
- the four drafts: Alabaster, Albedo, Transparent and Clarity
- the three sealed in the source registry: Citrine, Ember and Emerald
- the three marked consistently sealed: Terra, Viriditas and Void

The other 12 tablets remain census-only until x6.

## What the reading found, and how x3 handles it
- **New GD vocabularies.** Three are added to `schemes_x3.csv`:
  - D-ST4, the four alchemical stages in Albedo
  - D-ST5, the five stages in Citrine, which adds Celestial
  - D-GEM, Terra's five gem tablets, with Terra as Tablet 0
  
  Crosswalk rows X80–X93 are new, and option K6-E is new.
- **New tablet census.** It sits behind the config key `x3_census`, so the Baseline record is unchanged. It covers:
  - the governing stage of each tablet
  - "Baseline preserved" references and whether they resolve in the listing
  - "Phase 2 (structure and organization)" endings
  - set-size and count claims across all 26 Tablets files
  - the ordered stage sequences
- **Sensitivity (iter-2, rule `strict`).** Same-sense crosswalk rows are kept only when labelled Established. The test is whether every term still has a row, which measures how much of the crosswalk rests on Plausible or Hypothetical judgments.
- **Re-reading the Baseline.** No factual error was found in the Baseline REPORT. Conflicts K3 and K6 are extended (`conflicts_x3.csv`).

## Pre-registered checks
- X3-1 to X3-12 are the Baseline checks C0-1 to C0-12, with the same metrics and thresholds. They run on both iterations.
- The new checks are below. X3-13 to X3-15 test GD's own consistency, so a failure is a finding.

| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| X3-13 | Every "Baseline preserved" file exists | dangling_baseline_refs | = 0 |
| X3-14 | One alchemical stage sequence | stage_sequence_variants | = 1 |
| X3-15 | One set size across the Tablets files | tablet_set_size_claims | = 1 |
| X3-16 (iter-2 only) | The strict rule leaves no term unmapped | strict_unmapped_terms | = 0 |

**Disclosure.** The full reading already showed that X3-13 to X3-15 are likely to fail:
- the listing has no v1.0.0 files;
- Albedo and Citrine state different stage sequences;
- 22 and 18 both appear.

X3-16 is genuinely open. It has not been computed before this push.

## Gate
- PASS needs the method checks (X3-1 to X3-7, X3-12 and X3-16) plus identical reruns of the Baseline and x3.
- The crosswalk stays Proposed.
