"""SIM-R5 (Cycle 1+): toy rate models of 'ignition' (global-workspace-like) and local recurrence (RPT-like).
These are dynamical toys: they bear on the logic of signatures (all-or-none vs graded, local vs global), not on experience itself."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
f = lambda z, k: 1/(1+np.exp(-z/k))
def fixed_points(w, th, k):
    r = np.linspace(-0.5, 1.5, 20001); g = (f(w*r-th, k)-r) > 0; return int(np.sum(g[:-1] != g[1:]))
def settle(w, th, k, r0, tau=10.0, dt=0.1, T=400.0):
    r = r0
    for _ in range(int(T/dt)): r = r+dt/tau*(-r+f(w*r-th, k))
    return r
def run_trials(w, th, k, amp, stim_ms, post_ms, sigma, trials, rng, dt=0.1, tau=10.0, mask=0.0, mask_ms=0.0, late_from=200.0):
    n1 = int(stim_ms/dt); nm = int(mask_ms/dt); n2 = int(post_ms/dt); r = np.zeros(trials); acc = np.zeros(trials); cnt = 0
    for i in range(n1+n2):
        I = amp if i < n1 else (-mask if i < n1+nm else 0.0)
        r = r+dt/tau*(-r+f(w*r+I-th, k))+sigma*np.sqrt(dt)/tau*rng.standard_normal(trials)
        if i >= n1+int(late_from/dt): acc += r; cnt += 1
    return acc/cnt
def bimodality(x):
    n = len(x); x = np.asarray(x); m = x.mean(); s = x.std()
    if s < 1e-9: return 0.0
    g = ((x-m)**3).mean()/s**3; kx = ((x-m)**4).mean()/s**4-3
    return float((g*g+1)/(kx+3*(n-1)**2/((n-2)*(n-3))))
def two_area(c, p, amp, rng):
    dt = 0.1; n1 = int(p["stim_ms"]/dt); n2 = int(p["post_ms"]/dt); L = np.zeros(p["trials"]); G = np.zeros(p["trials"]); aL = np.zeros_like(L); aG = np.zeros_like(G); cnt = 0
    for i in range(n1+n2):
        I = amp if i < n1 else 0.0
        L, G = (L+dt/p["tau"]*(-L+f(p["wL"]*L+c*G+I-p["thL"], p["kappa"]))+p["sigma"]*np.sqrt(dt)/p["tau"]*rng.standard_normal(L.shape),
                G+dt/p["tau"]*(-G+f(p["wG"]*G+c*L-p["thG"], p["kappa"]))+p["sigma"]*np.sqrt(dt)/p["tau"]*rng.standard_normal(G.shape))
        if i >= n1+int(200/dt): aL += L; aG += G; cnt += 1
    return aL/cnt, aG/cnt
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []; k = P["kappa"]
    if "phase" in X:
        ph = X["phase"]; cells = []; agree = 0
        for w in ph["w"]:
            for th in ph["theta"]:
                nfp = fixed_points(w, th, k); lo = settle(w, th, k, 0.0); hi = settle(w, th, k, 1.0); bist = abs(hi-lo) > 0.2
                cells.append(dict(w=w, theta=th, n_fixed_points=nfp, sim_bistable=bool(bist))); agree += (nfp == 3) == bist
        res["phase"] = dict(cells=cells, frac_bistable=float(np.mean([c["sim_bistable"] for c in cells])), agreement=agree/len(cells))
        chk.append(R.chk("P1", "simulated bistability matches the fixed-point count (3 fixed points <=> two stable states) in every cell", agree/len(cells), agree == len(cells)))
        chk.append(R.chk("P2", "the C0 weak network (w=2, theta=4) is monostable and the strong one (w=8, theta=4) bistable", None,
                         fixed_points(2, 4, k) == 1 and fixed_points(8, 4, k) == 3))
    if "masking" in X:
        m = X["masking"]; rng = np.random.default_rng(m["seed"]); out = {}
        for net, w in (("strong", m["w_strong"]), ("weak", m["w_weak"])):
            rows = []
            for amp in m["amps"]:
                for dur in m["stim_ms"]:
                    late = run_trials(w, m["theta"], k, amp, dur, m["post_ms"], m["sigma"], m["trials"], rng, mask=m["mask"], mask_ms=m["mask_ms"])
                    rows.append(dict(amp=amp, stim_ms=dur, frac_high=float((late > 0.5).mean()), mean=float(late.mean()), BC=bimodality(late)))
            out[net] = rows
        res["masking"] = out
        mid = [r for r in out["strong"] if 0.2 <= r["frac_high"] <= 0.8]
        res["masking"]["strong_threshold_cells"] = mid
        chk.append(R.chk("K1", "strong network: near threshold (20-80% ignition) late activity is bimodal (BC > 0.555)", [round(r["BC"], 3) for r in mid], len(mid) > 0 and all(r["BC"] > 0.555 for r in mid), kind="hypothesis"))
        chk.append(R.chk("K2", "weak network never ignites (all-or-none signature absent: frac_high = 0 everywhere)", max(r["frac_high"] for r in out["weak"]), max(r["frac_high"] for r in out["weak"]) == 0, kind="hypothesis"))
        dmono = all(a["frac_high"] <= b["frac_high"]+0.1 for amp in m["amps"] for a, b in zip([r for r in out["strong"] if r["amp"] == amp], [r for r in out["strong"] if r["amp"] == amp][1:]))
        chk.append(R.chk("K3", "longer stimulus (before the mask) does not reduce ignition probability (monotone within 0.1)", None, dmono))
    if "two_area" in X:
        t = X["two_area"]; rng = np.random.default_rng(t["seed"]); rows = []
        for c in t["coupling"]:
            L, G = two_area(c, t, t["amp"], rng); rows.append(dict(c=c, frac_local=float((L > 0.5).mean()), frac_global=float((G > 0.5).mean()), frac_local_only=float(((L > 0.5) & (G <= 0.5)).mean())))
        res["two_area"] = rows
        lo = [r for r in rows if r["frac_local_only"] > 0.5]
        res["two_area_local_only_regime"] = [r["c"] for r in lo]
        chk.append(R.chk("A1", "a 'local recurrence without global ignition' regime exists for some coupling (RPT-like signature possible in the toy)", [r["c"] for r in lo], len(lo) > 0, kind="hypothesis"))
        chk.append(R.chk("A2", "global ignition fraction is non-decreasing in coupling (within 0.1)", [r["frac_global"] for r in rows], all(a["frac_global"] <= b["frac_global"]+0.1 for a, b in zip(rows, rows[1:]))))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
