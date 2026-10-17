"""Package complete offline output and verify all ZIP entries after writing."""
import hashlib, json, zipfile
from pathlib import Path

root=Path(__file__).resolve().parents[1]
dist=root/'dist'
html=(dist/'index.html').read_text()
assert html.endswith('<!-- DRAFTDECK_ATLAS_COMPLETE_368 -->\n')
assert '</body></html>' in html and 'base64,' not in html
assets=json.loads((dist/'assets.json').read_text())
assert len(assets)==368
assert all((dist/a['assetUrl']).is_file() for a in assets)
files=[dist/'index.html', dist/'assets.js', dist/'assets.json', dist/'source-pack.zip', dist/'import-report.json']
files += [dist/a['assetUrl'] for a in assets]
readme='Extract the entire archive, then open index.html in a browser. Keep assets.js and the assets folder beside index.html. All 368 real symbols are included. No web server, CDN, or installation is required. Original sources and licenses are in source-pack.zip. SHA-256 values for the complete package contents are in PACKING-LIST.json.\n'
(dist/'START-HERE.txt').write_text(readme)
files.append(dist/'START-HERE.txt')
receipt={str(p.relative_to(dist)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
(dist/'PACKING-LIST.json').write_text(json.dumps(receipt,indent=2)+'\n')
archive=dist/'DraftDeck_Engineering_Atlas_Complete.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files+[dist/'PACKING-LIST.json']:z.write(p,str(p.relative_to(dist)))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for name,record in receipt.items():
        data=z.read(name)
        assert len(data)==record['bytes'] and hashlib.sha256(data).hexdigest()==record['sha256']
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'assets':len(assets),'entries_verified':len(receipt)+1,'index_bytes':(dist/'index.html').stat().st_size}))
