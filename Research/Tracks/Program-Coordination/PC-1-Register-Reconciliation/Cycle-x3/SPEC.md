# PC-1 Cycle x3: Specification

Written and pushed **before** any x3 run. Stacked on `research/pc1-c0` (e454f5e4). Pre-registered checks: `config.json`.

## Why x3 (from the Baseline report)
The Baseline checks proved that the proposal is well formed, not that it is right. x3 does four things the Baseline did not:
1. **Anchor re-read.** Every Baseline anchor's passage is read and judged as `direct`, `partial` or `none` support (`../judgments/anchor_review_x3.csv`). Anchors judged `none` are replaced. Anchors are added where a domain lacked direct support. The result is `../judgments/domains_x3.csv`.
2. **Deeper audit mapping.** Every audit v2 item gets exactly one **primary** domain, plus secondary domains (`../judgments/audit_map_x3.csv`). Every non-PASS item gets a **remedy home**: the file where its fix would be proposed, which must be its primary domain's home.
3. **Authority-ambiguity register** (`../judgments/authority_x3.csv`). Every file a domain cites, other than its home, is classified as one of:
   - `parent`: a higher-precedence standard
   - `companion`: a register or index that sits beside the home
   - `subordinate`: operates under the home
   - `evidence`: a record, not a rule
   - `superseded-on-approval`: replaced once the owner approves the home
4. **Wave proposals** (`../judgments/wave_proposals_x3.csv`). The owner gets options for each wave/priority mismatch, including 028, which the Baseline newly found.

## Fixes carried from the Baseline
- Output titles use the register filename's short slug (`title_style: short`), not the full title.
- The boundary check now also scans this run's own data outputs. Baseline's two flagged files are listed as known and are not re-scored.

## Iterations (home-rule sensitivity)
- **1:** `as_judged`
- **2:** `always_new`, where every domain gets a new file
- **3:** `no_planned`, where ToG §19 planned files are not used

X3-12 and X3-13 are consistency checks of the rule logic. They are largely definitional and are reported as such.

## Pre-registered checks
See `config.json` (X3-1 to X3-14). A failed check stays failed, and none will be re-thresholded after the run.

## Reproduction
The Baseline must still verify identically with the x3 tool.
