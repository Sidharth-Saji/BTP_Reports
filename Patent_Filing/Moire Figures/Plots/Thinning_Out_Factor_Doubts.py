import numpy as np
import matplotlib.pyplot as plt

N = 2000
cycles = 15

x = np.arange(N)
y = np.sin(2*np.pi*cycles*x/N)

D_values = [132, 100, 67]

fig, axs = plt.subplots(len(D_values), 1, figsize=(12, 8))

for ax, D in zip(axs, D_values):

    xd = x[::D]
    yd = y[::D]

    ax.plot(x, y, 'k', alpha=0.25, label='Original')

    ax.plot(
        xd,
        yd,
        'o-',
        linewidth=2,
        markersize=6,
        label=f'D={D}'
    )

    ax.set_title(
        f'D={D}   Samples={len(xd)}'
    )

    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()