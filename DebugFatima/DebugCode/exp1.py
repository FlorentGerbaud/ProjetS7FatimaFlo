import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(0, 250, 10)  
# ce que j'aurais fait 
#deinir les deux tableaux x1 et x2 position des deux voitures
#definir la fct x1_prime et x2_prime les fcts qui calcule la vitesse (comme sur la feuille)
#implémenter euler Explicite
x1=np.zeros(10)
x2=np.zeros(10)
t=np.zeros(10)
h=1


###########################################################################################################

#def x1_prime():
#    return V1 #tu retourne une vitessse constante comme t'est au tn

#def x2_prime():
#    return x_2_prime

#implémentation de euler explicite

#si tu veux visualiser la vitesse tu peux le faire grace aux x1_prime et x2_prime mais tu est obligé de calculer la position

###########################################################################################################

##################### ca pour moi tu en a pas besoin mais si tu pense en avoir besoin tu peux l'utiliser #####################

#Afunction to evaluate the speech for each car


# def vitesse_exp(V_max, lambda_j, d_j, x):
    
#     v_t = []
    
#     for i in range(len(x)):
#         if i == 0:
#             v_t.append(0)#at the beginnig the speed is 0
#         else:
#             #we calculate the speed in each point x[i]
#             v_i = V_max * (1 - np.exp(-lambda_j * (x[i-1] - x[i] - d_j) / V_max))
#             v_t.append(v_i)
#     return v_t

# #evalute the speed for the first car, which its Vmax=180,lambda=1 and d=10 
# v1 = vitesse_exp(70,0.3,30, x)
# #evalute the speed for the first car, which its Vmax=100,lambda=0.5 and d=20 
# v2=vitesse_exp(60,0.2,20,x)
#for the two cases we have x[i-1]-x[i]<dj
#on a toujours des vitesses négatives ?? Problème à résoudre
plt.plot(x,v1)
plt.plot(x,v2)
plt.xlabel('x')
plt.ylabel('Speed')
plt.title('Two cars')
plt.grid(True)
#plt.show()
