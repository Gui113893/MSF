import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 48 , 96, 144, 192, 240, 288, 336, 384])
valores = np.array([10.03, 7.06, 4.88, 3.38, 2.26, 1.66, 1.14, 0.79, 0.58])

data_points = np.size(t)

mul_sum = np.sum(np.multiply(t, valores))

x_sum = np.sum(t)
y_sum = np.sum(valores)

m_numerator = data_points * mul_sum - x_sum * y_sum

x2_sum = np.sum(np.square(t))
x_sum2 = np.square(np.sum(t))

x_denom = data_points * x2_sum - x_sum2

m = m_numerator / x_denom   #Declive

b = (x2_sum * y_sum - x_sum * mul_sum) / x_denom  #Ordenada na origem

y2_sum = np.sum(np.square(valores))
y_sum2 = np.square(np.sum(valores))

y_denom = data_points * y2_sum - y_sum2

r2 = m_numerator**2 / (x_denom * y_denom)  #Coeficiente de Determinação

#Erros
delta_m = np.absolute(m) * np.sqrt((1 / r2 - 1) / (data_points - 2))

delta_b = delta_m * np.sqrt(x2_sum / data_points)

plt.figure(1)
plt.title("Gráfico Relação Linear")
plt.xlabel("t(h)")
plt.ylabel("atividade(mBq)")
plt.plot(t, valores, "go")
plt.plot(t, m*t + b)
print("Coeficiente de Determinação: ", r2) #r2= 0.86
plt.show()

#A relação entre a atividade e o tempo não é linear pois o valor do coeficiente de determinação está longe de 1
