#!/usr/bin/env node
/**
 * Structural pre-composition custody gate for native React art and story layers.
 * This DOES NOT verify that a reviewer is human or grant compilation authority.
 * Authentic human decisions must be checked outside the untrusted source tree.
 */
import {readFileSync,realpathSync,existsSync} from 'node:fs';
import {resolve,relative,sep} from 'node:path';
import {createHash} from 'node:crypto';

const digest = b => createHash('sha256').update(b).digest('hex');
const isHash = x => typeof x === 'string' && /^[0-9a-f]{64}$/.test(x);
const local = (root,path) => {
  if(typeof path !== 'string' || !path || path.startsWith('/') || path.includes('\\')) throw Error('non-relative path');
  const rootReal=realpathSync(root),target=realpathSync(resolve(root,path));
  const rel=relative(rootReal,target);
  if(rel==='..'||rel.startsWith('..'+sep)||rel.startsWith(sep)) throw Error('path outside approved root');
  return target;
};

export function inspect(root,manifest,review){
 const failures=[];
 const err = x=>failures.push(x);
 if(manifest?.contract !== 'BOSS-ART-STORY-PRECOMPOSE-V1')err('wrong contract');
 if(typeof manifest?.slide_id!=='string'||!manifest.slide_id)err('slide identity missing');
 if(typeof manifest?.candidate_id!=='string'||!manifest.candidate_id)err('candidate identity missing');
 if(manifest?.stage!=='SEPARATE_LAYERS_ONLY')err('pre-compose submission must contain separate layers only');
 if(review?.slide_id!==manifest?.slide_id||review?.candidate_id!==manifest?.candidate_id)err('review identity mismatch');

 const roles=['art','story'];
 const files={};
 for(const role of roles){
   const layer=manifest?.[role],decision=review?.[role];
   if(!layer || typeof layer !== 'object'){err(role+' source missing');continue;}
   if(!decision || typeof decision !== 'object'){err(role+' human decision missing');continue;}
   for(const kind of ['source','preview']){
     const path=layer[kind+'_path'],sha=layer[kind+'_sha256'];
     if(!isHash(sha)){err(role+' '+kind+' SHA missing or invalid');continue;}
     try{
       const f=local(root,path);
       if(!existsSync(f)){err(role+' '+kind+' file unavailable');continue;}
       files[role+':'+kind]=f;
       if(digest(readFileSync(f))!==sha)err(role+' '+kind+' bytes modified after selection');
     }catch(e){err(role+' '+kind+' '+String(e.message));}
     if(decision[kind+'_sha256']!==sha)err(role+' '+kind+' hash not selected by reviewer');
   }
   if(decision.decision!=='APPROVE_'+role.toUpperCase())err(role+' not explicitly approved');
   if(typeof decision.reviewer_account!=='string'||decision.reviewer_account.trim().length<2)err(role+' reviewer identity missing');
   if(typeof decision.review_reference!=='string'||!/^https:\/\//.test(decision.review_reference))err(role+' external review reference missing');
   if(decision.candidate_id!==manifest.candidate_id)err(role+' decision candidate differs');
   if(decision.slide_id!==manifest.slide_id)err(role+' decision slide differs');
 }
 if(files['art:source'] && files['art:source']===files['story:source'])err('art and story must be separate source files');
 if(files['art:preview'] && files['art:preview']===files['story:preview'])err('art and story must be separately reviewable previews');
 if(manifest?.composite_path||manifest?.compiled_pdf||manifest?.release_authorized)err('pre-compose stage must not assert a compiled slide/release');
 return {
  status:failures.length?'HOLD':'SOURCE_AND_RECEIPT_STRUCTURE_PASS',
  failures,
  source_custody_checked:!failures.length,
  external_reviewer_identity_verified:false,
  art_human_authentication:'NOT_TESTED',
  story_human_authentication:'NOT_TESTED',
  compiled_slide_permitted:false,
  release_authorized:false
 };
}
if(process.argv[1] && import.meta.url === new URL('file://'+resolve(process.argv[1])).href){
 try{
   if(process.argv.length!==5)throw Error('usage: node check_precomposition.mjs ROOT MANIFEST.json REVIEWS.json');
   const root=process.argv[2];
   const manifest=JSON.parse(readFileSync(process.argv[3],'utf8'));
   const review=JSON.parse(readFileSync(process.argv[4],'utf8'));
   const result=inspect(root,manifest,review);
   console.log(JSON.stringify(result,null,2));
   process.exit(result.failures.length?2:0);
 }catch(e){console.error('HOLD',String(e));process.exit(2)}
}
