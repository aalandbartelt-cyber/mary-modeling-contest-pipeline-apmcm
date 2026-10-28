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
- `references/common/13—17`（工件所有权、验证、总论文整合、数据路线、WSL/Git）

## 脚本

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm2600001.pdf \
  --control Aapmcm2600001cns.pdf --zip Aapmcm2600001fj.zip
python scripts/audit_git_hygiene.py --root .
python scripts/env_doctor.py
```

## 安装

复制到：
- `~/.codex/skills/mary-modeling-contest-pipeline-apmcm`
- `%USERPROFILE%\.agents\skills\mary-modeling-contest-pipeline-apmcm`

canonical 版本以本目录为准；mcup/base skill 的通用门禁如有更新，同步 `references/common/13—17`。
