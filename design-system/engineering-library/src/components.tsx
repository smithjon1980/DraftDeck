import React from 'react';

export type EngineeringAsset = {
  id: string; name: string; family: string; reference: string;
  source: string; license: string; svg: string;
  ports?: { x: string; y: string; orientation: string }[];
  attribution?: string; sourceUrl?: string; licenseUrl?: string;
  assetUrl?: string;
};
// Source geometry stays isolated as an image. Every editorial label is live HTML.
export function TechnicalSymbol({asset, width=200, height=140}: {asset: EngineeringAsset; width?: number; height?: number}) {
  return <img src={asset.assetUrl ?? 'data:image/svg+xml;base64,'+Buffer.from(asset.svg).toString('base64')} alt={asset.name} width={width} height={height} style={{objectFit:'contain'}} />;
}
export function LeaderCallout({number, label, detail, x, y, points}: {number: string; label: string; detail: string; x: number; y: number; points: string}) {
  return <><svg className="geometry" viewBox="0 0 1600 760" aria-hidden="true"><polyline points={points} fill="none" stroke="black" strokeWidth="1.5" /><circle cx={x} cy={y} r="4" fill="black" /></svg><div className="leader-label" style={{left:x+16,top:y+12}}><b>{number} / {label}</b><p>{detail}</p></div></>;
}
export function DimensionLine({x1,x2,y,label}: {x1:number;x2:number;y:number;label:string}) {
  return <><svg className="geometry" viewBox="0 0 1600 760" aria-hidden="true"><path d={`M${x1} ${y-24}v48 M${x2} ${y-24}v48 M${x1} ${y}H${x2}`} fill="none" stroke="black" /><path d={`M${x1} ${y}l12 -4v8z M${x2} ${y}l-12 -4v8z`} fill="black" /></svg><span className="dimension-label" style={{left:(x1+x2)/2,top:y-14}}>{label}</span></>;
}
export function EngineeringAtlas({assets, shellOnly=false}: {assets:EngineeringAsset[]; shellOnly?:boolean}) {
  return <main>
    <header className="masthead"><p className="font-mono text-sm">DraftDeck / Engineering graphics library / Candidate 0.2</p><h1>Technical symbol atlas</h1><p>ISO-referenced process equipment · ANSI/IEEE logic · mechanical drafting</p></header>
    <section className="intro"><strong>{assets.length} reusable assets</strong><p>Original geometry, identifiable references, separate live labels. Select a component to inspect its source and licensing.</p><a href="#library-notes">Source and reuse notes ↓</a></section>
    <nav className="filters" aria-label="Filter engineering assets"><label>Find a component <input id="query" type="search" placeholder="heat exchanger, pump, datum, AND…" /></label><label>Collection <select id="family"><option value="">All collections</option>{[...new Set(assets.map(a=>a.family))].map(f=><option key={f}>{f}</option>)}</select></label><output id="count">{assets.length} assets</output></nav>
    <section className="atlas" aria-label="Engineering components">{!shellOnly && assets.map(a=><button key={a.id} className="asset" data-id={a.id} data-search={`${a.name} ${a.reference} ${a.id}`.toLowerCase()} data-family={a.family} aria-label={`Inspect ${a.name}`}><span className="asset-ref">{a.family} / {a.reference}</span><TechnicalSymbol asset={a}/><span className="asset-name">{a.name}</span></button>)}</section>
    <dialog id="inspector"><form method="dialog"><button>Close</button></form><h2 id="detail-name"/><img id="detail-image" alt=""/><dl id="detail-meta"/><a id="detail-download">Download this SVG</a></dialog>
    <footer id="library-notes">Asset licensing and provenance are available in each record. Engineering semantics must match the lesson. This collection is not a certified ISO/ANSI implementation, and schematic symbols do not replace detailed mechanical illustrations.</footer>
  </main>;
}
