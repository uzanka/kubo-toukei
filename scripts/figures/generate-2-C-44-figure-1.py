import os, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams['font.size'] = 11

# Dieterici: p = (8-t)*exp(5/2 - 4/t)
t_d = np.linspace(0.3, 7.99, 600)
p_d = (8 - t_d) * np.exp(2.5 - 4.0 / t_d)

# van der Waals: p = -27 + 24*sqrt(3t) - 12t
t_v = np.linspace(0, 2.25, 600)
p_v = -27 + 24 * np.sqrt(3 * t_v) - 12 * t_v

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(t_d, p_d, 'b-', linewidth=2.5, label='Dieterici', zorder=3)
ax.plot(t_v, p_v, 'r--', linewidth=2.5, label='van der Waals', zorder=3)

# Critical point
ax.plot(1, 1, 'ko', markersize=8, label=r'Critical $(p_c, v_c, t_c)$', zorder=4)

# Grid lines at critical values
ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5, zorder=1)
ax.axvline(x=1, color='gray', linestyle=':', alpha=0.3, zorder=1)
ax.axhline(y=1, color='gray', linestyle=':', alpha=0.3, zorder=1)

# Max points
idx_max = np.argmax(p_d)
t_max_d, p_max_d = t_d[idx_max], p_d[idx_max]
ax.plot(t_max_d, p_max_d, 'bo', markersize=6, zorder=4)
ax.annotate(f'Max: ({t_max_d:.2f}, {p_max_d:.1f})',
           xy=(t_max_d, p_max_d), xytext=(t_max_d+0.5, p_max_d-3),
           fontsize=9, color='blue', arrowprops=dict(arrowstyle='->', color='blue'))

idx_max_v = np.argmax(p_v)
t_max_v, p_max_v = t_v[idx_max_v], p_v[idx_max_v]
ax.plot(t_max_v, p_max_v, 'rs', markersize=6, zorder=4)
ax.annotate(f'Max: ({t_max_v:.3f}, {p_max_v:.1f})',
           xy=(t_max_v, p_max_v), xytext=(t_max_v+0.2, p_max_v-5),
           fontsize=9, color='red', arrowprops=dict(arrowstyle='->', color='red'))

ax.set_xlabel(r'Reduced temperature $t = T/T_c$', fontsize=13)
ax.set_ylabel(r'Reduced pressure $p = P/P_c$', fontsize=13)
ax.set_title('Joule-Thomson Inversion Curves\n久保統計 2-C-44', fontsize=14, pad=10)
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3, zorder=2)
ax.set_xlim(-0.1, 8.5)
ymax = max(np.max(p_d), np.max(p_v)) + 3
ax.set_ylim(-2, ymax)

plt.tight_layout()
out = '../../2/2-C-44-figure-1.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'Done: {out} ({os.path.getsize(out)} bytes)')
