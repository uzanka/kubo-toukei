"""
演習問題【5-A-5】(i) 位相空間 (x, p) における質点の軌道を図示するスクリプト.

0 <= x <= l の範囲で運動する質量 m の質点は，x=0 および x=l で弾性衝突を行い，
位相空間上では p = +p0 と p = -p0 の2本の直線を描く.
"""

import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# --- パラメータ（数値は図示用） ---
l_val = 5.0    # 箱の全長
p0_val = 3.0   # 運動量の大きさ

# --- 位相空間の軌道データ ---
# 往路: x=0 -> l, p = +p0
x_forward = np.array([0.0, l_val])
p_forward = np.array([+p0_val, +p0_val])

# 復路: x=l -> 0, p = -p0
x_backward = np.array([l_val, 0.0])
p_backward = np.array([-p0_val, -p0_val])

# --- プロット ---
fig, ax = plt.subplots(figsize=(6, 5))

# 軌道を描く
ax.plot(x_forward, p_forward, 'b-', linewidth=2, label='$p = +p_0$')
ax.plot(x_backward, p_backward, 'r-', linewidth=2, label='$p = -p_0$')

# 始点と終点を矢印で示す
ax.annotate('', xy=(l_val - 0.3, p0_val), xytext=(0.3, p0_val),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.annotate('', xy=(0.3, -p0_val), xytext=(l_val - 0.3, -p0_val),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))

# 壁の位置を点線で示す
ax.axvline(x=0, color='gray', linestyle=':', linewidth=1)
ax.axvline(x=l_val, color='gray', linestyle=':', linewidth=1)

# x = l の壁に跳ね返りの矢印を追加
ax.annotate('', xy=(l_val, p0_val + 0.3), xytext=(l_val, -p0_val - 0.3),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))

# --- 軸とラベル ---
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$p$', fontsize=14)
ax.set_xlim(-0.5, l_val + 0.5)
ax.set_ylim(-p0_val - 1.0, p0_val + 1.0)
ax.set_xticks([0, l_val])
ax.set_xticklabels(['0', '$l$'])
ax.set_yticks([-p0_val, p0_val])
ax.set_yticklabels([f'$-p_0$', f'$+p_0$'])

# グリッドとタイトルの設定
ax.grid(True, alpha=0.3)
ax.set_title('Phase Space Trajectory', fontsize=12)

# 凡例
ax.legend(loc='upper right', fontsize=11)

# 図を保存
fig.tight_layout()
fig.savefig('../../5/5-A-5-figure-1.png', dpi=150, bbox_inches='tight')
plt.close(fig)

print("Figure saved to 5/5-A-5-figure-1.png")
