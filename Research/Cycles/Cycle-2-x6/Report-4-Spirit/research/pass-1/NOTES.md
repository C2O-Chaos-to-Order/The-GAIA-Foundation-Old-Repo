# Report-4-Spirit — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** Queries on attendance and mortality logged; S12 (Cycle 0, full text) selected for its mediation table.

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| S12: Li S, Stampfer MJ, Williams DR, VanderWeele TJ (2016). Association of Religious Service Attendance With Mortality Among Women. JAMA Intern Med 176(6):777-785. doi:10.1001/jamainternmed.2016.1615 | full text (PMC author manuscript PMC5503841) | C0v2-R4-09; C0v2-R4-14; C2-R4-01 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:37+00:00 | Europe PMC REST search (sort: CITED desc) | `(religious OR religion OR spirituality) AND "service attendance" AND mortality AND (mediation OR mediator OR "social support")` | 358 |
| 2026-10-24T02:02:00+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:"mediation analysis" AND (VanderWeele) AND OPEN_ACCESS:y` | 109 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
