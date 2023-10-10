import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.title("Lei do Movimento")

plt.xlabel("t(s)")
plt.ylabel("y(m)")

t = np.linspace(0, 4, 100)

vt = 6.80

yt = (vt**2/9.8)*np.log10(np.cosh((9.8*t)/vt))

plt.plot(t, yt)


y, v, g, t = sy.symbols("y, v, g, t")
y = (v**2/g)*sy.log(sy.cosh((g*t)/v))

y2 = y.subs([(v, 6.80), (g, 9.8)])

y_lamb = sy.lambdify(t, y, "numpy")

df = sy.diff(y_lamb, t)

print(df)





plt.show()

