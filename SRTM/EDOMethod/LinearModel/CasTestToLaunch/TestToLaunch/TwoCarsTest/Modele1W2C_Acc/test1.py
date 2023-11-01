import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 250, 10)  

def fct_exp(V_j, lambda_j, d_j, x):
    v_t = []

    for i in range(len(x)):
        if i == 0:
            v_t.append(0)
        else:
            v_i = V_j * (1 - np.exp(-lambda_j * (x[i - 1] - x[i] - d_j) / V_j))
            v_t.append(v_i)
    return v_t

v2 = fct_exp(180, 0.79, 20, x)
plt.plot(x,v2)
plt.show()
