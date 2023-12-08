#_____________________________________________________ import libraries ______________________________________________________
#________________________________________________________________________________________________________________________

import sys
import numpy as np
import matplotlib.pyplot as plt


#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________

if len(sys.argv) != 5:
    print("Usage: python your_script_name.py a2 h a3")
    sys.exit(1)


accident=False
lambda2 = float(sys.argv[1])
h = float(sys.argv[2])
d2 = float(sys.argv[3])
x2_prime_max=160*(1000/3600) #maximum speed of the second car #maximum speed of the second car
nameCaseToLaunch=sys.argv[4]



T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________


#____________________________________________ initialise arrays to storing data  ____________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________ 

x1= np.zeros(n_steps)
x2= np.zeros(n_steps)
time = np.zeros(n_steps)
x1_prime_values = np.zeros(n_steps)
x2_prime_values = np.zeros(n_steps)
accident=False

#______________________________________________ intialise the arrays with the initial conditions  ________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________

time[0] = 0.0  # Initial time
x1[0] = 3.0  # Initial value for x1 as specified
x2[0] = 1.0  # Initial value for x2 as specified , we verify also that the security disstance is respected


#_________________________________________________ Define the functions  ___________________________________________________
#______________________________________________________________________________________________________________________________

# x1_prime :
# Return : This function returns the speed of x1

def x1_prime():
    return 110 *(1000/3600)

# x2_prime :
#input : t : time
# Return : This function returns the speed of x2 at time t

def x2_prime(t):
    return x2_prime_max*(1-np.exp((-lambda2/x2_prime_max)*(x1[t]-x2[t]-d2)))

def d1_equilibrium():
       return -(x2_prime_max/lambda2)*np.log(((x2_prime_max-x1_prime())/x2_prime_max)*np.exp(-(lambda2*d2/x2_prime_max)))


#_________________________________________________ Resolution of the position for each cars  ___________________________________________________
#______________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    x1_prime_values[t] = x1_prime()  # Stocker les valeurs de vitesse de x1
    x2_prime_values[t] = x2_prime(t-1)  # Stocker les valeurs de vitesse de x2
    x1[t] = x1[t-1] + x1_prime_values[t] * h
    x2[t] = x2[t-1] + x2_prime_values[t] * h
    time[t] = time[t-1] + h
    if(x1[t]-x2[t]<= d2 ):
        accident=True
        break
    

#_________________________________________________ Plotting the results  ___________________________________________________
#______________________________________________________________________________________________________________________________

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

if accident:
    # Plot the distance in the first subplot
    ax1.plot(time[0:t+1], x1[0:t+1], label='x1(t)')
    ax1.plot(time[0:t+1], x2[0:t+1], label='x2(t)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Distance (m/s)')
    ax1.legend()
    ax1.set_title(nameCaseToLaunch)
    ax1.grid(True)

else:
    # Plot the distance in the first subplot
    ax1.plot(time, x1, label='x1(t)')
    ax1.plot(time, x2, label='x2(t)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Distance (m)')
    ax1.legend()
    ax1.grid()
    ax1.set_title(nameCaseToLaunch)
 

if(accident):
    #print("There is an accident at time t = ", t*h, "s")
    # Plot the speeds in the second subplot
    ax2.plot(time[0:t+1], x1_prime_values[0:t+1], label='Speed of x1(t)')
    ax2.plot(time[0:t+1], x2_prime_values[0:t+1], label='Speed of x2(t)')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Speed (m/s)')
    ax2.legend()
    ax2.set_title('Evolution of the speed of the cars over time')
    ax2.grid()
else:
    # Plot the speeds in the second subplot
    ax2.plot(time, x1_prime_values, label='Speed of x1(t)')
    ax2.plot(time, x2_prime_values, label='Speed of x2(t)')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Speed (m/s)')
    ax2.legend()
    ax2.set_title('Evolution of the speed of the cars over time')
    ax2.grid(True)

# Display the subplots side by side
plt.tight_layout()
plt.show()

print("distance between the two cars at the end of the simulation : ", x1[t]-x2[t], "m")

#___________________________________ Plotting the vector field ______________________________________________________
#____________________________________________________________________________________________________________________

# Define the vector field function
def d1_point(f, t):
    return x1_prime() - x2_prime_max + x2_prime_max * np.exp((-lambda2 * (f - d2)) / x2_prime_max)

# Define or import x1_prime(), lambda2, d2, x2_prime_max, and d1_equilibrium() as needed.

# Create the vector field plot
f = np.linspace(0, 100, 20)
t = np.linspace(0, 25, 20)
F, T = np.meshgrid(f, t)

# Calculate the derivatives for the existing 'f' values
df = d1_point(F, T)
dt = np.ones_like(df)

# Normalize the vectors for plotting
length = np.sqrt(df**2 + dt**2)
df /= length
dt /= length

# Create the vector field plot with an increased scale value
plt.figure(figsize=(8, 6))
plt.quiver(T, F, dt, df, angles='xy', scale=100, color='blue')  # Adjust the scale value as needed

# Add the red line f(t) = d1_point
plt.plot(t, x1_prime() / lambda2 * np.ones_like(t), 'r', label=f'$d_1^*$ = $-\\frac{{V_2}}{{\\lambda_2}}\\ln \\left(\\frac{{V_2-V_1}}{{V_2}}e^{{-\\frac{{\\alpha_2}}{{V_2}}d_2}} \\right)$ = {d1_equilibrium()}')


plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')

plt.title('Vector Field for ' + r"$\dot{d}_1 = V_1 - V_2 + V_2 \cdot e^{-\frac{\alpha \cdot (d_1 - d_2)}{V_2}}$")
plt.legend()
plt.grid()
plt.show()