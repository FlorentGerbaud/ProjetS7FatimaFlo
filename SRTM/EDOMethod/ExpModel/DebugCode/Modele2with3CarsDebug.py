import numpy as np
import matplotlib.pyplot as plt

#__________________________________________Definition and initialization of parameters_____________________________________________#

h=1.0 #Time step
T=50.0 #Total simulation steps
n_steps=int(T/h) #Tumber of time steps
accident=False

#Parameters for car 2
lambda_2=10.0 #Capacity of acceleration/deceleration 
x2_prime_max=160*(1000/3600) #Maximum speed 
d2=1.0 #Security distance

#Parameters for car 3
lambda_3=5.0 #Capacity of acceleration/deceleration 
x3_prime_max=180*(1000/3600) #Maximum speed 
d3=2.0 #Security distance

#Positions: x1,x2 et x3
x1=np.zeros(n_steps)
x2=np.zeros(n_steps)
x3=np.zeros(n_steps)

#Initialisation of positions
x1[0]=6.0
x2[0]=4.0 #respecting d2
x3[0]=1.0 #respecting d3

#Time 
time=np.zeros(n_steps) 
time[0]=0.0

#Velocities: 
x1_prime_values = np.zeros(n_steps)
x2_prime_values = np.zeros(n_steps)
x3_prime_values = np.zeros(n_steps)

#_____________________________________________________Definition of functions_________________________________________________________#

#Definition of x1's speed function
def x1_prime():
    return 120*(1000/3600)

# Definition of x2's speed function using a special exponential model
def x2_prime(t):
    return x2_prime_max*(1-np.exp((-lambda_2/x2_prime_max)*(x1[t]-x2[t]-d2)))

# Definition of x3's speed function using a special exponential model
def x3_prime(t):
    return x3_prime_max*(1-np.exp((-lambda_3/x3_prime_max)*(x2[t]-x3[t]-d3)))

#Euler implicite
for t in range(1, n_steps):
    x1_prime_values[t] = x1_prime()  #Store the speed values of x1
    x2_prime_values[t] = x2_prime(t-1)  #Store the speed values of x1
    x3_prime_values[t] = x3_prime(t-1)  #Store the speed values of x1

    x1[t] = x1[t-1] + x1_prime() * h
    x2[t] = x2[t-1] + x2_prime(t-1) * h
    x3[t] = x3[t-1] + x3_prime(t-1) * h
    time[t] = time[t-1] + h
    
    

#__________________________________________Plot of solutions____________________________________________#
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Subplot for positions
axes[0].plot(time, x1, label='x1(t)')
axes[0].plot(time, x2, label='x2(t)')
axes[0].plot(time, x3, label='x3(t)')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Position (m)')
axes[0].legend()
axes[0].set_title('Positions')
axes[0].grid(True)

# Subplot for velocities
axes[1].plot(time, x1_prime_values, label="x1'(t)")
axes[1].plot(time, x2_prime_values, label="x2'(t)")
axes[1].plot(time, x3_prime_values, label="x3'(t)")
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Velocity (m/s)')
axes[1].legend()
axes[1].set_title('Velocities')
axes[1].grid(True)

plt.show()






