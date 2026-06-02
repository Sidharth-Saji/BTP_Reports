import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# ORIGINAL SIGNAL
# ==========================================================

N = 2000
cycles = 15

x = np.arange(N)

# 15 cycles across 2000 pixels
y = np.sin(2*np.pi*cycles*x/N)

# ==========================================================
# DECIMATION FACTORS TO TEST
# ==========================================================

decimation_factors = [10, 20, 40, 66]

# ==========================================================
# PLOT
# ==========================================================

fig, axs = plt.subplots(len(decimation_factors)+1,
                        1,
                        figsize=(12, 10),
                        sharex=True)

# Original
axs[0].plot(x, y, lw=1)
axs[0].set_title("Original Signal (15 cycles / 2000 pixels)")
axs[0].grid(True)

# Decimated versions
for ax, D in zip(axs[1:], decimation_factors):

    x_d = x[::D]
    y_d = y[::D]

    ax.plot(x, y, alpha=0.3, lw=1, label='Original')
    ax.plot(x_d, y_d, 'o-', label=f'D = {D}')

    samples_per_cycle = (N/cycles)/D

    ax.set_title(
        f"Decimation Factor D={D}  "
        f"({samples_per_cycle:.2f} samples/cycle)"
    )
    ax.grid(True)
    ax.legend()

axs[-1].set_xlabel("Pixel Position")

plt.tight_layout()
plt.show()