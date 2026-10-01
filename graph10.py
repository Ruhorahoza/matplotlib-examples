import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time at 200 ms intervals
t = np.arange(0.0, 5.0, 0.2)

# Red, blue and green lines
lines = plt.plot(
    t, t, "b-",
    t, t**2, "r-",
    t, t**3, "g-",
    linewidth=2.0
)

# Set properties for all lines
plt.setp(lines, color="r", linewidth=2.0)

# Labels
plt.xlabel("Dummy data for x")
plt.ylabel("Dummy data for y")

# Title
plt.title("An example graph")

# Add text
plt.text(1, 80, "Lew is good at graphs")

plt.show()