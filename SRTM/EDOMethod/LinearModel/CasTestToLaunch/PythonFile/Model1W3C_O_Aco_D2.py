#__________________________________________ Importing the required libraries __________________________________________
#______________________________________________________________________________________________________________________

import sys
import numpy as np
import random   
import matplotlib.pyplot as plt
isDebug=False
# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5:
    print("Usage: python your_script_name.py a2 h")
    sys.exit(1)


#_________________________________________________ Defining the parameters  ___________________________________________________
#______________________________________________________________________________________________________________________________


accident=False
a2 = float(sys.argv[1])
a3 = float(sys.argv[3])
h = float(sys.argv[2])
nameCaseToLaunch=sys.argv[4]
T = 50.0  # Total simulation time
V1max = 130 * (1000 / 3600)  # Maximum speed of x1
n_steps = int(T / h)  # Number of time steps


#_________________________________________________ Initialise arrays to storing data  ___________________________________________________
#______________________________________________________________________________________________________________________________

x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
x3Pos = np.zeros(n_steps)
a2Val = np.zeros(n_steps)

v1 = np.zeros(n_steps)
v2 = np.zeros(n_steps)
v3 = np.zeros(n_steps)

time = np.zeros(n_steps)
accident = False

#_________________________________________________ Initialise the arrays with the initial values  ___________________________________________________
#______________________________________________________________________________________________________________________________

time[0] = 0.0  # Initial time
x1Pos[0] = 80.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified
x3Pos[0] = 0.5  # Initial value for x2 as specified
a2Val[0] = a2

#_________________________________________________ Define the functions  ___________________________________________________
#______________________________________________________________________________________________________________________________

# sinusoidal_model :
#input : W : Amplitude of the perturbation
#        omega : Angular frequency
#        t : time
#        phi : Phase (in radians)
# Return : This function return a value of acceleration which follows a sinusoidal model with random noise

def sinusoidal_model(W, omega, t, phi):
    return abs(W * np.sin(omega * t + phi) + np.random.normal(0, 0.1)) #random noise

# x1_prime :
# Return : This function returns the speed of x1

def x1_prime():
    return V1max

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

# obstacle :
#input : t : time
# Return : This function returns the new speed of x1 if there is an obstacle where the obstacle appears randomly

def obstacle(t):
    V1max_initial = 130 * (1000 / 3600)
    base_interval = 10  # Durée de base entre les apparitions d'obstacles en secondes
    reduction_factor = 0.4  # Facteur de réduction de la vitesse maximale

    # Utiliser un générateur de nombres aléatoires pour introduire de l'aléatoire dans les intervalles
    random.seed(t)  # Utilisez le temps actuel t comme graine

    if random.random() < 0.2:  # 50% de chance d'avoir un obstacle
        V1max = V1max_initial * reduction_factor
    else:
        V1max = V1max_initial

    return V1max

# VariationsOfComportment :
#input : criticalDistance : critical distance between the cars
#        boringDistance : distance when we can accelerate
#        t : time
# Return : This function returns the new values of a2 and a3 according to the distance between the cars

def VariationsOfComportment(criticalDistance, boringDistance,t):
    W = 1.1  # Amplitude de la perturbation
    omega = 2.0  # Fréquence angulaire
    phi = np.pi / 4  # Phase (en radians)
    a2 = 0
    a3 = 0
    delta = 0.0008  # Calculate the increment per unit distance

    d1 = x1Pos[t] - x2Pos[t]
    d2 = x2Pos[t] - x3Pos[t]

    if d1 <= criticalDistance:
        a2 = 0
    elif d1 >= boringDistance:
        # model with constant acceleration :
        #a2 = 0.5
        #_______________________________________
        
        a2=sinusoidal_model(W, omega, t, phi) 

    if d2 <= criticalDistance:
        a3 = 0
    elif d2 >= boringDistance:
        a3=0.9
        #a3=sinusoidal_model(0.9, omega, t, phi) 

    if isDebug:
        print("a2= ", a2)
        print("a3= ", a3)

    if isDebug:
        print("d1= ", d1, "d2= ", d2)
    a2Val[t]=a2

    return a2, a3


#_________________________________________________ Resolution of the position for each cars  ___________________________________________________
#______________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    x3Pos[t] = x3Pos[t-1] + x3_prime(t-1) * h
    
    if(isDebug):
        print("a2= ", a2, "a3= ", a3)
    a2,a3=VariationsOfComportment(1,73,t)
    V1max=obstacle(t)
    
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
    ax1.set_title(nameCaseToLaunch)
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
    ax1.set_title(nameCaseToLaunch)
 

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

# Create a line plot
if accident:
    plt.plot(time[0:t+1], a2Val[0:t+1], marker='o', linestyle='-', color='b', label='Alpha Values')
    plt.xlabel('Time')
    plt.ylabel('Alpha Values')
    plt.title('Alpha Values Over Time')
    plt.grid(True)
    plt.legend()
    plt.show()
else:
    plt.plot(time, a2Val, marker='o', linestyle='-', color='b', label='Alpha Values')
    plt.xlabel('Time')
    plt.ylabel('Alpha Values')
    plt.title('Alpha Values Over Time')
    plt.grid(True)
    plt.legend()
    plt.show()

