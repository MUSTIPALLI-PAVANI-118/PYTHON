import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(1, 9, 1)

# Generate the Unit Step Signal
u = np.ones(len(t))

# Plot the signal
plt.plot(t, u, 'b-', linewidth=2)
plt.plot(t, u, 'r*', markersize=10)

# Display grid
plt.grid(True)

# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

# Add title
plt.title("Unit Step Signal")

# Display the graph
plt.show()


