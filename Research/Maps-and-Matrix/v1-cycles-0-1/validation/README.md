# Validation outputs (v1)

| File | Tool | What it shows |
|---|---|---|
| `schema_validation.json` | `python -m gaia_tools.validate ..` | schema + cross-file rule errors (0) and quality warnings |
| `claim_source_C0.json`, `claim_source_C1.json` | `python -m gaia_tools.claimsource .. C<n>` | per-claim K-resolve / K-access / K-sim results |
| `rerun_C0.json`, `rerun_C1.json` | `python -m gaia_tools.rerun .. C<n>` | re-execution of every non-archived run from a fresh copy; output/check/params identity |

See `../data-model/README.md` for the interpretation.
