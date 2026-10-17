import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { Layers } from 'lucide-react';
import { SlideCanvas, TopMetadataRail, ComponentLabel, ComparisonPanel, LayerStack, DecisionMatrix, AuditTable, ArtworkWithCaption, ReflectionFooter } from './components.js';

// Demonstration copy describes the kit; it is not approved lesson content.
export function Catalogue() {
  const art = 'data:image/svg+xml;base64,' + Buffer.from(renderToStaticMarkup(<Layers size={120} strokeWidth={1} />)).toString('base64');
  return <SlideCanvas title="Reusable slide components" footer={<ReflectionFooter question="Which pattern best explains this slide’s relationship?" notesLabel="Review notes: __________________________________" />}>
    <TopMetadataRail section="DraftDeck / Episode 01 profile" identifier="Component catalogue · Candidate 0.1" />
    <p className="caption mt-4 mb-6">Geometry studies from reference pages 5, 6, 9 and 19. Demonstration copy only. No lesson or artwork approval implied.</p>
    <div className="catalogue-grid">
      <section className="specimen"><ComponentLabel kind="comparison">01 / Comparison panel</ComponentLabel><ComparisonPanel left={{title:'Source',body:'Preserve supplied wording and provenance.'}} right={{title:'Candidate',body:'Label proposed changes for review.'}} /></section>
      <section className="specimen"><ComponentLabel kind="stack">02 / Layer stack</ComponentLabel><LayerStack layers={[{id:'01',label:'Content',description:'Source copy and evidence.'},{id:'02',label:'Composition',description:'Live text, layout and separate artwork.'},{id:'03',label:'Review',description:'Inspect the actual rendered result.'}]} /></section>
      <section className="specimen"><ComponentLabel kind="matrix">03 / Decision matrix</ComponentLabel><DecisionMatrix horizontal="one item → repeated items" vertical="low density → high density" cells={[{title:'One comparison',body:'Two related panels.'},{title:'Repeated comparisons',body:'Aligned rows.'},{title:'One specification',body:'Labeled fields.'},{title:'Repeated specifications',body:'Structured table.'}]} /></section>
      <section className="specimen"><ComponentLabel kind="audit">04 / Audit table</ComponentLabel><AuditTable caption="Demonstration review record" columns={['Check','Status','Evidence']} rows={[{label:'Live text',values:['Required','Native HTML']},{label:'Source fidelity',values:['[UNKNOWN]','Match each lesson source']},{label:'Canva editability',values:['NOT TESTED','Destination inspection needed']}]} /></section>
      <section className="specimen"><ComponentLabel kind="artwork">05 / Separate artwork</ComponentLabel><ArtworkWithCaption src={art} alt="Three outlined layers" caption="Illustration and editable caption occupy separate elements." provenance="Lucide Layers icon; specimen only, not a substitute for story artwork." /></section>
      <section className="specimen"><ComponentLabel kind="reflection">06 / Reflection rail</ComponentLabel><p className="text-[22px] leading-relaxed">The footer pairs a focused question with writing space. It can be reused without baking text into an image.</p><p className="caption mt-6">Profile: 1920 × 1080 · white ground · black ink · 1px rules<br />Cyan #00BCEB / magenta #E30074 reserved for identity and selective emphasis.</p></section>
    </div>
  </SlideCanvas>;
}
