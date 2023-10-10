import numpy as np
import matplotlib.pyplot as plt


# Valores dados
k = 1
m = 1
g = 9.8

# Valores calculados
omega = np.sqrt(k/m)
A = 4
phi = 0

# Parâmetros
dt = 0.001
t0 = 0
tf = 10
x0 = 4
v0 = 0

# Esta função calcula a posição a partir do tempo atual
def pos(t):
    return A * np.cos(omega * t + phi)

def maxminv(x0,x1,x2,y0,y1,y2): 
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xm, ymax
    xab=x0-x1
    xac=x0-x2
    xbc=x1-x2
    a=y0/(xab*xac)
    b=-y1/(xab*xbc)
    c=y2/(xac*xbc)
    xmla=(b+c)*x0+(a+c)*x1+(a+b)*x2
    xm=0.5*xmla/(a+b+c)
    xta=xm-x0
    xtb=xm-x1
    xtc=xm-x2
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax


def energiaMecanica(x, v):
    # Energia cinética
    E_c = 1/2 * np.abs(v)**2
    # Energia potencial
    E_p = 1/2 * x**2
    # Energia mecânica
    return E_c + E_p
    

# Esta função calcula a aceleração a partir do tempo atual
def accel(t):
    x = pos(t)
    return -k * x 

# Número de passos/iterações
#
# + 0.1 para garantir que não há arrendodamentos
# para baixo
n = int((tf-t0) / dt + 0.1)

t = np.zeros(n + 1)
x = np.zeros(n + 1)
v = np.zeros(n + 1)
a = np.zeros(n + 1)
E_m = np.zeros(n + 1)

# Insert initial values
a[0] = accel(t0)
v[0] = v0
t[0] = t0
x[0] = x0
E_m[0] = energiaMecanica(x0, v0)

for i in range(n):
    a[i] = -k*x[i]
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i+1] * dt
    t[i + 1] = t[i] + dt

    E_m[i] = energiaMecanica(x[i], v[i])

(t_max, x_max) = maxminv(t[6000], t[6700], t[6500], x[6000], x[6700], x[6500])
print("Interpolação Amplitude: {}" .format(x_max))
print(f"Período: {t_max}")
plt.figure(1)
plt.plot(t[6000], x[6000], "go")
plt.plot(t[6700], x[6700], "go")
plt.plot(t[6500], x[6500], "go")
plt.plot(t, x, label="Cálculo númerico")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.title("Posição mola")
plt.legend(loc="upper right")
plt.figure(2)
plt.plot(t, E_m, "g")
plt.xlabel("t (s)")
plt.ylabel("Energia (J)")
plt.title("Energia mecânica")

print(f"Amplitude teórica = {A}")



plt.show()
