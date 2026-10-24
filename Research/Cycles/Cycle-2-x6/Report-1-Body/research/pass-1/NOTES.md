# Report-1-Body — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** 4 queries logged (see SEARCH_LOG.jsonl, report R1). Two broad full-text queries returned thousands of loosely relevant hits; title-restricted retries narrowed this. Selection continued in pass 2.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:35+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"feedforward" OR TITLE:"anticipatory" OR TITLE:"predictive") AND (thermoregulation OR homeostasis OR allostasis)` | 6099 |
| 2026-10-24T01:59:43+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:(feedforward OR anticipatory OR allostasis) AND TITLE:(thermoregulation OR "body temperature" OR homeostasis OR allostasis)` | 220 |
| 2026-10-24T02:00:53+00:00 | Europe PMC REST search (sort: CITED desc) | `(feedforward OR "feed-forward" OR anticipatory) AND thermoregulation AND OPEN_ACCESS:y` | 675 |
| 2026-10-24T02:00:54+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:"thermoregulation" AND TITLE:("concepts" OR "set point" OR "setpoint")` | 18 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
