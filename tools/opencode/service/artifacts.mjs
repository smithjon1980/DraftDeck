import express from 'express';
import path from 'node:path';
import crypto from 'node:crypto';
import { mkdir, readFile, writeFile, rename, readdir, statfs, unlink, open } from 'node:fs/promises';
import yauzl from 'yauzl';
import crc32 from 'crc-32';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const MAX_ARCHIVE = 50 * 1024 * 1024;
const MAX_EXPANDED = 100 * 1024 * 1024;
const MAX_FILE = 32 * 1024 * 1024;
const expectedAudio = {
  'smoke_generated.wav': '7833cd4126fb84c194f621bba5a117a2ed68a0b07351f7c17d26911f86e8082d',
  'solo_generated.wav': 'ebb6d688cdec0d3103eaa982a4de1bbac9688c444d6aa247799973bbffae7f3a',
  'deep_dive_generated.wav': 'f3539898457064c41e133e9116c46e8ce68059c020fd21009b45ec8c7ec64093',
};
const trialReference = 'smithjon1980/boss-audio-003-kaggle-setup-repair';

export function notebookReference(value) {
  if (typeof value !== 'string') throw new Error('Enter the notebook owner/name.');
  const ref = value.trim().replace(/^https:\/\/www\.kaggle\.com\/code\//, '').replace(/\/output\/?$/, '').replace(/\/$/, '');
  if (!/^[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+$/.test(ref)) throw new Error('Use a Kaggle notebook reference such as owner/notebook-name.');
  return ref;
}

export function allowedDownload(value) {
  const url = new URL(value);
  if (url.protocol !== 'https:' || url.username || url.password || (url.port && url.port !== '443')) throw new Error('Kaggle returned an unsupported download address.');
  const host = url.hostname;
  if (!['www.kaggle.com', 'kaggle.com', 'storage.googleapis.com'].includes(host) && !host.endsWith('.kaggleusercontent.com') && !host.endsWith('.googleusercontent.com')) throw new Error('Kaggle returned an unrecognized download host.');
  return url;
}

function findDownload(result) {
  const found = [];
  function walk(value) {
    if (typeof value === 'string') {
      try { walk(JSON.parse(value)); } catch {}
      for (const match of value.matchAll(/https:\/\/[^\s<>"\[\]{}]+/g)) {
        const candidate = match[0].replace(/[),.;]+$/, '');
        try { found.push(allowedDownload(candidate)); } catch {}
      }
    } else if (Array.isArray(value)) value.forEach(walk);
    else if (value && typeof value === 'object') Object.values(value).forEach(walk);
  }
  walk(result);
  const urls = [...new Map(found.map(url => [url.href, url])).values()];
  if (urls.length !== 1) throw new Error('Kaggle did not return one supported file download URL. No endpoint was guessed.');
  return urls[0];
}

async function download(url, credential, target) {
  let current = allowedDownload(url);
  const signal = AbortSignal.timeout(180000);
  let response;
  for (let redirects = 0; redirects < 6; redirects++) {
    const headers = ['www.kaggle.com', 'kaggle.com'].includes(current.hostname) ? { Authorization: `Bearer ${credential}` } : {};
    response = await fetch(current, { headers, redirect: 'manual', signal });
    if (![301, 302, 303, 307, 308].includes(response.status)) break;
    const location = response.headers.get('location');
    await response.body?.cancel();
    if (!location) throw new Error('Kaggle download redirect has no destination.');
    current = allowedDownload(new URL(location, current).href);
    response = undefined;
  }
  if (!response?.ok || !response.body) throw new Error(`Kaggle file download failed${response ? ` (HTTP ${response.status})` : ''}.`);
  if (Number(response.headers.get('content-length') || 0) > MAX_ARCHIVE) { await response.body.cancel(); throw new Error('Archive exceeds the 50 MB trial limit.'); }
  const out = await open(target, 'wx', 0o600);
  const hash = crypto.createHash('sha256');
  let size = 0;
  try {
    for await (const bytes of response.body) {
      size += bytes.length;
      if (size > MAX_ARCHIVE) throw new Error('Archive exceeds the 50 MB trial limit.');
      hash.update(bytes);
      await out.writeFile(bytes);
    }
    await out.close();
    return { bytes: size, sha256: hash.digest('hex') };
  } catch (error) { await out.close().catch(() => {}); await unlink(target).catch(() => {}); throw error; }

}

export async function inspectArchive(filename, directory, reference) {
  const archiveBytes = await readFile(filename);
  if (archiveBytes.length > MAX_ARCHIVE) throw new Error('Archive exceeds the 50 MB trial limit.');
  const zip = await new Promise((resolve, reject) => yauzl.fromBuffer(archiveBytes, { lazyEntries: true, validateEntrySizes: true }, (error, value) => error ? reject(error) : resolve(value)));
  let total = 0, entries = 0;
  const audio = [];
  try {
    await new Promise((resolve, reject) => {
      zip.on('error', reject); zip.on('end', resolve);
      zip.on('entry', entry => { void (async () => {
        if (++entries > 5000) throw new Error('Too many archive entries.');
        if (entry.fileName.startsWith('/') || entry.fileName.includes('\\') || entry.fileName.split('/').some(part => part === '..' || part === '.')) throw new Error('Unsafe archive path.');
        if (((entry.externalFileAttributes >>> 16) & 0o170000) === 0o120000) throw new Error('Archive symlinks are not accepted.');
        if (entry.generalPurposeBitFlag & 1) throw new Error('Encrypted archives are not accepted.');
        total += entry.uncompressedSize;
        if (total > MAX_EXPANDED || entry.uncompressedSize > MAX_FILE) throw new Error('Expanded archive exceeds the trial size limit.');
        if (entry.fileName.endsWith('/')) { zip.readEntry(); return; }
        const stream = await new Promise((resolveStream, rejectStream) => zip.openReadStream(entry, (error, value) => error ? rejectStream(error) : resolveStream(value)));
        const hash = crypto.createHash('sha256');
        const parts = [];
        let size = 0, crc = 0;
        const isAudio = /\.wav$/i.test(entry.fileName);
        for await (const bytes of stream) {
          size += bytes.length;
          if (size > MAX_FILE) throw new Error('Expanded file exceeds the trial limit.');
          crc = crc32.buf(bytes, crc); hash.update(bytes);
          if (isAudio) parts.push(bytes);
        }
        if (size !== entry.uncompressedSize || (crc >>> 0) !== entry.crc32) throw new Error('Archive integrity check failed.');
        const digest = hash.digest('hex');
        if (isAudio) {
          const bytes = Buffer.concat(parts);
          if (bytes.length < 12 || bytes.toString('ascii', 0, 4) !== 'RIFF' || bytes.toString('ascii', 8, 12) !== 'WAVE') throw new Error('A WAV entry has an invalid header.');
          const name = path.posix.basename(entry.fileName);
          const saved = `${String(audio.length + 1).padStart(3, '0')}-${name.replace(/[^a-zA-Z0-9_.-]/g, '_')}`;
          await writeFile(path.join(directory, saved), bytes, { flag: 'wx', mode: 0o600 });
          const expected = reference === trialReference ? expectedAudio[name] : undefined;
          audio.push({ name, source_path: entry.fileName, saved, bytes: size, sha256: digest, reference_hash: expected ? (digest === expected ? 'MATCH' : 'MISMATCH') : 'NOT_AVAILABLE', listening_review: 'PENDING', wording_review: 'PENDING' });
        }
        zip.readEntry();
      })().catch(reject); });
      zip.readEntry();
    });
  } finally { zip.close(); }
  if (!audio.length) throw new Error('No WAV files found in this package. The original archive is retained for inspection.');
  if (reference === trialReference) {
    if (audio.length !== 3) throw new Error('Expected audio count differs from the three-file trial.');
    for (const name of Object.keys(expectedAudio)) if (audio.filter(file => file.name === name && file.reference_hash === 'MATCH').length !== 1) throw new Error(`Expected audio is missing, duplicated, or changed: ${name}`);
  }
  return { entries, expanded_bytes: total, audio, archive_integrity: 'PASS', trial_audio_hashes: reference === trialReference ? 'MATCH' : 'NOT_APPLICABLE' };
}

export async function createArtifacts({ dataDirectory, page, publicOrigin }) {
  await mkdir(dataDirectory, { recursive: true, mode: 0o700 });
  let credential = process.env.KAGGLE_API_TOKEN || '';
  let activeJob;
  const fileFor = id => {
    if (typeof id !== 'string' || !/^[a-f0-9-]{36}$/.test(id)) throw new Error('Invalid job ID.');
    return path.join(dataDirectory, id, 'manifest.json');
  };
  const save = async job => {
    const filename = fileFor(job.id);
    await writeFile(filename + '.tmp', JSON.stringify(job, null, 2), { mode: 0o600 });
    await rename(filename + '.tmp', filename);
  };
  const get = async id => JSON.parse(await readFile(fileFor(id), 'utf8'));
  async function list() {
    const jobs = [];
    for (const name of await readdir(dataDirectory)) {
      if (!/^[a-f0-9-]{36}$/.test(name)) continue;
      try { jobs.push(await get(name)); } catch {}
    }
    return jobs.sort((a, b) => b.created_at.localeCompare(a.created_at));
  }
  for (const job of await list()) if (['QUEUED', 'RETRIEVING', 'VERIFYING'].includes(job.status)) {
    job.status = 'INTERRUPTED'; job.error = 'Service restarted during retrieval. Retry manually; existing evidence was retained.'; await save(job);
  }
  const summary = job => ({ ...job, portal: `${publicOrigin || ''}/artifacts`, downloads: job.status === 'VERIFIED_FILES' ? [{ name: 'Original results ZIP', url: `${publicOrigin || ''}/artifacts/jobs/${job.id}/files/results.zip` }, ...job.audio.map(file => ({ name: file.name, url: `${publicOrigin || ''}/artifacts/jobs/${job.id}/files/${file.saved}` })), { name: 'Verification record', url: `${publicOrigin || ''}/artifacts/jobs/${job.id}/files/manifest.json` }] : [] });

  async function retrieve(reference) {
    const ref = notebookReference(reference);
    if (!credential) throw new Error('Connect Kaggle in the portal before retrieving private outputs.');
    if (activeJob) throw new Error('Another retrieval is running. Wait for its result.');
    const disk = await statfs(dataDirectory);
    if (disk.bavail * disk.bsize < MAX_ARCHIVE + MAX_EXPANDED + 20 * 1024 * 1024) throw new Error('Insufficient free storage for a bounded retrieval. Existing files were preserved.');
    const job = { id: crypto.randomUUID(), reference: ref, source_file: 'BOSS_AUDIO_003_RESULTS.zip', created_at: new Date().toISOString(), status: 'QUEUED', publication_authorized: false, audio: [] };
    if (activeJob) throw new Error('Another retrieval is running. Wait for its result.');
    activeJob = job.id;
    const directory = path.dirname(fileFor(job.id));
    try {
    await mkdir(directory, { mode: 0o700 }); await save(job);
    } catch (error) { activeJob = undefined; throw error; }
    const currentCredential = credential;
    void (async () => {
      const client = new Client({ name: 'boss-artifact-retrieval', version: '0.1.0' });
      try {
        job.status = 'RETRIEVING'; await save(job);
        const transport = new StreamableHTTPClientTransport(new URL('https://www.kaggle.com/mcp'), { requestInit: { headers: { Authorization: `Bearer ${currentCredential}` } } });
        await client.connect(transport, { timeout: 30000 });
        const [ownerSlug, kernelSlug] = ref.split('/');
        const response = await client.callTool({ name: 'download_notebook_output', arguments: { request: { ownerSlug, kernelSlug, filePath: job.source_file, hasFilePath: true } } }, undefined, { timeout: 60000 });
        if (response.isError) throw new Error('Kaggle denied or could not supply this notebook output. Verify the credential and notebook access.');
        const url = findDownload(response);
        job.archive = await download(url.href, currentCredential, path.join(directory, 'results.zip'));
        job.status = 'VERIFYING'; await save(job);
        Object.assign(job, await inspectArchive(path.join(directory, 'results.zip'), directory, ref));
        job.status = 'VERIFIED_FILES'; job.completed_at = new Date().toISOString();
      } catch (error) {
        job.status = 'HOLD';
        // Error text from SDK/network libraries can contain signed URLs or credentials.
        job.error = /^(Kaggle |Archive |Expanded |Unsafe |Encrypted |A WAV |No WAV |Expected audio)/.test(error.message) ? error.message : 'Retrieval could not complete. Check the Kaggle connection and retry manually.';
      } finally { await client.close().catch(() => {}); await save(job); activeJob = undefined; }
    })().catch(() => { activeJob = undefined; console.error('Artifact job record could not be saved.'); });
    return summary(job);
  }

  const router = express.Router();
  router.use((_req, res, next) => { res.set('Cache-Control', 'no-store'); res.set('X-Content-Type-Options', 'nosniff'); next(); });
  router.get('/', (_req, res) => res.type('html').sendFile(page));
  router.get('/api/status', async (_req, res) => res.json({ credential_configured: !!credential, credential_persistence: process.env.KAGGLE_API_TOKEN ? 'HOST_SECRET' : 'UNTIL_RESTART', private_access: 'NOT_VERIFIED', jobs: (await list()).map(summary) }));
  router.use(express.json({ limit: '8kb' }));
  router.use((req, res, next) => {
    if (req.method === 'POST' && !req.is('application/json')) return res.status(415).json({ error: 'Use JSON requests.' });
    next();
  });
  router.post('/api/connect', (req, res) => {
    const value = req.body?.token;
    if (typeof value !== 'string' || !/^KGAT[A-Za-z0-9_.=+/-]{10,4000}$/.test(value.trim())) return res.status(400).json({ error: 'Enter a Kaggle API token beginning with KGAT.' });
    credential = value.trim(); res.json({ credential_configured: true, private_access: 'NOT_VERIFIED', credential_persistence: 'UNTIL_RESTART' });
  });
  router.post('/api/retrieve', async (req, res) => { try { res.status(202).json(await retrieve(req.body?.reference)); } catch (error) { res.status(400).json({ error: error.message }); } });
  router.get('/jobs/:id/files/:name', async (req, res) => {
    try {
      const job = await get(req.params.id);
      const names = ['manifest.json', ...(job.status === 'VERIFIED_FILES' ? ['results.zip', ...job.audio.map(file => file.saved)] : [])];
      if (!names.includes(req.params.name)) return res.sendStatus(404);
      res.download(path.join(path.dirname(fileFor(job.id)), req.params.name), req.params.name, { dotfiles: 'deny' });
    } catch { res.sendStatus(404); }
  });
  router.use((_error, _req, res, _next) => res.status(500).json({ error: 'Artifact request could not be completed.' }));
  return {
    router,
    tools: [
      { name: 'boss_artifacts', description: 'List retained artifact jobs and authenticated download links. Does not establish wording or listening quality.', inputSchema: { type: 'object', properties: {}, additionalProperties: false }, annotations: { readOnlyHint: true } },
      { name: 'boss_retrieve_audio', description: 'Retrieve the existing BOSS_AUDIO_003_RESULTS.zip from a Kaggle notebook and verify archive integrity and trial WAV hashes. Does not run the notebook or invoke a model. Requires a Kaggle credential configured in the private portal.', inputSchema: { type: 'object', properties: { reference: { type: 'string' } }, required: ['reference'], additionalProperties: false }, annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: false } },
    ],
    call: async (name, args) => name === 'boss_artifacts' ? { credential_configured: !!credential, jobs: (await list()).map(summary) } : retrieve(args?.reference),
  };
}
