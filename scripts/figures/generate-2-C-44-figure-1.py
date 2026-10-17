#!/usr/bin/env python3
"""Plot Joule-Thomson inversion curves for Dieterici and van der Waals gases.

The axes use reduced (critical-point-normalized) variables:
    t = T / T_c
    p = P / P_c

Run:
    python jt_inversion_curves.py

Dependencies:
    numpy
    matplotlib
"""

import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def dieterici_pressure(t: np.ndarray) -> np.ndarray:
    """Reduced inversion pressure for the Dieterici gas.

    p = (8 - t) * exp(5/2 - 4/t), valid for 0 < t < 8.
    """
    return (8.0 - t) * np.exp(2.5 - 4.0 / t)


def van_der_waals_pressure(t: np.ndarray) -> np.ndarray:
    """Reduced inversion pressure for the van der Waals gas.

    p = 24*sqrt(3*t) - 12*t - 27.
    The physical positive-pressure branch is 3/4 <= t <= 27/4.
    """
    return 24.0 * np.sqrt(3.0 * t) - 12.0 * t - 27.0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--show", action="store_true",
        help="also display the plot in an interactive window",
    )
    args = parser.parse_args()

    # Dieterici branch: p >= 0 for 0 < t < 8.
    t_dieterici = np.linspace(0.01, 8.0, 2000, endpoint=False)
    p_dieterici = dieterici_pressure(t_dieterici)

    # van der Waals branch: p >= 0 for 3/4 <= t <= 27/4.
    t_vdw = np.linspace(0.75, 6.75, 1200)
    p_vdw = van_der_waals_pressure(t_vdw)

    fig, ax = plt.subplots(figsize=(8.2, 5.4), constrained_layout=True)

    ax.plot(
        t_dieterici,
        p_dieterici,
        linewidth=2.2,
        label=r"Dieterici: $p=(8-t)e^{5/2-4/t}$",
    )
    ax.plot(
        t_vdw,
        p_vdw,
        linewidth=2.2,
        label=r"van der Waals: $p=24\sqrt{3t}-12t-27$",
    )

    # Mark each curve's maximum, derived from the analytic expressions.
    t_d_max = 4.0
    p_d_max = 4.0 * np.exp(1.5)
    t_vdw_max = 3.0
    p_vdw_max = 9.0
    ax.plot(t_d_max, p_d_max, marker="o", linestyle="none")
    ax.annotate(
        rf"max $({t_d_max:g},\ {p_d_max:.2f})$",
        (t_d_max, p_d_max),
        xytext=(10, -20),
        textcoords="offset points",
        fontsize=9,
    )
    ax.plot(t_vdw_max, p_vdw_max, marker="o", linestyle="none")
    ax.annotate(
        rf"max $({t_vdw_max:g},\ {p_vdw_max:g})$",
        (t_vdw_max, p_vdw_max),
        xytext=(10, 8),
        textcoords="offset points",
        fontsize=9,
    )

    ax.set_xlabel(r"Reduced temperature $t=T/T_c$", fontsize=12)
    ax.set_ylabel(r"Reduced pressure $p=P/P_c$", fontsize=12)
    ax.set_title("Joule-Thomson inversion curves", fontsize=13)
    ax.set_xlim(0.0, 8.0)
    ax.set_ylim(0.0, 20.0)
    ax.set_xticks(np.arange(0.0, 8.1, 1.0))
    ax.set_yticks(np.arange(0.0, 20.1, 2.0))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", frameon=True, fontsize=9)

    # Save the figure in the same directory as this script.
    output_path = Path(__file__).resolve().with_name("jt_inversion_curves.png")
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    print(f"Saved figure to: {output_path}")

    if args.show:
        plt.show()
    else:
        plt.close(fig)


if __name__ == "__main__":
    main()
