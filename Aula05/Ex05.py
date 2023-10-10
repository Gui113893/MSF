import matplotlib.pyplot as plt
from math import sqrt

plt.arrow(0, 0, 0, 5, color="r", width=0.1)
plt.arrow(0, 0, 5/2, (5*sqrt(3))/2, color="r", width=0.1)
plt.arrow(0, 0, -(5*sqrt(3))/2, 5/2, color="r", width=0.1)
plt.arrow(0, 0, 3.214, -3.8302222155, color="r", width=0.1)

plt.axis("equal")
plt.show()