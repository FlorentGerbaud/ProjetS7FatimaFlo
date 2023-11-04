#__________________________________________ Importing the required libraries __________________________________________
#______________________________________________________________________________________________________________________

import sys
import numpy as np
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

# system :
#input : d1 : distance between x1 and x2
#        d2 : distance between x2 and x3
#        a2 : capacity of acceleration/deceleration for x2
#        a3 : capacity of acceleration/deceleration for x3
#        v1 : max speed of x1
# Return : This function returns the variation of the speed between x1 and x2 and the variation of the speed between x2 and x3

def system(D1, D2, a2, a3, v1):
    d1_dot = v1 - a2 * D1
    d2_dot = a2 * D1 - a3 * D2
    return d1_dot, d2_dot

# C1 :
#input : d1_0 : initial distance between x1 and x2
#        a2 : capacity of acceleration/deceleration for x2
#        V1 : max speed of x1
# Return : This function returns the constant C1

def C1(d1_0,a2,V1):
    return (d1_0*a2-V1)/(a3-a2)

# C2 : 
#input : d2_0 : initial distance between x2 and x3
#        a3 : capacity of acceleration/deceleration for x3
#        V1 : max speed of x1
#        d1_0 : initial distance between x1 and x2
#        a2 : capacity of acceleration/deceleration for x2
# Return : This function returns the constant C2

def C2(d2_0,a3,V1,d1_0,a2):
    return d2_0- (V1/a3) - C1(d1_0,a2,V1)

# d1 :
#input : t_values : time values
#        d1_0 : initial distance between x1 and x2
#        a2 : capacity of acceleration/deceleration for x2
#        a3 : capacity of acceleration/deceleration for x3
#        V1 : max speed of x1
# Return : This function returns the distance between x1 and x2 at time t

def d1(t_values,d1_0,a2,a3,V1):
    return [(C1(d1_0,a2,v1)*(a3-a2))/(a2*np.exp(a2*t)) + (V1/a2) for t in t_values]

# d2 :
#input : t_values : time values
#        d2_0 : initial distance between x2 and x3
#        a2 : capacity of acceleration/deceleration for x2
#        a3 : capacity of acceleration/deceleration for x3
#        V1 : max speed of x1
#        d1_0 : initial distance between x1 and x2
# Return : This function returns the distance between x2 and x3 at time t

def d2(t_values,d2_0,a2,a3,V1,d1_0):
    return [C1(d1_0,a2,v1)*np.exp(-a2*t) + C2(d2_0,a3,v1,d1_0,a2)*np.exp(-a3*t) + (V1/a3) for t in t_values]

#_________________________________________________ Resolution of the position for each cars  ___________________________________________________
#_______________________________________________________________________________________________________________________________________________    

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

if isDebug:
    print("The distance between x1 and x2 is : ", x1Pos[-1] - x2Pos[-1], "m")
    print("The distance between x2 and x3 is : ", x2Pos[-1] - x3Pos[-1], "m")

plt.show()

#_________________________________________________ Plotting the vector field  ___________________________________________________
#______________________________________________________________________________________________________________________________

v1=x1_prime()

#___eqquilibrium point____

equilibrium_x = v1 / a2
equilibrium_y = v1 / a3

#___ Create a grid of (x, y) values ___

x = np.linspace(equilibrium_x - 10, equilibrium_x + 10, 20)
y = np.linspace(equilibrium_y - 10, equilibrium_y + 10, 20)
X, Y = np.meshgrid(x, y)

#___  Initialize arrays for vector field components ___ 

U = np.zeros_like(X)
V = np.zeros_like(Y)

#___   Calculate vector field values at each point in the grid ___

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        d1_dot, d2_dot = system(X[i, j], Y[i, j], a2, a3, v1)
        U[i, j] = d1_dot
        V[i, j] = d2_dot

#___  Create a figure ___

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('white')

#___  Plot the vector field ___

ax.quiver(X, Y, U, V, color='blue', angles='xy', scale_units='xy', scale=10)
ax.plot(equilibrium_x, equilibrium_y, 'ro', label='Equilibrium Point')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Vector Field for ODE System with Equilibrium Point')
ax.legend()
ax.grid(True)

plt.show()

#_________________________________________________ Plotting the Analitycal solutions of the systems  ___________________________________________________
#______________________________________________________________________________________________________________________________

d1_0=x1Pos[0]-x2Pos[0]
d2_0=x2Pos[0]-x3Pos[0]
t_values = np.linspace(0, 10, 100)

d1_t=d1(t_values,d1_0,a2,a3,v1)
d2_t=d2(t_values,d2_0,a2,a3,v1,d1_0)

# Plot the x and y values
plt.figure(figsize=(8, 6))
plt.plot(t_values, d1_t, label='x(t)')
plt.plot(t_values, d2_t, label='y(t)')
plt.xlabel('t')
plt.ylabel('x(t) and y(t)')
plt.legend()
plt.title('Plot of x(t) and y(t)')
plt.grid(True)
plt.show()


