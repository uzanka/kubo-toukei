#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reduced van der Waals isotherms, spinodal curve, and Boyle curve.

Requirements:
    pip install numpy matplotlib

Run:
    python van_der_waals_plot.py

Output:
    van_der_waals_plot_final.png
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


def configure_japanese_font() -> None:
    """Use an installed Japanese font if one is available."""
    candidates = [
        "Noto Sans CJK JP",
        "Noto Sans Japanese",
        "IPAexGothic",
        "IPAGothic",
        "Yu Gothic",
        "Meiryo",
        "Hiragino Sans",
        "TakaoGothic",
    ]

    installed = {font.name for font in font_manager.fontManager.ttflist}
    selected = next((name for name in candidates if name in installed), None)

    if selected:
        plt.rcParams["font.family"] = selected
    else:
        print(
            "Warning: Japanese font not found. "
            "Install Noto Sans CJK JP or IPAexGothic to display Japanese labels."
        )

    plt.rcParams["axes.unicode_minus"] = False


def reduced_pressure(v: np.ndarray, t: float) -> np.ndarray:
    """Reduced van der Waals isotherm."""
    return 8.0 * t / (3.0 * v - 1.0) - 3.0 / v**2


def spinodal_pressure(v: np.ndarray) -> np.ndarray:
    """Spinodal locus: (partial p / partial v)_t = 0."""
    return (3.0 * v - 2.0) / v**3


def boyle_pressure(v: np.ndarray) -> np.ndarray:
    """Boyle locus, excluding the endpoint v = 2/3."""
    return 3.0 * (3.0 * v - 2.0) / v**2


def main() -> None:
    configure_japanese_font()

    # Plot only in the physical volume domain v > 1/3.
    v = np.linspace(0.34, 3.0, 4000)

    # Split the Boyle curve around the excluded point (2/3, 0).
    v_endpoint = 2.0 / 3.0
    endpoint_gap = 0.003
    v_boyle_negative = np.linspace(0.34, v_endpoint - endpoint_gap, 650)
    v_boyle_positive = np.linspace(v_endpoint + endpoint_gap, 3.0, 2200)

    fig, ax = plt.subplots(figsize=(12, 7.2))

    # Reduced isotherms.
    for t in (0.6, 0.8, 1.0, 1.2):
        ax.plot(
            v,
            reduced_pressure(v, t),
            linewidth=2.1,
            label=rf"等温線 $\mathfrak{{t}}={t:.1f}$",
        )

    # Spinodal curve. The endpoint (2/3, 0) belongs to this curve.
    ax.plot(
        v,
        spinodal_pressure(v),
        linestyle="--",
        linewidth=2.4,
        label=(
            r"スピノーダル曲線："
            r"$(\partial\mathfrak{p}/\partial\mathfrak{v})_{\mathfrak{t}}=0$"
        ),
    )

    # Boyle curve. Both positive- and negative-pressure branches have
    # the same color and line style. The excluded endpoint is left open.
    boyle_negative_line, = ax.plot(
        v_boyle_negative,
        boyle_pressure(v_boyle_negative),
        linestyle=":",
        linewidth=3.0,
        label="Boyle曲線（正圧側・負圧側）",
    )
    boyle_color = boyle_negative_line.get_color()

    ax.plot(
        v_boyle_positive,
        boyle_pressure(v_boyle_positive),
        linestyle=":",
        linewidth=3.0,
        color=boyle_color,
    )

    # This point is excluded from the Boyle locus but lies on the spinodal.
    # A hollow marker allows the dashed spinodal line to remain visible.
    ax.plot(
        [v_endpoint],
        [0.0],
        marker="o",
        markersize=10,
        markerfacecolor="none",
        markeredgecolor="black",
        markeredgewidth=1.8,
        linestyle="None",
        zorder=8,
        label="Boyle条件からの除外点（スピノーダル上）",
    )

    # Critical point.
    ax.plot(
        [1.0],
        [1.0],
        marker="o",
        markersize=7,
        color="black",
        linestyle="None",
        zorder=9,
    )
    ax.annotate(
        "臨界点 (1, 1)",
        xy=(1.0, 1.0),
        xytext=(1.22, 1.35),
        arrowprops={"arrowstyle": "->"},
        fontsize=11,
    )

    # Axes and layout.
    ax.axhline(0.0, linewidth=0.9, color="black")
    ax.set_xlim(0.34, 3.0)
    ax.set_ylim(-1.25, 3.65)
    ax.set_xlabel(r"換算体積 $\mathfrak{v}=V/V_c$", fontsize=12)
    ax.set_ylabel(r"換算圧力 $\mathfrak{p}=p/p_c$", fontsize=12)
    ax.set_title("Reduced van der Waals 等温線と各軌跡", fontsize=15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=9, framealpha=0.96)

    ax.text(
        0.355,
        -1.12,
        "注：Boyle曲線・スピノーダル曲線の負圧側は表示下限より下にも続く",
        fontsize=9,
    )

    fig.tight_layout()

    output_path = Path(__file__).resolve().with_name(
        "1-R-8-figure-1.png"
    )
    fig.savefig(output_path, dpi=240, bbox_inches="tight")
    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    main()
