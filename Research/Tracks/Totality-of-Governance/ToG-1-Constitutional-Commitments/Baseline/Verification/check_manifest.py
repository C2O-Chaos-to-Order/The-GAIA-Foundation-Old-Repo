from pathlib import Path
import hashlib
p=Path(__file__).resolve().parents[1]
lines=(p/'Provenance/MANIFEST.sha256').read_text().splitlines()
bad=[]
for line in lines:
    h,name=line.split('  ',1)
    target=p/name
    if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=h:
        bad.append(name)
if bad:
    raise SystemExit('Manifest FAIL: '+repr(bad))
print('Manifest PASS: '+str(len(lines))+' files')
