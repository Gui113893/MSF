import numpy as np
import matplotlib.pyplot as plt
import math

vt=1
g = 9.80
dt = 0.001 
tf = 180
ti = 0
m = 75
Po = 0.4 * 735
Cres = 0.9
Afrontal = 0.3 #Area frontal
par = 1.225 #Densidade do ar
res_u = 0.004 #Coeficiente da resistencia de um piso
D = g/vt**2


n = int((tf-ti)/dt + 0.1)

y = np.zeros(n+1)
y[0] = 0

x = np.zeros(n+1)
x[0] = 0

z = np.zeros(n+1)
z[0] = 0

vx = np.zeros(n+1)
vx[0] = 1

vy = np.zeros(n+1)
vy[0] = 0

vz = np.zeros(n+1)
vz[0] = 0


t = np.zeros(n+1)
t[0] = 0

ay = np.zeros(n+1)
ax = np.zeros(n+1)
az = np.zeros(n+1)


for i in range(n):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 +vy[i]**2 + vz[i]**2)

    ay[i] = 0
    ax[i] = (Po/(m*vv)) - ((Cres/(2*m))*Afrontal*par*vv*vx[i]) - (res_u*g)
    az[i] = 0

    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    z[i+1] = z[i] + vz[i]*dt
    vz[i+1] = vz[i] + az[i]*dt 


    if i == n-1:
        print("Velocidade terminal: " + str(vx[i]))

plt.plot(t, x)
plt.show()