import hashlib
import json
import math
from pathlib import Path

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(root):
    cfg = json.loads((root / 'config.json').read_text())
    c, radius = cfg['speed_of_light_m_s'], cfg['radius_m']
    modes = cfg['mode_numbers']
    observed = cfg['literature_frequencies_hz']
    ideal = [c * math.sqrt(n * (n + 1)) / (2 * math.pi * radius) for n in modes]
    alpha = observed[0] / ideal[0]
    fitted = [alpha * f for f in ideal]
    rows = [{'mode': n, 'published_summary_hz': o, 'ideal_hz': f, 'fitted_hz': a, 'ideal_relative_error': abs(f - o) / o, 'fitted_relative_error': abs(a - o) / o, 'role': 'calibration' if n == 1 else 'cross_mode_check'} for n, o, f, a in zip(modes, observed, ideal, fitted)]
    checks = {
        'V01': all(math.isfinite(f) and f > 0 for f in ideal) and all(a < b for a, b in zip(ideal, ideal[1:])),
        'V02': all(math.isclose(f * f, (c / (2 * math.pi * radius)) ** 2 * n * (n + 1), rel_tol=1e-12) for n, f in zip(modes, ideal)),
        'V03': all(math.isclose(c * math.sqrt(n * (n + 1)) / (2 * math.pi * radius * 1.01), f / 1.01, rel_tol=1e-12) for n, f in zip(modes, ideal)),
        'V04': math.isclose(fitted[0], observed[0], abs_tol=1e-10),
        'H01': all(r['ideal_relative_error'] <= cfg['relative_error_tolerance'] for r in rows),
        'H02': all(r['fitted_relative_error'] <= cfg['relative_error_tolerance'] for r in rows[1:])
    }
    out = root / 'iter-1' / 'outputs'
    out.mkdir(parents=True, exist_ok=True)
    result = {'model_id': cfg['model_id'], 'alpha': alpha, 'modes': rows, 'checks': checks, 'boundary': 'No consciousness or Spirit inference is computed.'}
    result_path = out / 'results.json'
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    record = {'model_id': cfg['model_id'], 'iteration': 1, 'inputs_sha256': {p: sha(root / p) for p in ['SPEC.md', 'config.json', 'tools/model.py']}, 'output_sha256': sha(result_path), 'checks': checks, 'execution_kind': 'Reconstructed deterministic analytic evaluation; not raw-data replication'}
    (root / 'iter-1' / 'EXECUTION_RECORD.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    return result

if __name__ == '__main__':
    run(Path(__file__).resolve().parents[1])
