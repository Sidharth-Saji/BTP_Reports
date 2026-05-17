import numpy as np
import matplotlib.pyplot as plt

# 1. Setup Parameters
fs = 1000       # Sampling frequency (samples per second)
f = 5           # Frequency of the sine wave in Hz
duration = 1    # Duration in seconds

# 2. Generate Time and Sine Data
# Create an array of time points from 0 to 'duration'
t = np.linspace(0, duration, fs, endpoint=False)
# Calculate the sine wave values: y = sin(2 * pi * f * t)
y = np.sin(2 * np.pi * f * t)

# 3. Create the Plot
plt.figure(figsize=(10, 4))
plt.plot(t, y, label=f'{f} Hz Sine Wave', color='tab:blue')

# Formatting the visual
plt.title('Generated Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--')
plt.legend()

# 4. Save to PDF
output_filename = "sine_wave.pdf"
plt.savefig(output_filename, format='pdf')
print(f"Successfully saved plot to {output_filename}")

# Optional: Show the plot on screen
# plt.show()
