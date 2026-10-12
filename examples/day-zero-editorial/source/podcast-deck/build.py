from pathlib import Path
import base64, shutil, re
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
# Shared native drawing/text functions; no presentation intermediate.
base=Path('process-comp/build.py').read_text();base=base[:base.index('line(50,40,1582,40)')]
base=base.replace('P=Path(__file__).parent; W,H=1632,1056','P=Path("podcast-deck"); W,H=1632,1056').replace("P/'DraftDeck_Process_Comp.pdf'","P/'BOSS_Podcast_Story_Deck.pdf'")
exec(base)
shutil.copy('/workspace/scratch/0539641e8868/output/integrated/story.png',P/'logistics-art.png')
art64=base64.b64encode((P/'logistics-art.png').read_bytes()).decode();pages=[];outline=[]
def start(n,t,k,tm,lead):
 global svg,texts
 svg=[];texts=[];line(50,40,1582,40);text(50,53,'BOSS / BIOSCILLATE OPERATING SYSTEM BY SEVEN',13);text(1170,53,f'{k.upper()} / {n:02d}',13)
 text(50,108,t,46,True);text(50,180,lead,23,width=1480)
 outline.append(f'{n:02d}. {t} | {tm} | {k}')
def end(n,prompt):
 line(50,872,1582,872);text(50,897,'YOUR TURN / '+prompt,20,True,width=1480)
 for y in (953,986):line(50,y,1582,y,'#B9BFC4')
 text(50,1016,f'DAY ZERO / PODCAST COMPANION / {n:02d} OF 15 / REVIEW CANDIDATE',12)
 artwork='<svg xmlns="http://www.w3.org/2000/svg" width="1632" height="1056" viewBox="0 0 1632 1056">'+''.join(svg)+'</svg>'
 (P/f'diagram-{n:02d}.svg').write_text(artwork)
 pages.append('<section class="page" data-document-role="page"><div class="diagram">'+artwork+'</div>'+''.join(texts)+'</section>');c.showPage();
 if n<15:c.scale(.75,.75)
def section(x,y,num,title,body,w=680):
 text(x,y,num,16,True,col='#B34700');text(x,y+30,title,27,True,width=w);text(x,y+80,body,22,width=w)
def story(y=300,h=440):
 c.drawImage(ImageReader(str(P/'logistics-art.png')),50,H-y-h,width=1532,height=h,preserveAspectRatio=True,anchor='c',mask='auto')
 texts.append(f'<img class="story" style="left:50px;top:{y}px;width:1532px;height:{h}px" src="data:image/png;base64,{art64}" alt="Shipping scene: payload, inspection, and release barrier">')
def flow(items,y=400):
 w=310;xs=[70,460,850,1240][:len(items)]
 for i,(a,b) in enumerate(items):
  box(xs[i],y,w,140,a,b)
  if i<len(items)-1:arrow([(xs[i]+w,y+70),(xs[i+1],y+70)])
# 1
start(1,'CONFIDENCE IS NOT A RECEIPT.','opener','00:00–02:15','Make the task explicit. Carry its context. Inspect the result.');story()
text(50,765,'From a one-off prompt to a governed handoff.',30,True)
end(1,'Where does your current workflow depend on trust without evidence?')
# 2
start(2,'MAKE THE WORK VISIBLE.','editorial','00:35–02:24','A useful answer is a beginning. A repeatable process needs boundaries and evidence.')
section(60,285,'01','The wishing-well problem','A vague request leaves the system to infer the objective, invent missing context, and choose what completion looks like. In a multi-step workflow, those assumptions travel into the next task. Fluency can make the handoff look complete before anyone has checked its content.')
section(860,285,'02','The governor’s work','Define a bounded task. Identify what enters, who may act, and where the result belongs. Inspect returned evidence against the source. Recover affected work when input, access, or capability is missing. The learner retains responsibility for the frame and the acceptance decision.',650)
flow([('DEFINE','Name objective and boundaries.'),('PERFORM','Execute within authorized scope.'),('INSPECT','Compare evidence with criteria.')],665)
end(2,'Which boundary would make your next request inspectable?')
# 3
start(3,'A SHARED FRAME TRAVELS WITH THE TASK.','concept','02:15–03:06','A working agreement does not create shared memory, access, or identical capabilities.')
box(80,320,400,160,'SENDER','Prepare the source and explicit task frame.');box(630,320,400,160,'PAYLOAD','Source text + identified version + instructions.');box(1180,320,370,160,'RECEIVER','Use only the context actually supplied.')
arrow([(480,400),(630,400)]);arrow([(1030,400),(1180,400)])
section(80,570,'BOUNDARY','Context is carried','A second chat does not inherit the first chat’s memory. A filename does not expose file contents. Confirm what the receiving executor can actually read.',660)
section(860,570,'AUTHORITY','Capability is checked','The shared frame states scope. It does not grant tools or permissions. Confirm authorization for the affected action and exact destination.',650)
end(3,'What must travel with your payload so another executor can proceed?')
#4
start(4,'TEN FIELDS. ONE WORKING AGREEMENT.','reference','03:10–06:18','Use the fields to make the task testable, bounded, and traceable.')
fields=[('Run ID','Unique execution reference.'),('Observable objective','Result you can observe.'),('Actual inputs & versions','Exact source material and version.'),('Exact destination','Named receiving chat or resource.'),('Necessary definitions','Terms required to interpret the task.'),('Permitted actions','Actions within granted scope.'),('Constraints','Limits and prohibitions.'),('Unknowns','Absent or unverified information.'),('Completion criteria','Named acceptance checks.'),('Return format','Required output structure.')]
for i,(a,b) in enumerate(fields):
 x=60 if i<5 else 860;y=280+(i%5)*108
 line(x,y,x+690,y,'#B9BFC4');text(x,y+12,f'{i+1:02d} / {a}',23,True);text(x,y+49,b,20)
end(4,'Which of these ten fields do you usually leave implicit?')
#5
start(5,'SCOPE STATES THE WORK. LIMITS BOUND IT.','comparison','04:31–05:41','Permitted actions and constraints answer different questions.')
section(70,300,'PERMITTED','What may happen?','Read the supplied text. Extract the title, schedule, materials, and missing details. Report the inventory in the requested format. These actions establish the task’s authorized scope.',660)
section(870,300,'CONSTRAINTS','What must remain protected?','Do not invent a date, location, organizer, or room number. Preserve source wording where exact extraction is required. Do not browse or change an external destination unless the authorization covers it.',640)
line(70,590,1510,590);text(70,630,'WRITTEN PERMISSIONS STATE SCOPE.',29,True);text(70,687,'Access controls can enforce boundaries. A prompt alone is not an access-control system.',24,width=1400)
end(5,'Write one permitted action and one constraint for the same task.')
#6
start(6,'THE ROOM NUMBER IS UNKNOWN.','practice','07:16–09:40','The Community Workshop example tests preservation of facts and missing information.')
section(70,290,'SOURCE','Community Workshop','Schedule: The workshop starts at 10:00 a.m. on Saturday.\nMaterials: Bring paper and a pencil.\nOpen question: The room number has not been supplied.',690)
section(870,290,'RETURN','Inventory the source','Extract the known title, schedule, and materials. Report the room number as UNKNOWN. Do not infer it from prior workshops. An UNKNOWN label makes missing evidence explicit; it does not guarantee model behavior.',640)
rect(70,640,1450,132);text(95,665,'KNOWN FACTS + EXPLICIT UNKNOWN',29,True);text(95,719,'The inventory can complete even when the source leaves one value unresolved.',23)
end(6,'Which claim would become fabricated if you filled the missing value?')
#7
start(7,'TWO CHATS. ONE HUMAN RELAY.','process','09:40–11:33','Perform the handoff manually so the transport and inspection steps are visible.')
flow([('PREPARE IN CHAT A','Create the read-only inventory request and shared frame.'),('CARRY TO CHAT B','Paste complete source text and the frame.'),('RETURN EVIDENCE','Bring the exact response back for comparison.')],340)
section(80,575,'MANUAL FIRST','Expose each boundary','Choose the receiving chat. Carry the whole payload. State permitted actions. Compare the output with the source. This exercise establishes a process you can later map to automation.',650)
section(860,575,'RECORD','Keep the actual exchange','Save the sent request and returned response. Record what was observed, which checks passed, and what remains unresolved. Agreement between models is not verification.',650)
end(7,'Where could context disappear during your manual relay?')
#8
start(8,'ARRIVAL DOES NOT OPEN THE PACKAGE.','reference','11:39–13:37','State labels describe different claims. Match the evidence to the claim.')
statuses=[('RECEIVED','Payload arrived.'),('READABLE','Required content can be accessed.'),('IMPORTED','Destination acceptance was reported.'),('VERIFIED','Named evidence checks passed; verifier identified.'),('PARTIAL','Required work remains.'),('FAILED','An attempted operation failed.'),('UNKNOWN','Evidence is insufficient.')]
for i,(a,b) in enumerate(statuses):
 y=275+i*77;line(60,y,1540,y,'#B9BFC4');text(80,y+17,a,23,True);text(450,y+17,b,22)
end(8,'What evidence would establish READABLE beyond a visible filename?')
#9
start(9,'OMIT THE SOURCE. OBSERVE THE RESULT.','recovery','13:37–15:17','A separate missing-input attempt teaches recovery rather than imagined success.')
box(70,300,340,130,'SEND FRAME ONLY','Deliberately omit the practice source.');box(610,300,340,130,'RECORD BEHAVIOR','Did it request input, invent content, or return incomplete work?');arrow([(410,365),(610,365)])
box(610,530,340,130,'SUPPLY SOURCE','Repeat the bounded request with the missing text.');arrow([(780,430),(780,530)])
box(1170,530,340,130,'COMPARE AGAIN','Inspect against the actual source; save the recovery record.');arrow([(950,595),(1170,595)])
text(70,730,'Pause dependent work. Independent, authorized work may continue.',27,True,width=1450)
end(9,'What actually happened, and what evidence changed after recovery?')
#10
start(10,'CHANGE THE DELIVERY. KEEP THE CLAIM PRECISE.','case study','15:17–17:18','The reported relay illustrates a format bottleneck; it is not an independently verified archive.')
section(70,280,'REPORTED RELAY','Metadata was not content','The podcast describes a ZIP delivery whose file names were visible while contents were not readable. Individual files improved access. An inaccessible markdown file was later supplied as pasted plain text. These are reported observations from the relay, not proof that every source reached the destination intact.',690)
section(870,280,'WORKFLOW LESSON','Recover the affected step','Identify the precise access gap. Use a readable format within authorized scope. Request destination evidence. An import receipt supports acceptance; it does not establish exhaustive source fidelity. Do not upgrade sampled evidence into a full-document verification claim.',640)
flow([('ZIP METADATA','Received; content access unresolved.'),('INDIVIDUAL FILE','Check actual readability.'),('PASTED TEXT','Recheck affected content.')],655)
end(10,'What claim can you support without assuming full-text fidelity?')
#11
start(11,'UNSUPPORTED IS A ROUTING DECISION.','case study','production amendment','NotebookLM audio generation exposed a limitation during an attempted programmatic action.')
flow([('ATTEMPT','Programmatic audio generation was unsupported.'),('CHECK SCOPE','Confirm new tool, action, and destination authorization.'),('REROUTE','Use the supported web interface.')],325)
section(80,570,'OBSERVED / REPORTED','Describe the actual order','The capability limitation was discovered during an attempted generation. Do not retell it as a pre-action capability check that already happened. Authorized source import was reported successful; full-text fidelity was not independently inspected.',660)
section(870,570,'PROPOSED IMPROVEMENT','Check before affected action','Check capability earlier when practical. Rerouting does not grant authority. Existing authorization may cover the alternative route; obtain additional authorization only when scope expands.',640)
end(11,'Which capability can you check before the next affected action?')
#12
start(12,'AUTOMATE THE LOGISTICS. PRESERVE THE FRAME.','mapping','17:31–19:42','Manual steps correspond to transport, scope enforcement, and acceptance checks.')
maps=[('Choose receiving chat','Destination and tool selection'),('Copy complete source text','Payload transfer'),('State permitted actions','Authorization scope; controls enforce it'),('Compare output to source','Validation against named criteria')]
for i,(a,b) in enumerate(maps):
 y=285+i*130;line(60,y,1540,y,'#B9BFC4');text(80,y+23,a,24,True);arrow([(710,y+50),(815,y+50)]);text(860,y+23,b,23,width=650)
text(70,815,'Run IDs, logs, duplicate detection, and bounded retries require implementation.',21)
end(12,'Which manual step is ready to automate, and what check must survive?')
#13
start(13,'CHOOSE THE MECHANISM FOR THE STEP.','editorial','18:34–19:42 + amendment','Model output and external execution are distinct. Neither transfers command responsibility.')
roles=[('AI','Supports interpretation and probabilistic reasoning. Its fluent output still needs evidence checks.'),('RULES','Evaluate explicit conditions and deterministic logic. Define what happens when a condition is unmet.'),('APIs','Provide interfaces through which authorized tools or systems may act. An interface does not grant permission.'),('RPA','Executes configured interactions. Use it where the task and application behavior suit prescribed execution.')]
for i,(a,b) in enumerate(roles):
 x=70 if i%2==0 else 870;y=290+(i//2)*245
 section(x,y,f'{i+1:02d}',a,b,650)
end(13,'Which step needs interpretation, and which needs prescribed execution?')
#14
start(14,'VERIFY CONTENT. CHECK RELEASE SCOPE.','decision','19:28–21:10 + amendment','Evidence acceptance and external distribution are separate checkpoints.')
box(80,330,330,120,'CHECK CONTENT','Compare source anchors and completion criteria.');diamond(560,315,230,150);text(602,350,'Checks',24,True);text(585,395,'passed?',24);arrow([(410,390),(560,390)])
box(1000,330,480,120,'VERIFIED','Record named checks, verifier, and limitations.');arrow([(790,390),(1000,390)]);text(850,356,'YES',18,True)
arrow([(675,465),(675,545)],'#B34700');text(530,570,'NO / UNKNOWN: hold for review',22,True,col='#B34700')
text(80,670,'VERIFIED ALONE DOES NOT AUTHORIZE RELEASE.',31,True)
text(80,729,'Confirm authorization covering the artifact, action, and destination. Existing explicit authorization may already cover release. Evaluate visual and content acceptance separately.',23,width=1400)
end(14,'Could a beautiful artifact still fail its content acceptance checks?')
#15
start(15,'SUBMIT EVIDENCE. KEEP THE UNKNOWNS.','closing','19:47–22:00','Agreement between models is not proof of correctness.')
items=['The completed shared frame','The exact request sent','The exact response returned','Source comparison and named checks','Missing-input recovery record','Unresolved questions and limitations']
for i,a in enumerate(items):text(80,285+i*78,f'{i+1:02d} / {a}',25,True)
section(870,290,'NEXT','From rehearsal to integration','First explain and perform the process. Then assign suitable steps to tools and automation. Preserve task boundaries, authorization, and evidence requirements. A manual rehearsal establishes observations within its tested environment; it does not prove production behavior.',630)
text(870,660,'A consensus can repeat the same mistake.',29,True,width=630)
text(870,742,'Check the source. Record the evidence. Resolve only what the evidence supports.',23,width=630)
end(15,'What remains unknown before you automate this handoff?')
c.save()
css='*{box-sizing:border-box}body{margin:0;background:#fff;font-family:Arial,Helvetica,sans-serif;color:#20252a}.page{position:relative;width:1632px;height:1056px;background:#fff;overflow:hidden;break-after:page}.diagram{position:absolute;inset:0;width:100%;height:100%}.copy{position:absolute;line-height:1.3;white-space:pre-wrap;margin:0}.story{position:absolute;object-fit:contain}@page{size:17in 11in;margin:0}'
(P/'styles.css').write_text(css)
(P/'BOSS_Podcast_Story_Deck.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>BOSS Day Zero podcast companion</title><style>'+css+'</style><body>'+''.join(pages)+'</body></html>')
(P/'STORY_MAP.md').write_text('\n'.join(outline))
(P/'REVIEW.md').write_text('DraftDeck trial candidate — awaiting human review.\nSource: supplied 22-minute voiceover transcript in this conversation, plus current Day Zero amendments. This is a 15-page companion, not a new 60-minute script. Narration is adapted, not reproduced verbatim. The supplied transcript omits a short part of the manual relay around 10:49; page 7 uses the established manual-handoff doctrine rather than inventing missing spoken text. The Jonathan relay is explicitly reported; unsupported programmatic audio capability is described as discovered during attempted generation. Historical dates, salaries, market and zero-error claims excluded.\n17 x 11 landscape, mixed page types. Live HTML text and separate SVG geometry / raster opener art. PDF independently composed from same coordinates, not browser export. No PowerPoint. Browser rendering, print on paper and Canva import untested. No external release.\n')
