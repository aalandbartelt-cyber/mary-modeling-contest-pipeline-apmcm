#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""env_doctor.py — 数模环境体检（Windows / WSL 均可跑）。

用法:
    python scripts/env_doctor.py
    python scripts/env_doctor.py --project /path/to/project
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import sys
from pathlib import Path

ROWS = []


def add(level, name, detail=""):
    ROWS.append((level, name, detail))


def which_any(names):
    for n in names:
        p = shutil.which(n) if not os.path.isabs(n) else (n if Path(n).is_file() else None)
        if p:
            return p
    return None


def check_pkg(mod, label=None):
    ok = importlib.util.find_spec(mod) is not None
    add("PASS" if ok else "WARN", label or mod, "已安装" if ok else "未安装（可选）")
    return ok


def main():
    add("INFO", "平台", f"{sys.platform} / Python {sys.version.split()[0]} / {sys.executable}")

    py = which_any(["python", "python3", "py"])
    add("PASS" if py else "WARN", "Python", py or "不在 PATH（用绝对路径）")

    rs = which_any([
        "Rscript", "Rscript.exe",
        str(Path.home() / "miniconda3/envs/r/bin/Rscript"),
        r"C:\Program Files\R\R-4.5.3\bin\Rscript.exe",
    ])
    add("PASS" if rs else "WARN", "Rscript", rs or "未找到（用绝对路径）")

    soffice = which_any([
        "soffice", "soffice.exe", "soffice.com",
        r"C:\Program Files\LibreOffice\program\soffice.exe",
    ])
    add("PASS" if soffice else "WARN", "LibreOffice", soffice or "未找到（PPTX→PDF 兜底）")

    for mod in ["docx", "pptx", "openpyxl", "lxml", "pypdf"]:
        check_pkg(mod)
    for mod in ["fitz", "pymupdf"]:
        if importlib.util.find_spec(mod):
            add("PASS", "PyMuPDF", mod)
            break
    else:
        add("WARN", "PyMuPDF", "未安装（PDF 渲染/文本检查需要）")

    add("PASS" if sys.platform.startswith("win") else "INFO", "Windows COM",
        "Word/PowerPoint 可尝试 COM" if sys.platform.startswith("win") else "非 Windows；用 LibreOffice/PyMuPDF")
    if sys.platform.startswith("win"):
        try:
            import win32com.client  # noqa: F401
            add("PASS", "pywin32", "已安装")
        except Exception:
            add("WARN", "pywin32", "未安装（Word/PowerPoint COM 不可用）")

    add("PASS" if shutil.which("git") else "WARN", "git", shutil.which("git") or "未找到")
    add("INFO", "gh", shutil.which("gh") or "WSL 下不要直接调 Windows gh.exe")

    fonts = []
    if sys.platform.startswith("win"):
        windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
        for f in ["msyh.ttc", "simsun.ttc", "times.ttf", "cambria.ttc"]:
            if (windir / "Fonts" / f).is_file():
                fonts.append(f)
    add("INFO", "字体", ", ".join(fonts) if fonts else "未检查（Windows Fonts 目录）")

    fails = 0
    for level, name, detail in ROWS:
        print(f"[{level}] {name}: {detail}")
        if level == "FAIL":
            fails += 1
    print(f"\nSUMMARY: {len(ROWS)} checks, {fails} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
