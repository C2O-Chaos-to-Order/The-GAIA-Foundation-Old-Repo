"""SIM-<PH>-APP: Applied-Sciences simulations (Phases track). Usage: python sim_app.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def clonal_branching(P, rng):
    """Neutral (or selective) birth-death growth from one cell to N cells; each daughter gains Poisson(u) new mutations
    (infinite sites). Mutation tree kept as nodes; cell fraction of each mutation = descendant cells / N.
    Tests the neutral-growth prediction M(f) ~ a (1/f - 1/fmax) for subclonal mutations (cf. P05's neutral-evolution simulation)."""
    parent = [-1]; nmut = [0]; cells = [0]; fit = [1.0]; total = 0
    while 0 < len(cells) < P["N"]:
        k = rng.integers(len(cells)); f = fit[cells[k]]
        b = P["birth"] * f; d = P["death"]
        if rng.random() < b / (b + d):
            node = cells[k]; new = []
            for _ in range(2):
                km = rng.poisson(P["u"])
                if km:
                    parent.append(node); nmut.append(km); total += km
                    fit.append(fit[node] * (1 + P["s"]) if rng.random() < P["p_driver"] else fit[node]); new.append(len(parent) - 1)
                else: new.append(node)
            cells[k] = new[0]; cells.append(new[1])
        else:
            cells[k] = cells[-1]; cells.pop()
    n = len(cells); cnt = np.bincount(cells, minlength=len(parent)).astype(float)
    for i in range(len(parent) - 1, 0, -1): cnt[parent[i]] += cnt[i]
    freq = cnt / max(n, 1); fr = np.repeat(freq[1:], nmut[1:])
    fgrid = np.linspace(P["fmin"], P["fmax"], 12); M = np.array([(fr >= f).sum() for f in fgrid]); X = 1 / fgrid - 1 / P["fmax"]
    a, b0 = np.polyfit(X, M, 1); pred = a * X + b0; r2 = 1 - ((M - pred) ** 2).sum() / max(((M - M.mean()) ** 2).sum(), 1e-12)
    res = dict(final_cells=n, total_mutations=int(total), bookkeeping=int(sum(nmut)), clonal=int((fr >= 0.99).sum()),
               subclonal_in_window=int(((fr >= P["fmin"]) & (fr < P["fmax"])).sum()), M=M.tolist(), r2=float(r2), slope=float(a), mean_mut_per_cell=float(np.repeat(freq[1:], nmut[1:]).sum()))
    c = [chk("V1", "population reached N (no extinction) and mutation bookkeeping is exact", [n, int(total), int(sum(nmut))], n == P["N"] and total == sum(nmut)),
         chk("H1", f"cumulative subclonal mutations M(f) is linear in 1/f on [{P['fmin']}, {P['fmax']}] with R^2 >= {P['h1']}", float(r2), r2 >= P["h1"], "hypothesis"),
         chk("R1", "slope a (estimates mutation rate / effective division ratio) and clonal count", [float(a), res["clonal"]], True, "reporting")]
    return res, c

def _clonal_once(P, rng):
    parent = [-1]; nmut = [0]; cells = [0]; total = 0
    while 0 < len(cells) < P["N"]:
        k = rng.integers(len(cells))
        if rng.random() < P["birth"] / (P["birth"] + P["death"]):
            node = cells[k]; new = []
            for _ in range(2):
                km = rng.poisson(P["u"])
                if km: parent.append(node); nmut.append(km); total += km; new.append(len(parent) - 1)
                else: new.append(node)
            cells[k] = new[0]; cells.append(new[1])
        else:
            cells[k] = cells[-1]; cells.pop()
    n = len(cells)
    if n == 0: return None
    cnt = np.bincount(cells, minlength=len(parent)).astype(float)
    for i in range(len(parent) - 1, 0, -1): cnt[parent[i]] += cnt[i]
    fr = np.repeat(cnt[1:] / n, nmut[1:])
    fgrid = np.linspace(P["fmin"], P["fmax"], 12); M = np.array([(fr >= f).sum() for f in fgrid]); X = 1 / fgrid - 1 / P["fmax"]
    a, b0 = np.polyfit(X, M, 1); pred = a * X + b0; r2 = 1 - ((M - pred) ** 2).sum() / max(((M - M.mean()) ** 2).sum(), 1e-12)
    return dict(n=n, total=int(total), book=int(sum(nmut)), r2=float(r2), slope=float(a))

def clonal_branching_reps(P, rng):
    """Replicates of the neutral clonal_branching model of DV0 (birth-death growth from one cell to N cells, Poisson(u) new
    mutations per daughter, infinite sites; cf. P05's neutral-evolution simulation). Reports the distribution of R^2 of the
    M(f) ~ 1/f fit across replicates (extinct runs are restarted and counted)."""
    runs = []; extinct = 0
    while len(runs) < P["reps"]:
        r = _clonal_once(P, rng)
        if r is None: extinct += 1; continue
        runs.append(r)
    r2 = np.array([r["r2"] for r in runs]); ok = all(r["n"] == P["N"] and r["total"] == r["book"] for r in runs)
    res = dict(r2=r2.tolist(), median_r2=float(np.median(r2)), min_r2=float(r2.min()), frac_ge_h1=float((r2 >= P["h1"]).mean()), slopes=[r["slope"] for r in runs], extinct_restarts=extinct)
    c = [chk("V1", "every replicate reached N cells and mutation bookkeeping is exact", ok, ok),
         chk("H1", f"median R^2 of the M(f) ~ 1/f fit across {P['reps']} replicates >= {P['h1']}", res["median_r2"], res["median_r2"] >= P["h1"], "hypothesis"),
         chk("R1", "R^2 per replicate, slopes, extinct restarts", [res["r2"], res["slopes"], extinct], True, "reporting")]
    return res, c

def euler_stability(P, rng):
    """Numerical divergence of an iterative solver: explicit Euler on y' = -lam y, y(0) = 1, step h. The iteration
    y_{n+1} = (1 - h lam) y_n converges to 0 iff |1 - h lam| < 1 (0 < h lam < 2) and diverges if h lam > 2. Deterministic."""
    out = {}
    for hl in P["hlam"]:
        y = 1.0; traj = []
        for k in range(P["steps"]): y = (1 - hl) * y; traj.append(abs(y))
        out[str(hl)] = dict(final_abs=float(abs(y)), factor=float(abs(1 - hl)), max_abs=float(max(traj)))
    s = [str(x) for x in P["hlam"]]; conv = [k for k in s if float(k) < 2]; div = [k for k in s if float(k) > 2]
    exact = all(abs(out[k]["final_abs"] - abs(1 - float(k)) ** P["steps"]) <= 1e-9 * max(1.0, abs(1 - float(k)) ** P["steps"]) for k in s)
    c = [chk("V1", "final |y| equals |1 - h lam|^steps for every h lam (relative error <= 1e-9)", exact, exact),
         chk("V2", "h lam < 2: |y| -> 0 (final < 1e-6); h lam > 2: |y| grows (final > 1e6)", {k: out[k]["final_abs"] for k in s},
             all(out[k]["final_abs"] < 1e-6 for k in conv) and all(out[k]["final_abs"] > 1e6 for k in div)),
         chk("R1", "amplification factor by h lam", {k: out[k]["factor"] for k in s}, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
