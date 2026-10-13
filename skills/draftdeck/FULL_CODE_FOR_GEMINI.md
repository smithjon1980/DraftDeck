# DraftDeck — Full End-to-End Canonical Source Bundle

Candidate branch: `feature/book-to-skills-intake-candidate`.

This is a **verbatim code-and-instructions snapshot** for Google Gemini inspection. Do not treat it as executed evidence. Production HOLD. The Story model, external Art agent, persistent storage and Phase 3 independent visual QA are not implemented.

## skills/draftdeck/SKILL.md

```markdown
---
name: draftdeck
description: Canonical phase-gated instructional visual artifact builder: Go supervisor/assembly, Tailwind CSS, Chromium PDF; Story PNG/WebP, Art HTML/CSS, Text semantic HTML; no SVG or React, no Canva pipeline.
---

# DraftDeck — Canonical Production Process

**Candidate, not released.** Phase 1 low-fidelity structure execution has passed prior GitHub Actions trials. Phase 2 requires an actual raster Story asset and an Art component. Phase 3 is independent high-fidelity QA plus explicit human release authority.

## One process — no historical fallback
Only the code in `skills/draftdeck/engine/` and workflow `.github/workflows/draftdeck-canonical.yml` is the *active DraftDeck execution candidate*. Superseded experiments are not fallback implementations. No SVG source, output, conversion, icons or intermediate files; no React, Canvas flattening, Canva or PowerPoint.

## Lifecycle
**Phase 1 / WIREFRAME:** supervisor checks scene contract; Text layer establishes live headings, copy, page geometry and a structural PDF. Story and Art may be missing. Structural pass does NOT constitute visual approval.

**Phase 2 / LAYERED COMPOSITION:** supervisor receives one genuine PNG/WebP Story asset, HTML/CSS Art components and semantic Text content; treats worker outputs as separately scoped, immutable, provenance-bearing inputs. No autonomous image model or task-dispatch service is presently wired into the engine. Missing required layers or invalid assets → HOLD. Render via Go html/template + Tailwind + Chromium.

**Phase 3 / HIGH FIDELITY:** independent reference comparison, overflow and clipping tests, exact source text, contrast and visual inspection, hashes, licensing, storage read-back, and explicit human release. Never self-certify. Production RELEASE_HOLD until proof exists.

## Execution
GitHub Actions is the candidate execution environment. `engine/main.go` reads a structured JSON scene, performs layer separation and exclusions, assembles deterministic HTML, invokes Chromium to write PDF, and creates a hash evidence manifest. Run `go test ./...` and compile Tailwind CSS first; use `scenes/phase1.json` for the verified wireframe milestone.

## Inspector handoff
Read `GEMINI_INSPECTION.md`, audit **all** canonical files, inspect the actual PDF artifact, and report supported PASS/FAIL/NOT_ESTABLISHED. Do not interpret a successful workflow as visual fidelity or operational autonomous agents. Do not publish or overwrite on inspection.
```

## skills/draftdeck/engine/go.mod

```markdown
module github.com/smithjon1980/DraftDeck/skills/draftdeck/engine

go 1.24
```

## skills/draftdeck/engine/main.go

```go
package main

import (
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "errors"
 "fmt"
 "html/template"
 "io"
 "os"
 "os/exec"
 "path/filepath"
 "regexp"
 "strings"
)

type Layer struct { ID string `json:"id"`; Kind string `json:"kind"`; Text string `json:"text,omitempty"`; Asset string `json:"asset,omitempty"` }
type Scene struct { RunID string `json:"run_id"`; Phase int `json:"phase"`; Title string `json:"title"`; Subtitle string `json:"subtitle"`; Source string `json:"source"`; Layers []Layer `json:"layers"` }
type Evidence struct { RunID string `json:"run_id"`; Phase int `json:"phase"`; Status string `json:"status"`; PDFSHA256 string `json:"pdf_sha256,omitempty"`; SourceSHA256 string `json:"source_sha256"`; StorySHA256 string `json:"story_sha256,omitempty"`; Tests []string `json:"tests"`; VisualQA string `json:"visual_qa"`; HumanRelease string `json:"human_release"` }
type View struct { Scene Scene; StoryURI string; Text []Layer; Art []Layer }
func checksum(data []byte)string{h:=sha256.Sum256(data);return hex.EncodeToString(h[:])}
func saveJSON(path string,v any)error{b,e:=json.MarshalIndent(v,"","  ");if e!=nil{return e};return os.WriteFile(path,append(b,'\n'),0644)}
func readSafeAsset(root,name string)([]byte,error){if name==""||filepath.Base(name)!=name||strings.Contains(name,".."){return nil,errors.New("UNSAFE_ASSET_PATH")};extension:=strings.ToLower(filepath.Ext(name));if extension!=".png"&&extension!=".webp"{return nil,errors.New("STORY_ASSET_MUST_BE_PNG_OR_WEBP")};b,e:=os.ReadFile(filepath.Join(root,name));if e!=nil{return nil,e};if extension==".png"&&!strings.HasPrefix(string(b),"\x89PNG\r\n\x1a\n"){return nil,errors.New("PNG_SIGNATURE_INVALID")};if extension==".webp"&&(len(b)<12||string(b[:4])!="RIFF"||string(b[8:12])!="WEBP"){return nil,errors.New("WEBP_SIGNATURE_INVALID")};return b,nil}
func run(scenePath,out,chrome string)error{
 bytes,err:=os.ReadFile(scenePath);if err!=nil{return err}
 var s Scene
 if err=json.Unmarshal(bytes,&s);err!=nil{return err}
 if !regexp.MustCompile(`^[A-Za-z0-9_-]{1,80}$`).MatchString(s.RunID)||s.Title==""||s.Source==""||s.Phase<1||s.Phase>3{return errors.New("CONTRACT_INVALID")}
 if err=os.MkdirAll(out,0755);err!=nil{return err}
 ev:=Evidence{RunID:s.RunID,Phase:s.Phase,Status:"HOLD",SourceSHA256:checksum(bytes),Tests:[]string{},VisualQA:"NOT_ESTABLISHED",HumanRelease:"NOT_AUTHORIZED"}
 var view View;view.Scene=s
 ids:=map[string]bool{};storyCount:=0;textCount:=0;artCount:=0
 for _,l:=range s.Layers{
  if l.ID==""||ids[l.ID]{return errors.New("DUPLICATE_OR_EMPTY_LAYER_ID")};ids[l.ID]=true
  if containsSVG(l.Text)||strings.HasSuffix(strings.ToLower(l.Asset),".svg"){return errors.New("SVG_FORBIDDEN")}
  switch l.Kind{
  case "story":storyCount++;if s.Phase>=2{b,e:=readSafeAsset(filepath.Dir(scenePath),l.Asset);if e!=nil{return e};mime:="image/png";if strings.HasSuffix(strings.ToLower(l.Asset),".webp"){mime="image/webp"};view.StoryURI="data:"+mime+";base64,"+base64Encode(b);ev.StorySHA256=checksum(b)}
  case "art":artCount++;view.Art=append(view.Art,l)
  case "text":textCount++;if l.Text==""{return errors.New("EMPTY_TEXT_LAYER")};view.Text=append(view.Text,l)
  default:return fmt.Errorf("UNKNOWN_LAYER_KIND:%s",l.Kind)
  }
 }
 if textCount==0{return errors.New("TEXT_LAYER_REQUIRED")}
 if s.Phase>=2&&(storyCount!=1||artCount==0){return errors.New("PHASE_2_REQUIRES_STORY_AND_ART")}
 if s.Phase==3{return errors.New("PHASE_3_REQUIRES_SEPARATE_INDEPENDENT_QA_AND_HUMAN_APPROVAL")}
 if s.Phase==1{ev.Status="P1_BUILD_CANDIDATE"}else{ev.Status="P2_COMPOSITION_CANDIDATE"}
 ev.Tests=append(ev.Tests,"SCENE_CONTRACT_VALID","LAYER_SCOPE_VALID","SVG_SOURCE_EXCLUDED")
 t,err:=template.ParseFiles("templates/page.html");if err!=nil{return err}
 htmlPath:=filepath.Join(out,"day-zero.html");file,err:=os.Create(htmlPath);if err!=nil{return err}
 if err=t.Execute(file,view);err!=nil{file.Close();return err};if err=file.Close();err!=nil{return err}
 if chrome==""{chrome="google-chrome"}
 absHTML,err:=filepath.Abs(htmlPath);if err!=nil{return err}
 absPDF,err:=filepath.Abs(filepath.Join(out,"day-zero.pdf"));if err!=nil{return err}
 cmd:=exec.Command(chrome,"--headless","--no-sandbox","--disable-gpu","--disable-dev-shm-usage","--no-pdf-header-footer","--print-to-pdf="+absPDF,"file://"+absHTML)
 log,err:=cmd.CombinedOutput();if err!=nil{return fmt.Errorf("CHROMIUM_ERROR: %v: %s",err,log)}
 pdf,err:=os.ReadFile(absPDF);if err!=nil{return err}
 if len(pdf)<5||string(pdf[:5])!="%PDF-"{return errors.New("PDF_SIGNATURE_INVALID")}
 ev.PDFSHA256=checksum(pdf);ev.Tests=append(ev.Tests,"PDF_SIGNATURE_VALID","PDF_HASH_COMPUTED")
 if err=saveJSON(filepath.Join(out,"evidence.json"),ev);err!=nil{return err}
 fmt.Printf("%s PDF_SHA256=%s VISUAL_QA=%s RELEASE=%s\n",ev.Status,ev.PDFSHA256,ev.VisualQA,ev.HumanRelease)
 return nil
}
func base64Encode(b []byte)string{const abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";var x strings.Builder;for i:=0;i<len(b);i+=3{v:=uint(b[i])<<16;remaining:=len(b)-i;if remaining>1{v|=uint(b[i+1])<<8};if remaining>2{v|=uint(b[i+2])};x.WriteByte(abc[(v>>18)&63]);x.WriteByte(abc[(v>>12)&63]);if remaining>1{x.WriteByte(abc[(v>>6)&63])}else{x.WriteByte('=')};if remaining>2{x.WriteByte(abc[v&63])}else{x.WriteByte('=')}};return x.String()}
func containsSVG(s string)bool{return strings.Contains(strings.ToLower(s),"<svg")||strings.Contains(strings.ToLower(s),"image/svg+xml")}\nfunc main(){if len(os.Args)!=3{fmt.Fprintln(os.Stderr,"usage: go run . <scene.json> <output-dir>");os.Exit(2)};if err:=run(os.Args[1],os.Args[2],os.Getenv("CHROME_BIN"));err!=nil{fmt.Fprintln(os.Stderr,"HOLD:",err);os.Exit(1)}}
var _ io.Reader
```

## skills/draftdeck/engine/main_test.go

```go
package main
import "testing"
func TestChecksum(t *testing.T){if checksum([]byte("abc"))!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"{t.Fatal("bad hash")}}
func TestRejectSVG(t *testing.T){s:="<svg viewBox='0 0 4 4'>";if !containsSVG(s){t.Fatal("SVG accepted")}}
```

## skills/draftdeck/engine/templates/page.html

```html
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1600,initial-scale=1"><link rel="stylesheet" href="styles.css"><style>@page{size:16.666667in 9.375in;margin:0}html,body{margin:0;width:1600px;height:900px}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}</style><title>DraftDeck Candidate</title></head><body class="bg-white text-neutral-950"><main class="relative w-[1600px] h-[900px] overflow-hidden bg-white px-[56px] py-[42px] flex flex-col"><div class="absolute inset-0 z-0" data-layer="story">{{if .StoryURI}}<img alt="Text-free story" class="absolute inset-0 w-full h-full object-cover" src="{{.StoryURI}}">{{end}}</div><div class="relative z-10 flex-1 flex flex-col"><header class="flex items-center justify-between border-b-2 border-black pb-4 font-mono text-[17px] font-bold"><span>bioscillate / BOSS</span><span>OPERATING SYSTEM BY SEVEN · DAY ZERO</span></header><p class="mt-8 font-mono text-[15px]">INSTRUCTIONAL DISPATCH / LAYERED COMPOSITION</p><h1 class="mt-8 text-[54px] font-bold tracking-tight leading-[1.08]">{{.Scene.Title}}</h1><p class="mt-5 text-[23px] leading-[1.35] max-w-[1120px]">{{.Scene.Subtitle}}</p><section class="mt-14 border-t border-neutral-700 pt-8" data-layer="art"><div class="font-mono text-center text-[17px] font-semibold">GOVERNED EXECUTION CHAIN</div><div class="mt-8 flex justify-center items-center gap-5 font-mono text-[18px] font-bold"><div class="border border-black px-6 py-4 bg-white">INTAKE</div><span>→</span><div class="border border-black px-6 py-4 bg-white">PACKAGE</div><span>→</span><div class="border border-black px-6 py-4 bg-white">ROUTE</div><span>→</span><div class="border border-black px-6 py-4 bg-white">INSPECT</div><span>→</span><div class="border border-black px-6 py-4 bg-white">DELIVER</div></div>{{range .Art}}<div class="mt-5 text-right font-mono text-[15px]">{{.Text}}</div>{{end}}</section><section class="mt-auto grid grid-cols-4 gap-5 pb-10" data-layer="text">{{range .Text}}<article class="border-t-2 border-black pt-4"><div class="font-mono text-[16px] font-semibold">{{.ID}}</div><p class="mt-4 text-[19px] leading-[1.32]">{{.Text}}</p></article>{{end}}</section><footer class="border-t-2 border-black pt-4 flex justify-between font-mono text-[13px]"><span>DATA IS CARGO. VERIFICATION IS PROOF OF DELIVERY.</span><span>CANDIDATE · NO SVG · HUMAN RELEASE HOLD</span></footer></div></main></body></html>
```

## skills/draftdeck/engine/scenes/phase1.json

```json
{
  "run_id": "day-zero-phase1-001",
  "phase": 1,
  "title": "From AI Consumer to Governed Operator.",
  "subtitle": "Stop asking what the model can generate. Start defining what the business needs, who is authorized, and what counts as verified delivery.",
  "source": "Day Zero reference — candidate fixture, source authentication pending",
  "layers": [
    {
      "id": "01 IDENTIFY THE CARGO",
      "kind": "text",
      "text": "The request, its source, intended recipient, and handling destination."
    },
    {
      "id": "02 RECORD THE EVIDENCE",
      "kind": "text",
      "text": "What is known, where it came from, and what remains uncertain."
    },
    {
      "id": "03 VERIFY THE RESULT",
      "kind": "text",
      "text": "Compare delivered work with the declared standard and ground truth."
    },
    {
      "id": "04 RELEASE BY PERMISSION",
      "kind": "text",
      "text": "Human authorization—not model confidence—controls final release."
    }
  ]
}
```

## skills/draftdeck/engine/input.css

```css
@import "tailwindcss";
@source "./templates/*.html";
```

## .github/workflows/draftdeck-canonical.yml

```yaml
name: DraftDeck Canonical Go Pipeline
on:
  workflow_dispatch:
    inputs:
      phase:
        description: "Run phase 1 or 2"
        type: choice
        options: ['1', '2']
        default: '1'
  push:
    branches: [feature/book-to-skills-intake-candidate]
    paths:
      - 'skills/draftdeck/**'
      - '.github/workflows/draftdeck-canonical.yml'
permissions:
  contents: read
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    defaults:
      run:
        working-directory: skills/draftdeck/engine
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.24'
          cache: false
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
      - name: Compile Tailwind
        run: |
          npm install --no-save --no-audit --no-fund tailwindcss@4 @tailwindcss/cli@4
          mkdir -p output
          npx @tailwindcss/cli -i input.css -o output/styles.css --minify
      - uses: browser-actions/setup-chrome@v2
        id: chrome
      - name: Unit tests
        run: go test ./...
      - name: Build Phase 1
        env:
          CHROME_BIN: ${{ steps.chrome.outputs.chrome-path }}
        run: go run . scenes/phase1.json output
      - name: Inspect structural evidence
        run: |
          python3 - <<'PY'
          import json,hashlib,pathlib
          o=pathlib.Path('output')
          e=json.loads((o/'evidence.json').read_text())
          pdf=(o/'day-zero.pdf').read_bytes()
          assert pdf[:5]==b'%PDF-'
          assert e['pdf_sha256']==hashlib.sha256(pdf).hexdigest()
          assert e['status']=='P1_BUILD_CANDIDATE'
          assert e['visual_qa']=='NOT_ESTABLISHED'
          assert not list(o.rglob('*.svg'))
          print('PHASE 1 STRUCTURAL CHECK PASS; VISUAL QA NOT ESTABLISHED')
          PY
      - uses: actions/upload-artifact@v4
        with:
          name: draftdeck-canonical-phase1
          path: skills/draftdeck/engine/output/
          retention-days: 7
```

## skills/draftdeck/GEMINI_INSPECTION.md

```markdown
# Gemini Inspection Brief — DraftDeck Canonical Go Pipeline

## Task
Independently audit the complete **active** implementation. Treat this as a code review, not permission to execute unapproved side effects. Do not consult deprecated experiments as working implementations.

## Read in order
1. `skills/draftdeck/SKILL.md`
2. `skills/draftdeck/engine/main.go`
3. `skills/draftdeck/engine/templates/page.html`
4. `skills/draftdeck/engine/scenes/phase1.json`
5. `skills/draftdeck/engine/input.css`
6. `.github/workflows/draftdeck-canonical.yml`
7. `skills/draftdeck/engine/main_test.go`

## Questions requiring evidence
- Does HTML preserve semantic editable text? Does Story stay PNG/WebP and Art HTML/CSS, with no SVG in execution?
- Is Phase 1 output correctly distinguished from Phase 2 composition and Phase 3 acceptance?
- Are content sources genuinely authenticated, or merely labeled?
- Is Story asset loading vulnerable to path traversal, malicious file contents or excessive size?
- Does the page physically render at one 16:9 sheet? Does the PDF have selectable text?
- Does Tailwind scan template classes correctly? Does CSS resolve when opening `output/day-zero.html` from Chromium?
- Is PDF SHA-256 independently matched on the downloaded artifact, not only CI workspace?
- Is the Go supervisor a *real multi-agent* controller? If not, name all gaps.
- Can the QA gate incorrectly report success from PDF signature only?
- Does any obsolete runner still trigger on commits? Identify residual legacy files, but do not delete unrelated repository history.

## Response format
Architecture matrix; file-by-file finding with path/line references; security and visual fidelity defects; reproducible commands; PASS/FAIL/NOT_ESTABLISHED for each phase; severity-ranked repairs. **No invented test results**. Production HOLD.

## Boundary
This is a code-and-evidence inspection packet. Gemini must not amend, merge, deploy, delete, or assert release without explicit authorization.
```

