import math
import numpy as np
import matplotlib.pyplot as plt

plt.title("Lei do Movimento")
plt.xlabel("Tempo")
plt.ylabel("Posição")

t = np.linspace(0, 30, 100)


x1 = t**2

plt.plot(t, x1)

x2 = (70/3.6)*t

plt.plot(t, x2)


plt.show()

