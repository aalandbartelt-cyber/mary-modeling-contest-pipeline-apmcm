#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_git_hygiene.py — 提交/推送前的仓库卫生检查。

用法:
    python scripts/audit_git_hygiene.py --root .
    python scripts/audit_git_hygiene.py --root . --max-untracked-mb 100 --max-file-mb 50
    python scripts/audit_git_hygiene.py --root . --check-push

检查:
  1. git 仓库/分支/remote
  2. tracked 修改、未跟踪文件数量与体积
  3. 未跟踪大文件（默认 >50 MB）
  4. 环境/构建产物（.venv/node_modules/bin/obj/__pycache__）
  5. 未跟踪文本中的常见密钥模式
  6. ignored 体积（提示，不失败）
  7. 可选 git push --dry-run

退出码: 0 通过（可有 WARN），1 有 FAIL。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

RESULT = []


def add(level, title, detail=""):
    RESULT.append((level, title, detail))


def run_git(root: Path, *args, timeout=60):
    try:
        p = subprocess.run(["git", "-C", str(root), *args],
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=timeout)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except Exception as e:
        return 999, "", str(e)


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024
    return str(n)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="仓库根目录")
    ap.add_argument("--max-untracked-mb", type=float, default=100.0)
    ap.add_argument("--max-file-mb", type=float, default=50.0)
    ap.add_argument("--check-push", action="store_true", help="执行 git push --dry-run（可能触发凭据）")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    rc, top, err = run_git(root, "rev-parse", "--show-toplevel")
    if rc != 0:
        add("FAIL", "不是 git 仓库", err or top)
        return report()
    repo = Path(top)

    rc, branch, _ = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    add("PASS" if rc == 0 else "WARN", "当前分支", branch or "unknown")

    rc, remote, _ = run_git(repo, "remote", "-v")
    add("PASS" if remote else "WARN", "remote", remote.splitlines()[0] if remote else "未配置 remote")

    rc, status, _ = run_git(repo, "status", "--porcelain")
    lines = [x for x in status.splitlines() if x.strip()]
    staged = [x for x in lines if not x.startswith("??")]
    untracked = [x for x in lines if x.startswith("??")]
    add("PASS" if not staged else "WARN", "tracked 修改", f"{len(staged)} 项")
    add("PASS" if not untracked else "WARN", "未跟踪条目", f"{len(untracked)} 项")

    rc, out, _ = run_git(repo, "ls-files", "--others", "--exclude-standard", "-z")
    raw = out.split("\0") if out else []
    files = [repo / p for p in raw if p]
    total = sum(f.stat().st_size for f in files if f.is_file()) if files else 0
    add("PASS" if total <= args.max_untracked_mb * 1024 * 1024 else "FAIL",
        "未跟踪体积", f"{human(total)}（阈值 {args.max_untracked_mb:g} MB）")

    big = []
    for f in files:
        try:
            if f.is_file() and f.stat().st_size > args.max_file_mb * 1024 * 1024:
                big.append((f.stat().st_size, f))
        except OSError:
            pass
    if big:
        big.sort(reverse=True)
        add("FAIL", "未跟踪大文件", "; ".join(f"{human(s)} {p.relative_to(repo)}" for s, p in big[:10]))
    else:
        add("PASS", "未跟踪大文件", f"无 >{args.max_file_mb:g} MB")

    bad_dirs = {".venv", "node_modules", "__pycache__", ".Rlibrary", ".git"}
    bad = [f for f in files if any(part in bad_dirs for part in f.parts)]
    bad += [f for f in files if f.name.endswith((".pyc", ".pyo"))]
    add("PASS" if not bad else "FAIL", "环境/缓存文件",
        "无" if not bad else "; ".join(str(p.relative_to(repo)) for p in bad[:10]))

    secret_re = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|"
                           r"AIza[0-9A-Za-z_-]{20,}|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
                           r"api[_-]?key\s*[:=]\s*['\"][^'\"]{12,})", re.I)
    hits = []
    for f in files:
        try:
            if not f.is_file() or f.stat().st_size > 1_000_000:
                continue
            if f.suffix.lower() in {".png", ".jpg", ".jpeg", ".zip", ".pdf", ".docx", ".xlsx", ".gz", ".npz", ".npy"}:
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            if secret_re.search(text):
                hits.append(str(f.relative_to(repo)))
        except OSError:
            pass
    add("PASS" if not hits else "FAIL", "未跟踪文本密钥扫描",
        "0 命中" if not hits else "; ".join(hits[:10]))

    rc, out, _ = run_git(repo, "ls-files", "--others", "--ignored", "--exclude-standard", "-z")
    ignored = [repo / p for p in (out.split("\0") if out else []) if p]
    itotal = sum(f.stat().st_size for f in ignored if f.is_file()) if ignored else 0
    add("INFO", "ignored 本地体积", f"{human(itotal)}（不进 git，建议 Release/网盘）")

    if args.check_push:
        rc, out, err = run_git(repo, "push", "--dry-run", timeout=60)
        add("PASS" if rc == 0 else "FAIL", "git push --dry-run",
            (out or err)[-500:] or f"exit {rc}")
    else:
        add("SKIP", "git push --dry-run", "未启用 --check-push")

    return report()


def report() -> int:
    symbols = {"PASS": "PASS", "FAIL": "FAIL", "WARN": "WARN", "INFO": "INFO", "SKIP": "SKIP"}
    fails = 0
    for level, title, detail in RESULT:
        print(f"[{symbols.get(level, level)}] {title}: {detail}")
        if level == "FAIL":
            fails += 1
    print(f"\nSUMMARY: {len(RESULT)} checks, {fails} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
