# Data model 1.4.0 (gaia_tools 0.5.0)

Schemas 1.3.0 (claim, source, link, simulation, execution record) are unchanged for the main cycles (copies in `../../v4-cycles-0-4/data-model/schemas/`, master copies in `Research/tools/gaia_tools/schemas/`). New in 1.4.0 (copied here), for tracks:
- `track_claim.schema.json`: track ledger rows (`T<L>-<TOPIC>-nn`; topics SOUL, SPIRIT, SUBC, CONS; `deepens` names the report claims a track claim extends; sources may be `K` (track) or main-cycle IDs; SIM citations `SIM-<TOPIC>-<L>/iter-k#check`).
- `track_execution_record.schema.json`: **track run layout**, two files per run: `SPEC.md` (written before execution, with the parameters in a ```json block) and `EXECUTION_RECORD.json` (embedded results, `spec_sha256`, `params_sha256`, `results_sha256`). Re-runs compare all three hashes and the check outcomes.
Matrix placement of track topics (pre-declared): SOUL→Soul, SPIRIT→Spirit, CONS→Consciousness, SUBC→Mind. Master Report claims are placed by `report_feed`.
