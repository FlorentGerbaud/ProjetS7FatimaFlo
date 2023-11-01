import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 250, 10)  

def vitesse_exp(V_max, lambda_j, d_j, x):
    v_t = []

    for i in range(len(x)):
        if i == 0:
            v_t.append(0)
        else:
            v_i = V_max * (1 - np.exp(-lambda_j * (x[i - 1] - x[i] - d_j) / V_max))
            v_t.append(v_i)
    return v_t


v1 = vitesse_exp(180,1,10, x)
v2=vitesse_exp(100,0.5,20,x)
plt.plot(x,v1)
plt.plot(x,v2)
plt.xlabel('x')
plt.ylabel('vitesse')
plt.title('Two cars')
plt.grid(True)
plt.show()
