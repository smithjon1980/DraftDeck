import hashlib
import io
import json
import pathlib
import sys
import tempfile
import threading
import unittest
import wave
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import audition

class SpeechHandler(BaseHTTPRequestHandler):
    calls=[]
    def log_message(self,*args):pass
    def do_POST(self):
        assert self.path=='/v1/audio/speech'
        n=int(self.headers.get('Content-Length','0'))
        p=json.loads(self.rfile.read(n))
        self.calls.append(p['input'])
        # Distinct, deterministic wav based on text. Synthetic MOCK, not real neural speech.
        seed=int(hashlib.sha256(p['input'].encode()).hexdigest()[:4],16)
        samples=[(seed % 10000)+1]*2400
        raw=b''.join(int(x).to_bytes(2,'little',signed=True) for x in samples)
        b=io.BytesIO()
        with wave.open(b,'wb') as wav:
            wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(24000);wav.writeframes(raw)
        audio=b.getvalue()
        self.send_response(200);self.send_header('Content-Type','audio/wav');self.send_header('Content-Length',str(len(audio)));self.end_headers();self.wfile.write(audio)

class AuditionTests(unittest.TestCase):
    def test_fifteen_turns_and_single_patch(self):
        SpeechHandler.calls=[]
        server=ThreadingHTTPServer(('127.0.0.1',0),SpeechHandler)
        th=threading.Thread(target=server.serve_forever,daemon=True);th.start()
        try:
            with tempfile.TemporaryDirectory() as td:
                report=audition.run_pilot('http://127.0.0.1:'+str(server.server_port),
                    audition.ROOT/'fixtures/controlled_turns.json',pathlib.Path(td),skip_probes=False)
                self.assertEqual(len(SpeechHandler.calls),18) # 15 baseline + 1 patch + 2 probes
                self.assertEqual(report['source_words'],750)
                self.assertEqual(report['patch_test']['neighbor_count'],14)
                self.assertTrue(report['patch_test']['all_neighbors_identical'])
                self.assertTrue(report['patch_test']['patched_clip_differs'])
                self.assertEqual(report['baseline']['pause_injected']['frames'],48000)
                self.assertNotEqual(report['baseline']['sha256'],report['patched']['sha256'])
                self.assertEqual(report['checks']['ipa_brand_pronunciation'],'NOT_ESTABLISHED')
                self.assertEqual(report['public_release'],'HOLD')
        finally:
            server.shutdown();server.server_close();th.join()
    def test_reject_remote(self):
        with self.assertRaises(ValueError):
            audition.request_wav('https://example.com','test','af_heart')
    def test_source_words(self):
        turns=json.loads((audition.ROOT/'fixtures/controlled_turns.json').read_text())
        self.assertEqual(len(turns),15)

if __name__=='__main__': unittest.main()
