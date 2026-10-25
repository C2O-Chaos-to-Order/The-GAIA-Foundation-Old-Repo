# N-A Level-Name Crosswalk — x9 report

**Status:** researched (x9). The crosswalk is still **Proposed**. Every option is "open (Kyle)", and the review verdicts below are judgments about how options stand up to scrutiny, not decisions.

**Inputs:**
- `config.json`
- `../judgments/*_x9.csv`, including `option_review_x9.csv`
- ledger `../ledger/ledger_x9.csv`. There was no new GD reading. The Work Queue §N entry was re-read in full.

The tables are in `TABLES.md`. The run records are in `iter-1/` (`as_judged`), `iter-2/` (`strict`) and `iter-3/` (`adversarial`).

## What x9 adds

**1. Adversarial review (judgments, mostly Plausible).** Each of the 27 options was given its strongest objection:

| Verdict | Count | Options |
|---|---|---|
| survives | 6 | K1-B, K2-A, K4-B, K5-A, K5-C, K6-D |
| survives-qualified | 16 | the rest not listed |
| weakened | 4 | K2-B, K3-D, K4-C, K5-D |
| superseded | 1 | K3-C, by K3-F (its sense comparison was done in x6) |

The weakened options, with the main reason:
- **K2-B** (rename the Foundation level "Metaphysical"): this collides with Synergy's fifth rung "metaphysical" and splits README §2's second-order "Meta Power".
- **K3-D** (defer phases): report 2 needs GD track numbers.
- **K4-C** (bridge through the Tablets' Being axis): it imports K6's unresolved status into K4.
- **K5-D** (wait until the Control Standard "leaves Proposed"): the standard's status model has no Proposed value, so there is no defined exit.

**2. Reproducibility ripple (Established for N-A and PC-1, Plausible for PC-4) — X9-25 FAIL.**
- Three options would edit Foundation files that other verified records read: K1-C, K2-B and K3-B.
- `Research/WORK_QUEUE.md` is named by 11 config or tool files:
  - N-A's `tools/na.py`
  - five PC-1 configs
  - five PC-4 configs
- `Research/README.md` is named by N-A's tool only. This is a string match, so other references could be missed.
- PC-1 records hash their inputs (SHA-256), and N-A records hash the Work Queue blob. An in-place edit would therefore leave every such record reproducible at its own commit but **not on rerun at a later commit**.
- **This is a cost Kyle should see before choosing any align-foundation option.** An appended correction or change-log note avoids it (the K3-B qualifier).
- The prose ripple counts (`option_ripple.csv`) are coarse. K3-F's regex matches 1,344 Foundation files because the phase names are everywhere. That measures how widely the names are used, not how often the Tablets are cited.

**3. Checks on earlier records:**
- **X9-23 FAIL.** Two citations were flagged:
  - K5 cites `vocab.canonical_home`, but the census key is `canonical_home_gaiadoc`. This is a genuine dangling citation in my own records.
  - K3's `phase_senses_x6.csv` was flagged as a metric. **This is a tool defect:** a dotted file name matches the metric pattern. The file exists.
  
  Both are carried to x12: a corrected citation, and an extractor fix behind a key.
- **X9-24 FAIL.** The Work Queue says "The 24 tablet files are to be read". The listing has 22 tablet files, or 26 files under `Tablets/` counting INDEX and the three matrices. No GD file states 24 (Established).

**4. Re-reading the conflicts against the Work Queue.**
- The queue assigns K5 to "(N-B, PC-8)" and K6 to "(N-B)". N-A covers their vocabulary and documentary side at the owner's request, and K5-C and K6-D (route or defer to N-B) are consistent with the queue.
- Every other Work Queue conflict statement was checked against x6. No new error was found beyond those already recorded:
  - "Phase 1–7" is in fact 1–8.
  - "Many files" is in fact 7 of 333.
  - "two meanings" of Meta is in fact at least three.

**5. Survival under the adversarial rule.**
- X9-26 PASS: under iters 1–2, every conflict keeps a surviving non-defer option.
- **X9-27 FAIL** (iter-3): K3 and K6 have no unqualified surviving non-defer option.
- As disclosed in the SPEC, this follows from my own verdicts and is a summary, not an independent test. It means that **for phases and tablets, every active option needs a stated condition.**

## Gate
- **x9 gate: PASS (method), subject to `VERIFICATION.md`.**
  - X9-1 to X9-7, X9-12, X9-17, X9-21 and X9-22 PASS.
- Findings that FAIL: X9-8, -9, -11, -13, -14, -15, -19, -20, -23, -24, -25 and -27, plus X9-16 outside the gate.

## Limitations
- The objections are mine. A second reviewer, or Kyle, may find stronger ones.
- Ripple dependents are found by string match, and prose ripple by coarse regex.
- The evidence checker has the defect described in item 3.
