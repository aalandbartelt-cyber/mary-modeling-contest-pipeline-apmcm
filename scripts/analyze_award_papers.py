#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyze_award_papers.py — 统计 APMCM 优秀论文的页数/摘要/图表结构。

用法:
    python scripts/analyze_award_papers.py --input 优秀论文.zip --out metrics.csv
    python scripts/analyze_award_papers.py --input 优秀论文目录 --out metrics.csv

输出列:
  file, pages, summary_words, summary_numbers, contents_page, refs_page,
  body_pages, figs, tables, images, our_work, model_evaluation, sensitivity, appendix
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import zipfile
from pathlib import Path

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf


def read_pdf(data: bytes):
    return pymupdf.open(stream=data, filetype="pdf")


def analyze(name: str, data: bytes):
    doc = read_pdf(data)
    pages = [pg.get_text() or "" for pg in doc]
    txt = "\n".join(pages)
    first = pages[0] if pages else ""
    m = re.search(r"(?i)(summary|abstract)\s*", first)
    summary = first[m.end():] if m else first
    contents = None
    for i, t in enumerate(pages[:5]):
        if re.search(r"(?i)\bcontents\b", t):
            contents = i + 1
            break
    refs = None
    for i in range(2, len(pages)):
        if re.search(r"(?im)^\s*(?:[IVX]+\.\s*)?(references|bibliography)\s*$", pages[i]):
            refs = i + 1
            break
    body = (refs - 2) if refs else None
    figs = [int(x) for x in re.findall(r"(?i)figure\s+(\d+)", txt)]
    tabs = [int(x) for x in re.findall(r"(?i)table\s+(\d+)", txt)]
    labels = {
        "our_work": bool(re.search(r"(?i)our works?", txt)),
        "model_evaluation": bool(re.search(r"(?i)model evaluation", txt)),
        "sensitivity": bool(re.search(r"(?i)sensitivity", txt)),
        "appendix": bool(re.search(r"(?i)appendix", txt)),
    }
    row = {
        "file": name,
        "pages": len(pages),
        "summary_words": len(re.findall(r"\b[A-Za-z]{2,}\b", summary)),
        "summary_numbers": len(re.findall(r"\d+(?:\.\d+)?%?", summary)),
        "contents_page": contents,
        "refs_page": refs,
        "body_pages": body,
        "figs": max(figs) if figs else 0,
        "tables": max(tabs) if tabs else 0,
        "images": sum(len(pg.get_images(full=True)) for pg in doc),
        **labels,
    }
    doc.close()
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="PDF 目录或 zip")
    ap.add_argument("--out", default="award_paper_metrics.csv")
    args = ap.parse_args()
    src = Path(args.input)
    rows = []
    if src.is_dir():
        for p in sorted(src.glob("*.pdf")):
            rows.append(analyze(p.name, p.read_bytes()))
    else:
        with zipfile.ZipFile(src) as z:
            for n in z.namelist():
                if not n.lower().endswith(".pdf"):
                    continue
                try:
                    name = n.encode("cp437").decode("gbk")
                except Exception:
                    name = n
                rows.append(analyze(Path(name).name, z.read(n)))
    with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {args.out}: {len(rows)} papers")


if __name__ == "__main__":
    main()
