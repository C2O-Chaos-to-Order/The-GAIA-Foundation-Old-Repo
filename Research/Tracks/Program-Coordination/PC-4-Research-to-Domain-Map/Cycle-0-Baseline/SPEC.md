# PC-4 Cycle 0 (Baseline): Specification

Written and pushed **before** the Baseline run. Method: `../PLAN.md`. Pre-registered checks: `config.json` (copied below).

## Scope
- Inventory every Work Queue checkbox (`Research/WORK_QUEUE.md` on this branch; base `research/work-queue-phases-done` @ 7d5ab2c1, which carries PR #29's content 97ad5704 merged with main 456f806b).
- Map every item of kind report, candidate, governance and level (PLAN §3) to the 45 domains: `../judgments/map_c0.csv`.
- Propose a single home for each of the 9 b7 clusters: `../judgments/clusters_c0.csv`.
- Compute coverage: domains with no report (primary only; primary or secondary; and with candidates) and reports with no domain.

## Pass and iteration
- **Pass 1 (agent judgment).** One read of each item against the register's title and purpose (and the charter where unsure). Primary, secondary, label, basis. Disclosure: the judgment files were drafted before this SPEC was committed, but before any matcher run or coverage computation.
- **Iteration 1.** Matcher variant `charter`, stemming on, k = 3.

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C0-1 | The inventory captures every Work Queue checkbox outside the change log | inventory_gap | = 0 |
| C0-2 | Every in-scope item is mapped and every row passes the integrity checks | problems | = 0 |
| C0-3 | The matcher puts the judged primary in its top 3 for ≥ 40% of reports | topk_primary_rate | ≥ 0.40 |
| C0-4 | The matcher's top 3 contains some judged domain for ≥ 55% of reports | topk_any_rate | ≥ 0.55 |
| C0-5 | Coverage is concentrated: ≥ 10 domains have no report as primary home | domains_no_report_primary | ≥ 10 |
| C0-6 | At most 3 reports have no domain | reports_no_domain | ≤ 3 |
| C0-7 | All 9 b7 proposals pass the structural checks | clusters_ok | = 9 |

C0-3 and C0-4 are genuine predictions (the matcher has never been run); many reports are Philosophical/Spiritual subjects whose words do not appear in the charters, so either may fail.

## Verification
`python3 tools/pc4.py verify --cycle Cycle-0-Baseline` reruns the iteration in a temporary directory and requires an identical EXECUTION_RECORD. Repository checks: `mancheck.sh`, `gaia_tools.phases validate`, pytest, and a fresh-clone rerun.

## Labels
Established, Plausible, Philosophical/Spiritual, Hypothetical (PLAN §4). Gates: PASS, FAIL, INDETERMINATE (never PASS).
