"""Restricted MCP editorial PREVIEW only. Not authorized to manufacture final artifacts."""
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.request
import uuid
from mcp.server.fastmcp import FastMCP

# Hard-coded private Docker service. Never take endpoint or filesystem paths from model input.
BACKEND = 'http://kokoro:8880/v1/audio/speech'
OUTDIR = Path('/data/previews')
VOICES = {'af_heart', 'am_michael', 'af_bella', 'bf_emma'}
MAX_TEXT = 1000
MAX_AUDIO = 5_000_000
mcp = FastMCP('bioscillate-editorial-preview')

@mcp.tool()
def preview_paragraph(text: str, voice: str = 'af_heart', speed: float = 1.0) -> dict:
    """Preview an unapproved paragraph; never publish output or bypass review gates."""
    if not isinstance(text, str) or not 1 <= len(text) <= MAX_TEXT:
        raise ValueError('Text must contain between 1 and 1000 characters')
    if voice not in VOICES:
        raise ValueError('Voice is not on the approved preview list')
    if not .75 <= speed <= 1.25:
        raise ValueError('Speed outside preview limits')
    if re.search(r'\[(?:pause|voice|rate):|\]\(/|<[^>]+>',text,re.I):
        raise ValueError('Engine control tags/markup are disallowed in editorial previews')
    payload = json.dumps({'model':'kokoro','input':text,'voice':voice,
                          'speed':speed,'response_format':'wav'}).encode()
    req = urllib.request.Request(BACKEND,data=payload,
                                 headers={'Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=180) as response:
        if int(response.headers.get('Content-Length','0'))>MAX_AUDIO:
            raise ValueError('Backend response too large')
        audio=response.read(MAX_AUDIO+1)
    if len(audio)>MAX_AUDIO or not audio.startswith(b'RIFF'):
        raise ValueError('Unexpected backend audio')
    OUTDIR.mkdir(mode=0o700,parents=True,exist_ok=True)
    filename='preview-'+uuid.uuid4().hex+'.wav'
    dest=OUTDIR / filename
    with dest.open('xb') as f:
        f.write(audio)
    dest.chmod(0o600)
    return {'status':'CANDIDATE_PREVIEW_ONLY','path':str(dest),'sha256':hashlib.sha256(audio).hexdigest(),
            'voice':voice,'human_review':'REQUIRED','publication_authority':'NONE'}

if __name__=='__main__':
    mcp.run(transport='stdio')
