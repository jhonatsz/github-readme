"""Generate the Matrix-rain profile banner (static SVG, CSS animation only)."""
import random
import sys

W, H = 900, 260
COL_W = 15          # column pitch
GLYPH_H = 16        # vertical pitch of glyphs in a stream
FONT = 14
GLYPHS = "0101010123456789ABCDEF<>/=+*$#{}[]|&%;:"

NAME = "JHONATHAN HOWARD"
PROMPT = "jhonatsz@github:~$ "
TYPED = "Building innovations for the Great Commission"
CHAR_W = 9.0        # forced via textLength so typing steps line up in any font

rnd = random.Random(20261118)


def esc(c):
    return {"<": "&lt;", ">": "&gt;", "&": "&amp;"}.get(c, c)


def stream(x, idx):
    n = rnd.randint(8, 18)
    length = n * GLYPH_H
    dur = round(rnd.uniform(4.5, 11.0), 2)
    delay = round(-rnd.uniform(0, dur), 2)
    spans = []
    for i in range(n):
        c = esc(rnd.choice(GLYPHS))
        y = (i + 1) * GLYPH_H
        if i == n - 1:
            spans.append(f'<tspan x="{x}" y="{y}" class="h">{c}</tspan>')
        else:
            op = round(0.08 + 0.80 * (i / (n - 1)) ** 1.6, 2)
            spans.append(f'<tspan x="{x}" y="{y}" fill-opacity="{op}">{c}</tspan>')
    return (
        f'<g class="s" style="--l:-{length}px;animation-duration:{dur}s;animation-delay:{delay}s">'
        f'<text>{"".join(spans)}</text></g>'
    )


streams = []
for i, x in enumerate(range(8, W, COL_W)):
    streams.append(stream(x, i))
    if rnd.random() < 0.45:      # some columns carry a second stream
        streams.append(stream(x, i))

line = PROMPT + TYPED
line_w = len(line) * CHAR_W
line_x = (W - line_w) / 2
typed_x = line_x + len(PROMPT) * CHAR_W
typed_w = len(TYPED) * CHAR_W
n_typed = len(TYPED)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Jhonathan Howard</title>
<desc id="d">Matrix-style banner: {TYPED}</desc>
<style>
.s{{animation:fall linear infinite;transform:translateY(var(--l))}}
.s text{{font:{FONT}px ui-monospace,SFMono-Regular,Menlo,Consolas,"DejaVu Sans Mono",monospace;fill:#00ff41;text-anchor:middle}}
.s .h{{fill:#d8ffe0}}
@keyframes fall{{from{{transform:translateY(var(--l))}}to{{transform:translateY({H}px)}}}}
.name{{font:700 54px ui-monospace,SFMono-Regular,Menlo,Consolas,"DejaVu Sans Mono",monospace;fill:#00ff41;text-anchor:middle;letter-spacing:4px}}
.line{{font:15px ui-monospace,SFMono-Regular,Menlo,Consolas,"DejaVu Sans Mono",monospace;fill:#00ff41}}
.dim{{fill:#008f11}}
.reveal{{animation:type 9s infinite}}
.cur{{fill:#00ff41;animation:move 9s infinite,blink 1s steps(1) infinite}}
@keyframes type{{0%,8%{{transform:translateX(-{typed_w}px)}}55%,100%{{transform:translateX(0)}}}}
@keyframes move{{0%,8%{{transform:translateX(0)}}55%,100%{{transform:translateX({typed_w}px)}}}}
@keyframes blink{{50%{{opacity:0}}}}
.reveal,.cur{{animation-timing-function:steps({n_typed},end)}}
.cur{{animation-timing-function:steps({n_typed},end),steps(1)}}
@media (prefers-reduced-motion:reduce){{.s{{animation-play-state:paused}}.reveal,.cur{{animation:none}}.reveal{{transform:none}}.cur{{transform:translateX({typed_w}px)}}}}
</style>
<defs>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="10"/></clipPath>
<clipPath id="typed"><rect class="reveal" x="{typed_x}" y="150" width="{typed_w}" height="30"/></clipPath>
<radialGradient id="shade" cx="50%" cy="50%" r="50%" gradientTransform="translate(0.5 0.5) scale(1 0.62) translate(-0.5 -0.5)">
<stop offset="0" stop-color="#0d0208" stop-opacity="0.96"/>
<stop offset="0.55" stop-color="#0d0208" stop-opacity="0.9"/>
<stop offset="1" stop-color="#0d0208" stop-opacity="0"/>
</radialGradient>
<filter id="glow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="#0d0208"/>
{chr(10).join(streams)}
<rect width="{W}" height="{H}" fill="url(#shade)"/>
<text class="name" x="{W / 2}" y="128" filter="url(#glow)">{NAME}</text>
<text class="line dim" x="{line_x}" y="170" textLength="{len(PROMPT) * CHAR_W - CHAR_W}" lengthAdjust="spacingAndGlyphs">{PROMPT.rstrip()}</text>
<g clip-path="url(#typed)"><text class="line" x="{typed_x}" y="170" textLength="{typed_w}" lengthAdjust="spacingAndGlyphs">{TYPED}</text></g>
<rect class="cur" x="{typed_x + 1}" y="157" width="8" height="16"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="none" stroke="#003b00"/>
</svg>
'''
open(sys.argv[1], "w", encoding="utf-8").write(svg)
print(len(svg), "bytes,", len(streams), "streams")
