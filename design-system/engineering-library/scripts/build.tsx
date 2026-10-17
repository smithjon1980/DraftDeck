import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { EngineeringAtlas, type EngineeringAsset } from '../src/components.js';

const assets: EngineeringAsset[]=JSON.parse(readFileSync('dist/assets.json','utf8'));
const bounds=JSON.parse(readFileSync('vendor/viewboxes.json','utf8'));
const provenance=JSON.parse(readFileSync('vendor/provenance.json','utf8'));
for(const a of assets){
  if(!bounds[a.id])throw Error('Missing inspected viewbox: '+a.id);
  a.svg=a.svg.replace(/viewBox="[^"]*"/,`viewBox="${bounds[a.id].join(' ')}"`);
  const family=a.source.split('/')[0], path=a.source.slice(family.length+1);
  const commit=provenance.find((p:any)=>p.family===family&&p.path===path).commit;
  if(family==='iso'){
    a.attribution='Steven Baltakatei Sandoval, copyright 2023. Adapted by DraftDeck: extracted symbol geometry and cropped viewbox; editorial labels separated.';
    a.sourceUrl='https://gitlab.com/baltakatei/BK-2020-04/-/blob/'+commit+'/'+path;
    a.licenseUrl='https://creativecommons.org/licenses/by-sa/4.0/';
  }else if(family==='qet'){
    a.attribution='The QElectroTech team. Adapted by DraftDeck from ELMT primitives to SVG; terminals retained in asset record. Upstream prohibits use as sample data for building machine-learning models.';
    a.sourceUrl='https://github.com/qelectrotech/qelectrotech-elements/blob/'+commit+'/'+path;
    a.licenseUrl='https://creativecommons.org/licenses/by/3.0/';
  }else{
    a.attribution='FreeCAD contributors; original per-file metadata retained and original source included in source-pack.zip. Adapted by DraftDeck: cropped viewbox.';
    a.sourceUrl='https://github.com/FreeCAD/FreeCAD/blob/'+commit+'/'+path;
    a.licenseUrl='https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html';
  }
  const notice=JSON.stringify({attribution:a.attribution,source:a.sourceUrl,license:a.license,licenseUrl:a.licenseUrl}).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
  a.svg=a.svg.replace(/(<svg\b[^>]*>)/,'$1<metadata>'+notice+'</metadata>');
}
writeFileSync('dist/assets.json',JSON.stringify(assets));
execFileSync(process.execPath,['node_modules/@tailwindcss/cli/dist/index.mjs','-i','src/styles.css','-o','dist/styles.css','--minify'],{stdio:'inherit'});
const css=readFileSync('dist/styles.css','utf8');
const body=renderToStaticMarkup(<EngineeringAtlas assets={assets}/>);
const data=JSON.stringify(assets).replaceAll('<','\\u003c');
writeFileSync('dist/index.html',`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DraftDeck Engineering Atlas</title><style>${css}</style></head><body>${body}<script type="application/json" id="asset-data">${data}</script><script>
const data=JSON.parse(document.querySelector('#asset-data').textContent), byId=new Map(data.map(a=>[a.id,a]));
const query=document.querySelector('#query'),family=document.querySelector('#family');
function filter(){let n=0;document.querySelectorAll('.asset').forEach(e=>{e.hidden=!(e.dataset.search.includes(query.value.toLowerCase())&&(!family.value||e.dataset.family===family.value));if(!e.hidden)n++});document.querySelector('#count').textContent=n+' assets'}query.addEventListener('input',filter);family.addEventListener('change',filter);
document.querySelectorAll('.asset').forEach(e=>e.addEventListener('click',()=>{const a=byId.get(e.dataset.id);document.querySelector('#detail-name').textContent=a.name;const image=document.querySelector('#detail-image');image.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(a.svg);image.alt=a.name;const meta=document.querySelector('#detail-meta');meta.replaceChildren();for(const [k,v]of Object.entries({Collection:a.family,Reference:a.reference,Attribution:a.attribution,Source:a.sourceUrl,License:a.license+' / '+a.licenseUrl,Ports:a.ports?JSON.stringify(a.ports):'Not encoded; inspect source geometry'})){const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=k;dd.textContent=v;meta.append(dt,dd)}const download=document.querySelector('#detail-download');download.href=image.src;download.download=a.id+'.svg';document.querySelector('#inspector').showModal()}));
</script></body></html>`);
console.log('Built standalone technical atlas: '+assets.length+' assets.');
