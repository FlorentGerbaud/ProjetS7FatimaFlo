#__________________________________________ Importing the required libraries __________________________________________
#______________________________________________________________________________________________________________________

import sys
import numpy as np
import matplotlib.pyplot as plt
isDebug=False
#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________
print("ici")
if len(sys.argv) != 7:
    print("Usage: python your_script_name.py a2 h a3")
    sys.exit(1)


accident=False
a2 = float(sys.argv[1])
a3 = float(sys.argv[5])
h = float(sys.argv[2])
d2 = float(sys.argv[3])
d3= float(sys.argv[6])
V1max=120*(1000/3600) #maximum speed of the first car
V2max=160*(1000/3600) #maximum speed of the second car #maximum speed of the second car
V3max=180*(1000/3600) #maximum speed of the third car #maximum speed of the second car
nameCaseToLaunch=sys.argv[4]



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
x1Pos[0] = 6.0  # Initial value for x1 as specified
x2Pos[0] = 4.0  # Initial value for x2 as specified
x3Pos[0] = 1.0  # Initial value for x2 as specified

#_________________________________________________ Define the functions  ___________________________________________________
#______________________________________________________________________________________________________________________________

# x1_prime :
# Return : This function returns the speed of x1

def x1_prime():
    return V1max

# Definition of x2's speed function using a special exponential model
def x2_prime(t):
    return V2max*(1-np.exp((-a2/V2max)*(x1Pos[t]-x2Pos[t]-d2)))

# Definition of x3's speed function using a special exponential model
def x3_prime(t):
    return V3max*(1-np.exp((-a3/V3max)*(x2Pos[t]-x3Pos[t]-d3)))

# isAccident :
#input : t : time
# Return : This function check all the positions of the cars at time t and returns True if there is an accident

def isAccident(t):
    return (x2Pos[t] >= x1Pos[t] ) or (x3Pos[t] >= x2Pos[t]) 

def obstacle(t):
    V1max=0
    if (t%10==0):
        V1max=V1max*0.40
    else:
        V1max=130 * (1000 / 3600)
    return V1max

def VariationsOfComportment(criticalDistance,boringDistance):
    a2=0
    a3=0
    if(x1Pos[t] - x2Pos[t] <= criticalDistance):
        a2 = 15.0
        if(isDebug):
            print("a2= ", a2)
    elif(x1Pos[t] - x2Pos[t] >= boringDistance):
        a2 = 16.0
        if(isDebug):
            print("a2= ", a2)
    elif(x2Pos[t] - x3Pos[t] <= criticalDistance):
        a3 = 3.5
        if(isDebug):
            print("a3= ",a3)
    elif(x2Pos[t] - x3Pos[t] >= boringDistance):
        a3 = 4.0
        if(isDebug):
            print("a3= ",a3)
    if(isDebug):
        print("d1= ", x1Pos[t] - x2Pos[t], "d2= ",x2Pos[t] - x3Pos[t])
    return a2,a3

#_________________________________________________ Resolution of the position for each cars  ___________________________________________________
#______________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    x3Pos[t] = x3Pos[t-1] + x3_prime(t-1) * h
    
    if(isDebug):
        print("a2= ", a2, "a3= ", a3)
    a2,a3=VariationsOfComportment(1,20)
    #V1max=obstacle(t)
    
    v1[t] = x1_prime()
    v2[t] = x2_prime(t)
    v3[t] = x3_prime(t)
    
    time[t] = time[t-1] + h
    if isAccident(t):
        accident = True
        break

#_________________________________________________ Plotting the results  ___________________________________________________
#______________________________________________________________________________________________________________________________

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# if accident:
#     # Plot the distance in the first subplot
#     ax1.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
#     ax1.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
#     ax1.plot(time[0:t+1], x3Pos[0:t+1], label='x3(t)')
#     ax1.set_xlabel('Time')
#     ax1.set_ylabel('Distance')
#     ax1.legend()
#     ax1.set_title(nameCaseToLaunch)
#     ax1.grid(True)

# else:
#     # Plot the distance in the first subplot
#     ax1.plot(time, x1Pos, label='x1(t)')
#     ax1.plot(time, x2Pos, label='x2(t)')
#     ax1.plot(time, x3Pos, label='x3(t)')
#     ax1.set_xlabel('Time(s)')
#     ax1.set_ylabel('Distance(m)')
#     ax1.legend()
#     ax1.grid()
#     ax1.set_title(nameCaseToLaunch)
 

# if(accident):
#     #print("There is an accident at time t = ", t*h, "s")
#     # Plot the speeds in the second subplot
#     ax2.plot(time[0:t+1], v1[0:t+1], label='Speed of x1(t)')
#     ax2.plot(time[0:t+1], v2[0:t+1], label='Speed of x2(t)')
#     ax2.plot(time[0:t+1], v3[0:t+1], label='Speed of x3(t)')
#     ax2.set_xlabel('Time(s)')
#     ax2.set_ylabel('Speed(m/s)')
#     ax2.legend()
#     ax2.set_title('Speed of Cars Over Time')
#     ax2.grid()
# else:
#     # Plot the speeds in the second subplot
#     ax2.plot(time, v1, label='Speed of x1(t)')
#     ax2.plot(time, v2, label='Speed of x2(t)')
#     ax2.plot(time, v3, label='Speed of x3(t)')
#     ax2.set_xlabel('Time')
#     ax2.set_ylabel('Speed(m/s)')
#     ax2.legend()
#     ax2.set_title('Speed of Cars Over Time')
#     ax2.grid(True)

# # Display the subplots side by side
# plt.tight_layout()
# plt.show()

if accident:
    # Plot the distance in the first subplot
    plt.plot(time[0:t+1], x1Pos[0:t+1], label='$x_1(t)$')
    plt.plot(time[0:t+1], x2Pos[0:t+1], label='$x_2(t)$')
    plt.plot(time[0:t+1], x3Pos[0:t+1], label='$x_3(t)$')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)

else:
    # Plot the distance in the first subplot
    plt.plot(time, x1Pos, label='$x_1(t)$')
    plt.plot(time, x2Pos, label='$x_2(t)$')
    plt.plot(time, x3Pos, label='$x_3(t)$')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.grid()
    plt.title('Position of the cars over time')

# Display the plot
plt.show()