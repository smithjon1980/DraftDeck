#!/usr/bin/env python3
"""BOSS manuscript custody candidate v0.2. Python stdlib only; no automatic triggers.

No GitHub operations occur unless --mode private-github is explicitly supplied.
This candidate requires further human security review before any real remote use.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote

class Hold(ValueError):
    pass

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

ID_PATTERN = re.compile(r'BOSS\.EP\d{2}\.A\d{2}\.S\d{2}\Z', re.ASCII)
REV_PATTERN = re.compile(r'v\d{1,4}(?:\.\d{1,3})?\Z', re.ASCII)
REPO_PATTERN = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z', re.ASCII)
HEADING = re.compile(r'^#{0,6}\s*(\d{3})\s*[—-]\s*(\S.*?)(?:\s*)$', re.UNICODE)
PARAGRAPH_HINT = re.compile(r'^\s*#{0,6}\s*\d{3}\s*[-—–:]')

def check_component(value: str, pattern: re.Pattern, name: str) -> str:
    if not pattern.fullmatch(value) or '/' in value or '\\' in value or value in ('.','..'):
        raise Hold(f'unsafe {name}: {value!r}')
    return value

def load_paragraphs(raw: bytes, first: int, last: int, title_contract: dict | None = None) -> list[dict]:
    if first < 1 or first > last or last > 999:
        raise Hold('invalid expected paragraph range')
    try:
        content = raw.decode('utf-8', errors='strict')
    except UnicodeDecodeError as e:
        raise Hold('source is not valid UTF-8') from e
    if '\x00' in content:
        raise Hold('NUL in source')
    content = content.replace('\r\n','\n').replace('\r','\n')
    records, current, body = [], None, []
    def close():
        if current is not None:
            text = '\n'.join(body).strip()
            if not text:
                raise Hold(f'empty body for P{current[0]:03d}')
            records.append({'number':f'{current[0]:03d}', 'title':current[1].strip(), 'body':text})
    for line in content.split('\n'):
        m = HEADING.fullmatch(line.strip())
        if m:
            close()
            current = (int(m.group(1)), m.group(2))
            body = []
        else:
            if PARAGRAPH_HINT.match(line):
                raise Hold('malformed paragraph heading')
            if current is not None:
                body.append(line)
    close()
    numbers = [int(r['number']) for r in records]
    required = list(range(first,last+1))
    if numbers != required:
        raise Hold(f'paragraph range mismatch; expected P{first:03d}–P{last:03d}, got {numbers}')
    if title_contract is not None:
        required_keys = {f'{p:03d}' for p in required}
        if set(title_contract) != required_keys:
            raise Hold('title contract does not cover exactly expected paragraphs')
        for r in records:
            if title_contract[r['number']] != r['title']:
                raise Hold(f'title mismatch at P{r["number"]}')
    return records

def canonical_bytes(paragraphs: list[dict]) -> bytes:
    # V1 canonical scope is explicit; it need not match any legacy BOSS hash algorithm.
    record = {'schema':'BOSS-CANONICAL-PARAGRAPHS-V1', 'paragraphs':paragraphs}
    return (json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',',':'))+'\n').encode('utf-8')

def scope_sha(paragraphs: list[dict], first: int, last: int) -> str:
    selection = [p for p in paragraphs if first <= int(p['number']) <= last]
    return digest(canonical_bytes(selection))

def validate_approvals(spec: dict, paragraphs: list[dict]) -> list[dict]:
    """Only an approval CLAIM is representable; verified authorizations require external attestation."""
    if not isinstance(spec,dict) or set(spec) != {'ranges'} or not isinstance(spec['ranges'],list):
        raise Hold('approval schema requires ranges array')
    allowed = {'DRAFT','PENDING_REVIEW','REJECTED','APPROVAL_CLAIM'}
    covered = []
    output = []
    for entry in spec['ranges']:
        if not isinstance(entry,dict):
            raise Hold('approval range must be an object')
        if not isinstance(entry.get('start'),int) or isinstance(entry['start'],bool) or not isinstance(entry.get('end'),int) or isinstance(entry['end'],bool):
            raise Hold('approval range must use integer boundaries')
        first,last,state = entry['start'],entry['end'],entry.get('state')
        if not isinstance(state,str) or state not in allowed or first>last:
            raise Hold('unsupported approval state or invalid range')
        if state == 'APPROVAL_CLAIM':
            if set(entry) != {'start','end','state','decision_ref','actor','scope_canonical_sha256'}:
                raise Hold('approval claim requires scoped decision evidence')
            if not all(isinstance(entry.get(k),str) and entry[k].strip() for k in ('decision_ref','actor','scope_canonical_sha256')):
                raise Hold('empty approval decision evidence')
            if entry['scope_canonical_sha256'] != scope_sha(paragraphs,first,last):
                raise Hold('approval claim does not match exact paragraph scope')
        elif set(entry) != {'start','end','state'}:
            raise Hold('non-approval range has unsupported fields')
        covered.extend(range(first,last+1))
        output.append(dict(entry))
    actual = [int(p['number']) for p in paragraphs]
    if sorted(covered) != actual:
        raise Hold('approval ranges do not exactly cover source or overlap')
    return output

def safe_path(root: Path, manuscript_id: str, revision: str, raw_sha: str) -> tuple[Path,Path]:
    check_component(manuscript_id,ID_PATTERN,'manuscript_id')
    check_component(revision,REV_PATTERN,'revision')
    base = root.resolve()
    p = base / 'snapshots' / manuscript_id / revision / f'{raw_sha}.md'
    m = p.with_suffix('.json')
    if not p.resolve().is_relative_to(base) or not m.resolve().is_relative_to(base):
        raise Hold('archive path escapes root')
    for directory in (base, base/'snapshots', base/'snapshots'/manuscript_id, p.parent):
        if directory.is_symlink():
            raise Hold('symlink archive directory is not allowed')
    return p,m

def atomic_save(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.tmp-',dir=path.parent)
    try:
        with os.fdopen(fd,'wb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name,path)
    finally:
        if os.path.exists(name):
            os.unlink(name)

def prepare(raw: bytes, manuscript_id: str, revision: str, first: int, last: int, approval: dict, titles:dict|None=None) -> tuple[list[dict],dict]:
    check_component(manuscript_id,ID_PATTERN,'manuscript_id')
    check_component(revision,REV_PATTERN,'revision')
    paragraphs = load_paragraphs(raw,first,last,titles)
    approvals = validate_approvals(approval,paragraphs)
    manifest = {
        'schema':'BOSS-CUSTODY-MANIFEST-V2',
        'manuscript_id':manuscript_id,'revision':revision,
        'paragraph_range':{'start':first,'end':last,'count':len(paragraphs)},
        'local_raw_source_sha256':digest(raw),
        'canonicalization_schema':'BOSS-CANONICAL-PARAGRAPHS-V1',
        'canonical_paragraphs_sha256':digest(canonical_bytes(paragraphs)),
        'approval_claims':approvals,'approval_authority_verified':False,
        'remote_commit_sha':None,'remote_readback_sha256':None,
        'archival_status':'PREPARED_NOT_ARCHIVED',
    }
    return paragraphs,manifest

def archive_synthetic_local(source:Path, root:Path, manuscript_id:str, revision:str, first:int,last:int, approvals:dict, titles:dict|None=None)->dict:
    raw = source.read_bytes()
    _,manifest = prepare(raw, manuscript_id,revision,first,last,approvals,titles)
    root = root.resolve()
    if any(parent.name == '.git' for parent in [root,*root.parents]):
        raise Hold('synthetic output cannot be located in .git')
    p,m = safe_path(root,manuscript_id,revision,manifest['local_raw_source_sha256'])
    if p.parent.exists() and any(x.suffix=='.md' and x.name!=p.name for x in p.parent.iterdir()):
        raise Hold('same manuscript revision has different bytes')
    if p.exists() and p.read_bytes()!=raw:
        raise Hold('source digest path collision')
    if m.exists() and json.loads(m.read_text('utf-8')).get('local_raw_source_sha256')!=digest(raw):
        raise Hold('manifest conflict')
    manifest['archival_status']='LOCAL_VERIFIED_GITHUB_HOLD'
    manifest['local_snapshot_readback_verified']=True
    mb = (json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    atomic_save(p,raw)
    atomic_save(m,mb)
    if p.read_bytes()!=raw or digest(p.read_bytes())!=manifest['local_raw_source_sha256'] or json.loads(m.read_bytes())!=manifest:
        raise Hold('LOCAL_READBACK_FAILED')
    return {'status':'LOCAL_VERIFIED_GITHUB_HOLD','snapshot_path':str(p),'manifest_path':str(m),
            'local_raw_source_sha256':digest(raw),'canonical_paragraphs_sha256':manifest['canonical_paragraphs_sha256'],
            'remote_commit_sha':None,'remote_readback_sha256':None}

class GhTransport:
    """GH CLI operations; exact SHA ref readback, not a cached working-tree inspection."""
    def api(self, method: str, endpoint: str, fields:dict|None=None) -> dict:
        cmd = ['gh','api','--method',method,endpoint,'-H','Accept: application/vnd.github+json']
        for k,v in (fields or {}).items():
            cmd += ['-f',f'{k}={v}']
        try:
            p = subprocess.run(cmd, check=True, capture_output=True,text=True,timeout=30)
            return json.loads(p.stdout)
        except (FileNotFoundError,subprocess.CalledProcessError,subprocess.TimeoutExpired,ValueError) as e:
            raise Hold(f'GitHub operation failed: {type(e).__name__}') from e
    def metadata(self,repo:str)->dict:
        return self.api('GET',f'repos/{repo}')
    def get(self,repo:str,path:str,ref:str)->bytes:
        response=self.api('GET',f'repos/{repo}/contents/{quote(path,safe="/")}',{'ref':ref})
        if response.get('encoding')!='base64' or not isinstance(response.get('content'),str):
            raise Hold('GitHub returned non-base64 content')
        try:
            return base64.b64decode(response['content'],validate=False)
        except ValueError as e:
            raise Hold('remote content could not be decoded') from e
    def put(self,repo:str,path:str,branch:str,data:bytes,message:str)->dict:
        return self.api('PUT',f'repos/{repo}/contents/{quote(path,safe="/")}',{
            'message':message,'branch':branch,'content':base64.b64encode(data).decode('ascii')})
    def list_dir(self,repo:str,path:str,branch:str):
        # Tree listing distinguishes an empty/new directory from unrelated HTTP failures.
        tree = self.api('GET',f'repos/{repo}/git/trees/{quote(branch,safe="")}',{'recursive':'1'})
        if tree.get('truncated') is not False or not isinstance(tree.get('tree'),list):
            raise Hold('remote tree listing incomplete or unverifiable')
        return [item for item in tree['tree'] if isinstance(item,dict) and
                (item.get('path') == path or str(item.get('path','')).startswith(path + '/'))]

def require_private(repo:str, transport)->None:
    if not REPO_PATTERN.fullmatch(repo):
        raise Hold('invalid private GitHub repo identifier')
    meta=transport.metadata(repo)
    if meta.get('private') is not True or meta.get('visibility') not in (None,'private'):
        raise Hold('PRIVATE_REPOSITORY_REQUIRED')
    perms=meta.get('permissions')
    if not isinstance(perms,dict) or perms.get('push') is not True:
        raise Hold('authenticated repository write access not established')

def archive_private_github(source:Path, repo:str, branch:str, manuscript_id:str, revision:str, first:int,last:int,approvals:dict, transport=None, titles:dict|None=None)->dict:
    """Two-phase commit plus verification; on partial failure report HOLD, do not say ARCHIVED."""
    raw=source.read_bytes()
    _,manifest=prepare(raw,manuscript_id,revision,first,last,approvals,titles)
    transport=transport or GhTransport()
    require_private(repo,transport)  # no remote source bytes sent until privacy verified
    if not isinstance(branch,str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._/-]{0,100}',branch) or '..' in branch or branch.endswith('/'):
        raise Hold('invalid explicit branch')
    prefix=f'manuscripts/{manuscript_id}/{revision}'
    destination=f'{prefix}/{manifest["local_raw_source_sha256"]}.md'
    manifest_path=f'{prefix}/{manifest["local_raw_source_sha256"]}.manifest.json'
    # A path listing prevents a second hash for the same version. Failure to list is HOLD.
    listing=transport.list_dir(repo,prefix,branch)
    # Implementations may return [] for a missing directory; failures are HOLD.
    if not isinstance(listing,list):
        raise Hold('could not verify remote revision directory')
    if listing:
        raise Hold('remote revision directory already has content: manual reconciliation required')
    write=transport.put(repo,destination,branch,raw,f'custody: preserve {manuscript_id} {revision} source')
    source_commit=write.get('commit',{}).get('sha')
    if not isinstance(source_commit,str) or not re.fullmatch(r'[a-fA-F0-9]{40,64}',source_commit):
        raise Hold('GitHub source commit not confirmed')
    if transport.get(repo,destination,source_commit)!=raw:
        raise Hold('REMOTE_SOURCE_READBACK_FAILED')
    # Do not embed the manifest commit SHA inside itself (self-reference).
    manifest['remote_source_commit_sha']=source_commit
    manifest['remote_readback_sha256']=digest(raw)
    manifest['archival_status']='REMOTE_SOURCE_VERIFIED_RECEIPT_PENDING'
    manifest['local_snapshot_readback_verified']=False
    mb=(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    require_private(repo,transport)
    receipt=transport.put(repo,manifest_path,branch,mb,f'custody: add provenance {manuscript_id} {revision}')
    final_commit=receipt.get('commit',{}).get('sha')
    if not isinstance(final_commit,str) or not re.fullmatch(r'[a-fA-F0-9]{40,64}',final_commit):
        raise Hold('GitHub manifest commit not confirmed')
    if transport.get(repo,destination,final_commit)!=raw or transport.get(repo,manifest_path,final_commit)!=mb:
        raise Hold('REMOTE_MANIFEST_COMMIT_READBACK_FAILED')
    # Persist the verified readback result in a third immutable commit.
    # Receipt cites the manifest commit and source; never embeds its own commit SHA.
    receipt_path=f'{prefix}/{manifest["local_raw_source_sha256"]}.receipt.json'
    durable_receipt={
        'schema':'BOSS-CUSTODY-RECEIPT-V1',
        'archival_status':'REMOTE_ARCHIVED_VERIFIED',
        'source_path':destination,'manifest_path':manifest_path,
        'source_commit_sha':source_commit,'manifest_commit_sha':final_commit,
        'local_raw_source_sha256':digest(raw),
        'remote_readback_sha256':digest(transport.get(repo,destination,final_commit)),
        'manifest_readback_sha256':digest(transport.get(repo,manifest_path,final_commit)),
        'canonical_paragraphs_sha256':manifest['canonical_paragraphs_sha256'],
        'approval_authority_verified':False,
    }
    if durable_receipt['remote_readback_sha256']!=digest(raw) or durable_receipt['manifest_readback_sha256']!=digest(mb):
        raise Hold('REMOTE_RECEIPT_PRECONDITION_FAILED')
    rb=(json.dumps(durable_receipt,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    require_private(repo,transport)
    third=transport.put(repo,receipt_path,branch,rb,f'custody: persist verified readback {manuscript_id} {revision}')
    receipt_commit=third.get('commit',{}).get('sha')
    if not isinstance(receipt_commit,str) or not re.fullmatch(r'[a-fA-F0-9]{40,64}',receipt_commit):
        raise Hold('GitHub receipt commit not confirmed')
    if (transport.get(repo,destination,receipt_commit)!=raw or
        transport.get(repo,manifest_path,receipt_commit)!=mb or
        transport.get(repo,receipt_path,receipt_commit)!=rb):
        raise Hold('REMOTE_RECEIPT_COMMIT_READBACK_FAILED')
    return {'status':'REMOTE_ARCHIVED_VERIFIED','repository':repo,'branch':branch,
            'source_path':destination,'manifest_path':manifest_path,'receipt_path':receipt_path,
            'source_commit_sha':source_commit,'manifest_commit_sha':final_commit,
            'remote_commit_sha':receipt_commit,
            'local_raw_source_sha256':digest(raw),'canonical_paragraphs_sha256':manifest['canonical_paragraphs_sha256'],
            'remote_readback_sha256':digest(raw),'approval_authority_verified':False}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode',required=True,choices=['synthetic-local','private-github'])
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--id',required=True)
    parser.add_argument('--revision',required=True)
    parser.add_argument('--expected-start',type=int,required=True)
    parser.add_argument('--expected-end',type=int,required=True)
    parser.add_argument('--approvals-json',type=Path,required=True)
    parser.add_argument('--titles-json',type=Path)
    parser.add_argument('--root',type=Path)
    parser.add_argument('--synthetic',action='store_true')
    parser.add_argument('--github-repo')
    parser.add_argument('--branch')
    args=parser.parse_args(argv)
    try:
        approval=json.loads(args.approvals_json.read_text('utf-8'))
        titles=json.loads(args.titles_json.read_text('utf-8')) if args.titles_json else None
        if args.mode=='synthetic-local':
            if not args.synthetic or not args.root or args.github_repo or args.branch:
                raise Hold('synthetic-local requires --synthetic and --root and prohibits remote options')
            result=archive_synthetic_local(args.source,args.root,args.id,args.revision,args.expected_start,args.expected_end,approval,titles)
        else:
            if args.synthetic or args.root or not args.github_repo or not args.branch:
                raise Hold('private-github requires explicit repo and branch; no synthetic/local fallback')
            result=archive_private_github(args.source,args.github_repo,args.branch,args.id,args.revision,args.expected_start,args.expected_end,approval,titles=titles)
        print(json.dumps(result,indent=2))
        return 0
    except (Hold,FileNotFoundError,PermissionError,IsADirectoryError,json.JSONDecodeError) as e:
        print(f'HOLD: {e}',file=sys.stderr)
        return 2

if __name__=='__main__':
    sys.exit(main())
