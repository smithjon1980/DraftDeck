#!/usr/bin/env python3
"""Render authorized local DraftDeck HTML in Chromium without HTTP navigation.
Python Playwright and Chromium are prerequisites. Does not install design skills,
authorize release, test manuscript accuracy, or certify printer readiness.
Only use with trusted local HTML; JavaScript is disabled and HTTP requests blocked.
"""
import argparse
import base64
import hashlib
import json
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

IMAGE_EXTS = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html_file", type=Path)
    ap.add_argument("--image-dir", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--pages", type=int, default=2)
    ap.add_argument("--chromium", default="/usr/bin/chromium")
    args = ap.parse_args()
    if not args.html_file.is_file():
        ap.error("HTML file does not exist")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    html = args.html_file.read_text(encoding="utf-8")

    def replace(m):
        filename = m.group(1)
        if filename != Path(filename).name:
            raise ValueError("Image source must be a local basename: " + filename)
        path = args.image_dir / filename
        ext = path.suffix.lower()
        if ext not in IMAGE_EXTS or not path.is_file():
            raise ValueError("Missing or unsupported local art: " + filename)
        enc = base64.b64encode(path.read_bytes()).decode("ascii")
        return 'src="data:' + IMAGE_EXTS[ext] + ';base64,' + enc + '"'

    html = re.sub(r'src="([A-Za-z0-9_.-]+\.(?:png|jpg|jpeg|webp))"',
                  replace, html, flags=re.I)
    results = {
        "status": "PASS", "source": str(args.html_file), "pages": [],
        "manual_visual_approval": "PENDING", "printer_acceptance": "NOT_TESTED"
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=args.chromium, headless=True,
                                    args=["--no-sandbox"])
        context = browser.new_context(
            viewport={"width": 1750, "height": 1150}, java_script_enabled=False)
        context.route("**/*", lambda route: route.abort())
        page = context.new_page()
        page.set_content(html, wait_until="load")
        elements = page.locator(".page")
        count = elements.count()
        if count != args.pages:
            results["status"] = "FAIL"
        for index in range(count):
            elem = elements.nth(index)
            elem.screenshot(path=str(args.output_dir / f"page_{index+1:02}.png"))
            stats = elem.evaluate("""el => {
                const r = el.getBoundingClientRect();
                const paras = [...el.querySelectorAll('.spoken')].map(x=>x.innerText);
                return {
                  width:r.width,height:r.height,paragraphs:paras.length,
                  selected_text_chars:paras.reduce((n,t)=>n+t.length,0),
                  image_count:el.querySelectorAll('img').length,
                  page_overflow:el.scrollHeight>el.clientHeight+1 ||
                                el.scrollWidth>el.clientWidth+1
                };
            }""")
            if stats["page_overflow"] or abs(stats["width"] - 1632) > 1 \
                    or abs(stats["height"] - 1056) > 1:
                results["status"] = "FAIL"
            results["pages"].append(stats)
        pdf_path = args.output_dir / "proof.pdf"
        page.pdf(
            path=str(pdf_path), width="17in", height="11in",
            print_background=True, prefer_css_page_size=True,
            margin={"top":"0","bottom":"0","left":"0","right":"0"}
        )
        results["pdf_sha256"] = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
        results["render_method"] = (
            "Python Playwright + local Chromium; JS off; no HTTP navigation")
        browser.close()
    (args.output_dir / "render_result.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    raise SystemExit(0 if results["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
