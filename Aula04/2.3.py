import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#C)
t0 = 0
tf = 4
g = 9.80
vy0 = 0
dt = 0.001
y0 = 0

n = int((tf - t0) / dt + 0.1)
t = np.zeros(n+1)
y = np.zeros(n+1)
vy = np.zeros(n+1)
ay = np.zeros(n+1)

vy[0] = vy0
t[0] = t0
y[0] = y0

for i in range(n):
    ay[i] = g
    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + ay[i] * dt
    t[i+1] = t[i] + dt

print(vy[3000])


#B)
t0 = 0
tf = 4
g = 9.80
vy0 = 0
dt = 0.01
y0 = 0

n = int((tf - t0) / dt + 0.1)
t = np.zeros(n+1)
y = np.zeros(n+1)
vy = np.zeros(n+1)
ay = np.zeros(n+1)

vy[0] = vy0
t[0] = t0
y[0] = y0

for i in range(n):
    ay[i] = g
    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + 9.8 * dt
    t[i+1] = t[i] + dt

print(vy[300])

#D)
print("Exato ", end="")
print(9.8 * 3)

#E)

t0 = 0
tf = 3
g = 9.80
dt = 0.01
y0 = 0

n = int((tf - t0) / dt + 0.1)
t = np.zeros(n+1)
y = np.zeros(n+1)
vy = np.zeros(n+1)


vy[0] = vy0
t[0] = t0
y[0] = y0

for i in range(n):
    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + 9.8 * dt
    t[i+1] = t[i] + dt

print(y[200])

#F)

t0 = 0
tf = 3
g = 9.80
dt = 0.001
y0 = 0

n = int((tf - t0) / dt + 0.1)
t = np.zeros(n+1)
y = np.zeros(n+1)
vy = np.zeros(n+1)


vy[0] = vy0
t[0] = t0
y[0] = y0

for i in range(n):
    y[i+1] = y[i] + vy[i]*dt
    vy[i+1] = vy[i] + 9.8 * dt
    t[i+1] = t[i] + dt

print(y[2000])

#G)
print("Exato ", end="")
print(1/2 * 9.8 * 2*2)
