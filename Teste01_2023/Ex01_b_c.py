import numpy as np
import matplotlib.pyplot as plt

#B)
t = np.array([0, 48 , 96, 144, 192, 240, 288, 336, 384])
valores = np.array([10.03, 7.06, 4.88, 3.38, 2.26, 1.66, 1.14, 0.79, 0.58])

logvalores = np.log(valores)

data_points = np.size(t)

mul_sum = np.sum(np.multiply(t, logvalores))

x_sum = np.sum(t)
y_sum = np.sum(logvalores)

m_numerator = data_points * mul_sum - x_sum * y_sum

x2_sum = np.sum(np.square(t))
x_sum2 = np.square(np.sum(t))

x_denom = data_points * x2_sum - x_sum2

m = m_numerator / x_denom   #Declive

b = (x2_sum * y_sum - x_sum * mul_sum) / x_denom  #Ordenada na origem

y2_sum = np.sum(np.square(logvalores))
y_sum2 = np.square(np.sum(logvalores))

y_denom = data_points * y2_sum - y_sum2

r2 = m_numerator**2 / (x_denom * y_denom)  #Coeficiente de Determinação

#Erros
delta_m = np.absolute(m) * np.sqrt((1 / r2 - 1) / (data_points - 2))

delta_b = delta_m * np.sqrt(x2_sum / data_points)

plt.figure(2)
plt.title("Gráfico x-log")
plt.xlabel("t(h)")
plt.ylabel("log(mBq)")
plt.plot(t, logvalores, "go")
plt.plot(t, m*t + b)
print(f"Declive: {m}; Erro(Declive): {delta_m}") #Declive: -0.0075 Erro declive: 6.33*10^-5
print("Coeficiente de Determinação: ", r2) #r2=0.9995
plt.show()

#C)
decaimento = (-np.log(2))/m
decaimento_erro = (-np.log(2))/delta_m

print(f"Meia-vida Decaimento: {decaimento}; Seu erro: {decaimento_erro}") #Meia vida: 92.46