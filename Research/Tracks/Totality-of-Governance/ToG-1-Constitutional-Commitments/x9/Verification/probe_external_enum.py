import ast, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
tree=ast.parse((root/'simulation/run.py').read_text())
fn=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='assess')
assignment=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='fields' for t in n.targets))
namespace={'fields':ast.literal_eval(assignment.value)}
exec(compile(ast.Module(body=[fn],type_ignores=[]),'exact_delivered_assess','exec'),namespace)
valid=json.loads((root/'simulation/iter-1/outputs/transfer.json').read_text())['structured_record']
rows=[]
for value in ['UNRECOGNIZED',None,True]:
    decision,reasons=namespace['assess'](dict(valid),value)
    rows.append({'input':value,'actual':decision,'expected':'Must not PASS','result':'FAIL' if decision=='PASS' else 'PASS','reasons':reasons})
print(json.dumps(rows,indent=2))
raise SystemExit(1 if any(x['result']=='FAIL' for x in rows) else 0)
