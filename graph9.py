import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time at 200 ms intervals
t = np.arange(0.0, 5.0, 0.2)

# Red crosses, blue stars and green circles
plt.plot(
    t, t, "rx",
    t, t**2, "b*",
    t, t**3, "go"
)

plt.show()