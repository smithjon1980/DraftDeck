import {plans} from './layouts.mjs';
const required=['illustration','framework','narration','reflection','notes'];
export function validate({layouts=plans,colors=[],background='#FFFFFF',medium='PREMIUM_PHOTOREALISTIC_EDITORIAL',page=[17,11],darkFullBleed=false}={}){
 const errors=[];if(page[0]!==17||page[1]!==11)errors.push('GEOMETRY');
 if(background!=='#FFFFFF'||darkFullBleed)errors.push('DARK_BACKGROUND');
 if(!['EDITORIAL_ILLUSTRATION','PREMIUM_PHOTOREALISTIC_EDITORIAL','TECHNICAL_CAD_ISO_DIAGRAM'].includes(medium))errors.push('MEDIUM');
 if(colors.some(c=>!['#FFFFFF','#00BCEB','#E30074','#000000'].includes(c.toUpperCase())))errors.push('PALETTE');
 if(layouts.length!==7)errors.push('COUNT');
 const signatures=new Set();
 layouts.forEach((v,i)=>{const keys=Object.keys(v.zones||{});if(keys.length!==5||required.some(k=>!keys.includes(k))){errors.push('ZONE:'+i);return}
 const entries=Object.entries(v.zones);
 entries.forEach(([k,a])=>{const [x,y,w,h]=a;if([x,y,w,h].some(n=>!Number.isFinite(n))||x<.5||y<1.4||w<=0||h<=0||x+w>16.5+1e-8||y+h>10.3+1e-8)errors.push('BOUND:'+i+':'+k)});
 for(let a=0;a<entries.length;a++)for(let b=a+1;b<entries.length;b++){let [x,y,w,h]=entries[a][1],[X,Y,W,H]=entries[b][1];if(Math.min(x+w,X+W)>Math.max(x,X)+1e-8&&Math.min(y+h,Y+H)>Math.max(y,Y)+1e-8)errors.push('OVERLAP:'+i)}
 const s=JSON.stringify(entries.sort(([a],[b])=>a.localeCompare(b)));if(signatures.has(s))errors.push('DUPLICATE:'+i);signatures.add(s);
 });return {pass:errors.length===0,errors};
}
