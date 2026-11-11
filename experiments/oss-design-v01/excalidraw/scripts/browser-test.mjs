import fs from "node:fs";
import path from "node:path";
import {pathToFileURL} from "node:url";
import puppeteer from "puppeteer";
const root=path.resolve(import.meta.dirname,"..");
const browser=await puppeteer.launch({
  executablePath:process.env.CHROME_BIN || "/usr/bin/google-chrome",
  headless:true,args:["--no-sandbox","--disable-setuid-sandbox","--allow-file-access-from-files"]
});
const out=path.join(root,"screenshots");fs.mkdirSync(out,{recursive:true});
try{
  const page=await browser.newPage();
  await page.setViewport({width:1520,height:900,deviceScaleFactor:1});
  const errors=[];page.on("pageerror",e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.join(root,"dist","index.html")).href,
    {waitUntil:"domcontentloaded",timeout:60000});
  try {
    await page.waitForFunction(()=>{
      const api=window.__bossExcalidrawAPI;
      if(!api) return false;
      const els=api.getSceneElements();
      const ids=els.map(x=>x.id);
      const required=["msc-request","msc-check","msc-hold","msc-work"];
      if(!required.every(x=>ids.includes(x))) return false;
      window.__bossTrial={...(window.__bossTrial||{}),ready:true,
        initialCount:els.length,initialIDs:ids};
      return true;
    },{timeout:20000});
  } catch(err){
    const diagnostics=await page.evaluate(()=>({
      status:document.querySelector("#status")?.textContent,
      root:document.querySelector("#root")?.textContent?.slice(0,800),
      apiPresent:Boolean(window.__bossExcalidrawAPI),
      currentIDs:window.__bossExcalidrawAPI?.getSceneElements()?.map(x=>x.id),
      trial:window.__bossTrial,
      appCanvasCount:document.querySelectorAll("canvas").length,
    }));
    await page.screenshot({path:path.join(out,"initialization-failure.png"),fullPage:true});
    console.error("BROWSER_SCENE_DIAGNOSTIC",JSON.stringify({diagnostics,errors},null,2));
    throw err;
  }
  const initial=await page.evaluate(()=>window.__bossTrial);
  if(!initial.initialIDs.includes("msc-request")||!initial.initialIDs.includes("msc-hold")||
     !initial.initialIDs.includes("msc-check")||!initial.initialIDs.includes("msc-work")){
    throw Error("SCENE_IMPORT_MISSING_REQUIRED_NODES:"+JSON.stringify(initial.initialIDs));
  }
  if(initial.initialCount<7)throw Error("SCENE_IMPORT_UNDERSIZED:"+initial.initialCount);
  await page.screenshot({path:path.join(out,"excalidraw-before.png"),fullPage:true});
  await page.click("#edit");
  await page.waitForFunction(()=>window.__bossTrial?.modified===true,{timeout:15000});
  const after=await page.evaluate(()=>window.__bossTrial);
  const serialized=JSON.parse(after.serialized);
  const ids=serialized.elements.map(x=>x.id);
  if(!ids.includes("msc-hold")||!ids.includes("msc-request"))throw Error("EXPORT_LOST_NODE");
  if(after.editResult.holdStroke!=="#000000")throw Error("EDIT_DID_NOT_PERSIST");
  if(errors.length)throw Error("BROWSER_ERRORS:"+errors.join(" | "));
  await page.screenshot({path:path.join(out,"excalidraw-edited.png"),fullPage:true});
  fs.writeFileSync(path.join(out,"excalidraw-roundtrip.json"),after.serialized+"\n");
  const report={
    test:"ACTUAL_EXCALIDRAW_REACT_LIBRARY_IMPORT_EDIT_EXPORT",
    status:"PASS",initialElementCount:initial.initialCount,exportedElementCount:ids.length,
    requiredNodeIDsRetained:["msc-request","msc-check","msc-hold","msc-work"].every(id=>ids.includes(id)),
    actualEditedHoldStroke:after.editResult.holdStroke,
    runtimeErrors:errors,brandProductionCompliance:"NOT_ESTABLISHED",
    nativeEditorialReactMaster:"UNCHANGED",humanVisualApproval:"PENDING",
    accountConnection:"NOT_TESTED",cost:"NO_PAID_INFERENCE"
  };
  fs.writeFileSync(path.join(out,"excalidraw-report.json"),JSON.stringify(report,null,2)+"\n");
  console.log(JSON.stringify(report));
  await page.close();
}finally{await browser.close();}
