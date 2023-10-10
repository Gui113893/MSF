
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


def getMaxMin(x0,x1,x2,y0,y1,y2):
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2)
    # Resultados (output): xm, yMaxMin
    
    xab = x0 - x1
    xac = x0 - x2
    xbc = x1 - x2
    
    a = y0/(xab * xac)
    b = -y1/(xab * xbc)
    c = y2/(xac * xbc)
    
    xmla = (b+c)*x0 +(a+c)*x1 + (a+b)*x2
    xm = 0.5 * xmla/(a+b+c)
    
    xta = xm - x0
    xtb = xm - x1
    xtc = xm - x2
    
    yMaxMin = a*xtb*xtc + b*xta*xtc + c*xta*xtb
    
    return xm, yMaxMin       
    

# Método de Euler Cromer (Complexo com RA) - Oscilador Harmónico Forçado

t0 = 0
tf = 500
dt = 0.001

xeq = 0   

m = 1  # kg
k = 1   # Constante elástica
b = 0.05
F0 = 7.5
wf = 1

g = 9.8
x0 = -2
v0 = -4

Nt = int(np.ceil((tf - t0) / dt) + 1)

t = np.linspace(t0, tf, Nt)

x = np.zeros((Nt,)) 
x[0] = x0  

v = np.zeros((Nt,))
v[0] = v0

a = np.zeros((Nt,))


Ec = np.zeros((Nt,)) # Energia cinética
Ec[0] = (1/2) * m * np.sqrt(v0**2)**2

Ep = np.zeros((Nt,))# Energia potencial 
Ep[0] = (1/2) * k * (x0**2)
Em = np.zeros((Nt,)) # Energia mecanica
Em[0] = Ec[0] + Ep[0]

w0 = np.sqrt(k / m)
A_wf = (F0 / m) / (np.sqrt((wf**2 - w0**2)**2 + (b * wf / m)**2))
fase = 0
x_exato = A_wf * np.cos(wf*t + fase)


# Método de Euler Cromer
for i in range(Nt - 1):

    a[i]= (- k * x[i] - b * v[i] + F0 * np.cos(wf * t[i]))/m

    v[i+1]=v[i]+a[i]*dt
    
    x[i+1]=x[i]+v[i+1]*dt
    
    Ec[i+1] = (1/2) * m * np.sqrt(v[i+1]**2)**2
    
    Ep[i+1] = (1/2) * k * x[i+1]**2
    
    # Deveria ser constante pois só tem forcas conservativas
    Em[i+1] = Ec[i+1] + Ep[i+1]
    

extremosCount = 4
x_max = []
t_max = []
x_min = []
t_min = []

for i in range(Nt-2, 1, -1):
    if(extremosCount == 0): break
    if(x[i] > x[i-1] and x[i] > x[i+1]):
        tmax, xmax = getMaxMin(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        t_max.append(tmax)
        x_max.append(xmax)
       
        extremosCount -= 1
    if(x[i] < x[i-1] and x[i] < x[i+1]):
        tmin, xmin = getMaxMin(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        t_min.append(tmin)
        x_min.append(xmin)

        extremosCount -= 1

print(x_max)
   
# Amplitude = (Xmax0 - Xmin0) / 2
amplitude = (x_max[0] - x_min[0]) / 2
print("Amplitude:",amplitude)

# Periodo = (tMax1 - tMax0)
# Frequencia = 1/Periodo
periodo = np.abs(t_max[1] - t_max[0])
#frequencia = 1 / periodo
print("Periodo:",periodo) 
#print("Frequencia:",frequencia) 


print("Energia mecanica: ",Em)



# Plotting
plt.figure(1)
plt.plot(t, x, '-b', linewidth=2)
plt.plot(t, x_exato, '-r', linewidth=2)

plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title("Lei do Movimento")
plt.xlim(0, 200)
plt.legend(["Euler Cromer","Exato"])


plt.figure(2)
plt.plot(t, Em, '-b', linewidth=2)
plt.title("Energia Mecânica")

plt.show() 



