import {chromium} from 'playwright';import{readFile,mkdir,writeFile}from'node:fs/promises';import{resolve,dirname}from'node:path';import{createHash}from'node:crypto';
export async function buildPdf({source,output,runId='trial-pdf-001'}){
 const html=await readFile(resolve(source),'utf8');
 if(!html.includes('<html')||!html.includes('</html>'))throw Error('INVALID_HTML_SOURCE');
 const target=resolve(output);await mkdir(dirname(target),{recursive:true});
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1536,height:864},deviceScaleFactor:1});
  await page.goto('file://'+resolve(source),{waitUntil:'load'});
  await page.evaluate(()=>document.fonts.ready);
  await page.pdf({path:target,width:'16in',height:'9in',printBackground:true,preferCSSPageSize:true,margin:{top:'0',right:'0',bottom:'0',left:'0'}});
 }finally{await browser.close()}
 const bytes=await readFile(target);
 if(bytes.subarray(0,5).toString()!=='%PDF-')throw Error('PDF_SIGNATURE_INVALID');
 const manifest={run_id:runId,status:'BUILT_UNVERIFIED_VISUAL',source:resolve(source),output:target,sha256:createHash('sha256').update(bytes).digest('hex'),bytes:bytes.length,storage_status:'EPHEMERAL_CI_ARTIFACT'};
 await writeFile(target+'.manifest.json',JSON.stringify(manifest,null,2)+'\n');
 return manifest;
}
