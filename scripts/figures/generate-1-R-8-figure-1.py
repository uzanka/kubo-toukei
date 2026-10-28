#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reduced van der Waals 等温線、スピノーダル線、
ボイル軌跡を描画する。

reduced van der Waals 方程式：
    p_r = 8 T_r / (3 V_r - 1) - 3 / V_r**2

厳密なボイル軌跡の条件：
    (d(p_r * V_r) / d p_r)_(T_r) = 0

ボイル軌跡を媒介変数で表した曲線には、
V_r = 2/3、T_r = 27/32、p_r = 0 に特異点が存在する。
この点では dp_r/dV_r = 0 となるため、
連鎖律による微分の比から元の条件を定義できない。
そのため、この点は厳密なボイル軌跡の描画から除外する。
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


def configure_japanese_font() -> None:
    """利用可能な日本語フォントを選択する。"""
    candidates = [
        "Noto Sans CJK JP",
        "Noto Serif CJK JP",
        "IPAexGothic",
        "IPAGothic",
        "Yu Gothic",
        "Meiryo",
        "Hiragino Sans",
        "BIZ UDPGothic",
        "TakaoGothic",
    ]

    # インストール済みフォントの名前を取得する。
    installed_fonts = {
        font.name for font in font_manager.fontManager.ttflist
    }

    # 利用可能な日本語フォントを優先順位に従って選択する。
    for font_name in candidates:
        if font_name in installed_fonts:
            plt.rcParams["font.family"] = font_name
            break
    else:
        print(
            "警告：日本語フォントが見つかりません。"
            "日本語フォントをインストールしてください。"
        )

    # 負の数の記号が文字化けするのを防ぐ。
    plt.rcParams["axes.unicode_minus"] = False


def reduced_pressure(v: np.ndarray, t: float) -> np.ndarray:
    """Reduced van der Waals 方程式から Reduced 圧力 を計算する。"""
    return 8.0 * t / (3.0 * v - 1.0) - 3.0 / v**2


def main() -> None:
    # 日本語フォントを設定する。
    configure_japanese_font()

    # ファン・デル・ワールス方程式の物理的な定義域は V_r > 1/3。
    v_min = 1.0 / 3.0 + 0.006
    v_max = 3.0
    v = np.linspace(v_min, v_max, 1600)

    # 描画する還元温度。
    temperatures = [0.6, 0.8, 1.0, 1.2]

    # グラフを作成する。
    fig, ax = plt.subplots(figsize=(10, 6.5))

    # --------------------------------------------------
    # 1. 等温線
    # --------------------------------------------------
    for t in temperatures:
        p = reduced_pressure(v, t)
        ax.plot(
            v,
            p,
            linewidth=2,
            label=fr"等温線 $T_r={t}$",
        )

    # --------------------------------------------------
    # 2. スピノーダル線
    # --------------------------------------------------
    # スピノーダル線の条件：
    # (∂p_r / ∂v_r)_T_r = 0
    #
    # この条件から、次の媒介表示が得られる。
    # T_r = (3v_r - 1)^2 / (4v_r^3)
    # p_r = (3v_r - 2) / v_r^3
    vs = np.linspace(v_min, v_max, 1200)
    p_spinodal = (3.0 * vs - 2.0) / vs**3

    ax.plot(
        vs,
        p_spinodal,
        linestyle="--",
        linewidth=2,
        label=(
            r"スピノーダル線："
            r"$(\partial p_r/\partial v_r)_{T_r}=0$"
        ),
    )

    # --------------------------------------------------
    # 3. ボイル軌跡
    # --------------------------------------------------
    # ボイル軌跡の式：
    # p_r = 3(3v_r - 2) / v_r^2
    #
    # V_r = 2/3 の近傍では、元の微分条件を
    # 連鎖律による微分の比で評価できないため、
    # その近傍を描画対象から除外する。
    v_boyle_left = np.linspace(
        v_min,
        2.0 / 3.0 - 0.008,
        450,
    )
    v_boyle_right = np.linspace(
        2.0 / 3.0 + 0.008,
        v_max,
        850,
    )

    for i, vb in enumerate(
        (v_boyle_left, v_boyle_right)
    ):
        p_boyle = 3.0 * (3.0 * vb - 2.0) / vb**2

        ax.plot(
            vb,
            p_boyle,
            linestyle=":",
            linewidth=2.5,
            label="ボイル軌跡" if i == 0 else "_nolegend_",
        )

    # --------------------------------------------------
    # 4. 臨界点
    # --------------------------------------------------
    ax.scatter([1.0], [1.0], zorder=5)

    ax.annotate(
        "臨界点 (1, 1)",
        xy=(1.0, 1.0),
        xytext=(1.18, 1.25),
        arrowprops={
            "arrowstyle": "->",
            "linewidth": 1.2,
        },
    )

    # --------------------------------------------------
    # 5. グラフの体裁
    # --------------------------------------------------
    # 還元圧力がゼロとなる水平線を描画する。
    ax.axhline(0.0, linewidth=0.8)

    # 横軸・縦軸の表示範囲を設定する。
    ax.set_xlim(0.33, 3.0)
    ax.set_ylim(-0.8, 3.2)

    # 軸ラベルとグラフタイトルを日本語化する。
    ax.set_xlabel(r"Reduced 体積 $\mathfrak{v}=V/V_c$")
    ax.set_ylabel(r"Reduced 圧力 $\mathfrak{p}=p/p_c$")
    ax.set_title("Reduced van der Waals 等温線と各軌跡")

    # 目盛線を表示する。
    ax.grid(True, alpha=0.3)

    # 凡例を自動的に適切な位置に配置する。
    ax.legend(loc="best", fontsize=9)

    # 図の余白を自動調整する。
    fig.tight_layout()

    # --------------------------------------------------
    # 6. グラフの保存と表示
    # --------------------------------------------------
    # このスクリプトと同じフォルダーに画像を保存する。
    output_path = Path(__file__).resolve().with_name(
        "1-R-8-figure-1.png"
    )

    fig.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
    )

    print(f"グラフを保存しました：{output_path}")

    # グラフを画面に表示する。
    plt.show()


if __name__ == "__main__":
    main()
