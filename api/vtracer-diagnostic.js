'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const EXPECTED_SOURCE = 'e2fced54d21303aa208aebd862ea3dda03982c7b51aad836d16045f7d940177c';
const EXPECTED_SVG = '04859fc64b2ad845a266c15c8850d3206c3082f0e557193a2eec5da7e0d906ae';
const root = path.resolve(__dirname, '../vtracer-bundle');
const sha256 = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

module.exports = async function handler(req, res) {
  if (req.method !== 'GET') return res.status(405).json({diagnostic:'BOSS-CF-009-P7',status:'FAIL',error:'Method Not Allowed'});
  const start = process.hrtime.bigint();
  try {
    const source = fs.readFileSync(path.join(root,'test_shape.png'));
    const sourceHash = sha256(source);
    if (sourceHash !== EXPECTED_SOURCE) throw new Error('Input fixture SHA-256 mismatch');
    const vtracer = require('../vtracer-bundle/node_modules/@visioncortex/vtracer/index.js');
    const raw = vtracer.convertBuffer(source,{preset:'poster'});
    let svg;
    if (typeof raw === 'string') svg = raw;
    else if (raw instanceof Uint8Array) svg = Buffer.from(raw).toString('utf8');
    else throw new TypeError('Unexpected VTracer output type');
    if (!/<svg(?:\s|>)/.test(svg) || !/<\/svg>\s*$/.test(svg)) throw new Error('SVG boundary invalid');
    const svgHash = sha256(Buffer.from(svg, 'utf8'));
    const matched = svgHash === EXPECTED_SVG;
    const receipt = {
      diagnostic:'BOSS-CF-009-P7',
      status:matched?'PASS':'FAIL',
      node:process.version,
      source_sha256:sourceHash,
      svg_sha256:svgHash,
      expected_svg_sha256:EXPECTED_SVG,
      svg_bytes:Buffer.byteLength(svg,'utf8'),
      svg_paths:(svg.match(/<path\b/g)||[]).length,
      elapsed_ms:Number(process.hrtime.bigint()-start)/1e6,
      comparison:'P6_REFERENCE_SHA256'
    };
    return res.status(matched?200:422).json(receipt);
  } catch (error) {
    return res.status(500).json({diagnostic:'BOSS-CF-009-P7',status:'FAIL',error:error.message});
  }
};
