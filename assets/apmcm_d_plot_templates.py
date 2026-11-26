"""
APMCM D 题（量子优化 + 材料机器学习）出版级出图模板库
蒸馏自 2025D（Fig1/Fig6/Fig10/Fig11）、2025B（Fig2/Fig7）优秀论文与 playbook §13-15。
规范：英文-only、白底去顶/右框、300 dpi、字号>=8pt、灰度可辨、语义配色固定。
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LogNorm

# 全局出版级样式底座
def apply_apmcm_style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    })

PALETTE = {
    "classical": "#3b6fa0",   # 深海蓝：经典/基线
    "quantum":   "#d9822b",   # 暖橙：量子/启发式
    "feasible":  "#1b8a6b",   # 青绿：可行/裕度/收益
    "violation": "#d62728",   # 红：约束上限/违约/最优点
    "neutral":   "#6c757d",   # 灰：参照/基线
}


def plot_tri_panel_precision(bit_widths, dyn_ranges_naive, dyn_ranges_reduced,
                             hit_rates_naive, hit_rates_reduced, hit_rates_tight_lam,
                             strat_names, strat_costs, strat_feas,
                             out_path="fig_precision_tri_panel.png"):
    """
    复刻 2025D Fig10 三联诊断图（适用于 2026D 精度-位宽实证）：
      Panel (a): 位宽 vs 矩阵动态范围对比（Naive vs PrecisionReducer）
      Panel (b): 位宽 vs Top-k 命中保持率（硬件可行性衰减曲线 + 8-bit 竖虚线）
      Panel (c): 精度适配策略对比柱状图（含可行性标签）
    """
    apply_apmcm_style()
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.3))
    plt.subplots_adjust(wspace=0.32)

    # (a) Dynamic range / scale compression
    ax = axes[0]
    ax.plot(bit_widths, dyn_ranges_naive, "o-", color=PALETTE["violation"], lw=1.6, ms=4, label="Naive truncation")
    ax.plot(bit_widths, dyn_ranges_reduced, "s--", color=PALETTE["classical"], lw=1.6, ms=4, label="PrecisionReducer")
    ax.axvline(8, color=PALETTE["neutral"], ls=":", lw=1.2)
    ax.text(8.2, max(dyn_ranges_naive)*0.85, "8-bit limit", fontsize=8, color=PALETTE["neutral"])
    ax.set_xlabel("Coefficient Bit Width (bits)")
    ax.set_ylabel("Max |h| / Min Coupling")
    ax.set_title("(a) Dynamic Range Compression")
    ax.set_yscale("log")
    ax.legend(frameon=False, loc="upper right")

    # (b) Hardware feasibility / hit retention curve
    ax = axes[1]
    ax.plot(bit_widths, hit_rates_naive, "o-", color=PALETTE["violation"], lw=1.6, ms=4, label="Naive (loose λ)")
    ax.plot(bit_widths, hit_rates_tight_lam, "^-.", color=PALETTE["quantum"], lw=1.6, ms=4, label="Tightened λ")
    ax.plot(bit_widths, hit_rates_reduced, "s-", color=PALETTE["feasible"], lw=1.8, ms=4, label="PrecisionReducer")
    ax.axvline(8, color=PALETTE["violation"], ls="--", lw=1.2)
    ax.axvspan(min(bit_widths), 8, color=PALETTE["violation"], alpha=0.07)
    ax.text(8.2, 15, "SPQC 8-bit\nhardware cap", fontsize=7.5, color=PALETTE["violation"])
    ax.set_xlabel("Coefficient Bit Width (bits)")
    ax.set_ylabel("Top-k Hit Retention (%)")
    ax.set_ylim(0, 108)
    ax.set_title("(b) Hardware Precision Feasibility")
    ax.legend(frameon=False, loc="lower right")

    # (c) Strategy impact bars
    ax = axes[2]
    colors = [PALETTE["feasible"] if f else PALETTE["neutral"] for f in strat_feas]
    bars = ax.bar(strat_names, strat_costs, color=colors, width=0.55, edgecolor="black", lw=0.6)
    for b, f in zip(bars, strat_feas):
        h = b.get_height()
        tag = f"{h:.1f}%\n({'OK' if f else 'Fail'})"
        ax.text(b.get_x() + b.get_width()/2, h + 1.5, tag, ha="center", va="bottom", fontsize=7.5)
    ax.set_ylabel("Feasible Solution Rate (%)")
    ax.set_ylim(0, max(strat_costs) * 1.22)
    ax.set_title("(c) Adaptation Strategy Comparison")
    ax.tick_params(axis="x", rotation=15)

    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def plot_pareto_bubble_ledger(costs, scores, bit_widths, weights, labels, regions,
                              out_path="fig_pareto_cost_ledger.png"):
    """
    复刻 2025B Fig7 四维气泡 Pareto 成本账本图：
      x=时间/能耗成本, y=命中质量/富集度, 气泡大小=Qubit位宽, 颜色=策略权重
      含红色虚线前沿 + 黄色圆角高亮工作区标签框
    regions: list of (x, y, text)
    """
    apply_apmcm_style()
    fig, ax = plt.subplots(figsize=(6.2, 4.4))

    sizes = np.array(bit_widths) * 1.8
    sc = ax.scatter(costs, scores, s=sizes, c=weights, cmap="viridis",
                    edgecolors="black", linewidths=0.8, alpha=0.9, zorder=3)
    # Pareto front dashed line (sorted by cost)
    idx = np.argsort(costs)
    ax.plot(np.array(costs)[idx], np.array(scores)[idx], "--", color=PALETTE["violation"],
            lw=1.3, alpha=0.85, zorder=2, label="Pareto Frontier")

    for x, y, lbl in zip(costs, scores, labels):
        ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(0, -13),
                    ha="center", fontsize=7.5, color="#222222")

    for rx, ry, rtxt in regions:
        ax.text(rx, ry, rtxt, fontsize=8, fontweight="bold", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff3b0", edgecolor="#b08900", lw=0.9),
                zorder=4)

    cbar = fig.colorbar(sc, ax=ax, pad=0.02)
    cbar.set_label("Penalty / Precision Weight", fontsize=8.5)
    ax.set_xlabel("Computational Cost (Runtime s / Normalized Energy)")
    ax.set_ylabel("Screening Quality Score (%)")
    ax.set_title("Cost–Quality Pareto Trade-off Across QUBO Solvers")
    ax.grid(True, linestyle=":", alpha=0.35)
    ax.legend(frameon=False, loc="lower right")

    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def plot_heatmap_with_band_and_opt(grid_z, x_vals, y_vals, opt_xy, band_x_range=None,
                                   xlabel="Penalty Weight λ", ylabel="Bit Width",
                                   cbar_label="Feasible Hit Rate (%)",
                                   title="Parameter Landscape with Optimal Point",
                                   out_path="fig_param_heatmap.png"):
    """
    复刻 2025B Fig2 二维参数热图：
      plasma 色标 + 半透明物理/硬件有效区间带 + 大红点+白框钉死最优解坐标
    """
    apply_apmcm_style()
    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    im = ax.imshow(grid_z, origin="lower", aspect="auto", cmap="plasma",
                   extent=[x_vals[0], x_vals[-1], y_vals[0], y_vals[-1]])
    if band_x_range is not None:
        ax.axvspan(band_x_range[0], band_x_range[1], color="white", alpha=0.22,
                   label="Target Feasible Window")
    ox, oy = opt_xy
    ax.scatter([ox], [oy], color=PALETTE["violation"], s=75, edgecolors="white", linewidths=1.2, zorder=5)
    ax.annotate(f"Optimal: ({ox:.1f}, {oy:.1f})", (ox, oy),
                textcoords="offset points", xytext=(10, -14), fontsize=8, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="black", lw=0.8),
                arrowprops=dict(arrowstyle="->", color="white", lw=1.0), zorder=6)

    cbar = fig.colorbar(im, ax=ax, pad=0.02)
    cbar.set_label(cbar_label, fontsize=8.5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if band_x_range is not None:
        ax.legend(frameon=False, loc="upper left")

    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def plot_enrichment_bar(methods, ef_vals, p_vals, baseline_ef=1.0,
                        out_path="fig_enrichment_stats.png"):
    """
    2026D 专属：小样本富集度统计图（含随机基线横虚线 + 单侧超几何 p 值直印）
    """
    apply_apmcm_style()
    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    colors = [PALETTE["neutral"] if m.lower().startswith("random") or m.lower().startswith("rule")
              else PALETTE["classical"] for m in methods]
    bars = ax.bar(methods, ef_vals, color=colors, width=0.52, edgecolor="black", lw=0.6)
    ax.axhline(baseline_ef, color=PALETTE["violation"], ls="--", lw=1.1, label="Uniform Random (EF = 1.0x)")
    for b, ef, p in zip(bars, ef_vals, p_vals):
        lbl = f"{ef:.1f}x\n(p={p:.2e})" if p is not None else f"{ef:.1f}x"
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + max(ef_vals)*0.02,
                lbl, ha="center", va="bottom", fontsize=7.5)
    ax.set_ylabel("Enrichment Factor (EF@20)")
    ax.set_ylim(0, max(ef_vals) * 1.24)
    ax.set_title("Top-20 Screening Enrichment Over Finite Holdout Pool")
    ax.legend(frameon=False, loc="upper left")
    ax.tick_params(axis="x", rotation=12)

    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def plot_dashboard_2x2(x_idx, target_vals, solver_vals, margin_vals,
                       bar_labels, bar_rates, cap_limit,
                       series_c_x, series_c_y,
                       step_x, step_violations,
                       out_path="fig_dashboard_2x2.png"):
    """
    复刻 2025D Fig6 2x2 约束验证仪表盘：
      (a) 目标 vs 实际 + 半透明裕度填充带
      (b) 约束/容量利用率柱图 + 顶部红色水平上限虚线
      (c) 关键稳定性指标折线
      (d) 约束违规次数阶梯图
    """
    apply_apmcm_style()
    fig, axes = plt.subplots(2, 2, figsize=(8.8, 5.6))
    plt.subplots_adjust(hspace=0.36, wspace=0.28)

    # (a) Target vs Solver + margin band
    ax = axes[0, 0]
    ax.plot(x_idx, target_vals, "-", color=PALETTE["classical"], lw=1.5, label="Reference / Target")
    ax.plot(x_idx, solver_vals, "--", color=PALETTE["quantum"], lw=1.5, label="QUBO Solver")
    ax.fill_between(x_idx, np.array(solver_vals) - np.array(margin_vals),
                    np.array(solver_vals) + np.array(margin_vals),
                    color=PALETTE["quantum"], alpha=0.18, label="Sampling Band")
    ax.set_title("(a) Objective Tracking & Stability Band")
    ax.set_xlabel("Candidate / Run Index")
    ax.set_ylabel("Objective Score")
    ax.legend(frameon=False, loc="upper right", fontsize=7.5)

    # (b) Capacity / Bit-budget loading bars + red cap line
    ax = axes[0, 1]
    ax.bar(bar_labels, bar_rates, color="#7b5ea7", width=0.55, alpha=0.88)
    ax.axhline(cap_limit, color=PALETTE["violation"], ls="--", lw=1.3, label=f"Limit ({cap_limit}%)")
    ax.set_title("(b) Hardware / Constraint Utilization")
    ax.set_ylabel("Utilization (%)")
    ax.set_ylim(0, max(max(bar_rates), cap_limit) * 1.18)
    ax.legend(frameon=False, loc="upper right", fontsize=7.5)
    ax.tick_params(axis="x", rotation=12)

    # (c) Stability metric curve
    ax = axes[1, 0]
    ax.plot(series_c_x, series_c_y, "o-", color=PALETTE["feasible"], lw=1.4, ms=3.5)
    ax.set_title("(c) Feasible Rate Across Penalty λ")
    ax.set_xlabel("Penalty Weight λ")
    ax.set_ylabel("Feasible Rate (%)")
    ax.set_ylim(0, 108)

    # (d) Violation step chart
    ax = axes[1, 1]
    ax.step(step_x, step_violations, where="mid", color="#222222", lw=1.4)
    ax.plot(step_x, step_violations, "o", color="#222222", ms=3)
    ax.set_title("(d) Constraint Violations per Sample")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Violation Count")
    ax.set_ylim(-0.2, max(step_violations) + 0.8)

    fig.savefig(out_path)
    plt.close(fig)
    return out_path
