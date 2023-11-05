import numpy as np
import matplotlib.pyplot as plt



#________________________________________Definition and initialization of the parameters________________________________________#

lambda2 = 10.0  #Acceleration/Deceleration capacity
h = 1.0  # Time step
T = 50.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps
d2=3.0 #Security distance
x2_prime_max=160*(1000/3600) #Maximum speed of the second car
accident=False #Flag to indicate if an accident has occurred

# Initialize arrays to store the results
x1= np.zeros(n_steps) #Array to store the position of the first car
x2= np.zeros(n_steps) #Array to store the position of the second car
time = np.zeros(n_steps) #Array to store the time values
x1_prime_values = np.zeros(n_steps) #Array to store the speed values of the first ca
x2_prime_values = np.zeros(n_steps) #Array to store the speed values of the second car


# Initial conditions
time[0] = 0.0  # Initial time
x1[0] = 3.0  # Initial value for x1 as specified
x2[0] = 1.0  # Initial value for x2 as specified, we also verify that the security distance is respected

#________________________________________Definition of the functions________________________________________#

#Definition of the function to calculate x1's speed
def x1_prime():
    return 110 *(1000/3600)

#Definition of the function to calculate x2's speed with a special exponential model
def x2_prime(t):
    return x2_prime_max*(1-np.exp((-lambda2/x2_prime_max)*(x1[t]-x2[t]-d2)))


# Euler's explicit method
for t in range(1, n_steps):
    x1_prime_values[t] = x1_prime()  #Store the speed values of x1
    x2_prime_values[t] = x2_prime(t-1)  #Store the speed values of x2
    x1[t] = x1[t-1] + x1_prime() * h
    x2[t] = x2[t-1] + x2_prime(t-1) * h
    time[t] = time[t-1] + h
    if(x1[t-1]-x2[t-1]<= d2 ): #Verify if the security distance is respected 
        accident=True
        print(t)
        print(accident)
        
    

#________________________________________Displaying the simulation results________________________________________#
   
# Display the results in side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Subplot for positions
axes[0].plot(time, x1, label='x1(t)')
axes[0].plot(time, x2, label='x2(t)')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Position (m)')
axes[0].legend()
axes[0].set_title('Positions')
axes[0].grid(True)

# Subplot for velocities
axes[1].plot(time, x1_prime_values, label="x1'(t)")
axes[1].plot(time, x2_prime_values, label="x2'(t)")
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Velocity (m/s)')
axes[1].legend()
axes[1].set_title('Velocities')
axes[1].grid(True)

#Display the plots
plt.show()

