# N-A Level-Name Crosswalk — x3 report

**Status:** researched (x3). The crosswalk is still **Proposed**. Every resolution is an option for Kyle.

**Inputs:**
- `config.json`
- `../judgments/*_x3.csv`
- ledger `../ledger/ledger_x3.csv`. Ten more tablets are now read in full, so 20 sources have been read in full overall.

The tables are in `TABLES.md`. The run records are in `iter-1/` (rule `as_judged`) and `iter-2/` (rule `strict`).

## What x3 adds

**1. A tool defect, caught by its own check (X3-3 FAIL, method).**
- The new stage-sequence extractor reads past the end of the sentence that states each sequence. As a result:
  - Albedo yields `Nigredo > Albedo > Citrinitas > Rubedo > Nigredo > Albedo`, not the four stages its text gives.
  - Citrine yields six terms, not the five its text gives.
- The judged lists D-ST4 and D-ST5, taken from reading the tablets, are correct. The extraction is what is wrong.
- The X3-14 value (2 variants) is therefore computed from contaminated sequences. The conclusion still holds, because the stated sequences differ (four stages against five with Celestial), but this cycle's number does not demonstrate it.
- The failure stays recorded. The fix is due in x6: stop at the first sentence end.

**2. Tablet provenance (X3-13 FAIL, a finding; Established).**
- 20 of 22 tablets cite a "Baseline preserved" `Tablets/*.v1.0.0.md` file that is not in the repository listing.
- 19 tablets end by awaiting "Phase 2 (structure and organization)". This is a fifth GD use of "phase", after the track numbers, Phase A–D, the Integrity Courts steps and the Tablets' phase names.

**3. Stage vocabulary (Established).** Tablet headers give 15 distinct "Governing Stage" values, and 5 tablets state none. The values mix three kinds of thing:
- classical stages (Nigredo, Albedo, Citrinitas, Rubedo)
- an operation (Calcination)
- non-stage labels (All Stages, Cross-stage, Perception Layer, Transition, Akashic)

This is a GD-internal vocabulary with no Foundation counterpart (X80–X83, different-kind, Plausible). It matters for report 7 (Modernization of Alchemy), which is option K6-E.

**4. Set-size claims (X3-15 FAIL, a finding; Established).** The Tablets files state sizes of 22 and 18:
- "The set is 22": INDEX and all three matrices.
- "18" in various forms: INDEX ("registry-listed"), the four drafts ("18-tablet registry"), the matrices ("the 18 remain the 18") and Emerald ("18 Hermetic Tablets").

Emerald also names "Seven Tablets of NEXUS", and Terra names five gem tablets plus Tablet 0. Two readings are possible: 22 = 18 + the 4 drafts, or 22 sealed tablets. They give different answers to whether the drafts are sealed. That is the core of K6.

**5. Self-attribution (Plausible).** Terra, Viriditas and Void say the sealing discrepancies are "a property of the transfer, not … of the tablets". Terra also calls itself "the only" tablet where the two status records agree (D6).

**6. Sensitivity (X3-16 FAIL, a finding about this crosswalk; Plausible).**
- Only 13 of the 35 same-sense rows are Established.
- Under the strict rule, 25 terms lose their only mapping. These include:
  - all five Tablets phase names
  - four of the five Tablets Being terms
  - reflexive Meta (D-4L)
  - Foundation Mind and Consciousness in the Seven-Reports scheme
- **The "same sense" links between the repositories therefore rest mostly on Plausible or Hypothetical judgments.** Names match, but the senses have not been compared. Report 2 should not treat these rows as identities.

## Changes to the conflicts (`conflicts_x3.csv`)
- K3 is extended with the transfer "Phase 2".
- K6 is extended with items 2–5 above.
- One option is new: K6-E keeps the alchemical stages as a separate GD vocabulary.

## Gate
- **x3 gate: FAIL (method).**
  - X3-3 failed because of the extractor defect above.
  - The other method checks (X3-1, X3-2, X3-4 to X3-7 and X3-12) PASS.
  - X3-8, -9, -11, -13, -14, -15 and -16 FAIL as findings.
- The reruns are recorded in `VERIFICATION.md`.

## Limitations
- Twelve tablets are still census-only: Amber, Amethyst, Aqua, Celestial and the eight with sealing discrepancies.
- The sense comparison is not done.
- The X3-14 number depends on the defective extractor (item 1).
