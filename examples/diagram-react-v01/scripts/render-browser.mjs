// Chromium evidence: React/Tailwind reconstructs native HTML components from
// compiler-validated Mermaid/PlantUML source, not an embedded diagram image.
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import puppeteer from "puppeteer";

const project=path.resolve(import.meta.dirname,"..");
const dist=path.join(project,"dist");
const screenshots=path.join(project,"screenshots");
fs.mkdirSync(screenshots,{recursive:true});
const readIR=file=>JSON.parse(fs.readFileSync(path.join(dist,"diagrams",file),"utf8"));
const referenceFlow=readIR("intake.ir.json"),referenceSeq=readIR("clarification.ir.json");
const browser=await puppeteer.launch({
  executablePath:process.env.CHROME_BIN||"/usr/bin/google-chrome",headless:true,
  args:["--no-sandbox","--disable-setuid-sandbox","--allow-file-access-from-files"]
});
const report=[];
try{
  for(let i=1;i<=2;i++){
    const page=await browser.newPage();
    await page.setViewport({width:1920,height:1080,deviceScaleFactor:1});
    const errors=[];
    page.on("pageerror",err=>errors.push(err.message));
    const href=pathToFileURL(path.join(dist,"index.html")).href+"?slide="+i;
    await page.goto(href,{waitUntil:"load",timeout:45000});
    await page.waitForSelector("#slide[data-render-master='react-tailwind']");
    if(i===1)await page.waitForFunction(()=>document.querySelector('[data-boss-composer="flow"]')?.dataset.edgesReady==="true");
    await page.evaluate(async()=>{await document.fonts.ready;});
    const data=await page.evaluate(()=>{
      const root=document.querySelector("#slide");
      const b=root.getBoundingClientRect();
      const composer=root.querySelector("[data-boss-composer]");
      const flow=composer?.dataset.bossComposer==="flow";
      return {
        slideId:root.dataset.slideId,canvas:[b.width,b.height],
        composerType:composer?.dataset.bossComposer||null,
        sourceSha256:composer?.dataset.sourceHash||null,
        independentEditorialNodes:root.querySelectorAll("h1,h2,p").length,
        actualDiagramImages:composer.querySelectorAll("img").length,
        nativeDiagramLabels:composer.querySelectorAll("[data-boss-native-label]").length,
        text:root.innerText,
        groupIds:flow?Array.from(composer.querySelectorAll("[data-boss-stage]")).map(x=>x.dataset.bossStage):[],
        nodeIds:flow?Array.from(composer.querySelectorAll("[data-boss-node]")).map(x=>x.dataset.bossNode):[],
        edgeIds:flow?Array.from(composer.querySelectorAll("[data-boss-edge]")).map(x=>x.dataset.bossEdge):[],
        actorIds:!flow?Array.from(composer.querySelectorAll("[data-boss-actor]")).map(x=>x.dataset.bossActor):[],
        messageRows:!flow?Array.from(composer.querySelectorAll("[data-boss-message]")).map(x=>({
          from:x.dataset.from,to:x.dataset.to,branch:x.dataset.branch,
          label:x.querySelector("[data-boss-native-label]")?.textContent.replace(/^\s*\d+\s*/,"").trim()
        })):[],
        branchRows:!flow?Array.from(composer.querySelectorAll("[data-boss-branch]")).map(x=>x.dataset.bossBranch):[],
        overflowingNodes:Array.from(composer.querySelectorAll("[data-boss-node]")).filter(x=>{
          const r=x.getBoundingClientRect(),g=composer.getBoundingClientRect();
          return r.left<g.left-1||r.right>g.right+1||r.top<g.top-1||r.bottom>g.bottom+1;
        }).map(x=>x.dataset.bossNode)
      };
    });
    if(errors.length)throw Error("BROWSER_RUNTIME_ERRORS:"+JSON.stringify(errors));
    if(data.canvas[0]!==1920||data.canvas[1]!==1080)throw Error("CANVAS_DRIFT:"+JSON.stringify(data.canvas));
    if(data.actualDiagramImages!==0)throw Error("SVG_IMAGE_EMBED_STILL_PRESENT");
    if(data.independentEditorialNodes<10||data.nativeDiagramLabels<8)throw Error("MISSING_NATIVE_HTML_TEXT");
    if(!data.text.includes("REFLECT")||!data.text.toUpperCase().includes("HOLD"))throw Error("MISSING_STORY_OR_REFLECTION");
    if(data.overflowingNodes.length)throw Error("NODE_OUTSIDE_DIAGRAM:"+data.overflowingNodes);
    const expected=i===1?referenceFlow:referenceSeq;
    if(data.sourceSha256!==expected.sourceSha256)throw Error("SOURCE_HASH_MISMATCH");
    if(i===1){
      const same=(a,b)=>JSON.stringify([...a].sort())===JSON.stringify([...b].sort());
      if(!same(data.groupIds,expected.groups.map(x=>x.id)))throw Error("LOST_MERMAID_STAGE");
      if(!same(data.nodeIds,expected.nodes.map(x=>x.id)))throw Error("LOST_MERMAID_NODE");
      if(!same(data.edgeIds,expected.edges.map(x=>x.from+"->"+x.to)))throw Error("LOST_MERMAID_LINK");
    }else{
      if(JSON.stringify(data.actorIds)!==JSON.stringify(expected.actors.map(x=>x.id)))throw Error("UML_ACTOR_DRIFT");
      const messages=expected.items.filter(x=>x.type==="message").map(x=>({
        from:x.from,to:x.to,branch:x.branch,label:x.label
      }));
      if(JSON.stringify(data.messageRows)!==JSON.stringify(messages))throw Error("UML_MESSAGE_DRIFT");
      if(JSON.stringify(data.branchRows)!==JSON.stringify(
        expected.items.filter(x=>x.type!=="message").map(x=>x.type)))throw Error("UML_ALT_ELSE_DRIFT");
    }
    const name=i===1?"flowchart":"sequence";
    await page.screenshot({path:path.join(screenshots,name+".png"),type:"png"});
    await page.pdf({path:path.join(screenshots,name+".pdf"),width:"1920px",height:"1080px",
      printBackground:true,preferCSSPageSize:false});
    report.push({
      slide:data.slideId,status:"STRUCTURE_AND_CHROMIUM_PASS",
      engineInputSha256:data.sourceSha256,reactComposer:data.composerType,
      nativeDiagramLabels:data.nativeDiagramLabels,embeddedDiagramImages:data.actualDiagramImages,
      flowEdges:data.edgeIds.length,sequenceMessages:data.messageRows.length,
      browserErrors:errors,semanticApproval:"NOT_TESTED",visualApproval:"PENDING",logoApproval:"PENDING",
    });
    await page.close();
  }
}finally{await browser.close();}
fs.writeFileSync(path.join(screenshots,"report.json"),JSON.stringify({
  status:"REACT_IR_EQUIVALENCE_STRUCTURAL_PASS",
  model_inference:"NOT_EXECUTED",source_privacy:"SYNTHETIC_ONLY",
  approval:"PENDING",limit:"restricted grammar and synthetic fixtures, not full Mermaid/UML coverage",
  slides:report
},null,2)+"\n");
console.log(JSON.stringify(report));
