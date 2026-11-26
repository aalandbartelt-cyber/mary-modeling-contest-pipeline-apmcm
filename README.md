# mary-modeling-contest-pipeline-apmcm

APMCM（亚太杯英文赛）专属 skill：4 天、A—D 四题、英文、正文 25 页、summary + contents + team header、control sheet 单独提交。2026-11 起按官方 AI 规定执行：使用 AI 须正文标注/References 工具条目/`AI工具使用详情.pdf`；未使用须写官方中文声明。

2026-11 官方另发布《论文提交规范、论文模板、承诺书》：PDF `#***.pdf`、Control Sheet `#***cns.pdf/.jpg`（单独一页签名）、支撑材料 `#***fj.rar/.zip`（题面未明确要求则不要提交）、正文 ≤25 页、附录不限。原件在比赛工作区 `00_赛题与规则/官方发布/2026论文规范与模板/`（本地，gitignore）；规则摘要见 `references/01_APMCM赛制与提交.md`。

## 入口

先读 `SKILL.md`；再按赛题读：
- `references/01_APMCM赛制与提交.md`
- `references/02_英文论文结构与写作.md`
- `references/03_四题路线与选题.md`
- `references/04_四天冲刺与分工.md`
- `references/05_图表公式与LaTeX模板.md`
- `references/06_评审与答辩式自查.md`
- `references/07_优秀论文解剖.md`
- `references/08_M杯最终论文参考.md`（重要结构/验证参考，非 APMCM 模板）
- `references/09_写作与审稿项目规范.md`（项目级写作/审稿）
- `references/10_图表与排版项目规范.md`（最终尺寸/图例/图文连续/PDF 验收）
- `references/11_验证与结果叙事.md`
- `references/12_AI工具与学术诚信.md`（APMCM 2026 官方 AI 规定；勿套另一赛事阈值）
- `references/13_评分与专家评阅.md`
- `references/14_协作与Git规范.md`
- `references/15_附录、支撑材料与复现.md`
- `references/16_数据与业务题实战.md`
- `references/17_在线信息约束与盲测纪律.md`
- `references/18_C题优秀论文逐页解剖.md`
- `references/19_优秀论文追踪分析规程.md`
- `references/20_建模叙事公式与可读性规范.md`
- `references/21_自有论文蒸馏.md`
- `references/22_数维杯与亚太杯摘要深度解剖.md`
- `references/23_章节级解剖与模板库.md`
- `references/24_表格解剖与评委阅读路径.md`
- `references/important/MathorCup_2026_A2601605.pdf`（M 杯 2026 A 最终论文，元数据已清理）
- `references/common/`（13—17：工件所有权、验证、总论文整合、数据路线、WSL/Git）

## 常用资产

- `assets/apmcm_submission_checklist.md`
- `assets/apmcm_review_report_template.md`
- `assets/apmcm_figure_inventory_template.csv`
- `assets/apmcm_problem_chain_template.md`
- `assets/apmcm_ai_disclosure_checklist.md`
- `assets/AI_Tool_Usage_Details_Template.md`（English Markdown source）
- `assets/AI_Tool_Usage_Details_Template.docx`（English, 2 pages, editable）
- `assets/apmcm_terminology_template.csv`
- `assets/apmcm_external_review_prompt_template.md`
- `assets/apmcm_figure_playbook.md`
- `assets/summary_sheet_template.md`

## 脚本

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm263XXXXX.pdf \
  --control Aapmcm263XXXXXcns.pdf --zip Aapmcm263XXXXXfj.zip
python scripts/audit_git_hygiene.py --root .
python scripts/env_doctor.py
python scripts/analyze_award_papers.py --input 优秀论文.zip --out metrics.csv
```

## 优秀论文证据

`assets/award_paper_metrics.csv` 汇总 2022—2025 共 16 篇 APMCM 优秀论文的页数、summary 词数/数字数、图/表数量；`references/07_优秀论文解剖.md` 给出结构、summary、图表与 Model Evaluation 的获奖规律。

## 安装

复制到：
- `~/.codex/skills/mary-modeling-contest-pipeline-apmcm`
- `%USERPROFILE%\.agents\skills\mary-modeling-contest-pipeline-apmcm`

canonical 版本以本目录为准；mcup/base skill 的通用门禁如有更新，同步 `references/common/`。
