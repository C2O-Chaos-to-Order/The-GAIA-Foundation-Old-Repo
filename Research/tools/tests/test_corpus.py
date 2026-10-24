"""Integration tests on the real corpus (skipped when Research/Cycles is absent)."""
import csv, json, os
import pytest
from conftest import RESEARCH
from gaia_tools import data as D, validate as V, claimsource as K, maps as M

HAVE = os.path.isdir(os.path.join(RESEARCH, "Cycles"))
pytestmark = pytest.mark.skipif(not HAVE, reason="corpus not present")


def test_validation_has_no_errors():
    rep = V.validate(RESEARCH)
    assert rep["n_errors"] == 0, rep["errors"][:5]


def test_claim_sources_resolve_every_cycle():
    for cid, _ in D.cycles(RESEARCH):
        r = K.check(RESEARCH, cid)
        assert r["n_fail"] == 0, [c for c in r["claims"] if "Fail" in c["results"].values()][:3]


def test_maps_deterministic(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    M.build(RESEARCH, str(a), "test"); M.build(RESEARCH, str(b), "test")
    for root, _, files in os.walk(a):
        for f in files:
            pa = os.path.join(root, f); pb = os.path.join(b, os.path.relpath(pa, a))
            assert open(pa, "rb").read() == open(pb, "rb").read(), pa


def test_matrix_shape(tmp_path):
    M.build(RESEARCH, str(tmp_path), "test")
    cells = list(csv.DictReader(open(tmp_path / "matrix" / "intersections_625.csv")))
    assert len(cells) == 625 and len({c["id"] for c in cells}) == 625
    assert all(c["claims_placed_exactly"] == "0" for c in cells)  # Alchemy/Phase are undefined -> no exact placement
    g = json.load(open(tmp_path / "graph" / "link_graph.json"))
    assert g["center"] == "GAIA" and all(e["label_code"] in ("E", "P", "PS", "H") for e in g["edges"])


@pytest.mark.skipif(os.environ.get("GAIA_RERUN") != "1", reason="slow; set GAIA_RERUN=1 to re-execute all simulations")
def test_rerun_identical():
    from gaia_tools import rerun as R
    for cid, _ in D.cycles(RESEARCH):
        r = R.run_cycle(RESEARCH, cid)
        assert r["all_identical"], [x for x in r["runs"] if not (x["outputs_identical"] and x["checks_identical"])]


@pytest.mark.skipif(not os.environ.get("GAIA_SNAPSHOTS"), reason="set GAIA_SNAPSHOTS to a directory of <source_id>.txt snapshots")
def test_verification_phrases_found_every_cycle():
    for cid, _ in D.cycles(RESEARCH):
        r = K.check(RESEARCH, cid, snapshots=os.environ["GAIA_SNAPSHOTS"])
        bad = [c for c in r["claims"] if c["results"].get("K-phrase") in ("Fail", "Indeterminate")]
        assert not bad, bad[:3]
