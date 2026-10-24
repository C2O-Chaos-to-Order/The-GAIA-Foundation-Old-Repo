# Provenance (Cycle 4)

- `SOURCE_REGISTER.csv` — 157 sources (6 added in Cycle 4: Y01–Y06; column `cycle_added`), with access mode, retrieval URL, date, HTTP status and SHA-256 of the fetched snapshot. Third-party text is not redistributed. Y05 is **abstract only**.
- `SEARCH_LOG.jsonl` — 19 logged queries (Europe PMC REST; OpenAlex DOI lookups) with UTC time, report, research pass, exact query, URL, hit count and top hits. Screening covered top-ranked hits only.
- `FETCH_LOG.jsonl` — 12 Cycle-4 retrieval attempts with HTTP status and SHA-256. Y03, Y05 and Y06 first returned HTTP 500 from Europe PMC and were then retrieved through NCBI efetch (author manuscripts; Y05 returned metadata and abstract only); Y06 also has an eScholarship submitted-version PDF (logged as Y06P, not registered separately).
- **Read, nothing usable (logged, not registered, nothing rests on them):** Y07 Avraham et al. 2022 (eLife; no Mackintosh rule specification); Y08 Krasne, Fanselow & Zelikowsky 2011 (mentions Mackintosh 1975 only).
- **Not found / closed:** a faithful specification of the Mackintosh (1975) rule in any open-access text (R2 carried item BLOCKED); W03 Lenton & Lovelock 2000 still closed (OpenAlex lookup logged).
- `MANIFEST.sha256` — SHA-256 of every file in this cycle folder except itself.
