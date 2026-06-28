import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(0, 11, 1)

# Generate the signals
step = np.ones(len(t))
ramp = t

# Plot the Step Signal
plt.plot(t, step, 'b-', linewidth=2)
plt.plot(t, step, 'r*', markersize=10)

# Plot the Ramp Signal
plt.plot(t, ramp, 'g-', linewidth=2)
plt.plot(t, ramp, 'm*', markersize=10)

# Display grid
plt.grid(True)

# Label the axes
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

# Add title
plt.title("Step and Ramp Signals")

# Add legend
plt.legend(["Step Signal",
            "Step Points",
            "Ramp Signal",
            "Ramp Points"])

# Display the graph
plt.show()