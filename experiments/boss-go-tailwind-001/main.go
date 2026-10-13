package main

import (
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "fmt"
 "html/template"
 "os"
 "os/exec"
 "path/filepath"
 "strings"
)

type Panel struct { N, Title, Body string }
type Scene struct { Title, Subtitle string; Panels []Panel }
func main() {
 out := "output"
 if err := os.MkdirAll(out,0755); err != nil { panic(err) }
 scene:=Scene{
  Title:"From AI Consumer to Governed Operator.",
  Subtitle:"Stop asking what the model can generate. Start defining what the business needs, who is authorized, and what counts as verified delivery.",
  Panels:[]Panel{{"01","IDENTIFY THE CARGO","The request, its source, intended recipient, and handling destination."},{"02","RECORD THE EVIDENCE","What is known, where it came from, and what remains uncertain."},{"03","VERIFY THE RESULT","Compare delivered work with the declared standard and ground truth."},{"04","RELEASE BY PERMISSION","Human authorization—not model confidence—controls final release."}},
 }
 const page=`<!doctype html><html lang="en"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles.css"><style>@page{size: 16.6667in 9.375in;margin:0}html,body{margin:0;width:1600px;height:900px;overflow:hidden}*{box-sizing:border-box}</style></head>
 <body class="bg-white text-neutral-950"><main class="w-[1600px] h-[900px] px-[55px] py-[36px] font-sans flex flex-col">
 <header class="flex justify-between border-b-2 border-black pb-3 text-[19px] font-bold"><span>bioscillate / BOSS</span><span class="font-mono text-[15px]">OPERATING SYSTEM BY SEVEN · DAY ZERO / 01</span></header>
 <p class="font-mono text-[15px] tracking-wide mt-4">INSTRUCTIONAL DISPATCH / LEARNING PACKAGE 001</p>
 <h1 class="text-[51px] leading-[1.08] font-semibold tracking-tight mt-8">{{.Title}}</h1>
 <p class="text-[24px] leading-[1.3] max-w-[1120px] mt-3">{{.Subtitle}}</p>
 <div class="text-center mt-[54px] font-mono font-semibold text-[17px]">GOVERNED EXECUTION CHAIN</div>
 <section class="mt-6 pt-9 border-t border-neutral-500 flex justify-center items-center gap-3 font-mono text-[19px]">
 <div class="border border-black px-7 py-5">INTAKE</div><span>→</span><div class="border border-black px-7 py-5">PACKAGE</div><span>→</span><div class="border border-black px-7 py-5">ROUTE</div><span>→</span><div class="border border-black px-7 py-5">INSPECT</div><span>→</span><div class="border border-black px-7 py-5">DELIVER</div></section>
 <p class="text-right font-mono text-[15px] mt-6">VERIFICATION GATE: FAIL / UNCERTAIN → HOLD → HUMAN REVIEW</p>
 <section class="grid grid-cols-4 gap-5 mt-auto pb-8">{{range .Panels}}<article class="border border-neutral-700 p-5 min-h-[170px]"><h2 class="font-mono font-bold text-[17px]"><span class="text-cyan-700">{{.N}}</span> {{.Title}}</h2><div class="border-t border-neutral-400 mt-4 pt-5 text-[18px] leading-snug">{{.Body}}</div></article>{{end}}</section>
 <footer class="border-t-2 border-black pt-4 font-mono text-[13px] flex justify-between"><span>DATA IS CARGO. VERIFICATION IS PROOF OF DELIVERY.</span><span>GO + TAILWIND + CHROMIUM · CANDIDATE · NOT A RELEASE</span></footer></main></body></html>`
 t:=template.Must(template.New("page").Parse(page))
 f,err:=os.Create(filepath.Join(out,"day-zero.html"));if err!=nil{panic(err)}
 if err=t.Execute(f,scene);err!=nil{panic(err)};if err=f.Close();err!=nil{panic(err)}
 css,err:=os.ReadFile("output/styles.css");if err!=nil{panic(err)}
 if !strings.Contains(string(css),".grid-cols-4") {panic("Tailwind CSS missing expected grid utility")}
 abs,err:=filepath.Abs(filepath.Join(out,"day-zero.html"));if err!=nil{panic(err)}
 pdf,err:=filepath.Abs(filepath.Join(out,"day-zero.pdf"));if err!=nil{panic(err)}
 chrome:=os.Getenv("CHROME_BIN");if chrome==""{chrome="google-chrome"}
 cmd:=exec.Command(chrome,"--headless","--no-sandbox","--disable-gpu","--disable-dev-shm-usage","--no-pdf-header-footer","--print-to-pdf="+pdf,"file://"+abs)
 b,err:=cmd.CombinedOutput();if err!=nil{panic(fmt.Sprintf("chromium: %v %s",err,string(b)))}
 data,err:=os.ReadFile(pdf);if err!=nil{panic(err)}
 if len(data)<5||string(data[:5])!="%PDF-"{panic("invalid PDF signature")}
 sum:=sha256.Sum256(data)
 manifest:=map[string]string{"pdf_sha256":hex.EncodeToString(sum[:]),"status":"AWAITING_HUMAN_VISUAL_REVIEW","renderer":"Go html/template + Tailwind CSS + Chromium","svg_policy":"no SVG"}
 m,_:=json.MarshalIndent(manifest,"","  ");if err:=os.WriteFile(filepath.Join(out,"manifest.json"),m,0644);err!=nil{panic(err)}
 fmt.Printf("GO TAILWIND CHROMIUM PASS: %d PDF bytes, SHA256 %x\n",len(data),sum)
}
