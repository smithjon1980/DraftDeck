import { useState } from 'react';
import { SlideCanvas } from './components';
import { slides, brand } from './content';
import artwork from '../../../episode01/assets/story/slide02-two-operating-outcomes.candidate.webp';

const copy = slides.find(slide => slide.slide === '02');
const [network, capability] = copy.comparison_columns;
export const directions = {
  A: { name: 'Parallel operating circuits', difference: 'Two equal illustrated systems; the operational distinction occupies a separate right panel.' },
  B: { name: 'Capability engine', difference: 'A large delivered-work illustration leads; recruitment and the distinction share a compact supporting panel.' },
  C: { name: 'Two outputs, one comparison', difference: 'Both topologies occupy one panoramic field; actions and outcomes form a horizontal instrument strip.' },
  D: { name: 'Operator diagnosis', difference: 'The comparison is read as two telemetry panels around a central illustrated operating field; the explanation spans the base.' },
};

function Artwork({ scene = 'pair', className = '' }) {
  const single = scene !== 'pair';
  return <figure className={`story-art relative overflow-hidden ${className}`} data-story-scene={scene}>
    <img src={artwork} alt={scene === 'network' ? 'Candidate illustration: professional relationships circulate around an expanding network.' : scene === 'capability' ? 'Candidate illustration: connected practitioners coordinate tools and a delivered engineering artifact.' : 'Candidate illustration: an expanding relationship loop beside practitioners coordinating a delivered engineering artifact.'}
      className={single ? 'absolute top-0 h-full max-w-none w-[200%]' : 'block h-full w-full object-contain'}
      style={single ? { left: scene === 'capability' ? '-100%' : '0' } : undefined} />
  </figure>;
}

function ColumnHeading({ column, large = false }) {
  return <h2 data-secondary={column === network} className={`${large ? 'text-[42px]' : 'text-[30px]'} leading-[1.16] font-semibold tracking-[-0.025em] ${column === network ? 'text-[#646464]' : 'text-black'}`}>{column.header}</h2>;
}

function Actions({ column, className = '', horizontal = false }) {
  return <ol className={`${horizontal ? 'flex items-baseline gap-[32px]' : 'flex flex-col gap-[20px]'} list-none p-0 ${className}`}>
    {column.items.slice(0, 3).map(text => <li key={text}><p className="leading-[1.18]">{text}</p></li>)}
  </ol>;
}

function Outcome({ column, className = '' }) {
  return <p className={`text-[26px] leading-[1.25] font-semibold tracking-[-0.012em] ${className}`}>{column.items[3]}</p>;
}

function Distinction({ className = '', compact = false }) {
  return <aside className={className}>
    <h2 className="font-mono text-[18px] leading-[1.3] font-bold tracking-[0.045em]">{copy.sidebar_title}</h2>
    <p className={`${compact ? 'text-[22px] leading-[1.42]' : 'text-[25px] leading-[1.45]'} mt-[26px]`}>{copy.sidebar_body}</p>
  </aside>;
}

function Masthead() {
  return <header className="flex h-[144px] items-center justify-between gap-[56px] border-b border-black px-[64px]">
    <h1 className="text-[52px] leading-[1.12] font-semibold tracking-[-0.025em]">{copy.headline}</h1>
    <img data-brand-logo src={brand.logoSrc} alt={brand.logoAlt} className="block h-auto w-[248px] shrink-0" />
  </header>;
}

function CandidateA() {
  return <div className="grid h-[846px] grid-cols-[1fr_1fr_420px] gap-[48px] px-[64px] py-[40px]">
    {[network, capability].map((column, index) => <section key={column.header} className="flex min-w-0 flex-col">
      <ColumnHeading column={column} />
      <Artwork scene={index ? 'capability' : 'network'} className="mt-[24px] h-[360px] w-[360px] self-center" />
      <Actions column={column} className="mt-[28px] text-[32px] font-medium" />
      <Outcome column={column} className="mt-auto border-t border-black pt-[24px]" />
    </section>)}
    <Distinction className="border-l border-black pl-[36px] pt-[4px]" />
  </div>;
}

function CandidateB() {
  return <div className="grid h-[846px] grid-cols-[minmax(0,1fr)_490px] gap-[48px] px-[64px] py-[40px]">
    <section className="flex min-w-0 flex-col">
      <ColumnHeading column={capability} large />
      <div className="grid flex-1 grid-cols-[580px_minmax(0,1fr)] items-center gap-[36px]">
        <Artwork scene="capability" className="h-[580px] w-[580px]" />
        <Actions column={capability} className="text-[42px] font-semibold" />
      </div>
      <Outcome column={capability} className="border-t border-black pt-[24px]" />
    </section>
    <div className="border-l border-black pl-[40px]">
      <ColumnHeading column={network} />
      <Actions column={network} className="mt-[30px] text-[28px]" />
      <Outcome column={network} className="mt-[30px] text-[24px]" />
      <Distinction compact className="mt-[36px] border-t border-black pt-[32px]" />
    </div>
  </div>;
}

function CandidateC() {
  return <div className="grid h-[846px] grid-cols-[minmax(0,1fr)_450px] gap-[48px] px-[64px] py-[40px]">
    <section className="flex min-w-0 flex-col">
      <div className="grid grid-cols-2 gap-[48px]">
        <ColumnHeading column={network} /><ColumnHeading column={capability} />
      </div>
      <Artwork className="my-[24px] h-[470px]" />
      <div className="grid flex-1 grid-cols-2 gap-[48px] border-t border-black pt-[28px]">
        {[network, capability].map(column => <div key={column.header} className="flex flex-col">
          <Actions column={column} className="text-[27px] font-medium" horizontal />
          <Outcome column={column} className="mt-auto" />
        </div>)}
      </div>
    </section>
    <Distinction className="border-l border-black pl-[36px] pt-[4px]" />
  </div>;
}

function CandidateD() {
  return <div className="h-[846px] px-[64px] py-[40px]">
    <div className="grid h-[516px] grid-cols-[350px_minmax(0,1fr)_350px] gap-[32px]">
      <section className="flex flex-col border-r border-black pr-[32px]">
        <ColumnHeading column={network} />
        <Actions column={network} className="mt-[54px] text-[30px]" />
        <Outcome column={network} className="mt-auto" />
      </section>
      <Artwork className="h-[490px] self-center" />
      <section className="flex flex-col border-l border-black pl-[32px]">
        <ColumnHeading column={capability} />
        <Actions column={capability} className="mt-[54px] text-[36px] font-semibold" />
        <Outcome column={capability} className="mt-auto" />
      </section>
    </div>
    <div className="mt-[36px] grid grid-cols-[350px_minmax(0,1fr)] gap-[32px] border-t border-black pt-[30px]">
      <h2 className="font-mono text-[18px] leading-[1.3] font-bold tracking-[0.045em]">{copy.sidebar_title}</h2>
      <p className="max-w-[1290px] text-[25px] leading-[1.45]">{copy.sidebar_body}</p>
    </div>
  </div>;
}

const compositions = { A: CandidateA, B: CandidateB, C: CandidateC, D: CandidateD };

export function Slide02Candidate({ id }) {
  const Composition = compositions[id];
  return <SlideCanvas slideId="02" candidateId={id}>
    <Masthead /><Composition />
    <footer className="mx-[64px] flex h-[88px] items-center border-t border-black"><p className="font-mono text-[17px] tracking-[0.035em]">{copy.footer}</p></footer>
  </SlideCanvas>;
}

export function Slide02Review() {
  const [selected, setSelected] = useState('all');
  return <main className="preview-shell">
    <div className="preview-controls border-b border-black">
      <div><h1>BOSS · Episode 01 · Slide 02</h1><p>Four composition candidates · source designation and visual approval unconfirmed</p></div>
      <div className="preview-selector"><label htmlFor="candidate-selector">Candidate</label>
        <select id="candidate-selector" value={selected} onChange={event => setSelected(event.target.value)}>
          <option value="all">All four</option>{Object.keys(directions).map(id => <option key={id} value={id}>{id} · {directions[id].name}</option>)}
        </select>
      </div>
    </div>
    <p className="preview-notice">Proposed source: BOSS_System_Diagnostics.pdf, pages 2–3. Earlier-deck provenance retained. Story artwork is newly generated candidate art; copy and original logo are unchanged.</p>
    <p className="preview-notice unresolved-notice">Jonathan Smith retains selection and visual approval. Internal metadata, reduced logo variant, Canva editability, and final source designation remain unconfirmed.</p>
    <div className="slide-list">{Object.entries(directions).filter(([id]) => selected === 'all' || selected === id).map(([id, direction]) => <article key={id} className="preview-entry">
      <p className="entry-label">Candidate {id} · {direction.name} — {direction.difference}</p><Slide02Candidate id={id} />
    </article>)}</div>
  </main>;
}
