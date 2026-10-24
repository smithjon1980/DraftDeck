import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {inspect} from '../tools/visual-gate/check_precomposition.mjs';

const sha=t=>createHash('sha256').update(t).digest('hex');
function fixture(){
 const dir=mkdtempSync(join(tmpdir(),'boss-precompose-'));
 const a='export function ArtLayer(){return <div className="absolute inset-0">Independent picture</div>;}';
 const s='export function StoryLayer(){return <div className="absolute inset-0">Observable change</div>;}';
 const artifact={
  art:{source_path:'art.tsx',source_sha256:sha(a),preview_path:'art.png',preview_sha256:sha('art-preview')},
  story:{source_path:'story.tsx',source_sha256:sha(s),preview_path:'story.png',preview_sha256:sha('story-preview')}
 };
 for(const [name,value] of Object.entries({'art.tsx':a,'story.tsx':s,'art.png':'art-preview','story.png':'story-preview'}))
  writeFileSync(join(dir,name),value);
 const manifest={contract:'BOSS-ART-STORY-PRECOMPOSE-V1',slide_id:'EP01_S05',candidate_id:'cand03-replacement',stage:'SEPARATE_LAYERS_ONLY',...artifact};
 const reviews={slide_id:manifest.slide_id,candidate_id:manifest.candidate_id};
 for(const role of ['art','story'])reviews[role]={
  decision:'APPROVE_'+role.toUpperCase(),reviewer_account:'human-owner',
  review_reference:'https://github.com/example-owner/example-repo/issues/123',
  candidate_id:manifest.candidate_id,slide_id:manifest.slide_id,
  source_sha256:artifact[role].source_sha256,preview_sha256:artifact[role].preview_sha256
 };
 return {dir,manifest,reviews,cleanup:()=>rmSync(dir,{recursive:true,force:true})};
}
function check(name,mutate,expectReason){
 test(name,()=>{
  const f=fixture();try{
   mutate?.(f);
   const outcome=inspect(f.dir,f.manifest,f.reviews);
   if(expectReason) {
    assert.equal(outcome.status,'HOLD');
    assert.match(outcome.failures.join('; '),expectReason);
   }else {
    assert.equal(outcome.status,'SOURCE_AND_RECEIPT_STRUCTURE_PASS');
    assert.equal(outcome.compiled_slide_permitted,false);
    assert.equal(outcome.external_reviewer_identity_verified,false);
   }
  }finally{f.cleanup()}
 });
}
check('matching independent receipts: only structural pass, not compile permission');
check('missing art authorization fails',(f)=>delete f.reviews.art,/art human decision missing/);
check('missing story authorization fails',(f)=>delete f.reviews.story,/story human decision missing/);
check('art is rejected',(f)=>f.reviews.art.decision='REJECT',/art not explicitly approved/);
check('story is rejected',(f)=>f.reviews.story.decision='REJECT',/story not explicitly approved/);
check('art source tampered',(f)=>writeFileSync(join(f.dir,'art.tsx'),'export function ArtLayer() {}'),/art source bytes modified/);
check('story source tampered',(f)=>writeFileSync(join(f.dir,'story.tsx'),'export function StoryLayer() {}'),/story source bytes modified/);
check('art preview tampered',(f)=>writeFileSync(join(f.dir,'art.png'),'other'),/art preview bytes modified/);
check('approval for wrong slide',(f)=>f.reviews.story.slide_id='EP01_S06',/story decision slide differs/);
check('approval for wrong candidate',(f)=>f.reviews.art.candidate_id='old-candidate',/art decision candidate differs/);
check('approval for wrong source digest',(f)=>f.reviews.story.source_sha256=sha('wrong'),/story source hash not selected/);
check('same art story source rejected',(f)=>f.manifest.story.source_path='art.tsx',/art and story must be separate/);
check('same art story preview rejected',(f)=>f.manifest.story.preview_path='art.png',/separately reviewable previews/);
check('Python art source not accepted',(f)=>f.manifest.art.source_path='art.py',/native React TSX/);
check('compiled output cannot claim precomposition authority',(f)=>f.manifest.composite_path='slide05.html',/must not assert a compiled slide/);
check('embedded SVG editorial text not permitted',(f)=>{
  const c='<svg><text>Fake narration</text></svg> function ArtLayer() {return <div className="flex"></div>}';
  writeFileSync(join(f.dir,'art.tsx'),c); f.manifest.art.source_sha256=sha(c);f.reviews.art.source_sha256=sha(c)
},/forbidden flattened/);
check('private source root escape rejected',(f)=>f.manifest.art.source_path='../secret.tsx',/non-relative path|outside approved root|path/);
