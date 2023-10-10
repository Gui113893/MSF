import numpy as np
import matplotlib.pyplot as plt


# Valores dados
k = 1
m = 1
xeq = 1.5

# Valores calculados
omega = np.sqrt(k/m)


# Parâmetros
dt = 0.001
t0 = 0
tf = 10
x0 = 4
v0 = 0

# Esta função calcula a aceleração a partir do tempo atual
def accel(t):
    return -2 * k * (x[t]**2 - xeq **2) * x[t]

def energiaMecanica(x, v):
    # Energia cinética
    E_c = 1/2 * np.abs(v)**2
    # Energia potencial
    E_p = 1/2 * (x**2 - xeq**2)**2
    # Energia mecânica
    return E_c + E_p

def energiaPotencial(x, v):
    return 1/2 * (x**2 - xeq**2)**2

# Número de passos/iterações
#
# + 0.1 para garantir que não há arrendodamentos
# para baixo
n = int((tf-t0) / dt + 0.1)

t = np.zeros(n + 1)
x = np.zeros(n + 1)
v = np.zeros(n + 1)
a = np.zeros(n + 1)
Ep = np.zeros(n+1)

# Insert initial values
v[0] = v0
t[0] = t0
x[0] = x0
a[0] = accel(0)
Ep[0] = energiaPotencial(x0, v0)

for i in range(n):
    a[i + 1] = accel(i)
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i] * dt
    t[i + 1] = t[i] + dt

    Ep[i] = energiaPotencial(x[i], v[i])

plt.figure(1)
plt.plot(x, Ep, "orange")
plt.ylabel("Energia Potencial (J)")
plt.xlabel("x (m)")
plt.title("Oscilador Duplo")
plt.xlim(-4, 4)
plt.ylim(0, 10)
plt.show()


