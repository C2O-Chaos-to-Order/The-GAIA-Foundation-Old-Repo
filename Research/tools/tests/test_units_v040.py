"""Unit tests for changes in gaia_tools 0.4.0 / data model 1.3.0 (Cycle 4)."""
import re
from gaia_tools import validate as V, __version__, DATA_MODEL_VERSION


def test_versions():
    assert tuple(map(int, __version__.split("."))) >= (0, 4, 0) and tuple(map(int, DATA_MODEL_VERSION.split("."))) >= (1, 3, 0)


def test_y_prefix_source_ids():
    S = V.load_schemas()
    pats = [S["source"]["properties"]["source_id"]["pattern"]]
    it = S["claim"]["properties"]["source_ids"]["items"]
    pats += [a["pattern"] for a in it.get("anyOf", []) if "pattern" in a and a["pattern"].startswith("^[")]
    assert len(pats) >= 2
    for pat in pats:
        assert re.match(pat, "Y06") and re.match(pat, "X26") and re.match(pat, "W01") and not re.match(pat, "Z01")


def test_c4_sim_ids():
    S = V.load_schemas()
    assert re.match(S["execution_record"]["properties"]["sim_id"]["pattern"], "SIM-R7-C4")
