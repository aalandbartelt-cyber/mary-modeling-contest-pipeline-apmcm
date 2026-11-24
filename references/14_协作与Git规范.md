# 14 协作与 Git 规范（APMCM 版）

> 用途：多 AI/多人协作时，保证 APMCM 论文、代码、图和交付包不互相覆盖、可回滚。
> 环境与代理细节见 `references/common/17_WSL_Windows环境与Git.md`；本文件补充分支、所有权、提交和交接。

---

## 14.1 角色与所有权

| 角色 | 位置 | 负责 | 不负责 |
|---|---|---|---|
| Codex | WSL | 建模、代码、结果、正式论文/包、`main` 集成 | 不替用户签字/上传 |
| Cursor | WSL | Codex 不可用时的备份主力；写候选分支 | 不直接改 `main`/正式交付，除非用户明确授权 |
| ZCode | Windows | 数据/文档/复核/候选图/提交检查 | 不覆盖正式论文/交付件 |
| dsh / 外部评审 | Windows | 论文评审、文字优化、评分建议 | 不建模/不选型/不改正式件 |

**正式论文/正式图/交付包默认只由当前主智能体写。** 任何跨角色修改都要在 handoff/decision 中记录授权。

---

## 14.2 分支模型

```text
main                 稳定可交付；只合并已验证内容
codex/<scope>-<topic> Codex 主工作分支
cursor/<scope>-<topic> Cursor 备份分支
zcode/<scope>-<topic>  Windows 辅助/文档分支
review/<topic>        评审/评分报告，不改论文正文
```

- 一个分支只做一件事；不要在同一分支混“改模型 + 改论文 + 改图”。
- 合并前先 rebase/merge 最新 `main`，跑相关检查。
- 冲突时保留双方内容，重新编号/重跑验证，不覆盖对方未合并工作。
- 不 force-push 共享分支；必须强推时先备份并说明。

---

## 14.3 Commit 格式

```text
<type>(<scope>): <short imperative summary>
```

常用 type：

- `feat` 新模型/新结果/新功能；
- `fix` 修 bug/修数据/修口径；
- `docs` 论文/报告/README；
- `fig` 图表/图源；
- `exp` 实验/参数/结果；
- `chore` 构建/依赖/清理；
- `revert` 回滚。

示例：

```text
feat(q2): add matched-window baseline comparison
fix(data): correct environment grouping key
docs(paper): tighten summary and direct answers
fig(q3): redraw capacity tradeoff at final print size
```

- 一个 commit 只做一类变化；不要 `update`/`final`/`fix again` 这种信息量为零的 message。
- 提交前 `git diff --stat` + 相关测试/编译；不要把大文件、数据、PDF、密钥混入。
- 需要追溯的结果 commit，在 message 里写实验编号/结果文件路径。

---

## 14.4 路径与阶段门

建议仓库结构（按 APMCM 实际项目调整）：

```text
00_赛题与规则/      官方规则、模板、数据说明（大文件按需忽略）
01_参考学习/        参考论文/资料（通常不入库）
02_口径与约定/      数据契约、写作/图表/评审规范
03_求解/            代码、配置、结果
05_论文/            候选稿、图源、编译脚本
06_交付/            最终 PDF/control sheet/支撑包
docs/collab/        handoff、决策、评审
```

**阶段门：**

| 阶段 | 必须落盘 |
|---|---|
| 选题/口径冻结 | 赛事参数、数据契约、决策记录 |
| 每问代码/结果 | 源码、配置、结果摘要 |
| 每问验证 | validation CSV/JSON、图源 |
| 总论文每个版本 | PDF/DOCX、图清单、SHA |
| 最终包 | 论文、control sheet、支撑包、提交清单、SHA |

正式交付目录只放最终件；候选稿留在 `05_论文/待审/` 或候选目录。

---

## 14.5 不提交什么

- 原始赛题数据/大参考 PDF/视频/模型权重（按当届规则和仓库策略）；
- `.env`、token、密钥、个人信息；
- `__pycache__`、`.pytest_cache`、`.venv`、`node_modules`；
- 临时编译产物（`.aux/.log/.out/.toc` 如无必要）；
- 重复的旧版本 PDF/zip；
- 未授权的第三方数据/图片。

提交前：

```bash
git status --short
git diff --stat
python scripts/audit_git_hygiene.py --root .
```

仓库未跟踪体积建议 <100 MB；最终交付物必须在 `06_交付/`，不能只留 D 盘。

---

## 14.6 交接最小字段

跨 agent/跨人交接只写文件，不依赖对话上下文。每个 handoff 至少：

```text
# HANDOFF
- 当前状态/版本/hash：
- 已完成：
- 未完成/下一步：
- 关键文件/路径：
- 不能动的东西：
- 验证命令/预期结果：
- 风险/待核：
```

- 接手先读 `AGENTS.md`、本 skill、handoff、`git status`。
- 不重做已完成部分；不恢复别人的对话线程。
- 完成后写 `DONE`/`BLOCKED`，附证据路径。
- 不把密钥、隐私、未公开赛题原文写进 bus/handoff。

---

## 14.7 Codex 额度不足时

- 先确认是否有官方额度/恢复时间；不要用不明中转站处理敏感数据。
- Cursor 接手：新分支、读 handoff、只写候选；正式件需用户明确授权。
- 不要在 Cursor 里假称“续上 Codex 线程”；用仓库文件补上下文。
- 交接后保留备份/哈希；回到 Codex 时先核对当前状态，不覆盖 Cursor 未合并工作。

---

## 14.8 每日/提交前 checklist

- [ ] `git status` 干净或只剩预期改动；
- [ ] 当前分支/负责人明确；
- [ ] 大文件/密钥/数据未入库；
- [ ] 结果/图/论文版本对应；
- [ ] handoff 已更新；
- [ ] 正式交付目录未被候选稿覆盖；
- [ ] 提交前跑审计脚本；
- [ ] 重要节点打 tag/备份。
