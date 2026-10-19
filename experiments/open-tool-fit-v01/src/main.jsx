import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { Excalidraw, convertToExcalidrawElements } from "@excalidraw/excalidraw";
import { parseMermaidToExcalidraw } from "@excalidraw/mermaid-to-excalidraw";
import "@excalidraw/excalidraw/index.css";
import source from "../sample-msc.mmd";
import "./style.css";

// Editor sandbox only. These elements must NOT become BOSS slide authority.
// Official Excalidraw converter accepts a supported Mermaid subset.
function Trial(){
  const [scene,setScene]=useState(null);
  const [status,setStatus]=useState("PARSING");
  useEffect(()=>{
    let active=true;
    (async()=>{
      try {
        const result=await parseMermaidToExcalidraw(source,{
          themeVariables:{fontSize:"24px"},maxEdges:25,maxTextSize:3000
        });
        if(!active)return;
        const skeleton=result.elements||[];
        const elements=convertToExcalidrawElements(skeleton);
        const sceneText=elements.filter(x=>x.type==="text").map(x=>x.text||"").join(" ");
        const types=elements.reduce((a,x)=>{a[x.type]=(a[x.type]||0)+1;return a;},{});
        window.__bossTrial={
          state:"CONVERTED",
          skeletonCount:skeleton.length,
          editableElementCount:elements.length,
          types,hasHold:/HOLD/.test(sceneText),
          sourceKind:"mermaid",outputKind:"excalidraw-scene",
          release:"NOT_AUTHORIZED",visualApproval:"NOT_TESTED"
        };
        setScene({elements,appState:{viewBackgroundColor:"#FFFFFF"}});
        setStatus("SCENE_READY");
      } catch(error){
        if(!active)return;
        window.__bossTrial={state:"FAIL",reason:String(error)};
        setStatus("FAILED: "+String(error));
      }
    })();
    return()=>{active=false;};
  },[]);
  return <div className="trial">
    <header>
      <div><strong>BOSS / OPEN TOOL TRIAL</strong><span>MAIN STREET COPY · MERMAID → EXCALIDRAW</span></div>
      <div>CONCEPT ONLY / NOT APPROVED</div>
    </header>
    <section className="explain">
      <h1>Editable storyboard conversion</h1>
      <p>Source: synthetic Mermaid intake / HOLD process. Output: Excalidraw elements in a separate editor, <em>not</em> the finished React/Tailwind slide.</p>
      <p className="status" data-conversion-status={status}>{status}</p>
    </section>
    <div className="editor" data-test-editor={Boolean(scene)}>
      {scene && <Excalidraw initialData={{elements:scene.elements,appState:scene.appState,scrollToContent:true}}
         excalidrawAPI={api=>{window.__bossEditorApi=api;}}
         UIOptions={{canvasActions:{loadScene:false,saveAsImage:false}}}/>}
    </div>
    <footer><strong>EDITOR PROOF</strong> · preserved BOSS palette in host shell · artwork/diagram styling not production-approved</footer>
  </div>;
}
createRoot(document.getElementById("root")).render(<Trial/>);
