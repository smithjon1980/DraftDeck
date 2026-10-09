import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { slides, brand } from './content';
import { SlideCanvas, TopMetadataRail, SplitPanelLayout, SequenceDiagram } from './components';
import './styles.css';

function Footer({ text }) {
  return <footer className="slide-footer border-t border-black"><p>{text}</p></footer>;
}

function TitleSlide({ slide }) {
  return <>
    <div className="title-logo"><img src={brand.logoSrc} alt={brand.logoAlt} /></div>
    <div className="title-frame border border-black"><h1>{slide.headline}</h1></div>
  </>;
}

function Comparison({ slide }) {
  return <SplitPanelLayout
    main={<div className="comparison-grid">{slide.comparison_columns.map((column, index) => (
      <section className="comparison-column" key={column.header}>
        <h2 className="border-b border-black" data-secondary={index === 0}>{column.header}</h2>
        <ol>{column.items.slice(0, 3).map((step, i) => (
          <li className="border-b border-black" key={step}>
            <span className="step-index" aria-hidden="true">{String(i + 1).padStart(2, '0')}</span><p>{step}</p>
          </li>
        ))}</ol>
        <p className="comparison-outcome">{column.items[3]}</p>
      </section>
    ))}</div>}
    sidebar={<><h2 className="small-label">{slide.sidebar_title}</h2><p>{slide.sidebar_body}</p></>}
  />;
}

function Slide({ slide }) {
  const title = slide.slide === '01';
  return <SlideCanvas slideId={slide.slide}>
    {title ? <TitleSlide slide={slide} /> : <>
      <TopMetadataRail metadata="[UNKNOWN]" brand={brand} />
      <div className="slide-heading border-b border-black"><h1>{slide.headline}</h1></div>
      {slide.slide === '02' ? <Comparison slide={slide} /> : <div className="sequence-panel">
        <SequenceDiagram steps={slide.sequence_labels.map(label => ({ id: label, label }))} />
      </div>}
      <Footer text={slide.footer} />
    </>}
  </SlideCanvas>;
}

function App() {
  const [selected, setSelected] = useState('all');
  return <main className="preview-shell">
    <div className="preview-controls border-b border-black">
      <div><h1>BOSS · Episode 01</h1><p>Composition candidate · Visual Authority Spec v1.0 · approval pending</p></div>
      <div className="preview-selector"><label htmlFor="slide-selector">View</label>
        <select id="slide-selector" value={selected} onChange={event => setSelected(event.target.value)}>
          <option value="all">All three slides</option>
          {slides.map(slide => <option key={slide.slide} value={slide.slide}>Slide {slide.slide}</option>)}
        </select>
      </div>
    </div>
    <p className="preview-notice">Candidate composition from the supplied textual specification. Original recovered logo unchanged; full lockup scaled in internal rails. Proposed Arial typography and geometry. No approved rendered reference supplied.</p>
    <p className="preview-notice unresolved-notice">Unresolved: internal metadata and reduced lockup; Slide 01 footer; Slide 06 participants, messages, arrows, and gates. No additional illustration was supplied.</p>
    <div className="slide-list">{slides.filter(slide => selected === 'all' || selected === slide.slide).map(slide => (
      <article key={slide.slide} className="preview-entry"><p className="entry-label">Slide {slide.slide} · {slide.type} · CANDIDATE</p><Slide slide={slide} /></article>
    ))}</div>
  </main>;
}

createRoot(document.getElementById('root')).render(<App />);
