from pathlib import Path
import json,math,base64,html,shutil,importlib.util
R=Path(__file__).resolve().parent;DECK=R.parent;A=DECK/'artwork';OUT=DECK/'output';OUT.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('build',str(R.parents[2]/'skills/draftdeck/scripts/build_slide.py'));b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
BLACK='#1A1A1A';ORANGE='#B34700';GRAY='#DEDEDE'
scenes=[]
class Slide:
 def __init__(self,n,k,title,block):
  self.n=n;self.layers=[];self.paths=[];self.title=title;self.block=block
  self.paths.append('<rect width="1920" height="1080" fill="white"/>')
  for x in range(56,1865,28):self.line(x,52,x,1028,.4,GRAY)
  for y in range(52,1029,28):self.line(56,y,1864,y,.4,GRAY)
  self.rect(56,52,1808,976,2)
  for x in range(56,1865,226):self.line(x,35,x,52,1);self.line(x,1028,x,1045,1)
  for y in [52,296,540,784,1028]:self.line(38,y,56,y,1);self.line(1864,y,1882,y,1)
  for i in range(8):self.text(str(i+1),158+i*226,30,12,'Courier New');self.text(str(i+1),158+i*226,1034,12,'Courier New')
  for i,y in enumerate([172,416,660,904]):self.text(chr(65+i),26,y,12,'Courier New');self.text(chr(65+i),1882,y,12,'Courier New')
  self.text('// '+k.upper(),85,80,22,'Courier New')
  for i,s in enumerate(title.split('\n')):self.text(s,85,122+i*61,51,'Georgia','bold')
  self.rect(1520,916,344,112,1.1);self.line(1520,970,1864,970,1);self.line(1520,996,1864,996,1)
  self.line(1632,970,1632,1028,1);self.line(1750,970,1750,1028,1)
  self.text('TITLE:',1534,927,14,'Courier New');self.text(block,1534,949,18,'Arial','bold')
  for s,x in [('REV:',1534),('STATUS:',1645),('SHEET:',1763)]:self.text(s,x,976,13,'Courier New')
  for s,x in [('4.0',1534),('CANDIDATE',1645),(f'{n:02d} / 15',1763)]:self.text(s,x,1004,15,'Courier New')
 def line(self,x,y,ex,ey,w=1,c=BLACK):self.paths.append(f'<path d="M{x},{y} L{ex},{ey}" fill="none" stroke="{c}" stroke-width="{w}"/>')
 def rect(self,x,y,w,h,stroke=1,c=BLACK,fill='none'):self.paths.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{c}" stroke-width="{stroke}"/>')
 def circle(self,x,y,r,stroke=1,c=BLACK):self.paths.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="white" stroke="{c}" stroke-width="{stroke}"/>')
 def arrow(self,x,y,ex,ey,c=BLACK):
  self.line(x,y,ex,ey,2,c);a=math.atan2(ey-y,ex-x)
  for d in [-.5,.5]:self.line(ex,ey,ex-14*math.cos(a+d),ey-14*math.sin(a+d),2,c)
 def text(self,s,x,y,size=25,font='Arial',weight='normal',color=BLACK):self.layers.append(dict(type='text',text=s,x=x,y=y,size=size,font=font,weight=weight,color=color))
 def copy(self,rows,x=90,y=330,size=28,step=49):
  for i,s in enumerate(rows):self.text(s,x,y+i*step,size)
 def art(self,n,x=760,y=280,w=1040,h=585):self.layers.append(dict(type='image',path=f'artwork/story-{n:02d}.webp',x=x,y=y,width=w,height=h,alt=f'Text-free story artwork for slide {self.n}'))
 def footer(self,s,s2=None):
  self.text(s,85,944,24)
  if s2:self.text(s2,85,980,23)
 def done(self):
  name=f'frame-{self.n:02d}.svg';(A/name).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">'+''.join(self.paths)+'</svg>')
  scene=dict(title=self.title.replace('\n',' '),width=1920,height=1080,background='white',layers=[dict(type='image',path='artwork/'+name,x=0,y=0,width=1920,height=1080,alt='CAD drafting background and precision geometry')]+self.layers)
  scenes.append(scene)
# 01
s=Slide(1,'2026 logistics framework - rev 4.0','Logistics Framework Architecture & Interface QA:\nThe Canonical 2026 Developer Gate','QA IMPLEMENTATION GATE')
s.art(5,220,230,1480,680);s.text('INTERFACE / IMPLEMENTATION REVIEW',100,294,23,'Courier New')
s.text('APPROVED FOR INGESTION',98,817,36,'Arial','bold',ORANGE)
s.footer('Approval wording reproduced from the reference.', 'Candidate rebuild: approval is not newly conferred.');s.done()
# 02
s=Slide(2,'root doctrine - logistics architecture','Stop Managing Magic and\nStart Routing Logistics','ROOT DOCTRINE')
s.copy(['Data = cargo','Information payloads','Agents = couriers','Proxy handlers','Models = transport','Freight services'],90,340,30,60);s.art(2)
s.footer('Data is cargo. Agents are couriers. Models are freight.','Verification is proof of delivery.');s.done()
# 03
s=Slide(3,'shipping and receiving authority','The Shipping & Receiving Control Desk\nSecures Non-Delegable Human Intent','HUMAN CONTROL DESK')
s.copy(['The sender owns intent and objective.','The receiver / consignee owns the','release context. Systems may route,','transform, and report within declared','handling constraints.','','Final release authority remains human.'],90,335,27,47)
s.rect(1000,340,630,380,2);s.text('SHIPPING & RECEIVING',1080,382,28,'Courier New','bold');s.text('CONTROL DESK',1170,426,34,'Arial','bold')
for y in [505,575,645]:s.rect(1080,y,470,42,1)
s.text('INBOUND CARGO',1110,514,20,'Courier New');s.text('ROUTE / HANDLE / HOLD',1110,584,20,'Courier New');s.text('RELEASE AUTHORITY',1110,654,20,'Courier New')
s.arrow(860,530,995,530);s.arrow(1635,650,1770,650);s.text('DISPATCH / ROUTING',720,485,20,'Courier New');s.text('PROOF / RELEASE',1630,610,20,'Courier New')
s.done()
# 04 precise ledger
s=Slide(4,'claim control - epistemic layer','Classify, Sever, Account,\nRoute, and Adjudicate','EPISTEMIC GEOGRAPHY')
for i,(a,z) in enumerate([('LOCATION','Triage Gate'),('ACCOUNTING','Claim Ledger'),('ADJUDICATION','Ground Truth Fixture'),('AUTHORITY','Control Desk')]):
 x=95+i*445;s.rect(x,310,380,98,2);s.text(a,x+20,330,28,'Courier New','bold');s.text(z,x+20,371,22)
 if i<3:s.arrow(x+383,359,x+436,359)
s.text('GENERATED OUTPUT',95,469,25,'Courier New','bold');s.rect(95,510,280,320,1.5)
for y in range(550,801,35):s.line(120,y,345,y,.8)
for i,name in enumerate(['Proposition A','Proposition B','Proposition C']):
 y=510+i*115;s.rect(475,y,820,90,1.2);s.text(name,495,y+23,27);s.text('Warrant + competence',1360,y+23,25);s.arrow(1298,y+45,1340,y+45)
s.footer('Procedural completion is not evidentiary establishment.','Account for each proposition before it supports a conclusion.');s.done()
# 05
s=Slide(5,'execution discipline','The D.A.T.A. Hardware Interface\nEnforces Execution Discipline','D.A.T.A. PROTOCOL')
s.art(5,390,265,1140,585)
s.copy(['D — DIRECT: objective / format','A — ANCHOR: pinned source','T — THROTTLE: time / cost limits','A — AUDIT: append-only trace'],95,300,24,42)
s.footer('Lock model version and source before execution.','Record the run; constrain time, cost, and compute cadence.');s.done()
# 06
s=Slide(6,'proof-of-delivery protocol','The Canonical 6-Field Verification Tag\nSchema Serves as Proof of Delivery','6-FIELD SCHEMA')
fields=[('RUN_ID','Unique run identifier'),('CARGO_CLASS','Security / governance handling class'),('QUALIFICATION_ID','Qualified model / environment'),('ROUTE_PLAN_ID','Approved shipment / route boundaries'),('STATUS','HELD / VERIFIED / RELEASED / BLOCKED'),('ELAPSED_TIME','Execution duration')]
for i,(a,z) in enumerate(fields):
 y=325+i*80;s.line(90,y+70,840,y+70,.8);s.text(a,90,y,25,'Courier New','bold');s.text(z,90,y+34,22)
s.art(6,890,270,880,600);s.footer('UI state is not Verification Tag status.','Fluent delivery is not verified delivery. Check the tag.');s.done()
#07
s=Slide(7,'UI/UX doctrine - system invariant','Interface Rendering Is an Operational\nControl Surface, Not a Cosmetic Overlay','UI/UX DOCTRINE')
steps=[('External','Primitive'),('Grammar','Normalization'),('Canonical','Glyph'),('Compound','Component'),('Operational','State'),('Rendered','Interface')]
for i,(a,z) in enumerate(steps):
 x=95+i*292;s.rect(x,345,240,165,1.5);s.text(a,x+16,390,27);s.text(z,x+16,432,24)
 if i<5:s.arrow(x+245,428,x+282,428)
s.paths.append('<path d="M300 620 L415 666 L398 779 L300 848 L202 779 L185 666 Z" fill="none" stroke="#B34700" stroke-width="4"/>')
s.copy(['Visual ambiguity masks split-signal errors.','Uncontrolled inheritance from third-party libraries','degrades state legibility when clarity matters most.'],520,650,31,58);s.done()
#08
s=Slide(8,'semantic sourcing','External Libraries Supply\nSemantics, Not Native Styling','SEMANTIC SOURCING')
s.copy(['LUCIDE','Technical UI, workflow, routing,','databases, tools.','','MATERIAL SYMBOLS OUTLINED','Operational status and control panels.','','PHOSPHOR ICONS','Specialized logistics, transport, roles.'],90,315,25,45);s.art(8,850,280,900,580)
s.footer('Select by meaning. External libraries are semantic search tiers','feeding one unified Logistics Framework visual grammar.');s.done()
#09
s=Slide(9,'canonical glyph reconstruction','Normalize by Geometry Using\nthe Canonical Logistics Framework Glyph','GLYPH RECONSTRUCTION')
def gear(cx,cy,r):
 pts=[]
 for i in range(64):
  a=i*math.pi/32;rr=r*(1 if i%8 in [1,2,3,4] else .82);pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
 s.paths.append('<polygon points="'+' '.join(pts)+'" fill="none" stroke="#1A1A1A" stroke-width="3"/>');s.circle(cx,cy,r*.4,3)
gear(400,550,145);gear(1300,550,145);s.arrow(630,550,1030,550);s.text('GEOMETRY NORMALIZATION',630,487,24,'Courier New');s.text('BEFORE',330,758,27,'Courier New');s.text('AFTER',1250,758,27,'Courier New')
s.copy(['Linecap: butt','Linejoin: miter','Stroke: 1.5 / 2.0px','Fill: none','Non-scaling stroke'],1520,400,22,56)
s.footer('Never inherit a library’s native style blindly.','Maintain structural vector integrity like CAD drawings.');s.done()
#10
s=Slide(10,'controlled aesthetics - token registry','The Absolute Zero-Fill Palette\nand Structural Line Hierarchy','TOKEN REGISTRY')
for i,(name,code) in enumerate([('Near-Black Ink','#1A1A1A'),('Pure White Ground','#FFFFFF'),('Drafting Gray','#DEDEDE'),('Burnt Orange','#B34700')]):
 x=95+i*250;s.rect(x,380,195,225,3,code if code!='#FFFFFF' else BLACK);s.text(name,x,637,21);s.text(code,x,672,23,'Courier New')
s.text('STRUCTURAL STROKE HIERARCHY',1140,331,26,'Courier New','bold')
for i,(w,a,z) in enumerate([(3,'1.0pt','Outer frames / major dividers'),(1.5,'0.5pt','Controls / connector housings'),(.75,'0.25pt','Grid / hatch / detail lines')]):
 y=415+i*125;s.line(1140,y,1770,y,w);s.text(a+'  '+z,1140,y+25,23)
s.footer('Prohibited: solid pictogram fills, UI red, gradients, glows,','ambient occlusion, glossy 3D, and soft pill shapes.');s.done()
#11
s=Slide(11,'visual state registry','Render by State Using Architectural\nDrafting Textures to Communicate Hierarchy','VISUAL STATE REGISTRY')
for i,a in enumerate(['DEFAULT','ROUTED','HELD','BLOCKED','VERIFIED']):
 x=95+i*346;s.rect(x,340,280,420,2)
 if i==1:
  for dx in range(8,279,12):s.line(x+dx,343,x+dx,757,.8)
 if i in [2,3]:
  for dy in range(-280,420,15):
   xx=max(0,-dy);yy=max(0,dy);length=min(280-xx,420-yy);s.line(x+xx,340+yy,x+xx+length,340+yy+length,.7)
 if i==3:
  for dy in range(-280,420,15):
   xx=max(0,-dy);yy=max(0,dy);length=min(280-xx,420-yy);s.line(x+280-xx,340+yy,x+280-xx-length,340+yy+length,.7)
 if i==4:s.paths.append(f'<path d="M{x+140} 610 l25 25 l55 -65" fill="none" stroke="#1A1A1A" stroke-width="4"/>')
 s.text(a,x+20,796,26,'Courier New','bold')
s.footer('Hatching communicates state without relying exclusively on color.','Visual texture preserves situational awareness.');s.done()
#12
s=Slide(12,'layer 0 governance - custom exceptions','Authorized Project-Specific\nNative Component Geometry','CUSTOM EXCEPTIONS')
items=[('CONTROL DESK',105),('VERIFICATION TAG',550),('D.A.T.A. CONNECTOR',990),('CLAIM COMPARATOR',1430)]
for label,x in items:
 s.rect(x,330,350,360,1.5);s.text(label,x+18,715,22,'Courier New','bold')
 if label=='CONTROL DESK':
  s.rect(x+65,430,220,120,2);s.line(x+105,390,x+105,430,2);s.line(x+245,390,x+245,430,2);s.line(x+105,390,x+245,390,2);s.text('IN',x+30,474,18,'Courier New');s.text('OUT',x+292,474,18,'Courier New')
 elif label=='VERIFICATION TAG':
  s.rect(x+70,390,210,210,2);s.circle(x+105,425,12,2);s.line(x+105,437,x+105,470,1.5);s.line(x+95,505,x+255,505,1);s.line(x+95,545,x+255,545,1)
 elif label=='D.A.T.A. CONNECTOR':
  s.circle(x+175,495,95,2);s.circle(x+175,495,45,2)
  for dx,dy in [(0,-70),(70,0),(0,70),(-70,0)]:s.circle(x+175+dx,495+dy,9,1.5)
 else:
  s.rect(x+55,400,240,70,1.5);s.rect(x+55,535,240,70,1.5);s.line(x+175,470,x+175,535,1.5);s.text('A',x+165,423,18,'Courier New');s.text('B',x+165,558,18,'Courier New')
s.footer('Layer 0 governs the Shipping & Receiving Control Desk.','Register custom native components; do not improvise exceptions.');s.done()
#13 reuse the bundled validated CAD scene
cad=json.loads((R/'Slide13_Seed.json').read_text())
scenes.append(cad)
#14
s=Slide(14,'binary implementation gate','The 20-Category Developer QA Gate\nDictates Absolute Binary Implementation','20-POINT QA GATE')
req=['Semantic source: approved libraries','No native styles inherited','24 / 32px grid locked','1.5 / 2.0px stroke locked','Butt linecaps','Miter joins','Non-scaling vector effect','Absolute zero fill','No gradients / glows / shadows','Near-black primary ink','Pure white ground','Burnt orange restricted accent','State conveyed via hatching','6-field verification tag present','UI state detached from tag status','Serif titles / mono kickers','Structural line hierarchy','Custom exceptions registered','No magic AI copy / metaphors','Human release latch required']
for col in range(2):
 x=90+col*880;s.text('REQUIREMENT',x+15,315,22,'Courier New','bold');s.text('STATUS',x+703,315,22,'Courier New','bold');s.rect(x,350,820,500,1.5);s.line(x+680,350,x+680,850,1)
 for j in range(10):
  i=col*10+j;y=350+j*50;s.line(x,y+50,x+820,y+50,.7);s.text(f'{i+1:02d}  '+req[i],x+15,y+14,22);s.text('PENDING',x+693,y+15,20,'Courier New')
s.footer('Reproduced requirements; statuses await implementation review.','Reference PASS / CLEARED markings are not new approval.');s.done()
#15
s=Slide(15,'doctrine footer rail','Consignee Release Latch:\nHuman Authority Alone Releases','CONSIGNEE RELEASE LATCH')
s.art(15,145,270,1630,585);s.text('HELD / BLOCKED',95,292,25,'Courier New');s.text('OPEN / RELEASED',1440,292,25,'Courier New')
s.footer('Epistemic control may classify, account, route, and hold.','Verification may compare and adjudicate. Human authority alone releases.');s.done()
assert len(scenes)==15
(OUT/'Scenes.json').write_text(json.dumps(scenes,indent=2))
sections=[]
for i,scene in enumerate(scenes):
 h=b.build(scene,DECK);start=h.index('<section');end=h.index('</section>')+len('</section>');sections.append(h[start:end]);(OUT/f'Slide-{i+1:02d}.html').write_text(h)
(OUT/'Logistics_Framework_15_Slides_Layered.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>Logistics Framework - 15 Layered CAD Slides</title><style>html,body{margin:0;padding:0;background:white}*{box-sizing:border-box}section{page-break-after:always}</style></head><body>'+''.join(sections)+'</body></html>')
print('15 pages;',sum(sum(l['type']=='text' for l in s['layers']) for s in scenes),'live text elements')
