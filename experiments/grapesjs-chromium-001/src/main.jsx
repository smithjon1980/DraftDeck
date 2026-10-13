import React,{useEffect,useRef,useState} from 'react';
import{createRoot}from'react-dom/client';
import grapesjs from 'grapesjs';
import 'grapesjs/dist/css/grapes.min.css';
import './ui.css';
import {sampleHtml,sampleCss} from './sample.js';
function download(name,txt,type='text/plain'){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([txt],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),2500)}
function App(){
 const slot=useRef(null),ed=useRef(null),upload=useRef(null);
 const [selected,setSelected]=useState(null),[message,setMessage]=useState('Select text on the canvas to edit it.');
 useEffect(()=>{
  const editor=grapesjs.init({container:slot.current,height:'calc(100vh - 82px)',storageManager:false,fromElement:false,components:sampleHtml,style:sampleCss,canvas:{styles:[]},panels:{defaults:[]},deviceManager:{devices:[{id:'slide',name:'Slide 16:9',width:'1536px'},{id:'mobile',name:'Mobile',width:'390px'}]}});
  ed.current=editor;editor.setDevice('slide');
  function updateSelection(){const cmp=editor.getSelected();if(!cmp){setSelected(null);return}setSelected({id:cmp.getId(),tag:cmp.get('tagName'),text:cmp.is('text')?cmp.get('content'):null});}
  editor.on('component:selected',updateSelection);editor.on('component:deselected',updateSelection);
  return()=>{editor.off('component:selected',updateSelection);editor.off('component:deselected',updateSelection);ed.current=null;editor.destroy()}
 },[]);
 function changeText(txt){const editor=ed.current,cmp=editor?.getSelected();if(!cmp||!cmp.is('text'))return;cmp.set('content',txt);setSelected(s=>({...s,text:txt}));setMessage('Text updated in editable source.');}
 function saveProject(){if(ed.current)download('overview01.project.json',JSON.stringify(ed.current.getProjectData(),null,2),'application/json')}
 function loadProject(file){if(!file||!ed.current)return;const reader=new FileReader();reader.onload=()=>{try{const data=JSON.parse(reader.result);if(!data.pages&&!data.components)throw Error('Not a GrapesJS project');ed.current.loadProjectData(data);setMessage('Project JSON restored. Check content before exporting.')}catch(e){setMessage('Import failed: '+e.message)}};reader.readAsText(file)}
 function exportSource(){const editor=ed.current;if(!editor)return;const html=editor.getHtml(),css=editor.getCss();download('overview01.html',`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>@page{size:16in 9in;margin:0}html,body{padding:0;margin:0}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}\n${css}</style></head><body>${html}</body></html>`,'text/html')}
 return <><header><strong>BOSS / DraftDeck · GrapesJS Trial</strong><nav><button onClick={()=>ed.current?.setDevice('slide')}>Slide</button><button onClick={()=>ed.current?.setDevice('mobile')}>Mobile</button><button onClick={saveProject}>Save project</button><button onClick={()=>upload.current?.click()}>Load project</button><button onClick={exportSource}>Export HTML/CSS</button><input ref={upload} type="file" accept=".json,application/json" hidden onChange={e=>loadProject(e.target.files?.[0])}/></nav></header><section className="workspace"><aside><h2>Editable content</h2><p>{message}</p>{selected?<><small>{selected.tag} · {selected.id}</small>{selected.text!==null?<textarea rows={9} aria-label="Selected text" value={selected.text} onChange={e=>changeText(e.target.value)}/>:<p>Selected graphical element: use canvas drag or style tools in a future iteration.</p>}</>:<p>No element selected.</p>}<hr/><p>Text is live HTML. This trial does not create named PDF layers, and no Canva adapter is involved.</p></aside><main ref={slot}/></section></>
};createRoot(document.getElementById('root')).render(<App/>);
