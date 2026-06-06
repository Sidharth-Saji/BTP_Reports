import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# SENSOR PARAMETERS
# ==========================================================

N = 2048
sensor_length_mm = 30.0

pixel_pitch_mm = sensor_length_mm / N

x = np.arange(N)
x_mm = x * pixel_pitch_mm

# ==========================================================
# GRATING PARAMETERS
# ==========================================================

grating_pitch_mm = 1.0

p_pix = grating_pitch_mm / pixel_pitch_mm

signal = 0.5 + 0.5*np.cos(
    2*np.pi*x/p_pix
)

# ==========================================================
# SAMPLING MOIRE PARAMETERS
# ==========================================================

T = 65

idx = np.arange(0, N, T)

samples = signal[idx]

moire_interp = np.interp(
    x,
    idx,
    samples
)

# ==========================================================
# THEORETICAL VALUES
# ==========================================================

Pm_pix = p_pix*T/abs(T-p_pix)

Pm_mm = Pm_pix * pixel_pitch_mm

M = Pm_pix/p_pix

R_orig_um = (grating_pitch_mm/p_pix)*1000

R_moire_um = R_orig_um/M

print(f"Original pitch      = {grating_pitch_mm:.3f} mm")
print(f"Pitch on sensor     = {p_pix:.2f} pixels")
print(f"Moire pitch         = {Pm_pix:.1f} pixels")
print(f"Moire pitch         = {Pm_mm:.2f} mm")
print(f"Magnification       = {M:.2f}")
print(f"Original resolution = {R_orig_um:.2f} um")
print(f"Moire resolution    = {R_moire_um:.2f} um")

# ==========================================================
# FIGURE 1
# ==========================================================

plt.figure(figsize=(12,4))

plt.plot(
    x,
    signal,
    lw=1.5
)

plt.xlim(0,2100)

plt.grid(True)

plt.title(
    f"Original Grating Signal (Pitch = {grating_pitch_mm} mm)"
)

plt.xlabel("Pixel Number")
plt.ylabel("Intensity")

plt.tight_layout()

# ==========================================================
# FIGURE 2
# ==========================================================

plt.figure(figsize=(12,4))

plt.plot(
    x,
    signal,
    color='0.8',
    lw=1
)

plt.plot(
    idx,
    samples,
    'o',
    markersize=5
)

plt.xlim(0,2100)

plt.grid(True)

plt.title(
    f"Thinning-Out Process (T = {T})"
)

plt.xlabel("Pixel Number")
plt.ylabel("Intensity")

plt.tight_layout()

# ==========================================================
# FIGURE 3
# ==========================================================

plt.figure(figsize=(12,4))

plt.plot(
    x,
    moire_interp,
    lw=2
)

plt.plot(
    idx,
    samples,
    'o',
    markersize=4
)

plt.xlim(0,2100)

plt.grid(True)

plt.title(
    "Interpolated Sampling Moire Signal"
)

plt.xlabel("Pixel Number")
plt.ylabel("Intensity")

plt.tight_layout()

# ==========================================================
# FIGURE 4
# ==========================================================

plt.figure(figsize=(12,5))

plt.plot(
    x,
    signal,
    label="Original Grating",
    lw=1.5
)

plt.plot(
    x,
    moire_interp,
    label="Sampling Moire",
    lw=2
)

plt.xlim(0,2100)

plt.grid(True)

plt.legend()

plt.title(
    "Original Signal vs Sampling Moire Signal"
)

plt.xlabel("Pixel Number")
plt.ylabel("Intensity")

plt.tight_layout()

# ==========================================================
# FIGURE 5
# ==========================================================

plt.figure(figsize=(8,5))

labels = [
    "Original",
    "Sampling Moire"
]

values = [
    R_orig_um,
    R_moire_um
]

bars = plt.bar(
    labels,
    values
)

plt.ylabel(
    "Theoretical Resolution (um)"
)

plt.title(
    f"Resolution Improvement (M = {M:.1f}x)"
)

for bar, val in zip(bars, values):

    plt.text(
        bar.get_x() + bar.get_width()/2,
        val,
        f"{val:.2f}",
        ha='center',
        va='bottom'
    )

plt.tight_layout()

# ==========================================================

plt.show()