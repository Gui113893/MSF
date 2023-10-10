import numpy as np
import matplotlib.pyplot as plt
import math


vt = 20

g = 9.80
dt = 0.01  #Quanto menor for dt, mais precisos vão ser os resultados. Os resultados apresentados serão todos com dt=0.01
tf = 1.8
ti = 0
D = g/vt**2


n = int((tf-ti)/dt + 0.1)

y = np.zeros(n+1)
y[0] = 2

x = np.zeros(n+1)
x[0] = 0

vx = np.zeros(n+1)
vx[0] = math.cos(math.pi/6) * 15

vy = np.zeros(n+1)
vy[0] = math.sin(math.pi/6) * 15

t = np.zeros(n+1)
t[0] = 0

ay = np.zeros(n+1)
ax = np.zeros(n+1)

subir = True
valor_encontrado = False


for i in range(n):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 +vy[i]**2)

    ay[i] = -g-D*vv*vy[i]
    ax[i] = -D*vv*vx[i]

    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    if vy[i] < 0 and subir and not valor_encontrado:
        subir = False
    

    if y[i] < 3 and not subir and not valor_encontrado:
        d = x[i-1] #Distância percorrida
        h = y[i-1]  #Altura
        print(y[i-1])
        print(f"Distância: ", x[i-1]) #13.56m
        print(f"Momento: ", t[i-1]) #1.25s
        subir = True
        valor_encontrado = True


plt.figure(3)
plt.title("Trajetória Bola")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.plot(x, y)
plt.plot(d, h, "go") #Ponto onde a bola está a descer e passa pelo cesto
plt.show()


    
    


