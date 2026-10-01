import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time at 200 ms intervals
t = np.arange(0.0, 5.0, 0.2)

# Create three lines
lines = plt.plot(
    t, t, "b-",
    t, t**2, "r-",
    t, t**3, "g-",
    linewidth=2.0
)

# Set multiple properties for all lines
plt.setp(
    lines,
    color="r",
    linewidth=2.0
)

# MATLAB-style property/value pairs
plt.setp(
    lines,
    "color", "r",
    "linewidth", 2.0
)

# Display the graph
plt.show()