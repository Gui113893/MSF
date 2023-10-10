import numpy as np
import matplotlib.pyplot as plt
import math


vt = 100/3.6

g = 9.80
dt = 0.01 
tf = 3
ti = 0
D = g/vt**2
v = 130/3.6
m = 0.057
raio = 0.067/2 #metros


n = int((tf-ti)/dt + 0.1)

y = np.zeros(n+1)
y[0] = 1

x = np.zeros(n+1)
x[0] = -10

z = np.zeros(n+1)
z[0] = 0

vx = np.zeros(n+1)
vx[0] = math.cos(math.pi/18) * v

vy = np.zeros(n+1)
vy[0] = math.sin(math.pi/18) * v

vz = np.zeros(n+1)
vz[0] = 0


t = np.zeros(n+1)
t[0] = 0

ay = np.zeros(n+1)
ax = np.zeros(n+1)
az = np.zeros(n+1)


maxaltura_found = False
chao_found = False

for i in range(n):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 +vy[i]**2)

    ay[i] = -g-D*vv*vy[i]
    ax[i] = -D*vv*vx[i]
    az[i] = 0

    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    z[i+1] = z[i] + vz[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    if not maxaltura_found and vy[i] < 0:
        print(y[i-1])
        maxaltura_found = True

    if y[i] < 0 and not chao_found:
        print(x[i])
        chao_found = True
        

ax = plt.axes(projection="3d")
ax.plot3D(x, z, y, "k")
ax.set_xlabel("x")
ax.set_ylabel("z")
ax.set_zlabel("y")
plt.show()



