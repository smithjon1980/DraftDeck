from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
import html, json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("Copy", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("CopyBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
P=Path(__file__).parent; W,H=1632,1056
c=canvas.Canvas(str(P/'DraftDeck_Process_Comp.pdf'),pagesize=(1224,792));c.scale(.75,.75)
svg=[];texts=[]
def line(x,y,a,b,col='#20252A',dash=False):
 c.setStrokeColor(HexColor(col));c.setLineWidth(1.5);c.setDash(5,5) if dash else c.setDash();c.line(x,H-y,a,H-b)
 svg.append(f'<path d="M{x},{y} L{a},{b}" fill="none" stroke="{col}" stroke-width="1.5"'+(' stroke-dasharray="5 5"' if dash else '')+'/>')
def rect(x,y,w,h,col='#20252A'):
 c.setStrokeColor(HexColor(col));c.setDash();c.setLineWidth(1.5);c.rect(x,H-y-h,w,h)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="{col}" stroke-width="1.5"/>')
def diamond(x,y,w,h):
 pts=[(x+w/2,y),(x+w,y+h/2),(x+w/2,y+h),(x,y+h/2),(x+w/2,y)]
 for u,v in zip(pts,pts[1:]):line(*u,*v)
def text(x,y,s,size=19,bold=False,col='#20252A',width=None):
 font='CopyBold' if bold else 'Copy'
 lines=[]
 if width:
  row=''
  for word in s.split():
   z=(row+' '+word).strip()
   if stringWidth(z,font,size)>width and row:lines.append(row);row=word
   else:row=z
  lines.append(row)
 else:lines=s.split('\n')
 for i,t in enumerate(lines):
  c.setFillColor(HexColor(col));c.setFont(font,size);c.drawString(x,H-y-size-i*size*1.3,t)
 texts.append(f'<div class="copy" style="left:{x}px;top:{y}px;font-size:{size}px;font-weight:{700 if bold else 400};color:{col};'+(f'width:{width}px;' if width else '')+'">'+html.escape(s).replace('\n','<br>')+'</div>')
def arrow(points,col='#20252A'):
 for a,b in zip(points,points[1:]):line(*a,*b,col)
 x,y=points[-1];u,v=points[-2];dx=x-u;dy=y-v;import math
 z=math.hypot(dx,dy);dx/=z;dy/=z
 line(x,y,x-dx*10+dy*5,y-dy*10-dx*5,col);line(x,y,x-dx*10-dy*5,y-dy*10+dx*5,col)
def box(x,y,w,h,title,body):
 rect(x,y,w,h);text(x+16,y+14,title,20,True);text(x+16,y+44,body,15,width=w-32)
line(50,40,1582,40);text(50,53,'BOSS / DAY ZERO',14);text(1200,53,'PROCESS COMP / 01',14)
text(50,95,'DELIVERED IS NOT VERIFIED.',53,True)
text(50,166,'A receipt records arrival. Inspection establishes evidence. Authorization governs onward dispatch.',23)
text(50,216,'ONE HANDOFF / THREE RESPONSIBILITIES / EXPLICIT BRANCHES',15,True,col='#B34700')
# swimlane rails
for y in (250,375,615,810):line(50,y,1582,y)
line(205,250,205,810)
text(60,282,'SENDER',18,True);text(60,313,'Defines the frame',15,width=130)
text(60,420,'EXECUTOR',18,True);text(60,453,'Reads and reports',15,width=130)
text(60,655,'REVIEWER',18,True);text(60,688,'Checks evidence\nand release scope',15)
box(235,270,285,85,'Define shipment','Inputs, versions, destination, scope')
box(570,270,285,85,'Transfer payload','Carry the source and shared frame')
arrow([(520,312),(570,312)])
box(570,400,220,85,'Record receipt','RECEIVED: payload arrived')
arrow([(680,355),(680,400)])
diamond(840,393,165,100);text(882,418,'Source',18,True);text(872,443,'readable?',18)
arrow([(790,442),(840,442)])
box(1080,400,370,85,'Run authorized inventory','Report source facts; preserve missing room as UNKNOWN')
arrow([(1005,442),(1080,442)]);text(1015,410,'YES',14,True)
box(820,526,360,65,'Pause dependent work','Supply required source, then recheck')
arrow([(922,493),(922,526)],'#B34700');text(935,501,'NO / NOT ESTABLISHED',13,True,col='#B34700')
arrow([(820,558),(805,558),(805,510),(870,510),(870,493)],'#B34700')
diamond(1060,633,250,114);text(1122,658,'Evidence',19,True);text(1090,690,'checks passed?',18)
arrow([(1250,485),(1250,603),(1185,603),(1185,633)])
diamond(1370,640,170,105);text(1404,663,'Release',18,True);text(1389,688,'authorized?',17)
arrow([(1310,690),(1370,690)]);text(1320,666,'YES',13,True);arrow([(1185,747),(1185,765)],'#B34700');text(1050,770,'NO / UNKNOWN: hold for review',14,True,col='#B34700')
text(1360,760,'YES: dispatch   NO: hold',16,True,col='#B34700')
arrow([(1455,745),(1455,756)],'#B34700')
text(240,650,'MISSING VALUE ≠ MISSING SOURCE',20,True)
text(240,688,'A room number may remain UNKNOWN while an authorized inventory completes. Missing required source content pauses the action that depends on it.',19,width=660)
text(50,835,'STATUS KEY',15,True,col='#B34700')
text(240,831,'PARTIAL: work remains     FAILED: attempted operation failed     UNKNOWN: evidence is insufficient',18)
line(50,880,1582,880)
text(50,898,'YOUR TURN / What proves arrival, correctness, and permission to dispatch?',20,True)
for y in (953,986):line(50,y,1582,y,'#B9BFC4')
text(50,1015,'17 × 11 IN / LIVE TEXT + SEPARATE VECTOR DIAGRAM / HUMAN REVIEW REQUIRED',12)
c.showPage();c.save()
art='<svg xmlns="http://www.w3.org/2000/svg" width="1632" height="1056" viewBox="0 0 1632 1056">'+''.join(svg)+'</svg>'
(P/'process.svg').write_text(art)
css='*{box-sizing:border-box}body{margin:0;background:#fff;font-family:Arial,Helvetica,sans-serif;color:#20252a}.page{position:relative;width:1632px;height:1056px;background:#fff;overflow:hidden}.diagram{position:absolute;inset:0;width:100%;height:100%}.copy{position:absolute;line-height:1.3;white-space:pre-wrap;margin:0}@page{size:17in 11in;margin:0}'
(P/'styles.css').write_text(css)
(P/'DraftDeck_Process_Comp.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>BOSS process comp</title><style>'+css+'</style><body><section class="page" data-document-role="page"><div class="diagram">'+art+'</div>'+''.join(texts)+'</section></body></html>')
(P/'REVIEW.md').write_text('DraftDeck trial candidate — awaiting human review.\n\nOriginal process diagram built deterministically; no generated scene artwork. Three responsibility swimlanes, labeled readability branches, source recovery loop, verification followed by separate release authorization. Missing room value remains UNKNOWN without blocking authorized inventory. Diagram geometry is a separate SVG; instructional labels and copy are live HTML. PDF is independently composed from the same coordinates and copy, not a browser export. Browser rendering, physical print and Canva import untested. No production release.\n')
