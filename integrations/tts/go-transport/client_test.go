package kokororest

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestRESTOnly(t *testing.T) {
	calls := 0
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls++
		if r.URL.Path != "/v1/audio/speech" || r.Method != "POST" {
			t.Errorf("unexpected route %s", r.URL.Path)
		}
		var body SpeechRequest
		if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
			t.Error(err)
		}
		if body.Model != "kokoro" || body.Input != "one exact spoken sentence" || body.Voice != "af_heart" || body.ResponseFormat != "wav" {
			t.Errorf("bad payload %+v", body)
		}
		w.Header().Set("Content-Type", "audio/wav")
		w.Write(append([]byte("RIFF"), append(make([]byte, 4), []byte("WAVEfmt ")...)...))
	}))
	defer srv.Close()
	audio, err := Client{BaseURL: srv.URL}.Synthesize(context.Background(), "one exact spoken sentence", "af_heart")
	if err != nil || len(audio) < 12 || calls != 1 {
		t.Fatalf("audio %d calls %d err %v", len(audio), calls, err)
	}
}
func TestRejectInvalid(t *testing.T) {
	if _, err := (Client{BaseURL: "file:///tmp"}).Synthesize(context.Background(), "one", "af_heart"); err == nil {
		t.Fatal("bad URL accepted")
	}
	if _, err := (Client{BaseURL: "http://localhost:8880"}).Synthesize(context.Background(), "", "af_heart"); err == nil {
		t.Fatal("empty input accepted")
	}
}
