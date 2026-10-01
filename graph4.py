import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 50, 2]

plt.plot(x, y, "-", linewidth=2.0)

plt.axis([0, 10, 0, 60])

plt.title("Changing Line Properties")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()