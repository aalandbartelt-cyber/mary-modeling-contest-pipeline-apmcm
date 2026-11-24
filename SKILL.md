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
- **2026 奖项（官方表 1）**：创新奖 2 队/题（1000 元/队）；一等奖 5%；二等奖 15%；三等奖 25%；成功参赛奖。没有通过/不通过分数线，评审依据解决方案质量。

详细解剖见 `references/07_优秀论文解剖.md`，原始统计见 `assets/award_paper_metrics.csv`。

### 0.2 重要参考：M 杯 2026 A 题最终论文

`references/important/MathorCup_2026_A2601605.pdf`（元数据已清理，正文未改）是 MathorCup 2026 A 题最终提交版，用作**结构/验证/附录**参考，不是 APMCM 模板：

- 可借：每问“模型→结果→检验→边界”、共享数据接口、技术路线树、附录 A—E、具体边界句；
- 不可借：中文、30 页正文、MathorCup 格式/AI 声明、啤酒具体模型；
- 详细页面对照与精读顺序见 `references/08_M杯最终论文参考.md`。

### 0.3 项目级写作、图表与协作规范（2026-11-24 迁移）

本项目在实战协作中积累的写作/审稿、图表/排版、验证/复现和 Git/交接经验，已蒸馏为 APMCM 版参考。先读 `09`、`10`；其余按任务取用。

- `references/09_写作与审稿项目规范.md`：summary/正文/假设/结果叙事/审稿输出。
- `references/10_图表与排版项目规范.md`：最终印刷字号、图例、多面板、技术路线图、三维图、图文连续、PDF/Word 验收。
- `references/11_验证与结果叙事.md`：基线、敏感性、负对照、绝对差/百分点、数据/代码可复现。
- `references/12_AI工具与学术诚信.md`：APMCM 2026 官方 AI 规定、正文标注、References 格式、`AI工具使用详情.pdf`、未使用声明。
- `references/13_评分与专家评阅.md`：APMCM 七条质量门、100 分内部诊断、P0/P1/P2。
- `references/14_协作与Git规范.md`：分支/commit/路径所有权/阶段门/交接。
- `references/15_附录、支撑材料与复现.md`：附录代码、可选支撑包、运行说明。
- `references/16_数据与业务题实战.md`：问题链、预处理、不确定性、业务约束、数字溯源。
- `references/17_在线信息约束与盲测纪律.md`：决策时刻信息清单、未来信息审计、一次性盲测、评估历史日志。
- `references/18_C题优秀论文逐页解剖.md`：数据类获奖论文逐页地图、页面配方、可迁移写法、非技术 Article。
- `references/19_优秀论文追踪分析规程.md`：新获奖论文三步分析流程、必答问题、截断副本检测。
- `references/20_建模叙事公式与可读性规范.md`：建模思路谱系、公式呈现规范、可读性句式、格式细节。
- `references/21_自有论文蒸馏.md`：三篇跨赛终稿的结构/证据链参考实现、附录体系、迁移边界。
- `references/22_数维杯与亚太杯摘要深度解剖.md`：Summary 黄金配方、证据链型/品牌叙事型双模板、逐句技巧。

**不可直接迁移（APMCM 优先）：**

- APMCM 正文 ≤25 页，summary/contents 是前置页；不要套用另一赛事“25 页含 summary/contents”的口径。以当届 APMCM 官方模板/格式说明为准。
- 页眉只用 `Team #<team number> Page <x> of <y>`；不要套用另一赛事的队号/题号页眉格式。
- Control Sheet 单独签名提交，**不进论文 PDF**。
- AI：APMCM 2026-11 已发布官方 AI 工具使用规定：允许辅助，但核心模型构建、算法设计与求解、结果分析必须由队员独立完成；使用 AI 须在正文相应位置标注、References 列工具、提交 `AI工具使用详情.pdf`；未使用须在 References 后写官方中文声明。不要套用另一赛事 30%/50% 阈值或 AI 报告模板。见 `12`。
- 另一赛事的具体题目、数据、图号、交付哈希/批次号不能迁移；只迁移可复用的方法与检查表。

---

## 1. 开赛 10 分钟：填 APMCM 参数

复制到 `00_赛题与规则/赛事参数.md`：

```markdown
P1 赛事：APMCM 2026（第十六届）
P2 题目：A / B / C / D（只能选一个）
P3 语言：English only；正文/图表/表注不得出现中文
P4 页数：summary p1；contents p2；正文≤25页；附录不限
P5 页眉：Team #<team number> Page <x> of <y>
P6 提交：论文 PDF（题号+队号.pdf）；control sheet 单独签名 PDF/JPG/PNG；支撑材料可选 .rar/.zip；如使用 AI，另提交 AI工具使用详情.pdf
P7 匿名：论文任何页不得出现姓名/学校/指导教师；队号可用
P8 模板：官方 LaTeX 模板 / Word；字号 11–12；英文
P9 AI：2026 官方规定；使用 AI 须正文标注/References 工具条目/AI工具使用详情.pdf；未使用须写官方中文声明
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

写作/审稿细则见 `09_写作与审稿项目规范.md`；评分/互审见 `13_评分与专家评阅.md`。

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

最终印刷尺寸、图例、多面板、图文连续和 PDF/Word 验收见 `10_图表与排版项目规范.md`；图件清单模板见 `assets/apmcm_figure_inventory_template.csv`。

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

- 2026 规则原文要求**每一页顶部**有参赛编号和页码；官方示例 `Team#apmcm2600001Page10of20`（空格/大小写按官方模板）。
- 2025 模板可能写作 `Team #<team number> Page <x> of <y>`；不要凭记忆固定空格，按当届模板生成并逐页核对（含 Summary/Contents）。
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

附录代码、可选支撑包、运行说明和复现检查见 `15_附录、支撑材料与复现.md`。

---

## 9. 验证与稳定性（APMCM 评审第 5 条）

每问至少做：

- 一致性/可行性：约束满足、残差、输出范围；
- 参数敏感性：关键参数 ±10—30%，或 2—3 档；
- 对照/负对照：baseline、随机基线、置换、留一；
- 误差/不确定性：bootstrap/重复实验/区间；
- 边界：不能声称什么（外推、因果、真实政策效果等）。

**写作**：不要只写“robust”；给表/图 + 数字 + 口径。详见 `references/common/14_模型检验与稳健性.md`。

验证/结果叙事/可复现的细则见 `11_验证与结果叙事.md`；数据/业务题见 `16_数据与业务题实战.md`。

### 9.1 AI 工具与学术诚信（APMCM 2026 强制披露）

- APMCM 2026-11 官方 AI 规定：AI 可作辅助，但**核心模型构建、算法设计与求解、结果分析必须由参赛队独立完成**；参赛队对 AI 内容的正确性/可靠性/学术规范负责。
- 使用 AI 必须：正文相应位置标注 + References 按官方格式列工具 + 提交 `AI工具使用详情.pdf`（工具/版本、用途/环节、关键提示与回复、采纳与人工修改）。
- 未使用 AI：在 References 后写官方原句 `本参赛队未使用任何AI工具`；不要改写成英文或另一赛事措辞。
- References 格式：`[编号]工具名称，版本/型号，开发机构/公司，使用日期。` 官方示例：`[1]DeepSeek,DeepSeek-R1-0528,深度求索（DeepSeek）,2026-6-12`。
- 不合规可取消评奖资格；不要伪造“未使用 AI”或 AI 记录。
- 不套用另一赛事 30%/50% AIGC 阈值或 AI 报告模板；APMCM 这份通知未给该阈值。本地 AIGC/PPL 扫描只作方向参考。
- 详见 `12_AI工具与学术诚信.md`；English 模板见 `assets/AI_Tool_Usage_Details_Template.md` / `.docx`。

---

## 10. 四天里的角色分工（3 人）

| 角色 | 职责 | 不做什么 |
|---|---|---|
| Modeler | 选题、假设、模型、结果解释 | 不包办全部写作 |
| Coder | 数据管线、求解、图、复现 | 不改模型主张 |
| Writer | 英文正文、summary、格式、提交 | 不编造结果 |

**每天固定 2 次对齐**：中午看结果/图，晚上看页数/摘要/第二天计划。
**任何数字只从结果文件进论文**；summary 与正文由同一张 `key_numbers.csv` 驱动。

分支、commit、路径所有权、阶段门和 handoff 见 `14_协作与Git规范.md`；环境/Git 凭据见 `references/common/17_WSL_Windows环境与Git.md`。

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
- [ ] 按时刻决策的规则做过未来扰动审计；freeze 早于首次测试，评估历史有日志（见 `references/17_在线信息约束与盲测纪律.md`）。
- [ ] 事件/窗口类指标有同速率平凡对照；逐时刻辨识与窗口命中分开报。
- [ ] 摘要/正文核心数字与附录对照、敏感性、负对照逐条无矛盾；最优解若退化已标代价。
- [ ] 全文一套评估身份名；同名量跨问口径一致或有解释。
- [ ] AI 四处留痕（正文标注 / References / 详情 PDF / 声明）一致；AI 报告未被擅自读写。

一键审计：

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf --zip Aapmcm2600001fj.zip
python scripts/audit_git_hygiene.py --root .
python scripts/env_doctor.py
```

---

## 12. 常见错误（Top 22）

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
| 13 | 把另一赛事 AI 阈值/模板套 APMCM | 误报/误填/诚信风险 | 先查 APMCM 当届规则，见 `12` |
| 14 | 决策规则用到决策后才产生的信息 | 在线成绩无效，原则性错误 | 决策时刻信息清单 + 未来扰动审计，见 `references/17_在线信息约束与盲测纪律.md` |
| 15 | 测试集被旧方案评过后再修模型 | 修订版永远无法补首次盲测 | 测试集最后一天才开；freeze 与评估历史日志 |
| 16 | 摘要/正文核心数字与附录对照矛盾 | 判选择性呈现 | 提交前逐条对账，弱于对照就降级写法 |
| 17 | 最优解是退化解还当主结果报 | 读成没回答问题 | 报代价指标 + 推荐工作点，上界与推荐分开 |
| 18 | AI 四处留痕不一致/擅扩写 AI 阐述 | 合规与诚信风险 | 四处对账；AI 阐述只写队员口径；报告不擅动 |
| 19 | 附件字段名义≠内容（运保费当货值） | 全盘皆输 | 开工先审计：导出参数+锚点量级+年份覆盖，见 `references/16_数据与业务题实战.md` |
| 20 | 五问五套割裂模型/五问全浅 | 无主线无深度 | 共享参数情景贯穿；主攻取舍写进论文，见 `16` |
| 21 | 非技术信件问写成技术报告 | 直接丢该问分 | 最后一问常要求给公司/市民/UN 写信，按非技术读者写，见 `references/03_四题路线与选题.md` |
| 22 | 结果页只放图表没有编号发现 | 评委自己解读，记不住 | 每个结果配"名字+数字+机制"编号发现句+每问小结，见 `references/18_C题优秀论文逐页解剖.md` |

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
| `references/09_写作与审稿项目规范.md` | summary/正文/假设/结果叙事/审稿输出/停止条件 |
| `references/10_图表与排版项目规范.md` | 最终尺寸字号、图例、多面板、技术路线图、三维图、图文连续、PDF/Word 验收 |
| `references/11_验证与结果叙事.md` | 基线、敏感性、负对照、绝对差/百分点、数据/代码可复现 |
| `references/12_AI工具与学术诚信.md` | APMCM 2026 官方 AI 规定、标注/References/详情说明/未使用声明；不套用另一赛事阈值/模板 |
| `references/13_评分与专家评阅.md` | APMCM 七条质量门、100 分内部诊断、P0/P1/P2 |
| `references/14_协作与Git规范.md` | 分支/commit/路径所有权/阶段门/handoff |
| `references/15_附录、支撑材料与复现.md` | 附录代码、可选支撑包、运行说明、复现检查 |
| `references/16_数据与业务题实战.md` | 问题链、预处理、不确定性、业务约束、数字溯源 |
| `references/17_在线信息约束与盲测纪律.md` | 决策时刻信息清单、未来扰动审计、盲测一次性、评估历史日志 |
| `references/18_C题优秀论文逐页解剖.md` | 数据类四篇获奖论文逐页地图、页面配方、品牌化手法、非技术 Article 写法 |
| `references/19_优秀论文追踪分析规程.md` | 每年新获奖论文的三步分析流程、必答问题、稳定结论、截断副本检测 |
| `references/20_建模叙事公式与可读性规范.md` | 获奖论文建模思路谱系、公式呈现规范（校准块/underbrace/分阶段）、可读性句式、格式细节 |
| `references/21_自有论文蒸馏.md` | 队上三篇跨赛终稿（数维杯为主）的结构/证据链参考实现、附录体系、迁移边界 |
| `references/22_数维杯与亚太杯摘要深度解剖.md` | Summary 黄金配方：硬指标区间、证据链型/品牌叙事型双模板、8 个逐句技巧与排版红线 |
| `references/important/MathorCup_2026_A2601605.pdf` | M 杯最终论文原件（元数据已清理，正文未改） |
| `references/common/` | 工件所有权、验证、总论文整合、数据路线、WSL/Git（13—17） |
| `assets/award_paper_metrics.csv` | 16 篇获奖论文的页数/摘要词数/数字/图表统计 |
| `assets/apmcm_submission_checklist.md` | 提交前逐项勾 |
| `assets/apmcm_review_report_template.md` | 队内 100 分诊断 + P0/P1/P2 报告模板 |
| `assets/apmcm_figure_inventory_template.csv` | 图件清单（页/问题/数据/字号/引用/状态） |
| `assets/apmcm_problem_chain_template.md` | 问题链、数据契约、主张→证据、数字溯源 |
| `assets/apmcm_ai_disclosure_checklist.md` | APMCM 2026 AI 工具使用检查清单 |
| `assets/AI_Tool_Usage_Details_Template.md` | English Markdown source for the official four AI usage items |
| `assets/AI_Tool_Usage_Details_Template.docx` | English, 2-page editable template |
| `assets/apmcm_terminology_template.csv` | 术语/符号/单位/首次出现位置 |
| `assets/summary_sheet_template.md` | 一页 summary 模板 |
| `assets/english_style_guide.md` | 英文写作/术语/标点 |
| `assets/paper_outline.md` | 论文骨架 |
| `assets/apmcm_external_review_prompt_template.md` | 请外部 AI 全量复核原则性错误的提示词模板 |
| `assets/apmcm_figure_playbook.md` | 数据题图表手册：目的→图型对照、配色规范、注释手法、图文衔接句式 |
| `scripts/audit_apmcm_submission.py` | PDF/页眉/目录/中文/元数据/包检查 |
| `scripts/analyze_award_papers.py` | 优秀论文结构特征批量扫描（v2：页眉截断检测、公式密度、小结件、代码页） |
| `scripts/audit_git_hygiene.py` | 仓库卫生 |
| `scripts/env_doctor.py` | 环境体检 |
