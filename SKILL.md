---
name: mary-modeling-contest-pipeline-apmcm
description: Use when preparing, running, writing, or rescuing an APMCM (Asia and Pacific Mathematical Contest in Modeling, 亚太杯英文赛) submission — 4-day English contest, Problems A–D, 25-page main body, summary page + contents page + team-number header, LaTeX/Word paper, control sheet, optional support materials, English-only figures and body. Also use when an APMCM paper must be checked for Chinese leakage, page/header/contents violations, weak English summary, missing appendix code, or wrong file naming.
---

# MARY 数模竞赛流水线 · APMCM 亚太杯英文赛特化版

本 skill 是 `mary-modeling-contest-pipeline` 的 APMCM 专用 profile。
方法层继承：口径统一、逐问求解、验证优先、R/Python 出图、交接包、总论文整合、提交红线。
赛制层替换为：**英文、4 天、A—D 四题、正文 25 页、summary + contents + team-number header、control sheet 单独提交、支撑材料可选**。

> 先读官方：`2026年第十六届APMCM亚太地区大学生数学建模竞赛参赛规则.pdf` 与 `2025 APMCM Essay format and submission specifications.pdf`。
> 本文件是流程提炼，不替代当届官方文件；页数、命名、提交入口以当届通知为准。

---

## 0. APMCM 与国赛/MathorCup 的硬差异

| 项 | APMCM | 国赛 CUMCM | MathorCup 大数据 |
|---|---|---|---|
| 语言 | **英文**；正文/图表不得出现中文 | 中文 | 中文 |
| 时长 | **4 天**（2026: 11/26 06:00—11/30 09:00，北京时间） | 约 4 天 | 约 7 天 |
| 题目 | **A—D 四题任选一题** | 通常 A/B/C | A/B 赛道 |
| 首页 | **summary page（第 1 页）** | 摘要专用页 | 题目+摘要+关键词 |
| 第 2 页 | **contents（目录）** | 禁止目录 | 必须有目录 |
| 正文 | **≤25 页**；附录不限 | ≤30 页 | ≤30 页 |
| 页眉 | **Team #… Page X of Y**，只允许队号/页码 | 通常无页眉 | 无页眉 |
| 承诺书 | **control sheet 单独签名提交**，不在论文里 | 承诺书/编号页不进电子版 | 承诺书单独 |
| 支撑材料 | 可选 `.rar/.zip`；程序仍须进论文附录 | ZIP ≤20 MB | ZIP 可达 20 MB+ |
| 身份 | 论文任何页不得出现姓名/学校/指导教师；队号可用 | 全匿名 | 全匿名 |

**第一条要记住：APMCM 不是“把国赛论文翻译成英文”。** 首页 summary、第二页 contents、25 页、英文-only、control sheet 单独提交，都是独立的装订层。

---

## 0.1 获奖论文的实际画像（16 篇，2022—2025）

- Summary：**252—527 词**，中位 **387 词**；数字 **5—70 个**，中位 **18.5 个**。
- 图：中位 **14 张**；表：中位 **4 张**；有的论文图多表少，有的反过来。
- 总 PDF 中位 **35.5 页**，但正文仍按官方 **25 页**控制；不要把“获奖论文 30+ 页”当借口。
- 共同骨架：`Introduction → Assumptions → Notations → 每问模型/结果 → Model Evaluation → References → Appendix`。
- 页数分配：Introduction+Assumptions+Notation 约 **3—5 页**；每问 **4—6 页**；Model Evaluation/Conclusions **1—2 页**。
- 章节名不必死抠：14/16 有 Advantages/Strengths，11/16 有 Sensitivity，8/16 有 Limitations/Weaknesses；每问回答完整比标题规范更重要。
- 优秀论文的区分度不在“模型最新”，而在：**每问都回答、数字可追溯、图表能读、英文清楚、优缺点不是空话**。

详细解剖见 `references/07_优秀论文解剖.md`，原始统计见 `assets/award_paper_metrics.csv`。

### 0.2 重要参考：M 杯 2026 A 题最终论文

`references/important/MathorCup_2026_A2601605.pdf`（元数据已清理，正文未改）是 MathorCup 2026 A 题最终提交版，用作**结构/验证/附录**参考，不是 APMCM 模板：

- 可借：每问“模型→结果→检验→边界”、共享数据接口、技术路线树、附录 A—E、具体边界句；
- 不可借：中文、30 页正文、MathorCup 格式/AI 声明、啤酒具体模型；
- 详细页面对照与精读顺序见 `references/08_M杯最终论文参考.md`。

---

## 1. 开赛 10 分钟：填 APMCM 参数

复制到 `00_赛题与规则/赛事参数.md`：

```markdown
P1 赛事：APMCM 2026（第十六届）
P2 题目：A / B / C / D（只能选一个）
P3 语言：English only；正文/图表/表注不得出现中文
P4 页数：summary p1；contents p2；正文≤25页；附录不限
P5 页眉：Team #<team number> Page <x> of <y>
P6 提交：论文 PDF（题号+队号.pdf）；control sheet 单独签名 PDF/JPG/PNG；支撑材料可选 .rar/.zip
P7 匿名：论文任何页不得出现姓名/学校/指导教师；队号可用
P8 模板：官方 LaTeX 模板 / Word；字号 11–12；英文
```

**核对**：题目号与论文内容必须一致；不一致可能取消资格。

---

## 2. 四天节奏（建议）

| 时间 | 目标 | 必须落盘 |
|---|---|---|
| D1 上午 | 读题、选 A—D、拆【已知/要求/隐含/陷阱】 | `选题结论.md`、`赛事参数.md` |
| D1 下午 | 数据/假设/符号/模型路线；C 题先做数据管线 | `数据对账.md`、`符号表.md`、`模型路线.md` |
| D1 晚 | 基线结果 + 第一版 summary 骨架 | `summary_draft.md`、基线图 |
| D2 | 主模型求解 + 第一轮验证 | 结果 CSV、验证表 |
| D3 | 补充实验/敏感性/对比；图表成型；正文开写 | 图、表、正文 v1 |
| D3 晚 | 全文英文初稿；摘要重写 | 正文 v2、summary v2 |
| D4 上午 | 英文润色、页数/页眉/目录/图表编号 | 正文 v3 |
| D4 下午 | 格式、control sheet、支撑材料、PDF 元数据 | 最终 PDF/包 |
| D4 晚 | 只做提交检查，不再改模型 | `提交清单.md` |

**铁律**：summary 从 D1 开始写，不要留到最后一天；最后 6 小时只做格式/提交检查。

---

## 3. 选题：A—D 的路线判断

2025 年真题结构（用于理解 APMCM 出题风格，不保证 2026 相同）：

| 题 | 类型 | 核心方法 | 难度 | 竞争 | 适合 |
|---|---|---|---|---|---|
| A | 机器人运动/动力学 | 坐标变换、步态规划、逆运动学、能耗 | 3.5/5 | 较高 | 自动化/机械/控制 |
| B | 辐射制冷薄膜 | TMM、热平衡、结构优化 | 4/5 | 较低 | 物理/光学/材料 |
| C | 关税/贸易数据 | 弹性/引力模型、预测、综合评价、数据清洗 | 3.5/5 | **最高** | 经管/统计/数据 |
| D | 机组组合/量子优化 | MIP、QUBO、规模缩减、Kaiwu SDK | 4.5/5 | 最低 | 运筹/电力/工业工程 |

**选择原则**：

1. 先看数据是否可拿到、是否能清洗；C 题通常数据量大，D1 必须完成数据管线。
2. 不按“题简单”选，按“我们能在 4 天内做出完整证据链”选。
3. C 题选的人最多，必须靠**数据正确性 + 机制自洽 + 英文可视化**拉开差距；不要只做描述统计。
4. B/D 竞争小但门槛高；如果队伍没有相应背景，不要用“人少”当唯一理由。
5. 任何时候都不要四题都做；只选一题。

---

## 4. 官方评审七条 → 论文结构

2026 规则列出的评阅原则：

1. 对赛题给出满意解读，模糊概念有解释；
2. 明确前提/假设，并解释合理性；
3. 通过分析给出建模思路或论证合理性；
4. 设计能有效解决问题的数学模型；
5. 对模型给出稳定性检验；
6. 讨论模型优缺点，给出清晰结论；
7. 给出圆满准确的 summary。

对应论文结构：

```text
p1  Summary（题目/队号/问题号 + 摘要 + 关键词）
p2  Contents
1   Introduction（背景、问题重述、我们的工作）
2   Assumptions and Notations
3   Data / Problem Analysis
4   Model I（每问：分析 → 模型 → 求解 → 结果 → 验证）
5   Model II
...
N   Model Evaluation（strengths / weaknesses / sensitivity）
    Conclusions
    References
    Appendix（software + all source code）
```

**每一问必须有**：问题解读 → 假设/符号 → 模型 → 求解 → 结果 → 稳定性/敏感性 → 小结。
**不要**把“模型建立”写成方法堆砌；评审第 3、4 条看的是“为什么这个模型能解决问题”。

---

## 5. 英文 summary（第一页，决定第一印象）

### 硬规范

- 第 1 页：Team Number、Problem Chosen、Summary 标题、正文、Keywords。
- 一页内完成；不跨页；不要放公式、图、表、参考文献角标。
- 结构：背景 1—2 句 → 总体方法 1 段 → 每问 1 段（方法 + 关键数字）→ 结论/意义 1—2 句 → Keywords 3—5 个。
- 每问至少 1 个数字；数字必须与正文/结果文件一致。
- 用过去时描述做了什么，用现在时描述结论/意义；不要“we can see”“very good”这类空话。
- 目标 **350—450 词**；数字 **10—25 个**（每问 2—3 个关键结果），与正文/结果文件一致。

### 模板

```text
Problem Chosen: C
Team Number: apmcm26XXXXX

Summary

[Background: 1–2 sentences. Why this problem matters.]
[Overall approach: 1 paragraph. What data, what framework, what validation.]

For Problem 1, we [model/approach]. The [key metric] is [value], compared with [baseline].
For Problem 2, we [model/approach]. [Key result with number.]
For Problem 3, we [model/approach]. [Key result with number.]
For Problem 4, we [model/approach]. [Key result with number.]

[Conclusion: 1–2 sentences. What the results imply; what is not claimed.]

Keywords: keyword1; keyword2; keyword3; keyword4
```

### 常见扣分

- Summary 只复述题目，没有方法和数字；
- 每问没有数字，或数字与正文不一致；
- 出现中文、中文标点、中文图题；
- 关键词太多/太少（3—5 个）；
- Summary 跨页，或把 Contents 挤到第 1 页。

---

## 6. 英文正文写作

### 语言底线

- 全英文；正文、图题、表题、坐标轴、图例、附录说明不得出现中文。
- 用简单、可读的英文；避免中文式长句和堆砌形容词。
- 术语首次出现给全称/定义；同一概念只用一个词。
- 数字 + 单位；百分比写 `%`；千分位一致；日期/货币写清口径。
- 不写“very significant/obviously/best”没有证据的评价；用数值和比较。

### 每问段落模板

```text
4.1 Problem analysis
[What is given, what is unknown, what is the difficulty. 1–2 paragraphs.]

4.2 Assumptions and notation
[Only problem-specific assumptions; refer to global assumptions.]

4.3 Model
[Define variables; objective; constraints; explain why this model answers the question.]

4.4 Solution
[Algorithm/solver; parameters; reproducibility; runtime if relevant.]

4.5 Results
[Table/figure; quantitative comparison; answer the question.]

4.6 Validation and sensitivity
[Residual/consistency; parameter perturbation; negative control; boundary.]

4.7 Summary
[What is supported; what is not.]
```

### 常见英文问题

| 问题 | 改法 |
|---|---|
| 句子 50+ 词、多个从句 | 拆成 2—3 句；一句一个主张 |
| 全篇一般现在时 | 方法/实验用过去时，结论/意义用现在时 |
| 缺冠词/单复数 | 定稿前专查 `a/an/the`、`result(s)`、`model(s)` |
| 中文标点、全角字符 | 全文搜 `，。；：（）`，替换为英文标点 |
| 图内中文 | 重绘或改英文标签；不得用中文截图 |
| 术语漂移 | 建 `terminology.md`，全文统一 |

---

## 7. 图表与公式

- 图：白底、细框、无网格、英文标签、单位；300 dpi；颜色在灰度下可区分；图题在图下。
- 表：三线表；表题在表上；英文表头；单位写清；表不跨页。
- 公式：LaTeX/Word 原生公式；全文连续编号；正文引用同步；符号首次出现解释。
- 每张图/表必须在正文被点名，并解释“说明了什么”，不要只复述数字。
- 图内不得出现中文；LaTeX 模板里的中文示例（CJK、公众号图）必须删除/替换。

---

## 8. 论文格式与提交

### 论文结构

```text
p1 Summary（Team Number / Problem Chosen / Summary / Keywords）
p2 Contents
正文（page 1 开始）：
  Introduction
  Assumptions and Notations
  Data / Problem Analysis
  Model(s) and Solution(s)
  Model Evaluation / Sensitivity
  Conclusions
  References
  Appendix（software + all source code）
```

### 页眉/页码

- 每页顶部：`Team #<team number> Page <x> of <y>`（按官方示例）。
- 不出现姓名、学校、指导教师、邮箱。
- 正文页码从 1 开始；summary/contents 用 front matter 页码或不编号（按模板）。
- 正文 ≤25 页；附录不计。

### 文件命名

- 论文：`<题号><队号>.pdf`，如 `Aapmcm2600001.pdf`（以当届通知为准）。
- 承诺书：`<题号><队号>cns.pdf/jpg/png`。
- 支撑材料：`<题号><队号>fj.rar/zip`。
- 提交前核对题号、队号、文件名三者一致。

### Control Sheet

- 单独打印/签名/扫描或拍照；包含学校、成员姓名、指导教师、日期。
- **不要放进论文 PDF**；论文里只允许队号。
- 每个成员都要签名；缺签名可能取消资格。

### 支撑材料

- 可选；若提交，包含程序、非原始数据、结果等。
- 论文附录仍须有软件名称 + 全部源代码；支撑材料是额外副本，不是替代。
- 不把赛题原始数据打包进去。

---

## 9. 验证与稳定性（APMCM 评审第 5 条）

每问至少做：

- 一致性/可行性：约束满足、残差、输出范围；
- 参数敏感性：关键参数 ±10—30%，或 2—3 档；
- 对照/负对照：baseline、随机基线、置换、留一；
- 误差/不确定性：bootstrap/重复实验/区间；
- 边界：不能声称什么（外推、因果、真实政策效果等）。

**写作**：不要只写“robust”；给表/图 + 数字 + 口径。详见 `references/common/14_模型检验与稳健性.md`。

---

## 10. 四天里的角色分工（3 人）

| 角色 | 职责 | 不做什么 |
|---|---|---|
| Modeler | 选题、假设、模型、结果解释 | 不包办全部写作 |
| Coder | 数据管线、求解、图、复现 | 不改模型主张 |
| Writer | 英文正文、summary、格式、提交 | 不编造结果 |

**每天固定 2 次对齐**：中午看结果/图，晚上看页数/摘要/第二天计划。
**任何数字只从结果文件进论文**；summary 与正文由同一张 `key_numbers.csv` 驱动。

---

## 11. 提交前检查（P0）

- [ ] 题号与内容一致；文件名 = 题号+队号。
- [ ] p1 summary；p2 contents；正文从 p1 开始；正文 ≤25 页。
- [ ] 每页 header 有 Team # 和 Page x of y；无姓名/学校/教师/邮箱。
- [ ] 正文/图/表/图例/坐标轴无中文、无全角标点。
- [ ] 图/表/公式编号连续；正文引用一致；表不跨页；图题同页。
- [ ] 参考文献按引用顺序；正文有 [n]；无僵尸文献。
- [ ] 附录有软件名 + 全部源代码；代码路径与支撑包一致。
- [ ] Control sheet 已签名，单独提交，不在论文里。
- [ ] 支撑材料（若交）命名正确、无原始数据、无身份信息。
- [ ] PDF 元数据 author/creator 干净；无中文。
- [ ] 最终 PDF 在干净环境打开一次；页数/页眉/目录正确。

一键审计：

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf --zip Aapmcm2600001fj.zip
python scripts/audit_git_hygiene.py --root .
python scripts/env_doctor.py
```

---

## 12. 常见错误（Top 12）

| # | 错误 | 后果 | 防法 |
|---|---|---|---|
| 1 | 把国赛论文直接翻译 | 首页/目录/页眉/25 页全错 | 用 APMCM 模板重排 |
| 2 | 正文/图内中文 | 违反英文-only | 全文 + 图源 + PDF 三层扫描 |
| 3 | Summary 跨页/无数字 | 第一印象差 | 一页、每问 1 数字 |
| 4 | 目录缺失/页码不对 | 格式违规 | 第 2 页 contents；导出后核对 |
| 5 | 页眉带姓名/学校 | 身份违规 | 只留 Team # + Page |
| 6 | Control sheet 放进论文 | 身份泄露 | 单独提交 |
| 7 | 附录代码与包不一致 | 程序跑不通 | 包内实测 `--help`/compile |
| 8 | 15 页正文但模型很浅 | 评审第 4/5 条低分 | 深度优先，不为页数注水 |
| 9 | 只报结果不做稳定性 | 评审第 5 条低分 | 敏感性/对照/残差 |
| 10 | 英文长句/术语漂移 | 可读性差 | 术语表 + 短句 + 人工润色 |
| 11 | 最后一天才写 summary | 摘要烂尾 | D1 起写，D4 只润色 |
| 12 | PDF 元数据带用户名 | 身份违规 | 清 metadata |

---

## 13. 停止条件

1. 正文 >25 页且只能靠删关键结果压缩 → 先重写，不要删证据。
2. 只剩语言润色且时间 <3 h → 停止改模型，只做格式/提交。
3. Summary 与正文数字不一致 → 先对齐 `key_numbers.csv`，不要继续写。
4. 题号/文件名/队号不确定 → 停下来查官方，不要猜。

---

## 14. 参考文件

| 文件 | 用途 |
|---|---|
| `references/01_APMCM赛制与提交.md` | 2026 规则、2025 格式、命名、control sheet |
| `references/02_英文论文结构与写作.md` | summary/contents/正文/附录、英文句式、常见错误 |
| `references/03_四题路线与选题.md` | A—D 题型、2025 案例、选择矩阵 |
| `references/04_四天冲刺与分工.md` | D1—D4 节奏、三人分工、检查点 |
| `references/05_图表公式与LaTeX模板.md` | 英文图表、公式、LaTeX/Word、模板清理 |
| `references/06_评审与答辩式自查.md` | 官方七条、P0/P1/P2、英文 QA |
| `references/07_优秀论文解剖.md` | 2022—2025 获奖论文的量化结构、summary 写法、图表/章节规律 |
| `references/08_M杯最终论文参考.md` | M 杯 2026 A 最终论文的页面对照/可迁移做法/不可照搬项 |
| `references/important/MathorCup_2026_A2601605.pdf` | M 杯最终论文原件（元数据已清理，正文未改） |
| `references/common/13—17` | 工件所有权、验证、总论文整合、数据路线、WSL/Git |
| `assets/award_paper_metrics.csv` | 16 篇获奖论文的页数/摘要词数/数字/图表统计 |
| `assets/apmcm_submission_checklist.md` | 提交前逐项勾 |
| `assets/summary_sheet_template.md` | 一页 summary 模板 |
| `assets/english_style_guide.md` | 英文写作/术语/标点 |
| `assets/paper_outline.md` | 论文骨架 |
| `scripts/audit_apmcm_submission.py` | PDF/页眉/目录/中文/元数据/包检查 |
| `scripts/analyze_award_papers.py` | 统计优秀论文页数/summary/图表结构 |
| `scripts/audit_git_hygiene.py` | 仓库卫生 |
| `scripts/env_doctor.py` | 环境体检 |
