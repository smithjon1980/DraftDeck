import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1]/'scripts'/'archive.py'
spec = importlib.util.spec_from_file_location('boss_custody_archive',SCRIPT)
a = importlib.util.module_from_spec(spec)
sys.modules[spec.name]=a
spec.loader.exec_module(a)
MID = 'BOSS.EP00.A01.S01'

def manuscript(ids=(1,2,3), windows=False):
    line = '\r\n' if windows else '\n'
    return (line.join(f'## {n:03d} — Title {n}{line}{line}Synthetic body {n}.' for n in ids)+line).encode()

def approvals(start=1,end=3,state='DRAFT'):
    return {'ranges':[{'start':start,'end':end,'state':state}]}

class MockGH:
    def __init__(self, private=True, push=True, visibility='private', fail_manifest=False, modify_readback=False, existing=False):
        self.private=private; self.push=push; self.visibility=visibility
        self.fail_manifest=fail_manifest; self.modify_readback=modify_readback
        self.existing=existing; self.files={}; self.put_calls=0;self.privacy_checked=False
        self.read_refs=[]
    def metadata(self,repo):
        self.privacy_checked=True
        return {'private':self.private,'visibility':self.visibility,'permissions':{'push':self.push}}
    def list_dir(self,repo,path,branch):
        if not self.privacy_checked: raise AssertionError('privacy check missing')
        return [{'path':path+'/different.md'}] if self.existing else []
    def put(self,repo,path,branch,data,message):
        if not self.privacy_checked: raise AssertionError('privacy check missing')
        self.put_calls+=1
        if self.put_calls == 2 and self.fail_manifest: raise a.Hold('simulated manifest failure')
        if path in self.files: raise a.Hold('duplicate file')
        self.files[path]=data
        return {'commit':{'sha':f'{self.put_calls:040x}'}}
    def get(self,repo,path,ref):
        self.read_refs.append(ref)
        data=self.files[path]
        return data+b'altered' if self.modify_readback else data

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.source=self.root/'source.md'
        self.source.write_bytes(manuscript())
        self.approvals=approvals()
    def local(self, rev='v0.2', approval=None, first=1,last=3):
        return a.archive_synthetic_local(self.source,self.root/'output',MID,rev,first,last,approval or self.approvals)
    def remote(self, gh, approval=None, rev='v0.2'):
        return a.archive_private_github(self.source,'owner/private-repo','custody/test',MID,rev,1,3,approval or self.approvals,gh)
    def assertHold(self,fn):
        with self.assertRaises(a.Hold): fn()
    def test_happy_path_local_readback_and_distinct_hashes(self):
        result=self.local(); self.assertEqual(result['status'],'LOCAL_VERIFIED_GITHUB_HOLD')
        self.assertEqual(Path(result['snapshot_path']).read_bytes(),self.source.read_bytes())
        m=json.loads(Path(result['manifest_path']).read_text())
        self.assertIsNone(m['remote_commit_sha']);self.assertFalse(m['approval_authority_verified'])
        self.assertEqual(m['canonicalization_schema'],'BOSS-CANONICAL-PARAGRAPHS-V1')
    def test_interior_gap_rejected(self):
        self.source.write_bytes(manuscript((1,3)))
        self.assertHold(self.local)
    def test_trailing_gap_rejected(self):
        self.source.write_bytes(manuscript((1,2)))
        self.assertHold(self.local)
    def test_shifted_start_rejected(self):
        self.source.write_bytes(manuscript((2,3)))
        self.assertHold(self.local)
    def test_duplicate_rejected(self):
        self.source.write_bytes(manuscript((1,2,2,3)))
        self.assertHold(self.local)
    def test_no_numbered_paragraphs_rejected(self):
        self.source.write_bytes(b'No headings here')
        self.assertHold(self.local)
    def test_blank_body_rejected(self):
        self.source.write_bytes(b'## 001 - Empty\n## 002 - Two\nBody\n')
        self.assertHold(lambda:self.local(first=1,last=2))
    def test_arbitrary_free_text_approval_rejected(self):
        self.assertHold(lambda:self.local(approval=approvals(state='APPROVED WITHOUT EVIDENCE')))
    def test_plain_approved_flag_rejected(self):
        self.assertHold(lambda:self.local(approval=approvals(state='APPROVED')))
    def test_approval_claim_must_bind_exact_source(self):
        claim={'ranges':[{'start':1,'end':3,'state':'APPROVAL_CLAIM','actor':'editor','decision_ref':'review/001', 'scope_canonical_sha256':'deadbeef'}]}
        self.assertHold(lambda:self.local(approval=claim))
        paras=a.load_paragraphs(self.source.read_bytes(),1,3)
        claim['ranges'][0]['scope_canonical_sha256']=a.scope_sha(paras,1,3)
        result=self.local(approval=claim)
        m=json.loads(Path(result['manifest_path']).read_text())
        self.assertFalse(m['approval_authority_verified'])
    def test_missing_approval_coverage_rejected(self):
        self.assertHold(lambda:self.local(approval=approvals(1,2)))
    def test_revision_path_traversal_rejected(self):
        for rev in ('../elsewhere','v0.2/../../escape','/tmp/pwn','v0.2\\..\\escape'):
            with self.subTest(rev=rev): self.assertHold(lambda:self.local(rev=rev))
        self.assertFalse((self.root/'elsewhere').exists())
    def test_manuscript_path_traversal_rejected(self):
        self.assertHold(lambda:a.archive_synthetic_local(self.source,self.root/'output','../../evil','v0.2',1,3,self.approvals))
    def test_different_hash_same_revision_conflict(self):
        self.local()
        self.source.write_bytes(manuscript().replace(b'Synthetic body 1.', b'Changed synthetic body.'))
        self.assertHold(self.local)
    def test_titles_contract(self):
        records=a.load_paragraphs(self.source.read_bytes(),1,3)
        good={p['number']:p['title'] for p in records}
        self.assertEqual(len(a.load_paragraphs(self.source.read_bytes(),1,3,good)),3)
        good['002']='wrong'
        self.assertHold(lambda:a.load_paragraphs(self.source.read_bytes(),1,3,good))
    def test_canonical_ignores_crlf_only(self):
        p1=a.load_paragraphs(manuscript(),1,3)
        p2=a.load_paragraphs(manuscript(windows=True),1,3)
        self.assertEqual(a.digest(a.canonical_bytes(p1)),a.digest(a.canonical_bytes(p2)))
        self.assertNotEqual(a.digest(manuscript()),a.digest(manuscript(windows=True)))
    def test_public_remote_rejected_no_writes(self):
        gh=MockGH(private=False,visibility='public')
        self.assertHold(lambda:self.remote(gh))
        self.assertEqual(gh.put_calls,0)
    def test_unknown_privacy_remote_rejected_no_writes(self):
        gh=MockGH(private=None,visibility=None)
        self.assertHold(lambda:self.remote(gh))
        self.assertEqual(gh.put_calls,0)
    def test_remote_missing_permission_rejected_no_writes(self):
        gh=MockGH(push=False)
        self.assertHold(lambda:self.remote(gh))
        self.assertEqual(gh.put_calls,0)
    def test_remote_success_mock_readback_at_immutable_sha(self):
        gh=MockGH()
        result=self.remote(gh)
        self.assertEqual(result['status'],'REMOTE_ARCHIVED_VERIFIED')
        self.assertEqual(gh.put_calls,3)
        self.assertEqual(len(gh.files),3)
        self.assertTrue(any(k.endswith('.receipt.json') for k in gh.files))
        self.assertTrue(all(len(ref)==40 for ref in gh.read_refs))
        self.assertEqual(result['remote_readback_sha256'],a.digest(self.source.read_bytes()))
        self.assertFalse(result['approval_authority_verified'])
    def test_remote_readback_tampered_holds(self):
        gh=MockGH(modify_readback=True)
        self.assertHold(lambda:self.remote(gh))
    def test_remote_partial_manifest_failure_never_archived(self):
        gh=MockGH(fail_manifest=True)
        self.assertHold(lambda:self.remote(gh))
        self.assertEqual(gh.put_calls,2)
        self.assertEqual(len(gh.files),1) # source-only commit: HOLD and reconcile
    def test_duplicate_remote_revision_rejected(self):
        gh=MockGH(existing=True)
        self.assertHold(lambda:self.remote(gh))
        self.assertEqual(gh.put_calls,0)

if __name__=='__main__': unittest.main()
