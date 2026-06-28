import numpy as np
import matplotlib.pyplot as plt
# Define the time vector
t = np.arange(0, 11, 1)
# Generate the Unit Ramp Signal
r = t
# Plot the signal
plt.plot(t, r, 'b-', linewidth=2)
plt.plot(t, r, 'r*', markersize=10)
# Display grid
plt.grid(True)
# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
# Add title
plt.title("Unit Ramp Signal")
# Display the graph
plt.show()

