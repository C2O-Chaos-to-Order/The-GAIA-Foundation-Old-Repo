"""SIM-<PH>-NAT: Natural-Sciences simulations (Phases track). Usage: python sim_nat.py iter-<k> (from Natural-Sciences/simulation/)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def wf_divergence(P, rng):
    """Two-deme Wright-Fisher model, L independent biallelic neutral loci, 2N gene copies per deme, symmetric migration m
    per generation (gene copies replaced by migrants before drift). Returns Fst = (HT - HS)/HT averaged over loci, and
    within-deme heterozygosity decay. A toy population-genetic model; it does not model Heliconius genomes (P01)."""
    N2 = 2 * P["N"]; L = P["loci"]; T = P["generations"]; out = {}
    for lab, m in (("no_migration", 0.0), ("migration", P["m"])):
        p0 = rng.uniform(0.2, 0.8, L); p = np.vstack([p0, p0]).astype(float); H0 = 2 * p0 * (1 - p0); traj = []
        for t in range(1, T + 1):
            pm = (1 - m) * p + m * p[::-1]
            p = rng.binomial(N2, pm) / N2
            if t in P["checkpoints"]:
                hs = (2 * p * (1 - p)).mean(0); pb = p.mean(0); ht = 2 * pb * (1 - pb); ok = ht > 0
                traj.append(dict(t=t, fst=float(np.mean((ht[ok] - hs[ok]) / ht[ok])) if ok.any() else None,
                                 het_ratio=float((2 * p * (1 - p)).mean() / H0.mean())))
        out[lab] = traj
    t_end = P["checkpoints"][-1]; exp_ratio = (1 - 1 / N2) ** t_end
    obs_ratio = out["no_migration"][-1]["het_ratio"]; fst0 = out["no_migration"][-1]["fst"]; fstm = out["migration"][-1]["fst"]
    Nm = P["N"] * P["m"]
    c = [chk("V1", f"m = 0: within-deme heterozygosity ratio at t={t_end} within 10% (relative) of (1-1/2N)^t = {exp_ratio:.4f}", obs_ratio, abs(obs_ratio / exp_ratio - 1) <= 0.10),
         chk("H1", f"without gene flow the demes diverge: Fst at t={t_end} > {P['h1']}", fst0, fst0 > P["h1"], "hypothesis"),
         chk("H2", f"with gene flow Nm = {Nm:g}: Fst at t={t_end} < {P['h2']} (divergence held back by migration)", fstm, fstm < P["h2"], "hypothesis"),
         chk("R1", "island-model reference 1/(1+4Nm) (infinite-island formula; two demes differ)", 1 / (1 + 4 * Nm), True, "reporting")]
    return out, c

def wf_selection(P, rng):
    """Two-deme Wright-Fisher model (2N gene copies per deme, symmetric migration m) with one locus under divergent selection
    (allele A has relative fitness 1+s in deme 1 and 1/(1+s)... implemented as genic selection: p' = p(1+s)/(1+s p) in deme 1 and
    p' = p/(1+s(1-p)) in deme 2) plus neutral loci, all unlinked. Replicates of the selected locus are independent runs.
    Toy model of a 'genomic island of divergence': it does not model linkage, recombination or any real genome (P01)."""
    N2 = 2 * P["N"]; T = P["generations"]; out = {}
    def fst(p):
        hs = (2 * p * (1 - p)).mean(0); pb = p.mean(0); ht = 2 * pb * (1 - pb); ok = ht > 0
        return float(np.mean((ht[ok] - hs[ok]) / ht[ok])) if ok.any() else 0.0, (ht - hs)[ok] / ht[ok] if ok.any() else np.array([0.0])
    for s in P["s_values"]:
        R = P["reps"]; p0 = rng.uniform(0.2, 0.8, R); ps = np.vstack([p0, p0]).astype(float)
        q0 = rng.uniform(0.2, 0.8, P["loci"]); pn = np.vstack([q0, q0]).astype(float); m = P["m"]
        for t in range(T):
            ps = (1 - m) * ps + m * ps[::-1]; pn = (1 - m) * pn + m * pn[::-1]
            a = ps[0] * (1 + s) / (1 + s * ps[0]); b = ps[1] / (1 + s * (1 - ps[1])); ps = np.vstack([a, b])
            ps = rng.binomial(N2, ps) / N2; pn = rng.binomial(N2, pn) / N2
        f_sel, per_sel = fst(ps); f_neu, per_neu = fst(pn)
        out[str(s)] = dict(fst_selected=f_sel, fst_selected_se=float(per_sel.std(ddof=1) / np.sqrt(len(per_sel))) if len(per_sel) > 1 else 0.0,
                          fst_neutral=f_neu, fst_neutral_se=float(per_neu.std(ddof=1) / np.sqrt(len(per_neu))) if len(per_neu) > 1 else 0.0)
    z = out[str(P["s_values"][0])]; hi = out[str(P["s_values"][-1])]
    diff0 = abs(z["fst_selected"] - z["fst_neutral"]); se0 = (z["fst_selected_se"] ** 2 + z["fst_neutral_se"] ** 2) ** 0.5; k = P["tol_se"]
    sel = [out[str(s)]["fst_selected"] for s in P["s_values"]]
    c = [chk("V1", f"s = {P['s_values'][0]}: selected-locus Fst equals neutral Fst within {k} combined standard errors (code check: selection switched off)", [diff0, k * se0], diff0 <= k * se0),
         chk("H1", f"s = {P['s_values'][-1]}, Nm = {P['N']*P['m']:g}: selected-locus Fst > {P['h1']} while neutral Fst < {P['h2']} (an island of divergence)", [hi["fst_selected"], hi["fst_neutral"]],
             hi["fst_selected"] > P["h1"] and hi["fst_neutral"] < P["h2"], "hypothesis"),
         chk("H2", "selected-locus Fst is non-decreasing in s across the grid (tolerance 0.02)", sel, all(sel[i + 1] >= sel[i] - 0.02 for i in range(len(sel) - 1)), "hypothesis"),
         chk("R1", "Fst by s (selected, neutral) and m", {k2: [v["fst_selected"], v["fst_neutral"]] for k2, v in out.items()}, True, "reporting")]
    return out, c

def pitchfork_landscape(P, rng):
    """Waddington-style landscape as a formal toy (cf. P10's 'marble rolling down a rugged hillside'): cells follow
    dx = (a(t) x - x^3 + bias) dt + sigma dW, with a(t) ramping from a0 < 0 (one valley) to a1 > 0 (two valleys: a pitchfork
    bifurcation). Records the fraction of cells ending in the right-hand valley. No biological gene network is modelled."""
    n = P["cells"]; dt = P["dt"]; steps = int(P["T"] / dt); out = {}
    for bias in P["biases"]:
        x = np.zeros(n)
        for k in range(steps):
            a = P["a0"] + (P["a1"] - P["a0"]) * k / steps
            x = x + (a * x - x ** 3 + bias) * dt + P["sigma"] * np.sqrt(dt) * rng.normal(size=n)
        fr = float((x > 0).mean()); out[str(bias)] = dict(frac_right=fr, se=float(np.sqrt(fr * (1 - fr) / n)), mean_abs_x=float(np.abs(x).mean()))
    z = out["0.0"]; k = P["tol_se"]; seb = np.sqrt(0.25 / n); hb = out[str(P["biases"][-1])]
    c = [chk("V1", f"bias 0 (symmetric landscape): fraction in the right valley within {k} binomial standard errors of 0.5", [z["frac_right"], 0.5, k * seb], abs(z["frac_right"] - 0.5) <= k * seb),
         chk("V2", f"after the bifurcation cells sit near the valley floors: mean |x| within 10% of sqrt(a1) = {np.sqrt(P['a1']):.4f}", z["mean_abs_x"], abs(z["mean_abs_x"] / np.sqrt(P["a1"]) - 1) <= 0.10),
         chk("H1", f"a small bias {P['biases'][-1]} applied during the ramp sends > {P['h1']} of cells into one valley (sensitivity near the bifurcation)", hb["frac_right"], hb["frac_right"] > P["h1"], "hypothesis"),
         chk("R1", "fraction right by bias", {k2: v["frac_right"] for k2, v in out.items()}, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
