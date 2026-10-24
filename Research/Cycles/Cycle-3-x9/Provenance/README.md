# Provenance (Cycle 3)

- `SOURCE_REGISTER.csv` — 151 sources (21 added in Cycle 3: X02, X03, X05, X08, X09, X11–X26; column `cycle_added`), with access mode, retrieval URL, date, HTTP status and SHA-256 of the fetched snapshot. Third-party text is not redistributed.
- `SEARCH_LOG.jsonl` — 49 logged queries (Europe PMC REST; OpenAlex DOI lookups for open-access copies) with UTC time, report, research pass, exact query, URL, hit count and top hits. Screening covered top-ranked hits only.
- `FETCH_LOG.jsonl` — 29 Cycle-3 retrieval attempts with HTTP status and SHA-256.
- **Failed retrievals (logged, not registered, nothing rests on them):** X01 (full text of V22; HTTP 500, then PMC OAI 400), X04 (accepted manuscript of V39; HTTP 401), X06 (full text of S20; no HTTP response), X07 (full text of V16; HTTP 403), X10 (Horowitz 2008; HTTP 500, then OAI 400). X03 succeeded on the second route (PMC OAI) after HTTP 500.
- **Logging mistake (disclosed):** the OpenAlex lookup logged for T08 (report R4, pass 3) used a wrong DOI (`10.1159/000190790`; the correct DOI ends `.791`) and returned an unrelated meta-analysis. Nothing from it was used; the log line is kept as executed.
- `MANIFEST.sha256` — SHA-256 of every file in this cycle folder except itself.
