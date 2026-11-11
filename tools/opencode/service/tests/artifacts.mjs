import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import crypto from 'node:crypto';
import os from 'node:os';
import path from 'node:path';
import { inspectArchive, notebookReference, allowedDownload, createArtifacts } from '../artifacts.mjs';

const makeZip = (target, unsafe = false) => execFileSync('python3', ['-c', `
import io,wave,zipfile,sys
b=io.BytesIO()
with wave.open(b,'wb') as w:
 w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000);w.writeframes(b'\\x01\\x00'*240)
with zipfile.ZipFile(sys.argv[1],'w') as z:
 z.writestr('../escape.wav' if sys.argv[2]=='true' else 'run/solo_generated.wav',b.getvalue())
 z.writestr('record.txt','unique-integrity-fixture')
`, target, String(unsafe)]);

test('notebook references and download destinations stay bounded', () => {
  assert.equal(notebookReference('https://www.kaggle.com/code/smithjon1980/example/output'), 'smithjon1980/example');
  assert.throws(() => notebookReference('../../etc/passwd'));
  assert.throws(() => allowedDownload('http://www.kaggle.com/file'));
  assert.throws(() => allowedDownload('https://www.kaggle.com.evil.example/file'));
  assert.throws(() => allowedDownload('https://127.0.0.1/private'));
  assert.throws(() => allowedDownload('https://user:password@www.kaggle.com/file'));
  assert.equal(allowedDownload('https://storage.googleapis.com/bucket/file').hostname, 'storage.googleapis.com');
});

test('real ZIP CRC verification, bounded audio extraction, trial mismatch, and unsafe paths', async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), 'boss-archive-'));
  try {
    const archive = path.join(root, 'results.zip'); makeZip(archive); 
    const output = path.join(root, 'audio'); await mkdir(output);
     const result = await inspectArchive(archive, output, 'owner/other');
     assert.equal(result.archive_integrity, 'PASS');
    assert.equal(result.audio.length, 1);
    const file = result.audio[0];
    assert.equal(file.sha256, crypto.createHash('sha256').update(await readFile(path.join(output, file.saved))).digest('hex'));
    assert.equal(file.wording_review, 'PENDING');
    assert.equal(file.reference_hash, 'NOT_AVAILABLE');
    const mismatchOutput = path.join(root, 'mismatch'); await mkdir(mismatchOutput);
     await assert.rejects(inspectArchive(archive, mismatchOutput, 'smithjon1980/boss-audio-003-kaggle-setup-repair'), /Expected audio/);
     const corrupt = await readFile(archive); const position = corrupt.indexOf(Buffer.from('unique-integrity-fixture')); assert.ok(position >= 0); corrupt[position] ^= 1;
    const corrupted = path.join(root, 'corrupt.zip'); await writeFile(corrupted, corrupt);
    const badOutput = path.join(root, 'corrupt'); await mkdir(badOutput);
     await assert.rejects(inspectArchive(corrupted, badOutput, 'owner/other'), /integrity/);
     const unsafe = path.join(root, 'unsafe.zip'); makeZip(unsafe, true);
    await assert.rejects(inspectArchive(unsafe, output, 'owner/other'), /path|relative|invalid/i);
  } finally { await rm(root, { recursive: true, force: true }); }
});

test('unfinished persisted retrieval becomes interrupted after restart', async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), 'boss-recovery-'));
  try {
    const id = crypto.randomUUID(); await mkdir(path.join(directory, id));
    await writeFile(path.join(directory, id, 'manifest.json'), JSON.stringify({ id, reference: 'owner/notebook', created_at: new Date().toISOString(), status: 'RETRIEVING', audio: [] }));
    const service = await createArtifacts({ dataDirectory: directory, page: '/unused', publicOrigin: 'https://example.com' });
    const result = await service.call('boss_artifacts', {});
    assert.equal(result.jobs[0].status, 'INTERRUPTED');
    assert.equal(result.jobs[0].downloads.length, 0);
  } finally { await rm(directory, { recursive: true, force: true }); }
});
