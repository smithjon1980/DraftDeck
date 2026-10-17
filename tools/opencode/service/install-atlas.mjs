import { createHash } from 'node:crypto';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import yauzl from 'yauzl';

const root = path.dirname(fileURLToPath(import.meta.url));
const url = 'https://raw.githubusercontent.com/smithjon1980/DraftDeck/55762e23730642660c21430c31781f612d3a86f3/design-system/engineering-library/releases/DraftDeck_Engineering_Atlas_Complete.zip';
const expectedSha = 'c20af70fc76eadc5df4e3abfc8542d7f2e5c3db77c274d6b91d9e1b51dbfdc3f';
let bytes;
if (process.argv[2]) bytes = await readFile(process.argv[2]);
else {
  const response = await fetch(url, { signal: AbortSignal.timeout(60000) });
  if (!response.ok) throw new Error(`Atlas download failed: HTTP ${response.status}`);
  bytes = Buffer.from(await response.arrayBuffer());
}
if (bytes.length !== 751451 || createHash('sha256').update(bytes).digest('hex') !== expectedSha) throw new Error('Atlas package integrity mismatch');
const destination = path.join(root, 'public', 'atlas');
await mkdir(destination, { recursive: true });
const zip = await new Promise((resolve, reject) => yauzl.fromBuffer(bytes, { lazyEntries: true, validateEntrySizes: true }, (error, zip) => error ? reject(error) : resolve(zip)));
let count = 0, expanded = 0;
await new Promise((resolve, reject) => {
  zip.on('error', reject);
  zip.on('entry', async entry => {
    try {
      const name = entry.fileName;
      if (name.startsWith('/') || name.includes('\\') || name.split('/').some(part => part === '..' || part === '.') || ((entry.externalFileAttributes >>> 16) & 0xf000) === 0xa000) throw new Error('Unsafe atlas entry');
      expanded += entry.uncompressedSize;
      if (++count > 400 || expanded > 16000000 || entry.uncompressedSize > 4000000) throw new Error('Atlas extraction limit exceeded');
      const target = path.join(destination, name);
      if (name.endsWith('/')) await mkdir(target, { recursive: true });
      else {
        const stream = await new Promise((resolve, reject) => zip.openReadStream(entry, (error, stream) => error ? reject(error) : resolve(stream)));
        const chunks = [];
        for await (const chunk of stream) chunks.push(chunk);
        await mkdir(path.dirname(target), { recursive: true });
        await writeFile(target, Buffer.concat(chunks));
      }
      zip.readEntry();
    } catch (error) { zip.close(); reject(error); }
  });
  zip.on('end', resolve);
  zip.readEntry();
});
if (count !== 375) throw new Error('Atlas package entry count mismatch');
await writeFile(path.join(destination, 'complete.zip'), bytes);
console.log('Installed verified atlas: 368 symbols, 375 package entries.');
