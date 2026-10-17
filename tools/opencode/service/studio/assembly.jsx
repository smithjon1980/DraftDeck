import React from 'react';
function Segment({a,b}){const dx=b[0]-a[0],dy=b[1]-a[1];return <div className="assembly-leader" style={{left:a[0],top:a[1],width:Math.hypot(dx,dy),transform:`rotate(${Math.atan2(dy,dx)*180/Math.PI}deg)`}}/>;}
export function AssemblySlide({slide,logo,artwork,onMove,onPointer,index=0}){
 const model=slide.assembly;
 return <section className="assembly-slide" data-document-role="page" aria-label={'Assembly slide '+(index+1)}>
 <img className="assembly-artwork" src={artwork} alt="Illustrative exploded keyed cable connector with aligned mating halves, threaded collars, cutaway conductors and detached key plates"/>
 <div className="assembly-frame"/>
 <p className="assembly-metadata">BOSS / ENGINEERING COMP / RECONSTRUCTION</p>
 <h1 className="assembly-title">{slide.title}</h1>
 <div className="assembly-brand"><img src={logo} alt="bioscillate — Operating System by Seven"/></div>
 {model.callouts.map((c,i)=>{const start=[c.x+(c.side==='left'?246:-26),c.y+30];return <React.Fragment key={c.id}><Segment a={start} b={[c.bendX,c.bendY]}/><Segment a={[c.bendX,c.bendY]} b={[c.targetX,c.targetY]}/><span className="assembly-terminal" style={{left:c.targetX-7,top:c.targetY-7}}/><div className={'assembly-callout '+(onMove?'assembly-movable':'')} style={{left:c.x,top:c.y,width:c.side==='right'?330:570}} tabIndex={onMove?0:undefined} role={onMove?'button':undefined} aria-label={onMove?`Move ${c.title}; arrow keys move 4 pixels, Shift moves 20`:undefined} onKeyDown={onMove?e=>{const delta=e.shiftKey?20:4;const move={ArrowLeft:[-delta,0],ArrowRight:[delta,0],ArrowUp:[0,-delta],ArrowDown:[0,delta]}[e.key];if(move){e.preventDefault();onMove(i,c.x+move[0],c.y+move[1]);}}:undefined} onPointerDown={onPointer?e=>onPointer(e,i):undefined}><h2>{c.title}</h2><p>{c.text}</p></div></React.Fragment>;})}
 <footer className="assembly-footer"><p className="assembly-reflection">{slide.question}</p><p className="assembly-scope">{slide.evidence}</p></footer>
 </section>;
}
