import React, { type ReactNode } from 'react';
import { Columns2, Layers, Grid2X2, Table2, Image as ImageIcon, MessageSquare } from 'lucide-react';

// SVG is confined to imported pictograms. Editorial copy remains native HTML.
export const icons = { comparison: Columns2, stack: Layers, matrix: Grid2X2, audit: Table2, artwork: ImageIcon, reflection: MessageSquare };
export function ComponentLabel({ kind, children }: { kind: keyof typeof icons; children: ReactNode }) {
  const Icon = icons[kind];
  return <h2 className="flex items-center gap-4"><Icon size={28} strokeWidth={1.5} aria-hidden="true" />{children}</h2>;
}
export function SlideCanvas({ title, children, footer, lang = 'en' }: { title: string; children: ReactNode; footer: ReactNode; lang?: string }) {
  return <article className="slide bg-paper text-ink" lang={lang} aria-label={title}>
    <h1>{title}</h1><div className="slide-content">{children}</div>{footer}
  </article>;
}
export function TopMetadataRail({ section, identifier, logo }: { section: string; identifier: string; logo?: { src: string; alt: string } }) {
  return <header className="rail"><span>{section}</span>{logo && <img src={logo.src} alt={logo.alt} width="180" height="48" />}<span>{identifier}</span></header>;
}
export type Panel = { title: string; body: string };
export function ComparisonPanel({ left, right }: { left: Panel; right: Panel }) {
  return <div className="comparison">{[left, right].map((panel, i) => <section key={i}><h3>{panel.title}</h3><p>{panel.body}</p></section>)}</div>;
}
export function LayerStack({ layers }: { layers: { id: string; label: string; description: string }[] }) {
  return <ol className="stack">{layers.map(layer => <li key={layer.id}><span className="font-mono">{layer.id}</span><strong>{layer.label}</strong><p>{layer.description}</p></li>)}</ol>;
}
export function DecisionMatrix({ horizontal, vertical, cells }: { horizontal: string; vertical: string; cells: [Panel, Panel, Panel, Panel] }) {
  return <div><p className="caption mb-4">Columns: {horizontal} · Rows: {vertical}</p><div className="matrix">{cells.map((cell, i) => <section key={i}><h3>{cell.title}</h3><p>{cell.body}</p></section>)}</div></div>;
}
export function AuditTable({ caption, columns, rows }: { caption: string; columns: string[]; rows: { label: string; values: string[] }[] }) {
  if (columns.length < 2 || rows.some(row => row.values.length !== columns.length - 1)) throw new Error('AuditTable: each row must match its columns');
  return <table className="audit"><caption className="caption text-left mb-4">{caption}</caption><thead><tr>{columns.map((column, i) => <th scope="col" key={i}>{column}</th>)}</tr></thead><tbody>{rows.map((row, i) => <tr key={i}><th scope="row">{row.label}</th>{row.values.map((value, j) => <td key={j}>{value}</td>)}</tr>)}</tbody></table>;
}
export function ArtworkWithCaption({ src, alt, caption, provenance }: { src: string; alt: string; caption: string; provenance: string }) {
  return <figure className="artwork"><img src={src} alt={alt} /><figcaption>{caption}<p className="caption mt-4">{provenance}</p></figcaption></figure>;
}
export function ReflectionFooter({ question, notesLabel = 'Notes' }: { question: string; notesLabel?: string }) {
  return <footer className="reflection"><strong className="flex items-center gap-4"><MessageSquare size={24} strokeWidth={1.5} aria-hidden="true" />Pause & consider</strong><p>{question}</p><p className="notes">{notesLabel}</p></footer>;
}
