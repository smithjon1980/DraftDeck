"""Create the source pack from pinned local upstream checkouts, or expand it for building.

The archive retains original files and licenses. ISO derivatives retain symbol
geometry and necessary definitions; editorial labels are kept in the manifest.
"""
import argparse, copy, hashlib, json, math, re, subprocess, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

S = 'http://www.w3.org/2000/svg'
I = 'http://www.inkscape.org/namespaces/inkscape'
ET.register_namespace('', S)
ET.register_namespace('inkscape', I)
ROOT = Path(__file__).resolve().parents[1]

def sha(data): return hashlib.sha256(data).hexdigest()
def local(tag): return tag.split('}')[-1]

def pack(args):
    sources = [('iso', Path(args.iso), ['DWG/*PID*.svg', 'README.org']),
               ('freecad', Path(args.freecad), ['src/Mod/TechDraw/Symbols/gd-and-t/*.svg', 'src/Mod/TechDraw/Symbols/misc/*.svg', 'src/Mod/TechDraw/Symbols/other/*.svg', 'src/Mod/TechDraw/Symbols/surface-roughness-symbols/*.svg', 'LICENSE']),
               ('qet', Path(args.qet), ['20_logic/2010_logic_gates/201010_ansi_ieee/*.elmt', 'ELEMENTS.LICENSE'])]
    receipt = []
    with zipfile.ZipFile(ROOT/'vendor/source-pack.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for family, upstream, globs in sources:
            commit = subprocess.check_output(['git', '-C', str(upstream), 'rev-parse', 'HEAD'], text=True).strip()
            for pattern in globs:
                for p in sorted(upstream.glob(pattern)):
                    path = str(p.relative_to(upstream)); data = p.read_bytes()
                    z.writestr(f'{family}/{path}', data)
                    receipt.append(dict(family=family, path=path, commit=commit, sha256=sha(data)))
        z.writestr('provenance.json', json.dumps(receipt, indent=2))
    (ROOT/'vendor/provenance.json').write_text(json.dumps(receipt, indent=2)+'\n')

def iso_assets(data, source):
    root = ET.fromstring(data); labels = {}
    byid = {e.get('id'): e for e in root.iter() if e.get('id')}
    parents = {child: parent for parent in root.iter() for child in parent}
    for e in root.iter():
        label = e.get('{'+I+'}label', '')
        if label.startswith('REG#:') and label.endswith('_text'):
            labels[label[5:-5]] = ' '.join(''.join(e.itertext()).split())
    for e in root.iter():
        label = e.get('{'+I+'}label', '')
        if not(label.startswith('REG#:') and label.endswith('_symbol')): continue
        reg = label[5:-7]; description = labels.get(reg, '[UNKNOWN]')
        symbol = copy.deepcopy(e)
        # Keep artwork text-free. Symbol labels stay in native HTML.
        if any(local(x.tag) in ('text','foreignObject','script','image') for x in symbol.iter()):
            continue
        svg = ET.Element('{'+S+'}svg', {'viewBox':root.get('viewBox'), 'width':'400', 'height':'240'})
        defs = ET.SubElement(svg, '{'+S+'}defs'); found=set()
        def dependencies(node):
            for x in node.iter():
                for value in x.attrib.values():
                    refs=re.findall(r'url\(#([^)]+)\)', value)
                    if value.startswith('#'): refs.append(value[1:])
                    for ref in refs:
                        if ref in byid and ref not in found:
                            found.add(ref); target=copy.deepcopy(byid[ref]);defs.append(target);dependencies(target)
        dependencies(symbol)
        wrapper = ET.SubElement(svg, '{'+S+'}g', {'id':'asset-root'})
        ancestors=[]; p=parents.get(e)
        while p is not None and p is not root:
            ancestors.insert(0,p);p=parents.get(p)
        holder=wrapper
        for a in ancestors:
            attrs={k:v for k,v in a.attrib.items() if k in ('transform','style','fill','stroke','stroke-width')}
            # Layer visibility is an editor state, not part of the symbol.
            if 'style' in attrs: attrs['style']=re.sub(r'display\s*:\s*none', 'display:inline', attrs['style'])
            holder=ET.SubElement(holder, '{'+S+'}g', attrs)
        holder.append(symbol)
        yield dict(id='iso-'+reg+'-'+Path(source).stem.split('-')[-1]+'-'+e.get('id'), family='ISO process symbols', name=description.split('DESC:',1)[-1].strip(), reference=reg, source=source, license='CC-BY-SA-4.0', svg=ET.tostring(svg,encoding='unicode'))

def qet_asset(data, source):
    r=ET.fromstring(data); desc=r.find('description'); w=float(r.get('width'));h=float(r.get('height'))
    # QET hotspots identify the drawing's coordinate origin within its box.
    svg=ET.Element('{'+S+'}svg',{'viewBox':f'{-float(r.get("hotspot_x"))} {-float(r.get("hotspot_y"))} {w} {h}', 'width':str(w),'height':str(h)})
    group=ET.SubElement(svg,'{'+S+'}g',{'id':'asset-root','fill':'none','stroke':'black','stroke-width':'1'})
    ports=[]
    for e in desc:
        a=e.attrib;t=e.tag
        if t=='terminal': ports.append({k:a[k] for k in ('x','y','orientation')});continue
        if t=='dynamic_text':
            if ''.join(e.find('text').itertext()).strip(): raise ValueError('Unexpected symbol text '+source)
            continue
        style=a.get('style','');attrs={'fill':'black' if 'filling:black' in style else 'none'}
        if 'line-style:dashed' in style: attrs['stroke-dasharray']='4 2'
        if t=='line': attrs.update({k:a[k] for k in ('x1','y1','x2','y2')})
        elif t in ('rect','ellipse'):
            if t=='rect':attrs.update({k:a[k] for k in ('x','y','width','height')})
            else:
                attrs.update(cx=str(float(a['x'])+float(a['width'])/2),cy=str(float(a['y'])+float(a['height'])/2),rx=str(float(a['width'])/2),ry=str(float(a['height'])/2))
        elif t=='polygon':
            points=[];i=1
            while f'x{i}' in a: points.append(a[f'x{i}']+','+a[f'y{i}']);i+=1
            attrs['points']=' '.join(points);t='polyline' if a.get('closed')=='false' else 'polygon'
        elif t=='arc':
            cx=float(a['x'])+float(a['width'])/2;cy=float(a['y'])+float(a['height'])/2;rx=float(a['width'])/2;ry=float(a['height'])/2;start=float(a['start']);angle=float(a['angle'])
            def point(deg):return cx+rx*math.cos(math.radians(deg)),cy-ry*math.sin(math.radians(deg))
            x1,y1=point(start);x2,y2=point(start+angle)
            attrs['d']=f'M{x1},{y1} A{rx},{ry} 0 {int(abs(angle)>180)} {int(angle<0)} {x2},{y2}';t='path'
        else: raise ValueError('Unsupported QET primitive '+t+' '+source)
        ET.SubElement(group,'{'+S+'}'+t,attrs)
    name=r.find("names/name[@lang='en']").text
    return dict(id='ansi-'+Path(source).stem, family='ANSI / IEEE logic', name=name, reference='Upstream ANSI/IEEE collection', source=source, license='CC-BY-3.0 + upstream restriction', ports=ports,svg=ET.tostring(svg,encoding='unicode'))

def expand():
    out=ROOT/'dist';out.mkdir(exist_ok=True);assets=[];skipped=[]
    with zipfile.ZipFile(ROOT/'vendor/source-pack.zip') as z:
        receipt=json.loads(z.read('provenance.json'))
        for record in receipt:
            if sha(z.read(record['family']+'/'+record['path']))!=record['sha256']:
                raise ValueError('Source hash mismatch: '+record['path'])
        for name in sorted(z.namelist()):
            data=z.read(name)
            if name.startswith('iso/') and name.endswith('.svg'): assets.extend(iso_assets(data,name))
            elif name.startswith('freecad/') and name.endswith('.svg'):
                r=ET.fromstring(data)
                if any(local(e.tag) in ('text','foreignObject','script','image') for e in r.iter()): skipped.append(dict(source=name,reason='Contains text or image; requires an editable-label adapter'));continue
                if 'viewBox' not in r.attrib:r.set('viewBox',f'0 0 {r.get("width")} {r.get("height")}')
                assets.append(dict(id='draft-'+Path(name).stem,family='Drafting / '+Path(name).parent.name,name=Path(name).stem,reference='FreeCAD TechDraw; standard mapping requires review',source=name,license='LGPL-2.1; preserve upstream notices',svg=ET.tostring(r,encoding='unicode')))
            elif name.startswith('qet/') and name.endswith('.elmt'):
                if ET.fromstring(data).find('description/text') is not None:
                    skipped.append(dict(source=name,reason='Contains symbol text; requires an editable-label adapter'));continue
                assets.append(qet_asset(data,name))
    ids=[a['id'] for a in assets]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate asset identifiers: '+str(sorted({i for i in ids if ids.count(i)>1})))
    (out/'assets.json').write_text(json.dumps(assets,ensure_ascii=False))
    (out/'import-report.json').write_text(json.dumps({'assets':len(assets),'skipped':skipped},indent=2))
    print(f'{len(assets)} text-free engineering assets; {len(skipped)} require label adapters')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--iso');p.add_argument('--freecad');p.add_argument('--qet');args=p.parse_args()
    if args.iso:pack(args)
    expand()
