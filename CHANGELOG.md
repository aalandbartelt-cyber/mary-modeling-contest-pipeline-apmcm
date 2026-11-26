# Changelog

## 2026-11-26 — D 题（量子优化）专属材料

- 新增 `references/25_D题量子优化优秀论文解剖.md`：2025D 机组组合 27 页完整本逐页解剖——QUBO 叙事骨架、逐约束罚函数章法、验证织进结果表、成本/精度权衡表件、规模缩减叙事，附 2026D（钙钛矿）结构差异对照。
- 新增 `references/26_D题三模链条完整性与诚信纪律检查清单.md`：D 题冲奖验收闸口——一票否决红线、三模（经典/代理/量子）链条逐问检查、差异化反超点、评委攻防演练。
- 新增 `references/27_Kaiwu_SDK_1.4.4_精读蒸馏.md`：164 页官方文档 API 级精读——QUBO→Ising 精确转换、精度四法定级、`get_min_penalty` 实质、真机双模式、排雷速查表、方法节英文句式。
- 新增 `assets/apmcm_d_plot_templates.py`（三联诊断/四维气泡 Pareto/plasma 热图/富集度统计图）与 `assets/apmcm_d_table_templates.tex`（booktabs T1—T8，验证列内嵌结果表/量子经典对照/成本账本/质量六项/三层误差账）。
- `assets/apmcm_figure_playbook.md` 增补 §13—15 量子题专题：QUBO 矩阵热图、精度-位宽曲线、真机证据图、富集度统计图、成本账本图。
- `07_优秀论文解剖` / `19_优秀论文追踪分析规程` / `20_建模叙事公式与可读性规范` 与 SKILL 增补 D 题交叉引用；修正 Devin 插入 SKILL 0.3 时误用的表格行，恢复为列表并补齐 25—27 索引。

## 2026-11-26 — 2026 赛题发布 + 参赛纪律/提交方式说明

- 新增 2026 四题画像（`references/03_四题路线与选题.md` 3.1.1，`SKILL.md` 第 3 节）：A 洪水灾害评估与应急救援（图像识别）、B 转炉炼钢双模态时序融合、C 非洲企鹅声通信与回放响应、D 量子计算机钙钛矿稀有目标搜索；附数据规模、分问结构、方法路线与选题提示。
- 修正“字母位置极稳”的旧规律：2026 的 B/C 已换赛道，不能按字母押题型。
- 新增 `references/01_APMCM赛制与提交.md` 1.9 参赛纪律与提交操作：自建库查重 >30% 判作弊、摘要/正文个人信息最高只获成功参赛奖、承诺书英文签名、提前 30—60 分钟提交、重传须点“提交电子档”、备用邮箱规则。
- 队号统一为官方 13 位 `apmcm263XXXXX`（原 `apmcm26XXXXX` 少一位），涉及 SKILL/README/refs 01/02/05/08/assets/audit 脚本。
- `references/12_AI工具与学术诚信.md` 增补 2026 查重红线（与 AIGC 阈值是两套要求）。
- `assets/apmcm_submission_checklist.md` 增补查重、英文签名、提交窗口、重传确认、邮箱规则。
- `SKILL.md` P0 增补查重/签名/提交确认；参考索引更新 ref 01/03 描述。

## 2026-11-25 — 2026 官方提交规范 / 模板 / 承诺书落地

- 读取 2026-11 官方《Essay format and submission specifications》（2 页）、《论文提交规范、论文模板、承诺书发布》通知、`2026 APMCM Summary Sheet.docx`、`2026 APMCM Control Sheet.docx`、2026 LaTeX 模板（`apmcmthesis.cls` / `main.tex` / `ControlSheet.tex` / 示例 PDF）。
- 重写 `references/01_APMCM赛制与提交.md`：
  - 命名：论文 `#***.pdf`、Control Sheet `#***cns.pdf/.jpg`、支撑材料 `#***fj.rar/.zip`；官方例 `Aapmcm2630001.pdf`。
  - 页眉实测：p1 Summary / p2 Contents 只有 `Team # <队号>`；正文起左队号 + 右 `Page x of y`；y 来自 `\pageref{LastPage}`（正文+附录，不含前置页），不手写 `of 25`。
  - Control Sheet 必须单独一页、三人签名、可赛前预签后补题号、禁止混入论文。
  - 支撑材料官方括注：题面未明确要求则不要提交。
  - 参考文献三类格式（书籍必须带页码）、附录软件名+全部源码并保留到获奖名单公布、格式不合规无条件取消资格、模板仅供参考/不熟勿用 LaTeX。
- 更新 `references/05_图表公式与LaTeX模板.md` 5.4/5.5：2026 官方 LaTeX 模板实测设置、`ControlSheet.tex` 单独编译、Word 两套官方模板与分节页眉做法。
- 更新 `assets/apmcm_submission_checklist.md` A/D/E 节：首页/目录页眉、`Page x of y` 口径、命名、承诺书、支撑材料政策、书籍页码、源码保留。
- 更新 `SKILL.md`：对比表、参数模板、页眉/命名/Control Sheet/支撑材料小节、P0 清单与审计命令。
- 更新 `scripts/audit_apmcm_submission.py`：新增前置页队号页眉检查；control sheet 只接受 `.pdf/.jpg`；支撑材料增加“未要求不交”提示。

## 2026-11-25 — Devin 深度优化（references 17—22 + 指标脚本 v2）

- 新增 `references/17_在线信息约束与盲测纪律.md`：决策时刻信息清单、未来信息扰动审计、一次性盲测、评估历史日志。
- 新增 `references/18_C题优秀论文逐页解剖.md`：数据类获奖论文逐页地图、页面配方、可迁移写法、非技术 Article 写法。
- 新增 `references/19_优秀论文追踪分析规程.md`：每年新获奖论文三步分析流程、必答问题、截断副本检测。
- 新增 `references/20_建模叙事公式与可读性规范.md`：建模思路谱系、公式呈现规范、可读性句式、格式细节。
- 新增 `references/21_自有论文蒸馏.md`：MathorCup/国赛/数维杯三篇终稿的结构与证据链参考实现、附录体系、迁移边界。
- 新增 `references/22_数维杯与亚太杯摘要深度解剖.md`：Summary 黄金配方、证据链型/品牌叙事型双模板、逐句技巧。
- 新增 `assets/apmcm_external_review_prompt_template.md`、`assets/apmcm_figure_playbook.md`。
- `scripts/analyze_award_papers.py` 升级 v2：新增页眉页数、公式密度、代码页、正文词数中位数、图重页等指标；`assets/award_paper_metrics.csv` 同步为 v2 列。
- 更新 `SKILL.md`：0.3 增补 17—22 入口；常见错误扩为 Top 22；参考链接统一为完整文件名。
- 更新 `README.md`：入口与资产列表补 17—22 与两个新 asset。
- 修正 `references/21_自有论文蒸馏.md` 页数口径：88 页 = 25 计页（Summary + Contents + 23 正文）+ 63 附录。

## 2026-11-24 — APMCM 2026 官方 AI 规定与规则补充

- 读取 `2026年第十六届APMCM...参赛规则.pdf` 六页原文及组委会 2026-11《人工智能工具使用规定》。
- 重写 `references/12_AI工具与学术诚信.md`：AI 适用范围、核心模型/算法/结果分析独立完成、正文标注、References 格式、`AI工具使用详情.pdf`、未使用官方中文声明、违规取消资格、剽窃/来源确认。
- 新增 `assets/AI_Tool_Usage_Details_Template.md` 与 `.docx`（English，2 页）：官方四项内容模板；DOCX 可直接填写后导出 PDF。提交用模板不含内部 self-check checklist；检查项留在 `apmcm_ai_disclosure_checklist.md` 与项目 AI 规范中。
- 更新 `references/01_APMCM赛制与提交.md`：2026 规则易漏点（3 人队、禁止队外帮助、引用出处、论文形式、每页页眉原文示例、支撑材料/源代码、保留附件、奖项表）。
- 更新 `SKILL.md` 9.1/0.3/AI 提交参数；`06_评审与答辩式自查.md` 6.6；`assets/apmcm_submission_checklist.md`、`apmcm_ai_disclosure_checklist.md`。
- 明确：APMCM 2026 这份 AI 通知没有 30%/50% AIGC 阈值；不得把另一赛事阈值/报告模板当 APMCM 规则。

## 2026-11-24 — 项目写作/图表/Git 规范迁移

- 新增 `references/09_写作与审稿项目规范.md`：summary、正文、假设/符号、结果叙事、审稿输出、停止条件。
- 新增 `references/10_图表与排版项目规范.md`：最终印刷字号、图例、多面板、技术路线图、三维图、图文连续、PDF/Word 验收。
- 新增 `references/11_验证与结果叙事.md`：基线、敏感性、负对照、百分比/百分点、数据/代码复现。
- 新增 `references/12_AI工具与学术诚信.md`：APMCM AI 披露（后续按 2026-11 官方通知更新为强制披露）；明确不套用另一赛事的 30%/50% 阈值、六类留痕或 AI 报告模板。
- 新增 `references/13_评分与专家评阅.md`：APMCM 七条质量门、100 分内部诊断、P0/P1/P2。
- 新增 `references/14_协作与Git规范.md`：分支/commit/路径所有权/阶段门/handoff。
- 新增 `references/15_附录、支撑材料与复现.md`：附录代码、可选支撑包、运行说明、复现。
- 新增 `references/16_数据与业务题实战.md`：问题链、预处理、不确定性、业务约束、数字溯源。
- 新增 assets：`apmcm_review_report_template.md`、`apmcm_figure_inventory_template.csv`、`apmcm_problem_chain_template.md`、`apmcm_ai_disclosure_checklist.md`、`apmcm_terminology_template.csv`。
- 更新 `SKILL.md`：0.3 项目规范入口、写作/图表/验证/AI/评分/协作指针、Top 13（2026-11-25 扩为 Top 22）。
- 明确不可直接迁移：APMCM 页码口径（正文 25 页、summary/contents 前置）、`Team #... Page x of y` 页眉、control sheet 单独提交、另一赛事 AIGC 阈值/AI 报告、具体题目/数据/图号/交付哈希。

## 2026-10-28 — 加入 M 杯最终论文参考

- 新增 `references/important/MathorCup_2026_A2601605.pdf`：M 杯 2026 A 题最终论文；仅清理 PDF 元数据，正文/页数未改。
- 新增 `references/08_M杯最终论文参考.md`：页面对照、可迁移做法（验证/共享接口/技术路线/附录/边界）、不可照搬项（中文/30 页/赛道格式/具体模型）。
- `SKILL.md` 增加 0.2 重要参考；README/参考索引同步。
- 说明：M 杯论文是结构/证据链参考，不是 APMCM 模板；APMCM 仍按英文、25 页、summary/contents/control sheet 执行。

## 2026-10-28 — 优秀论文二次解剖

- 阅读 2022—2025 年 16 篇 APMCM 优秀论文（A—E，含 2025 A—D）。
- 新增 `references/07_优秀论文解剖.md`：量化画像、共同骨架、summary 写法、图表/Model Evaluation 规律、题型信号、章节标签频率、页数分配、不要照抄的例外。
- 新增 `assets/award_paper_metrics.csv`：页数、summary 词数/数字数、图/表数量统计。
- 新增 `scripts/analyze_award_papers.py`：可从优秀论文 zip/目录重新统计结构指标。
- 更新 `SKILL.md`：获奖论文实际画像；summary 目标 350—450 词、10—25 个数字；页数分配；章节标签频率。
- 更新 `assets/summary_sheet_template.md`：获奖式开头/每问段落/结尾/边界。
- 更新 `references/06_评审与答辩式自查.md`：从 16 篇论文提炼的“获奖动作”。

## 2026-10-28 — 初始 APMCM 专属版


- 新建 `mary-modeling-contest-pipeline-apmcm`。
- 基于 2026 APMCM 参赛规则 + 2025 论文格式规范 + 2025 A—D 题分析 + 2025 优秀论文。
- 固化：4 天、A—D 四题、英文-only、正文 ≤25 页、summary p1、contents p2、Team # header、control sheet 单独提交、支撑材料可选。
- 新增 references 01—06：赛制/英文写作/四题路线/四天冲刺/图表与 LaTeX/评审自查。
- 新增 assets：提交清单、summary 模板、英文风格指南、论文骨架。
- 新增 `scripts/audit_apmcm_submission.py`：文件名、summary、contents、25 页、header、中文、身份、元数据、control sheet、ZIP。
- 复用 common 13—17：工件所有权、模型检验、总论文整合、数据概览/技术路线、WSL/Git。
