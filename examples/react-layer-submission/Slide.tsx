import React from "react";
export function ArtLayer(){return <div className="absolute inset-0" aria-label="Technical isometric art"><svg viewBox="0 0 400 160"><path d="M10 90L110 40L210 90L110 140Z" fill="none" stroke="currentColor"/></svg></div>}
export function StoryLayer(){return <div className="relative grid grid-cols-3 gap-6"><span>INPUT</span><span>PROCESS</span><span>INSPECT</span></div>}
export function TextLayer(){return <div className="relative flex flex-col"><h1>Editable candidate title</h1><p>Native HTML instructional text</p></div>}
export default function Slide(){return <main className="relative w-full h-full"><ArtLayer/><StoryLayer/><TextLayer/></main>}
