# Report-7-Unified — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** One analogy/self-regulation query logged (4,850 hits; noisy); no source selected.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:23:49+00:00 | Europe PMC REST search (sort: CITED desc) | `(analogy OR "analogical reasoning") AND (homeostasis OR "self-regulation") AND (organism OR planet OR Earth) AND OPEN_ACCESS:y` | 4850 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
