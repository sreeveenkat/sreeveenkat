#!/usr/bin/env python3
"""Build assets/stats.svg and assets/languages.svg from the GitHub API.

Needs the `gh` CLI (logged in, or GH_TOKEN set). Run: python3 scripts/gen_stats.py
"""
import json
import subprocess
import sys
from pathlib import Path

USER = "sreeveenkat"
OUT = Path(__file__).resolve().parent.parent / "assets"
MONO = "'JetBrains Mono','Fira Code',Consolas,'DejaVu Sans Mono',monospace"
PALETTE = ["#2ee6a6", "#38bdf8", "#a78bfa", "#f59e0b", "#ef4444", "#8fb3c4"]


def api(path, *extra):
    r = subprocess.run(["gh", "api", path, *extra], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh api {path} failed: {r.stderr.strip()}")
    return json.loads(r.stdout)


user = api(f"users/{USER}")
repos = [r for r in api(f"users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
stars = sum(r["stargazers_count"] for r in repos)
try:
    commits = api(f"search/commits?q=author:{USER}&per_page=1")["total_count"]
except SystemExit:
    commits = None

langs = {}
for r in repos:
    for lang, n in api(f"repos/{USER}/{r['name']}/languages").items():
        langs[lang] = langs.get(lang, 0) + n
total = sum(langs.values()) or 1
top = sorted(langs.items(), key=lambda kv: -kv[1])[:6]


def frame(w, h, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1117"/><stop offset="1" stop-color="#0a2430"/></linearGradient></defs>
<rect width="{w}" height="{h}" rx="12" fill="url(#bg)" stroke="#1f3b4d"/>
<g font-family="{MONO}">
<circle cx="24" cy="26" r="4" fill="#2ee6a6"/>
<text x="38" y="31" font-size="15" font-weight="700" fill="#2ee6a6">{title}</text>
{body}
</g></svg>'''


rows = [("Public repos", len(repos)), ("Total stars", stars), ("Followers", user["followers"])]
if commits is not None:
    rows.append(("Public commits", commits))
body = []
for i, (label, val) in enumerate(rows):
    y = 68 + i * 30
    body.append(f'<text x="28" y="{y}" font-size="13" fill="#8fb3c4">{label}</text>'
                f'<text x="372" y="{y}" font-size="15" font-weight="700" fill="#f0f6fc" text-anchor="end">{val}</text>'
                f'<line x1="28" y1="{y+10}" x2="372" y2="{y+10}" stroke="#16303d"/>')
(OUT / "stats.svg").write_text(frame(400, 68 + len(rows) * 30 + 6, "GitHub Stats", "\n".join(body)))

body, x, bar_w = [], 28, 344
segs = []
for i, (lang, n) in enumerate(top):
    w = max(bar_w * n / total, 3)
    segs.append(f'<rect x="{x:.1f}" y="52" width="{max(w-2, 1):.1f}" height="10" rx="2" fill="{PALETTE[i]}"/>')
    x += w
body.append("".join(segs))
for i, (lang, n) in enumerate(top):
    cx, cy = 28 + (i % 2) * 176, 92 + (i // 2) * 26
    body.append(f'<circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{PALETTE[i]}"/>'
                f'<text x="{cx+16}" y="{cy}" font-size="13" fill="#c9d4dc">{lang}</text>'
                f'<text x="{cx+158}" y="{cy}" font-size="12" fill="#8fb3c4" text-anchor="end">{100*n/total:.1f}%</text>')
h = 92 + ((len(top) + 1) // 2) * 26 + 6
(OUT / "languages.svg").write_text(frame(400, h, "Top Languages", "\n".join(body)))
print(f"repos={len(repos)} stars={stars} followers={user['followers']} commits={commits} langs={top}")
