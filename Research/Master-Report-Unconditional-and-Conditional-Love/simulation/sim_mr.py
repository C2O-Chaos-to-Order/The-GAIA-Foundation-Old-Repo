"""SIM-MR-1: conditional vs unconditional cooperation strategies in the iterated PD.
A model of strategies, NOT of love. See run-1/SPEC.md (written before execution)."""
import sys, json, hashlib, datetime, platform, os
import numpy as np
run = sys.argv[1]; P = json.load(open(os.path.join(run, 'params.json')))
T, R, Pp, S = (P['payoffs'][k] for k in 'TRPS'); N = P['rounds']; q = P['gtft_forgive_q']
STRAT = {'ALLC': (1, 1, 1), 'ALLD': (0, 0, 0), 'TFT': (1, 1, 0), 'GTFT': (1, 1, q)}  # (first, after partner C, after partner D)
PAY = {(1, 1): (R, R), (1, 0): (S, T), (0, 1): (T, S), (0, 0): (Pp, Pp)}
def eff(p, e): return p * (1 - e) + (1 - p) * e
def exact(a, b, e):
    A, B = STRAT[a], STRAT[b]
    pa, pb = eff(A[0], e), eff(B[0], e)
    dist = {(1, 1): pa * pb, (1, 0): pa * (1 - pb), (0, 1): (1 - pa) * pb, (0, 0): (1 - pa) * (1 - pb)}
    sa = sb = cc = 0.0
    for t in range(N):
        for k, w in dist.items(): sa += w * PAY[k][0]; sb += w * PAY[k][1]
        cc += dist[(1, 1)]
        nd = {k: 0.0 for k in dist}
        for (x, y), w in dist.items():
            pa = eff(A[1] if y else A[2], e); pb = eff(B[1] if x else B[2], e)
            nd[(1, 1)] += w * pa * pb; nd[(1, 0)] += w * pa * (1 - pb); nd[(0, 1)] += w * (1 - pa) * pb; nd[(0, 0)] += w * (1 - pa) * (1 - pb)
        dist = nd
    return sa / N, sb / N, cc / N
def mc(a, b, e, rng, reps):
    A, B = STRAT[a], STRAT[b]; tot = 0.0
    for _ in range(reps):
        x = rng.random() < eff(A[0], e); y = rng.random() < eff(B[0], e); s = 0
        for t in range(N):
            s += PAY[(int(x), int(y))][0]
            x, y = rng.random() < eff(A[1] if y else A[2], e), rng.random() < eff(B[1] if x else B[2], e)
        tot += s / N
    return tot / reps
names = P['strategies']; started = datetime.datetime.now(datetime.timezone.utc).isoformat()
mats, coop = {}, {}
for e in P['noise_levels']:
    M = np.zeros((4, 4)); C = np.zeros((4, 4))
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            M[i, j], _, C[i, j] = exact(a, b, e)
    mats[e], coop[e] = M, C
ix = {n: i for i, n in enumerate(names)}
def score(M, members): return {n: float(np.mean([M[ix[n], ix[m]] for m in members])) for n in members}
rng = np.random.default_rng(P['mc']['seed']); e5 = 0.05
mcdiff = max(abs(mc(a, b, e5, rng, P['mc']['reps']) - mats[e5][ix[a], ix[b]]) for a in names for b in names)
# replicator
Mr = mats[P['replicator']['noise']]; x = np.ones(4) / 4; dt = P['replicator']['dt']
for g in range(P['replicator']['generations']):
    f = Mr @ x; x = x + dt * x * (f - x @ f); x = np.clip(x, 0, None); x /= x.sum()
s0 = score(mats[0.0], names); s0n = score(mats[0.0], ['ALLC', 'TFT', 'GTFT']); s5n = score(mats[e5], ['ALLC', 'TFT', 'GTFT'])
checks = [
 dict(id='V1', kind='validation', expect='ALLD vs ALLC = 5 / 0', observed=[mats[0.0][ix['ALLD'], ix['ALLC']], mats[0.0][ix['ALLC'], ix['ALLD']]]),
 dict(id='V2', kind='validation', expect='TFT-TFT 3; TFT vs ALLD 0.995', observed=[mats[0.0][ix['TFT'], ix['TFT']], mats[0.0][ix['TFT'], ix['ALLD']]]),
 dict(id='V3', kind='validation', expect='max |MC - exact| < 0.05 at eps 0.05', observed=mcdiff),
 dict(id='H1', kind='hypothesis', expect='eps 0 with ALLD: ALLC < TFT and ALLC < GTFT', observed=s0),
 dict(id='H2', kind='hypothesis', expect='eps 0.05: TFT-TFT CC < 0.60 and GTFT-GTFT CC >= 0.80', observed=[coop[e5][ix['TFT'], ix['TFT']], coop[e5][ix['GTFT'], ix['GTFT']]]),
 dict(id='H3', kind='hypothesis', expect='replicator: ALLC < 0.01 and TFT+GTFT > 0.5', observed=dict(zip(names, x.tolist()))),
 dict(id='H4', kind='hypothesis', expect='eps 0 no ALLD: identical scores', observed=s0n),
 dict(id='H5', kind='hypothesis', expect='eps 0.05 no ALLD: ALLC >= TFT', observed=s5n),
 dict(id='R1', kind='reporting', expect='payoff matrices', observed={str(e): np.round(m, 4).tolist() for e, m in mats.items()}),
 dict(id='R2', kind='reporting', expect='replicator end shares', observed=dict(zip(names, np.round(x, 6).tolist()))),
]
ok = [abs(checks[0]['observed'][0] - 5) < 1e-9 and abs(checks[0]['observed'][1]) < 1e-9,
      abs(checks[1]['observed'][0] - 3) < 1e-9 and abs(checks[1]['observed'][1] - 0.995) < 1e-9, mcdiff < 0.05,
      s0['ALLC'] < s0['TFT'] and s0['ALLC'] < s0['GTFT'],
      checks[4]['observed'][0] < 0.60 and checks[4]['observed'][1] >= 0.80,
      x[ix['ALLC']] < 0.01 and x[ix['TFT']] + x[ix['GTFT']] > 0.5,
      max(s0n.values()) - min(s0n.values()) < 1e-9, s5n['ALLC'] >= s5n['TFT']]
for c, k in zip(checks, ok): c['result'] = ('Pass' if k else 'Fail') if c['kind'] == 'validation' else ('Supported' if k else 'Not supported')
for c in checks[8:]: c['result'] = 'Reported'
os.makedirs(os.path.join(run, 'outputs'), exist_ok=True)
out = os.path.join(run, 'outputs', 'results.json'); json.dump(checks, open(out, 'w'), indent=1, default=float)
rec = dict(sim_id='SIM-MR-1', iteration=1, status='executed', started_utc=started, finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  environment=dict(python=platform.python_version(), platform=platform.platform(), numpy=np.__version__), command=f'python simulation/sim_mr.py {run}',
  spec_sha256=hashlib.sha256(open(os.path.join(run, 'SPEC.md'), 'rb').read()).hexdigest(),
  params_sha256=hashlib.sha256(open(os.path.join(run, 'params.json'), 'rb').read()).hexdigest(),
  code_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
  outputs={'outputs/results.json': hashlib.sha256(open(out, 'rb').read()).hexdigest()},
  pre_registered_checks=[{k: c[k] for k in ('id', 'kind', 'expect', 'result')} for c in checks],
  n_validation=3, n_validation_pass=int(sum(map(bool,ok[:3]))), n_hypothesis=5, n_supported=int(sum(map(bool,ok[3:]))), all_validation_passed=bool(all(ok[:3])),
  notes='First invocation (same spec/params) crashed while serialising this record (numpy int64); fixed with int()/bool() casts only, then re-run. Model code unchanged.')
json.dump(rec, open(os.path.join(run, 'EXECUTION_RECORD.json'), 'w'), indent=1)
for c in checks[:8]: print(c['id'], c['result'], json.dumps(c['observed'], default=float)[:200])
print('R2', checks[9]['observed'])
