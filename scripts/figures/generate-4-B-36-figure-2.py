"""
演習問題 4-B-36 の解答用図 2: 比熱 Cs と Cn の温度依存性

(iii) で導かれた関係から、超伝導状態の比熱 Cs と正常状態の比熱 Cn の
温度依存性を描画する。

key relations:
- H_c(T) = H_0 {1 - (T/T_0)^2}
- Cs - Cn = -(V*H_0^2 / 2pi*T_0^2) * {1 - 3(T/T_0)^2}  [from derivation]
  Actually: Cn - Cs = (V*H_0^2 / 2pi*T_0^2) * T * {1 - 3(T/T_0)^2}

For visualization, we use dimensionless form:
- Cn*/Cn(T0) vs T/T0
- Cs*/Cn(T0) vs T/T0
"""

import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'BIZ UDPGothic'
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['axes.linewidth'] = 1.2
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['axes.axisbelow'] = True

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# T/T_0 の範囲 (0 から T_0 まで)
T_norm = np.linspace(0.01, 1.0, 500)

# 比熱のモデル化
# Cn = gamma * T (電子比熱、線形依存)
# Cs = Cn + A * {1 - 3(T/T_0)^2} (A は定数)

# 規格化: C* = C / (gamma * T_0)
# Cn* = T/T_0
Cn_star = T_norm

# Cs - Cn の温度依存性 (式(7)より)
# Cn - Cs = (Vbar * H_0^2 / 2pi * T_0^2) * T * {1 - 3(T/T_0)^2}
# 定数 kappa を導入して規格化:
kappa = 0.5  # 比熱ジャンプの大きさを決めるパラメータ
delta_C_star = kappa * T_norm * (1.0 - 3.0 * T_norm**2)

# Cs = Cn - delta_C
Cs_star = Cn_star - delta_C_star

fig, ax = plt.subplots(figsize=(8, 6))

# Cn と Cs を描画
ax.plot(T_norm, Cn_star, 'r-', linewidth=2.5, label=r'$C_n / (\gamma T_0)$ (正常状態)')
ax.plot(T_norm, Cs_star, 'b-', linewidth=2.5, label=r'$C_s / (\gamma T_0)$ (超伝導状態)')

# T = 1/sqrt(3) に垂直線 (Cs = Cn となる点)
T_cross = 1.0 / np.sqrt(3)
ax.axvline(x=T_cross, linestyle='--', color='gray', alpha=0.7)
ax.text(T_cross, 0.02, r'$1/\sqrt{3}$', ha='center', va='bottom', fontsize=11, style='italic')

# T = T_0 に垂直線
ax.axvline(x=1.0, linestyle='--', color='gray', alpha=0.7)
ax.text(1.0, 0.02, r'$T_0$', ha='center', va='bottom', fontsize=11, style='italic')

# 両者の差を塗りつぶす
ax.fill_between(T_norm, Cn_star, Cs_star, where=(Cs_star < Cn_star), alpha=0.3, color='blue', label=r'$C_n - C_s > 0$ ($T < T_0/\sqrt{3}$)')
ax.fill_between(T_norm, Cn_star, Cs_star, where=(Cs_star > Cn_star), alpha=0.3, color='red', label=r'$C_n - C_s < 0$ ($T > T_0/\sqrt{3}$)')

# アノトロピー点にマーク
ax.plot(T_cross, Cn_star[int(T_cross * len(T_norm))], 'go', markersize=10, markeredgewidth=2, markeredgecolor='k')

# 軸ラベル
ax.set_xlabel(r'温度 $T / T_0$', fontsize=16)
ax.set_ylabel(r'規格化比熱 $C / (\gamma T_0)$', fontsize=16)

# 凡例
ax.legend(loc='upper left', fontsize=12)

# グリッド
ax.grid(True, alpha=0.3)

# タイトル
ax.set_title(r'Specific heat vs temperature for superconducting transition', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('../../4/4-B-36-figure-2.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 2 saved: 4-B-36-figure-2.png")
