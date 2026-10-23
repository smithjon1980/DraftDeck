import React, {useEffect,useLayoutEffect,useRef,useState} from 'react';
const SAMPLE=['A proposed facility is not proof of a functioning operation.','An authorized work order defines what must be produced.','An inspection produces evidence of whether the output meets the specification.','Shipping labels, carrier handoffs and recipient deliveries are different evidence states.'];
function ScriptColumns({count}){
  return <div className="manuscript-grid" style={{gridTemplateColumns:'repeat('+count+', minmax(0,1fr))'}}>
    {Array.from({length:count},(_,index)=><section className="copy-col" key={index} data-col={index}>
      <h2>MANUSCRIPT COLUMN {String(index+1).padStart(2,'0')}</h2>
      <p className="spoken" data-para-id={'PUBLIC_SAMPLE_'+index}>{SAMPLE[index]}</p>
    </section>)}
  </div>;
}
function Slide({count,showGuides}){
 return <article className={'slide '+(showGuides?'guides':'')} role="document" aria-label={'Synthetic layout '+count}>
  <header><div className="sample-mark">B<span>O</span>S<span>S</span></div><div className="meta">React + Tailwind · PUBLIC SAMPLE</div></header>
  <h1>The operation matters more than the drawing.</h1>
  <p className="kicker">ONE PRIMARY IDEA / {count} MANUSCRIPT COLUMN{count>1?'S':''}</p>
  <ScriptColumns count={count}/>
  <footer>STRUCTURAL DEMONSTRATION · DOES NOT CONTAIN EPISODE 01 NARRATION</footer>
 </article>;
}
function Stage({count,showGuides}){
 const box=useRef(null);
 const [bounds,setBounds]=useState({width:0,height:0});
 useLayoutEffect(()=>{
  const obs=new ResizeObserver(items=>setBounds({width:items[0].contentRect.width,height:items[0].contentRect.height}));
  if(box.current)obs.observe(box.current);
  return ()=>obs.disconnect();
 },[]);
 const scale=Math.min(bounds.width/1920,bounds.height/1080);
 return <div className="stage" ref={box}><div className="canvas-wrap" style={{transform:'translate(-50%,-50%) scale('+(scale||0.1)+')'}}><Slide count={count} showGuides={showGuides}/></div></div>;
}
export default function App(){
 const [count,setCount]=useState(1),[guides,setGuides]=useState(true);
 return <main className="h-screen min-h-[520px] flex flex-col bg-slate-900 text-white">
   <nav className="flex items-center justify-between gap-4 border-b border-slate-700 px-5 py-3">
    <strong className="text-base">BOSS / React Editorial Proof</strong>
    <div className="flex items-center gap-2">
     {[1,2,3,4].map(n=><button key={n} onClick={()=>setCount(n)} aria-current={count===n?'page':undefined} className={'rounded border px-3 py-1 text-sm '+(count===n?'border-cyan-300 bg-slate-700':'border-slate-500')}>{n} COL</button>)}
     <label className="ml-2 text-xs"><input type="checkbox" checked={guides} onChange={e=>setGuides(e.target.checked)}/> Grid</label>
    </div>
   </nav><Stage count={count} showGuides={guides}/>
   <div className="border-t border-slate-700 p-3 text-xs text-slate-300">Live JSX · CSS fixed canvas · separate narration DOM · synthetic public copy only</div>
 </main>;
}
