# Changelog

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
