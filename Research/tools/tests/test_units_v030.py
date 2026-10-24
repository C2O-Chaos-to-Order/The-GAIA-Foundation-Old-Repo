"""Unit tests for changes in gaia_tools 0.3.0 / data model 1.2.0 (Cycle 3)."""
import os, re, json, tempfile
from gaia_tools import data as D, validate as V, __version__, DATA_MODEL_VERSION


def test_versions():
    assert __version__ == "0.3.0" and DATA_MODEL_VERSION == "1.2.0"


def test_x_prefix_source_ids():
    S = V.load_schemas()
    for pat in (S["source"]["properties"]["source_id"]["pattern"], S["claim"]["properties"]["source_ids"]["items"]["anyOf"][0]["pattern"]
                if "anyOf" in S["claim"]["properties"]["source_ids"]["items"] else S["source"]["properties"]["source_id"]["pattern"]):
        assert re.match(pat, "X26") and re.match(pat, "W01") and not re.match(pat, "Y01")


def test_link_rule_columns_allowed():
    s = V.load_schemas()["link"]
    keys = list(s["patternProperties"])
    assert any(re.match(k, "c3_strict_rule") for k in keys) and any(re.match(k, "c3_essential_rule") for k in keys)
    assert not any(re.match(k, "c3_other") for k in keys)


def test_is_archived():
    assert D.is_archived("archive/run-1")
    assert D.is_archived(os.path.join("superseded-run-1", "iter-3"))
    assert not D.is_archived("iter-3")
    assert not D.is_archived("superseded")  # only the 'superseded-run-' prefix counts


def _rec(d, sim_id, it):
    os.makedirs(d, exist_ok=True)
    json.dump(dict(sim_id=sim_id, iteration=it, pre_registered_checks=[dict(id="H1", result="Supported")], outputs={}), open(os.path.join(d, "EXECUTION_RECORD.json"), "w"))
    open(os.path.join(d, "params.json"), "w").write("{}"); open(os.path.join(d, "SPEC.md"), "w").write("# spec")


def test_superseded_runs_indexed_but_not_cited():
    t = tempfile.mkdtemp(); sim = os.path.join(t, "Report-4-Spirit", "simulation")
    _rec(os.path.join(sim, "iter-1"), "SIM-R4-C3", 1); open(os.path.join(sim, "sim_r4.py"), "w").write("")
    _rec(os.path.join(sim, "superseded-run-1", "iter-1"), "SIM-R4-C3", 1); open(os.path.join(sim, "superseded-run-1", "sim_r4_run1.py"), "w").write("")
    idx = D.simulations(t, "C3")
    assert len(idx) == 2
    sup = [s for s in idx if s["archived"]][0]; cur = [s for s in idx if not s["archived"]][0]
    assert sup["script"].endswith("superseded-run-1/sim_r4_run1.py") and cur["script"].endswith("simulation/sim_r4.py")
    ci = D.check_index(t, "C3")
    assert list(ci) == ["SIM-R4-C3/iter-1#H1"]
