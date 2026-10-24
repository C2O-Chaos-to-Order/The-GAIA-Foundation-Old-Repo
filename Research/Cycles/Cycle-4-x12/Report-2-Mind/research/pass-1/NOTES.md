# Report-2-Mind — research pass 1 — logged systematic search (Cycle 4)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-4 agenda; record every query with hit counts and top hits.

**Outcome.** Two Mackintosh/associability queries logged.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T04:01:49+00:00 | Europe PMC REST search (sort: CITED desc) | `"latent inhibition" AND (Mackintosh OR "attention theory" OR associability) AND (model OR simulation)` | 206 |
| 2026-10-24T04:02:25+00:00 | Europe PMC REST search (sort: CITED desc) | `(Mackintosh AND associability AND (model OR rule)) AND OPEN_ACCESS:Y` | 55 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`. Sources read but not usable (Y07, Y08) are recorded in the fetch log and in pass notes, not in the source register.
