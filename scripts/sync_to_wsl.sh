#!/bin/bash
# 把 Windows 侧 skill 主仓同步到 WSL codex 副本。
# 规则：文本文件 CRLF->LF 转换；二进制文件逐字节复制；排除 .git/__pycache__。
# 用法（WSL 内）: bash scripts/sync_to_wsl.sh
set -e
SRC="/mnt/c/Users/mary3/.agents/skills/mary-modeling-contest-pipeline-apmcm"
DST="/home/mary/.codex/skills/mary-modeling-contest-pipeline-apmcm"

python3 - <<'EOF'
import os

src_root = "/mnt/c/Users/mary3/.agents/skills/mary-modeling-contest-pipeline-apmcm"
dst_root = "/home/mary/.codex/skills/mary-modeling-contest-pipeline-apmcm"
BINARY_EXT = {'.pdf', '.png', '.jpg', '.jpeg', '.zip', '.docx', '.xlsx', '.mp4', '.pyc'}

copied = unchanged = 0
for root, dirs, files in os.walk(src_root):
    dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
    rel = os.path.relpath(root, src_root)
    for fn in files:
        sp = os.path.join(root, fn)
        dp = os.path.join(dst_root, rel, fn) if rel != '.' else os.path.join(dst_root, fn)
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        with open(sp, 'rb') as f:
            data = f.read()
        ext = os.path.splitext(fn)[1].lower()
        if ext not in BINARY_EXT:
            data = data.replace(b'\r\n', b'\n')
        if os.path.exists(dp):
            with open(dp, 'rb') as f:
                if f.read() == data:
                    unchanged += 1
                    continue
        with open(dp, 'wb') as f:
            f.write(data)
        copied += 1
print(f"copied={copied} unchanged={unchanged}")
EOF

# 校验：文本按 --strip-trailing-cr 比，二进制按字节比
FAIL=0
while IFS= read -r -d '' f; do
  rel="${f#$SRC/}"
  case "$rel" in .git*|*/.git/*) continue;; esac
  t="$DST/$rel"
  [ -f "$t" ] || { echo "MISSING: $rel"; FAIL=1; continue; }
  ext="${f##*.}"
  case "$ext" in
    pdf|png|jpg|jpeg|zip|docx|xlsx|mp4)
      cmp -s "$f" "$t" || { echo "BIN-DIFF: $rel"; FAIL=1; } ;;
    *)
      diff -q --strip-trailing-cr "$f" "$t" >/dev/null 2>&1 || { echo "TXT-DIFF: $rel"; FAIL=1; } ;;
  esac
done < <(find "$SRC" -type f -not -path "*/.git/*" -not -name "*.pyc" -print0)

[ "$FAIL" = 0 ] && echo "SYNC-VERIFIED: all files identical (modulo line endings)" || echo "SYNC-HAD-DIFFS"
