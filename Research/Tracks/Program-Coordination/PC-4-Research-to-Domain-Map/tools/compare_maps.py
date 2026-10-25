#!/usr/bin/env python3
"""Exploratory (not pre-registered): matcher agreement of two judgment maps under each variant.
Usage: compare_maps.py CYCLE_DIR MAP_A MAP_B  (paths relative to the PC-4 folder)"""
import json, os, sys, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pc4
cyc, a, b = sys.argv[1:4]
cfg = json.load(open(os.path.join(cyc, "config.json")))
print("| Map | Variant | top-1 | top-3 primary | top-3 any | n |\n|---|---|---|---|---|---|")
for mp in (a, b):
    for v in ("charter", "title_purpose", "title"):
        tmp = tempfile.mkdtemp()
        c = dict(cfg, judgment_map=os.path.relpath(mp, cyc), clusters=None, checks=[],
                 queue_named_checks=False, iterations={"1": {"variant": v, "stem": True, "k": 3}})
        json.dump(c, open(os.path.join(tmp, "config.json"), "w"))
        c["work_queue"] = os.path.relpath(os.path.normpath(os.path.join(cyc, cfg["work_queue"])), tmp)
        c["judgment_map"] = os.path.relpath(os.path.abspath(mp), tmp)
        json.dump(c, open(os.path.join(tmp, "config.json"), "w"))
        m = pc4.run(tmp, 1, outdir=os.path.join(tmp, "o"))["metrics"]
        print(f"| {os.path.basename(mp)} | {v} | {m['top1_rate']} | {m['topk_primary_rate']} | {m['topk_any_rate']} | {m['n_matcher_items']} |")
        shutil.rmtree(tmp)
