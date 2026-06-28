import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(0, 11, 1)

# Generate the Unit Impulse Signal
imp = np.zeros(len(t))
imp[0] = 1

# Plot the signal
plt.stem(t, imp)

# Highlight the impulse point
plt.plot(t[0], imp[0], 'r*', markersize=12)

# Display grid
plt.grid(True)

# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

# Add title
plt.title("Unit Impulse Signal")

# Display the graph
plt.show()

