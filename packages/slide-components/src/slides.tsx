import React from 'react';
import {design_tokens,assertExactTitle,requireContract} from '@draftdeck/standards';

/** These props are semantic only. Do not spread unknown props into the DOM. */
export type BossTitleProps = {content:string};
export function BossTitle({content}:BossTitleProps) {
  assertExactTitle(content);
  const token = design_tokens.typography.scale.title_h1;
  return <h1 data-element-id="EP01.S01.TEXT.TITLE" style={{fontFamily:design_tokens.typography.font_family_primary,fontSize:token.size_px,fontWeight:token.weight,lineHeight:token.line_height,color:design_tokens.colors.text_primary,margin:0,overflowWrap:'break-word'}}>{content}</h1>;
}
export type StoryRegionProps = {sourceAsset:string; description:string};
export function StoryRegion({sourceAsset,description}:StoryRegionProps) {
  requireContract('EP01.S01.STORY.WORKSTATION');
  if (!sourceAsset.startsWith('/approved-assets/')) throw new Error('STORY source must be an approved local asset');
  return <div className="dd-story" data-element-id="EP01.S01.STORY.WORKSTATION"><img src={sourceAsset} alt={description} /></div>;
}
export type BossCanvasProps = {children:React.ReactNode};
export function BossCanvas({children}:BossCanvasProps){
  requireContract('EP01.S01.ART.CANVAS');
  return <section className="dd-canvas" data-element-id="EP01.S01.ART.CANVAS" data-document-role="page"><div className="dd-rail dd-rail-top"/><div className="dd-rail dd-rail-bottom"/>{children}</section>;
}
export function Episode01Slide({sourceAsset}:{sourceAsset:string}) {
  return <BossCanvas><div className="dd-layout"><div className="dd-text"><div className="dd-eyebrow">DAY ZERO · EPISODE 01</div><BossTitle content="YOU ALREADY MOVE INFORMATION"/><p>What makes an ordinary information transfer accountable?</p></div><StoryRegion sourceAsset={sourceAsset} description="Original NotebookLM technical workstation, linked to a document, person, cloud, and network"/></div><div className="dd-footer">BIOSCILLATE · OPERATING SYSTEM BY SEVEN <span>01 / 12</span></div></BossCanvas>;
}
