#_____________________________________________________ import libraries ______________________________________________________
#________________________________________________________________________________________________________________________

import sys
import numpy as np
import matplotlib.pyplot as plt

#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________

if len(sys.argv) != 7:
    print("Usage: python your_script_name.py a2 h a3")
    sys.exit(1)


accident=False
lambda_2 = float(sys.argv[1])
lambda_3 = float(sys.argv[5])
h = float(sys.argv[2])
d2 = float(sys.argv[3])
d3= float(sys.argv[6])
x2_prime_max=160*(1000/3600) #maximum speed of the second car #maximum speed of the second car
x3_prime_max=140*(1000/3600) #maximum speed of the third car #maximum speed of the second car
nameCaseToLaunch=sys.argv[4]



T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

#__________________________________________Definition and initialization of parameters_____________________________________________#


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
    return 110*(1000/3600)

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

# Check if there is an accident or not
for t in range(n_steps):
    if (x1[t] - x2[t] <= d2) or (x2[t] - x3[t] <= d3):
        accident = True
        t_accident = t
        print("There is an accident in this simulation.")
        print("The moment of the accident is:", t_accident)
        break;
    accident=False
    

    
    

#__________________________________________Plot of solutions____________________________________________#
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# if accident:
#     # Plot the distance in the first subplot
#     ax1.plot(time[0:t+1], x1[0:t+1], label='x1(t)')
#     ax1.plot(time[0:t+1], x2[0:t+1], label='x2(t)')
#     ax1.plot(time[0:t+1], x3[0:t+1], label='x3(t)')
#     ax1.set_xlabel('Time')
#     ax1.set_ylabel('Distance')
#     ax1.legend()
#     ax1.set_title('Accident case')
#     ax1.grid(True)

# else:
#     # Plot the distance in the first subplot
#     ax1.plot(time, x1, label='x1(t)')
#     ax1.plot(time, x2, label='x2(t)')
#     ax1.plot(time, x3, label='x3(t)')
#     ax1.set_xlabel('Time(s)')
#     ax1.set_ylabel('Distance(m)')
#     ax1.legend()
#     ax1.grid()
#     ax1.set_title('Simulation of the Accordion phenomenon')
 

# if(accident):
#     #print("There is an accident at time t = ", t*h, "s")
#     # Plot the speeds in the second subplot
#     ax2.plot(time[0:t+1], x1_prime_values[0:t+1], label='Speed of x1(t)')
#     ax2.plot(time[0:t+1], x2_prime_values[0:t+1], label='Speed of x2(t)')
#     ax2.plot(time[0:t+1], x3_prime_values[0:t+1], label='Speed of x3(t)')
#     ax2.set_xlabel('Time(s)')
#     ax2.set_ylabel('Speed(m/s)')
#     ax2.legend()
#     ax2.set_title('Speed of Cars Over Time')
#     ax2.grid()
# else:
#     # Plot the speeds in the second subplot
#     ax2.plot(time, x1_prime_values, label='Speed of x1(t)')
#     ax2.plot(time, x2_prime_values, label='Speed of x2(t)')
#     ax2.plot(time, x3_prime_values, label='Speed of x3(t)')
#     ax2.set_xlabel('Time')
#     ax2.set_ylabel('Speed(m/s)')
#     ax2.legend()
#     ax2.set_title('Simulation of the Accordion phenomenon')
#     ax2.grid(True)

# #Display the plots
# plt.show()

# print(x1[-1]-x2[-1])
# print("sitance entre x2 et x3 : ",x2[-1]-x3[-1])

if accident:
    # Plot the distance in the first subplot
    plt.plot(time[0:t+1], x1[0:t+1], label='$x_1(t)$')
    plt.plot(time[0:t+1], x2[0:t+1], label='$x_2(t)$')
    plt.plot(time[0:t+1], x3[0:t+1], label='$x_3(t)$')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)

else:
    # Plot the distance in the first subplot
    plt.plot(time, x1, label='$x_1(t)$')
    plt.plot(time, x2, label='$x_2(t)$')
    plt.plot(time, x3, label='$x_3(t)$')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.grid()
    plt.title('Position of the cars over time')

# Display the plot
plt.show()