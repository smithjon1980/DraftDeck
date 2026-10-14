// Package kokororest defines the REST-only transport boundary for the Go manufacturing supervisor.
// It deliberately contains no MCP client and grants no release authority.
package kokororest

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"time"
)

const limit = 16 << 20

type Client struct {
	BaseURL string
	HTTP    *http.Client
}

type SpeechRequest struct {
	Model          string  `json:"model"`
	Input          string  `json:"input"`
	Voice          string  `json:"voice"`
	ResponseFormat string  `json:"response_format"`
	Speed          float64 `json:"speed"`
}

// Synthesize performs exactly one typed POST to /v1/audio/speech with given words.
// Source script approval, IPA authorization, and spoken-fidelity auditing are external gates.
func (c Client) Synthesize(ctx context.Context, words, voice string) ([]byte, error) {
	if strings.TrimSpace(words) == "" || len(words) > 12000 || len(voice) > 80 || voice == "" {
		return nil, errors.New("invalid bounded TTS input")
	}
	if strings.ContainsAny(voice, " /\\\t\n") {
		return nil, errors.New("invalid voice")
	}
	u, err := url.Parse(c.BaseURL)
	if err != nil || u == nil || (u.Scheme != "http" && u.Scheme != "https") || u.Host == "" || u.User != nil || u.RawQuery != "" || u.Fragment != "" {
		return nil, errors.New("invalid configured REST base URL")
	}
	payload := SpeechRequest{Model: "kokoro", Input: words, Voice: voice, ResponseFormat: "wav", Speed: 1.0}
	body, err := json.Marshal(payload)
	if err != nil {
		return nil, err
	}
	dest := strings.TrimRight(c.BaseURL, "/") + "/v1/audio/speech"
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, dest, bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")
	hc := c.HTTP
	if hc == nil {
		hc = &http.Client{Timeout: 5 * time.Minute}
	}
	resp, err := hc.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("tts http status %d", resp.StatusCode)
	}
	if resp.ContentLength > limit {
		return nil, errors.New("tts response too large")
	}
	audio, err := io.ReadAll(io.LimitReader(resp.Body, limit+1))
	if err != nil {
		return nil, err
	}
	if len(audio) > limit {
		return nil, errors.New("tts response too large")
	}
	if len(audio) < 12 || !bytes.Equal(audio[:4], []byte("RIFF")) || !bytes.Equal(audio[8:12], []byte("WAVE")) {
		return nil, errors.New("tts response not wav")
	}
	return audio, nil
}
