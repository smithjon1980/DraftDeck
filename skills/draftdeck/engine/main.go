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
const maxStoryBytes int64 = 10 << 20
const maxSceneBytes int64 = 1 << 20
func readBounded(path string,limit int64)([]byte,error){
 f,err:=os.Open(path);if err!=nil{return nil,err};defer f.Close()
 data,err:=io.ReadAll(io.LimitReader(f,limit+1));if err!=nil{return nil,err}
 if int64(len(data))>limit{return nil,errors.New("INPUT_SIZE_LIMIT_EXCEEDED")}
 return data,nil
}
func readSafeAsset(root,name string)([]byte,error){
 if name==""||filepath.Base(name)!=name||strings.Contains(name,".."){return nil,errors.New("UNSAFE_ASSET_PATH")}
 ext:=strings.ToLower(filepath.Ext(name));if ext!=".png"&&ext!=".webp"{return nil,errors.New("STORY_ASSET_MUST_BE_PNG_OR_WEBP")}
 b,err:=readBounded(filepath.Join(root,name),maxStoryBytes);if err!=nil{return nil,err}
 if ext==".png"&&(len(b)<8||!strings.HasPrefix(string(b),"\x89PNG\r\n\x1a\n")){return nil,errors.New("PNG_SIGNATURE_INVALID")}
 if ext==".webp"&&(len(b)<12||string(b[:4])!="RIFF"||string(b[8:12])!="WEBP"){return nil,errors.New("WEBP_SIGNATURE_INVALID")}
 return b,nil
}
func run(scenePath,out,chrome string)error{
 bytes,err:=readBounded(scenePath,maxSceneBytes);if err!=nil{return err}
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
func containsSVG(s string)bool{return strings.Contains(strings.ToLower(s),"<svg")||strings.Contains(strings.ToLower(s),"image/svg+xml")}
func main(){if len(os.Args)!=3{fmt.Fprintln(os.Stderr,"usage: go run . <scene.json> <output-dir>");os.Exit(2)};if err:=run(os.Args[1],os.Args[2],os.Getenv("CHROME_BIN"));err!=nil{fmt.Fprintln(os.Stderr,"HOLD:",err);os.Exit(1)}}

