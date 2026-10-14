#!/usr/bin/env python3
"""BOSS candidate Kokoro REST-only controlled audition. Never grants publication approval."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import struct
import time
import urllib.error
import urllib.request
import wave

ROOT = Path(__file__).resolve().parent
VOICE = {'HOST_A': 'af_heart', 'HOST_B': 'am_michael'}
PATCH_ID = 'P12'
PATCH_OLD = 'Then inspect the join, compare the resulting hashes, and confirm neighboring audio was not rebuilt.'
PATCH_NEW = 'Then inspect the join, compare the resulting hashes, and confirm neighboring clips remain unchanged.'
GAP_S = 0.16
PAUSE_S = 2.0
WAV_RATE = 24000
MAX_AUDIO_BYTES = 16_000_000


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def request_wav(base, phrase, voice, timeout=300):
    if not base.startswith(('http://127.0.0.1:', 'http://localhost:', 'http://kokoro:8880')):
        raise ValueError('Audition REST target MUST be localhost or the private Docker service; external endpoints forbidden')
    body = json.dumps({'model': 'kokoro', 'input': phrase, 'voice': voice,
                       'response_format': 'wav', 'speed': 1.0}).encode()
    req = urllib.request.Request(base.rstrip('/') + '/v1/audio/speech', data=body,
                                 headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if int(response.headers.get('Content-Length', 0)) > MAX_AUDIO_BYTES:
            raise ValueError('Oversized speech response')
        data = response.read(MAX_AUDIO_BYTES + 1)
    if len(data) > MAX_AUDIO_BYTES:
        raise ValueError('Oversized speech response')
    pcm = parse_wav(data)
    if not pcm:
        raise ValueError('Speech result contains no PCM samples')
    return data


def parse_wav(b):
    try:
        with wave.open(io.BytesIO(b), 'rb') as wav:
            if (wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getcomptype()) != (1, 2, WAV_RATE, 'NONE'):
                raise ValueError('WAV must be PCM16 mono 24000 Hz for lossless deterministic assembly')
            return wav.readframes(wav.getnframes())
    except (wave.Error, EOFError) as exc:
        raise ValueError('Invalid WAV payload') from exc


def write_wav(path, samples):
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as out:
        out.setnchannels(1);out.setsampwidth(2);out.setframerate(WAV_RATE)
        out.writeframes(samples)
    write_bytes(path, buf.getvalue())
    return digest(buf.getvalue())


def assemble(turns, paths, target):
    pcm_parts = []
    samples = 0
    spans = []
    pause = None
    for turn in turns:
        t = turn['id']
        chunk = parse_wav(paths[t].read_bytes())
        start = samples
        pcm_parts.append(chunk)
        samples += len(chunk) // 2
        spans.append({'id': t, 'from_s': round(start / WAV_RATE, 3), 'to_s': round(samples / WAV_RATE, 3)})
        if t == 'P11':
            begin = samples
            size = round(PAUSE_S * WAV_RATE)
            pcm_parts.append(b'\x00\x00' * size)
            samples += size
            pause = {'start_frame': begin, 'frames': size, 'seconds': size / WAV_RATE}
        gap = round(GAP_S * WAV_RATE)
        pcm_parts.append(b'\x00\x00' * gap)
        samples += gap
    content = b''.join(pcm_parts)
    final_sha = write_wav(target, content)
    return {'file': str(target), 'sha256': final_sha, 'duration_seconds': round(samples / WAV_RATE, 3),
            'pause_injected': pause, 'turn_spans': spans}


def run_pilot(base, turns_file, output, human_ipa=None, skip_probes=False):
    source = turns_file.read_bytes()
    turns = json.loads(source)
    assert len(turns) == 15 and len({t['id'] for t in turns}) == 15
    assert [t['id'] for t in turns] == [f'P{i:02d}' for i in range(1, 16)]
    assert all(t['speaker'] in VOICE for t in turns)
    count = sum(len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", t['text'])) for t in turns)
    if count != 750:
        raise ValueError(f'Unapproved source drift: expected 750 words, got {count}')
    if human_ipa is not None and not re.fullmatch(r'[a-zA-Zɑɐɒæɓʙβɔɕçɗɖðʤəɘɛɜɞɟɡɢʛɣɤɥɦɧħɨɪʝɭɬɫɮɯɰɱɲɳŋɴøɵœɶɸɹɻʁɾɽʀʂʃʈθʊʋʌɣɨɡɚɝʍχʎʏʑʐʒˈˌːˑʰ̃\u0303\u0329\-\. ]{1,90}',human_ipa):
        raise ValueError('Invalid IPA override syntax')
    output.mkdir(parents=True, exist_ok=True)
    baseline = output / 'baseline'
    patched = output / 'patched'
    baseline_segments = baseline / 'segments'
    patched_segments = patched / 'segments'
    baseline_segments.mkdir(parents=True, exist_ok=True)
    patched_segments.mkdir(parents=True, exist_ok=True)
    report = {'schema':'boss-kokoro-audition-v0.1','status':'CANDIDATE_NOT_RELEASED',
              'source_file':turns_file.name,'source_sha256':digest(source), 'source_words':count,
              'voice_map':VOICE,'engine':'kokoro-fastapi-v0.9.0-candidate','call_route':'REST_ONLY',
              'production_approval':None,'human_pronunciation_approval':None,
              'probes':{},'segments':[], 'neighbor_hashes_unchanged':None,
              'semantic_accuracy':'NOT_ESTABLISHED','human_listening':'NOT_TESTED',
              'public_release':'HOLD'}
    audios={}
    for turn in turns:
        p = baseline_segments / (turn['id'] + '.wav')
        input_text = turn['text']
        if human_ipa and 'Bioscillate' in input_text:
            input_text = input_text.replace('Bioscillate', f'[Bioscillate](/' + human_ipa + '/)')
        data = request_wav(base, input_text, VOICE[turn['speaker']])
        write_bytes(p, data)
        audios[turn['id']] = p
        report['segments'].append({'id':turn['id'],'voice':VOICE[turn['speaker']],
            'source_sha256':digest(turn['text'].encode()), 'sent_sha256':digest(input_text.encode()),
            'baseline_sha256':digest(data), 'bytes':len(data)})
        print('rendered', turn['id'],len(data),flush=True)
    report['baseline'] = assemble(turns, audios, baseline/'pilot.wav')
    # Patch just one sentence in P12. All other WAV segment files are copied byte-for-byte.
    patched_turns=[]
    for turn in turns:
        t = dict(turn)
        if t['id'] == PATCH_ID:
            if PATCH_OLD not in t['text']:
                raise ValueError('P12 exact patch target not found')
            t['text'] = t['text'].replace(PATCH_OLD, PATCH_NEW, 1)
        patched_turns.append(t)
    patched_audios={}
    for turn in patched_turns:
        src = audios[turn['id']]
        dst = patched_segments / src.name
        if turn['id'] == PATCH_ID:
            data = request_wav(base, turn['text'], VOICE[turn['speaker']])
            write_bytes(dst, data)
        else:
            shutil.copyfile(src, dst)
        patched_audios[turn['id']] = dst
    neighbors={id:digest(audios[id].read_bytes())==digest(patched_audios[id].read_bytes()) for id in audios if id!=PATCH_ID}
    patch_diff=digest(audios[PATCH_ID].read_bytes()) != digest(patched_audios[PATCH_ID].read_bytes())
    report['patched'] = assemble(patched_turns, patched_audios,patched/'pilot.wav')
    report['patch_test']={'only_synthesized_turn':PATCH_ID,'modified_sentence':PATCH_NEW,
        'original_sentence':PATCH_OLD,'neighbor_hashes':neighbors,
        'neighbor_count':len(neighbors),'all_neighbors_identical':all(neighbors.values()),
        'patched_clip_differs':patch_diff,
        'assembly_differs':report['baseline']['sha256']!=report['patched']['sha256']}
    report['neighbor_hashes_unchanged']=all(neighbors.values())
    if not skip_probes:
        # Punctuation/IPA exercise is a functional transport test only, never human sound adjudication.
        ipa_text='The city of [Worcester](/wˈʊstər/) is the example.'
        ipa_bytes=request_wav(base,ipa_text, VOICE['HOST_A'])
        write_bytes(output/'probe_ipa_worcester.wav',ipa_bytes)
        report['probes']['ipa_tag_api_acceptance']={'status':'API_RETURNED_WAV','example':'Worcester',
             'sha256':digest(ipa_bytes),'bioscillate_pronunciation':'NOT_ESTABLISHED'}
        pause_text='Inspect the payload. [pause:2s] Now proceed.'
        pause_bytes=request_wav(base,pause_text,VOICE['HOST_A'])
        write_bytes(output/'probe_pause_tag.wav',pause_bytes)
        # Detect near-silent interval; heuristic only. The exact assembly pause is independently enforced.
        pcm=parse_wav(pause_bytes)
        sample_count=len(pcm)//2
        samples=struct.unpack('<'+str(sample_count)+'h',pcm)
        maximum=0;run=0
        for s in samples:
            if abs(s) <= 8:
                run+=1; maximum=max(maximum,run)
            else:run=0
        measured=maximum/WAV_RATE
        report['probes']['pause_tag_2s']={'status':'MEASURED_HEURISTIC',
            'longest_near_silence_s':round(measured,4), 'tolerance_check':'PASS' if 1.8<=measured<=2.3 else 'REVIEW',
            'note':'Near-zero audio threshold is a heuristic, not proof of semantic silence.'}
    report['checks']={
        'source_750_words':'PASS','rest_only':'PASS','15_turns':'PASS',
        'neighbor_isolation':'PASS' if all(neighbors.values()) else 'FAIL',
        'patched_turn_changes':'PASS' if patch_diff else 'REVIEW',
        'two_second_assembly_pause':'PASS' if report['baseline']['pause_injected']['frames']==48000 else 'FAIL',
        'ipa_brand_pronunciation':'NOT_ESTABLISHED',
        'human_review':'HOLD','publish':'HOLD'}
    report_file=output/'audition_report.json'
    report_file.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    if not all(neighbors.values()):
        raise RuntimeError('Non-target segment changed')
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--api-base', default=os.getenv('KOKORO_API_BASE','http://127.0.0.1:8880'))
    p.add_argument('--turns',type=Path,default=ROOT/'fixtures/pilot_turns.json')
    p.add_argument('--out',type=Path,default=ROOT/'output')
    p.add_argument('--human-approved-ipa',default=None,help='Only after documented human pronunciation approval')
    p.add_argument('--skip-probes',action='store_true')
    args=p.parse_args()
    print(json.dumps({'run':'candidate audition','source':str(args.turns),'output':str(args.out),'permission':'NO PUBLIC RELEASE'}),flush=True)
    x=run_pilot(args.api_base,args.turns,args.out,args.human_approved_ipa,args.skip_probes)
    print(json.dumps({'checks':x['checks'],'probes':x['probes']},indent=2))

if __name__=='__main__':main()
