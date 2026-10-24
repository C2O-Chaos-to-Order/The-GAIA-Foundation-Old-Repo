"""SIM-<PH>-SOC: Social-Sciences simulations (Phases track). Usage: python sim_soc.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def _clusters(x, gap, min_share):
    xs = np.sort(x); cut = np.where(np.diff(xs) > gap)[0]; groups = np.split(xs, cut + 1)
    return [g for g in groups if len(g) >= min_share * len(x)]

def deffuant(P, rng):
    """Deffuant-Weisbuch bounded-confidence model: random pairs interact if |xi - xj| < eps and move mu toward each other;
    optional Gaussian noise (sd 'noise') per interaction (cf. P03's noisy assimilative influence). Counts major opinion clusters."""
    out = {}
    for eps in P["eps_values"]:
        ks, drift = [], []
        for rep in range(P["reps"]):
            x = rng.uniform(0, 1, P["agents"]); m0 = x.mean()
            for _ in range(P["steps"]):
                i, j = rng.integers(0, P["agents"], 2)
                if i != j and abs(x[i] - x[j]) < eps:
                    d = P["mu"] * (x[j] - x[i]); x[i] += d; x[j] -= d
                    if P["noise"] > 0: x[i] = np.clip(x[i] + rng.normal(0, P["noise"]), 0, 1); x[j] = np.clip(x[j] + rng.normal(0, P["noise"]), 0, 1)
            drift.append(abs(x.mean() - m0)); ks.append(len(_clusters(x, P["gap"], P["min_share"])))
        out[str(eps)] = dict(clusters=ks, mean_clusters=float(np.mean(ks)), max_mean_drift=float(max(drift)))
    lo, hi = str(P["eps_values"][0]), str(P["eps_values"][-1])
    c = [chk("V1", "noise = 0: pairwise updates conserve the mean opinion (|drift| < 1e-9)", max(v["max_mean_drift"] for v in out.values()),
             (max(v["max_mean_drift"] for v in out.values()) < 1e-9) if P["noise"] == 0 else True),
         chk("H1", f"eps = {hi}: every replicate ends in one major cluster (consensus)", out[hi]["clusters"], all(k == 1 for k in out[hi]["clusters"]), "hypothesis"),
         chk("H2", f"eps = {lo}: mean number of major clusters in [{P['h2'][0]}, {P['h2'][1]}] (fragmentation; ~floor(1/(2 eps)))", out[lo]["mean_clusters"],
             P["h2"][0] <= out[lo]["mean_clusters"] <= P["h2"][1], "hypothesis"),
         chk("R1", "clusters per replicate by eps", {k: v["clusters"] for k, v in out.items()}, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
