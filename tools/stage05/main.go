// DraftDeck Stage 05: three human-review candidates, never a release decision.
// Provider-routed HTTP interface needs validation against a live authenticated run.
package main

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "errors"
 "fmt"
 "image/png"
 "io"
 "net/http"
 "os"
 "strconv"
 "strings"
 "time"
)

const (
 endpoint = "https://router.huggingface.co/fal-ai/models/black-forest-labs/FLUX.1-dev"
 model = "black-forest-labs/FLUX.1-dev"
 provider = "fal-ai"
 contract = "SCC-02-SLIDE05"
 manifestFile = "SCC-02-SLIDE05-stage05-manifest.json"
 width = 1536
 height = 864
)
const prompt = "Minimalist technical editorial illustration, 16:9 aspect ratio, isometric perspective. A clean, human-operated print-proof registration bench in a neighborhood printing and shipping studio. Left side of the bench: a visually polished but completely blank document packet resting on the surface. Right side of the bench: a blank authoritative source binder and a blank reference-proof tray. Center: an analog mechanical comparison fixture featuring a visibly misregistered pair of alignment pins. Nearby: a blank physical inspection clipboard and a manual comparison lever resting in the unengaged/open position. ABSOLUTELY NO automated scanners, NO robots, and NO digital screens. Pure white background, zero gradients, no solid decorative panels. CAD/ISO standard drafting style, minimalist structural line art. Use cyan, magenta, and black sparingly as strict structural accents only. Compositional constraints: Leave the top span entirely blank for titles. Leave clear white space above the left document packet, above the right source binder, precisely in the center between them, and across the bottom edge. NO TEXT, NO LABELS, NO WATERMARKS, NO TYPOGRAPHY, NO SIMULATED DOCUMENT SQUIGGLES."
const negativePrompt = "text, labels, words, letters, numbers, typography, captions, watermark, signature, handwriting, simulated document squiggles, digital screens, monitors, UI panels, robots, robotic arms, automated scanners, cameras, optical scanning rigs, autonomous machinery, gradients, decorative solid panels"

type Candidate struct {
 Index int `json:"index"`
 FileName string `json:"file_name"`
 Seed int `json:"seed"`
 RequestTimestamp string `json:"request_timestamp"`
 ResponseTimestamp string `json:"response_timestamp,omitempty"`
 HTTPStatus int `json:"http_status,omitempty"`
 ContentType string `json:"content_type,omitempty"`
 SizeBytes int64 `json:"size_bytes,omitempty"`
 SHA256 string `json:"sha256,omitempty"`
 Status string `json:"status"`
 Error string `json:"error,omitempty"`
 RequestParameters map[string]any `json:"request_parameters"`
}

type Manifest struct {
 SchemaVersion string `json:"schema_version"`
 ContractID string `json:"contract_id"`
 Stage string `json:"stage"`
 Status string `json:"status"`
 GeneratedAtUTC string `json:"generated_at_utc"`
 Model string `json:"model"`
 Provider string `json:"provider"`
 Endpoint string `json:"endpoint"`
 OutputFormat string `json:"output_format"`
 Prompt string `json:"prompt"`
 NegativePrompt string `json:"negative_prompt"`
 CandidateCount int `json:"candidate_count"`
 BaseSeed int `json:"base_seed"`
 CommonParameters map[string]any `json:"common_parameters"`
 Candidates []Candidate `json:"candidates"`
}
func timestamp() string { return time.Now().UTC().Format(time.RFC3339Nano) }
func fail(err error) { fmt.Fprintln(os.Stderr, "HOLD:", err); os.Exit(2) }
func truncate(s string, n int) string { if len(s) <= n { return s }; return s[:n]+" [truncated]" }

func main() {
 token := strings.TrimSpace(os.Getenv("HF_TOKEN"))
 if token == "" { fail(errors.New("HF_TOKEN is missing: no inference was attempted")) }
 baseSeed := 42
 if raw := os.Getenv("HF_BASE_SEED"); raw != "" {
  value, err := strconv.Atoi(raw)
  if err != nil || value < 0 || value > 2147483644 { fail(errors.New("HF_BASE_SEED must be an integer from 0 through 2147483644")) }
  baseSeed = value
 }
 common := map[string]any{"negative_prompt":negativePrompt,"guidance_scale":3.5,"num_inference_steps":50,"width":width,"height":height}
 manifest := Manifest{SchemaVersion:"1.0",ContractID:contract,Stage:"05",Status:"IN_PROGRESS",GeneratedAtUTC:timestamp(),Model:model,Provider:provider,Endpoint:endpoint,OutputFormat:"png",Prompt:prompt,NegativePrompt:negativePrompt,CandidateCount:3,BaseSeed:baseSeed,CommonParameters:common,Candidates:make([]Candidate,0,3)}
 client := &http.Client{Timeout:240*time.Second}
 successes := 0
 for i:=1;i<=3;i++ {
  seed:=baseSeed+i-1
  name:=fmt.Sprintf("%s-stage05-candidate-%02d.png",contract,i)
  parameters:=map[string]any{"guidance_scale":3.5,"num_inference_steps":50,"width":width,"height":height,"seed":seed}
  c:=Candidate{Index:i,FileName:name,Seed:seed,Status:"PENDING",RequestTimestamp:timestamp(),RequestParameters:parameters}
  if _, err:=os.Stat(name);err==nil {
   c.Status="ERROR";c.Error="refusing to overwrite an existing candidate"
  } else if !errors.Is(err,os.ErrNotExist) {
   c.Status="ERROR";c.Error=err.Error()
  } else if err:=generate(client,token,seed,name,&c);err!=nil {
   c.Status="ERROR";c.Error=err.Error()
  } else {
   c.Status="OK"; successes++
   fmt.Printf("Saved %s seed=%d sha256=%s\n",name,seed,c.SHA256)
  }
  if c.Status=="ERROR" { fmt.Fprintf(os.Stderr,"Candidate %02d HOLD: %s\n",i,c.Error) }
  manifest.Candidates=append(manifest.Candidates,c)
 }
 switch successes { case 3: manifest.Status="COMPLETED_WITH_CANDIDATES"; case 0: manifest.Status="FAILED"; default: manifest.Status="PARTIAL_SUCCESS" }
 data,err:=json.MarshalIndent(manifest,"","  ");if err!=nil { fail(err) }
 if err=os.WriteFile(manifestFile,append(data,'\n'),0644);err!=nil { fail(err) }
 fmt.Printf("Manifest: %s (%d/3 successful)\n",manifestFile,successes)
 if successes!=3 { os.Exit(1) }
}

func generate(client *http.Client,token string,seed int,path string,c *Candidate) error {
 params:=map[string]any{"negative_prompt":negativePrompt,"guidance_scale":3.5,"num_inference_steps":50,"width":width,"height":height,"seed":seed}
 raw,err:=json.Marshal(map[string]any{"inputs":prompt,"parameters":params})
 if err!=nil{return fmt.Errorf("serialize request: %w",err)}
 req,err:=http.NewRequest(http.MethodPost,endpoint,bytes.NewReader(raw))
 if err!=nil{return fmt.Errorf("create request: %w",err)}
 req.Header.Set("Authorization","Bearer "+token)
 req.Header.Set("Content-Type","application/json")
 req.Header.Set("Accept","image/png,image/jpeg,image/webp,application/json")
 resp,err:=client.Do(req)
 if err!=nil{return fmt.Errorf("network request: %w",err)}
 defer resp.Body.Close()
 c.ResponseTimestamp=timestamp()
 c.HTTPStatus=resp.StatusCode
 c.ContentType=resp.Header.Get("Content-Type")
 body,err:=io.ReadAll(io.LimitReader(resp.Body,35*1024*1024))
 if err!=nil{return fmt.Errorf("read response: %w",err)}
 if resp.StatusCode<200||resp.StatusCode>=300{return fmt.Errorf("HTTP %d: %s",resp.StatusCode,truncate(string(body),900))}
 if strings.ToLower(strings.TrimSpace(strings.Split(c.ContentType,";")[0]))!="image/png" {
  return fmt.Errorf("expected image/png, received %s (provider payload not approved for packaging)",c.ContentType)
 }
 cfg,err:=png.DecodeConfig(bytes.NewReader(body))
 if err!=nil{return fmt.Errorf("invalid PNG: %w",err)}
 if cfg.Width!=width||cfg.Height!=height {
  return fmt.Errorf("wrong dimensions: %dx%d (expected %dx%d)",cfg.Width,cfg.Height,width,height)
 }
 if err:=os.WriteFile(path,body,0644);err!=nil{return fmt.Errorf("write PNG: %w",err)}
 c.SizeBytes=int64(len(body))
 sum:=sha256.Sum256(body)
 c.SHA256=hex.EncodeToString(sum[:])
 return nil
}
