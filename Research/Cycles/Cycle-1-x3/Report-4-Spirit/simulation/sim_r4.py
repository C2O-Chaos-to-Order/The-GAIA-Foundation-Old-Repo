"""SIM-R4 (Cycle 1+): sensitivity of attendance-health associations to unmeasured confounding, and toy sibling / instrument designs.
Estimates are taken from the cited sources; everything else is a model. A sensitivity analysis is not evidence of causation."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def evalue(rr):
    r = 1/rr if rr < 1 else rr; return float(r+np.sqrt(r*(r-1)))
def hr_to_rr(hr): return (1-0.5**np.sqrt(hr))/(1-0.5**np.sqrt(1/hr))   # S14 common-outcome conversion
B = lambda a, b: a*b/(a+b-1)
def as_rr(e):
    return (hr_to_rr(e["est"]), hr_to_rr(e["ci_upper"])) if e.get("common_outcome") else (e["est"], e["ci_upper"])
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    if "evalues" in X:
        out = []
        for e in X["evalues"]["estimates"]:
            rr, ci = as_rr(e); out.append(dict(label=e["label"], source=e["source"], est=e["est"], ci_upper=e["ci_upper"], scale="common-outcome RR" if e.get("common_outcome") else "as reported",
                                               RR=rr, E_point=evalue(rr), E_CI=evalue(ci) if ci < 1 else 1.0))
        res["evalues"] = out
        for e in X["evalues"]["estimates"]:
            if "reported_E" in e:
                mine = [o for o in out if o["label"] == e["label"]][0]
                chk.append(R.chk(f"V_{e['label']}", f"recomputed E-value matches the value reported in {e['source']} ({e['reported_E']}) within 0.02", mine["E_point"], abs(mine["E_point"]-e["reported_E"]) <= 0.02))
        chk.append(R.chk("V0", "E-value formula reproduces the S14 worked example (RR 3.9 -> E-value 7.2 as printed)", evalue(3.9), abs(evalue(3.9)-7.2) < 0.1))
    if "pba" in X:
        b = X["pba"]; rng = np.random.default_rng(b["seed"]); out = []
        for e in X["evalues"]["estimates"] if "evalues" in X else b["estimates"]:
            rr, _ = as_rr(e); a = np.exp(np.abs(rng.normal(b["log_mu"], b["log_sd"], b["n"]))); c = np.exp(np.abs(rng.normal(b["log_mu"], b["log_sd"], b["n"])))
            corr = rr*B(a, c)            # protective estimate: removing confounding moves it toward/over 1
            out.append(dict(label=e["label"], RR=rr, corrected_median=float(np.median(corr)), corrected_q05=float(np.quantile(corr, .05)), corrected_q95=float(np.quantile(corr, .95)), frac_corrected_ge_1=float(np.mean(corr >= 1))))
        res["pba"] = dict(prior=dict(log_mu=b["log_mu"], log_sd=b["log_sd"], note="|N(mu,sd)| on log scale for RR_EU and RR_UD, independent"), results=out)
        if b.get("log_sd_sweep"):
            sw = {}
            for sd in b["log_sd_sweep"]:
                r2 = np.random.default_rng(b["seed"]+1); row = {}
                for e in X["evalues"]["estimates"]:
                    rr, _ = as_rr(e); a = np.exp(np.abs(r2.normal(b["log_mu"], sd, b["n"]))); c = np.exp(np.abs(r2.normal(b["log_mu"], sd, b["n"])))
                    row[e["label"]] = float(np.mean(rr*B(a, c) >= 1))
                sw[str(sd)] = row
            res["pba"]["sweep_frac_explained_away"] = sw
            chk.append(R.chk("P3", "fraction explained away increases with prior spread for every estimate (monotone in log_sd)", None,
                             all(all(sw[str(x)][k] <= sw[str(y)][k]+1e-9 for x, y in zip(b["log_sd_sweep"], b["log_sd_sweep"][1:])) for k in sw[str(b["log_sd_sweep"][0])])))
        chk.append(R.chk("P1", "bias analysis is monotone: estimates with larger E-values have smaller fractions explained away (Spearman rho < 0)",
                         None, (lambda x, y: float(np.corrcoef(np.argsort(np.argsort(x)), np.argsort(np.argsort(y)))[0, 1]) < 0)([evalue(o["RR"]) for o in out], [o["frac_corrected_ge_1"] for o in out]) if len(out) > 2 else True))
        chk.append(R.chk("P2", "report the fraction of bias-analysis draws in which each association is fully explained away", {o["label"]: round(o["frac_corrected_ge_1"], 3) for o in out}, True, kind="reporting"))
    if "designs" in X:
        d = X["designs"]; rng = np.random.default_rng(d["seed"]); out = {}
        for scen in d["scenarios"]:
            nf, beta = d["n_families"], scen["beta"]
            F = rng.normal(size=nf); F = np.repeat(F, 2); U = rng.normal(size=2*nf)*scen["u_sd"]; Z = rng.normal(size=2*nf)
            A = 0.8*F + scen["u_to_a"]*U + scen["z_to_a"]*Z + rng.normal(size=2*nf)
            Y = beta*A + 0.8*F + scen["u_to_y"]*U + scen["z_to_y"]*Z + rng.normal(size=2*nf)
            ols = np.polyfit(A, Y, 1)[0]
            dA = A[0::2]-A[1::2]; dY = Y[0::2]-Y[1::2]; sfe = float((dA*dY).sum()/(dA*dA).sum())
            iv = float(np.cov(Z, Y)[0, 1]/np.cov(Z, A)[0, 1]); first_F = float((np.corrcoef(Z, A)[0, 1]**2)*(2*nf-2)/(1-np.corrcoef(Z, A)[0, 1]**2))
            out[scen["name"]] = dict(true_beta=beta, naive=float(ols), sibling_FE=sfe, IV=iv, first_stage_F=first_F, bias=dict(naive=float(ols-beta), sibling_FE=sfe-beta, IV=iv-beta))
        res["designs"] = out; s = out
        chk.append(R.chk("S1", "with only family-level confounding, sibling FE is unbiased (|bias|<0.02) and naive OLS is not (|bias|>0.1)", [s["family_only"]["bias"]["sibling_FE"], s["family_only"]["bias"]["naive"]], abs(s["family_only"]["bias"]["sibling_FE"]) < 0.02 and abs(s["family_only"]["bias"]["naive"]) > 0.1))
        chk.append(R.chk("S2", "individual-level confounding biases sibling FE (|bias|>0.05)", s["individual_confounding"]["bias"]["sibling_FE"], abs(s["individual_confounding"]["bias"]["sibling_FE"]) > 0.05))
        chk.append(R.chk("S3", "valid strong instrument recovers beta under individual confounding (|IV bias|<0.03)", s["individual_confounding"]["bias"]["IV"], abs(s["individual_confounding"]["bias"]["IV"]) < 0.03))
        chk.append(R.chk("S4", "exclusion-restriction violation biases IV (|bias|>0.05)", s["exclusion_violated"]["bias"]["IV"], abs(s["exclusion_violated"]["bias"]["IV"]) > 0.05))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
