"""BOSS Day Zero editorial deck builder v0.4.

Single content model drives three renderers:
  1. PDF review rendition (ReportLab, coordinate-composed, not a browser export)
  2. Geometry SVGs (separate diagram layer per slide)
  3. Semantic token-based HTML (headings, landmarks, components, responsive)

Governing contracts: design-system/editorial-components.md,
design-system/tokens/tokens.css, doctrine/composition-standard.md.
v0.4 changes: Slide 6 SOURCE block carries the exact workshop source only
(commentary separated); repeated filler paragraphs removed; each of the ten
editorial features renders through its own component; slide 4 fields are
numbered 01-10; slides 7/9/14/15 use dedicated practice, recovery,
checkpoint, and submission components; HTML uses semantic headings and a
reflow layout below the declared breakpoint.
"""
from pathlib import Path
import ast, json, re, base64, shutil, html as htmllib
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = Path(__file__).resolve().parent          # source/editorial-deck
SRC = HERE.parent                                # source/
ROOT = HERE.parents[3]                           # repo root
base = (SRC/'process-comp/build.py').read_text()
base = base[:base.index('line(50,40,1582,40)')]
base = base.replace("P=Path(__file__).parent; W,H=1632,1056", "P=Path('editorial-deck'); W,H=1632,1056")
base = base.replace("P/'DraftDeck_Process_Comp.pdf'", "P/'BOSS_Day_Zero_Editorial_v0.4.pdf'")
exec(base)  # provides: c, svg, texts, line, rect, diamond, text, arrow, box, W, H, P

TOKENS = (ROOT/'design-system/tokens/tokens.css').read_text()

# ---------- content model ----------
old = ast.parse((SRC/'podcast-deck/build.py').read_text()); slides = {}; cur = 0
for node in old.body:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        q = node.value; name = getattr(q.func, 'id', '')
        if name == 'start':
            a = [ast.literal_eval(x) for x in q.args]
            cur = a[0]; slides[cur] = {'title': a[1], 'kind': a[2], 'time': a[3], 'lead': a[4], 'blocks': []}
        elif name == 'section' and cur:
            a = [ast.literal_eval(x) for x in q.args]
            slides[cur]['blocks'].append((a[2], a[3], a[4]))

# Low-density page copy (teaching blocks; verbatim source material is isolated per slide).
low = {
1: [('FRAME', 'A bounded task travels with its source.', 'Identify what enters the workflow, who may act, where the result belongs, and what evidence establishes completion. A confident answer is not a receipt. The shared frame makes those requirements explicit before you inspect a returned result.'),
    ('EVIDENCE', 'Keep three claims separate.', 'Arrival records delivery. Inspection compares content with criteria. Release requires authorization covering the artifact, action, and destination. Begin manually so each boundary is visible; automate suitable steps after the process is understood.')],
3: [('SENDER', 'Prepare the agreement.', 'Supply the source, identified version, objective, permitted actions, constraints, and return format.'),
    ('PAYLOAD', 'Carry actual context.', 'A second chat does not inherit the first chat\u2019s memory. The frame and source must travel together.'),
    ('RECEIVER', 'Confirm the boundary.', 'The frame does not create access or capability. Confirm readability and authorization for the affected task. Missing required source pauses dependent work; independent authorized work can continue.')],
7: [('PREPARE', 'Draft in Chat A.', 'Create a read-only inventory request using the shared frame and practice source.'),
    ('TRANSFER', 'Carry to Chat B.', 'Paste the complete frame and source. Save the exact request you sent. Do not assume context transfers automatically.'),
    ('COMPARE', 'Bring back the evidence.', 'Return the exact response and inspect it against the source. Record checks and unknowns. Keep the source comparison as part of the evidence package rather than treating agreement between chats as correctness.')],
9: [('OMIT', 'Send the frame without the source.', 'Use a separate attempt. Observe whether the receiver requests input, fabricates details, or returns incomplete work. These are possible behaviors, not guaranteed results.'),
    ('RECOVER', 'Supply what is required.', 'Record the actual response. Supply the missing practice source and repeat the bounded request.'),
    ('RECHECK', 'Compare again.', 'Inspect the new response against the source. Recover affected work without duplicating completed steps. Preserve the missing-input attempt and recovery record.')],
11: [('ATTEMPT', 'A capability gap was discovered.', 'Programmatic Audio Overview generation was unsupported during an attempted action. This is a reported production example, not an observed pre-action capability check.'),
     ('SCOPE', 'Check the alternative route.', 'Confirm that existing authorization covers the new tool, action, and destination. Additional authorization is needed where scope expands.'),
     ('REROUTE', 'Use the supported interface.', 'The activity moved to the web interface. Checking capability earlier is the proposed improvement. Reported import success does not establish full-text fidelity.')],
14: [('VERIFY', 'Compare content with criteria.', 'Identify the source anchors, acceptance checks, verifier, and limitations. If checks do not pass or evidence is insufficient, hold the affected result for review.'),
     ('AUTHORIZE', 'Check release scope.', 'VERIFIED does not grant permission to deploy, publish, or forward. Existing explicit authorization may already cover release; additional authorization is needed only when scope expands.'),
     ('RELEASE', 'Record the actual action.', 'Check the artifact, action, and exact destination. Evaluate visual and content acceptance separately. A polished artifact can still fail content checks.')]
}
# Medium-copy sections: one explicit teaching relationship per slide.
extra = {
2: ('BOUNDARY', 'Trace one handoff', 'Suppose a receiving system returns a clean workshop summary. The title and materials match, but the room number was supplied without a source. The response may look useful while failing the preservation rule. The governor identifies the deviation using the frame, not the model\u2019s tone. Keep known facts separate from interpretations and unknowns. Decide which action can continue, which needs recovery, and what evidence would resolve the gap. This is the difference between getting an answer and establishing an inspectable result.'),
5: ('ENFORCEMENT', 'Separate instructions from controls', 'Written permissions describe what the executor is allowed to do. Active access controls can enforce limits in a connected system. Neither guarantees correct content. An executor might have a tool available but lack authorization for the requested destination. Another might be authorized yet unable to access the required source. Inspect these conditions independently. Before changing a document, sending a payload, or publishing a result, check scope for that specific action. Keep the returned evidence tied to the same objective and source version used in the request.'),
6: ('ACCEPTANCE', 'Use the source as the comparator', 'The missing room value is not the same as a missing source document. The supplied document contains enough evidence to inventory the known details and explicitly report the absent field. If the document itself is missing, the executor cannot extract its facts. Pause that dependent action and request the payload. Define completion as the required inventory and explicit unknown, not a fully populated schedule. Do not invent a calendar date from Saturday. Preserve source wording where the request requires exact extraction, and save the comparison that establishes acceptance.'),
10: ('CLAIM', 'Match the receipt to its scope', 'The locked-package analogy explains access, not proof of correctness. Receiving a package establishes arrival. Reading its label establishes metadata visibility. Opening it establishes some access to contents. Inspection must still compare those contents with the expected source. A record that one document was accepted does not establish that every document was imported. Name which source was checked, what was visible, and what remains unknown. Preserve recovery details so later automation can handle the same format boundary without repeating already completed work.'),
12: ('IMPLEMENTATION', 'Keep acceptance checks attached', 'Automating transfer changes the transport mechanism, not the required evidence. A destination selection becomes a tool or API route. Copying becomes payload transport. Permission statements define scope; access controls may enforce it. Comparison becomes a validation check. Run identifiers, duplicate detection, bounded retries, and logs require implementation rather than appearing automatically. A retry should address the affected operation without repeating successful writes. Keep the source version and returned result associated with the same run. When evidence is incomplete, report the limit instead of silently upgrading the status.'),
13: ('SELECTION', 'Assign the step deliberately', 'A workflow may combine all four mechanisms or use only the ones required. Inspect the result against the same acceptance criteria in every case. Model output is not an external action; successful execution is not proof of source fidelity.')
}
# Dense reference pages: explicit entries, not a wall of undifferentiated text.
fields = [('Run ID', 'Give each execution a unique reference so the request, source, returned result, and recovery record can be associated. The identifier supports traceability; it does not prove correctness.'),
('Observable objective', 'State a result that can be inspected. For the workshop example, extract title, schedule, materials, and unknowns from the supplied source. Avoid objectives whose completion depends only on a confident claim.'),
('Actual inputs & versions', 'Identify the source material and version used for the run. Pin a version where supported; record limitations where it cannot be pinned. A filename alone does not establish readable content.'),
('Exact destination', 'Name the receiving chat or resource precisely. Authorization applies to the affected action and destination. Moving the payload to another interface does not automatically authorize its receipt, modification, or release.'),
('Necessary definitions', 'Define terms needed to interpret the task. Inventory means reporting the required source facts and missing details within the stated preservation rule. Definitions prevent the receiver from silently choosing a different meaning.'),
('Permitted actions', 'State the work that falls within scope, such as reading the source and returning an inventory. Capability is separate: having a tool available does not authorize its use for every action.'),
('Constraints', 'Specify prohibitions and preservation requirements. Do not invent a room number, date, location, or organizer. Do not silently correct extracted wording when the task requires exact source preservation.'),
('Unknowns', 'Record absent, unreadable, or unverified information. An unknown room value may remain explicit while the inventory completes. Missing required source content pauses the action that depends on that source.'),
('Completion criteria', 'Name the acceptance checks that establish the result. Compare title, schedule, materials, and unknowns with the source. Record the verifier and limitations. Passing a visual review does not pass a content check.'),
('Return format', 'State the required structure of the returned result. Format compliance is visible; content fidelity still requires the comparison named in the completion criteria.')]
states = [('RECEIVED', 'The payload arrived at the destination. A receipt supports this arrival claim. It does not prove that required contents are readable, that the source was preserved, or that the requested task completed. Record what actually arrived and identify the destination.'),
('READABLE', 'The executor can access the required content. Reading a filename is metadata visibility, not content access. Ask for evidence appropriate to the task. If only some portions are visible, record that limit rather than treating it as exhaustive source access.'),
('IMPORTED', 'Destination acceptance was reported. This status applies when content is accepted into a receiving resource. It does not automatically establish complete fidelity. A reported successful import needs destination evidence before stronger claims about preservation or correctness can be made.'),
('VERIFIED', 'The named evidence checks passed and the verifier is identified. Compare the output with source anchors and completion criteria. Keep the verification scope explicit. Passing checks does not authorize external release; authorization must cover the artifact, action, and destination.'),
('PARTIAL', 'Required work remains. Interruption, unsupported capability, unfinished extraction, or incomplete verification may leave a task partial without an attempted operation failure. Identify completed work and affected work separately, then recover only the portion that still requires attention.'),
('FAILED', 'An attempted operation failed. Record which action was attempted, what failure was observed, and what evidence supports that description. Do not label missing information as an execution failure. Recovery may reroute the operation within existing authorization or require expanded scope.'),
('UNKNOWN', 'Evidence is insufficient to establish the claim. This may describe an absent room number or unverified destination content. It is distinct from FAILED. Do not substitute fluency or agreement between models for missing facts.')]
evidence = [('Shared frame', 'Submit the actual ten-field agreement used for the run: objective, source identifiers, destination, permitted actions, constraints, unknowns, acceptance checks, and return format. This is the comparator for the handoff, not a retrospective claim that everything went well.'),
('Sent request', 'Keep the exact request carried to the receiving system, including the source payload actually supplied. A planned request is not evidence of delivery. Identify intentional missing-input attempts separately.'),
('Returned response', 'Save the exact response returned by the receiving executor. Do not replace it with a polished summary. Identify claims from the source, interpretations added by the model, and missing information.'),
('Source comparison', 'Record the checks performed against the identified source version: verifier, acceptance criteria, observed results. Separate visual acceptance from content acceptance.'),
('Recovery record', 'Describe the missing input, unsupported capability, or failed operation actually observed. Record what changed and what was rechecked. Recover affected steps without repeating successful work.'),
('Unresolved questions', 'List what remains unknown and what evidence could resolve it. A manual rehearsal does not prove production behavior; future integrations need their own checks. Agreement between models is not proof of correctness.')]

# Slide 6: exact workshop source, kept separate from commentary (v0.4 fix).
WORKSHOP_SOURCE = ('Title: Community Workshop\n'
                   'Schedule: The workshop starts at 10:00 a.m. on Saturday.\n'
                   'Materials: Bring paper and a pencil.\n'
                   'Open question: The room number has not been supplied.')

# Structured editorial features: component id + typed payload (contract: editorial-components.md).
features = {
1:  ('loading-dock', {'scenario': 'A parcel arrives sealed at the receiving dock.', 'purpose': 'Establish that arrival, readability, and correct contents are three separate claims.', 'classification': 'Illustrative scenario'}),
2:  ('pause-consider', {'question': 'Which part of your last AI response came from the source, and which part was inferred?'}),
3:  ('carry-forward', {'principle': 'Context must travel.', 'action': 'Attach the source and frame to the receiving request.'}),
4:  ('working-agreement', {'fields': ['03 Actual inputs & versions', '04 Exact destination'], 'note': 'Selected-field strip. It does not replace the ten-field agreement on this page.'}),
5:  ('choose-route', {'condition': 'A tool is available, but destination authorization is unclear.', 'branches': [('Authorization confirmed', 'Proceed within stated scope.'), ('Authorization unclear', 'Hold the affected action; resolve scope first.')]}),
6:  ('inspect-payload', {'source': WORKSHOP_SOURCE, 'candidate': 'Room 204', 'finding': 'Unsupported addition. The source does not supply a room number; preserve UNKNOWN.'}),
7:  ('try-handoff', {'task': 'Carry the complete workshop source and frame to a second chat. Save the exact request and response.', 'record_lines': 3}),
8:  ('evidence-window', {'claim': 'VERIFIED', 'support': 'Named acceptance checks, observed results, identified verifier.', 'scope': 'The checks named on this page only.', 'limitations': 'Verification does not grant release; scope is recorded, not assumed.'}),
9:  ('recovery-record', {'observed': 'Source omitted from the request.', 'action': 'Supply the practice source; repeat the bounded request.', 'evidence': 'Compare the new response; retain both attempts.'}),
10: ('evidence-window', {'claim': 'Relay delivered the sources', 'support': 'Filenames visible at the destination.', 'scope': 'Metadata access only.', 'limitations': 'Readability of contents not established by a file listing.'}),
11: ('choose-route', {'condition': 'Programmatic generation unsupported during an attempted action.', 'branches': [('Within existing authorization', 'Reroute to the supported web interface.'), ('Scope expands', 'Obtain additional authorization first.')]}),
12: ('carry-forward', {'principle': 'Automate transport and preserve acceptance checks.', 'action': 'Identify the check each transfer must carry.'}),
13: ('pause-consider', {'question': 'Does this step need interpretation, a rule, an interface, or configured execution? What evidence tests the result?'}),
14: ('before-release', {'checkpoints': [('Checkpoint 1 — Acceptance', 'Content and visual acceptance are evaluated separately and both recorded.'), ('Checkpoint 2 — Authorization', 'Confirm authorization covers this artifact, action, and exact destination. VERIFIED alone does not release.')]}),
15: ('try-handoff', {'task': 'Submit the six-item evidence package: frame, request, response, comparison, recovery record, unresolved questions.', 'record_lines': 3}),
}
levels = {i: ('low' if i in low else 'high' if i in (4, 8, 15) else 'medium') for i in range(1, 16)}
LAYOUT = {1: 'opener', 2: 'duo', 3: 'payload-flow', 4: 'reference-ten', 5: 'compare',
          6: 'inspect', 7: 'steps', 8: 'reference-seven', 9: 'recovery', 10: 'case',
          11: 'route', 12: 'map', 13: 'quad', 14: 'checkpoints', 15: 'checklist'}
prompts = {1:'Where does your workflow trust confidence without evidence?',2:'Which boundary makes your next request inspectable?',3:'What context must travel with the payload?',4:'Which shared-frame field do you usually leave implicit?',5:'Write one permitted action and one constraint.',6:'What would you preserve as UNKNOWN?',7:'Where could context disappear in your manual relay?',8:'What evidence supports the status you assigned?',9:'What changed after you supplied the missing input?',10:'Which claim can you support from the retrieved evidence?',11:'Which capability can you check before the affected action?',12:'Which acceptance check must survive automation?',13:'Which mechanism fits your next step?',14:'Does release authorization cover this artifact and destination?',15:'What remains unresolved before the next integration?'}

def slide_blocks(n):
    """Return the teaching blocks for slide n from the content model."""
    if levels[n] == 'low':
        return low[n]
    if levels[n] == 'high':
        entries = fields if n == 4 else states if n == 8 else evidence
        return [(a, '', b) for a, b in entries]
    blocks = slides[n]['blocks'][:2]
    if n == 12:
        return [('ROUTE', 'Select the receiver', 'Choosing a receiving chat selects the destination and tool route. Carry the source as an identified payload. The frame defines objective and permitted actions; it does not create access, memory, or capability. Check what the receiver can actually use first.'),
                ('CHECK', 'Preserve scope and acceptance', 'Stating permitted actions defines authorization scope; access controls may enforce it. Comparing returned output with the source is validation against named criteria. Automated transport must preserve the same distinctions between receipt, readability, acceptance, and verification.')]
    if n == 13:
        blocks = [('REASON', 'AI and explicit rules', 'AI supports interpretation and probabilistic reasoning about supplied content. Rules evaluate explicit conditions. Both may work within one activity, but acceptance checks must remain inspectable. Fluent output is not evidence that a system action occurred.'),
                  ('ACT', 'APIs and configured execution', 'APIs let authorized systems act; RPA executes configured interactions. Choose the mechanism that fits the task. Availability does not grant authority. Record the action, destination, and returned evidence before assigning a stronger status.')]
    if n == 6:
        # Exact source stays verbatim and unmixed; commentary is a separate block.
        blocks = [('SOURCE', 'Community Workshop — exact source', WORKSHOP_SOURCE),
                  ('RETURN', 'Inventory the source', 'Extract the known title, schedule, and materials. Report the room number as UNKNOWN. Do not infer it from prior workshops. An UNKNOWN label makes missing evidence explicit; it does not guarantee model behavior.')]
    return blocks[:2] + [extra[n]]

# ---------- Consulting visuals (executive exhibits; token colors only) ----------
# One decision-grade exhibit per slide where it aids the teaching point.
# These break up the sequence diagrams and give the deck standard
# consulting visual grammar: MECE tree, chevron flow, loop, decision tree,
# staircase, 2x2 matrix, evidence funnel.
INK = '#20252A'; ACC = '#B34700'; RAIL = '#B9BFC4'; MUT = '#697177'; GRID = '#DEDEDE'

def _svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img">{body}</svg>')

def _t(x, y, s, size=15, bold=False, col=INK, anchor='start', mono=False):
    ff = "Courier New" if mono else "Arial"
    fw = ' font-weight="700"' if bold else ''
    return (f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}"'
            f' fill="{col}" text-anchor="{anchor}"{fw}>{s}</text>')

def _box(x, y, w, h, stroke=INK, sw=1.5, fill='white'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def _ln(x1, y1, x2, y2, col=INK, sw=1.5, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{col}" stroke-width="{sw}"{d}/>'

def _ah(x, y, col=INK, angle=0):
    # small filled arrowhead pointing right, rotated by angle deg around (x,y)
    return (f'<path d="M{x},{y} l-11,-5 l0,10 Z" fill="{col}" '
            f'transform="rotate({angle} {x} {y})"/>')

def visual_mece():
    # Slide 3: MECE decomposition of the ten-field working agreement.
    b = [_t(350, 34, 'THE WORKING AGREEMENT', 17, True, INK, 'middle'),
         _t(350, 56, 'ten fields / three branches', 12, False, MUT, 'middle', True),
         _box(230, 70, 240, 46), _t(350, 99, 'EVERY FIELD, EXACTLY ONE BRANCH', 12, True, ACC, 'middle', True)]
    branches = [
        ('01 IDENTIFY THE RUN', ['01 / Run ID', '02 / Observable objective', '03 / Actual inputs & versions']),
        ('02 BOUND THE WORK', ['04 / Exact destination', '05 / Necessary definitions', '06 / Permitted actions', '07 / Constraints']),
        ('03 CLOSE THE LOOP', ['08 / Unknowns', '09 / Completion criteria', '10 / Return format'])]
    for i, (title, leaves) in enumerate(branches):
        x = 20 + i * 230
        b.append(_ln(350, 116, 350, 150) if i == 1 else _ln(350, 150, x + 105, 150))
        b.append(_ln(x + 105, 150, x + 105, 168))
        b.append(_ln(x + 105, 208, x + 105, 224 + (len(leaves) - 1) * 52))  # trunk behind leaves
        b.append(_box(x, 168, 210, 40, ACC))
        b.append(_t(x + 105, 194, title, 13, True, ACC, 'middle', True))
        for j, leaf in enumerate(leaves):
            y = 224 + j * 52
            b.append(_box(x, y, 210, 40, RAIL))
            b.append(_t(x + 12, y + 26, leaf, 13))
    b.append(_t(350, 486, 'MECE: branches do not overlap; together they cover the agreement.', 13, False, MUT, 'middle'))
    return _svg(700, 500, ''.join(b))

def visual_chevron():
    # Slide 7: handoff as a chevron flow (replaces plain sequence).
    steps = [('01', 'PREPARE', 'Draft the bounded request in Chat A'),
             ('02', 'TRANSFER', 'Carry frame and source to Chat B'),
             ('03', 'COMPARE', 'Inspect the returned response')]
    b = []
    for i, (num, name, sub) in enumerate(steps):
        x = 20 + i * 500
        pts = f'{x},30 {x+400},30 {x+460},90 {x+400},150 {x},150 {x+60},90'
        b.append(f'<polygon points="{pts}" fill="white" stroke="{INK}" stroke-width="1.5"/>')
        b.append(_t(x + 90, 70, num, 16, True, ACC, 'start', True))
        b.append(_t(x + 90, 100, name, 19, True))
        b.append(_t(x + 90, 126, sub, 14, False, MUT))
    b.append(_t(740, 190, 'Evidence moves with the payload at every stage; no stage is skipped.', 13, False, MUT, 'middle'))
    return _svg(1480, 210, ''.join(b))

def visual_loop():
    # Slide 9: recovery as a closed loop, not a straight line.
    b = [_t(350, 60, 'RECOVERY LOOP', 17, True, INK, 'middle'),
         _t(350, 82, 'run until the comparison passes', 12, False, MUT, 'middle', True)]
    nodes = [('OMIT', 'frame without source', 350, 190),
             ('RECOVER', 'supply the payload', 560, 400),
             ('RECHECK', 'compare against source', 140, 400)]
    for name, sub, cx, cy in nodes:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="72" fill="white" stroke="{INK}" stroke-width="1.5"/>')
        b.append(_t(cx, cy - 4, name, 16, True, ACC, 'middle', True))
        b.append(_t(cx, cy + 20, sub, 11, False, MUT, 'middle'))
    arcs = [(405, 241, 505, 349, 45), (499, 451, 201, 451, 180), (195, 349, 299, 241, 315)]
    for x1, y1, x2, y2, a in arcs:
        b.append(_ln(x1, y1, x2, y2, ACC))
        b.append(_ah(x2, y2, ACC, a))
    b.append(_t(350, 330, 'each pass is', 13, False, MUT, 'middle'))
    b.append(_t(350, 350, 'recorded', 13, True, INK, 'middle'))
    return _svg(700, 500, ''.join(b))

def visual_decision():
    # Slide 11: routing decision tree (consulting decision grammar).
    b = [_t(350, 40, 'ROUTING DECISION', 17, True, INK, 'middle')]
    b.append(f'<polygon points="350,70 500,140 350,210 200,140" fill="white" stroke="{INK}" stroke-width="1.5"/>')
    b.append(_t(350, 132, 'CAPABILITY', 15, True, INK, 'middle', True))
    b.append(_t(350, 154, 'supported?', 14, False, INK, 'middle'))
    b.append(_ln(500, 140, 600, 140)); b.append(_ah(600, 140))
    b.append(_t(545, 128, 'YES', 13, True, INK, 'middle'))
    b.append(_box(610, 105, 300, 70)); b.append(_t(625, 135, 'PROCEED', 14, True, INK, 'start', True))
    b.append(_t(625, 158, 'within stated scope', 13, False, MUT))
    b.append(_ln(350, 210, 350, 270, ACC)); b.append(_ah(350, 270, ACC, 90))
    b.append(_t(365, 250, 'NO', 13, True, ACC))
    b.append(f'<polygon points="350,270 520,340 350,410 180,340" fill="white" stroke="{ACC}" stroke-width="1.5"/>')
    b.append(_t(350, 332, 'WITHIN EXISTING', 14, True, ACC, 'middle', True))
    b.append(_t(350, 352, 'authorization?', 13, False, INK, 'middle'))
    b.append(_ln(520, 340, 600, 340)); b.append(_ah(600, 340))
    b.append(_t(555, 328, 'YES', 13, True, INK, 'middle'))
    b.append(_box(610, 305, 320, 70)); b.append(_t(625, 335, 'REROUTE', 14, True, INK, 'start', True))
    b.append(_t(625, 358, 'use the supported interface', 13, False, MUT))
    b.append(_ln(350, 410, 350, 460, ACC)); b.append(_ah(350, 460, ACC, 90))
    b.append(_t(180, 442, 'NO / SCOPE EXPANDS', 13, True, ACC, 'middle'))
    b.append(_box(180, 460, 520, 60, ACC))
    b.append(_t(350, 497, 'OBTAIN ADDITIONAL AUTHORIZATION FIRST', 14, True, ACC, 'middle', True))
    return _svg(960, 560, ''.join(b))

def visual_staircase():
    # Slide 12: automation maturity ascent.
    steps = [('01 MANUAL RELAY', 'every boundary visible; slow but inspectable'),
             ('02 ASSISTED TRANSFER', 'tools carry the payload; checks still manual'),
             ('03 AUTOMATED PIPELINE', 'acceptance checks attached to every transfer')]
    b = []
    for i, (name, sub) in enumerate(steps):
        x = 40 + i * 500; y = 260 - i * 80; h = 80 + i * 80
        b.append(_box(x, y, 440, h))
        b.append(_t(x + 20, y + 32, name, 16, True, ACC if i == 2 else INK, 'start', True))
        b.append(_t(x + 20, y + 56, sub, 13, False, MUT))
    b.append(_ln(60, 250, 1440, 60, ACC, 1.5, '6 5'))
    b.append(_ah(1440, 60, ACC, -14))
    b.append(_t(1420, 44, 'automation rises; the frame does not change', 13, False, ACC, 'end'))
    return _svg(1480, 352, ''.join(b))

def visual_matrix():
    # Slide 13: 2x2 mechanism selection matrix.
    b = [_t(330, 36, 'MECHANISM SELECTION', 16, True, INK, 'middle'),
         _ln(80, 440, 620, 440), _ah(620, 440),
         _ln(80, 440, 80, 70), _ah(80, 70, INK, -90),
         _t(350, 468, 'TASK LOGIC:  DETERMINISTIC  \u2192  JUDGMENT', 12, True, MUT, 'middle', True),
         f'<text x="34" y="260" font-family="Courier New" font-size="12" font-weight="700" fill="{MUT}" text-anchor="middle" transform="rotate(-90 34 260)">ACTS ON EXTERNAL SYSTEMS</text>',
         _ln(350, 70, 350, 440, RAIL, 1, '4 4'), _ln(80, 255, 620, 255, RAIL, 1, '4 4')]
    quads = [('EXPLICIT RULES', 'condition has a defined test', 215, 170),
             ('AI INTERPRETATION', 'reasoning over supplied content', 485, 170),
             ('API / INTERFACE', 'authorized system communicates or acts', 215, 355),
             ('CONFIGURED EXECUTION', 'prescribed interactions in the application', 485, 355)]
    for name, sub, cx, cy in quads:
        b.append(_t(cx, cy - 8, name, 14, True, INK, 'middle'))
        b.append(_t(cx, cy + 14, sub, 12, False, MUT, 'middle'))
    b.append(_t(330, 520, 'Choose per step; the acceptance check stays the same in every quadrant.', 13, False, MUT, 'middle'))
    return _svg(660, 540, ''.join(b))

def visual_funnel():
    # Slide 15: evidence package narrows to one release decision.
    lv = [('06 EVIDENCE ITEMS', 'frame \u00b7 request \u00b7 response \u00b7 comparison \u00b7 recovery \u00b7 unknowns', 620),
          ('03 VERIFIED CLAIMS', 'arrival \u00b7 content fidelity \u00b7 authorization scope', 420),
          ('01 RELEASE DECISION', '', 300)]
    b = []
    for i, (name, sub, w) in enumerate(lv):
        y = 30 + i * 140; x = 350 - w / 2
        w2 = lv[i + 1][2] if i < 2 else 180
        pts = f'{x},{y} {x + w},{y} {350 + w2 / 2},{y + 110} {350 - w2 / 2},{y + 110}'
        b.append(f'<polygon points="{pts}" fill="white" stroke="{INK}" stroke-width="1.5"/>')
        b.append(_t(350, y + 55, name, 15, True, ACC if i == 2 else INK, 'middle', True))
        if sub:
            b.append(_t(350, y + 80, sub, 12, False, MUT, 'middle'))
    b.append(_ln(350, 450, 350, 484, ACC)); b.append(_ah(350, 484, ACC, 90))
    b.append(_t(350, 512, 'Nothing advances without its record.', 13, True, ACC, 'middle'))
    return _svg(700, 530, ''.join(b))

VISUALS = {3: ('mece', 'Working agreement decomposed MECE into three branches covering ten fields', visual_mece),
           7: ('chevron', 'Handoff chevron flow: prepare, transfer, compare', visual_chevron),
           9: ('loop', 'Recovery loop: omit, recover, recheck until comparison passes', visual_loop),
           11: ('decision', 'Routing decision tree with authorization branches', visual_decision),
           12: ('staircase', 'Automation maturity staircase: manual, assisted, automated', visual_staircase),
           13: ('matrix', 'Two-by-two mechanism selection matrix', visual_matrix),
           15: ('funnel', 'Evidence funnel: six items to three claims to one decision', visual_funnel)}

def visual_html(n):
    if n not in VISUALS: return ''
    kind, label, fn = VISUALS[n]
    return (f'<figure class="visual visual-{kind}" role="img" aria-label="{E(label)}">{fn()}</figure>')

def appendix_pdf():
    """Final PDF page: all consulting exhibits in one index (review rendition)."""
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF as _rpdf
    import io
    c.scale(.75, .75)
    line(50, 40, 1582, 40); text(50, 53, 'BOSS / BIOSCILLATE OPERATING SYSTEM BY SEVEN', 13)
    text(1200, 53, 'APPENDIX', 13)
    text(50, 102, 'CONSULTING EXHIBITS.', 44, True)
    text(50, 171, 'Decision-grade visuals referenced by the deck: one exhibit per teaching point.', 22, width=1490)
    cellw, cellh = 730, 205
    for i, n in enumerate(sorted(VISUALS)):
        kind, label, fn = VISUALS[n]
        drawing = svg2rlg(io.BytesIO(fn().encode()))
        sc = min(cellw / drawing.width, (cellh - 26) / drawing.height)
        x = 76 + (i % 2) * 770; y = 240 + (i // 2) * cellh
        c.saveState(); c.translate(x, H - y - drawing.height * sc); c.scale(sc, sc)
        _rpdf.draw(drawing, c, 0, 0)
        c.restoreState()
        text(x, y + cellh - 18, f'SLIDE {n:02d} / {kind.upper()}', 12, True, col='#B34700')
    c.showPage()

# ---------- PDF + geometry renderer (coordinate-composed review rendition) ----------
pages_html = []; manifest = []
artpath = SRC/'podcast-deck/logistics-art.png'

def feature_pdf(n, label, payload):
    """Bottom band: component name + typed payload summary (review rendition)."""
    line(50, 870, 1582, 870); line(50, 885, 50, 977, '#B34700')
    name = label.replace('-', ' ').upper()
    text(72, 886, name, 15, True, col='#B34700')
    if label == 'pause-consider': body = payload['question']
    elif label == 'carry-forward': body = 'Principle: %s Next action: %s' % (payload['principle'], payload['action'])
    elif label == 'working-agreement': body = ' | '.join(payload['fields']) + '. ' + payload['note']
    elif label == 'choose-route': body = payload['condition'] + ' ' + ' / '.join(f'{k}: {v}' for k, v in payload['branches'])
    elif label == 'inspect-payload': body = 'SOURCE (exact): ' + payload['source'].replace('\n', ' ') + '  CANDIDATE: ' + payload['candidate'] + '  FINDING: ' + payload['finding']
    elif label == 'try-handoff': body = payload['task']
    elif label == 'evidence-window': body = 'Claim: %s. Support: %s Scope: %s Limitations: %s' % (payload['claim'], payload['support'], payload['scope'], payload['limitations'])
    elif label == 'recovery-record': body = 'Observed: %s Action: %s Evidence: %s' % (payload['observed'], payload['action'], payload['evidence'])
    elif label == 'before-release': body = '  '.join('%s: %s' % (a, b) for a, b in payload['checkpoints'])
    else: body = payload.get('scenario', '') + ' ' + payload.get('purpose', '') + ' [' + payload.get('classification', '') + ']'
    text(72, 920, body, 17, width=1450)

def finish_pdf(n):
    global svg, texts
    label, payload = features[n]
    feature_pdf(n, label, payload)
    line(72, 984, 1582, 984, '#B9BFC4')
    text(50, 1015, f'BOSS / DAY ZERO / {levels[n].upper()} COPY / {n:02d} OF 15 / REVIEW CANDIDATE', 12)
    art = '<svg xmlns="http://www.w3.org/2000/svg" width="1632" height="1056" viewBox="0 0 1632 1056">' + ''.join(svg) + '</svg>'
    (P/f'geometry-{n:02d}.svg').write_text(art)
    c.showPage()
    if n < 15: c.scale(.75, .75)

def wordcount(blocks): return sum(len(re.findall(r"\S+", ' '.join(b))) for b in blocks)

for n in range(1, 16):
    svg = []; texts = []; s = slides[n]; level = levels[n]
    line(50, 40, 1582, 40); text(50, 53, 'BOSS / BIOSCILLATE OPERATING SYSTEM BY SEVEN', 13); text(1200, 53, f'{level.upper()} / {n:02d}', 13)
    size = 44
    while stringWidth(s['title'], 'CopyBold', size) > 1520: size -= 1
    text(50, 102, s['title'], size, True); text(50, 171, s['lead'], 22, width=1490)
    if level != 'high' and n != 1:
        text(50, 232, 'READING GUIDE / Connectors show topic order, not automatic execution.', 13, col='#697177')
    blocks = slide_blocks(n)
    if level == 'low':
        if n == 1:
            c.drawImage(ImageReader(str(artpath)), 60, H-265-395, width=1512, height=395, preserveAspectRatio=True, anchor='c', mask='auto')
            for i, (a, b, body) in enumerate(blocks):
                x = 60 + i*800; text(x, 678, a, 14, True, col='#B34700'); text(x, 710, b, 24, True, width=700); text(x, 754, body, 17, width=700)
        elif n in (7, 9):
            # practice / recovery: stepped sequence with record prompt
            for i, (a, b, body) in enumerate(blocks):
                x = 60 + i*510; y = 300
                rect(x, y, 470, 210); text(x+18, y+18, f'{i+1:02d}', 16, True, col='#B34700'); text(x+18, y+52, a, 23, True); text(x+18, y+94, b, 18, True, width=430); text(x+18, y+126, body, 15, width=430)
                if i < 2: arrow([(x+470, y+105), (x+505, y+105)])
            text(60, 585, 'RECORD SPACE', 15, True, col='#B34700')
            for y in (640, 690, 740): line(60, y, 1540, y, '#B9BFC4')
            text(60, 760, 'Write what you actually observed; blanks stay blank rather than fabricated.', 16, width=1200)
        elif n == 14:
            # two distinct checkpoints
            rect(60, 300, 700, 300); text(80, 318, 'CHECKPOINT 1 / ACCEPTANCE', 18, True, col='#B34700')
            text(80, 356, blocks[0][1], 22, True, width=660); text(80, 400, blocks[0][2], 17, width=660)
            rect(860, 300, 700, 300); text(880, 318, 'CHECKPOINT 2 / AUTHORIZATION', 18, True, col='#B34700')
            text(880, 356, blocks[1][1], 22, True, width=660); text(880, 400, blocks[1][2], 17, width=660)
            arrow([(760, 450), (855, 450)])
            text(60, 660, blocks[2][0] + ' — ' + blocks[2][1], 20, True); text(60, 700, blocks[2][2], 17, width=1450)
        elif n == 11:
            # routing with explicit branches
            diamond(120, 300, 300, 130); text(185, 345, 'Capability', 19, True); text(190, 372, 'supported?', 18)
            rect(560, 285, 440, 75); text(580, 300, 'YES: proceed within stated scope', 18)
            rect(560, 400, 440, 75); text(580, 415, 'NO: select a supported route', 18, True, col='#B34700')
            arrow([(420, 350), (560, 322)]); arrow([(420, 380), (560, 437)], '#B34700')
            diamond(1100, 300, 320, 130); text(1158, 345, 'Within existing', 19, True); text(1176, 372, 'authorization?', 18)
            arrow([(1000, 437), (1100, 380)], '#B34700')
            rect(560, 560, 620, 75); text(580, 575, 'Scope expands: obtain additional authorization first', 17, True, col='#B34700')
            arrow([(1260, 430), (1260, 500), (1180, 500), (1180, 560)], '#B34700'); text(1430, 470, 'NO', 14, True, col='#B34700')
            for i, (a, b, body) in enumerate(blocks):
                y = 690 + i*60; text(60, y, f'{a} — {b}', 18, True, width=1490)
        else:
            for i, (a, b, body) in enumerate(blocks):
                y = 285 + i*180; rect(60, y, 350, 120); text(80, y+20, a, 23, True); text(80, y+64, b, 18, width=307)
                line(410, y+55, 475, y+55, '#B34700'); text(495, y+8, body, 23, width=1030)
                if i < len(blocks)-1: arrow([(235, y+120), (235, y+175)])
    elif level == 'medium':
        right = n in (5, 10, 13)
        for i, (a, b, body) in enumerate(blocks):
            y = 275 + i*192; dx = 1200 if right else 60; tx = 60 if right else 445; tw = 1090 if right else 1110
            rect(dx, y+2, 330, 127); text(dx+18, y+18, a, 18, True, col='#B34700'); text(dx+18, y+57, b, 20, True, width=292)
            if right: line(1158, y+60, 1200, y+60, '#B34700')
            else: line(390, y+60, 427, y+60, '#B34700')
            text(tx, y+5, body, 18, width=tw)
            if i < 2: arrow([(dx+165, y+129), (dx+165, y+186)])
    else:
        intro = {'4': 'Each field answers a distinct question. Read the specification as a complete agreement rather than a collection of optional suggestions. Numbering is the reading order across formats: field 05 is the same field in the slide, the article, and the checklist.',
                 '8': 'Assign status to the specific claim being evaluated. These labels are not a mandatory ladder through which every artifact advances. Several claims may have different statuses at the same moment: arrival may be established while readability remains unknown. Record the evidence and limitations supporting each label.',
                 '15': 'The evidence package closes the exercise by making the work inspectable. Preserve actual requests, responses, checks, and recovery observations rather than replacing them with a success narrative. These records support future integration decisions, but they do not establish untested production behavior or authorize a new release action.'}[str(n)]
        text(60, 245, intro, 17, width=1470)
        entries = [(f'{i+1:02d} / {a}', b) for i, (a, b) in enumerate(fields)] if n == 4 else \
                  states if n == 8 else evidence
        if n == 15: entries = [(f'{i+1:02d} / {a}', b) for i, (a, b) in enumerate(evidence)]
        cols = 4 if n == 4 else 3; cw = 350 if cols == 4 else 475; gap = 35
        groups = [entries[i::cols] for i in range(cols)]; maxbottom = 0
        for col, group in enumerate(groups):
            x = 60 + col*(cw+gap); y = 375
            for a, b in group:
                line(x, y, x+cw, y, '#B9BFC4'); text(x, y+10, a, 19, True); text(x, y+42, b, 15, width=cw)
                lines = []; row = ''
                for word in b.split():
                    z = (row + ' ' + word).strip()
                    if stringWidth(z, 'Copy', 15) > cw and row: lines.append(row); row = word
                    else: row = z
                lines.append(row); y += 42 + len(lines)*15*1.3 + 10
            maxbottom = max(maxbottom, y)
        if maxbottom > 850: raise ValueError(f'High page {n} exceeds body: {maxbottom}')
        blocks = [('CONTEXT', '', intro)] + [(a, '', b) for a, b in entries]
    count = wordcount(blocks) + len(s['title'].split()) + len(s['lead'].split())
    manifest.append({'slide': n, 'title': s['title'], 'density': level, 'layout': LAYOUT[n],
                     'editorialFeature': features[n][0], 'consultingVisual': VISUALS.get(n, (None,))[0],
                     'copyWords': count, 'audioAnchor': s['time'],
                     'pattern': 'visual opener' if n == 1 else 'reference' if level == 'high' else 'integrated editorial',
                     'diagramArrows': 'reading order only, not operational authorization'})
    finish_pdf(n)
appendix_pdf()  # consulting exhibits index page (page 16)
c.save()

# ---------- Semantic HTML renderer (token-based, responsive) ----------
E = htmllib.escape

def component_html(n):
    label, p = features[n]
    if label == 'loading-dock':
        return (f'<aside class="cmp cmp-loading-dock" aria-label="At the Loading Dock">'
                f'<h2>At the Loading Dock</h2><p class="cmp-scenario">{E(p["scenario"])}</p>'
                f'<p class="cmp-purpose">{E(p["purpose"])}</p>'
                f'<p class="cmp-class">Evidence classification: {E(p["classification"])}</p></aside>')
    if label == 'pause-consider':
        return (f'<aside class="cmp cmp-pause" aria-label="Pause and Consider">'
                f'<h2>Pause &amp; Consider</h2><p class="cmp-question">{E(p["question"])}</p></aside>')
    if label == 'carry-forward':
        return (f'<aside class="cmp cmp-carry" aria-label="Carry Forward">'
                f'<h2>Carry Forward</h2><p><strong>Principle:</strong> {E(p["principle"])}</p>'
                f'<p><strong>Next bounded action:</strong> {E(p["action"])}</p></aside>')
    if label == 'working-agreement':
        lis = ''.join(f'<li><code>{E(f)}</code></li>' for f in p['fields'])
        return (f'<aside class="cmp cmp-agreement" aria-label="The Working Agreement">'
                f'<h2>The Working Agreement</h2><ul class="cmp-fields">{lis}</ul>'
                f'<p class="cmp-note">{E(p["note"])}</p></aside>')
    if label == 'choose-route':
        rows = ''.join(f'<li><strong>{E(k)}</strong><span class="cmp-outcome">{E(v)}</span></li>' for k, v in p['branches'])
        return (f'<aside class="cmp cmp-route" aria-label="Choose the Route">'
                f'<h2>Choose the Route</h2><p class="cmp-condition">Condition: {E(p["condition"])}</p>'
                f'<ul class="cmp-branches">{rows}</ul></aside>')
    if label == 'inspect-payload':
        return (f'<aside class="cmp cmp-inspect" aria-label="Inspect the Payload">'
                f'<h2>Inspect the Payload</h2><div class="cmp-cols">'
                f'<figure class="cmp-source"><figcaption>Exact source</figcaption><blockquote>{E(p["source"]).replace(chr(10), "<br>")}</blockquote></figure>'
                f'<div class="cmp-candidate"><h3>Candidate</h3><p>{E(p["candidate"])}</p></div>'
                f'<div class="cmp-finding"><h3>Inspection finding</h3><p>{E(p["finding"])}</p></div>'
                f'</div></aside>')
    if label == 'try-handoff':
        lines = ''.join('<li class="record-line" aria-hidden="true"></li>' for _ in range(p['record_lines']))
        return (f'<aside class="cmp cmp-handoff" aria-label="Try the Handoff">'
                f'<h2>Try the Handoff</h2><p class="cmp-task">{E(p["task"])}</p>'
                f'<ol class="cmp-record" aria-label="Record space — write your actual observations">{lines}</ol></aside>')
    if label == 'evidence-window':
        return (f'<aside class="cmp cmp-evidence" aria-label="Evidence Window">'
                f'<h2>Evidence Window</h2><dl>'
                f'<div><dt>Claim</dt><dd>{E(p["claim"])}</dd></div>'
                f'<div><dt>Required support</dt><dd>{E(p["support"])}</dd></div>'
                f'<div><dt>Scope</dt><dd>{E(p["scope"])}</dd></div>'
                f'<div><dt>Limitations</dt><dd>{E(p["limitations"])}</dd></div></dl></aside>')
    if label == 'recovery-record':
        return (f'<aside class="cmp cmp-recovery" aria-label="Recovery Record">'
                f'<h2>Recovery Record</h2><div class="cmp-cols">'
                f'<div><h3>Observed problem</h3><p>{E(p["observed"])}</p></div>'
                f'<div><h3>Recovery action</h3><p>{E(p["action"])}</p></div>'
                f'<div><h3>Obtained evidence</h3><p>{E(p["evidence"])}</p></div></div></aside>')
    if label == 'before-release':
        cps = ''.join(f'<section class="cmp-checkpoint"><h3>{E(a)}</h3><p>{E(b)}</p></section>' for a, b in p['checkpoints'])
        return (f'<aside class="cmp cmp-release" aria-label="Before You Release">'
                f'<h2>Before You Release</h2><div class="cmp-cols">{cps}</div></aside>')
    return ''

def block_html(n):
    out = []
    blks = slide_blocks(n)
    if n == 4:
        blks = [(f'{i+1:02d} / {a}', '', b) for i, (a, _, b) in enumerate(blks)]
    if n == 15:
        blks = [(f'{i+1:02d} / {a}', '', b) for i, (a, _, b) in enumerate(blks)]
    for a, b, body in blks:
        if n == 6 and a == 'SOURCE':
            out.append(f'<section class="block block-source"><h2>{E(b)}</h2>'
                       f'<blockquote class="exact-source">{E(body).replace(chr(10), "<br>")}</blockquote></section>')
        elif b:
            out.append(f'<section class="block"><h2><span class="block-kicker">{E(a)}</span> {E(b)}</h2><p>{E(body)}</p></section>')
        else:
            out.append(f'<section class="block block-ref"><h2>{E(a)}</h2><p>{E(body)}</p></section>')
    return ''.join(out)

slides_html = []
for n in range(1, 16):
    s = slides[n]; level = levels[n]
    opener = ''
    if n == 1:
        opener = (f'<figure class="story"><img src="../source/podcast-deck/logistics-art.png" '
                  f'alt="Logistics dock scene illustrating arrival, inspection, and release"></figure>')
    slides_html.append(
        f'<article class="slide layout-{LAYOUT[n]}" data-density="{level}" id="slide-{n:02d}" aria-labelledby="s{n:02d}-title">'
        f'<header class="slide-head">'
        f'<p class="kicker">BOSS / Bioscillate Operating System by Seven</p>'
        f'<p class="slide-index">{level} / {n:02d} of 15</p>'
        f'<h1 class="slide-title" id="s{n:02d}-title">{E(s["title"])}</h1>'
        f'<p class="lead">{E(s["lead"])}</p></header>'
        + opener +
        f'<div class="slide-body">{visual_html(n)}{block_html(n)}</div>'
        + component_html(n) +
        f'<footer class="slide-foot"><p class="prompt"><strong>Your turn:</strong> {E(prompts[n])}</p>'
        f'<p class="nav">BOSS / Day Zero / {level} copy / {n:02d} of 15 / review candidate</p></footer>'
        f'</article>')

CSS = TOKENS + r"""
/* ---------- deck shell ---------- */
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--boss-color-ground);color:var(--boss-color-ink);
  font-family:var(--boss-font-reading);line-height:var(--boss-leading-body)}
.slide{position:relative;width:var(--boss-canvas-w);height:var(--boss-canvas-h);
  margin:0 auto var(--boss-space-4);background:var(--boss-color-ground);
  overflow:hidden;break-after:page;border-top:var(--boss-stroke-control) solid var(--boss-color-ink)}
.slide-head{position:absolute;left:var(--boss-space-5);top:var(--boss-space-4);right:var(--boss-space-5)}
.kicker{font-family:var(--boss-font-label);font-size:var(--boss-text-label);letter-spacing:.04em;
  text-transform:uppercase;margin:0;padding-top:var(--boss-space-1);
  border-top:var(--boss-stroke-control) solid var(--boss-color-ink)}
.slide-index{position:absolute;right:0;top:var(--boss-space-1);margin:0;
  font-family:var(--boss-font-label);font-size:var(--boss-text-label);text-transform:uppercase}
.slide-title{font-family:var(--boss-font-display);font-weight:700;font-size:var(--boss-text-display);
  line-height:var(--boss-leading-tight);margin:var(--boss-space-3) 0 var(--boss-space-2)}
.lead{font-size:var(--boss-text-lead);margin:0;max-width:66em}
.slide-body{position:absolute;left:var(--boss-space-5);right:var(--boss-space-5);top:260px;bottom:230px;
  display:grid;gap:var(--boss-space-4)}
.story{position:absolute;left:60px;top:265px;width:1512px;height:395px;margin:0}
.story img{width:100%;height:100%;object-fit:contain}
.block h2{font-size:var(--boss-text-lead);margin:0 0 var(--boss-space-1)}
.block-kicker{display:block;font-family:var(--boss-font-label);font-size:var(--boss-text-small);
  color:var(--boss-color-accent);text-transform:uppercase}
.block p{font-size:var(--boss-text-body);margin:0}
.block-ref h2{font-size:var(--boss-text-body)}
.block-ref p{font-size:var(--boss-text-small)}
.block-source .exact-source,.cmp-source blockquote{font-family:var(--boss-font-label);
  font-size:var(--boss-text-body);margin:0;padding:var(--boss-space-2);
  border-left:var(--boss-stroke-frame) solid var(--boss-color-ink);background:var(--boss-color-ground)}
.slide-foot{position:absolute;left:var(--boss-space-5);right:var(--boss-space-5);bottom:var(--boss-space-3);
  border-top:var(--boss-stroke-detail) solid var(--boss-color-rail);padding-top:var(--boss-space-1)}
.prompt{font-size:var(--boss-text-body);margin:0}
.nav{font-family:var(--boss-font-label);font-size:.75rem;color:var(--boss-color-muted);margin:var(--boss-space-1) 0 0}
/* ---------- consulting visuals (one exhibit per teaching point) ---------- */
.visual{margin:0}
.visual svg{width:100%;height:auto;display:block}
/* full-width band exhibits sit above the blocks */
.visual-chevron,.visual-staircase{grid-column:1/-1}
/* layout variants — one arrangement per teaching purpose */
.layout-opener .slide-body{grid-template-columns:1fr 1fr;top:640px;bottom:200px}
.layout-duo .slide-body,.layout-compare .slide-body,.layout-inspect .slide-body{grid-template-columns:1fr 1fr;grid-auto-rows:min-content}
.layout-payload-flow .slide-body,.layout-steps .slide-body,.layout-recovery .slide-body{grid-template-columns:repeat(3,1fr);grid-auto-rows:min-content}
.layout-quad .slide-body{grid-template-columns:1fr 1fr}
.layout-case .slide-body,.layout-route .slide-body{grid-template-columns:1fr;grid-auto-rows:min-content;max-width:1100px}
.layout-checkpoints .slide-body{grid-template-columns:1fr;max-width:1100px}
.layout-reference-ten .slide-body{grid-template-columns:repeat(4,1fr);gap:var(--boss-space-3)}
.layout-reference-seven .slide-body,.layout-checklist .slide-body{grid-template-columns:repeat(3,1fr);gap:var(--boss-space-3)}
.layout-reference-ten .block-ref,.layout-reference-seven .block-ref,.layout-checklist .block-ref{
  border-top:var(--boss-stroke-detail) solid var(--boss-color-rail);padding-top:var(--boss-space-1)}
/* visual placement overrides (must follow the layout variants) */
.layout-payload-flow .slide-body{grid-template-columns:1fr 640px}
.layout-recovery .slide-body{grid-template-columns:1fr 520px}
.layout-quad .slide-body{grid-template-columns:1fr 520px}
.layout-route .slide-body{grid-template-columns:1fr 560px;max-width:none}
.layout-map .slide-body{grid-template-columns:1fr 1fr;grid-auto-rows:min-content;max-width:none}
.layout-checklist .slide-body{grid-template-columns:1fr 1fr 440px}
.layout-payload-flow .visual,.layout-recovery .visual,.layout-quad .visual,.layout-route .visual{
  grid-column:2;grid-row:1/span 10;align-self:start}
.layout-checklist .visual{grid-column:3;grid-row:1/span 10;align-self:start}
.layout-checklist .slide-body{gap:var(--boss-space-3)}
.layout-checklist .block-ref p{font-size:var(--boss-text-small)}
/* ---------- editorial components (ten distinct contracts) ---------- */
.cmp{position:absolute;left:var(--boss-space-5);right:var(--boss-space-5);bottom:96px;
  border-top:var(--boss-stroke-control) solid var(--boss-color-ink);padding-top:var(--boss-space-1)}
.cmp h2{font-family:var(--boss-font-label);font-size:var(--boss-text-small);letter-spacing:.04em;
  text-transform:uppercase;color:var(--boss-color-accent);margin:0 0 var(--boss-space-1)}
.cmp h3{font-size:var(--boss-text-small);margin:0 0 var(--boss-space-1);text-transform:uppercase}
.cmp p{margin:0;font-size:var(--boss-text-body)}
.cmp-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--boss-space-4)}
.cmp-pause .cmp-question{font-size:var(--boss-text-lead)}
.cmp-fields{display:flex;gap:var(--boss-space-4);list-style:none;margin:0 0 var(--boss-space-1);padding:0}
.cmp-fields code{font-family:var(--boss-font-label);font-size:var(--boss-text-body)}
.cmp-note{font-size:var(--boss-text-small);color:var(--boss-color-muted)}
.cmp-branches{list-style:none;margin:var(--boss-space-1) 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:var(--boss-space-3)}
.cmp-branches li{border-left:var(--boss-stroke-frame) solid var(--boss-color-accent);padding-left:var(--boss-space-2)}
.cmp-outcome{display:block}
.cmp-record{list-style:none;margin:var(--boss-space-1) 0 0;padding:0}
.record-line{border-bottom:var(--boss-stroke-detail) solid var(--boss-color-rail);height:var(--boss-space-4)}
.cmp-evidence dl{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--boss-space-3);margin:0}
.cmp-evidence dt{font-family:var(--boss-font-label);font-size:var(--boss-text-label);text-transform:uppercase}
.cmp-evidence dd{margin:0;font-size:var(--boss-text-small)}
.cmp-release .cmp-cols{grid-template-columns:1fr 1fr}
.cmp-checkpoint{border:var(--boss-stroke-control) solid var(--boss-color-ink);padding:var(--boss-space-2)}
a:focus-visible,.cmp:focus-visible{outline:var(--boss-focus-ring);outline-offset:var(--boss-focus-offset)}
@page{size:17in 11in;margin:0}
/* ---------- reflow: lesson layout below the declared breakpoint ---------- */
@media (max-width:1100px){
  .slide{width:auto;height:auto;overflow:visible;padding:var(--boss-space-3) var(--boss-space-2)}
  .slide-head,.slide-body,.cmp,.slide-foot,.story{position:static;width:auto;right:auto;left:auto}
  .slide-body{display:block;margin:var(--boss-space-3) 0}
  .block{margin-bottom:var(--boss-space-3)}
  .cmp-cols,.cmp-release .cmp-cols,.cmp-evidence dl,.cmp-branches{grid-template-columns:1fr}
  .story img{height:auto}
  .visual svg{max-width:640px;margin:0 auto}
}
"""
(P/'styles.css').write_text(CSS)
doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width, initial-scale=1">'
       '<title>BOSS Day Zero editorial companion v0.4</title>'
       '<link rel="stylesheet" href="styles.css"></head><body><main>'
       + ''.join(slides_html) + '</main></body></html>')
(P/'BOSS_Day_Zero_Editorial_v0.4.html').write_text(doc)
(P/'density-manifest.json').write_text(json.dumps(manifest, indent=2))
(P/'density-map.md').write_text('|Slide|Copy level|Layout|Words|Title|\n|---|---|---|---|---|\n' +
    '\n'.join(f'|{m["slide"]}|{m["density"]}|{m["layout"]}|{m["copyWords"]}|{m["title"]}|' for m in manifest))
(P/'reading-order.mmd').write_text('flowchart TB\n A["Arrival: record receipt"] -->|Next topic| B["Verification: compare evidence"]\n B -->|Next topic| C["Release: check authorization scope"]\n')
shutil.copy(SRC/'draftdeck-standards/process.puml', P/'handoff.puml')
shutil.copy(SRC/'draftdeck-standards/process.svg', P/'handoff.svg')
(P/'REVIEW.md').write_text(
 'DraftDeck editorial review candidate v0.4.\n'
 'Slide 6 SOURCE block now carries the exact workshop source only; acceptance commentary is a separate block. '
 'Repeated filler paragraphs removed from medium pages 2, 5, 10, 12, 13; each medium page carries one explicit teaching relationship. '
 'All ten editorial features render through distinct components per design-system/editorial-components.md; shared tokens in design-system/tokens/tokens.css replace inline style literals. '
 'Seven consulting exhibits break up the sequence diagrams, one per teaching point: '
 'MECE tree (slide 3), chevron flow (7), recovery loop (9), routing decision tree (11), '
 'automation maturity staircase (12), two-by-two mechanism matrix (13), evidence funnel (15). '
 'The PDF carries a sixteenth appendix page indexing all seven. '
 'Slide 4 fields are numbered 01-10 as a consistent reading order across formats. Slides 7 and 9 use stepped practice/recovery layouts with record space; slide 8 and 10 use the Evidence Window component; slide 11 uses explicit conditional routing branches; slide 14 presents acceptance and authorization as two distinct checkpoints; slide 15 uses the submission checklist layout. '
 'HTML is semantic (h1 per slide, h2 per block, landmarks, labeled record space) and reflows to a single-column lesson layout below the 1100px breakpoint; the fixed canvas is preserved for the 17x11 slide format. '
 'Word counts include page headline, lead, diagram labels and teaching body; recurring navigation and writing prompt excluded. '
 'PDF is independently composed from the same content model and coordinates, not a browser export. '
 'Drafting geometry is drawn for the PDF canvas and kept as standalone geometry-NN.svg artifacts; the HTML edition relies on semantic reading order instead of embedding PDF-coordinate geometry, which collided with the reflowed component layouts. '
 'Browser rendering verified with headless Chromium against the generated HTML (see verification notes). Canva compatibility untested. Ten recurring editorial features are teaching devices, not new canonical governance fields. Reflection questions have no invented learner results.\n')
print('v0.4 built:', len(slides_html), 'slides;', doc.count('<h1'), 'h1;', doc.count('style="'), 'inline style attributes')
