# Report-1-Body — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Three queries logged (broad, title-restricted, exact title for Smith et al. 2006).

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:44+00:00 | Europe PMC REST search (sort: CITED desc) | `("heat acclimation" OR "heat acclimatization") AND (decay OR retention OR "re-acclimation" OR reinduction)` | 1309 |
| 2026-10-24T02:55:09+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"heat acclimation" OR TITLE:"heat acclimatization") AND (TITLE:decay OR TITLE:retention OR TITLE:memory OR TITLE:"re-acclimation" OR TITLE:"re-induction")` | 21 |
| 2026-10-24T02:58:22+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:"Interacting adaptive processes with different timescales"` | 1 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
