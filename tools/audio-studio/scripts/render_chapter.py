#!/usr/bin/env python3
"""Render one exact BOSS speaker-labeled chapter; no LLM rewriting or release authority."""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import traceback

RATE = 24000
VOICE_MAP = {'HOST_A': 'af_heart', 'HOST_B': 'am_michael'}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.partial')
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True)+'\n', encoding='utf-8')
    tmp.replace(path)

def load(path: Path) -> tuple[bytes, dict]:
    raw = path.read_bytes()
    if not (100 <= len(raw) <= 40000): raise ValueError('Chapter source exceeds bounds')
    obj = json.loads(raw.decode('utf-8', 'strict'))
    if obj.get('schema') != 'boss.audio.chapter.v1' or obj.get('case_id') != 'BOSS-AUDIO-004':
        raise ValueError('Unexpected case/schema')
    if obj.get('release') != 'HOLD' or obj.get('speaker_attribution_status') != 'PROVISIONAL_EDITORIAL_NOT_ORIGINAL_DIARIZATION':
        raise ValueError('A speaker assignment or release boundary is missing')
    turns = obj.get('turns')
    if not isinstance(turns, list) or not (1 <= len(turns) <= 8): raise ValueError('Invalid turn count')
    seen = set()
    for turn in turns:
        if not isinstance(turn,dict): raise ValueError('Invalid turn')
        if not isinstance(turn.get('id'),str) or turn['id'] in seen: raise ValueError('Invalid/duplicate ID')
        seen.add(turn['id'])
        if turn.get('speaker') not in VOICE_MAP or turn.get('voice') != VOICE_MAP[turn['speaker']]:
            raise ValueError('Speaker and voice mismatch')
        text=turn.get('text')
        if not isinstance(text,str) or not text.strip() or text!=text.strip() or '\n' in text:
            raise ValueError('Missing or malformed text')
        if turn.get('original_host_verified') is not False: raise ValueError('Original speaker status not disclosed')
    words=sum(len(x['text'].split()) for x in turns)
    if not 20<=words<=320: raise ValueError(f'Chapter size {words} outside L1 bounds')
    if obj.get('chapter_id') not in {'CH'+str(i).zfill(2) for i in range(1,100)}:
        raise ValueError('Invalid chapter ID')
    return raw,obj

def synthesize(obj: dict, output_dir: Path) -> dict:
    import numpy as np
    import soundfile as sf
    from kokoro import KPipeline
    pipeline=KPipeline(lang_code='a')
    clips=[]; receipts=[]
    for turn in obj['turns']:
        segments=[]; returned=[]
        for graphemes,_phonemes,waveform in pipeline(turn['text'],voice=turn['voice'],speed=1,split_pattern=r'\n+'):
            if hasattr(waveform,'detach'): waveform=waveform.detach().cpu().numpy()
            chunk=np.asarray(waveform,dtype=np.float32).reshape(-1)
            if not len(chunk) or not np.isfinite(chunk).all():
                raise RuntimeError('Invalid waveform '+turn['id'])
            segments.append(chunk);returned.append(str(graphemes))
        if not segments: raise RuntimeError('No audio '+turn['id'])
        clip=np.concatenate(segments)
        if float(np.max(np.abs(clip))) < 1e-6: raise RuntimeError('Silent audio '+turn['id'])
        if clips: clips.append(np.zeros(int(RATE*0.22),dtype=np.float32))
        clips.append(clip)
        receipts.append({'id':turn['id'], 'speaker':turn['speaker'],'voice':turn['voice'],
          'submitted_sha256':sha(turn['text'].encode('utf-8')), 'words':len(turn['text'].split()),
          'tts_returned_graphemes':returned, 'frames':len(clip)})
    audio=np.concatenate(clips)
    output=output_dir/'chapter.wav'
    tmp=output_dir/'chapter.partial.wav'
    sf.write(str(tmp),audio,RATE,format='WAV',subtype='PCM_16')
    with sf.SoundFile(str(tmp)) as f:
        if f.samplerate!=RATE or f.channels!=1 or f.frames<1: raise RuntimeError('Invalid WAV')
        frames=int(f.frames)
    tmp.replace(output)
    return {'turn_receipts':receipts,'audio_frames':frames,'sample_rate':RATE,'duration_seconds':round(frames/RATE,3),
       'wav_sha256':sha(output.read_bytes()),'wav_bytes':output.stat().st_size}

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--chapter', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--preflight-only', action='store_true')
    args=parser.parse_args()
    out=args.output_dir
    out.mkdir(parents=True,exist_ok=True)
    record={'case_id':'BOSS-AUDIO-004','status':'NOT_ESTABLISHED',
      'speaker_attribution':'PROVISIONAL_EDITORIAL_NOT_ORIGINAL_DIARIZATION',
      'audible_word_accuracy_verified':False,'human_listening_verified':False,'release_authorized':False,
      'model_revision_pinned':False,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        raw,chapter=load(args.chapter)
        record.update({'chapter_id':chapter['chapter_id'],'source_sha256':sha(raw),'turn_count':len(chapter['turns']),
        'spoken_word_count':sum(len(x['text'].split()) for x in chapter['turns']),
        'joined_spoken_sha256':sha('\n'.join(x['text'] for x in chapter['turns']).encode()),
        'source_time_label':chapter['source_time_label']})
        if args.preflight_only: record['status']='PREFLIGHT_PASS_NOT_RENDERED'; return 0
        record.update(synthesize(chapter,out))
        record['status']='AUDIO_GENERATED_LISTENING_PENDING';return 0
    except Exception as error:
        record.update({'status':'HOLD','error_type':type(error).__name__,'error':str(error)})
        traceback.print_exc();return 1
    finally:
        record['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        write_json(out/'render_manifest.json',record)
        print(json.dumps({k:record.get(k) for k in ['chapter_id','status','spoken_word_count','duration_seconds','error_type']},sort_keys=True),flush=True)

if __name__=='__main__':
    raise SystemExit(main())
