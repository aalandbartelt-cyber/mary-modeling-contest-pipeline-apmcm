# mary-modeling-contest-pipeline-apmcm

APMCM（亚太杯英文赛）专属 skill：4 天、A—D 四题、英文、正文 25 页、summary + contents + team header、control sheet 单独提交。

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
- `references/important/MathorCup_2026_A2601605.pdf`（M 杯 2026 A 最终论文，元数据已清理）
- `references/common/13—17`（工件所有权、验证、总论文整合、数据路线、WSL/Git）

## 脚本

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf \
  --control Aapmcm2600001cns.pdf --zip Aapmcm2600001fj.zip
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

canonical 版本以本目录为准；mcup/base skill 的通用门禁如有更新，同步 `references/common/13—17`。
