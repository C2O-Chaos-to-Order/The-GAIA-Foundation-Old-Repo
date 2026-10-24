"""SIM-<PH>-PHI: Philosophy-Spirituality simulations (Phases track): formal models of conceptual structure only. Usage: python sim_phi.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def crp_one_many(P, rng):
    """Chinese restaurant process (concentration alpha): a formal 'one -> many' branching process starting from a single group.
    It models no tradition: it only tests formal properties a 'divergence from a single source' reading would need
    (unbounded but slow growth of the number of branches; persistence of a dominant branch)."""
    Ks, top, H = [], [], []
    for _ in range(P["reps"]):
        sizes = [1]
        for i in range(1, P["n"]):
            if rng.random() < P["alpha"] / (P["alpha"] + i): sizes.append(1)
            else:
                s = np.array(sizes, float); sizes[rng.choice(len(sizes), p=s / s.sum())] += 1
        s = np.array(sizes, float) / P["n"]; Ks.append(len(sizes)); top.append(s.max()); H.append(float(-(s * np.log(s)).sum()))
    EK = sum(P["alpha"] / (P["alpha"] + i) for i in range(P["n"]))
    res = dict(mean_K=float(np.mean(Ks)), expected_K=float(EK), alpha_ln_n=float(P["alpha"] * np.log(P["n"])), mean_top_share=float(np.mean(top)), mean_entropy=float(np.mean(H)))
    c = [chk("V1", "mean number of branches within 5% of the analytic sum alpha/(alpha+i)", res["mean_K"], abs(res["mean_K"] / EK - 1) <= 0.05),
         chk("H1", f"a dominant branch persists: mean largest-branch share > {P['h1']}", res["mean_top_share"], res["mean_top_share"] > P["h1"], "hypothesis"),
         chk("R1", "entropy of the final partition and alpha ln n reference", [res["mean_entropy"], res["alpha_ln_n"]], True, "reporting")]
    return res, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
