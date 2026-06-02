import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ============================================================
# PARAMETERS
# ============================================================

N = 60                # Number of CCD pixels
p = 6               # Grating pitch
p_s = 10            # Sampling pitch

num_phase_steps = 8

pixel_w = 1.0
pixel_h = 1.0

# ============================================================
# SPACING SETTINGS
# ============================================================

row_spacing = 1.8

y_d = 0
y_c = 16
y_b = 32
y_a = 42

# ============================================================
# FIGURE
# ============================================================

fig, ax = plt.subplots(figsize=(15, 20))

# ============================================================
# HELPER FUNCTION
# ============================================================

def draw_pixel_row(ax, y, values,
                   edgecolor='0.25',
                   linewidth=0.35):

    for k, v in enumerate(values):

        ax.add_patch(
            Rectangle(
                (k, y),
                pixel_w,
                pixel_h,
                facecolor=str(v),
                edgecolor=edgecolor,
                linewidth=linewidth
            )
        )

# ============================================================
# (a) CCD PIXELS + GRATING
# ============================================================

for k in range(N):

    ax.add_patch(
        Rectangle(
            (k, y_a),
            1,
            1,
            facecolor='white',
            edgecolor='goldenrod',
            linewidth=0.5
        )
    )

for k in range(N):

    if (k % p) < (p / 2):

        ax.add_patch(
            Rectangle(
                (k + 0.08, y_a + 0.08),
                0.84,
                0.84,
                facecolor='black',
                edgecolor='none'
            )
        )

# ============================================================
# (b) RECORDED INTENSITY
# ============================================================

x = np.arange(N)

signal = 0.5 + 0.5 * np.sin(
    2 * np.pi * x / p
)

draw_pixel_row(ax, y_b, 1 - signal)

# ============================================================
# (c) SAMPLING PROCESS
# ============================================================

sampled_rows = []

for row in range(num_phase_steps):

    yy = y_c + row * row_spacing

    # dotted reference line
    ax.plot(
        np.arange(N) + 0.5,
        np.full(N, yy + 0.45),
        '.',
        color='black',
        markersize=1.5
    )

    offset = row

    samples = np.full(N, np.nan)

    for k in range(offset, N, p_s):

        intensity = signal[k]

        samples[k] = intensity

        ax.add_patch(
            Rectangle(
                (k, yy),
                1,
                1,
                facecolor=str(1 - intensity),
                edgecolor='0.25',
                linewidth=0.35
            )
        )

    sampled_rows.append(samples)

# ============================================================
# (d) REARRANGED SAMPLED PIXELS + INTERPOLATION
# ============================================================

for row in range(num_phase_steps):

    yy = y_d + row * row_spacing

    samples = sampled_rows[row]

    valid = ~np.isnan(samples)

    x_valid = np.where(valid)[0]
    y_valid = samples[valid]

    # Linear interpolation
    interp_signal = np.interp(
        np.arange(N),
        x_valid,
        y_valid
    )

    draw_pixel_row(
        ax,
        yy,
        1 - interp_signal
    )

    # Optional: show sampled locations
    for xv, yv in zip(x_valid, y_valid):

        ax.add_patch(
            Rectangle(
                (xv + 0.25, yy + 0.25),
                0.5,
                0.5,
                facecolor='none',
                edgecolor='black',
                linewidth=0.5
            )
        )

# ============================================================
# SUBFIGURE LABELS
# ============================================================

ax.text(
    N / 2,
    y_a - 2,
    "(a)",
    fontsize=18,
    ha='center'
)

ax.text(
    N / 2,
    y_b - 2,
    "(b)",
    fontsize=18,
    ha='center'
)

ax.text(
    N / 2,
    y_c - 2,
    "(c)",
    fontsize=18,
    ha='center'
)

ax.text(
    N / 2,
    y_d - 2,
    "(d)",
    fontsize=18,
    ha='center'
)

# ============================================================
# p INDICATOR
# ============================================================

p_start = 10

ax.annotate(
    "",
    xy=(p_start, y_a - 1),
    xytext=(p_start + p, y_a - 1),
    arrowprops=dict(
        arrowstyle="<->",
        lw=1.5
    )
)

ax.text(
    p_start + p / 2,
    y_a - 2.2,
    r"$p$",
    fontsize=16,
    ha='center'
)

# ============================================================
# p_s INDICATOR
# ============================================================

ps_start = 10

ax.annotate(
    "",
    xy=(ps_start, y_c + 6),
    xytext=(ps_start + p_s, y_c + 6),
    arrowprops=dict(
        arrowstyle="<->",
        lw=1.5
    )
)

ax.text(
    ps_start + p_s / 2,
    y_c + 7,
    r"$p_s$",
    fontsize=16,
    ha='center'
)

# ============================================================
# ANNOTATIONS
# ============================================================

ax.annotate(
    "CCD pixels",
    xy=(45, y_a + 0.5),
    xytext=(55, y_a + 3),
    arrowprops=dict(arrowstyle="-"),
    fontsize=14
)

ax.annotate(
    "Recorded intensity",
    xy=(42, y_b + 0.5),
    xytext=(55, y_b + 3),
    arrowprops=dict(arrowstyle="-"),
    fontsize=14
)

ax.text(
    -5,
    y_b + 0.3,
    r"$i$",
    fontsize=16
)

# ============================================================
# FORMATTING
# ============================================================

ax.set_xlim(-8, N + 10)
ax.set_ylim(-3, 48)

ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

# ============================================================
# SAVE OUTPUTS
# ============================================================


plt.savefig(
    "Sampling_Moire_Representation.pdf",
    dpi=600,
    bbox_inches="tight"
)

plt.show()



