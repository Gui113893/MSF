import matplotlib.pyplot as plt

for t in range(1, 5):
    plt.arrow(0, 0, 2*t, t**2, color="r", width=0.1)

plt.axis("equal")
plt.show()

