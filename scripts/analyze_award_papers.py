#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyze_award_papers.py — 统计 APMCM 优秀论文的结构特征（v2 深度版）。

用法:
    python scripts/analyze_award_papers.py --input 优秀论文目录 --out metrics.csv
    python scripts/analyze_award_papers.py --input 优秀论文.zip --out metrics.csv

输出列:
  file, pages, hdr_pages(页眉 Page x of y 的 y,用于发现截断副本),
  summary_words, summary_numbers, figs, tables, images,
  eq_count(编号公式), conc_per_q(每问小结件), key_insights,
  notations, our_work, model_evaluation, sensitivity, appendix_flag,
  code_pages(附录代码页估计), med_body_words(正文页词数中位),
  fig_heavy_pages(词<100 且带图页数)

指标均为启发式近似：用于跨年对比趋势,不做精确断言。
"""
from __future__ import annotations

import argparse
import csv
import re
import statistics
import zipfile
from pathlib import Path

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf


def read_pdf(data: bytes):
    return pymupdf.open(stream=data, filetype="pdf")


def page_words(t: str) -> int:
    return len(re.findall(r"\b[A-Za-z]{2,}\b", t))


def analyze(name: str, data: bytes):
    doc = read_pdf(data)
    pages = [pg.get_text() or "" for pg in doc]
    imgs = [len(pg.get_images(full=True)) for pg in doc]
    doc.close()
    txt = "\n".join(pages)
    n = len(pages)
    first = pages[0] if pages else ""

    m = re.search(r"(?i)(summary|abstract)\s*", first)
    summary = first[m.end():] if m else first

    # 页眉 "Page x of y" —— y 与 pdf 页数不一致说明本地副本被截断
    hdr = [int(y) for t in pages[:6] for y in re.findall(r"(?i)page\s+\d+\s+of\s+(\d+)", t)]
    hdr_pages = max(hdr) if hdr else ""

    body = pages[2:] if n > 3 else pages  # 跳过 summary/contents
    body_w = [page_words(t) for t in body]
    fig_heavy = sum(1 for i, t in enumerate(body) if page_words(t) < 100 and (imgs[i + 2] > 0 or re.search(r"(?i)fig(?:ure)?|picture", t)))

    eqs = re.findall(r"(?m)^\s*\(\d+(?:\.\d+)?\)\s*$", txt)
    cq = len(re.findall(r"(?i)(conclusions?\s+(for|of)\s+(question|problem|task)|short\s+summary|conclusions?\s+of\s+the\s+model)", txt))
    ki = len(re.findall(r"(?i)key\s+(insights?|findings?|results?)", txt))

    code_pages = sum(
        1 for t in pages[int(n * 0.5):]
        if page_words(t) < 40
        or len(re.findall(r"(?m)^\s*(def |import |for |if |return |function |#include|clc|clear)", t)) > 6
    )

    figs = [int(x) for x in re.findall(r"(?i)figure\s+(\d+)", txt)]
    tabs = [int(x) for x in re.findall(r"(?i)table\s+(\d+)", txt)]

    return {
        "file": name,
        "pages": n,
        "hdr_pages": hdr_pages,
        "summary_words": page_words(summary),
        "summary_numbers": len(re.findall(r"\d+(?:\.\d+)?%?", summary)),
        "figs": max(figs) if figs else 0,
        "tables": max(tabs) if tabs else 0,
        "images": sum(imgs),
        "eq_count": len(eqs),
        "conc_per_q": cq,
        "key_insights": ki,
        "notations": int(bool(re.search(r"(?i)notation|symbol\s+(legend|table|description)", txt))),
        "our_work": int(bool(re.search(r"(?i)our works?", txt))),
        "model_evaluation": int(bool(re.search(r"(?i)model evaluation|advantages\s+and\s+(limitations|disadvantages|weakness)", txt))),
        "sensitivity": int(bool(re.search(r"(?i)sensitivity", txt))),
        "appendix_flag": int(bool(re.search(r"(?i)appendix", txt))),
        "code_pages": code_pages,
        "med_body_words": int(statistics.median(body_w)) if body_w else 0,
        "fig_heavy_pages": fig_heavy,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="PDF 目录或 zip")
    ap.add_argument("--out", default="award_paper_metrics.csv")
    args = ap.parse_args()
    src = Path(args.input)
    rows = []
    if src.is_dir():
        pdfs = sorted(src.rglob("*.pdf"))
        for p in pdfs:
            rows.append(analyze(p.name, p.read_bytes()))
    else:
        with zipfile.ZipFile(src) as z:
            for nm in z.namelist():
                if not nm.lower().endswith(".pdf"):
                    continue
                try:
                    name = nm.encode("cp437").decode("gbk")
                except Exception:
                    name = nm
                rows.append(analyze(Path(name).name, z.read(nm)))
    with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {args.out}: {len(rows)} papers")
    for r in rows:
        flag = " <-- TRUNCATED?" if isinstance(r["hdr_pages"], int) and r["hdr_pages"] > r["pages"] + 2 else ""
        print(f"  {r['file']}: {r['pages']}p (hdr {r['hdr_pages']}){flag}")


if __name__ == "__main__":
    main()
