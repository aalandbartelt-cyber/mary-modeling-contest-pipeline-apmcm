# 01 APMCM 赛制与提交

> 依据（2026-11 官方三件套）：
> - 《2026 APMCM Essay format and submission specifications》（2 页，2026.11）
> - 《APMCM 竞赛通知丨论文提交规范、论文模板、承诺书发布》（2026-11）
> - 2026 年第十六届 APMCM 参赛规则
>
> 官方原件在比赛工作区 `00_赛题与规则/官方发布/2026论文规范与模板/`（本地，gitignore）：格式规范 PDF、Summary Sheet.docx、Control Sheet.docx、APMCM LaTeX 模板（cls/cfg/main.tex/ControlSheet.tex/示例 PDF）。
> 本文件是备赛/提交清单，不替代原件；冲突时以官方原件为准。

---

## 1.1 2026 关键信息

| 项 | 2026 官方要求 |
|---|---|
| 名称 | 2026 年第十六届 APMCM 亚太地区大学生数学建模竞赛 |
| 报名截止 | 北京时间 2026-11-25 24:00 |
| 开赛 | 北京时间 2026-11-26（周四）06:00 |
| 结束/提交截止 | 北京时间 2026-11-30（周一）09:00 |
| 提交系统 | https://www.saikr.com/vse/apmcm26 |
| 队号 | **13 位**，赛氪报名编号 `apmcm263*****`（报名系统生成） |
| 队伍 | ≤3 名全日制在校大学生；每人只能参加一队 |
| 题目 | A/B/C/D 任选 **一题**；报名系统所选字母必须与论文内容一致，不一致**取消资格** |
| 语言 | 英文；正文、图表、表注不得出现中文 |
| 首页 | p1 = Summary Sheet（论文第一页） |
| 第 2 页 | p2 = Directory / Contents（目录页） |
| 正文 | 目录页之后开始；**正文 ≤25 页**；附录不限 |
| 页眉 | 只允许队号 + 页码，不得出现姓名/学校信息 |
| 字号 | 一般 11 或 12（其余版式无硬性要求，但要美观） |
| 论文 PDF | `#***.pdf`（`#`=题号，`***`=队号），例 `Aapmcm2630001.pdf` |
| Control Sheet | `#***cns.pdf` 或 `#***cns.jpg`，**单独一页、打印签名、扫描/拍照** |
| 支撑材料 | `#***fj.rar` 或 `#***fj.zip`；**题面未明确要求时不要提交**（见 1.6） |
| 匿名 | 论文任何页不得出现姓名、学校、指导教师、邮箱；队号可用 |
| 模板 | Word 或 LaTeX 均可；官方模板**仅供参考、不做强制要求** |

**合规红线（官方原文）**：`Solution papers that do not comply with this specification will be considered as breaking the competition rules and unconditionally disqualified.` 格式不合规 = 违规，无条件取消资格；不要赌“应该没事”。

---

## 1.2 论文结构

```text
p1  Summary Sheet
    - 顶部表：Team Number / Problem Chosen
    - 标题：2026 APMCM summary sheet
    - Summary 正文（一页内）
    - Keywords
p2  Contents（目录）
正文（页码从 1 重新开始）:
  Introduction
  Assumptions and Notations
  Data / Problem Analysis
  Model(s) and Solution(s)
  Model Evaluation / Sensitivity
  Conclusions
  References
  Appendix: 软件名 + 全部源代码
```

- Summary 必须**恰好一页**；Contents 单独一页；正文从 Contents 之后开始。
- 官方口径是 “main body ≤25 pages, appendix no limit”：25 页只约束正文，**Summary/Contents 是前置页，不占 25 页**；附录另计。
- 论文 PDF 不包含 Control Sheet / 支撑材料。
- 官方 Word `Summary Sheet.docx` 已把 Summary 页和 Contents 页放在同一文件；用它时不要把 Contents 删掉。

---

## 1.3 页眉与页码（官方模板实测）

官方 LaTeX 模板 `apmcmthesis.cls` 的实际行为（`main.pdf` 实测）：

| 页 | 左页眉 | 右页眉 |
|---|---|---|
| p1 Summary | `Team # apmcm263XXXXX` | 无页码 |
| p2 Contents | `Team # apmcm263XXXXX` | 无页码 |
| 正文 p1 起（`\setcounter{page}{1}`） | `Team # apmcm263XXXXX` | `Page x of y` |
| 附录 | 同上 | 同上 |

- `y` = `\pageref{LastPage}`，即**正文 + 附录**的最后一页（模板在 Contents 后重置页码，所以 y 不含 Summary/Contents）。**不要手写 `of 25`**；y 大于 25 不代表正文超页，正文页数单独按 References 前计算。
- 格式规范正文的示例写作 `Team Aapmcm26300001` / `Page 10 of 25`（不带 `#`，且 25 只是示例数字）；官方模板输出是 `Team # apmcm263XXXXX` + `Page x of y`。**以官方模板导出效果为准**；手工 Word 时照模板做左队号、右页码，不要自创第三种写法。
- 页眉只允许队号与页码；姓名、学校、指导教师、邮箱、学号一律不得出现。
- 每页都查：Summary、Contents、正文、附录、代码页。
- 2026 规范明确说“未提及的版式（字体、行距、颜色等）没有具体要求，但要让论文美观”——页眉/页码/首页/目录/25 页是硬项，版式是软项。

---

## 1.4 参考文献格式（官方三类）

正文引用用方括号编号 `[1]`、`[3]`；按首次引用顺序编号，每条都在正文被引用。

```text
书籍：  [ID] Author, Title[M], Place of Publication: Press, Year, start-end pages.
期刊：  [ID] Author, Paper title[J], Journal name, Year, Volume, start-end pages.
网络：  [ID] Author, Resource title, Website, visit time (Year, Month, Day).
```

- **引用书籍必须给页码**（官方明确要求）。
- 引用他人成果/公开信息（含网上资料）必须同时出现在正文引用位置和 References。
- 不把中文文献条目写成中文；英文/拼音按可核验信息写。
- 不编造条目；无法核验的来源要标注说明。

---

## 1.5 Control Sheet（承诺书）

官方要点（通知原文 + Control Sheet.docx）：

- Control Sheet 即承诺书，**必须单独一页**；打印后手写签名，扫描为 PDF，或拍照成 JPG。
- 电子签名可用：签名图片放入 Word → 转 PDF。
- 命名：`#***cns.pdf` 或 `#***cns.jpg`（如 `Aapmcm26300001cns.pdf`）；官方只列 PDF/JPG，不写 PNG。
- 可赛前先下载、签名；选题后在“Problem chosen”补题号。
- 字段：Problem chosen（A/B/C/D）、Team control number、School（全称）、Member name（三人手写签名）、Team adviser name、Date；全部用英文填写。
- 三名队员**每人都要签**；缺签名 → 全队取消资格（模板原文）。
- 提交后不得修改；填错可能取消评奖资格。
- **切勿把 Control Sheet 放进论文正文**，否则按违规处理。
- Control Sheet 可以出现学校/姓名/签名——它是单独文件，不受论文匿名约束。

---

## 1.6 支撑材料

官方原文：`The name of the supporting materials is "#***fj.rar", or "# *** fj.zip".` 并括注：

> `supporting materials (if they are not expressly required in the problem, please do not submit)`

- **题面没有明确要求时，不要提交支撑材料**；不要习惯性打包上传。
- 若题面要求（或你判断确有必要）：命名 `<题号><队号>fj.rar` / `.zip`；内容为程序、非赛题原始数据、结果等。
- 不含赛题原始数据；不含身份信息/缓存/虚拟环境。
- 无论是否交支撑材料，**论文附录都必须写软件名 + 全部源代码**；源代码保留到获奖名单公布，供组委会测试。

---

## 1.7 模板与排版路线

- 官方模板（Word Summary/Control Sheet、LaTeX `apmcmthesis`）**仅供参考，不做强制要求**；但套模板最省格式风险。
- 官方建议：不熟 LaTeX 的队不要用 LaTeX；任何排版软件自身编译错误，组委会不解答。
- Word 路线：用 `2026 APMCM Summary Sheet.docx`（含 p1 Summary + p2 Contents）与 `2026 APMCM Control Sheet.docx`；页眉按 1.3 手工设置；目录用 TOC 域并在导出前更新。
- LaTeX 路线：`\documentclass{apmcmthesis}`、`\tihao{A}`、`\baominghao{apmcm263XXXXX}`；`frontmatterstyle` → `abstract` → `\tableofcontents` → `mainmatterstyle` → `\setcounter{page}{1}`。
- 模板自带中文示例（CJK 字样、公众号图、中文 caption、`cat` 图）必须删除/替换；正文/图内不得有中文。
- 不要改模板的页面设置（geometry：上下 26.4 mm、左右 31.8 mm）和页眉格式。

---

## 1.8 提交前 P0

- [ ] 报名系统题号 = 论文题号 = 文件名首字母；队号 13 位 `apmcm263*****`；
- [ ] 论文名 `#***.pdf`；Control Sheet `#***cns.pdf/.jpg`；支撑材料仅在题面要求时交 `#***fj.rar/.zip`；
- [ ] p1 Summary（Team Number / Problem Chosen / Keywords）；p2 Contents；正文 ≤25 页；
- [ ] Summary 第一页填了选题 + 队号；
- [ ] 页眉每页只有队号+页码；正文页 `Page x of y`，y 用模板 `LastPage` 自动生成；
- [ ] 正文/图表/代码注释/图内文字无中文；
- [ ] 无姓名/学校/教师/邮箱/学号（摘要/正文出现个人信息最高只获成功参赛奖）；
- [ ] 查重自查：未与其他队共享文稿/代码；与公开/他队文本相似度 <30%；
- [ ] Control Sheet 三人英文签名、单独一页、未混入论文；
- [ ] 附录有软件名 + 全部源代码；代码保留到获奖名单公布；
- [ ] PDF 元数据干净；干净环境（另一台机器/阅读器）打开一次；
- [ ] 提前 ≥30 分钟提交；重传后点了“提交电子档”。

一键检查：

```bash
python scripts/audit_apmcm_submission.py --paper Aapmcm263XXXXX.pdf \
  --control Aapmcm263XXXXXcns.pdf [--zip Aapmcm263XXXXXfj.zip]
```

---

## 1.9 参赛纪律与提交操作（2026-11-26《参赛纪律和论文提交方式说明》）

> 官方 3 页说明，开赛当天发布；以下为原文要点。

**纪律红线**

- 严禁抄袭、购买论文；禁止参加各种“竞赛思路交流群”，否则取消评奖资格。
- 论文会做**自建库查重**：两篇论文相似度**超过 30%** 视为作弊，取消相似论文参赛资格，情节严重者公开通报。
  → 不与其他队共享文稿/代码/图表源文件；引用他人内容必须改写并标注来源；队友间也不要把同一份草稿发给外部“润色”。
- Summary 第一页必须填写**选题和队号**（赛氪报名编号 `apmcm263*****`，共 13 位）。
- 摘要页和正文**不得出现参赛者个人信息**；一旦出现，**最高只能获得成功参赛奖**（不是简单退回修改）。
- 控制页签名：**姓名用英文签名**。

**提交操作**

- 队长用自己电脑登录 https://www.saikr.com/vse/apmcm26 → 我的竞赛 → 报名管理 → 去提交。
- **至少提前 30 分钟—1 小时提交**；上传需要时间，卡点必失败。
- 截止前可重新上传；但必须点右下角**“提交电子档”**确认，不点不会更新。
- 备用邮箱：仅在赛氪系统上传失败时使用；**已在赛氪成功提交的队伍禁止再发邮箱**（重复无效，以赛氪为准）。
- 邮箱提交每人限一次，**以第一次为准**；所有文件放在**一封邮件、一个压缩包**里；邮箱地址 11-30 公布。
- 邮件标题写队号；论文附件 `题号+队号.pdf`；承诺书+支撑材料打包 `题号+队号.rar/zip`。
- 支撑材料口径冲突：本说明写“支撑材料（可选）”，格式规范写“题面未明确要求请不要提交”→ 以更严格的格式规范为准，除非题面明确要求。

---

## 1.10 2026 易漏点（规则 + 规范原文核对）

- 队伍上限 **3 名全日制在校大学生**；每人只能参加一支队伍，重复参赛取消成绩。
- 竞赛期间不得向指导教师或队外任何人寻求帮助/讨论（Email、电话、私下交谈、网络聊天、问答系统都禁止）。AI 工具按 `12_AI工具与学术诚信.md` 的官方规定单独处理，不能用来绕开“队外帮助”限制。
- 所有引用的数据/资料必须注明出处；未注明引用可能取消参赛资格。
- 提交电子版论文 + 承诺书；支撑材料按题面要求（未要求不交）。三件同时提交到报名系统。
- 摘要页必须是论文第一页；第二页是目录；正文从目录后开始；字号一般 11 或 12。
- 页眉只含队号与页码；官方模板 front matter 只有队号、正文起才加页码。
- 论文 PDF 不含 Control Sheet/附件；Control Sheet 单独命名上传。
- 附录必须给软件名 + 全部源代码；源代码保留到获奖名单公布。
- 官方模板仅供参考；不熟 LaTeX 不要硬上；编译问题组委会不解答。
- **格式不合规 = 无条件取消资格**；官方保留最终解释权。
- 2026 奖项表（官方表 1）：创新奖 2 队/题（1000 元/队）；一等奖 5%；二等奖 15%；三等奖 25%；成功参赛奖。没有通过/不通过分数线，评审依据解决方案质量。
- 评审七条：题意解读、假设合理性、建模思路、模型有效、稳定性检验、优缺点/结论、摘要。见 `06_评审与答辩式自查.md`。
- AI 使用：见 `12_AI工具与学术诚信.md`；使用 AI 须正文标注 + References 工具条目 + `#***ai.pdf`；未使用须写官方中文声明。
