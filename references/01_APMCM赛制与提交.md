# 01 APMCM 赛制与提交

> 依据：2026 年第十六届 APMCM 参赛规则；2025 APMCM Essay format and submission specifications。
> 关键数字以当届官方为准；本文件是备赛/提交清单，不替代原件。

---

## 1.1 2026 关键信息

| 项 | 2026 规则 |
|---|---|
| 名称 | 2026 年第十六届 APMCM 亚太地区大学生数学建模竞赛 |
| 报名截止 | 北京时间 2026-11-25 24:00 |
| 开赛 | 北京时间 2026-11-26（周四）06:00 |
| 结束/提交截止 | 北京时间 2026-11-30（周一）09:00 |
| 结果 | 预计 2027-01-15 前 |
| 队伍 | ≤3 名全日制在校大学生；每人只能参加一队 |
| 题目 | A/B/C/D 任选 **一题** |
| 语言 | 英文；正文、图表、表注不得出现中文 |
| 正文 | **≤25 页**；附录不限 |
| 首页 | Summary（第 1 页） |
| 第 2 页 | Contents（目录） |
| 页眉 | `Team #<team number> Page <x> of <y>`；只允许队号/页码 |
| 字号 | 一般 11 或 12 |
| 论文 PDF | `<题号><队号>.pdf`（如 `Aapmcm2600001.pdf`） |
| Control Sheet | `<题号><队号>cns.pdf/jpg/png`，单独签名上传 |
| 支撑材料 | `<题号><队号>fj.rar/zip`；可选 |
| 匿名 | 论文任何页不得出现姓名、学校、指导教师；队号可用 |

**注意**：2026 规则 PDF 是扫描件，关键条款以官方原件为准；本 skill 中的 25 页、summary/contents、header 已按 2026 规则与 2025 格式规范交叉核对。

---

## 1.2 论文结构

```text
p1  Summary: Team Number / Problem Chosen / Summary / Keywords
p2  Contents
正文（page 1 起）:
  Introduction
  Assumptions and Notations
  Data / Problem Analysis
  Model(s) and Solution(s)
  Model Evaluation / Sensitivity
  Conclusions
  References
  Appendix: software + all source code
```

- Summary 必须一页；Contents 单独一页；正文从 Contents 后开始。
- 正文页码从 1 开始；summary/contents 用 front matter 页码或不编号（按模板）。
- 正文 ≤25 页；附录不限。
- 论文 PDF 不包含 control sheet / 支撑材料。

---

## 1.3 页眉与匿名

- 2026 规则原文：解决方案的**每一页顶部**都需要参赛编号以及页码。官方示例写作：
  `Team#apmcm2600001Page10of20`（无空格；以官方模板/导出效果为准）。
- 2025 模板/格式说明可能用 `Team #<team number> Page <x> of <y>` 或带空格版本；不要凭记忆固定空格，按当届模板生成并逐页核对。
- 每页都查，包括 Summary、Contents、正文、附录；如果模板默认不给 front matter 页眉，提交前向组委会/模板说明确认，不要仅凭旧模板默认。
- `Page x of y` 的 `y` 与正文页数一致（模板可能按正文/附录分开计数；以模板和导出结果为准）。
- 不出现姓名、学校、指导教师、邮箱、学号。
- 论文正文/图表/代码注释/PDF 元数据都查。
- Control Sheet 可以有学校/姓名/签名，但它是**单独文件**，不放进论文。

---

## 1.4 参考文献格式

官方给的三类：

```text
书籍：[ID] Author, Title[M], Place of Publication: Press, Year, pages.
期刊：[ID] author, paper name[J], magazine name, year, volume: pages.
网络：[ID] author, resource title, website, visit time (year, month, day).
```

- 正文用方括号 `[1]`、`[3]`；按首次引用顺序编号。
- 每条都必须在正文被引用；无僵尸文献。
- 不把中文文献条目写成中文；英文/拼音按可核验信息写。

---

## 1.5 Control Sheet 与支撑材料

### Control Sheet

- 每个成员手写/电子签名；
- 含 Problem chosen、Team control number、School、Member names、Adviser、Date；
- 扫描/拍照成 PDF/JPG/PNG，命名 `<题号><队号>cns`；
- **不要放进论文 PDF**。

### 支撑材料

- 可选；若交，包含程序、非原始数据、结果；
- 不含赛题原始数据；
- 命名 `<题号><队号>fj.rar/zip`；
- 论文附录仍须有软件名 + 全部源代码。

**AI 使用/披露（2026 官方规定）**：使用 AI 须在正文相应位置标注、References 按格式列工具、提交 `AI工具使用详情.pdf`；未使用须在 References 后写官方原句 `本参赛队未使用任何AI工具`。核心模型构建、算法设计与求解、结果分析必须由队员独立完成；不合规可取消评奖资格。不要套用其他赛事的 30%/50% 阈值或 AI 报告模板。详见 `12_AI工具与学术诚信.md`。

---

## 1.6 提交前 P0

- [ ] 题号与内容一致；
- [ ] 文件名 = 题号+队号；
- [ ] p1 summary；p2 contents；正文 ≤25 页；
- [ ] 页眉 Team # + Page x of y；
- [ ] 正文/图表无中文；
- [ ] 无姓名/学校/教师/邮箱；
- [ ] Control sheet 已签名、单独提交；
- [ ] 支撑材料命名/内容正确；
- [ ] PDF 元数据干净；
- [ ] 最终 PDF 在干净环境打开一次。

一键检查：`python scripts/audit_apmcm_submission.py --paper ... --control ... --zip ...`

---

## 1.7 2026 规则易漏点（原文核对）

- 队伍上限 **3 名全日制在校大学生**；每人只能参加一支队伍，不得重复参赛，发现取消成绩。
- 竞赛期间不得向指导教师或队外任何人寻求帮助/讨论；Email、电话、私下交谈、网络聊天、问答系统等任何形式接触严格禁止。AI 工具按 `12_AI工具与学术诚信.md` 的官方规定单独处理，不能用来绕开“队外帮助”限制。
- 所有引用的数据/资料必须注明出处；未注明引用可能取消参赛资格。
- 解决方案必须是论文形式；不接受计算机文件、磁盘等非文档材料。
- 摘要页必须是论文第一页；英文；字号一般 11 或 12；摘要占评阅权重很大。
- 每一页顶部需有参赛编号和页码；官方示例 `Team#apmcm2600001Page10of20`（空格/格式按模板）。
- 论文 PDF 不含 control sheet/附件；control sheet 单独命名 `<题号><队号>cns` 上传。
- 支撑材料可选：程序、数据（赛题原始数据除外）、结果等压缩为 `<题号><队号>fj`；**源代码仍须在论文附录，同时也要以支撑材料提供**。
- 保留论文 PDF/Word、程序、计算结果等附件，直到获奖名单公布。
- 2026 奖项表（官方表 1）：创新奖 2 队/题（1000 元/队）；一等奖 5%；二等奖 15%；三等奖 25%；成功参赛奖。没有通过/不通过分数线，评审依据解决方案。
- 评审七条：题意解读、假设合理性、建模思路、模型有效、稳定性检验、优缺点/结论、摘要。见 `06_评审与答辩式自查.md`。
- AI 使用：见 `12_AI工具与学术诚信.md`；使用 AI 须正文标注 + References 工具条目 + `AI工具使用详情.pdf`；未使用须写官方中文声明。
