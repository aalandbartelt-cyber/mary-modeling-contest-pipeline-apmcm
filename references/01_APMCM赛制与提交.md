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

- 每页顶部：`Team #apmcm26XXXXX Page 1 of 25`（按模板/官方示例）。
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
