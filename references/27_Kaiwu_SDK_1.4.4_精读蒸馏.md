# 27. Kaiwu SDK 1.4.4 精读蒸馏（P2/P3 实施与论文写作专用）

> 来源：164 页官方文档汇编逐页精读（`01_Kaiwu官方/kaiwu_SDK_1.4.4_官方文档汇编_164页.pdf`），提取 API 级精确语义。
> 与第四轮审定版互补：那边是文献与理论框架，本文件是**安装版 SDK 的确切行为**。冲突时以安装版源码+小实例枚举验证为准。

---

## 27.1 QUBO→Ising 精确转换（论文公式节直接可用）

官方文档给出的转换公式（s = 2x − 1 代入展开）：

```
J_ij = q_ij / 4
h_i  = q_ii / 2 + (1/4) Σ_{k≠i} (q_ik + q_ki)
常数项 = Σ q_ii/2 + Σ_{i≠j} q_ij/4   ← 单独记录！
```

**三条纪律（全是血坑）：**
1. **Ising 线性项不能放对角线**——因为 s²=1 而非 x²=x；线性项必须进 h_i 或加辅助变量；
2. **常数项在优化中可忽略，但计算总能量/比较能量差时必须加回**——论文中所有能量数值若漏加常数项就是错的；
3. **SPQC 无法直接处理含线性项的 Ising，SDK 会加一个辅助自旋（参考自旋）**：104/208 个 QUBO 变量 → **105/209 个 Ising 自旋**（再加精度拆分增量）。辅助变量取 ±1 对应原问题两组解，属正常现象——**解码时必须先把解按参考自旋还原再读业务变量**。

**8-bit 的官方精确语义**：范围是有符号 [−128, 127]；**限制作用于最终 Ising 矩阵而非 QUBO 矩阵**；**整体同比例缩放后仍在范围内即合规**（(1280,1000) ≡ (128,100)）——这意味着"绝对值超界"和"相对分辨率不足"是两件事，精度适配的本质是**保相对差异**。

## 27.2 精度适配四法 API 级定级

| 方法 | 确切行为（文档原文级） | 保解性 | 使用建议 |
|---|---|---|---|
| `adjust_ising_matrix_precision` | 全局缩放+整数舍入 | **不保原最优** | 仅作 naive 基线对照 |
| `perform_precision_adaption_mutate(mat, iterations=100, heuristic='greedy', decision='heuristic')` | 迭代减小动态范围，每次改一个系数，**保持最优解不变**（思路引 Mücke et al. 2023）——但**不保证一定能降到目标精度** | **保最优（文档明示）** | 优先尝试！它是"optimum-preserving compression"的官方实现；配合枚举审计验证 |
| `perform_precision_adaption_split(mat, param_bit=8, min_increment=None, round_to_increment=True, method='var', penalty=None)` | 变量/项拆分；`min_increment` 默认=矩阵元素间最小正差值；`penalty` 默认=`min_increment×(2^(param_bit−1)−1)`；`round_to_increment` 保证拆分元素之和严格等于原值（7.5+7.5→7+8=15 而非 8+8=16） | 拆分一致时保等价 | `method='var'` 复制变量+罚约束；`method='item'` 不加罚项且返回索引可直接 `restore_split_solution`——**item 模式无罚项污染，优先考虑** |
| `PrecisionReducer(base_optimizer, precision=8)` | 装饰器：先适应性截断，不够再自动拆分；`only_feasible_solution=True` 只过滤**违反拆分一致性**的解 | 截断阶段可能失真——**截断丢失的信息不会因后续拆分恢复** | 作为端到端对照方案；`only_feasible_solution` **不验证业务 one-hot 约束，业务可行性必须独立重算** |

## 27.3 罚系数 get_min_penalty 的算法实质

官方算法（p43-44 原文级）：
- 目标函数中 x_i 从 0→1 的最大变化量上界：Δf < Σ_{q_ij>0} q_ij；从 1→0：Δf < Σ_{q_ij<0} q_ij；
- 估计罚项的最小非零变化量；
- **二者比值作为罚系数**——即"单变量翻转时目标变化恒小于罚项变化"的局部变化界。

```
用法：penalty = kw.core.get_min_penalty(obj, cons)
cons 传入的是罚项表达式本身（示例中为 (x0+x1+2x3-2)² + 2x2 整体）
```

**定级**：是合理的保守自动定标，但**不是精确全局临界值**；本题我们有更紧的解析推导（减最小值重参数化+1.1×max(W')，见第四轮审定版）——论文写法：**以解析推导为主，get_min_penalty 作为交叉验证**（两者对照一致是加分项）。

## 27.4 建模与验证 API（结果节验证工具）

```
qubo_model = kw.core.QuboModel()
qubo_model.set_objective(...)
qubo_model.add_constraint(expr, "name", penalty=λ)   # 约束式写法
unsat_cnt, res_dict = qubo_model.verify_constraint(sol_dict)  # 逐约束残差！
val = kw.core.get_val(qubo_model.objective, sol_dict)          # 业务目标值（不含罚项）
```

**`verify_constraint` 返回每个约束的残差字典——这正是"验证列内嵌结果表"的数据来源**：论文 Table 的 Feasible (y/n) 列应由它+业务重算双重生成。

官方 TSP 示例的诚实模式：SA 结果硬约束不为 0 时，**用禁忌搜索在邻域内修复**——若我们也做修复，论文必须分开报告修复前后（官方先例支持这种写法）。

## 27.5 真机使用规程（Optimization/Sampling 双模式）

```
from kaiwu.cim import CIMOptimizer, TaskMode
kw.common.CheckpointManager.save_dir = "/tmp"   # 检查点目录——证据链一部分

# Sampling 模式：sample_number 10-2000，探索解空间，随机性高
optimizer = CIMOptimizer(task_name="xxx", task_mode=TaskMode.SAMPLING, sample_number=100)

# Optimization 模式：动态策略调整演化次数，能量排序+聚类后处理，质量优先
optimizer = CIMOptimizer(task_name="xxx", task_mode=TaskMode.OPTIMIZATION)

solution = optimizer.solve(matrix)
```

**真机纪律清单：**
1. 提交前本地完成三层基准前两层（表示审计+匹配 SA），真机只跑冻结的 2-3 个方案；
2. Optimization 模式为主要求解证据，Sampling 模式可用于**能量分布/相位图**（探索解空间恰好是能量演化图的数据源）；
3. 控制台输出、task_name、Checkpoint 文件全部存档——论文真机证据图用原始截图+重绘双轨；
4. 68 元/次，未经用户批准不得提交。

## 27.6 HOBO 降阶 API 定级（P3 对照路线用）

```
hobo_model = kw.hobo.HoboModel(y3)
qubo_model = hobo_model.reduce()        # 自动引入积变量 _x2_x3 等 + Rosenberg 罚项
err_cnt, _ = hobo_model.verify_hobo_constraint(solution)  # 独立验证降阶一致性！
```

- Rosenberg 罚项：`p(x0,x1,y) = x0·x1 − 2x0·y − 2x1·y + 3y`，y≠x0x1 时 p>0；
- **k（罚系数）需自设**——降阶引入的额外能量尺度必须计入成本账本；
- `verify_hobo_constraint` 是"辅助一致性率"列的数据来源（与业务可行率分列！）；
- 实际生成多少辅助变量**以安装版输出为准**，不用手算 263/475 冒充。

## 27.7 排雷速查表（实施时逐条自查）

| 雷 | 拆法 |
|---|---|
| 能量数值漏加常数项 | 所有能量比较统一用完整哈密顿量重算 |
| 解码忘还原参考自旋 | 105/209 自旋先还原再读业务位；拆分解先 `restore_split_solution` |
| `only_feasible_solution` 当业务验证用 | 它只查拆分一致性；业务 one-hot 独立重算 |
| `mutate` 后默认精度达标 | 文档明说"不保证一定降低精度"——必须核验输出矩阵动态范围 |
| QUBO 矩阵直接当 8-bit 限制对象 | 限制作用于转换后的 Ising 矩阵 |
| 罚系数跨版本抄示例 | 1.2.0 是 `kw.qubo.get_min_penalty`，1.4.4 是 `kw.core.get_min_penalty` |
| 修复后结果冒充原始求解输出 | 修复前后分开报告（官方 TSP 示例同款诚实模式） |
| HOBO 辅助变量数手算冒充实测 | 以 `reduce()` 实际输出计数 |

## 27.8 论文方法节可用的 SDK 描述句式（英文）

> *"All QUBO models were constructed with the Kaiwu SDK (v1.4.4, Qboson). For deployment on the SPQC coherent Ising machine, whose coefficients are restricted to signed 8-bit integers [−128, 127], the quadratic forms were converted to Ising matrices via the standard spin transformation s = 2x − 1, introducing one auxiliary reference spin per matrix. Precision adaptation was performed using the optimum-preserving dynamic-range reduction (perform_precision_adaption_mutate, following Mücke et al.) and, where necessary, variable splitting with exact sum preservation. Constraint satisfaction was independently verified for every reported solution using both the SDK constraint evaluator and direct recomputation of the business constraints."*

配套边界句：*"The 8-bit restriction applies to the final Ising coefficients rather than the QUBO matrix; coefficient magnitudes are significant only up to uniform scaling, and the operative quantity is the preserved relative energy separation of feasible states."*
