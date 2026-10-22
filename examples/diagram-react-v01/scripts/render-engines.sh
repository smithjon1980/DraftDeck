#!/usr/bin/env bash
# Compile exactly two repository-reviewed synthetic fixture diagrams.
# Never run on arbitrary model input or private manuscripts.
set -euo pipefail
repo_root="$(cd "$(dirname "$0")/../../.." && pwd)"
project="$repo_root/examples/diagram-react-v01"
out="$project/dist/diagrams"
mkdir -p "$out" "$project/.local-tools"

browser="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [[ -z "$browser" ]]; then
  echo "HOLD: No Chromium/Chrome executable for real Mermaid rendering" >&2
  exit 1
fi
printf '{"executablePath":"%s","args":["--no-sandbox","--disable-setuid-sandbox"]}\n' "$browser" > "$project/.local-tools/puppeteer-config.json"
(
 cd "$project"
 ./node_modules/.bin/mmdc \
   -i "$repo_root/tests/diagram-golden-paths/main-street-copy-intake.mmd" \
   -o "$out/intake.svg" \
   -c "$repo_root/design-system/diagram/mermaid-theme.json" \
   -p "$project/.local-tools/puppeteer-config.json" \
   -b white
)

plantuml_version="1.2025.10"
jar="$project/.local-tools/plantuml-epl-$plantuml_version.jar"
base="https://repo.maven.apache.org/maven2/net/sourceforge/plantuml/plantuml-epl/$plantuml_version/plantuml-epl-$plantuml_version.jar"
if [[ ! -s "$jar" ]]; then
  curl --fail --location --silent --show-error --retry 2 --max-time 120 "$base" -o "$jar"
fi
curl --fail --location --silent --show-error --retry 2 --max-time 30 "$base.sha256" -o "$jar.sha256"
expected="$(tr -d '\n\r[:space:]' < "$jar.sha256")"
actual="$(sha256sum "$jar" | cut -d' ' -f1)"
if [[ "$actual" != "$expected" ]]; then
  echo "FAIL: PlantUML binary digest differs from provider digest" >&2
  exit 1
fi
java -Djava.awt.headless=true -jar "$jar" -tsvg -pipe \
  < "$repo_root/tests/diagram-golden-paths/main-street-copy-clarification.puml" \
  > "$out/clarification.svg"

python3 - "$out/intake.svg" "$out/clarification.svg" <<'PY'
import pathlib, sys, xml.etree.ElementTree as ET
for arg in sys.argv[1:]:
    path = pathlib.Path(arg)
    data = path.read_bytes()
    if len(data) < 1000:
        raise SystemExit("FAIL: suspiciously small render: " + path.name)
    root = ET.fromstring(data)
    if root.tag.split("}")[-1] != "svg":
        raise SystemExit("FAIL: not svg XML: " + path.name)
    if b"Syntax Error" in data or b"Cannot find Graphviz" in data or b"Error line" in data:
        raise SystemExit("FAIL: renderer produced an error image: " + path.name)
    print("Rendered real SVG: " + path.name + " / " + str(len(data)) + " bytes")
PY
echo "Engine renders completed; browser proof is a separate gate."
