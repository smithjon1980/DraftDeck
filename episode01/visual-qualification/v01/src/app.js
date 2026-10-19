/* BOSS visual qualification v0.1. React components with native DOM editorial text.
 * Content: exact candidate copy from episode01/reference/slide-copy.candidate.json.
 * Status: VISUAL_CANDIDATE, NOT HUMAN APPROVED.
 * Intentional test-fixture additions: navigation, candidate/status labels, reflection PLACEHOLDER.
 * Never replace original logo with an approximated vector or typographic recreation.
 */
(function () {
  'use strict';
  const h = React.createElement;
  const logo = '../../assets/brand/bioscillate-original-supplied.jpg';
  const slideIds = ['01','02','06'];
  const editable = (tag, className, text, extra={}) => h(tag,{className,...extra},text);
  function BrandMasthead({full=false}) {
    return h('div',{className:full?'brand-image-large':'brand-image-small'},
      h('img',{src:logo,alt:'Original Bioscillate logo: cyan waveform, black diamond, magenta fragmented waveform, bioscillate wordmark, Operating System by Seven',draggable:false}));
  }
  function Header({index,label}) {return h('header',{className:'technical-header'},
    h('div',{className:'header-brand'}, h(BrandMasthead)),
    h('div',{className:'header-meta'},
      editable('span','header-overline','BIOSCILLATE / EPISODE 01'),
      editable('span','header-title',label),
      editable('span','header-note','DESIGN QUALIFICATION · CANDIDATE')),
    editable('div','header-index',index)
  );}
  function Footer({slide,statement}) {return h('footer',{className:'technical-footer'},
    editable('span','footer-mark','BOSS / SEVEN'),
    editable('span','footer-statement',statement||'CANDIDATE VISUAL · NOT APPROVED'),
    editable('span','footer-number','EP01 / '+slide)
  );}
  function Reflection({small=false}) {return h('section',{className:small?'reflection compact':'reflection',role:'note'},
    editable('div','reflection-kicker','PAUSE & CONSIDER'),
    editable('div','reflection-copy','[REFLECTION QUESTION PENDING AUTHOR APPROVAL]'),
    h('div',{className:'reflection-lines'},h('span'),h('span'))
  );}
  function Slide01(){return h('section',{'data-document-role':'page','data-slide-id':'01','data-label':'Slide 01 — Title','className':'slide slide01'},
    h('div',{className:'slide01-top'},editable('div','brand-rail-label','01 / THE PITCH'),editable('div','brand-rail-label','INFRASTRUCTURE ENTREPRENEURSHIP')),
    h('main',{className:'slide01-main'},
      h('div',{className:'slide01-left'},
        editable('div','eyebrow','EPISODE 01 · OPENING POSITION'),
        editable('h1','title title01',"You Don't Need a Downline. You Need a Skill."),
        h('div',{className:'slide01-rule'}),
        editable('div','design-proof','SOURCED CANDIDATE TEXT / NOT RELEASED')),
      h('div',{className:'slide01-right'},h(BrandMasthead,{full:true}),editable('div','right-under','ORIGINAL BRAND ARTWORK · SEPARATE IMAGE LAYER'))
    ),
    h(Reflection,{small:true}),
    h(Footer,{slide:'01',statement:'OPENING FRAME · AUTHOR APPROVAL PENDING'})
  );}
  const leftItems=['Recruit','Sell','Expand the network','Growth through distribution'];
  const rightItems=['Learn','Build','Verify, Deploy, Support','Value through delivered work'];
  function ComparisonColumn({header,items,alt}) {return h('article',{className:alt?'compare-column muted':'compare-column active'},
    h('div',{className:'compare-heading'},editable('span','compare-heading-txt',header),editable('span','compare-index',alt?'A':'B')),
    h('div',{className:'compare-list'},items.map((item,i)=>h('div',{key:i,className:'compare-list-item'},editable('span','list-index',String(i+1).padStart(2,'0')),editable('span','list-copy',item))))
  );}
  function Slide02(){return h('section',{'data-document-role':'page','data-slide-id':'02','data-label':'Slide 02 — Technical Comparison','className':'slide slide02'},
    h(Header,{index:'02',label:'CAPABILITY COMMERCE'}),
    h('main',{className:'slide02-main'},
      editable('div','eyebrow','OPPORTUNITY STRUCTURES · COMPARATIVE FRAME'),
      editable('h1','title title02',"The Problem Isn't Networking"),
      h('div',{className:'compare-grid'},
        h(ComparisonColumn,{header:'Network-Driven Opportunity',items:leftItems,alt:true}),
        h(ComparisonColumn,{header:'Capability Commerce',items:rightItems,alt:false})),
      h('div',{className:'slide02-lower'},
        h('article',{className:'distinction'},editable('div','distinction-kicker','OPERATIONAL DISTINCTION'),editable('p','distinction-body',"Networking itself isn't the problem. Building professional relationships, sharing knowledge, collaborating, and referring customers are legitimate activities. The difference is what the network exists to produce. In BOSS, a practitioner network coordinates expertise and projects, not recruitment commissions.")),
        h(Reflection,{small:true})
      )
    ),
    h(Footer,{slide:'02',statement:'BOSS · EPISODE 01 · SLIDE 02 | VISUAL MASTER CANDIDATE'})
  );}
  const steps=[['01','LEARN'],['02','BUILD'],['03','VERIFY'],['04','DEPLOY'],['05','SUPPORT']];
  function SequenceDiagram(){return h('div',{className:'sequence-grid',role:'group','aria-label':'Five labels in their source-provided order: learn, build, verify, deploy, support'},
    steps.map(([n,s],i)=>h('div',{key:n,className:'sequence-item'},
      editable('div','sequence-number',n),editable('div','sequence-name',s),editable('div','sequence-bottom','STAGE '+n),
      i<4?h('div',{className:'sequence-link','aria-hidden':true}):null))
  );}
  function Slide06(){return h('section',{'data-document-role':'page','data-slide-id':'06','data-label':'Slide 06 — Sequence','className':'slide slide06'},
    h(Header,{index:'06',label:'OPERATING SEQUENCE'}),
    h('main',{className:'slide06-main'},
      editable('div','eyebrow','SEQUENCE · EXACT LABELS FROM CANDIDATE SOURCE'),
      editable('h1','title title06','A different operating sequence.'),
      h(SequenceDiagram),
      h('div',{className:'sequence-detail'},
        editable('div','sequence-claim','VALUE FOLLOWS DEMONSTRATED CAPABILITY. NOT RECRUITMENT.'),
        editable('div','sequence-caveat','PARTICIPANTS · MESSAGE LABELS · DECISION GATES: [UNKNOWN] — NOT DEPICTED')
      ),
      h(Reflection)
    ),
    h(Footer,{slide:'06',statement:'SOURCE-ORDER DIAGRAM · NO UNVERIFIED DECISION GATES'})
  );}
  const slides=[Slide01,Slide02,Slide06];
  class App extends React.Component {
    constructor(props){super(props);const start=Number(new URLSearchParams(location.search).get('index')||'0');this.state={active:Math.max(0,Math.min(2,start))};this.nav=this.nav.bind(this);this.scale=this.scale.bind(this)}
    componentDidMount(){this.scale();window.addEventListener('resize',this.scale)}
    componentDidUpdate(){this.scale()}
    componentWillUnmount(){window.removeEventListener('resize',this.scale)}
    nav(i){this.setState({active:Math.max(0,Math.min(2,i))})}
    scale(){const frame=document.getElementById('slide-holder'),slide=document.querySelector('.slide');if(!frame||!slide)return;const ratio=Math.min((window.innerWidth-36)/1920,(window.innerHeight-86)/1080,1);slide.style.transform=`scale(${ratio})`;frame.style.width=`${1920*ratio}px`;frame.style.height=`${1080*ratio}px`}
    render(){const active=this.state.active,comp=slides[active]||Slide01;return h('div',{className:'viewer-root'},
      h('div',{className:'viewer-toolbar',role:'toolbar','aria-label':'Slide navigation'},
        h('span',{className:'toolbar-title'},'BOSS / VISUAL QUALIFICATION 0.1'),
        h('div',{className:'toolbar-actions'},
          h('button',{onClick:()=>this.nav(active-1),disabled:active===0},'← PREVIOUS'),
          h('span',{className:'toolbar-count'},'SLIDE '+slideIds[active]+' / 06'),
          h('button',{onClick:()=>this.nav(active+1),disabled:active===2},'NEXT →'))),
      h('div',{id:'slide-holder'},h(comp)),
      h('div',{className:'viewer-info'},'RENDER CANDIDATE · SOURCE-GROUNDED COPY · ORIGINAL LOGO · VISUAL APPROVAL NOT ESTABLISHED')
    );}
  }
  window.BOSS={slides,ids:slideIds,App};
  ReactDOM.render(h(App),document.getElementById('root'));
})();

