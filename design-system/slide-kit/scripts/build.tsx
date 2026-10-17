import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from 'node:fs';
import { Catalogue } from '../src/catalogue.js';

mkdirSync('dist', { recursive: true });
execFileSync(process.execPath, ['node_modules/@tailwindcss/cli/dist/index.mjs', '-i', 'src/tokens.css', '-o', 'dist/styles.css', '--minify'], { stdio: 'inherit' });
const markup = renderToStaticMarkup(<Catalogue />);
const css = readFileSync('dist/styles.css', 'utf8');
const license = readFileSync('node_modules/lucide-react/LICENSE', 'utf8');
writeFileSync('dist/index.html', `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>DraftDeck component catalogue</title><style>${css}</style></head><body><main>${markup}</main><script>function fit(){const s=document.querySelector('.slide');s.style.transformOrigin='top left';s.style.transform='scale('+Math.min(1,innerWidth/1920)+')';document.querySelector('main').style.height=(1080*Math.min(1,innerWidth/1920))+'px'}fit();addEventListener('resize',fit);addEventListener('beforeprint',()=>{document.querySelector('.slide').style.transform='none'});addEventListener('afterprint',fit);</script><!-- Lucide notice follows. -->\n<!-- ${license.replaceAll('--', '—')} -->\n</body></html>`);
copyFileSync('node_modules/lucide-react/LICENSE', 'dist/LUCIDE-LICENSE');
console.log('Built self-contained dist/index.html with live HTML text and compiled Tailwind CSS.');
