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

#Display the plots
plt.show()

print(x1[-1]-x2[-1])
print("sitance entre x2 et x3 : ",x2[-1]-x3[-1])


#_________________________________________________ Stability study  ___________________________________________________
#


def d1_equilibrium():
       return -(x2_prime_max/lambda_2)*np.log(((x2_prime_max-x1_prime())/x2_prime_max)*np.exp(-(lambda_2*d2/x2_prime_max)))


def d2_equilibrium():
    result = - (x3_prime_max / lambda_3) * np.log(
    (-x3_prime_max + x2_prime_max - x2_prime_max * np.exp((-lambda_2 / x2_prime_max) * d1_equilibrium()) * np.exp((lambda_2 / x2_prime_max) * d2))
    / (-x3_prime_max) * np.exp((-lambda_3 / x3_prime_max) * d3)
    )
    return result

print("e1 : ",d1_equilibrium())
print("e2 : ", d2_equilibrium())


#_________________________________________________ Plotting the vector field  ___________________________________________________
#______________________________________________________________________________________________________________________________

v1=x1_prime()

# Define the vector field function
def system(x2_prime_max, x3_prime_max, lambda_2, lambda_3, d2, D1, D2, d3):
    d1_dot = x1_prime() - x2_prime_max + x2_prime_max * np.exp((-lambda_2 * (D1 - d2)) / x2_prime_max)
    d2_dot = x2_prime_max - x2_prime_max * np.exp((-lambda_2 * (D1 - d2)) / x2_prime_max) - x3_prime_max + x3_prime_max * np.exp((-lambda_3 * (D2 - d3)) / x3_prime_max)
    return d1_dot, d2_dot


# Equilibrium point
equilibrium_x = d1_equilibrium()
equilibrium_y = d2_equilibrium()

# Create a grid of (x, y) values
x = np.linspace(equilibrium_x - 5, equilibrium_x + 5, 20)
y = np.linspace(equilibrium_y - 5, equilibrium_y + 5, 20)
X, Y = np.meshgrid(x, y)

# Initialize arrays for vector field components
U = np.zeros_like(X)
V = np.zeros_like(Y)

# Calculate vector field values at each point in the grid
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        d1_dot, d2_dot = system(x2_prime_max, x3_prime_max, lambda_2, lambda_3, d2, X[i, j], Y[i, j], d3)
        U[i, j] = d1_dot
        V[i, j] = d2_dot

# Create a figure with adjusted size
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('white')

# Plot the vector field with a higher scale value for better visualization
ax.quiver(X, Y, U, V, color='blue', angles='xy', scale_units='xy', scale=40)
ax.plot(equilibrium_x, equilibrium_y, 'ro', label='Equilibrium Point')
ax.set_xlabel('d1')
ax.set_ylabel('d2')
ax.set_title('Vector Field for ODE System with Equilibrium Point')
ax.legend()
ax.grid(True)

plt.show()