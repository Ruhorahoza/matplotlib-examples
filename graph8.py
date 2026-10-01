import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time values at 200 ms intervals
t = np.arange(0, 5, 0.2)

# Plot the three lines
plt.plot(t, t, "b-", linewidth=2.0, label="Thing 1")
plt.plot(t, t**2, "r-", linewidth=2.0, label="Thing 2")
plt.plot(t, t**3, "g-", linewidth=2.0, label="Thing 3")

# Labels
plt.xlabel("Dummy data for x")
plt.ylabel("Dummy data for y")

# Title
plt.title("An example graph")

# Add legend outside the graph
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc=2,
    borderaxespad=0
)

plt.show()