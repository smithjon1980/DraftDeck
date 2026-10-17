import {build} from 'esbuild';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
await mkdir('public/studio',{recursive:true});
execFileSync(process.execPath,['node_modules/@tailwindcss/cli/dist/index.mjs','-i','studio/style.css','-o','public/studio/style.css','--minify'],{stdio:'inherit'});
const connector='data:image/png;base64,'+(await readFile('studio/artwork/connector-v1.png')).toString('base64');
const css=await readFile('public/studio/style.css','utf8');
const logo='data:image/jpeg;base64,'+(await readFile('studio/logo.jpg')).toString('base64');
await build({entryPoints:['studio/app.jsx'],bundle:true,minify:true,outfile:'public/studio/app.js',define:{'process.env.NODE_ENV':'"production"',STUDIO_CSS:JSON.stringify(css),STUDIO_LOGO:JSON.stringify(logo),STUDIO_CONNECTOR:JSON.stringify(connector)}});
await writeFile('public/studio/index.html','<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BOSS Slide Studio</title><link rel="stylesheet" href="/tools/slides/style.css"></head><body><div id="root"><p>Loading Slide Studio…</p></div><script src="/tools/atlas/assets.js"></script><script src="/tools/slides/app.js"></script></body></html>');

await mkdir('public/studio/assembly',{recursive:true});
await build({entryPoints:['studio/assembly-app.jsx'],bundle:true,minify:true,outfile:'public/studio/assembly/app.js',define:{'process.env.NODE_ENV':'\"production\"',STUDIO_CSS:JSON.stringify(css),STUDIO_LOGO:JSON.stringify(logo),STUDIO_CONNECTOR:JSON.stringify(connector)}});
await writeFile('public/studio/assembly/index.html','<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>BOSS Assembly Studio</title><link rel=\"stylesheet\" href=\"/tools/slides/style.css\"></head><body><div id=\"root\">Loading assembly studio…</div><script src=\"/tools/slides/assembly/app.js\"></script></body></html>');
