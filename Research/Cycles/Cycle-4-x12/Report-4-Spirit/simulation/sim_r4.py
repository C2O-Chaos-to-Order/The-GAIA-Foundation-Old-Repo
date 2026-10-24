"""SIM-R4-C4: negative-control designs for the attendance -> mortality question (carried item 'R4 negative-control designs').
Structure from Lipsitch, Tchetgen Tchetgen & Cohen 2010 (Y03: negative-control outcomes and exposures share the confounding structure
of the primary analysis but cannot be caused by the exposure / cannot cause the outcome) and Arnold et al. 2016 (Y04: negative controls
for selection bias). Synthetic cohort: unmeasured binary confounder U (e.g. underlying health / social engagement) raises attendance A
and lowers death D; negative-control outcome N (an outcome attendance cannot plausibly affect) shares U; negative-control exposure B
(an attendance-like behaviour with no effect) shares U. Odds ratios from 2x2 tables with Woolf 95% CI. Nothing fitted to real data."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
def expit(x): return 1 / (1 + np.exp(-x))
def cohort(rng, n, pU=0.5, gA=1.0, gD=1.0, gN=1.0, gB=1.0, bAD=0.0, pA=0.35, pD=0.10, pN=0.10, pB=0.35, sel=None):
    U = rng.random(n) < pU; lg = lambda p: np.log(p / (1 - p))
    A = rng.random(n) < expit(lg(pA) + gA * (U - pU)); B = rng.random(n) < expit(lg(pB) + gB * (U - pU))
    D = rng.random(n) < expit(lg(pD) - gD * (U - pU) + bAD * (A - pA)); N = rng.random(n) < expit(lg(pN) - gN * (U - pU))
    keep = np.ones(n, bool) if sel is None else rng.random(n) < expit(sel[0] + sel[1] * A + sel[2] * U)
    return dict(U=U[keep], A=A[keep], B=B[keep], D=D[keep], N=N[keep])
def orci(x, y):
    a = np.sum(x & y) + .5; b = np.sum(x & ~y) + .5; c = np.sum(~x & y) + .5; d = np.sum(~x & ~y) + .5
    o = a * d / (b * c); se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d); return float(o), float(np.exp(np.log(o) - 1.96 * se)), float(np.exp(np.log(o) + 1.96 * se))
def detect(x, y): o, l, h = orci(x, y); return not (l <= 1 <= h)
def power(seed, reps, n, out="N", expo="A", **kw):
    rng = np.random.default_rng(seed); hits = []; ors = []
    for _ in range(reps):
        c = cohort(rng, n, **kw); hits.append(detect(c[expo], c[out])); ors.append(orci(c[expo], c[out])[0])
    return float(np.mean(hits)), float(np.median(ors))
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; C = []; res = {}; k = P["iteration"]
    if k == 1:
        rng = np.random.default_rng(1); c = cohort(rng, 400000, gA=0, gD=0, gN=0, gB=0); oD = orci(c["A"], c["D"])[0]; oN = orci(c["A"], c["N"])[0]
        c2 = cohort(rng, 400000, gA=1, gD=1, bAD=-0.5); s = c2["U"]; oS = [orci(c2["A"][s == u], c2["D"][s == u])[0] for u in (0, 1)]
        res.update(or_null_D=oD, or_null_N=oN, or_strata=oS, true_or=float(np.exp(-0.5)))
        C += [R.chk("V1", "no confounding, no effect: OR(A,D) and OR(A,N) within 3% of 1", [oD, oN], abs(oD - 1) < .03 and abs(oN - 1) < .03),
              R.chk("V2", "U-stratified OR recovers the true conditional OR exp(-0.5)=0.607 within 5% in both strata", oS, all(abs(o / np.exp(-0.5) - 1) < .05 for o in oS))]
    elif k == 2:
        pw, orN = power(2, X["reps"], X["n"], gA=X["g"], gD=X["g"], gN=X["g"]); _, orD = power(2, X["reps"], X["n"], out="D", gA=X["g"], gD=X["g"])
        res.update(power_NCO=pw, median_or_D=orD, median_or_N=orN)
        C += [R.chk("H2", "confounding only (no true effect): the negative-control outcome flags it in >= 80% of cohorts (n = 10,000)", pw, pw >= .8, "hypothesis"), R.chk("H2r", "median spurious OR(A,D)", orD, True, "reporting")]
    elif k == 3:
        pw, _ = power(3, X["reps"], X["n"], gA=0, gD=0, gN=0, bAD=-0.5); res.update(false_flag=pw)
        C += [R.chk("V3", "no confounding, true protective effect: NCO false-flag rate within 2-8% (nominal 5%)", pw, .02 <= pw <= .08)]
    elif k == 4:
        out = []
        for gN in X["gN"]:
            rng = np.random.default_rng(40); c = cohort(rng, X["n"], gA=1, gD=1, gN=gN, bAD=X["b"]); oD = orci(c["A"], c["D"])[0]; oN = orci(c["A"], c["N"])[0]
            out.append(dict(gN=gN, or_D=oD, or_N=oN, corrected=oD / oN, true=float(np.exp(X["b"]))))
        res.update(table=out); ok = [abs(o["corrected"] / o["true"] - 1) < .1 for o in out]
        C += [R.chk("H4", "ratio correction OR_D/OR_N is within 10% of the truth only when U acts equally on N and D (gN = gD = 1)", ok, ok == [g == 1.0 for g in X["gN"]], "hypothesis"), R.chk("H4r", "corrected ORs", [round(o["corrected"], 3) for o in out], True, "reporting")]
    elif k == 5:
        pw, orB = power(5, X["reps"], X["n"], out="D", expo="B", gA=1, gD=1, gB=1); res.update(power_NCE=pw, median_or_B=orB)
        C += [R.chk("H5", "negative-control exposure (behaviour with no effect, shares U) flags confounding in >= 80% of cohorts", pw, pw >= .8, "hypothesis")]
    elif k == 6:
        pw, orN = power(6, X["reps"], X["n"], gA=0, gD=0, gN=0, sel=X["sel"]); _, orD = power(6, X["reps"], X["n"], out="D", gA=0, gD=0, gN=0, sel=X["sel"])
        res.update(power_sel=pw, median_or_N=orN, median_or_D=orD)
        C += [R.chk("H6", "selection that depends on attendance and on U (Y04) is flagged by the NCO in >= 80% of cohorts", pw, pw >= .8, "hypothesis")]
    elif k == 7:
        out = {}
        for g in X["g"]:
            pw, orD = power(70, X["reps"], X["n"], gA=g, gD=g, gN=g); out[str(g)] = dict(power=pw, spurious_or_D=orD)
        res.update(by_g=out); weak = out[str(X["g"][0])]
        C += [R.chk("H7", "weak confounding (spurious OR(A,D) about 0.9) is flagged in >= 80% at n = 10,000", weak, weak["power"] >= .8, "hypothesis"), R.chk("H7r", "power by strength", out, True, "reporting")]
    elif k == 8:
        out = {str(n): power(80, X["reps"], n, gA=X["g"], gD=X["g"], gN=X["g"])[0] for n in X["n"]}
        nmin = next((int(n) for n, p in out.items() if p >= .8), None); res.update(power_by_n=out, n80=nmin)
        C += [R.chk("H8", "80% power for the weak-confounding scenario is reached at n <= 50,000", nmin, nmin is not None and nmin <= 50000, "hypothesis")]
    elif k == 9:
        pw, orD = power(9, X["reps"], X["n"], gA=X["g"], gD=X["g"], gN=X["g"], pD=X["p"], pN=X["p"]); res.update(power=pw, median_or_D=orD)
        C += [R.chk("H9", "rare outcomes (2%): NCO power >= 80% at n = 20,000 for a confounder producing a spurious OR near 0.7", pw, pw >= .8, "hypothesis")]
    elif k == 10:
        pw, _ = power(10, X["reps"], X["n"], gA=X["g"], gD=X["g"], gN=X["gN"]); res.update(power=pw)
        C += [R.chk("H10", "imperfect NCO (U acts on N at one third of its effect on D) still flags confounding in >= 80%", pw, pw >= .8, "hypothesis")]
    elif k == 11:
        pw, orN = power(110, X["reps"], X["n"], gA=X["g"], gD=X["g"], gN=X["g"]); res.update(power_NCO=pw)
        C += [R.chk("H11", "replication of iteration 2 with new seeds: power >= 80%", pw, pw >= .8, "hypothesis")]
    elif k == 12:
        rng = np.random.default_rng(12); c = cohort(rng, X["n"], gA=X["g"], gD=X["g"], gN=X["g"], bAD=X["b"]); oD = orci(c["A"], c["D"]); oN = orci(c["A"], c["N"])
        res.update(or_D=oD, or_N=oN, corrected=oD[0] / oN[0], true=float(np.exp(X["b"])))
        C += [R.chk("H12", "with both confounding and a true effect, the NCO still flags bias and the ratio correction lands within 10% of the truth (equal U effects)", [oN, oD[0] / oN[0]], (not (oN[1] <= 1 <= oN[2])) and abs(oD[0] / oN[0] / np.exp(X["b"]) - 1) < .1, "hypothesis")]
    R.finish(H, P, res, C, t0)
if __name__ == "__main__": main()
