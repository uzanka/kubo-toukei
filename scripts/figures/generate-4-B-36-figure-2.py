#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""演習問題4-B-36: 比熱差と比熱の模式図を描く。
日本語フォントが環境に存在しない場合は、OSに日本語フォントをインストールしてください。
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォントを自動選択（OSごとの代表的なフォント名を順に確認）
FONT_CANDIDATES = [
    "Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic",
    "Yu Gothic", "Meiryo", "Hiragino Sans", "TakaoGothic",
    "MS Gothic", "DejaVu Sans"
]
available_fonts = {f.name for f in fm.fontManager.ttflist}
for font_name in FONT_CANDIDATES:
    if font_name in available_fonts:
        plt.rcParams["font.family"] = font_name
        break
plt.rcParams["axes.unicode_minus"] = False

# 設定値（無次元形状を見るための規格化例）
T0 = 1.0
gamma = 1.0
Vbar = 1.0
H0 = 1.0
dpi = 200

t = np.linspace(0.0, 1.0, 1000)  # t = T/T0
T = t * T0

# 解答(iii): C_n - C_s
delta_C = (Vbar * T * H0**2 / (2.0 * np.pi * T0**2)) * (1.0 - 3.0*t**2)
t_zero = 1.0 / np.sqrt(3.0)
t_max = 1.0 / 3.0

# 図2：参考用の比熱の模式図
# C_n(T) は解答式だけでは決まらないため、ここでは C_n=gamma*T と仮定。
Cn = gamma*T
Cs = Cn - delta_C
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.plot(t, Cn/(gamma*T0), color="red", linewidth=2.5,
        label=r"$C_n/(\gamma T_0)$（仮定：$C_n=\gamma T$）")
ax.plot(t, Cs/(gamma*T0), color="blue", linewidth=2.5,
        label=r"$C_s/(\gamma T_0)$（$C_s=C_n-(C_n-C_s)$）")
ax.axvline(t_zero, color="gray", linestyle="--", linewidth=1.2,
           label=r"$T/T_0=1/\sqrt{3}$")
ax.set_xlabel(r"温度 $T/T_0$")
ax.set_ylabel(r"規格化比熱 $C/(\gamma T_0)$")
ax.set_title("比熱そのものの模式図（正常状態の比熱を仮定）")
ax.set_xlim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("4-B-36-figure-2.png", dpi=dpi)

print("保存しました: 4-B-36-figure-2.png")
plt.show()
