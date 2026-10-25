# PC-4 Research-to-Domain Map: x3 report

Status: **Proposed research output, not adopted.** Suite: owner-provided GAIA Totality Suite v0.1.0 (Proposed, not filed here). Labels per `../PLAN.md` §4.

## Findings

1. **The map moved toward the charters' own scope lines.** TOT-038's scope names electromagnetic and geomagnetic concepts, cosmology, energy, quantum mechanics and consciousness claims. Together with the b7 Quantum cluster, this moves 14 reports to TOT-038 as primary home: 11 from TOT-023 (which they keep as a secondary), G-06 from TOT-005, G-07 from TOT-003, and G-10 from no domain. K-02 and K-03 move from TOT-023 to TOT-030. TOT-023 now has 33 primaries and TOT-038 has 20, so the two of them still home 53 of 91 reports [Plausible; the TOT-038 moves for §G are Established by reference to b7.8].
2. **29 reports are now Established**, up from 8: the queue itself names their domain, in their own text, in a b7 cluster line or in PC-4's examples. The tool checks every reference [Established].
3. **Domains with no report.** 25 domains are no report's primary home (TOT-005 dropped out when G-06 moved to TOT-038). Counting secondaries, only TOT-032 still has none. Counting candidates, every domain is touched [Plausible].
4. **Against the gap check's b8 list** (ten domains with no existing material): TOT-030 now has 3 planned primary reports (K-02, K-03, ToG-10) and TOT-043 has 1 (N-5). The other eight (010, 019, 022, 026, 028, 031, 036, 037) appear only as secondaries. They have no report of their own, so their Wave 2 and Wave 3 domain reports start from scratch [Plausible].
5. **Reports with no domain: 1**, KL-01 (The Echo That Began the Light; the owner has not yet defined its scope) [Hypothetical].
6. **Tensions** are recorded in `iter-1/EXECUTION_RECORD.json` (`queue_named_not_primary`): places where the queue names a domain but the judged primary differs. Examples: H-01 sits under the AI cluster but is homed at TOT-021 (human-technology interaction); ToG-06 and ToG-08 are named in the vulnerability-disclosure cluster but homed at TOT-017 and TOT-011; ToG-SYN and PC-7 are named in the dashboard cluster (TOT-039) but homed at TOT-045 and TOT-008. Each judgment is kept, with the charter basis in the map. The owner may prefer the queue's grouping [Plausible].
7. **b7 proposals unchanged** (same nine homes as Baseline). Cluster b7.8 now also lists K-01–K-04 [Plausible].

## Checks
X3-1, X3-2 and X3-4 to X3-9 PASS in every iteration where they apply. **X3-3 FAILS (4)**: the remaining hits are PC-4's example domains, a known flaw in the check; see `PASSES.md`. The first run's X3-3 failure (6) is kept in `attempts/`.

## Independent check, and how independent it is
Matcher top-3 primary agreement rose from 0.427 to 0.556 (charter text), 0.444 (title and purpose) and 0.467 (titles). An exploratory comparison (`../tools/compare_maps.py`; not pre-registered) shows the Baseline map would score 0.427, 0.360 and 0.371 on the same variants:

| Map | Variant | top-1 | top-3 primary | top-3 any | n |
|---|---|---|---|---|---|
| map_c0.csv | charter | 0.3146 | 0.427 | 0.6742 | 89 |
| map_c0.csv | title_purpose | 0.2584 | 0.3596 | 0.618 | 89 |
| map_c0.csv | title | 0.3034 | 0.3708 | 0.5843 | 89 |
| map_x3.csv | charter | 0.4333 | 0.5556 | 0.7333 | 90 |
| map_x3.csv | title_purpose | 0.3111 | 0.4444 | 0.6444 | 90 |
| map_x3.csv | title | 0.3778 | 0.4667 | 0.6222 | 90 |

**This gain is not independent validation.** Pass 1 read the same charter text the matcher uses, and pass 2 moved "Quantum …" reports to the domain whose title contains "Quantum". Part of the higher agreement is the judgment moving toward the matcher's own vocabulary [Plausible].

## Diminishing returns
Passes 1 and 2 changed the map; pass 3 added nothing beyond them.

## Tables
`TABLES.md` (generated from iter-1).
