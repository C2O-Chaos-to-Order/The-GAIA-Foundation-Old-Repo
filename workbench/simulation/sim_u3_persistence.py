import sqlite3, tempfile, io, zipfile, csv
from pathlib import Path
from common import *
from sim_u1_import import inspect, make_zip
SCHEMA="""
PRAGMA foreign_keys=ON;
CREATE TABLE artifacts(path TEXT PRIMARY KEY, sha TEXT NOT NULL, body BLOB NOT NULL, visibility TEXT NOT NULL CHECK(visibility IN ('public','private')));
CREATE TABLE cells(id TEXT PRIMARY KEY, status TEXT NOT NULL, definition TEXT NOT NULL, version INTEGER NOT NULL DEFAULT 1);
CREATE TABLE claims(id TEXT PRIMARY KEY, artifact_path TEXT NOT NULL REFERENCES artifacts(path), status TEXT NOT NULL);
CREATE TABLE nonces(nonce TEXT PRIMARY KEY);
CREATE TABLE intents(id TEXT PRIMARY KEY, state TEXT NOT NULL);
"""
def connect(path):
    db=sqlite3.connect(path,timeout=0);db.execute('PRAGMA foreign_keys=ON');db.execute('PRAGMA journal_mode=DELETE');db.execute('PRAGMA synchronous=FULL');return db
def init(path):
    db=connect(path);db.executescript(SCHEMA);return db
def research_snapshot(db,public_only=False):
    artifacts=db.execute('SELECT path,sha,body,visibility FROM artifacts'+(" WHERE visibility='public'" if public_only else '')+' ORDER BY path').fetchall()
    cells=db.execute('SELECT id,status,definition,version FROM cells ORDER BY id').fetchall()
    claims=db.execute('SELECT id,artifact_path,status FROM claims ORDER BY id').fetchall()
    if public_only:
        paths={a[0] for a in artifacts};claims=[c for c in claims if c[1] in paths]
    return {'artifacts':[(a,b,bytes(c).hex(),d) for a,b,c,d in artifacts],'cells':cells,'claims':claims}
def run():
    rec=Recorder('GAIA-SIM-U3',__file__,ROOT/'simulation/specs/U3.md')
    with tempfile.TemporaryDirectory(prefix='gaia-u3-') as tmp:
        tmp=Path(tmp);path=tmp/'source.db';db=init(path)
        with (ROOT/'maps/categorical_grid_625.csv').open() as f:grid=list(csv.DictReader(f))
        public=[('reports/demo.md',b'Synthetic public report\r\n'),('sources/demo.txt',b'FICTIONAL SOURCE: not external evidence')]
        secret=b'PRIVATE_SENTINEL_SYNTHETIC_7294'
        with db:
            for p,b in public+[('private/belief.txt',secret)]:db.execute('INSERT INTO artifacts VALUES(?,?,?,?)',(p,digest(b),b,'private' if p.startswith('private/') else 'public'))
            for row in grid:db.execute('INSERT INTO cells VALUES(?,?,?,?)',(row['cell_id'],'NOT_ASSESSED',canonical(row).decode(),1))
            db.execute('INSERT INTO claims VALUES(?,?,?)',('DEMO-CL-1','sources/demo.txt','PROPOSED'))
        snapshot_before=research_snapshot(db);db.close();db=connect(path)
        rec.check('restart_snapshot_equal',research_snapshot(db),snapshot_before)
        rec.check('persisted_cells',db.execute('SELECT COUNT(*) FROM cells').fetchone()[0],625)
        rec.check('unassessed_statuses',db.execute("SELECT COUNT(*) FROM cells WHERE status='NOT_ASSESSED'").fetchone()[0],625)
        rec.check('artifact_original_bytes',[bytes(r[0]).hex() for r in db.execute("SELECT body FROM artifacts WHERE visibility='public' ORDER BY path")],[b.hex() for _,b in sorted(public)])
        try:
            with db:db.execute('INSERT INTO cells VALUES(?,?,?,?)',(grid[0]['cell_id'],'SUPPORTED','{}',1))
            caught=False
        except sqlite3.IntegrityError:caught=True
        rec.check('duplicate_stable_id_rejected',caught,True)
        before=db.execute('SELECT COUNT(*) FROM artifacts').fetchone()[0]
        try:
            with db:
                db.execute('INSERT INTO artifacts VALUES(?,?,?,?)',('rollback.tmp',digest(b'tmp'),b'tmp','public'))
                db.execute('INSERT INTO claims VALUES(?,?,?)',('bad-claim','absent-source','PROPOSED'))
            fk_caught=False
        except sqlite3.IntegrityError:fk_caught=True
        rec.check('foreign_key_failure',fk_caught,True)
        rec.check('transaction_rollback',db.execute('SELECT COUNT(*) FROM artifacts').fetchone()[0],before)
        cid=grid[0]['cell_id']
        with db:
            first=db.execute('UPDATE cells SET version=version+1 WHERE id=? AND version=1',(cid,)).rowcount
            stale=db.execute('UPDATE cells SET status=? WHERE id=? AND version=1',('SUPPORTED',cid)).rowcount
        rec.check('optimistic_version_conflict',[first,stale],[1,0])
        rec.check('stale_update_did_not_promote',db.execute('SELECT status FROM cells WHERE id=?',(cid,)).fetchone()[0],'NOT_ASSESSED')
        c1=connect(path);c2=connect(path)
        c1.execute('BEGIN IMMEDIATE');c1.execute('INSERT INTO nonces VALUES(?)',('one-use',))
        try:c2.execute('BEGIN IMMEDIATE');locked=False
        except sqlite3.OperationalError:locked=True
        rec.check('second_writer_blocked_in_interleaving',locked,True)
        c1.commit()
        try:
            with c2:c2.execute('INSERT INTO nonces VALUES(?)',('one-use',))
            duplicate=False
        except sqlite3.IntegrityError:duplicate=True
        rec.check('committed_nonce_replay_rejected',duplicate,True)
        rec.check('exactly_one_nonce_record',db.execute('SELECT COUNT(*) FROM nonces WHERE nonce=?',('one-use',)).fetchone()[0],1)
        c1.close();c2.close()
        with db:db.execute('INSERT INTO intents VALUES(?,?)',('interrupted-fixture','PENDING'))
        db.close();db=connect(path)
        with db:db.execute("UPDATE intents SET state='UNKNOWN_OUTCOME' WHERE state='PENDING'")
        rec.check('recovery_preserves_uncertainty',db.execute('SELECT state FROM intents').fetchone()[0],'UNKNOWN_OUTCOME')
        rec.check('integrity_check',db.execute('PRAGMA integrity_check').fetchone()[0],'ok')
        backup=sqlite3.connect(tmp/'backup.db');db.backup(backup)
        rec.check('backup_research_snapshot',research_snapshot(backup),research_snapshot(db))
        rec.check('backup_unknown_intent',backup.execute('SELECT state FROM intents').fetchone()[0],'UNKNOWN_OUTCOME');backup.close()
        public_snap=research_snapshot(db,True)
        payloads={p:bytes.fromhex(b) for p,sha,b,vis in public_snap['artifacts']}
        state={'cells':public_snap['cells'],'claims':public_snap['claims']};payloads['state/research.json']=canonical(state)
        manifest={p:digest(b) for p,b in payloads.items()};payloads['MANIFEST.json']=canonical({'algorithm':'SHA-256','scope':'public-fixture','files':manifest,'self_excluded':True})
        expected={p:digest(b) for p,b in payloads.items()}
        export=make_zip(sorted(payloads.items()));validation=inspect(export,expected)
        rec.check('public_export_complete',validation['status'],'COMPLETE')
        private_digest=digest(secret).encode();unpacked=[]
        with zipfile.ZipFile(io.BytesIO(export)) as z:
            for name in z.namelist():unpacked.append(z.read(name))
            rec.check('private_path_absent','private/belief.txt' in z.namelist(),False)
        rec.check('private_body_absent',any(secret in b for b in unpacked),False)
        rec.check('private_digest_absent',any(private_digest in b for b in unpacked),False)
        fresh=init(tmp/'fresh.db')
        with zipfile.ZipFile(io.BytesIO(export)) as z:
            restored_state=json.loads(z.read('state/research.json'))
            with fresh:
                for p in sorted(public_snap['artifacts']):
                    name,sha,body,vis=p;data=z.read(name);fresh.execute('INSERT INTO artifacts VALUES(?,?,?,?)',(name,digest(data),data,'public'))
                fresh.executemany('INSERT INTO cells VALUES(?,?,?,?)',restored_state['cells'])
                fresh.executemany('INSERT INTO claims VALUES(?,?,?)',restored_state['claims'])
        roundtrip=research_snapshot(fresh,True)
        rec.check('roundtrip_research_snapshot',roundtrip,public_snap)
        rec.check('roundtrip_ids',len(roundtrip['cells']),625)
        mutated=dict(payloads);mutated['reports/demo.md']=b'corrupted fixture'
        changed=inspect(make_zip(sorted(mutated.items())),expected)
        rec.check('tamper_detected',changed['status'],'CHANGED')
        rec.check('tamper_exact_path',changed['changed'],['reports/demo.md'])
        rec.check('fresh_foreign_key_integrity',fresh.execute('PRAGMA foreign_key_check').fetchall(),[])
        fresh.close();db.close()
        (ROOT/'simulation/results/U3_public_demo.zip').write_bytes(export)
        (ROOT/'simulation/results/U3_public_demo_expected.json').write_text(json.dumps(expected,indent=2))
        (ROOT/'simulation/results/U3_public_snapshot_digest.json').write_text(json.dumps({'before_digest':digest(canonical(public_snap)),'after_digest':digest(canonical(roundtrip)),'source':'synthetic only; public scope excludes private artifact','sqlite_version':sqlite3.sqlite_version},indent=2))
    return rec.finish({'cells_persisted':625,'public_artifacts':2,'private_sentinel_artifacts':1,'public_roundtrip_equal':public_snap==roundtrip,'sqlite_version':sqlite3.sqlite_version,'controlled_lock_interleavings':1},['Logical equality is not byte-identical SQLite database backup','No actual process kill, power loss, disk-full or hardware fault tested','Controlled two-connection scheduling is not concurrent load testing','No external effect executed; one nonce row does not prove exactly-once tool execution','Fixture exporter is not a complete application or general privacy proof'])
if __name__=='__main__':run()
