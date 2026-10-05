from pathlib import Path
import hashlib
root = Path(__file__).resolve().parent
parts = sorted(root.glob('AI_Pilot_Interface_QA_Specification.pdf.part*'))
data = b''.join(p.read_bytes() for p in parts)
assert hashlib.sha256(data).hexdigest() == '909cb0cd785893cfce1a261933c9e9a6a757107264530b13d58a6925f8d1ddf0', 'Reference parts failed integrity verification'
output = root / 'AI_Pilot_Interface_QA_Specification.pdf'
output.write_bytes(data)
print(output)
