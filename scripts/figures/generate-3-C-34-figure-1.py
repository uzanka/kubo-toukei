import numpy as np
import matplotlib.pyplot as plt

# Parameters
T0 = 300.0       # Initial temperature [K]
alpha = 7.0e-4   # Coefficient [1/K]
delta = alpha * T0

# Stretch ratio L = l/l0
L = np.linspace(1.0, 2.0, 600)

# Normalized temperature change:
# Delta T = (A*l0*T0/(2*C_l)) * y_norm
y_norm = ((L - 1.0) / L) * (
    L**2 + L - 2.0 * (1.0 + delta)
)

# Zero crossing for L > 1
L_crit = (-1.0 + np.sqrt(9.0 + 8.0 * delta)) / 2.0

plt.figure(figsize=(8, 5))
plt.plot(L, y_norm, label="Normalized temperature change")
plt.axhline(0.0, linewidth=1)
plt.axvline(
    L_crit,
    linestyle="--",
    label=f"Zero crossing: L = {L_crit:.3f}"
)
plt.scatter([L_crit], [0.0], zorder=3)

plt.xlabel(r"Stretch ratio $L=l/l_0$")
plt.ylabel(
    r"Normalized $\Delta T$ "
    r"(factor $A l_0 T_0/(2C_l)$ removed)"
)
plt.title("Rubber Joule Effect: Temperature Change vs. Stretch Ratio")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the figure in the current directory
plt.savefig("rubber_joule_effect.png", dpi=200)
plt.show()

print(f"Zero-crossing stretch ratio: L_crit = {L_crit:.6f}")
