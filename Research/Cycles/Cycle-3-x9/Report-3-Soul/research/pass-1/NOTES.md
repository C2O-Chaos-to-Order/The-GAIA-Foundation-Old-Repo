# Report-3-Soul — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Two queries logged (broad, title-restricted).

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:43+00:00 | Europe PMC REST search (sort: CITED desc) | `(soul OR afterlife) AND (cross-cultural OR "cross cultural") AND (belief OR dualism)` | 1852 |
| 2026-10-24T02:55:09+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:soul OR TITLE:afterlife OR TITLE:"mind-body dualism") AND (TITLE:cultures OR TITLE:"cross-cultural" OR TITLE:universal OR TITLE:intuitive)` | 3 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
