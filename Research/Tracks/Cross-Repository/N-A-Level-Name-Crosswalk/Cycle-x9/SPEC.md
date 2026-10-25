# N-A x9: specification

This specification was written and pushed **before** the x9 run. It builds on x6 at `research/crosswalk-x6` (`82e4679d`).

## Purpose
x9 is an adversarial review of every option, a map of the Foundation files each option would touch, and a re-read of the conflicts against the Work Queue entry. No new GAIA-Documentation reading is needed: all 64 ledger files stay as read in x6 (`read_x9`). The Work Queue §N entry was re-read in full.

## Judgments
- **`../judgments/option_review_x9.csv`** has one row per option, 27 in all. Each row gives:
  - the strongest objection I could find, with its label
  - the Foundation files the option would edit (`ripple_targets`)
  - a regex for the Foundation prose it would bear on (`ripple_regex`)
  - a verdict: survives, survives-qualified, weakened or superseded
  - the qualifier
- **Verdicts are judgments.** They describe how each option stands up to review. They decide nothing, and every option stays "open (Kyle)".
- **`conflicts_x9.csv`** adds the re-read findings for K5 and K6:
  - The Work Queue assigns K5 to N-B/PC-8 and K6 to N-B.
  - The Work Queue says "24 tablet files".
- Schemes, crosswalk, options and phase senses are carried forward unchanged as `*_x9.csv`.

## Tool additions, behind the config key `x9`
- **Ripple.** For each option, the tool:
  - counts the Foundation `.md` files that match its regex (this track excluded)
  - lists the `config.json` and `*.py` files under `Research/` that name each target file. These files read or hash the target, so editing it would change their inputs.
- **Evidence check.** Every crosswalk row ID, metric name and judgment file cited in `conflicts_*.csv` evidence must exist.
- **Work Queue tablet claim.** The "N tablet files" statement is compared with the listing.
- **iter-3 (rule `adversarial`).** Qualified survival does not count.

## Pre-registered checks
- X9-1 to X9-20 carry over X6-1 to X6-20 unchanged. X9-16 runs on iter-2 only.

| ID | Hypothesis | Metric | Test | Kind |
|---|---|---|---|---|
| X9-21 | One review row per option | review_mismatches | = 0 | method |
| X9-22 | Review rows well-formed | review_problems | = 0 | method |
| X9-23 | Conflict evidence citations resolve | evidence_dangling | = 0 | check on earlier records |
| X9-24 | WQ tablet-file count equals the listing | wq_tablet_files_claim_diff | = 0 | check on an earlier claim |
| X9-25 | No align-foundation option edits a file other records read | align_foundation_with_repro_dependents | = 0 | open |
| X9-26 (iters 1–2) | Each conflict keeps a surviving non-defer option | conflicts_without_surviving_option | = 0 | summary of judgments |
| X9-27 (iter 3) | The same, with unqualified survival only | conflicts_without_surviving_option | = 0 | summary of judgments |

**Disclosure:**
- **X9-24 will fail.** The listing has 22 tablet files, and no GD file says 24.
- **X9-23 will probably fail.** K5 cites `vocab.canonical_home`, but the census key is `canonical_home_gaiadoc`. If so, the citation is fixed in x12, not here.
- **X9-25 will probably fail.** `tools/na.py` reads `Research/README.md` and `Research/WORK_QUEUE.md`. The counts for other tracks have not been computed.
- **X9-26 and X9-27 are not independent tests.** They follow mechanically from my own verdicts. From the verdicts, X9-27 is expected to fail for K3 and K6, where every non-defer option is qualified. They are reported as a summary.

## Gate
- PASS needs:
  - the method checks X9-1 to X9-7, X9-12, X9-17, X9-21 and X9-22
  - identical reruns of every N-A cycle
  - PC-1 reproduction
- The crosswalk stays Proposed.
