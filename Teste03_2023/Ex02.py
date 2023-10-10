import matplotlib.pyplot as plt
import numpy as np

#A)

def acell(t,x,v):
    F_amort = -b * v
    F_ext = F0 * np.cos(wf * t)
    F_x = - 4 * alpha * x**3
    return  (F_amort + F_ext + F_x) / m

def RungeKutte(t,x,vx,acell,dt):

    ax1=acell(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acell(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt # predicto:  vx(t+dt) * dt
    ax3=acell(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acell(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
     
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

t0 = 0
tf = 100
dt = 0.01
 
k = 1
b = 0.02 
alpha = 0.15
F0 = 7.5
wf = 1

m = 1

g = 9.8


Nt = int(np.ceil((tf - t0) / dt) + 1)

t = np.linspace(t0, tf, Nt)


x = np.zeros(Nt)
x[0] = 2

v = np.zeros(Nt)
v[0] = 0

a = np.zeros(Nt)


for i in range(Nt-1):
    (x[i+1],v[i+1]) = RungeKutte(t[i], x[i],v[i],acell,dt)

plt.plot(t, x)
plt.title("Lei do Movimento")
plt.xlabel("t(s)")
plt.ylabel("y(m)")

plt.show()

