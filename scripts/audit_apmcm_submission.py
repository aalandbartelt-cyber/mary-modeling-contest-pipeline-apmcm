#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_apmcm_submission.py — APMCM 论文 PDF / control sheet / support ZIP 检查。

用法:
    python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf
    python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf \
        --control Aapmcm2600001cns.pdf --zip Aapmcm2600001fj.zip

检查:
  - 文件名是否符合 <题号><队号>.pdf
  - 第 1 页 summary / Problem Chosen / Team Number / Keywords
  - 第 2 页 Contents
  - 正文 ≤25 页（summary+contents 之后，references 之前）
  - 页眉 Team # / Page x of y
  - 正文/图表无中文（CJK）
  - 正文无姓名/学校/邮箱等身份信息
  - PDF 元数据
  - control sheet 单独存在且命名正确
  - 支撑 ZIP 完整性/体积/身份/缓存

退出码: 0 通过（可有 WARN），1 有 FAIL。
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

RESULT = []
CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
ID = re.compile(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|\b(University|College|School|Advisor|Professor|指导教师)\b", re.I)
NAME_RE = re.compile(r"^[ABCD]apmcm\d{4,}\.pdf$", re.I)


def add(level, title, detail=""):
    RESULT.append((level, title, detail))


def audit_pdf(path: Path):
    if not path.is_file():
        add("FAIL", "论文 PDF 不存在", str(path)); return
    add("PASS" if NAME_RE.match(path.name) else "FAIL", "论文文件名",
        path.name + (" 符合 <题号><队号>.pdf" if NAME_RE.match(path.name) else " 应为 Aapmcm26XXXXX.pdf"))
    add("PASS" if path.stat().st_size / 1024 / 1024 <= 20 else "WARN", "PDF 体积",
        f"{path.stat().st_size/1024/1024:.2f} MB")

    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            add("SKIP", "PDF 深度检查", "未安装 PyMuPDF"); return

    doc = pymupdf.open(path)
    try:
        n = doc.page_count
        pages = [doc[i].get_text() or "" for i in range(n)]
        add("INFO", "PDF 页数", str(n))
        p1 = pages[0] if pages else ""
        low1 = p1.lower()
        add("PASS" if "summary" in low1 else "FAIL", "第 1 页 Summary", "检出" if "summary" in low1 else "未检出")
        add("PASS" if "problem chosen" in low1 or "team number" in low1 else "WARN", "Summary 头部",
            "Problem Chosen/Team Number")
        add("PASS" if ("keyword" in low1 or "key words" in low1) else "WARN", "Keywords",
            "检出" if ("keyword" in low1 or "key words" in low1) else "未检出")

        p2 = pages[1].lower() if len(pages) > 1 else ""
        add("PASS" if "contents" in p2 or "table of contents" in p2 else "FAIL", "第 2 页 Contents",
            "检出" if ("contents" in p2 or "table of contents" in p2) else "未检出")

        text = "\n".join(pages)
        ref_page = None
        ref_re = re.compile(r"(?m)^\s*(?:[IVX]+\.\s*)?(References|Bibliography)\s*$", re.I)
        for i in range(2, len(pages)):
            if ref_re.search(pages[i]):
                ref_page = i + 1
                break
        if ref_page:
            body = ref_page - 2
            add("PASS" if body <= 25 else "FAIL", "正文页数 ≤25", f"约 {body} 页（References p{ref_page}）")
            body_pages = pages[2:ref_page-1]
        else:
            add("WARN", "未定位 References", "无法计算正文页数")
            body_pages = pages[2:]

        # Official APMCM PDFs may contain a repeated Chinese watermark/header line.
        # Remove lines repeated on most body pages before scanning for real Chinese text.
        from collections import Counter
        freq = Counter(line.strip() for t in body_pages for line in t.splitlines() if line.strip())
        repeated = {line for line, c in freq.items()
                    if c >= max(3, int(0.5 * len(body_pages))) and CJK.search(line)}
        body_text = "\n".join(
            "\n".join(line for line in t.splitlines() if line.strip() not in repeated)
            for t in body_pages
        )

        # header on body pages
        bad_header = []
        for i in range(2, (ref_page - 1) if ref_page else n):
            t = pages[i]
            head = "\n".join(t.splitlines()[:4])
            if not (re.search(r"Team\s*#", head, re.I) and re.search(r"Page\s+\d+\s+of\s+\d+", head, re.I)):
                bad_header.append(i + 1)
        add("PASS" if not bad_header else "WARN", "页眉 Team # / Page x of y",
            "全部通过" if not bad_header else f"{len(bad_header)} 页异常，例 {bad_header[:8]}")

        # Chinese in body (not appendix)
        cjk = CJK.findall(body_text)
        add("PASS" if not cjk else "FAIL", "正文中文扫描", f"{len(cjk)} 个 CJK 字符" if cjk else "0 命中")
        # identity in body
        ids = sorted(set(m.group(0) for m in ID.finditer(body_text)))
        add("PASS" if not ids else "FAIL", "正文身份信息", str(ids[:8]) if ids else "0 命中")

        md = doc.metadata or {}
        dirty = {k: v for k, v in md.items()
                 if k in ("author", "creator", "producer", "title", "subject", "keywords")
                 and v and not re.fullmatch(r"Microsoft.?\s*Word.*|WPS.*|LibreOffice.*|.*PDF.*|TeX|pdfTeX.*|LaTeX.*|Overleaf.*", str(v))}
        add("FAIL" if dirty else "PASS", "PDF 元数据", str(dirty) if dirty else "干净")
    finally:
        doc.close()


def audit_control(path: Path | None):
    if path is None:
        add("WARN", "Control sheet", "未提供（提交前必须单独签名上传）"); return
    if not path.is_file():
        add("FAIL", "Control sheet 不存在", str(path)); return
    add("PASS" if re.search(r"[ABCD]apmcm\d+cns\.(pdf|jpe?g|png)$", path.name, re.I) else "FAIL",
        "Control sheet 命名", path.name)
    add("INFO", "Control sheet 体积", f"{path.stat().st_size/1024:.1f} KB")


def audit_zip(path: Path | None):
    if path is None:
        add("INFO", "支撑材料", "未提供（可选）"); return
    if not path.is_file():
        add("FAIL", "支撑 ZIP 不存在", str(path)); return
    add("PASS" if path.stat().st_size / 1024 / 1024 <= 200 else "WARN", "支撑 ZIP 体积",
        f"{path.stat().st_size/1024/1024:.2f} MB")
    try:
        with zipfile.ZipFile(path) as z:
            add("PASS" if z.testzip() is None else "FAIL", "ZIP 完整性", "OK" if z.testzip() is None else "bad")
            names = [n for n in z.namelist() if not n.endswith("/")]
            add("INFO", "ZIP 条目数", str(len(names)))
            bad = [n for n in names if "__pycache__" in n or n.endswith((".pyc", ".pyo"))
                   or "/.venv/" in n or "/node_modules/" in n]
            add("PASS" if not bad else "FAIL", "ZIP 环境/缓存", str(bad[:8]) if bad else "无")
            hits = []
            for n in names:
                try: s = z.read(n).decode("utf-8", "ignore")
                except Exception: continue
                if ID.search(s): hits.append(n)
            add("PASS" if not hits else "WARN", "ZIP 身份信息", str(hits[:8]) if hits else "0 命中")
    except zipfile.BadZipFile as e:
        add("FAIL", "ZIP 无法读取", str(e))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", type=Path, required=True)
    ap.add_argument("--control", type=Path)
    ap.add_argument("--zip", type=Path)
    args = ap.parse_args()
    audit_pdf(args.paper)
    audit_control(args.control)
    audit_zip(args.zip)
    fails = 0
    for level, title, detail in RESULT:
        print(f"[{level}] {title}: {detail}")
        if level == "FAIL": fails += 1
    print(f"\nSUMMARY: {len(RESULT)} checks, {fails} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
