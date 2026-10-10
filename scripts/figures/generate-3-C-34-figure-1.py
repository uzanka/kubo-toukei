"""
演習問題 3-C-34 の解答図: ジェール効果による温度変化 ΔT(L)

式(4): ΔT = (A l₀ / 2Cₗ) T₀ · [(L-1)/L] · {L² + L - 2(1+αT₀)}
の形状を図示する。
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---- CJKフォント設定 (Windows: YuGoth) ----
matplotlib.rcParams['font.family'] = 'Yu Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# ---- パラメータ ----
alpha = 7e-4          # 熱膨張係数 [deg⁻¹]
T0    = 300.0         # 初期温度 [K]（目安）
aT0   = alpha * T0    # αT₀ ≈ 0.21

def dT(L):
    """ΔT の L 依存性（比例定数を省略）"""
    return ((L - 1) / L) * (L**2 + L - 2 * (1 + aT0))

# ---- L の範囲 ----
L = np.linspace(0.5, 3.0, 500)
delta_T = dT(L)

# ---- プロット ----
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(L, delta_T, color='#1f77b4', linewidth=2, label=r'$\Delta T \propto \dfrac{L-1}{L}\{L^2+L-2(1+\alpha T_0)\}$')

# L=1 の縦線（自然長の位置）
ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=0.8)
latex_label = r'$L = 1$' + ' (自然長)'
ax.text(1.05, 0, latex_label, va='center', fontsize=9, color='gray')

# ΔT=0 の横線
ax.axhline(y=0, color='black', linewidth=0.5)

# 符号の境界 (L ≈ 1.14)
import math, os
L_crit = (-1 + math.sqrt(1 + 8*(1+aT0))) / 2
ax.plot(L_crit, 0, 'ro', markersize=6)
ax.text(L_crit + 0.05, -0.1, f' $\\Delta T = 0$ ({L_crit:.4f})', va='top', fontsize=9, color='red')

# 領域の注釈
ax.annotate('温度低下\n(伸長小域)', xy=(1.05, -0.3), fontsize=9,
            ha='left', va='center', color='blue',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.5))
ax.annotate('温度上昇\n(伸長大域)', xy=(2.5, 1.5), fontsize=9,
            ha='center', va='center', color='red',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.5))

# タイトル・ラベル
ax.set_title('演習問題【3-C-34】ゴムのジェール効果: 温度変化 $\\Delta T$ vs 伸張比 $L$', fontsize=12, fontweight='bold')
ax.set_xlabel('伸張比 $L = l / l_0$', fontsize=11)
ax.set_ylabel(r'$\Delta T$ （比例定数を省略）', fontsize=11)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(bottom=-2.0)

fig.tight_layout()

# ---- 保存 ----
os.makedirs('3', exist_ok=True)
out = '../../3/3-C-34-figure-1.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f'Saved: {out}')
