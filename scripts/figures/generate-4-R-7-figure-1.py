#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正則二元溶液の図を描くスクリプト
  1) 蒸気圧 p1, p2 と組成 x1
  2) 混合ギブズエネルギー g_mix/(RT) と組成 x1（複数温度）
  3) 相図（ビノーダル・スピノーダル）

モデル:
  p1 = x1 p1° exp[A(1-x1)^2/(RT)]
  p2 = (1-x1) p2° exp[A x1^2/(RT)]
  g_mix/(RT) = (A/RT)x1(1-x1) + x1 ln(x1) + (1-x1)ln(1-x1)

ここでは無次元パラメータ a=A/R として温度 T と比較し、
臨界温度 Tc = A/(2R) = a/2 を用いる。
デフォルトは a=600 K, Tc=300 K。
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- 設定（必要に応じて変更） ----------
A_over_R = 600.0       # A/R [K]（A > 0 なら相分離型）
p1_star = 1.0           # 純成分1の飽和蒸気圧（規格化値）
p2_star = 1.0           # 純成分2の飽和蒸気圧（規格化値）
temperatures = [250.0, 300.0, 400.0]  # [K]
save_dpi = 200
output_file = "regular_binary_solution.png"

# x=0,1 では x ln x の極限を数値的に扱うため、端点を少し避ける
x = np.linspace(1e-5, 1.0 - 1e-5, 1200)
Tc = A_over_R / 2.0

def g_mix_over_RT(x, T):
    """混合ギブズエネルギー g_mix/(RT)"""
    a = A_over_R / T
    return a * x * (1.0 - x) + x * np.log(x) + (1.0 - x) * np.log(1.0 - x)

def spinodal_compositions(T):
    """スピノーダル組成。Tcより低温でのみ実数解が存在する。"""
    q = 2.0 * T / A_over_R  # RT/A
    if q >= 0.5:
        return None
    delta = np.sqrt(1.0 - 2.0 * q)
    return (1.0 - delta) / 2.0, (1.0 + delta) / 2.0

def binodal_y(T):
    """
    ビノーダルの対称な共存組成を y で計算:
      atanh(y) = A y/(2RT), 0 < y < 1
    T<Tc のとき非零解を二分法で求める。
    """
    if T >= Tc:
        return None
    def f(y):
        return np.arctanh(y) - A_over_R * y / (2.0 * T)
    lo, hi = 1e-10, 1.0 - 1e-10
    # f(lo)<0, f(hi)>0 for T<Tc
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

# Figure 1: vapor pressure curves
fig, ax = plt.subplots(figsize=(8, 5.5))
for T in temperatures:
    a = A_over_R / T
    p1 = x * p1_star * np.exp(a * (1.0 - x)**2)
    p2 = (1.0 - x) * p2_star * np.exp(a * x**2)
    ax.plot(x, p1, label=fr"$p_1$ at $T={T:g}$ K")
    ax.plot(x, p2, linestyle="--", label=fr"$p_2$ at $T={T:g}$ K")
ax.set_xlabel(r"Mole fraction $x_1$")
ax.set_ylabel("Vapor pressure (normalized)")
ax.set_title("Vapor pressures of a regular binary solution")
ax.set_xlim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8, ncol=2)
fig.tight_layout()
fig.savefig("vapor_pressure.png", dpi=save_dpi)

# Figure 2: dimensionless mixing Gibbs energy
fig, ax = plt.subplots(figsize=(8, 5.5))
for T in temperatures:
    ax.plot(x, g_mix_over_RT(x, T), label=fr"$T={T:g}$ K")
ax.axvline(0.5, color="gray", linewidth=0.8, linestyle=":")
ax.set_xlabel(r"Mole fraction $x_1$")
ax.set_ylabel(r"$\Delta g_{\mathrm{mix}}/(RT)$")
ax.set_title("Mixing Gibbs energy")
ax.set_xlim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig("mixing_gibbs_energy.png", dpi=save_dpi)

# Figure 3: phase diagram, binodal and spinodal
fig, ax = plt.subplots(figsize=(7.5, 5.5))
T_values = np.linspace(0.5, Tc, 500)
x_bin_left, x_bin_right = [], []
for T in T_values:
    y = binodal_y(T)
    if y is not None:
        x_bin_left.append((1.0 - y) / 2.0)
        x_bin_right.append((1.0 + y) / 2.0)
    else:
        x_bin_left.append(0.5)
        x_bin_right.append(0.5)

ax.plot(x_bin_left, T_values, label="Binodal (coexistence)", linewidth=2)
ax.plot(x_bin_right, T_values, linewidth=2)

T_spin = np.linspace(0.5, Tc * (1 - 1e-6), 500)
x_spin_left, x_spin_right = [], []
for T in T_spin:
    pair = spinodal_compositions(T)
    if pair is not None:
        x_spin_left.append(pair[0])
        x_spin_right.append(pair[1])
    else:
        x_spin_left.append(0.5)
        x_spin_right.append(0.5)

ax.plot(x_spin_left, T_spin, linestyle="--", label="Spinodal (local instability)")
ax.plot(x_spin_right, T_spin, linestyle="--")
ax.scatter([0.5], [Tc], zorder=5, label=fr"Critical point ($T_c={Tc:g}$ K)")
ax.set_xlabel(r"Mole fraction $x_1$")
ax.set_ylabel("Temperature [K]")
ax.set_title("Temperature–composition phase diagram")
ax.set_xlim(0, 1)
ax.set_ylim(0, Tc * 1.08)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("4-R-7-figure-1.png", dpi=save_dpi)

print("Saved figures: vapor_pressure.png, mixing_gibbs_energy.png, phase_diagram.png")
print(f"Critical temperature Tc = {Tc:g} K")
plt.show()
