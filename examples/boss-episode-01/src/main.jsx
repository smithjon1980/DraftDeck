import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { slides, brand } from './content';
import { SlideCanvas, TopMetadataRail, SplitPanelLayout } from './components';
import './styles.css';

function Comparison({ slide }) {
  return (
    <SplitPanelLayout
      main={<div className="comparison-grid">
        {slide.comparison.map(column => (
          <section className="comparison-column" key={column.heading}>
            <h2 className="border-b border-black">{column.heading}</h2>
            <ol>{column.steps.map((step, index) => (
              <li className="border-b border-black" key={step}>
                <span className="step-index" aria-hidden="true">{String(index + 1).padStart(2, '0')}</span>
                <p>{step}</p>
              </li>
            ))}</ol>
            <p className="comparison-outcome">{column.outcome}</p>
          </section>
        ))}
      </div>}
      sidebar={<>
        <h2 className="small-label">{slide.sidebarHeading}</h2>
        {slide.sidebar.map(paragraph => <p key={paragraph}>{paragraph}</p>)}
      </>}
    />
  );
}

function Slide({ slide }) {
  return (
    <SlideCanvas slideId={slide.id}>
      <TopMetadataRail metadata={slide.metadata} brand={brand} />
      <div className="slide-heading border-b border-black"><h1>{slide.title}</h1></div>
      {slide.layout === 'diagnostic-comparison'
        ? <Comparison slide={slide} />
        : <div className="unresolved-layout"><p>[UNKNOWN]</p></div>}
    </SlideCanvas>
  );
}

function App() {
  const [selected, setSelected] = useState('all');
  return (
    <main className="preview-shell">
      <div className="preview-controls border-b border-black">
        <div><h1>BOSS · Episode 01</h1><p>Candidate geometry · creative approval pending</p></div>
        <div className="preview-selector">
          <label htmlFor="slide-selector">View</label>
          <select id="slide-selector" value={selected} onChange={event => setSelected(event.target.value)}>
            <option value="all">All three slides</option>
            {slides.map(slide => <option key={slide.id} value={slide.id}>Slide {slide.id}</option>)}
          </select>
        </div>
      </div>
      <p className="preview-notice">
        Slides 01 and 06: content unresolved. Slide 02: recovered diagnostic wording, approval unknown.
        Canonical logo and production footer unavailable. Layout measurements and Arial typography are proposals.
      </p>
      <div className="slide-list">
        {slides.filter(slide => selected === 'all' || selected === slide.id).map(slide => (
          <article key={slide.id} className="preview-entry">
            <p className="entry-label">Slide {slide.id} · {slide.layout === 'unresolved' ? 'Unresolved content' : 'Diagnostic copy / candidate layout'}</p>
            <Slide slide={slide} />
          </article>
        ))}
      </div>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
