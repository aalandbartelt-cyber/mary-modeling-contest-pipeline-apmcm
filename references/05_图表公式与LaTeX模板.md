# 05 图表、公式与 LaTeX/Word 模板

> 深度规范：`10_图表与排版项目规范.md`（最终字号/图例/多面板/图文连续/PDF 验收）。
> 本文是快速规则；冲突时以 APMCM 官方模板和 `10` 为准。

---

## 5.1 英文图表

- 图题在图下：`Figure 1: ...`；表题在表上：`Table 1: ...`。
- 所有标签、图例、单位、注释用英文；不得出现中文。
- 白底、细线框、无网格、颜色在灰度下可区分。
- 坐标轴写单位；图例内嵌、无边框；字号 ≥7 pt（缩到版心仍可读）。
- 每张图在正文被引用，并解释“说明了什么”，不要只复述数字。
- 图内不要放整段结论；结论写正文。
- 300 dpi PNG/矢量 PDF；不要用中文截图。

**常见错误**：中文坐标轴、中文图例、图题在图上、图表与正文数字不一致、图表未被正文引用。

---

## 5.2 表格

- 三线表；表题在表上；英文表头；单位写清。
- 表不跨页；跨页表重复表头。
- 数字对齐（小数点/位数）；百分比与小数口径统一。
- 每张表在正文被引用。
- 大表放附录；正文只留关键列。

---

## 5.3 公式

- 用 LaTeX/Word 原生公式；不要图片公式。
- 全文连续编号 `(1)...(N)`；正文引用同步。
- 符号首次出现解释；符号表只作汇总。
- 多字母变量用 `\mathrm{}` 或统一斜体规则；单位用正体。
- 公式前后要有文字说明，不要“公式堆”。

---

## 5.4 APMCM LaTeX 模板（2026 官方版）

2026 官方 LaTeX 模板在比赛工作区 `00_赛题与规则/官方发布/2026论文规范与模板/APMCM LaTeX 模板/`（`apmcmthesis.cls` + `apmcmthesis.cfg` + `main.tex` + `ControlSheet.tex` + 编译示例 PDF）。

关键设置：

```latex
\documentclass{apmcmthesis}
\tihao{A}                      % 题号
\baominghao{apmcm26XXXXX}      % 队号
\begin{document}
\pagestyle{frontmatterstyle}
\begin{abstract} ... \keywords{...} \end{abstract}
\newpage
\tableofcontents
\newpage
\pagestyle{mainmatterstyle}
\setcounter{page}{1}
...
\end{document}
```

- 页面：`geometry{top=26.4mm,bottom=26.4mm,left=31.8mm,right=31.8mm}`，行距 1.38；不要改。
- 页眉：`frontmatterstyle` 只放左页眉 `Team # <队号>`；`mainmatterstyle` 左队号 + 右 `Page \thepage\ of \pageref{LastPage}`；页码在 Contents 后重置为 1，所以 y = 正文+附录页数（不含 Summary/Contents）。
- Summary 页由 `abstract` 环境生成：顶部 Team Number/Problem Chosen 表 + `2026 APMCM summary sheet` + 摘要 + Keywords。
- Control Sheet 用 `ControlSheet.tex`（`\schoolname`、`\membera/b/c`、`\supervisor`、`\filldate`、`\makecontrolsheet`）单独编译；不要并进 `main.tex`。

**必须清理**：

- 模板里的中文示例（CJK、公众号图、中文 caption）全部删除/替换；
- `cat`、`gongzhonghao` 等示例图不要带入；
- 编译后检查 p1/p2 页眉（应只有队号）、正文页眉（队号+页码）、目录、页码重置；
- 不要改模板的页面设置/页眉格式。

**编译**：PDFLaTeX 推荐；含中文才用 XeLaTeX，但 APMCM 正文不允许中文，所以最终应无 CJK。官方提醒：不熟 LaTeX 的队不要用；编译错误组委会不解答。

---

## 5.5 Word 路线

官方 Word 模板（2026）：

- `2026 APMCM Summary Sheet.docx`：p1 Summary（Team Number/Problem Chosen 表 + 标题 + 摘要 + Keywords）+ p2 Contents；
- `2026 APMCM Control Sheet.docx`：单独一页承诺书，三人签名后导出 PDF/JPG，命名为 `<题号><队号>cns.pdf/.jpg`；不要并进论文。

手工 Word 要点：

- 第 1 页 Summary；第 2 页 Contents（TOC 域，导出前更新）；
- 页眉：Summary/Contents 页只放 `Team # <队号>`；正文起左队号、右 `Page X of Y`（分节 + 页码从 1 开始）；
- 正文 11/12 pt；页边距/行距无硬性规定，但整篇要统一、美观；
- 图表题注样式统一；公式用 Word 原生 OMML；
- 导出 PDF 后逐页检查页眉/目录/页码。

**Word 的坑**：TOC 域不更新、页眉“首页不同”导致 p1 没队号、分节符把页码带错、图片压缩、公式变图片、PDF 元数据带用户名。

---

## 5.6 提交前图表检查

- [ ] 图/表编号连续；
- [ ] 正文引用都存在；
- [ ] 图题在图下、表题在表上；
- [ ] 图与图题同页；表不跨页；
- [ ] 图内无中文；
- [ ] 灰度可区分；
- [ ] 单位/图例/坐标轴英文；
- [ ] 图表数字与 `key_numbers.csv` 一致。
