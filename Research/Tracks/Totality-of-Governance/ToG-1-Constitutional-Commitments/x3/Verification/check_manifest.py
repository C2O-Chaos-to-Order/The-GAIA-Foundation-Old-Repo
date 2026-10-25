from pathlib import Path
import hashlib
root=Path(__file__).resolve().parents[1]
items=(root/'Provenance/MANIFEST.sha256').read_text().splitlines()
bad=[]
for line in items:
    expected,name=line.split('  ',1)
    p=(root/name).resolve()
    if not p.is_relative_to(root.resolve()) or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
        bad.append(name)
if bad:raise SystemExit('FAIL: '+repr(bad))
print('PASS: '+str(len(items))+' manifest-listed files')
