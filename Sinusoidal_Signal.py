import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(0, 10.5, 0.5)

# Generate the Sinusoidal Signal
y = np.sin(t)

# Plot the signal
plt.plot(t, y, 'b-', linewidth=2)
plt.plot(t, y, 'r*', markersize=10)

# Display grid
plt.grid(True)

# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

# Add title
plt.title("Sinusoidal Signal")

# Display the graph
plt.show()