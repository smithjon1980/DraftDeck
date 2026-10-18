#!/usr/bin/env python3
"""Generate deliberately fake test art; no logos, customer data, or project assets."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

D = Path(__file__).with_name('synthetic')
D.mkdir(exist_ok=True)
font = ImageFont.load_default()
for kind in ('logo_top_right', 'offbrand_accent', 'compliant'):
    im = Image.new('RGB', (1600, 1035), '#FFFFFF')
    d = ImageDraw.Draw(im)
    d.rectangle((55, 48, 1545, 986), outline='#111111', width=3)
    d.text((85, 100), 'SYNTHETIC TEST — NOT A BOSS DESIGN', fill='#000000', font=font)
    d.text((85, 170), 'Software executes. Humans release.', fill='#000000', font=font)
    d.line((85, 260, 1510, 260), fill='#00BCEB', width=8)
    d.line((85, 279, 1510, 279), fill=('#EC6C18' if kind=='offbrand_accent' else '#E30074'), width=8)
    d.rectangle((160, 375, 1100, 760), outline='#222222', width=5)
    d.line((200, 710, 1080, 390), fill='#111111', width=8)
    d.arc((270, 400, 750, 730), 0, 250, fill='#111111', width=6)
    if kind == 'logo_top_right':
        b = (1270, 48, 1515, 135)
    else:
        b = (1270, 855, 1515, 943)
    d.rectangle(b, fill='#FFFFFF', outline='#000000', width=5)
    d.text((b[0]+15,b[1]+33), 'BRAND MARKER', fill='#000000', font=font)
    im.save(D / f'{kind}.png')
print('Generated 3 synthetic test images in', D)
