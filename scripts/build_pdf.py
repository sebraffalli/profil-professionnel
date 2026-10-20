#!/usr/bin/env python3
"""Génère la version PDF du dossier Markdown, sans extraction ni images."""
from pathlib import Path
import mistune
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "profil-professionnel.md"
OUTPUT = ROOT / "profil-professionnel.pdf"
CSS = r"""
@page {
  size: A4;
  margin: 20mm 19mm 19mm;
  @bottom-right { content: counter(page); font: 8pt sans-serif; color: #64748b; }
}
html { font-family: 'DejaVu Sans', 'Liberation Sans', sans-serif; color: #18263c; }
body { font-size: 9pt; line-height: 1.48; }
h1, h2, h3, h4 { break-after: avoid; page-break-after: avoid; line-height: 1.25; }
h1 { font-size: 17.5pt; color: #0e314d; margin: 24pt 0 9pt; border-bottom: 1px solid #c7dce7; padding-bottom: 5pt; }
h1:first-child { font-size: 23pt; border-bottom: 2px solid #0d628a; }
h2 { font-size: 12pt; color: #155b80; margin: 18pt 0 8pt; }
h3 { font-size: 10.5pt; color: #234966; margin: 13pt 0 6pt; }
p { margin: 0 0 9pt; orphans: 3; widows: 3; }
ul, ol { margin: 3pt 0 9pt; padding-left: 18pt; }
li { margin: 0 0 4pt; }
li p { margin: 0; }
blockquote { margin: 8pt 0 13pt; padding: 8pt 12pt; color: #1b4560; border-left: 3px solid #2c8db1; background: #f1f6f9; }
blockquote p:last-child { margin-bottom: 0; }
strong { font-weight: 700; }
a { color: #17638b; text-decoration: none; }
hr { border: 0; border-top: 1px solid #d2dfe7; margin: 13pt 0; }
code { font-family: monospace; background: #f0f4f6; }
pre { font-size: 8pt; padding: 10pt; white-space: pre-wrap; background: #f0f4f6; }
"""
if __name__ == "__main__":
    markdown = mistune.create_markdown(escape=True)
    body = markdown(SOURCE.read_text(encoding="utf-8"))
    html = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            f'<title>Parcours professionnel — Sébastien Raffalli</title>'
            f'<style>{CSS}</style></head><body>{body}</body></html>')
    HTML(string=html, base_url=ROOT.as_uri() + "/").write_pdf(OUTPUT)
    print(f"{OUTPUT}: {OUTPUT.stat().st_size} octets")
