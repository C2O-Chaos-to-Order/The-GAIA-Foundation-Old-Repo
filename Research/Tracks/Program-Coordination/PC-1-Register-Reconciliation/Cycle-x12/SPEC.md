# PC-1 Cycle x12: Specification

Written and pushed **before** any x12 run. Stacked on `research/pc1-x9` (c7eab334). Pre-registered checks: `config.json` (X12-1 to X12-15).

## Scope
1. **Repair the reviewer roles.** `../judgments/domains_x12.csv` equals the x6 rows, with one change: each domain's reviewer roles become its proposed roles plus the roles its x9 tier and the W overlay require. No other field may change, and X12-14 guards this.
2. **Fix the x9 issue enumeration.** With the config key `issues_from_main_metrics`, the b9 domains are now read from the main metrics. The list should hold 29 issues (X12-7).
3. **Final wave proposals** (`../judgments/wave_proposals_x12.csv`). These carry the agent preferences of decisions D-02 to D-06. 025 moves to Wave 3 (D-03), and 038 is left to the owner (scored as Wave 3).
4. **Register columns.** The reconciliation output adds three columns: scope tier, proposed wave and required roles (`register_columns`).
5. **Consolidated `../REGISTER.md`.** This is a generated table of all 45 domains plus a hand-written summary. It is produced after the run from iteration 1's record. It uses short slugs, not suite titles. The full-folder boundary scan in VERIFICATION covers it.

## Iterations
- **1:** W overlay rule on
- **2:** W overlay rule off. The repaired roles are a superset, so they should pass both ways.

A failed check stays failed. All earlier cycles must verify identically.
