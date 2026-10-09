import { useLayoutEffect, useRef, useState } from 'react';

export function SlideCanvas({ children, slideId, candidateId }) {
  const viewportRef = useRef(null);
  const [scale, setScale] = useState(1);
  useLayoutEffect(() => {
    const viewport = viewportRef.current;
    const update = () => setScale(Math.min(viewport.clientWidth / 1920, 1));
    const observer = new ResizeObserver(update);
    observer.observe(viewport);
    update();
    return () => observer.disconnect();
  }, []);
  return (
    <div ref={viewportRef} className="slide-viewport" style={{ height: 1080 * scale }}>
      <section
        className="slide-canvas bg-white text-black"
        data-document-role="page"
        data-slide-id={slideId}
        data-candidate-id={candidateId}
        aria-label={`Slide ${slideId}`}
        style={{ transform: `scale(${scale})` }}
      >{children}</section>
    </div>
  );
}

export function TopMetadataRail({ metadata, brand }) {
  return (
    <header className="metadata-rail border-b border-black">
      <div className="brand-slot">
        {brand.logoSrc
          ? <img src={brand.logoSrc} alt={brand.logoAlt} className="canonical-logo" />
          : <span aria-label="Canonical logo unavailable">[UNKNOWN]</span>}
      </div>
      <p className="metadata-value">{metadata}</p>
    </header>
  );
}

export function SplitPanelLayout({ main, sidebar }) {
  return (
    <div className="split-panel-layout">
      <div className="main-panel">{main}</div>
      <aside className="sidebar border-l border-black">{sidebar}</aside>
    </div>
  );
}

// Exact supplied labels only. Direction and messages remain unknown.
export function SequenceDiagram({ steps = [] }) {
  if (!steps.length) return <p>[UNKNOWN]</p>;
  return <ol className="sequence-diagram" aria-label="Operating sequence">
    {steps.map(step => <li className="sequence-node border border-black" key={step.id}>
      <h2>{step.label}</h2>
    </li>)}
  </ol>;
}
