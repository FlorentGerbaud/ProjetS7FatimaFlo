import numpy as np
import matplotlib.pyplot as plt



# Define the parameters
lambda2 = 2.0  #capacity of acceleration deceleration
h = 1.0  # Time step
T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps
d2=5.0 #security distance
x2_prime_max=100*(1000/3600) #maximum speed of the second car
accident= False

# Initialize arrays to store the results
x1= np.zeros(n_steps)
x2= np.zeros(n_steps)
time = np.zeros(n_steps)
accident=False

# Initial conditions
time[0] = 0.0  # Initial time
x1[0] = 15.0  # Initial value for x1 as specified
x2[0] = 5.0  # Initial value for x2 as specified , we verify also that the security disstance is respected


#def of the function
def x1_prime():
    return 130 *(1000/3600)

#def of the fucntion x2_prime with the special model of exp
def x2_prime(t):
    return x2_prime_max*(1-np.exp((-lambda2/x2_prime_max)*(x1[t]-x2[t]-d2)))


# Euler's explicit method
for t in range(1, n_steps):
    x1[t] = x1[t-1] + x1_prime() * h
    x2[t] = x2[t-1] + x2_prime(t-1) * h
    time[t] = time[t-1] + h

#Verify if we have an accident or not by respecting the security distance
for t in range(0,n_steps):
    if(x1[t]-x2[t]<= d2):
        accident=True
    else:
        accident=False
        

#Plot the results
if(accident==True):
    plt.figure(figsize=(10, 6))
    plt.plot(time[0:t+1], x1[0:t+1], label='x1(t)')
    plt.plot(time[0:t+1], x2[0:t+1], label='x2(t)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)
    plt.show()
else:
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1, label='x1(t)')
    plt.plot(time, x2, label='x2(t)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.title('Euler Explicit Method for x2')
    plt.grid(True)
    plt.show()
    
        


