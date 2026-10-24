# Report-1-Body — research pass 3 — widen (adjacent literature, open-access full-text upgrades) (Cycle 3)

**Aim.** Widen to adjacent literature; look up open-access full texts for sources previously read as abstracts.

**Outcome.** X25 read in full (C3-R1-05); OpenAlex lookup for T01 logged (no new full text).

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| X25: Ribeiro AI, Amaro J, Lisi C, Fraga S (2018). Neighborhood Socioeconomic Deprivation and Allostatic Load: A Scoping Review. International journal of environmental research and public health 15:E1092. doi:10.3390/ijerph15061092 | full text (Europe PMC PMC6024893) | C3-R1-05 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:54:13+00:00 | OpenAlex works API (OA location lookup) | `T01 doi:10.1016/j.physbeh.2011.06.004` | 1 |
| 2026-10-24T03:12:28+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"allostatic load") AND (TITLE:socioeconomic OR TITLE:inequalit* OR TITLE:discrimination) AND (TITLE:review OR TITLE:"meta-analysis") AND OPEN_ACCESS:y` | 4 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
