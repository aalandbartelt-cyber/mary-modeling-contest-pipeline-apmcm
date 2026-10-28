# APMCM English Style Guide

## 1. Sentence

- One claim per sentence; 15–25 words on average.
- Prefer active voice: "We estimate ...", "The model predicts ...".
- Avoid 50+ word sentences with multiple "which/that".
- Define abbreviations at first use.

## 2. Tense

| Part | Tense |
|---|---|
| Background / problem | present |
| What we did (method/experiment) | past |
| Results (specific run) | past |
| Conclusions / implications | present |
| Limitations | present |

## 3. Common fixes

| Weak | Better |
|---|---|
| "very significant" | "increases by 12.4% (0.31 vs 0.28)" |
| "we can see that" | "Table 3 shows that" |
| "obviously" | delete |
| "In order to" (too often) | "To" |
| "Firstly... Secondly... Finally..." | direct topic sentences |
| "model/framework/approach" mixed | pick one term per concept |

## 4. Punctuation

- Use English punctuation: `, . ; : ( )`.
- No full-width `，。；：（）`.
- Space between number and unit: `25 mm`, `12.4%`.
- Consistent decimal places in a column.
- Use `vs.` sparingly; prefer "compared with".

## 5. Figures/tables

- Figure caption below: `Figure 1: ...`
- Table caption above: `Table 1: ...`
- Axis labels include units.
- No Chinese in labels/legends.
- Explain the takeaway in text, not inside the figure.

## 6. Numbers

- Every number in the summary must appear in the body and a result file.
- Keep a `key_numbers.csv` as the single source.
- State the scope/period for every metric.

## 7. Final QA

1. terminology consistency
2. tense
3. articles/singular-plural
4. punctuation/full-width
5. numbers/units
6. captions
7. Chinese scan (body/figures)
