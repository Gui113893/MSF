import numpy as np
import matplotlib.pyplot as plt
import math

vt = 100/3.6

g = 9.80
dt = 0.01  #Quanto menor for dt, mais precisos vão ser os resultados. Os resultados apresentados serão todos com dt=0.01
tf = 1.2
ti = 0
D = g/vt**2
m = 0.057
v = 100/3.6


n = int((tf-ti)/dt + 0.1)

y = np.zeros(n+1)
y[0] = 0

x = np.zeros(n+1)
x[0] = 0

Em = np.zeros(n+1)
Em[0] = (1/2)*m*(v**2)

vx = np.zeros(n+1)
vx[0] = math.cos(math.pi/18) * (v)

vy = np.zeros(n+1)
vy[0] = math.sin(math.pi/18) * (v)

t = np.zeros(n+1)
t[0] = 0

ay = np.zeros(n+1)
ax = np.zeros(n+1)

forcaX = np.zeros(n+1)
forcaY = np.zeros(n+1)

trabalho = np.zeros(n+1)

integralX = 0
integralY = 0


for i in range(n):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 +vy[i]**2)

    Em[i] = (m*g*y[i]) + ((1/2)*m*(vv**2))  

    ay[i] = -g-D*vv*vy[i]
    ax[i] = -D*vv*vx[i]

    forcaX[i+1] = m*ax[i]
    forcaY[i+1] = m*(ay[i]+g)

    y[i+1] = y[i] + vy[i+1]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    integralX += ((forcaX[i+1] + forcaX[i])/2)*vx[i]*dt
    integralY += ((forcaY[i+1] + forcaY[i])/2)*vy[i]*dt

    trabalho[i] = integralX + integralY




plt.figure(1)
plt.title("Energia Mecância")
plt.plot(t, Em)

plt.figure(2)
plt.title("Força no OX")
plt.plot(t, forcaX)

plt.figure(3)
plt.title("Força no OY")
plt.plot(t, forcaY)

plt.figure(4)
plt.title("Trabalho")
plt.plot(t, trabalho)

plt.show()
    
    



