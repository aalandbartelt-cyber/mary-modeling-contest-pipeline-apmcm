# 17 WSL / Windows 环境与 Git

> 本文记录 2026 MathorCup 实际环境：Windows 宿主 + WSL Ubuntu 22.04 + Python/R/Word/LibreOffice/GitHub。
> 目标：换机器或换人时，5 分钟知道“工具在哪、哪个能跑、哪个会卡”。

---

## 17.1 实际可用路径

| 工具 | 路径/命令 | 备注 |
|---|---|---|
| Python（主） | `~/miniconda3/envs/mathorcup/bin/python` | `python` 不一定在 PATH |
| R | `~/miniconda3/envs/r/bin/Rscript` | `Rscript` 不一定在 PATH |
| Word | Windows COM `Word.Application` | DOCX→PDF 首选 |
| PowerPoint | `C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE` | COM 可能打不开 PPTX |
| LibreOffice | `C:\Program Files\LibreOffice\program\soffice.exe` | headless 可做 PPTX→PDF |
| PDF 渲染 | PyMuPDF（`fitz`/`pymupdf`） | `pdftoppm` 可能不存在 |
| Excel | `openpyxl` | 结果工作簿 |
| DOCX | `python-docx` + `lxml` | 表格/图片/OMML |
| Git | WSL `git` | credential helper 不要指向 Windows `gh.exe` |

**原则**：脚本里不写 `python`/`Rscript` 裸命令；用绝对路径或环境变量。

---

## 17.2 常见故障与兜底

| 现象 | 原因 | 兜底 |
|---|---|---|
| `python: command not found` | conda env 未激活 | 用绝对路径；或 wrapper |
| `Rscript: command not found` | R 在 conda env | `~/miniconda3/envs/r/bin/Rscript` |
| PowerPoint COM `Presentations.Open: Failed` | 自动化/授权/文件问题 | 用 LibreOffice headless 转 PDF |
| `soffice` 返回但无 PDF | 异步/并发配置锁 | `-env:UserInstallation=...` + 轮询 |
| 中文路径日志乱码 | LibreOffice 编码 | 用 ASCII 临时目录转换 |
| `pdftoppm` 不存在 | poppler 未装 | PyMuPDF `get_pixmap(dpi=300)` |
| Git push 卡住 | `credential.helper` 调 Windows `gh.exe` | 一次性 token + `GIT_ASKPASS` |
| 图片中文字体不对 | 字体缺失/回退 | 检查 PDF 字体；用 Microsoft YaHei/Times New Roman |
| OMML 显示异常 | 空 run/压平/字体 | OpenXML SDK + Word 打开 + PDF 渲染 |

---

## 17.3 Git 凭据（安全做法）

WSL 直接执行 `/mnt/c/.../gh.exe` 可能失败；credential helper 会卡住。

推荐流程：

1. Windows PowerShell：`gh auth token` 写入临时文件（仅当前用户可读）。
2. WSL 创建 `GIT_ASKPASS` 脚本：用户名返回 `x-access-token`，密码 `cat` 临时文件。
3. `GIT_ASKPASS=... GIT_TERMINAL_PROMPT=0 git -c credential.helper= push`。
4. 推送后**立即删除**临时 token 和 askpass。
5. 不把 token 写进仓库、脚本、日志、提示词。

```bash
# 示例（token 文件在 Windows TEMP）
cat > /tmp/mw_askpass <<'SH'
#!/bin/sh
case "$1" in
*Username*) printf "%s\n" "x-access-token" ;;
*) cat /mnt/c/Users/<user>/AppData/Local/Temp/mw_token ;;
esac
SH
chmod 700 /tmp/mw_askpass
GIT_ASKPASS=/tmp/mw_askpass GIT_TERMINAL_PROMPT=0 \
  git -c credential.helper= push origin main
rm -f /tmp/mw_askpass
```

---

## 17.4 仓库体积与 ignore

2026 比赛结束时：

- 本地仓库 pack 约 646 MB；
- 未跟踪约 919 MB；
- 忽略约 1.2 GB；
- 最终提交约 83 MB。

**结论**：历史快照、重复附件、`bin/obj`、环境目录不要进 git。

建议 `.gitignore`：

```gitignore
_archive/
**/bin/
**/obj/
.worktrees/
docs/collab/**/*.zip
docs/collab/**/*.pdf
docs/collab/**/*.png
docs/collab/**/*.docx
docs/collab/**/*.xlsx
docs/collab/**/*.json
docs/collab/**/*.csv
05_论文/总论文/2026_*_v[2-9].*
05_论文/总论文/2026_*_v1[0-2].*
05_论文/交付给论文手/待审_*/
```

最终论文/附件/结果必须进 `06_交付/`，不能只留在 D 盘 `终稿/`。

---

## 17.5 阶段 commit 节奏

| 阶段 | 必须提交 |
|---|---|
| 选题/口径冻结 | 赛事参数、数据契约、决策记录 |
| 每问代码/结果 | 源码、配置、结果摘要 |
| 每问验证 | validation CSV/JSON、图源 |
| 总论文每个版本 | DOCX/PDF、图清单、SHA |
| 最终包 | 论文、附件、结果、提交清单、SHA |

提交前：

```bash
git status --short
git diff --stat
python scripts/audit_git_hygiene.py --root .
```

---

## 17.6 环境医生检查项

- Python 版本/路径、依赖包；
- R 版本/路径、ggplot2/patchwork；
- Word COM、PowerPoint COM、LibreOffice；
- PyMuPDF、openpyxl、python-docx、lxml；
- 字体（YaHei/Times/Cambria Math）；
- Git remote、credential、push dry-run；
- 代理/DNS/GitHub 可达；
- PDF 渲染、OMML 字体。

建议 `scripts/env_doctor.py` 输出 PASS/FAIL + 替代方案；FAIL 不允许进入正式阶段。

---

## 17.7 验收

- [ ] 新机器 5 分钟内跑完 doctor；
- [ ] Python/R 用绝对路径；
- [ ] DOCX→PDF 有 Word 与 LibreOffice 两条路；
- [ ] PDF 渲染不依赖 `pdftoppm`；
- [ ] Git push 有安全 token 流程；
- [ ] 仓库未跟踪 <100 MB；
- [ ] 最终交付物在 `06_交付/`。
