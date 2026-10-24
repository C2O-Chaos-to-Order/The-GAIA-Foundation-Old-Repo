# Report-4-Spirit — research pass 1 — logged systematic search (Cycle 4)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-4 agenda; record every query with hit counts and top hits.

**Outcome.** Two queries logged; no negative-control study of attendance in top hits.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T04:01:50+00:00 | Europe PMC REST search (sort: CITED desc) | `("negative control" OR "E-value") AND ("religious service" OR religiosity OR spirituality) AND mortality` | 105 |
| 2026-10-24T04:02:26+00:00 | Europe PMC REST search (sort: CITED desc) | `"religious service attendance" AND (mortality OR "all-cause") AND (cohort OR prospective)` | 294 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`. Sources read but not usable (Y07, Y08) are recorded in the fetch log and in pass notes, not in the source register.
