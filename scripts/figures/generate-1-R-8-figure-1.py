#!/usr/bin/env python3
"""
Plot reduced van der Waals isotherms, the spinodal locus, and the Boyle locus.

Reduced van der Waals equation:
    p_r = 8 T_r / (3 V_r - 1) - 3 / V_r**2

The strict Boyle-locus condition is:
    (d(p_r * V_r) / d p_r)_(T_r) = 0

The parametrized Boyle curve has a singular point at V_r = 2/3,
T_r = 27/32, p_r = 0. This point is omitted from the plotted strict
locus because d p_r / d V_r = 0 there, so the derivative with respect
to p_r is not defined by the chain-rule ratio at that point.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def reduced_pressure(v: np.ndarray, t: float) -> np.ndarray:
    """Reduced pressure from the reduced van der Waals equation."""
    return 8.0 * t / (3.0 * v - 1.0) - 3.0 / v**2


def main() -> None:
    # Physical domain for the van der Waals equation is v > 1/3.
    v_min = 1.0 / 3.0 + 0.006
    v_max = 3.0
    v = np.linspace(v_min, v_max, 1600)
    temperatures = [0.6, 0.8, 1.0, 1.2]

    fig, ax = plt.subplots(figsize=(10, 6.5))

    # Isotherms.
    for t in temperatures:
        p = reduced_pressure(v, t)
        ax.plot(v, p, linewidth=2, label=fr"Isotherm $T_r={t}$")

    # Spinodal: (partial p_r / partial v_r)_T_r = 0.
    # t = (3v - 1)^2 / (4v^3), p = (3v - 2) / v^3.
    vs = np.linspace(v_min, v_max, 1200)
    p_spinodal = (3.0 * vs - 2.0) / vs**3
    ax.plot(
        vs,
        p_spinodal,
        linestyle="--",
        linewidth=2,
        label=r"Spinodal: $(\partial p_r/\partial v_r)_{T_r}=0$",
    )

    # Boyle locus: p_r = 3(3v_r - 2)/v_r^2.
    # Exclude a small interval around v_r = 2/3, where the original
    # derivative w.r.t. p_r is not defined (both chain-rule numerator
    # and denominator vanish).
    v_boyle_left = np.linspace(v_min, 2.0 / 3.0 - 0.008, 450)
    v_boyle_right = np.linspace(2.0 / 3.0 + 0.008, v_max, 850)

    for i, vb in enumerate((v_boyle_left, v_boyle_right)):
        p_boyle = 3.0 * (3.0 * vb - 2.0) / vb**2
        ax.plot(
            vb,
            p_boyle,
            linestyle=":",
            linewidth=2.5,
            label="Boyle locus" if i == 0 else "_nolegend_",
        )

    # Critical point.
    ax.scatter([1.0], [1.0], zorder=5)
    ax.annotate(
        "Critical point (1, 1)",
        xy=(1.0, 1.0),
        xytext=(1.18, 1.25),
        arrowprops={"arrowstyle": "->", "linewidth": 1.2},
    )

    ax.axhline(0.0, linewidth=0.8)
    ax.set_xlim(0.33, 3.0)
    ax.set_ylim(-0.8, 3.2)
    ax.set_xlabel(r"Reduced volume $\mathfrak{v}=V/V_c$")
    ax.set_ylabel(r"Reduced pressure $\mathfrak{p}=p/p_c$")
    ax.set_title("Reduced van der Waals Isotherms and Loci")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=9)
    fig.tight_layout()

    # Save beside this script. If run interactively, fall back to cwd.
    output_path = Path(__file__).resolve().with_name(
        "vdw_reduced_isotherms_loci.png"
    )
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    print(f"Saved graph to: {output_path}")
    plt.show()


if __name__ == "__main__":
    main()
