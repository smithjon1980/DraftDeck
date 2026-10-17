import React from 'react';
import {AssemblySlide} from './assembly.jsx';
export const variants={A:'Editorial split',B:'Evidence window',C:'Working agreement',D:'Reflection rail'};
export function Slide({slide:s,project:p,index=0,asset,logo,reviewed=false}){
 if(s.assembly)return <AssemblySlide slide={s} logo={logo} artwork={typeof STUDIO_CONNECTOR==='string'?STUDIO_CONNECTOR:''}/>;
 const paragraphs=s.body.split('\n').filter(Boolean);
 return <section className={'slide variant-'+s.variant} data-document-role="page" aria-label={'Slide '+(index+1)}>
  <header className="slide-mast"><img src={logo} alt="Bioscillate Operating System by Seven"/><span>{p.title||'[Project title]'} / {String(index+1).padStart(2,'0')}</span><span>{reviewed?'HUMAN REVIEW RECORDED':'CANDIDATE / '+s.variant}</span></header>
  <div className="slide-title"><p className="eyebrow">{p.audience||'[Audience not supplied]'}</p><h1>{s.title||'[Takeaway title]'}</h1><p className="slide-lead">{s.lead||'[Supporting statement]'}</p></div>
  <div className="slide-content"><div className="narrative">{paragraphs.length?paragraphs.map((t,i)=><p key={i}>{t}</p>):<p>[Enter source-grounded slide copy]</p>}</div><aside className="drawing">{asset?<><img src={asset.src} alt={asset.name}/><p className="drawing-caption">{asset.reference} · {asset.name}</p></>:<div className="empty-art">Artwork not selected<br/><small>Choose a technical symbol when it supports the story.</small></div>}</aside><div className="evidence"><strong>Evidence window</strong><p>{s.evidence||'[Evidence and limits not recorded]'}</p></div></div>
  <footer className="slide-footer"><div><strong>Pause & consider</strong><p>{s.question||'[Reflective question]'}</p></div><span>{s.sourceIds.length} source reference{s.sourceIds.length===1?'':'s'} · {s.variant} / {variants[s.variant]}</span></footer>
 </section>;
}
