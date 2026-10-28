# 05 图表、公式与 LaTeX/Word 模板

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

## 5.4 APMCM LaTeX 模板

官方 LaTeX 模板（2025）在 `2025 APMCM 论文提交规范、论文模板、承诺书/APMCM LaTex模板.zip`。

关键设置：

```latex
\documentclass{apmcmthesis}
\tihao{A}                 % 题号
\baominghao{apmcm26XXXXX} % 队号
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

**必须清理**：

- 模板里的中文示例（CJK、公众号图、中文 caption）全部删除/替换；
- `cat.pdf`、`gongzhonghao` 等示例图不要带入；
- 编译后检查页眉、目录、页码；
- 不要改模板的页面设置/页眉格式。

**编译**：PDFLaTeX 推荐；含中文才用 XeLaTeX，但 APMCM 正文不允许中文，所以最终应无 CJK。

---

## 5.5 Word 路线

如果不用 LaTeX：

- 第 1 页 Summary；第 2 页 Contents（可用 Word TOC 域）；
- 页眉 `Team #... Page X of Y`；
- 正文 11/12 pt；页边距/行距按模板；
- 图表题注样式统一；
- 公式用 Word 原生 OMML；
- 导出 PDF 后逐页检查页眉/目录/页码。

**Word 的坑**：TOC 域不更新、页眉首页不同、图片压缩、公式变图片、PDF 元数据带用户名。

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
