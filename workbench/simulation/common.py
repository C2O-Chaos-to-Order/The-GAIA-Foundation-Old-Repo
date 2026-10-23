import json, hashlib, platform, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def digest(data):return hashlib.sha256(data).hexdigest()
def canonical(value):return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
class Recorder:
    def __init__(self,run_id,script,spec):
        self.run_id=run_id;self.script=Path(script);self.spec=Path(spec);self.tests=[];self.started=datetime.now(timezone.utc).isoformat()
    def check(self,name,actual,expected):
        self.tests.append({'test_id':name,'actual':actual,'expected':expected,'pass':actual==expected})
    def finish(self,metrics,limitations):
        result={'run_id':self.run_id,'invocations_in_this_release':1,'started_utc':self.started,'ended_utc':datetime.now(timezone.utc).isoformat(),'environment':{'python':sys.version,'platform':platform.platform()},'script_sha256':digest(self.script.read_bytes()),'spec_sha256':digest(self.spec.read_bytes()),'shared_code_sha256':digest(Path(__file__).read_bytes()),'randomness':'none','assertions':len(self.tests),'passed':sum(t['pass'] for t in self.tests),'failed':sum(not t['pass'] for t in self.tests),'tests':self.tests,'metrics':metrics,'limitations':limitations,'independent_validation':False}
        path=ROOT/'simulation/results'/f'{self.run_id}.json';path.write_text(json.dumps(result,indent=2,ensure_ascii=False));return result
