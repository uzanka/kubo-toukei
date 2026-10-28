#!/usr/bin/env python3
"""Plot Helmholtz free energy versus gas-phase particle number.

The curves illustrate the equilibrium condition for a solid in equilibrium
with its ideal-gas vapor.  The plotted free energies are scaled by kT:

    F_g/(kT) = N_g [ln(N_g / z_g) - 1]
    F_s/(kT) = -(N - N_g) ln(z_s)
    F/(kT)   = F_g/(kT) + F_s/(kT)

The model predicts the unconstrained stationary point N_g* = z_g / z_s.
If N >= N_g*, the minimum is at this interior point; if N < N_g*, the
minimum over 0 <= N_g <= N lies at the boundary N_g = N (all atoms in gas).

Dependencies: numpy, matplotlib

Run:
    python free_energy_phase_equilibrium.py
or customize the illustrative parameters:
    python free_energy_phase_equilibrium.py --n-star 40 --z-s 3 \
        --n-high 100 --n-low 20 --output free_energy.png
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


def set_font_for_japanese() -> bool:
    """Use an installed Japanese font when available; return success flag."""
    preferred = [
        "Noto Sans CJK JP",
        "Noto Serif CJK JP",
        "IPAexGothic",
        "IPAGothic",
        "Yu Gothic",
        "Meiryo",
        "Hiragino Sans",
    ]
    installed = {font.name for font in font_manager.fontManager.ttflist}
    for name in preferred:
        if name in installed:
            plt.rcParams["font.family"] = name
            break
    else:
        return False
    plt.rcParams["axes.unicode_minus"] = False
    return True


def free_energy_curves(ng: np.ndarray, n_total: float, z_g: float, z_s: float):
    """Return F_g/(kT), F_s/(kT), and total F/(kT) at each N_g."""
    # The limit N_g * ln(N_g / z_g) -> 0 as N_g -> 0 is used at N_g = 0.
    f_g = np.zeros_like(ng, dtype=float)
    positive = ng > 0
    f_g[positive] = ng[positive] * (np.log(ng[positive] / z_g) - 1.0)
    f_s = -(n_total - ng) * np.log(z_s)
    return f_g, f_s, f_g + f_s


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Plot free-energy curves for solid-vapor equilibrium."
    )
    parser.add_argument(
        "--n-star", type=float, default=40.0,
        help="equilibrium gas population N_g* = z_g/z_s (default: 40)",
    )
    parser.add_argument(
        "--z-s", type=float, default=3.0,
        help="single-atom solid partition function z_s (default: 3)",
    )
    parser.add_argument(
        "--n-high", type=float, default=100.0,
        help="total atom count for the coexistence case (must exceed N_g*)",
    )
    parser.add_argument(
        "--n-low", type=float, default=20.0,
        help="total atom count for the all-gas case (must be below N_g*)",
    )
    parser.add_argument(
        "--output", type=Path, default=Path("6-A-11-figure-1.png"),
        help="output image filename (default: 6-A-11-figure-1.png)",
    )
    parser.add_argument(
        "--show", action="store_true",
        help="open the figure window after saving (useful in an interactive desktop session)",
    )
    args = parser.parse_args()

    if args.n_star <= 0 or args.z_s <= 0:
        parser.error("--n-star and --z-s must be positive.")
    if not (args.n_high > args.n_star):
        parser.error("--n-high must be greater than --n-star.")
    if not (0 < args.n_low < args.n_star):
        parser.error("--n-low must be positive and less than --n-star.")

    n_star = args.n_star
    z_s = args.z_s
    # Choose z_g so that the stationary point is exactly z_g/z_s = N_g*.
    z_g = n_star * z_s

    japanese = set_font_for_japanese()
    if japanese:
        title = "固相・気相平衡における自由エネルギー"
        x_label = "気相の原子数 $N_g$"
        y_label = "自由エネルギー $F/(kT)$"
        component_title = "自由エネルギーの各成分"
        total_title = "全自由エネルギー $F=F_g+F_s$"
        labels = ("気相 $F_g/(kT)$", "固相 $F_s/(kT)$", "全自由エネルギー")
        high_note = f"内部極小点  $N_g^*={n_star:g}$\n固相・気相が共存"
        low_note = f"最小点は境界  $N_g=N={args.n_low:g}$\n全原子が気相に存在"
        threshold_note = f"閾値 $N_g^*=z_g/z_s={n_star:g}$"
        row_high = f"全原子数 $N={args.n_high:g}>N_g^*$"
        row_low = f"全原子数 $N={args.n_low:g}<N_g^*$"
    else:
        title = "Helmholtz Free Energy for Solid-Vapor Equilibrium"
        x_label = "Gas-phase atom count $N_g$"
        y_label = "Dimensionless free energy $F/(kT)$"
        component_title = "Free-energy components"
        total_title = "Total free energy $F=F_g+F_s$"
        labels = ("Gas phase $F_g/(kT)$", "Solid phase $F_s/(kT)$", "Total free energy")
        high_note = f"Interior minimum: $N_g^*={n_star:g}$\nSolid and vapor coexist"
        low_note = f"Minimum at boundary: $N_g=N={args.n_low:g}$\nAll atoms are in the gas"
        threshold_note = f"Threshold $N_g^*=z_g/z_s={n_star:g}$"
        row_high = f"Total atoms $N={args.n_high:g}>N_g^*$"
        row_low = f"Total atoms $N={args.n_low:g}<N_g^*$"

    fig, axes = plt.subplots(2, 2, figsize=(13.5, 9.0), constrained_layout=True)
    fig.suptitle(title, fontsize=16)

    scenarios = [
        (args.n_high, row_high, high_note, True),
        (args.n_low, row_low, low_note, False),
    ]

    for row, (n_total, row_title, note, has_interior_minimum) in enumerate(scenarios):
        ng = np.linspace(0.0, n_total, 800)
        f_g, f_s, f_total = free_energy_curves(ng, n_total, z_g, z_s)
        ax_components = axes[row, 0]
        ax_total = axes[row, 1]

        # Component diagram: the total free energy is the sum of these curves.
        ax_components.plot(ng, f_g, linestyle="--", linewidth=2, label=labels[0])
        ax_components.plot(ng, f_s, linestyle="-.", linewidth=2, label=labels[1])
        ax_components.set_title(f"{row_title}\n{component_title}")
        ax_components.set_xlabel(x_label)
        ax_components.set_ylabel(y_label)
        ax_components.set_xlim(0, n_total)
        ax_components.grid(True, alpha=0.25)
        ax_components.legend(loc="best")

        # Total free energy and its constrained minimum.
        ax_total.plot(ng, f_total, linewidth=2.5, label=labels[2])
        ax_total.set_title(f"{row_title}\n{total_title}")
        ax_total.set_xlabel(x_label)
        ax_total.set_ylabel(y_label)
        ax_total.set_xlim(0, n_total)
        ax_total.grid(True, alpha=0.25)

        if has_interior_minimum:
            ng_eq = n_star
            f_eq = free_energy_curves(np.array([ng_eq]), n_total, z_g, z_s)[2][0]
            ax_components.axvline(ng_eq, linestyle=":", linewidth=1.5)
            ax_total.axvline(ng_eq, linestyle=":", linewidth=1.5)
            ax_total.scatter([ng_eq], [f_eq], zorder=5)
            ax_total.annotate(
                note,
                xy=(ng_eq, f_eq),
                xytext=(14, 25),
                textcoords="offset points",
                arrowprops={"arrowstyle": "->"},
            )
        else:
            ng_eq = n_total
            f_eq = f_total[-1]
            ax_total.scatter([ng_eq], [f_eq], zorder=5)
            ax_total.annotate(
                note,
                xy=(ng_eq, f_eq),
                xytext=(-155, 30),
                textcoords="offset points",
                arrowprops={"arrowstyle": "->"},
            )

        ax_total.text(
            0.03, 0.04, threshold_note,
            transform=ax_total.transAxes,
            va="bottom",
            bbox={"boxstyle": "round,pad=0.3", "alpha": 0.12},
        )

    fig.savefig(args.output, dpi=200, bbox_inches="tight")
    print(f"Saved figure: {args.output.resolve()}")
    if args.show:
        plt.show()
    else:
        plt.close(fig)


if __name__ == "__main__":
    main()
