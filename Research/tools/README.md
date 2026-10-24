# Research/tools — gaia_tools (research tooling only)

A small Python package used to check and map the research corpus. It is **research tooling only**: no application, no service and no deployment. It reads the cycle folders and writes reports and maps, and it never modifies cycle data.

| Module | Command | Purpose |
|---|---|---|
| `gaia_tools.validate` | `python -m gaia_tools.validate <Research> [--out f.json]` | JSON-Schema validation (data model 1.3.0, `gaia_tools/schemas/`) and cross-file rules V1–V6 (V3 resolves SIM citations across cycles); quality warnings Q1–Q4 |
| `gaia_tools.rerun` | `python -m gaia_tools.rerun <Research> C<n> [--python P]` | re-executes a cycle's simulations in a temporary copy and compares output hashes, check results and params with the stored execution records |
| `gaia_tools.claimsource` | `python -m gaia_tools.claimsource <Research> C<n> [--snapshots DIR]` | offline claim-source checks: K-resolve, K-access (full-text rule), K-sim (no Established claim on a Fail; 'not supported' wording) and optional K-phrase against local text snapshots (phrases are regular expressions with a literal fallback; a missing snapshot is Indeterminate, never Pass) |
| `gaia_tools.maps` | `python -m gaia_tools.maps <Research> <out> --version-label "..."` | claim map, 625-cell matrix and Being × Lens projection, GAIA-centred link graph (JSON + Mermaid), cross-cycle changes, simulation index; link pressure includes Report-7 strict-rule downgrades |
| `gaia_tools.data` | (library) | loaders for claims, sources, links, simulations and checks |

```
cd Research/tools
pip install -r requirements.txt
python -m pytest -q tests                 # unit + corpus tests (22; +1 phrase test with GAIA_SNAPSHOTS=<dir>)
GAIA_RERUN=1 python -m pytest -q tests     # also re-executes every simulation (~1 min)
```
Versions: gaia_tools 0.4.0; data model 1.3.0 (changes in `CHANGELOG.md`); lens rule 1.0.1 (`gaia_tools/lens_rules.json`, provisional).

## Tracks and maps over all work (0.5.0)
```
python -m gaia_tools.tracks validate ..                       # all track cycles
python -m gaia_tools.tracks claimsource .. TA --snapshots DIR  # one track cycle
python -m gaia_tools.tracks rerun .. TA                        # re-execute and compare hashes
python -m gaia_tools.maps_all .. ../Maps-and-Matrix/<version> --version-label "..."
```
Research tooling only, as before.

## Phases track (0.6.0)
```
python -m gaia_tools.phases validate ..                         # all phase cycles
python -m gaia_tools.phases claimsource .. DV0 --snapshots DIR   # one phase cycle
python -m gaia_tools.phases rerun .. DV0                         # re-execute and compare hashes
python -m gaia_tools.phases maps .. ../Maps-and-Matrix/<version> --version-label "..."
```
Research tooling only, as before.
