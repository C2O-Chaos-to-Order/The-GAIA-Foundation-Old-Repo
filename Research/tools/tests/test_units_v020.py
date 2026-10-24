"""Unit tests for changes in gaia_tools 0.2.0 / data model 1.1.0 (Cycle 2)."""
import jsonschema
from gaia_tools import data as D, validate as V, claimsource as K, __version__, DATA_MODEL_VERSION


def test_versions():
    assert tuple(map(int, __version__.split("."))) >= (0, 2, 0)  # relaxed in 0.3.0 (was ==)


def test_w_prefix_source_ids():
    s = V.load_schemas()["source"]; pat = s["properties"]["source_id"]["pattern"]
    import re
    assert re.match(pat, "W01") and re.match(pat, "V40") and not re.match(pat, "Z01")  # X allowed since 0.3.0, Y since 0.4.0 (was "Y01 invalid" until 0.4.0)


def test_check_ids_may_contain_dots():
    m = D.SIM_REF.match("SIM-R2-C2/iter-5#MR_0.2"); assert m and m.group("chk") == "MR_0.2"


def test_cross_cycle_sim_lookup():
    idx = {"C1": {"SIM-R4-C1/iter-1#V0": {"result": "Pass"}}, "C2": {"SIM-R4-C2/iter-1#V1": {"result": "Pass"}},
           "C0": {"SIM-R7-C0#E3": {"result": "Pass"}}}
    f = lambda c: idx.get(c, {})
    assert D.lookup_sim("SIM-R4-C1/iter-1#V0", "C2", f)["result"] == "Pass"     # carried claim cites a Cycle-1 run
    assert D.lookup_sim("SIM-R4-C2/iter-1#V1", "C2", f)["result"] == "Pass"
    assert D.lookup_sim("C0:SIM-R7-C0#E3", "C2", f)["result"] == "Pass"         # 1.0.0 convention still accepted
    assert D.lookup_sim("SIM-R4-C2/iter-9#V1", "C2", f) is None
    assert D.lookup_sim("S12", "C2", f) is None


def test_phrase_parsing_and_regex():
    assert K.parse_phrases("n/a (simulation claim; verified against execution records)") == []
    assert K.parse_phrases("S23|at least 3.4 billion || V08|3,465 Ma Apex chert") == ["S23|at least 3.4 billion", "V08|3,465 Ma Apex chert"]
    assert K.phrase_found(r"8\.7 million", "An estimated 8.7\n million species")
    assert K.phrase_found("13 (62%", "found 13 (62% of studies")          # invalid regex -> literal fallback
    assert not K.phrase_found(r"8\.7 million", "8x7 million")
