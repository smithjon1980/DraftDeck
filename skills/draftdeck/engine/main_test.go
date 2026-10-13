package main
import "testing"
func TestChecksum(t *testing.T){if checksum([]byte("abc"))!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"{t.Fatal("bad hash")}}
func TestRejectSVG(t *testing.T){s:="<svg viewBox='0 0 4 4'>";if !containsSVG(s){t.Fatal("SVG accepted")}}
