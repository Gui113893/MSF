import math
import numpy as np
import matplotlib.pyplot as plt



def main():
    x = [222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]
    y = [2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]
    xy = [x[i]*y[i] for i in range(len(x))]
    x2 = [x[i]**2 for i in range(len(x))]
    y2 = [y[i]**2 for i in range(len(x))]
    N = len(x)

    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(xy)
    sumx2 = sum(x2)
    sumy2 = sum(y2)

    m = ((N*sumxy - (sumx*sumy)) /  (N*sumx2 - (sumx)**2))
    b = ((sumx2*sumy - sumx*sumxy)/(N*sumx2 - (sumx **2)))
    r = math.sqrt(((N*sumxy - sumx*sumy)**2)/((N*sumx2 - (sumx**2))*(N*sumy2 - (sumy**2))))

    delta_m = abs(m)*math.sqrt((1/r**2 - 1)/(N - 2))
    delta_b = delta_m*math.sqrt(sumx2/N)

    print(sumxy)
    print(sumx)
    print(sumy)
    print(sumx2)
    print(sumy2)
    print(m)
    print(delta_m)
    print(b)
    print(delta_b)
    print(r**2)

    plt.plot(x, y, "s")
    plt.show()


if __name__ == "__main__":
    main()