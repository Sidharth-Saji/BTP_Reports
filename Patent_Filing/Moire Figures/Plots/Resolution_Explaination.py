import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# SENSOR
# ==========================================================

N = 2048
sensor_length_mm = 30.0

pixel_pitch = sensor_length_mm / N

x = np.arange(N)
# x_mm = x * pixel_pitch
x_mm = x

# ==========================================================
# GRATING
# ==========================================================

grating_pitch_mm = 1.0

p_pix = grating_pitch_mm / pixel_pitch

signal = 0.5 + 0.5*np.cos(
    2*np.pi*x/p_pix
)

# ==========================================================
# SAMPLING MOIRE
# ==========================================================

T = 66                 # thinning interval
num_k = 4              # k=0,1,2,3

# ==========================================================
# FIGURE
# ==========================================================

fig, axs = plt.subplots(
    6,
    1,
    figsize=(14,12),
    sharex=True
)

# ==========================================================
# (1) ORIGINAL SIGNAL
# ==========================================================

axs[0].plot(
    x_mm,
    signal,
    lw=1.5
)

axs[0].set_title(
    "Original Signal (1 mm Grating)"
)

# ==========================================================
# (2) k = 0 SAMPLES
# ==========================================================

k = 0

idx = np.arange(k, N, T)

axs[1].plot(
    x_mm,
    signal,
    color='0.8'
)

axs[1].plot(
    idx,
    signal[idx],
    'o'
)

axs[1].set_title(
    "k = 0 Thinned Samples"
)

# ==========================================================
# (3) k = 0 INTERPOLATION
# ==========================================================

interp = np.interp(
    x,
    idx,
    signal[idx]
)

axs[2].plot(
    x_mm,
    interp,
    lw=1.5
)

axs[2].plot(
    idx,
    signal[idx],
    'o'
)

axs[2].set_title(
    "Interpolated Signal (k = 0)"
)

# ==========================================================
# (4-6) k = 1,2,3
# ==========================================================

for row, k in enumerate([1,2,3], start=3):

    idx = np.arange(k, N, T)

    interp = np.interp(
        x,
        idx,
        signal[idx]
    )

    axs[row].plot(
        x_mm,
        interp,
        lw=1.5
    )

    axs[row].plot(
        idx,
        signal[idx],
        'o',
        markersize=3
    )

    axs[row].set_title(
        f"k = {k} Samples + Interpolation"
    )

# ==========================================================

for ax in axs:
    ax.grid(True)

axs[-1].set_xlabel(
    "Position on Sensor (mm)"
)

plt.tight_layout()
plt.show()

