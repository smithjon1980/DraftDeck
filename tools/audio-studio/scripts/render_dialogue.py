#!/usr/bin/env python3
"""BOSS-AUDIO-003: speak exact approved speaker turns with one Kokoro CPU pipeline.

No language model writes/rephrases the script. This is a bounded test, not release approval.
"""
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, pathlib, sys, traceback, datetime

CASE="BOSS-AUDIO-003"
RATE=24000
VOICES={"HOST_A":"af_heart", "HOST_B":"am_michael"}

def sha(b): return hashlib.sha256(b).hexdigest()
def stamp(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write_json(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8');tmp.replace(p)

def validate(path):
    raw=path.read_bytes()
    if not raw or len(raw)>24_000: raise ValueError('Invalid fixture size')
    obj=json.loads(raw.decode('utf-8','strict'))
    if obj.get('schema')!='boss.audio.dialogue.v1' or obj.get('case_id')!=CASE: raise ValueError('Case/schema mismatch')
    if obj.get('release')!='HOLD' or obj.get('speaker_attribution_status')!='EDITORIAL_CANDIDATE_NOT_DIARIZED': raise ValueError('Source status mismatch')
    turns=obj.get('turns')
    if not isinstance(turns,list) or not 4<=len(turns)<=16: raise ValueError('Expected 4-16 turns')
    ids=set(); spoken=[]; voices=set()
    for i,t in enumerate(turns,1):
        if not isinstance(t,dict) or set(t)!={'id','speaker','voice','text'}: raise ValueError('Unexpected turn fields')
        if t['id']!=f'T{i:03d}' or t['id'] in ids: raise ValueError('Unstable turn ID')
        ids.add(t['id']);s=t['speaker'];v=t['voice'];tx=t['text']
        if s not in VOICES or v!=VOICES[s]: raise ValueError('Speaker/voice mismatch')
        if not isinstance(tx,str) or not tx or tx!=tx.strip() or '\n' in tx: raise ValueError('Invalid spoken text')
        if any(c in tx for c in '<>{}'): raise ValueError('Possible unspoken markup')
        if len(tx.split())<10: raise ValueError('Turn too short')
        voices.add(s);spoken.append(tx)
    if voices!=set(VOICES): raise ValueError('Both speakers required')
    words=sum(len(x.split()) for x in spoken)
    if not 160<=words<=320: raise ValueError(f'Word limit exceeded: {words}')
    return raw,turns,words,spoken

def synthesize(turns,out):
    import numpy as np
    import soundfile as sf
    from kokoro import KPipeline
    pipe=KPipeline(lang_code='a')
    pause=np.zeros(int(RATE*0.22),dtype=np.float32)
    result=[]; clips=[]
    for turn in turns:
        chunks=[];observed=[]
        for text,phonemes,waveform in pipe(turn['text'],voice=turn['voice'],speed=1,split_pattern=r'\n+'):
            if hasattr(waveform,'detach'): waveform=waveform.detach().cpu().numpy()
            w=np.asarray(waveform,dtype=np.float32).reshape(-1)
            if not len(w) or not np.isfinite(w).all(): raise RuntimeError('Invalid audio in '+turn['id'])
            chunks.append(w);observed.append(str(text))
        if not chunks: raise RuntimeError('No audio for '+turn['id'])
        clip=np.concatenate(chunks)
        if np.max(np.abs(clip))<0.000001: raise RuntimeError('Silent audio for '+turn['id'])
        if clips: clips.append(pause)
        clips.append(clip)
        result.append({'turn_id':turn['id'],'speaker':turn['speaker'],'voice':turn['voice'],
          'submitted_text_sha256':sha(turn['text'].encode('utf8')),
          'submitted_word_count':len(turn['text'].split()),'rendered_chunks':len(chunks),
          'tts_returned_graphemes':observed,'audio_frames':len(clip),'duration_seconds':round(len(clip)/RATE,3)})
    audio=np.concatenate(clips)
    out.parent.mkdir(parents=True,exist_ok=True)
    tmp=out.with_name(out.stem+'.part.wav')
    sf.write(str(tmp),audio,RATE,subtype='PCM_16')
    with sf.SoundFile(str(tmp)) as f:
        if f.samplerate!=RATE or f.channels!=1 or f.frames<=0: raise RuntimeError('Invalid WAV properties')
        frames=int(f.frames)
    tmp.replace(out)
    return {'turns_rendered':result,'output_audio_frames':frames,'output_duration_seconds':round(frames/RATE,3),
      'output_wav_sha256':sha(out.read_bytes()),'output_wav_bytes':out.stat().st_size,'sample_rate_hz':RATE}

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--source',type=pathlib.Path,required=True)
    a.add_argument('--output',type=pathlib.Path,required=True)
    a.add_argument('--manifest',type=pathlib.Path,required=True)
    a.add_argument('--preflight-only',action='store_true')
    q=a.parse_args()
    rec={'case_id':CASE,'status':'NOT_ESTABLISHED','started_at_utc':stamp(),
         'source_path':str(q.source),'speaker_assignment':'EDITORIAL_NOT_ORIGINAL_DIARIZATION',
         'release_authorized':False,'human_listening_verified':False,'audible_word_fidelity_verified':False,
         'model_revision_pinned':False,'voice_mapping':VOICES}
    try:
        raw,turns,words,spoken=validate(q.source)
        rec.update({'source_sha256':sha(raw),'source_bytes':len(raw),'fixture_words':words,'turns_expected':len(turns),
            'submitted_joined_text_sha256':sha('\n'.join(spoken).encode('utf8')),'fixture_validation':'PASS'})
        if q.preflight_only:
            rec['status']='PREFLIGHT_PASS_NOT_RENDERED';return 0
        rec['kokoro_version']=importlib.metadata.version('kokoro')
        rec['torch_version']=importlib.metadata.version('torch')
        rec.update(synthesize(turns,q.output));rec['status']='AUDIO_GENERATED_LISTENING_PENDING';return 0
    except Exception as exc:
        rec['status']='HOLD';rec['error_class']=type(exc).__name__;rec['error_message']=str(exc)
        traceback.print_exc();return 1
    finally:
        rec['finished_at_utc']=stamp();write_json(q.manifest,rec)
        print(json.dumps({k:rec.get(k) for k in ('case_id','status','fixture_words','turns_expected','output_duration_seconds','error_class')},sort_keys=True),flush=True)

if __name__=='__main__': sys.exit(main())
