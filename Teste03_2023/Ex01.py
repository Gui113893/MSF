import matplotlib.pyplot as plt
import numpy as np


def getMaxMin(x0,x1,x2,y0,y1,y2):

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
    
    yMaxMin=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    
    return xm, yMaxMin       
    


t0 = 0
tf = 300
dt = 0.001

g = 9.8
x0 = 2.2
v0 = 0  


m = 1  
k = 1 
alpha = 0.05 

Nt = int(np.ceil((tf - t0) / dt) + 1)

t = np.linspace(t0, tf, Nt)


x = np.zeros(Nt) 
x[0] = x0  

v = np.zeros(Nt)
v[0] = v0

a = np.zeros(Nt)



Ec = np.zeros(Nt) # Energia cinética
Ec[0] = 0.5 * m * np.sqrt(v0**2)**2

Ep = np.zeros(Nt)# Energia potencial
Ep[0] = 0.5 * k * x0**2 + alpha * (x0**3)
Em = np.zeros(Nt) # Energia mecanica
Em[0] = Ec[0] + Ep[0]


# Método de Euler Cromer
for i in range(Nt - 1):
    a[i]= -k*x[i] - 3* alpha * x[i]**2
    v[i+1]=v[i]+a[i]*dt
    
    x[i+1]=x[i]+v[i+1]*dt
    
    Ec[i+1] = 0.5 * m * np.sqrt(v[i]**2)**2
    
    Ep[i+1] = 0.5 * k * x[i]**2 + alpha * (x[i]**3)
    
    # Deveria ser constante pois só tem forcas conservativas
    Em[i+1] = Ec[i+1] + Ep[i+1]
    
#a) e b)
plt.figure(1)
plt.plot(x, Ep)
plt.title("Energia Potencial")
plt.xlabel("x(m)")
plt.ylabel("Ep(J)")
plt.xlim(-8, 4)


plt.figure(2)
plt.plot(x, Em)
plt.title("Energia Total")
plt.xlabel("x(m)")
plt.ylabel("Energia Total(J)")

plt.figure(3)
plt.plot(t, x)
plt.title("Lei do Movimento")
plt.xlabel("t(s)")
plt.ylabel("x(m)")

#c)
extr = 4
i = np.where(t == 250)[0][0]
x_ext = []
t_ext = []

while True:
    if(x[i] > x[i-1] and x[i] > x[i+1]):
        tmax, xmax = getMaxMin(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        
        t_ext.append(tmax)
        x_ext.append(xmax)
        k += 1
       
    if(x[i] < x[i-1] and x[i] < x[i+1]):
        tmin, xmin = getMaxMin(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])   
        
        t_ext.append(tmin)
        x_ext.append(xmin)
        k += 1
    
    
    if k == extr:
        break
    
    i += 1

        

amplitude = (np.abs(x_ext[0]) + np.abs(x_ext[1])) / 2
print("Amplitude:",amplitude)

periodo = np.abs(t_ext[2] - t_ext[0])
print("Periodo:",periodo) 

frequencia = 1 / periodo
print("Frequencia:",frequencia)    
      

plt.show() 












