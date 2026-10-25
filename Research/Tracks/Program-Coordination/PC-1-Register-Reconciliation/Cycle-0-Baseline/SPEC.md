# PC-1 Cycle 0 (Baseline): Specification

Written and pushed **before** the Baseline run. Method: `../PLAN.md`. Pre-registered checks: `config.json`.

## Pass 1 (agent judgment)
- One row per domain in `../judgments/domains_c0.csv`, with these columns: proposed IDs, home type and path, UR domain(s), anchors in existing documents, required reviewer roles, label and basis.
- One row per audit v2 item in `../judgments/audit_map_c0.csv` (audit ID → domains).
- One row per domain in `../judgments/roadmap_c0.csv`: the roadmap wave in which the suite's wave text names the domain, or `unnamed`, with the wave phrase as basis (short).
- The tool derives the rest:
  - the laws, from the UR §5 headings;
  - the ToG §6 domains, from PC-4;
  - PC-4 primary reports;
  - the crosswalk coverage and b9;
  - the priority-implied wave (P0 → 1, P1 → 2, P2 → 3, P3 → 4) and the mismatches;
  - the open audit items per domain;
  - ID collisions;
  - duplicate homes;
  - the boundary scan.

## Iteration 1
Home rule `as_judged` (later cycles test alternatives).

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C0-1 | One row per register domain | domain_rows_ok | = 45 |
| C0-2 | Row integrity | problems | = 0 |
| C0-3 | Every anchor resolves | anchors_unresolved | = 0 |
| C0-4 | b9 recomputed equals the Work Queue's 11 | b9_symmetric_difference | = 0 |
| C0-5 | The four recorded mismatches are found | expected_mismatches_missing | = 0 |
| C0-6 | Canonical homes are unique | duplicate_homes | = 0 |
| C0-7 | No ID collisions | id_collisions | = 0 |
| C0-8 | Every audit v2 item mapped | audit_unmapped | = 0 |
| C0-9 | No 80-character overlap with the suite | boundary_overlaps | = 0 |

C0-4 and C0-5 are genuine checks of earlier work (the gap check and the Work Queue note). The tool recomputes them from the suite. Either may fail, for example if the range parsing differs from the gap check's reading.
