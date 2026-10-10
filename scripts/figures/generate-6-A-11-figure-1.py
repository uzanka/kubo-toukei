"""
演習問題 6-A-11 の解答図: Helmholtz自由エネルギー F を N_g の関数として図示する.

F_g(N_g) = -kT * N_g * (log(z_g) - log(N_g) + 1)  : 気相の自由エネルギー
F_s(N_g) = -kT * (N - N_g) * log(z_s)              : 固相の自由エネルギー
F(N_g)   = F_g(N_g) + F_s(N_g)                     : 全系の自由エネルギー
"""

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# ---- パラメータ（適当な単位で設定） ---
kT = 1.0       # kT = 1 (適当な単位)
z_g = 100.0    # 気体分子の分配関数
z_s = 10.0     # 固体の単一サイト分配関数
N = 30         # 総原子数

# N_g の範囲: 0 < N_g <= N
N_g = np.linspace(0.1, N, 500)

# F_g(N_g) = -kT * N_g * (log(z_g) - log(N_g) + 1)
F_g = -kT * N_g * (np.log(z_g) - np.log(N_g) + 1)

# F_s(N_g) = -kT * (N - N_g) * log(z_s)
F_s = -kT * (N - N_g) * np.log(z_s)

# F(N_g) = F_g + F_s
F = F_g + F_s

# 平衡点: N_g = z_g / z_s
N_g_eq = z_g / z_s

# ---- 描画 ---
FONT_SIZE = 14
LINE_WIDTH = 2.5
TICK_LABEL_SIZE = 12
LEGEND_FONT = 11

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('#fafafa')

# F_g: 気相の自由エネルギー
ax.plot(N_g, F_g, color='#2196F3', lw=LINE_WIDTH, label=r'$F_g$ (gas)')

# F_s: 固相の自由エネルギー
ax.plot(N_g, F_s, color='#FF9800', lw=LINE_WIDTH, ls='--', label=r'$F_s$ (solid)')

# F: 全系の自由エネルギー
ax.plot(N_g, F, color='#4CAF50', lw=LINE_WIDTH, label=r'$F=F_g+F_s$')

# 極小点を示す垂直破線
ax.axvline(x=N_g_eq, color='#E91E63', ls='-.', lw=1.5, alpha=0.8)

# 極小点にマーカー
F_eq_idx = np.argmin(np.abs(N_g - N_g_eq))
F_eq_val = F[F_eq_idx]
ax.plot(N_g[F_eq_idx], F_eq_val, 'D', color='#E91E63', markersize=10, alpha=0.8)

# ---- 軸ラベル・タイトル ---
ax.set_xlabel(r'$N_g$', fontsize=FONT_SIZE)
ax.set_ylabel(r'$F/kT$', fontsize=FONT_SIZE)
ax.set_title('Fig.6-A-11: Helmholtz free energy vs. gas atom number', fontsize=14, fontweight='bold')

# ---- 凡例 ---
ax.legend(loc='upper right', fontsize=LEGEND_FONT, frameon=True, facecolor='white')

# ---- グリッド ---
ax.grid(True, alpha=0.3)

# ---- 注釈 ---
ax.annotate(r'equilibrium: $N_g=z_g/z_s$',
            xy=(N_g_eq, F_eq_val),
            xytext=(N_g_eq + 4, F_eq_val + 5),
            fontsize=TICK_LABEL_SIZE,
            color='#E91E63',
            arrowprops=dict(arrowstyle='->', color='#E91E63', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='#E91E63'))

# 軸の設定
ax.set_xlim(0, N + 1)
ax.tick_params(labelsize=TICK_LABEL_SIZE)

# ---- 保存 ---
save_path = '../../6/6-A-11-figure-1.png'
fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)

print(f"Figure saved to {save_path}")
