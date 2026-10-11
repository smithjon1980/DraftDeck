import {initPlasmicLoader} from '@plasmicapp/loader-nextjs';
import {BossTitle,StoryRegion} from '@draftdeck/slide-components';
const id=process.env.NEXT_PUBLIC_PLASMIC_PROJECT_ID;
const token=process.env.NEXT_PUBLIC_PLASMIC_PUBLIC_TOKEN;
// This module is only imported when both environment variables exist.
if(!id || !token) throw new Error('Plasmic credentials are not configured');
export const PLASMIC=initPlasmicLoader({projects:[{id,token}],preview:process.env.NODE_ENV!=='production'});
PLASMIC.registerComponent(BossTitle,{name:'EP01_BossTitle',displayName:'BOSS Title (exact copy)',props:{content:{type:'string',defaultValue:'YOU ALREADY MOVE INFORMATION'}}});
PLASMIC.registerComponent(StoryRegion,{name:'EP01_StoryRegion',displayName:'BOSS Story (approved asset only)',props:{sourceAsset:{type:'string',defaultValue:'/approved-assets/ep01-workstation.png'},description:{type:'string',defaultValue:'Original workstation diagram'}}});
// No style, className, size, padding, or position props registered. Wrapper positioning in Plasmic remains a separate risk; locked slide composition is controlled by Episode01Slide and release tests.
