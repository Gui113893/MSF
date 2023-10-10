import numpy as np
import matplotlib.pyplot as plt

g = 9.8 # Aceleração gravítica na terra

mu = 0.04 # Coeficiente de resistência do rolamento
rho_ar = 1.225 # Densidade do ar
A = 2
m = 2000
C_res = 0.25 # Coeficiente de resistência do ar
p_carro = 40000

# Parâmetros
dt = 0.01
t0 = 0
tf = 150
x0 = 0
v0 = 1

# Inclinação em radianos
incl = np.radians(5)


def accel(v):

    accel_p = p_carro/(m * v)
    # Aceleração pela resistência do ar
    accel_res = -C_res/(2*m) * A * rho_ar * v**2
    # Aceleração pelo atrito
    accel_atrito = - mu * np.cos(incl) * g
    # Aceleração pelo peso
    accel_peso = - np.sin(incl) * g
    # Aceleração total
    return accel_p + accel_res + accel_atrito + accel_peso

n = int((tf-t0) / dt + 0.1)

t = np.zeros(n + 1)
x = np.zeros(n + 1)
v = np.zeros(n + 1)
a = np.zeros(n + 1)

# Valores iniciais
a[0] = accel(v0)
v[0] = v0
x[0] = x0
t[0] = t0

for i in range(n):
    a[i + 1] = accel(v[i])
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i] * dt
    t[i + 1] = t[i] + dt

plt.figure(1)
plt.title("Posição")
plt.plot(t, x)
plt.xlabel("t(s)")
plt.ylabel("x(t) (m)")


for i in range(n):
  # Subtrair 2km a posição
  scaledX0 = x[i] - 2000
  scaledX1 = x[i + 1] - 2000
  # Procurar os zeros com a posição modificada
  if scaledX0 == 0 or scaledX0 * scaledX1 < 0:
    idx = i
    break

x2000 = x[idx]
t2000 = t[idx]

print(f"Demora {t2000:.3f}s a percorrer 2km")

plt.plot(t2000, 2000, "go")

plt.figure(2)
plt.title("Velocidade")
plt.plot(t, v)
plt.xlabel("t(s)")
plt.ylabel("v(t) (m/s)")

W = np.zeros(n + 1)

# O trabalho é dado pela força * velocidade, logo fazemos já a multiplicação dos dois arrays
F_times_v = m * a * v

dx = (tf - t0)/n
W = dx * ((F_times_v[0] + F_times_v[n]) * 0.5 + np.sum(F_times_v[1:n]))

print(f"Trabalho durante a viagem: {W:.2f} J")



plt.show()
