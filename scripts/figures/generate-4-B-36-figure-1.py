"""
演習問題 4-B-36 の解答用図 1: Hc-T 相図の作成

問題文に示される限界磁場 H_c(T) と温度 T の関係を描画する。
- 横軸: 温度 T (規格化値 T/T_0)
- 縦軸: 限界磁場 H_c (規格化値 H_c/H_0)
- H_c(T) = H_0 {1 - (T/T_0)^2} に従う曲線を描く
- 超伝導状態 (s) と正常状態 (n) の領域を区別して塗り分ける
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

# T/T_0 の範囲を定義 (0 から 1.15 まで)
T_norm = np.linspace(0, 1.15, 500)

# H_c/H_0 = 1 - (T/T_0)^2 (ただし H_c >= 0)
H_norm = np.where(T_norm <= 1.0, 1.0 - T_norm**2, 0.0)

fig, ax = plt.subplots(figsize=(8, 6))

# 超伝導状態の領域を薄い色で塗りつぶす
ax.fill_between(T_norm, 0, H_norm, where=(T_norm <= 1.0), alpha=0.3, color='skyblue', label='s (超伝導状態)')

# 正常状態の領域を別の色で塗りつぶす
ax.fill_between(T_norm, 0, H_norm * 2, where=(T_norm > 1.0), alpha=0.3, color='lightcoral', label='n (正常状態)')

# 境界線を描画
ax.plot(T_norm[H_norm > 0], H_norm[H_norm > 0], 'b-', linewidth=2.5, label='$H_c(T)$')

# 重要な点をマーク
ax.plot(0, 1, 'ko', markersize=8)
ax.text(-0.03, 1.02, r'$(0,\;H_0)$', ha='right', va='bottom', fontsize=12)

ax.plot(1, 0, 'ko', markersize=8)
ax.text(1.03, -0.05, r'$(T_0,\;0)$', ha='left', va='top', fontsize=12)

# T_0 に垂直点線
ax.axvline(x=1, linestyle='--', color='gray', alpha=0.7)

# 軸ラベルとタイトル
ax.set_xlabel(r'温度 $T / T_0$', fontsize=16)
ax.set_ylabel(r'限界磁場 $H_c / H_0$', fontsize=16)

# 軸の範囲設定
ax.set_xlim(-0.05, 1.15)
ax.set_ylim(-0.08, 1.15)

# グリッドと凡例
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=12)

# T/T_0 = 1 の位置にラベルを配置
ax.axvline(x=1, linestyle='--', color='gray', alpha=0.5)
ax.text(1, -0.06, r'$T_0$', ha='center', va='top', fontsize=12, style='italic')

# T/T_0 = 0 に縦線
ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)

plt.tight_layout()
plt.savefig('../../4/4-B-36-figure-1.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 1 saved: 4-B-36-figure-1.png")
