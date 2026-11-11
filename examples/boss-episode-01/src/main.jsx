import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { slides, brand } from './content';
import { SlideCanvas, TopMetadataRail, SequenceDiagram } from './components';
import './styles.css';
import { Slide02Review } from './Slide02Candidates';

function Footer({ text }) {
  return <footer className="slide-footer border-t border-black"><p>{text}</p></footer>;
}

function TitleSlide({ slide }) {
  return <>
    <div className="title-logo"><img src={brand.logoSrc} alt={brand.logoAlt} /></div>
    <div className="title-frame border border-black"><h1><span className="block">{slide.headline.split(". ")[0]}.</span>{" "}<span className="block">{slide.headline.split(". ")[1]}</span></h1></div>
  </>;
}

function Comparison({ slide }) {
  return <div className="grid h-[790px] grid-cols-[minmax(0,1fr)_440px] gap-[64px] px-[64px] pt-[44px] pb-[56px]">
    <div className="grid grid-cols-[0.85fr_1.15fr] gap-[56px]">
      {slide.comparison_columns.map((column, index) => (
        <section key={column.header} className={index === 0 ? 'flex min-w-0 flex-col' : 'flex min-w-0 flex-col border-l border-black pl-[56px]'}>
          <h2 data-secondary={index === 0} className={index === 0 ? 'text-[28px] leading-[1.2] font-medium text-[#646464]' : 'text-[34px] leading-[1.2] font-bold'}>{column.header}</h2>
          <ol className="mt-[64px] flex h-[320px] list-none flex-col justify-between p-0">
            {column.items.slice(0, 3).map(step => <li key={step}><p className={index === 0 ? 'text-[32px] leading-[1.3] font-normal' : 'text-[44px] leading-[1.2] font-semibold tracking-[-0.02em]'}>{step}</p></li>)}
          </ol>
          <p className="mt-auto border-t border-black pt-[28px] text-[25px] leading-[1.35] font-semibold">{column.items[3]}</p>
        </section>
      ))}
    </div>
    <aside className="border-l border-black pl-[40px]">
      <h2 className="font-mono text-[18px] leading-[1.4] font-bold tracking-[0.025em]">{slide.sidebar_title}</h2>
      <p className="mt-[32px] text-[25px] leading-[1.55]">{slide.sidebar_body}</p>
    </aside>
  </div>;
}

function ComparisonSlide({ slide }) {
  return <>
    <header className="flex h-[200px] items-center justify-between gap-[64px] px-[64px]">
      <h1 className="max-w-[1180px] text-[54px] leading-[1.12] font-semibold tracking-[-0.025em]">{slide.headline}</h1>
      <div className="relative flex h-full w-[300px] shrink-0 items-center">
        <img className="block h-auto w-full" src={brand.logoSrc} alt={brand.logoAlt} />
        <p className="absolute right-0 bottom-[4px] font-mono text-[14px]">[UNKNOWN]</p>
      </div>
    </header>
    <Comparison slide={slide} />
    <footer className="mx-[64px] flex h-[88px] items-center border-t border-black"><p className="font-mono text-[17px] tracking-[0.035em]">{slide.footer}</p></footer>
  </>;
}

function Slide({ slide }) {
  const title = slide.slide === '01';
  return <SlideCanvas slideId={slide.slide}>
    {title ? <TitleSlide slide={slide} /> : slide.slide === '02' ? <ComparisonSlide slide={slide} /> : <>
      <TopMetadataRail metadata="[UNKNOWN]" brand={brand} />
      <div className="slide-heading border-b border-black"><h1>{slide.headline}</h1></div>
      {<div className="sequence-panel">
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

createRoot(document.getElementById('root')).render(new URLSearchParams(location.search).get('review') === 'slide02' ? <Slide02Review /> : <App />);
