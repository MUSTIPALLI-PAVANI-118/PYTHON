import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(0, 11, 1)

# Generate the Parabolic Signal
p = t**2

# Plot the signal
plt.plot(t, p, 'b-', linewidth=2)
plt.plot(t, p, 'r*', markersize=10)

# Display grid
plt.grid(True)

# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

# Add title
plt.title("Parabolic Signal")

# Display the graph
plt.show()