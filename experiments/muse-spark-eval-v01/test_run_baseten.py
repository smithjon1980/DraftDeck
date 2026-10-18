import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from run_baseten import (
    ENDPOINT, MODEL, build_payload, parse_completion, read_cases,
    reserved_usd, main,
)


class TestBasetenAdapter(unittest.TestCase):
    def setUp(self):
        self.good = {
            "case_id": "V01", "category": "visual",
            "prompt": "Inspect marker position",
            "evidence": {"img": "synthetic image provided"},
            "image_data_url": "data:image/png;base64,QUJD",
            "response_schema": {"decision": ["PASS", "FAIL", "HOLD"]}
        }

    def test_uses_documented_baseten_model_and_url(self):
        self.assertEqual(MODEL, "meta-models/muse-spark-open")
        self.assertEqual(ENDPOINT, "https://inference.baseten.co/v1/chat/completions")

    def test_multimodal_image_and_no_ground_truth(self):
        p = build_payload(self.good, 200)
        self.assertEqual(p["messages"][1]["content"][1]["type"], "image_url")
        self.assertNotIn("reference", json.dumps(p))
        self.assertEqual(p["max_tokens"], 200)

    def test_cost_reservation_increases_for_vision(self):
        p = build_payload(self.good, 200)
        p2 = build_payload({k:v for k,v in self.good.items()
                            if k != "image_data_url"}, 200)
        self.assertGreater(
            reserved_usd(p, 200, 20000, 1.25, 4.25),
            reserved_usd(p2, 200, 20000, 1.25, 4.25))

    def test_parser_refusal_for_empty_or_invalid(self):
        self.assertEqual(parse_completion({}, "X")["decision"], "REFUSE")
        self.assertEqual(parse_completion({
            "choices":[{"message":{"content":"not JSON"}}]
        }, "X")["decision"], "REFUSE")

    def test_parser_for_valid_structured_json(self):
        a={"decision":"FAIL","route":"NONE","defects":["LOGO_POSITION"],
           "evidence_ids":["img"],"explanation":"incorrect corner"}
        output=parse_completion({"choices":[{"message":{"content":json.dumps(a)}}]}, "V01")
        self.assertEqual(output["decision"], "FAIL")
        self.assertEqual(output["evidence_ids"], ["img"])

    def test_reject_unblinded_reference(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td)/"blind.jsonl"
            f.write_text(json.dumps({**self.good,"reference":{"decision":"FAIL"}})+"\n")
            with self.assertRaises(ValueError):
                read_cases(f)

    def test_default_dry_run_never_calls_network_or_requires_key(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td)/"blind.jsonl"
            f.write_text(json.dumps(self.good)+"\n")
            argv=["run_baseten.py","--blind-requests",str(f),"--max-calls","1"]
            with patch.object(sys,"argv",argv), \
                 patch.dict(os.environ, {"BASETEN_API_KEY":""}), \
                 patch("run_baseten.urllib.request.urlopen") as u:
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    main()
                self.assertIn("NO_INFERENCE_RUN", out.getvalue())
                u.assert_not_called()

    def test_live_requires_both_authorization_flags_before_network(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"blind.jsonl"
            f.write_text(json.dumps(self.good)+"\n")
            argv=["run_baseten.py","--blind-requests",str(f),"--max-calls","1",
                  "--mode","live","--max-usd","1",
                  "--input-usd-per-million","1.25",
                  "--output-usd-per-million","4.25"]
            with patch.object(sys,"argv",argv), \
                 patch("run_baseten.urllib.request.urlopen") as u:
                with self.assertRaises(SystemExit) as ctx:
                    main()
                self.assertIn("LIVE HOLD", str(ctx.exception))
                u.assert_not_called()


if __name__ == "__main__":
    unittest.main()
