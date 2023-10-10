import numpy as np
import matplotlib.pyplot as plt



# Define the parameters
a2 = 2.0  #capacity of acceleration deceleration
a3= 1.0
h = 1.0  # Time step
T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

# Initialize arrays to store the results
x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
x3Pos = np.zeros(n_steps)
time = np.zeros(n_steps)
accident=False

# Initial conditions
time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified
x3Pos[0] = 0.5  # Initial value for x2 as specified

#def of the function

def x1_prime():
    return 130 * (1000 / 3600)

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

def x3_prime(t):
    return a3 * (x2Pos[t] - x3Pos[t])

# Euler's explicit method
for t in range(1, n_steps):
    
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    x3Pos[t] = x3Pos[t-1] + x3_prime(t-1) * h
    time[t] = time[t-1] + h
    if(x2Pos[t] >= x1Pos[t]):
        accident=True
        break
        
print(t)

if(accident==True):
    plt.figure(figsize=(10, 6))
    plt.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
    plt.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
    plt.plot(time[0:t+1], x3Pos[0:t+1], label='x3(t)')
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)
    plt.show()
else:
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1Pos, label='x1(t)')
    plt.plot(time, x2Pos, label='x2(t)')
    plt.plot(time, x3Pos, label='x3(t)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.title('Euler Explicit Method for x2\' = a2(x1(t) - x2(t)) with Constant x1\'')
    plt.grid(True)
    plt.show()


# Initialize arrays to store the speeds of the cars
v1 = np.zeros(n_steps)
v2 = np.zeros(n_steps)
v3 = np.zeros(n_steps)

# Calculate speeds
for t in range(1, n_steps):
    v1[t] =  x1_prime()
    v2[t] = (x2Pos[t] - x2Pos[t-1]) 
    v3[t] = (x3Pos[t] - x3Pos[t-1]) 

# Plot the speeds
plt.figure(figsize=(10, 6))
plt.plot(time, v1, label='Speed of x1(t)')
plt.plot(time, v2, label='Speed of x2(t)')
plt.plot(time, v3, label='Speed of x3(t)')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.legend()
plt.title('Speed of Cars Over Time')
plt.grid(True)
plt.show()