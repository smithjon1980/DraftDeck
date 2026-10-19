// Browser-only QA for two synthetic React/Tailwind slides.
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import puppeteer from "puppeteer";

const project = path.resolve(import.meta.dirname, "..");
const dir = path.join(project, "dist");
const screenshots = path.join(project, "screenshots");
fs.mkdirSync(screenshots, {recursive: true});
const executablePath = process.env.CHROME_BIN || "/usr/bin/google-chrome";
const browser = await puppeteer.launch({
  executablePath, headless: true,
  args: ["--no-sandbox", "--disable-setuid-sandbox", "--allow-file-access-from-files"],
});
const reports = [];
try {
  for (let i = 1; i <= 2; i += 1) {
    const page = await browser.newPage();
    await page.setViewport({width: 1920, height: 1080, deviceScaleFactor: 1});
    const errors = [];
    page.on("pageerror", (error) => errors.push(error.message));
    const url = pathToFileURL(path.join(dir, "index.html")).href + "?slide=" + i;
    await page.goto(url, {waitUntil: "load", timeout: 45000});
    await page.waitForSelector("#slide[data-render-master='react-tailwind']");
    await page.evaluate(async () => { await document.fonts.ready; });
    const result = await page.evaluate(() => {
      const root = document.querySelector("#slide");
      const bbox = root.getBoundingClientRect();
      const diagram = root.querySelector("section img");
      const text = root.innerText;
      return {
        id: root.getAttribute("data-slide-id"),
        width: bbox.width, height: bbox.height,
        rootTextNodes: root.querySelectorAll("h1,h2,p").length,
        realHeading: root.querySelector("h1")?.textContent?.trim() || "",
        hasValidDiagram: Boolean(diagram?.complete && diagram.naturalWidth > 0 && diagram.naturalHeight > 0),
        renderedDiagramWidth: diagram?.naturalWidth || 0,
        sourceSVGIsSeparate: diagram?.tagName === "IMG",
        hasHold: text.toUpperCase().includes("HOLD"),
        hasReflection: text.includes("REFLECT"),
        noRetiredWaveform: !text.toLowerCase().includes("waveform"),
      };
    });
    if (errors.length) throw new Error("JavaScript errors: " + JSON.stringify(errors));
    if (result.width !== 1920 || result.height !== 1080) throw new Error("Wrong canvas: " + JSON.stringify(result));
    if (!result.hasValidDiagram || !result.sourceSVGIsSeparate) throw new Error("Missing rendered SVG: " + JSON.stringify(result));
    if (result.rootTextNodes < 10 || !result.hasReflection || !result.hasHold || !result.noRetiredWaveform) {
      throw new Error("Missing native text, reflection, or HOLD: " + JSON.stringify(result));
    }
    const name = ["flowchart", "sequence"][i-1];
    await page.screenshot({path: path.join(screenshots, name + ".png"), type: "png"});
    await page.pdf({path: path.join(screenshots, name + ".pdf"),
      width: "1920px", height: "1080px", printBackground: true, preferCSSPageSize: false});
    reports.push({...result, browserErrors: errors, browserCapture: name + ".png",
      result: "STRUCTURAL_AND_BROWSER_PASS", visualApproval: "NOT_TESTED",
      semanticApproval: "NOT_TESTED", logoApproval: "PENDING"});
    await page.close();
  }
} finally {
  await browser.close();
}
fs.writeFileSync(path.join(screenshots,"report.json"), JSON.stringify({
  evidence_scope: "real Mermaid + PlantUML SVG in React/Tailwind browser frame; synthetic only",
  engine_rendered: true, model_inference: "NOT_EXECUTED",
  human_approval: "PENDING", results: reports
}, null, 2) + "\n");
console.log(JSON.stringify(reports.map(x=>({slide:x.id,result:x.result,diagramWidth:x.renderedDiagramWidth}))));
