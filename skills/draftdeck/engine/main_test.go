package main
import ("os";"path/filepath";"strings";"testing")
func TestChecksum(t *testing.T){if checksum([]byte("abc"))!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"{t.Fatal("bad hash")}}
func TestRejectSVG(t *testing.T){for _,s:=range []string{"<svg viewBox='0 0 4 4'>","IMAGE/SVG+XML"}{if !containsSVG(s){t.Fatalf("accepted %s",s)}}}
func TestRejectTraversal(t *testing.T){for _,s:=range []string{"../bad.png","nested/bad.png","bad.svg"}{if _,err:=readSafeAsset(t.TempDir(),s);err==nil{t.Errorf("accepted %s",s)}}}
func TestRejectOversizedStory(t *testing.T){root:=t.TempDir();f,err:=os.Create(filepath.Join(root,"huge.png"));if err!=nil{t.Fatal(err)};if err=f.Truncate(maxStoryBytes+1);err!=nil{t.Fatal(err)};f.Close();_,err=readSafeAsset(root,"huge.png");if err==nil||!strings.Contains(err.Error(),"SIZE_LIMIT"){t.Fatalf("expected bound: %v",err)}}
func TestRejectMalformedStory(t *testing.T){root:=t.TempDir();os.WriteFile(filepath.Join(root,"bad.png"),[]byte("abc"),0600);if _,err:=readSafeAsset(root,"bad.png");err==nil{t.Fatal("accepted malformed PNG")}}
func TestRejectOversizedScene(t *testing.T){p:=filepath.Join(t.TempDir(),"scene.json");f,_:=os.Create(p);f.Truncate(maxSceneBytes+1);f.Close();_,err:=readBounded(p,maxSceneBytes);if err==nil{t.Fatal("accepted oversized scene")}}
func TestMalformedScene(t *testing.T){root:=t.TempDir();p:=filepath.Join(root,"scene.json");os.WriteFile(p,[]byte("{"),0600);if err:=run(p,filepath.Join(root,"output"),"unused");err==nil{t.Fatal("accepted malformed JSON")}}
