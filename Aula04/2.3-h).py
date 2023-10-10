import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 4
dt = [0.1, 0.01, 0.001, 0.0001]
g = 9.8

desvio = np.empty(len(dt))

for i in range(len(dt)):
    n = int((tf-t0)/dt[i])   
    t = np.linspace(t0, tf, n)
    v = np.empty(n)
    v[0] = 0
    x = np.empty(n)
    x[0] = 0
    
    for j in range(n-1):
        v[j+1] = v[j] + g*dt[i]
        x[j+1] = x[j] + v[j]*dt[i]
    
    for j in range(n-1):
        if ((2-dt[i]) < t[j] < (2+dt[i])):
            print("dt, t, x =", dt[i], t[j], x[j])
            desvio[i] = abs(abs(19.6) - abs(x[j]))

plt.xlabel("Dt (s)")
plt.ylabel("Desvio (m)")
plt.plot(dt, desvio)
plt.show()