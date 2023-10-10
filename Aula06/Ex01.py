import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
tf = 1 #TEMPO FINAL
ti = 0   #TEMPO INICIAL
g = 9.80
vt = 100/3.6 #VELOCIDADE TERMINAL
D = g/vt**2 
v_inicial = 100/3.6  #VELOCIDADE INICIAL  KM/H -> M/S


N = np.int((tf-ti)/dt + 0.1)

x = np.zeros(N+1)
x[0] = 0

y = np.zeros(N+1)
y[0] = 0

t = np.zeros(N+1)
t[0] = 0

vx = np.zeros(N+1)
vx[0] = (v_inicial)*np.cos(np.pi/18)

vy = np.zeros(N+1)
vy[0] = (v_inicial)*np.sin(np.pi/18)

ax = np.zeros(N+1)
ax[0] = 0

ay = np.zeros(N+1)
ay[0] = -g

for i in range(N):
    ax[i] = 0
    ay[i] = -g

    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    t[i+1] = t[i] + dt

plt.plot(x, y)
altura_NaoEncontrada = True
distancia_NaoEncontrada = True

for i in range(N):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 +vy[i]**2)
    ax[i] = -D*vv*vx[i]
    ay[i] = -g-D*vv*vy[i]

    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    if vy[i] < 0 and altura_NaoEncontrada:
        print(y[i], t[i])
        altura_NaoEncontrada = False
    
    if y[i] < 0 and distancia_NaoEncontrada:
        print(x[i-1], t[i-1])
        distancia_NaoEncontrada = False


plt.plot(x, y)
plt.show()