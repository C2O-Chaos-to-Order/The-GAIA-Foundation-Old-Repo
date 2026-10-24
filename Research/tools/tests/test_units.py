"""Unit tests on small synthetic inputs (no corpus needed)."""
import json, os
import jsonschema
from gaia_tools import data as D, maps as M, validate as V


def test_sim_ref_parsing():
    m = D.SIM_REF.match("C0:SIM-R1-C0#E2"); assert m and m.group("c0") and m.group("chk") == "E2"
    m = D.SIM_REF.match("SIM-R4-C1/iter-1#V_Chen2021_mortality_pooled"); assert m and m.group("it") == "1"
    assert D.SIM_REF.match("S14") is None


def test_split_ids():
    assert D.split_ids("U04; S01;;") == ["U04", "S01"]
    assert D.split_ids("") == []


def test_git_blob_sha(tmp_path):
    p = tmp_path / "x.txt"; p.write_bytes(b"hello\n")
    assert D.git_blob_sha(str(p)) == "ce013625030ba8dba906f756967f9e9ca394464a"  # `git hash-object` of "hello\n"


def test_claim_schema_accepts_and_rejects():
    s = V.load_schemas()["claim"]; v = jsonschema.Draft202012Validator(s)
    ok = dict(claim_id="C1-R2-03", report="R2", wording="A sufficiently long wording.", claim_class="Empirical",
              framework_label="Established", conclusion_status="Supported", source_ids=["V04", "SIM-R2-C1/iter-1#H1"],
              locator="p. 3", confidence="High", counterevidence_limits="", cross_links=["R5"], verification_phrases="V04|x",
              c1_change="New in Cycle 1.")
    assert not list(v.iter_errors(ok))
    bad = dict(ok, framework_label="Proven", claim_id="X-1")
    assert len(list(v.iter_errors(bad))) >= 2
    hyp = dict(ok, framework_label="Hypothetical", conclusion_status="Supported")
    assert list(v.iter_errors(hyp)), "Hypothetical label must carry Hypothetical status"
    extra = dict(ok, surprise="x")
    assert list(v.iter_errors(extra)), "unknown columns are rejected"


def test_execution_record_schema_kinds():
    s = V.load_schemas()["execution_record"]; v = jsonschema.Draft202012Validator(s)
    base = dict(sim_id="SIM-R1-C1", iteration=1, status="executed", started_utc="2026-10-24T01:00:00+00:00",
                finished_utc="2026-10-24T01:00:01+00:00", environment=dict(python="3.13", platform="Linux"),
                command="python sim.py iter-1", params_sha256="0" * 64, outputs={"outputs/results.json": "a" * 64},
                pre_registered_checks=[dict(id="G1", kind="validation", expect="xyz", observed=1, result="Pass")],
                n_checks=1, all_validation_passed=True)
    assert not list(v.iter_errors(base))
    wrong = json.loads(json.dumps(base)); wrong["pre_registered_checks"][0]["result"] = "Supported"
    assert list(v.iter_errors(wrong)), "a validation check cannot be 'Supported'"
    nokind = json.loads(json.dumps(base)); del nokind["pre_registered_checks"][0]["kind"]
    assert list(v.iter_errors(nokind)), "iteration records need typed checks"


def test_lens_rules_word_start():
    rules = M.lens_rules()
    assert M.lenses_for("Replication rates were measured", rules) == ["Truth"]
    assert "Love" not in M.lenses_for("a careful career", rules)      # 'care\\b' must not match 'careful'/'career'
    assert M.lenses_for("hun and po souls", rules) == []


def test_change_classification():
    p = dict(framework_label="Established", conclusion_status="Supported", wording="w", source_ids="S1")
    assert M.classify_claim_change(None, p, "") == "new"
    assert M.classify_claim_change(p, None, "") == "dropped"
    assert M.classify_claim_change(p, dict(p, framework_label="Plausible"), "").startswith("weakened")
    assert M.classify_claim_change(dict(p, framework_label="Plausible"), p, "").startswith("strengthened (label")
    assert M.classify_claim_change(p, dict(p, source_ids="V1;S1"), "Upgraded to full text V1.").startswith("strengthened (full-text")
    assert M.classify_claim_change(p, dict(p), "Carried forward unchanged") == "unchanged"
