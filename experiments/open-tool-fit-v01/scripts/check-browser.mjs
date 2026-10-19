import fs from "node:fs";
import path from "node:path";
import {pathToFileURL} from "node:url";
import puppeteer from "puppeteer";

const root=path.resolve(import.meta.dirname,"..");
const out=path.join(root,"proof");
fs.mkdirSync(out,{recursive:true});
const browser=await puppeteer.launch({
  executablePath:process.env.CHROME_BIN||"/usr/bin/google-chrome",headless:true,
  args:["--no-sandbox","--disable-setuid-sandbox","--allow-file-access-from-files","--disable-dev-shm-usage"]
});
try{
  const page=await browser.newPage();
  await page.setViewport({width:1600,height:900,deviceScaleFactor:1});
  const errors=[];
  page.on("pageerror",e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.join(root,"dist","index.html")).href,
    {waitUntil:"load",timeout:45000});
  await page.waitForFunction(()=>window.__bossTrial?.state==="CONVERTED" ||
    window.__bossTrial?.state==="FAIL",{timeout:60000});
  await page.waitForFunction(()=>Boolean(window.__bossEditorApi?.getSceneElements),
    {timeout:45000});
  const result=await page.evaluate(()=>{
    const trial=window.__bossTrial;
    const editor=window.__bossEditorApi;
    const items=editor.getSceneElements();
    const labels=items.filter(x=>x.type==="text").map(x=>x.text||"");
    const types=items.reduce((acc,x)=>{acc[x.type]=(acc[x.type]||0)+1;return acc;},{});
    return {
      conversion:trial.state,
      declaredEditableElements:trial.editableElementCount,
      mountedEditorElements:items.length,
      elementTypes:types,
      holdPreserved:labels.join(" ").includes("HOLD"),
      outputUsesExcalidrawAPI:typeof editor.updateScene==="function",
      sourceIsSynthetic:true,
      finalReactSlideReplaced:false,
      humanVisualReview:"PENDING"
    };
  });
  const assertions={
    noBrowserExceptions:errors.length===0,
    conversionSucceeded:result.conversion==="CONVERTED",
    editorHasElements:result.mountedEditorElements>=5,
    editorElementsMatchConversion:result.mountedEditorElements===result.declaredEditableElements,
    editableShapesExist:((result.elementTypes.rectangle||0)+(result.elementTypes.diamond||0))>=2,
    editableArrowsExist:(result.elementTypes.arrow||0)>=1,
    sourceHoldTextPreserved:result.holdPreserved,
    programmaticEditorAPI:result.outputUsesExcalidrawAPI,
  };
  await page.screenshot({path:path.join(out,"excalidraw-conversion.png"),fullPage:false});
  fs.writeFileSync(path.join(out,"evidence.json"),JSON.stringify({
    status:Object.values(assertions).every(Boolean)?"PASS":"FAIL",
    assertions,result,browserErrors:errors,
    disclaimer:"Proof of a synthetic Mermaid-to-Excalidraw conversion and React editor mount, NOT print fidelity, UML semantics, editor save/reopen, student scale or BOSS visual approval."
  },null,2)+"\n");
  console.log(JSON.stringify({assertions,result,errors}));
  if(!Object.values(assertions).every(Boolean))throw new Error("EXCALIDRAW_CONVERSION_OR_EDITOR_CHECK_FAILED");
}finally{
  await browser.close();
}
