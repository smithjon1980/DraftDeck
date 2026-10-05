#!/usr/bin/env python3
"""Build self-contained static Canva-import HTML from an explicit scene JSON."""
import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path


def num(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('Coordinates and sizes must be numbers')
    return str(value)


def build(scene, root):
    w, h = scene.get('width', 1920), scene.get('height', 1080)
    if w <= 0 or h <= 0 or w * 9 != h * 16:
        raise ValueError('Use exact positive 16:9 dimensions')
    content = []
    for layer in scene['layers']:
        style = f"position:absolute;left:{num(layer['x'])}px;top:{num(layer['y'])}px;margin:0;padding:0;"
        for key in ('width', 'height'):
            if key in layer:
                style += f'{key}:{num(layer[key])}px;'
        if 'rotation' in layer:
            style += f"transform:rotate({num(layer['rotation'])}deg);transform-origin:center;"
        if layer['type'] == 'image':
            path = (root / layer['path']).resolve()
            mime = mimetypes.guess_type(path.name)[0]
            if mime not in ('image/png', 'image/jpeg', 'image/svg+xml', 'image/webp'):
                raise ValueError('Unsupported artwork file type')
            uri = f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()
            content.append(f'<img alt="{html.escape(layer.get("alt", "Separate artwork"), quote=True)}" src="{uri}" style="{html.escape(style, quote=True)}">')
        elif layer['type'] == 'text':
            style += f"font-family:{layer.get('font', 'Arial')};font-size:{num(layer.get('size', 24))}px;font-weight:{layer.get('weight', 'normal')};color:{layer.get('color', '#1A1A1A')};line-height:{num(layer.get('line_height', 1.1))};white-space:pre-wrap;"
            content.append(f'<div style="{html.escape(style, quote=True)}">{html.escape(layer["text"])}</div>')
        elif layer['type'] == 'border':
            style += f"border:{num(layer.get('stroke', 1))}px solid {layer.get('color', '#1A1A1A')};background:transparent;"
            content.append(f'<div style="{html.escape(style, quote=True)}"></div>')
        else:
            raise ValueError('Unknown layer type')
    title = html.escape(scene.get('title', 'Layered slide'))
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>html,body{{margin:0;padding:0;background:white}}*{{box-sizing:border-box}}</style></head><body><section data-document-role="page" data-label="{html.escape(scene.get("title", "Slide"), quote=True)}" style="position:relative;width:{num(w)}px;height:{num(h)}px;overflow:hidden;background:{html.escape(scene.get("background", "#FFFFFF"), quote=True)}">'+''.join(content)+'</section></body></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scene', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    scene = json.loads(args.scene.read_text())
    result = build(scene, args.scene.parent)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result)
    print(json.dumps({'output': str(args.output.resolve()), 'width': scene.get('width', 1920), 'height': scene.get('height', 1080), 'text_layers': sum(x['type']=='text' for x in scene['layers']), 'image_layers': sum(x['type']=='image' for x in scene['layers'])}))


if __name__ == '__main__':
    main()
