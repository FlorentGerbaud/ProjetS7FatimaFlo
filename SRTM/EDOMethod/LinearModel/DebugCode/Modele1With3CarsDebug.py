#__________________________________________ Importing the required libraries __________________________________________
#______________________________________________________________________________________________________________________

import numpy as np
import matplotlib.pyplot as plt

#_________________________________________________ Defining the parameters  ___________________________________________________
#______________________________________________________________________________________________________________________________

a2 = 2.0  # Capacity of acceleration/deceleration for x2
a3 = 1.0  # Capacity of acceleration/deceleration for x3
h = 1.0  # Time step
T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

#_________________________________________________ Initialise arrays to storing data  ___________________________________________________
#______________________________________________________________________________________________________________________________

x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
x3Pos = np.zeros(n_steps)

v1 = np.zeros(n_steps)
v2 = np.zeros(n_steps)
v3 = np.zeros(n_steps)

time = np.zeros(n_steps)
accident = False

#_________________________________________________ Initialise the arrays with the initial values  ___________________________________________________
#______________________________________________________________________________________________________________________________

time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified
x3Pos[0] = 0.5  # Initial value for x2 as specified

#_________________________________________________ Define the functions  ___________________________________________________
#______________________________________________________________________________________________________________________________

# x1_prime :
# Return : This function returns the speed of x1

def x1_prime():
    return 130 * (1000 / 3600)

# x2_prime :
#input : t : time
# Return : This function returns the speed of x2 at time t

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

# x3_prime :
#input : t : time
# Return : This function returns the speed of x3 at time t

def x3_prime(t):
    return a3 * (x2Pos[t] - x3Pos[t])

# isAccident :
#input : t : time
# Return : This function check all the positions of the cars at time t and returns True if there is an accident

def isAccident(t):
    return (x2Pos[t] >= x1Pos[t] ) or (x3Pos[t] >= x2Pos[t]) 

#_________________________________________________ Resolution of the position for each cars  ___________________________________________________
#______________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    x3Pos[t] = x3Pos[t-1] + x3_prime(t-1) * h
    
    v1[t] = x1_prime()
    v2[t] = x2_prime(t)
    v3[t] = x3_prime(t)
    
    time[t] = time[t-1] + h
    if isAccident(t):
        accident = True
        break

#_________________________________________________ Plotting the results  ___________________________________________________
#______________________________________________________________________________________________________________________________

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

if accident:
    # Plot the distance in the first subplot
    ax1.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
    ax1.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
    ax1.plot(time[0:t+1], x3Pos[0:t+1], label='x3(t)')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Distance')
    ax1.legend()
    ax1.set_title('Accident case')
    ax1.grid(True)

else:
    # Plot the distance in the first subplot
    ax1.plot(time, x1Pos, label='x1(t)')
    ax1.plot(time, x2Pos, label='x2(t)')
    ax1.plot(time, x3Pos, label='x3(t)')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Distance(m)')
    ax1.legend()
    ax1.grid()
    ax1.set_title('position of the cars over time')
 

if(accident):
    #print("There is an accident at time t = ", t*h, "s")
    # Plot the speeds in the second subplot
    ax2.plot(time[0:t+1], v1[0:t+1], label='Speed of x1(t)')
    ax2.plot(time[0:t+1], v2[0:t+1], label='Speed of x2(t)')
    ax2.plot(time[0:t+1], v3[0:t+1], label='Speed of x3(t)')
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('Speed(m/s)')
    ax2.legend()
    ax2.set_title('Speed of Cars Over Time')
    ax2.grid()
else:
    # Plot the speeds in the second subplot
    ax2.plot(time, v1, label='Speed of x1(t)')
    ax2.plot(time, v2, label='Speed of x2(t)')
    ax2.plot(time, v3, label='Speed of x3(t)')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Speed(m/s)')
    ax2.legend()
    ax2.set_title('Speed of Cars Over Time')
    ax2.grid(True)

# Display the subplots side by side
plt.tight_layout()
plt.show()
