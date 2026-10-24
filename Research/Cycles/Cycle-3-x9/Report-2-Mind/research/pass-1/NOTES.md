# Report-2-Mind — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Three LI queries logged; no discriminating open dataset found in top hits.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:44+00:00 | Europe PMC REST search (sort: CITED desc) | `"latent inhibition" AND (model OR "Pearce-Hall" OR "attention") AND (preexposure OR "pre-exposure")` | 617 |
| 2026-10-24T02:55:09+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:"latent inhibition" AND (ABSTRACT:"number of pre-exposures" OR ABSTRACT:"amount of preexposure" OR ABSTRACT:parametric OR ABSTRACT:"computational model")` | 9 |
| 2026-10-24T02:58:23+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"latent inhibition") AND (TITLE:"computational" OR TITLE:"model") AND OPEN_ACCESS:y` | 1 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
