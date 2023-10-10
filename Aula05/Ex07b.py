import matplotlib.pyplot as plt

for t in range(1, 7):
    
    plt.arrow(2*t, t**2, 2, 2*t, color="r", width=0.1)
    plt.arrow(0, 0, 2*t, t**2, color="b", width=0.1)

plt.axis("equal")
plt.show()

