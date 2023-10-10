import numpy as np
import matplotlib.pyplot as plt


g = 9.8                          # constante g
vi = 30                          # velocidade inicial
v0 = [30, 0, 0]                  # velocidade inicial nos 3 eixos
r0 = [0, 3, 0]                   # posição inicial nos 3 eixos
a0 = [0, -g, 0]                  # aceleração nos 3 eixos
r = 0.034                         # raio
m = 0.057                        # massa
vT = 20                          # velocidade terminal
dar = 1.225                      # constante densidade do ar
w = [0, 0, -60]                    # rotação descrita por w

ti = 0
tf = 1
dt = 0.001
n = int((tf - ti)/dt)

t = np.linspace(ti, tf, n+1)

def prodExt(a,b):
    return (a[1]*b[2] - b[1]*a[2], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def magnus_3D(r0, v0, a0, rot, p_ar, r, n, dt, vt, m):
    
    A = np.pi * r**2             # área
    apr = .5 * p_ar * A * r      # força de magnus sem produto externo

    x = np.empty(n+1)
    y = np.empty(n+1)
    z = np.empty(n+1)
    
    vx = np.empty(n+1)
    vy = np.empty(n+1)
    vz = np.empty(n+1)
    
    ax = np.empty(n+1)
    ay = np.empty(n+1)
    az = np.empty(n+1)
    
    x[0] = r0[0]
    y[0] = r0[1]
    z[0] = r0[2]
    
    vx[0] = v0[0]
    vy[0] = v0[1]
    vz[0] = v0[2]
    
    ax[0] = a0[0]
    ay[0] = a0[1]
    az[0] = a0[2]
    
    dres = g/vt**2
    for i in range(n):

        vv = np.sqrt(vx[i]**2 + vy[i]**2 + vz[i]**2)  # módulo da velocidade
        rot_v = prodExt(rot, (vx[i], vy[i], vz[i]))
        
        mag_x = apr * rot_v[0]/m
        mag_y = apr * rot_v[1]/m
        mag_z = apr * rot_v[2]/m
        
        ax[i] = a0[0] - dres*vv*vx[i] + mag_x
        ay[i] = a0[1] - dres*vv*vy[i] + mag_y
        az[i] = a0[2] - dres*vv*vz[i] + mag_z
        
        vx[i+1] = vx[i] + ax[i]*dt
        vy[i+1] = vy[i] + ay[i]*dt
        vz[i+1] = vz[i] + az[i]*dt
        
        x[i+1] = x[i] + vx[i]*dt
        y[i+1] = y[i] + vy[i]*dt
        z[i+1] = z[i] + vz[i]*dt

    return (x, y, z), (vx, vy, vz), (ax, ay, az)

def is_Valid(n, x, y, z):
    for i in range(n):
       if (12 < x[i] < 18.4) and (0 <= z[i]) and (1 < y[i]):
            return True
    
    return False
    
values = magnus_3D(r0, v0, a0, w, dar, r, n, dt, vT, m)
x = values[0][0]
y = values[0][1]
z = values[0][2]

if (is_Valid(n, x, y, z)):
    print("Serviço válido")
else:
    print("Serviço não válido")

#alcance

for i in range(n):
    if y[i]<= 0:
        idx = i
        break

xRange = x[idx]
tRange = t[idx]

print(f"A bola cai no solo a {xRange:.2f}m")


plt.plot(x, y)
plt.plot(xRange, 0, "go")
plt.xlabel("x(t) (m)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória XY + Magnus")
plt.show()