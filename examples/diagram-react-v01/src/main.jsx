import React from "react";
import { createRoot } from "react-dom/client";

const PROOFS = [
  {
    id: "EP01-038",
    index: "01",
    type: "MERMAID / GOVERNED FLOW",
    title: "When the request is incomplete,",
    titleAccent: "production stops.",
    subtitle: "A missing copy count is not a production instruction.",
    narrative: [
      "At Main Street Copy, the work begins with a customer's request. A clean procedure must distinguish the information actually provided from what is still unknown.",
      "If the copy count or another required field is missing, the work order is placed on HOLD. The counter operator requests clarification and then rechecks the complete request.",
      "Only a validated request can proceed to an authorized production step. Completion requires inspection and a recorded handoff, not merely a confident statement."
    ],
    principle: "Missing information must remain visible until it is resolved.",
    diagramPath: "./diagrams/intake.svg",
    diagramLabel: "Rendered Mermaid flowchart of Main Street Copy intake and HOLD branches",
    diagramTitle: "MSC-01 // ORDER INTAKE AND HOLD",
    method: "Mermaid 11.x engine family",
    cue: "FLOWCHART",
    reflection: "Which condition prevents the job from advancing to production?",
    caption: "Companion proof: engine-generated diagram geometry and labels, with independently selectable HTML editorial content."
  },
  {
    id: "EP01-039",
    index: "02",
    type: "PLANTUML / UML SEQUENCE",
    title: "A request is a sequence",
    titleAccent: "of accountable exchanges.",
    subtitle: "Different participants, different responsibilities, one verifiable outcome.",
    narrative: [
      "A customer may provide all required quantities, or the request may remain incomplete. Those paths must not be silently treated as equivalent.",
      "The counter operator checks the work order. A missing field returns a HOLD result, and clarification is requested from the customer before the same request is validated again.",
      "The resulting sequence explains the handoff boundary: production is authorized only after the required data has been checked. The diagram is a teaching candidate, not evidence that a real shop system executed."
    ],
    principle: "An acknowledgement is not proof that production was authorized.",
    diagramPath: "./diagrams/clarification.svg",
    diagramLabel: "Rendered PlantUML sequence diagram showing customer, counter operator, work order, and production interactions",
    diagramTitle: "MSC-02 // ACTORS AND HANDOFFS",
    method: "PlantUML 1.2025.10",
    cue: "UML SEQUENCE",
    reflection: "Who is responsible for obtaining and validating the missing information?",
    caption: "Sequence semantics remain candidates for human review; successful UML rendering verifies syntax, not the business process."
  }
];

function Grid() {
  return <div aria-hidden="true" className="pointer-events-none absolute inset-[34px] opacity-[0.14]">
    {Array.from({length: 13}, (_,i)=><div key={"v"+i} className="absolute top-0 bottom-0 border-l border-slate-400" style={{left: `${i*100/12}%`}} />)}
    {Array.from({length: 8}, (_,i)=><div key={"h"+i} className="absolute left-0 right-0 border-t border-slate-400" style={{top: `${i*100/7}%`}} />)}
  </div>;
}

function Meta({slide}) {
  return <div className="flex justify-between items-start border-b border-boss-ink pb-3 relative z-10">
    <div className="flex gap-7 items-center">
      <span className="font-black text-[27px] tracking-[-0.045em]">BOSS</span>
      <span className="border-l border-boss-ink pl-6 font-label text-[20px] tracking-widest">EPISODE 01 / TECHNICAL EXPLAINER</span>
    </div>
    <div className="font-label text-right text-[17px] tracking-[0.10em]">
      <p>{slide.id} / CANDIDATE</p>
      <p>1920 × 1080 / NTS</p>
    </div>
  </div>;
}

function SourceStatus() {
  return <div className="border border-boss-magenta bg-white px-4 py-2 font-label text-[15px] font-bold uppercase tracking-[0.03em] text-boss-magenta">
    BRAND MASTER: REVIEW HOLD · NO LOGO RECREATION
  </div>;
}

function Slide({slide}) {
  return <main id="slide" data-slide-id={slide.id} data-render-master="react-tailwind" className="relative h-[1080px] w-[1920px] overflow-hidden bg-boss-white text-boss-ink font-display">
    <Grid />
    <div className="relative z-10 flex h-full flex-col px-[65px] pt-[37px] pb-[32px]">
      <Meta slide={slide} />
      <div className="mt-7 mb-5 flex items-center justify-between">
        <div className="font-label text-[21px] font-bold text-boss-magenta tracking-widest">MSC / MAIN STREET COPY • {slide.type}</div>
        <SourceStatus />
      </div>
      <header className="border-b border-slate-300 pb-[18px]">
        <h1 className="text-[72px] leading-[1.04] tracking-[-0.068em] font-black">
          {slide.title} <span className="text-boss-magenta">{slide.titleAccent}</span>
        </h1>
        <p className="text-[31px] mt-[13px] tracking-[-0.015em]">{slide.subtitle}</p>
      </header>
      <section className="grid grid-cols-[640px_1fr] gap-10 pt-[30px] flex-1 min-h-0">
        <article className="border-l-[6px] border-boss-cyan pl-[27px] pr-[16px] flex flex-col justify-between">
          <div className="space-y-[24px]">
            {slide.narrative.map((paragraph,i)=><p key={i} className="text-[26px] leading-[1.34] tracking-[-0.014em]">{paragraph}</p>)}
          </div>
          <div className="border-l-[5px] border-boss-magenta pl-5 mb-3">
            <p className="font-black text-[30px] leading-[1.09] tracking-[-0.02em]">{slide.principle}</p>
          </div>
        </article>
        <section aria-labelledby="diagram-title" className="flex flex-col min-h-0">
          <div className="flex justify-between items-center border-t-[2px] border-boss-cyan pt-3">
            <h2 id="diagram-title" className="font-label font-bold text-[21px] tracking-[0.03em]">{slide.diagramTitle}</h2>
            <span className="font-label text-[16px] text-slate-600">{slide.method}</span>
          </div>
          <div className="relative min-h-0 flex-1 flex justify-center items-center py-[15px]">
            <img className="max-w-full max-h-full w-full h-full object-contain" src={slide.diagramPath} alt={slide.diagramLabel} />
          </div>
          <div className="border-t border-slate-400 pt-2 font-label text-[16px]">{slide.caption}</div>
        </section>
      </section>
      <footer className="mt-[25px] flex items-start gap-7 border-t-2 border-boss-ink pt-4">
        <div className="flex items-center justify-center border-2 border-boss-magenta rounded-full w-[68px] h-[68px] text-[42px] font-black text-boss-magenta">?</div>
        <div className="flex-1 pt-1">
          <div className="flex gap-6 items-baseline">
            <span className="font-bold tracking-[0.02em] text-[22px] text-boss-magenta">REFLECT</span>
            <p className="text-[23px]">{slide.reflection}</p>
          </div>
          <div className="border-b border-slate-500 mt-5"></div>
        </div>
        <div className="w-[215px] border border-boss-ink px-3 py-2 font-label text-[14px] tracking-[0.045em]">
          <p>{slide.id} / REV A</p>
          <p className="mt-1">NOT RELEASED / NTS</p>
        </div>
      </footer>
    </div>
  </main>;
}
const requested = new URLSearchParams(window.location.search).get("slide") || "1";
const slideNumber = Math.min(2,Math.max(1,Number.parseInt(requested,10)||1));
createRoot(document.getElementById("root")).render(<Slide slide={PROOFS[slideNumber-1]}/>);
