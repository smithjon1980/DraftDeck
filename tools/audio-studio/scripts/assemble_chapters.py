#!/usr/bin/env python3
"""Assemble exact checked WAV chapters; reject missing, reordered, or mismatched inputs."""
import argparse,hashlib,json
from pathlib import Path

def digest(b):return hashlib.sha256(b).hexdigest()

def assemble(index_path, inputs, dest):
    import numpy as np
    import soundfile as sf
    index=json.loads(index_path.read_text(encoding='utf8'))
    chapters=index['chapters']
    if not 2 <= len(chapters) <= 25: raise ValueError('Unexpected chapter count')
    identity=[]; frames=[]; seen=set()
    for ix,part in enumerate(chapters):
        cid=part['chapter_id']
        if cid in seen: raise ValueError('Duplicate chapter')
        seen.add(cid)
        # The artifact content is rooted at the uploaded chapter directory.
        folder=inputs/f'boss-audio-004-{cid}'
        if not folder.is_dir(): raise ValueError('Missing chapter '+cid)
        manifest=json.loads((folder/'render_manifest.json').read_text(encoding='utf8'))
        if manifest.get('status')!='AUDIO_GENERATED_LISTENING_PENDING':raise ValueError('Unrendered chapter '+cid)
        if manifest.get('source_sha256')!=part['sha256'] or manifest.get('chapter_id')!=cid:
            raise ValueError('Source identity mismatch '+cid)
        if manifest.get('turn_count')!=len(part['speaker_turn_ids']): raise ValueError('Turn count mismatch '+cid)
        if [x['id'] for x in manifest['turn_receipts']]!=part['speaker_turn_ids']:
            raise ValueError('Turn order mismatch '+cid)
        wav=folder/'chapter.wav'
        if digest(wav.read_bytes())!=manifest['wav_sha256']: raise ValueError('WAV hash mismatch '+cid)
        a,sr=sf.read(str(wav),dtype='float32',always_2d=False)
        if sr!=24000 or a.ndim!=1 or len(a)!=manifest['audio_frames']: raise ValueError('Format/frames mismatch '+cid)
        if ix:frames.append(np.zeros(int(sr*0.40),dtype=np.float32))
        frames.append(a)
        identity.append({'chapter_id':cid,'source_sha256':part['sha256'],'wav_sha256':manifest['wav_sha256'],
          'duration_seconds':manifest['duration_seconds'],'turn_ids':part['speaker_turn_ids']})
    audio=np.concatenate(frames)
    dest.mkdir(parents=True,exist_ok=True)
    target=dest/'assembled_dialogue.wav'
    sf.write(str(target),audio,24000,subtype='PCM_16')
    receipt={'case_id':'BOSS-AUDIO-004','status':'ASSEMBLED_INSPECTION_PENDING','chapters':identity,'chapter_count':len(identity),
      'duration_seconds':round(len(audio)/24000,3),'wav_sha256':digest(target.read_bytes()),
      'human_listening_verified':False,'publication_authorized':False}
    (dest/'assembly_manifest.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({'status':receipt['status'],'chapters':len(identity),'duration':receipt['duration_seconds']},sort_keys=True))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--index',type=Path,required=True);ap.add_argument('--inputs',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
    a=ap.parse_args();assemble(a.index,a.inputs,a.output_dir)
if __name__=='__main__':main()
