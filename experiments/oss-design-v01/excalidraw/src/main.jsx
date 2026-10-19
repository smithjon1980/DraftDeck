import React, {useRef,useState} from "react";
import {createRoot} from "react-dom/client";
import {Excalidraw,convertToExcalidrawElements,serializeAsJSON} from "@excalidraw/excalidraw";
import "@excalidraw/excalidraw/index.css";
import "./style.css";
import scene from "../assets/scene.json";

const source=convertToExcalidrawElements(scene.elements);
function App(){
  const apiRef=useRef(null);
  const [status,setStatus]=useState("LOADING");
  function markReady(api){
    if(!api)return;
    apiRef.current=api;
    const current=api.getSceneElements();
    window.__bossTrial={ready:false, initialCount:current.length,
      initialIDs:current.map(x=>x.id),
      hasReactEditor:true, modified:false};
    setStatus("EDITOR MOUNTED / WAITING FOR SCENE");
  }
  function onSceneChange(elements){
    if(!window.__bossTrial) return;
    const ids=elements.map(x=>x.id);
    const expected=["msc-request","msc-check","msc-hold","msc-work"];
    if(expected.every(id=>ids.includes(id))){
      window.__bossTrial.ready=true;
      window.__bossTrial.initialCount=elements.length;
      window.__bossTrial.initialIDs=ids;
      setStatus("READY / EDITABLE SCRATCHPAD");
    }
  }
  function edit(){
    if(!apiRef.current)throw Error("NO_EXCALIDRAW_API");
    const before=apiRef.current.getSceneElements();
    const after=before.map(el=>el.id==="msc-hold"?
      {...el,strokeColor:"#000000",version:el.version+1,versionNonce:el.versionNonce+1}:el);
    apiRef.current.updateScene({elements:after});
    const now=apiRef.current.getSceneElements();
    const result={count:now.length,holdStroke:now.find(el=>el.id==="msc-hold")?.strokeColor,
      changed:now.find(el=>el.id==="msc-hold")?.strokeColor==="#000000"};
    window.__bossTrial.editResult=result;
    window.__bossTrial.modified=result.changed;
    window.__bossTrial.serialized=serializeAsJSON(now,apiRef.current.getAppState());
    setStatus(result.changed?"EDITED / JSON EXPORT READY":"EDIT FAILED");
  }
  return <main>
    <header><strong>BOSS / MAIN STREET COPY</strong><span>EXCALIDRAW INTEROPERABILITY — SCRATCHPAD ONLY</span></header>
    <section className="layout">
      <div className="editor" data-test-editor>
        <Excalidraw excalidrawAPI={markReady} onChange={onSceneChange} initialData={{
          elements:source,appState:{viewBackgroundColor:"#FFFFFF",zenModeEnabled:true,
            currentItemStrokeColor:"#000000"},files:{}
        }} UIOptions={{canvasActions:{loadScene:false}}}/>
      </div>
      <aside>
        <h1>Concept sketch, not production artwork.</h1>
        <p>The original four-node request and HOLD scenario is editable in the live Excalidraw React editor.</p>
        <p>Its hand-drawn visual language is NOT a substitute for the BOSS CAD/ISO/NC master or the React diagram composer.</p>
        <p><b>Method:</b> Load the actual library, inspect the scene elements, modify a synthetic node and export JSON.</p>
        <button id="edit" onClick={edit}>Test edit and JSON export</button>
        <div id="status">{status}</div>
        <footer>BRAND IDENTITY / CANDIDATE — NO LOGO REPLACEMENT</footer>
      </aside>
    </section>
  </main>;
}
createRoot(document.getElementById("root")).render(<App/>);
