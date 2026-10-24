"""Validate every cycle's claims, sources, links, simulation index and execution records.

Usage:  python -m gaia_tools.validate <Research dir> [--out report.json]
Two layers: (1) JSON Schema (data model 1.0.0, gaia_tools/schemas/), (2) cross-file integrity rules:
  V1 claim IDs unique within a cycle; claim.report matches its report folder
  V2 every literature source ID cited by a claim exists in that cycle's SOURCE_REGISTER
  V3 every SIM citation resolves to a pre-registered check (C0: prefix -> Cycle 0 records)
  V4 every link basis claim ID exists in that cycle
  V5 each report's sources.csv rows are byte-for-byte rows of the register (same fields, same values)
  V6 execution-record output hashes match files on disk; params_sha256 (iteration records) matches params.json
Quality warnings (reported, do not fail validation):
  Q1 empty counterevidence_limits   Q2 access_mode outside the controlled prefixes   Q3 dash placeholder rejection criterion
  Q4 archived run whose output was renamed after archiving (matched by SHA-256 to another file in the archive folder)
Exit code 0 only if there are zero errors."""
import argparse, json, os, sys
from importlib import resources
import jsonschema
from . import data as D


def load_schemas():
    out = {}
    for n in ("claim", "source", "link", "execution_record", "simulation"):
        with resources.files("gaia_tools.schemas").joinpath(f"{n}.schema.json").open() as f:
            out[n] = json.load(f)
    return out


def _validator(schema):
    return jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())


def norm_claim(r):
    o = {k: v for k, v in r.items() if not k.startswith("_")}
    o["source_ids"] = D.split_ids(o.get("source_ids"))
    o["cross_links"] = D.split_ids(o.get("cross_links"))
    return o


def norm_link(r):
    o = dict(r)
    o["basis"] = D.split_ids(o.get("basis"))
    return o


def validate(research_dir):
    S = load_schemas(); V = {k: _validator(s) for k, s in S.items()}
    errors, warnings, counts = [], [], {}
    cyc = D.cycles(research_dir)
    c0_checks = D.check_index(cyc[0][1], cyc[0][0]) if cyc else {}

    def err(cycle, kind, ident, msg):
        errors.append(dict(cycle=cycle, kind=kind, id=ident, error=msg))

    def warn(cycle, kind, ident, msg):
        warnings.append(dict(cycle=cycle, kind=kind, id=ident, warning=msg))

    for cid, cp in cyc:
        cl, src, lk = D.claims(cp), D.sources(cp), D.links(cp)
        sims = D.simulations(cp, cid); checks = D.check_index(cp, cid)
        reg = {s["source_id"]: s for s in src}
        n = dict(claims=len(cl), sources=len(src), links=len(lk), simulations=len(sims), execution_records=len(sims))
        counts[cid] = n
        for r in cl:
            for e in V["claim"].iter_errors(norm_claim(r)):
                err(cid, "schema:claim", r.get("claim_id"), e.message)
            if not r.get("counterevidence_limits", "").strip():
                warn(cid, "Q1", r.get("claim_id"), "counterevidence_limits is empty")
        for s in src:
            for e in V["source"].iter_errors(s):
                err(cid, "schema:source", s.get("source_id"), e.message)
            if not s.get("access_mode", "").startswith(("full text", "abstract only", "excerpt")):
                warn(cid, "Q2", s.get("source_id"), f"access_mode outside controlled prefixes: {s.get('access_mode')!r}")
        for l in lk:
            for e in V["link"].iter_errors(norm_link(l)):
                err(cid, "schema:link", l.get("link_id"), e.message)
            if l.get("rejection_criterion", "").strip() in ("-", "\u2014", "\u2013"):
                warn(cid, "Q3", l.get("link_id"), f"rejection criterion is a placeholder (label {l.get('framework_label')})")
        for s in sims:
            for e in V["simulation"].iter_errors(s):
                err(cid, "schema:simulation", s["directory"], e.message)
            rec = json.load(open(os.path.join(cp, s["execution_record"])))
            for e in V["execution_record"].iter_errors(rec):
                err(cid, "schema:execution_record", s["execution_record"], e.message)
            # V6
            rd = os.path.join(cp, s["directory"])
            for rel, h in rec.get("outputs", {}).items():
                p = os.path.join(rd, rel)
                if not os.path.exists(p):
                    alt = [f for f in os.listdir(rd) if os.path.isfile(os.path.join(rd, f)) and D.sha256_file(os.path.join(rd, f)) == h]
                    if s["archived"] and alt:
                        warn(cid, "Q4", s["execution_record"], f"archived output {rel} renamed to {alt[0]} (SHA-256 matches)")
                    else:
                        err(cid, "V6", s["execution_record"], f"output missing: {rel}")
                elif D.sha256_file(p) != h:
                    err(cid, "V6", s["execution_record"], f"output hash mismatch: {rel}")
            if "params_sha256" in rec and s["params_sha256"] != rec["params_sha256"]:
                err(cid, "V6", s["execution_record"], "params_sha256 mismatch")
        # V1
        seen = set()
        for r in cl:
            if r["claim_id"] in seen:
                err(cid, "V1", r["claim_id"], "duplicate claim_id")
            seen.add(r["claim_id"])
            if r["report"] != r["_report_dir"]:
                err(cid, "V1", r["claim_id"], f"report {r['report']} stored under {r['_report_dir']}")
        # V2, V3
        for r in cl:
            for sid in D.split_ids(r["source_ids"]):
                m = D.SIM_REF.match(sid)
                if m:
                    key = sid[3:] if m.group("c0") else sid
                    pool = c0_checks if m.group("c0") else checks
                    if key not in pool:
                        err(cid, "V3", r["claim_id"], f"unresolved simulation citation {sid}")
                elif sid not in reg:
                    err(cid, "V2", r["claim_id"], f"source {sid} not in register")
        # V4
        for l in lk:
            for b in D.split_ids(l["basis"]):
                if b not in seen:
                    err(cid, "V4", l["link_id"], f"basis claim {b} not found")
        # V5
        for rid, rows in D.report_sources(cp).items():
            for s in rows:
                if reg.get(s["source_id"]) != s:
                    err(cid, "V5", f"{rid}:{s['source_id']}", "report sources.csv row differs from register")
    return dict(data_model="1.0.0", cycles=counts, n_errors=len(errors), n_warnings=len(warnings), errors=errors, warnings=warnings)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("research_dir"); ap.add_argument("--out")
    a = ap.parse_args(argv)
    rep = validate(a.research_dir)
    s = json.dumps(rep, indent=1, ensure_ascii=False)
    if a.out:
        open(a.out, "w").write(s + "\n")
    print(json.dumps({"cycles": rep["cycles"], "n_errors": rep["n_errors"], "n_warnings": rep["n_warnings"]}))
    for e in rep["errors"][:50]:
        print(e)
    return 0 if rep["n_errors"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
