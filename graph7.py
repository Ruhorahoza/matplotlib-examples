import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time values
t = np.arange(0, 5, 0.2)

# Plot the lines
lines = plt.plot(
    t, t, "b-",
    t, t**2, "r-",
    t, t**3, "g-",
    linewidth=2.0
)

# Set line properties
plt.setp(lines, color="r", linewidth=2.0)

# Labels
plt.xlabel("Dummy data for x")
plt.ylabel("Dummy data for y")

# Title
plt.title("An example graph")

# Add annotation
plt.annotate(
    "Divergence point",
    xy=(1.4, 3),
    xytext=(3, 1.5),
    arrowprops=dict(
        facecolor="black",
        shrink=0.05
    )
)

plt.show()