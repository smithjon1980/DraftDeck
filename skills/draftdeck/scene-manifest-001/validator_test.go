package scenevalidation
import ("strings";"testing")
func fixture() Manifest {m:=Manifest{};m.Canvas.Width=1600;m.Canvas.Height=900;m.Elements=[]Element{{Layer:"art",ID:"a",Z:10,Component:"container-box",Bounds:Bounds{X:1,Y:1,Width:100,Height:100},Tokens:[]string{"stroke-2"},Links:[]string{"b"}},{Layer:"text",ID:"b",Z:20,Bounds:Bounds{X:120,Y:1,Width:100,Height:100}}};return m}
func TestGeometry(t *testing.T){m:=fixture();if e:=ValidateBounds(m);e!=nil{t.Fatal(e)};m.Elements[0].Bounds.Width=1601;if ValidateBounds(m)==nil{t.Fatal("overflow accepted")}}
func TestIDsLinks(t *testing.T){m:=fixture();if e:=ValidateLinks(m);e!=nil{t.Fatal(e)};m.Elements[1].ID="a";if ValidateLinks(m)==nil{t.Fatal("duplicate accepted")};m=fixture();m.Elements[0].Links=[]string{"missing"};if ValidateLinks(m)==nil{t.Fatal("orphan accepted")}}
func TestTokens(t *testing.T){m:=fixture();m.Elements[0].Tokens=[]string{"unapproved"};if ValidateTokens(m)==nil{t.Fatal("unapproved token accepted")}}
func TestLayers(t *testing.T){m:=fixture();m.Elements[0].Z=20;if ValidateLayers(m)==nil{t.Fatal("invalid stratification accepted")}}
func TestProvenanceHolds(t *testing.T){m:=fixture();if err:=ValidateProvenance(m);err==nil||!strings.Contains(err.Error(),"NOT_ESTABLISHED"){t.Fatalf("expected HOLD, got %v",err)}}
