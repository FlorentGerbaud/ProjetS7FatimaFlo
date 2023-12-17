import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 

isBOundaryCOnd=False

# Parameters for the simulation
deltaX = 1.0   # Spatial step
deltaT = 0.01  # Time step
T = 10.0       # Total simulation time
L = 100.0     # Length of the domain
#to first model
#Vmax = 4.0 # Maximum velocity
#R = 2.0   
Vmax=40.0
R = 1.0       # Some constant value
V_ref = 39.99  # Given reference velocity

def u_0_x(x):
    #max values possible 0.8
    # if x<L/2:
    #     return 0.99
    # else:
    #     return 0.998
    #________________________________________________
    return 0.2 * np.sin(2 * np.pi *x*2 / L) + 0.80 #mettre 0.3 pour modèle pourri
    #________________________________________________
    #return np.where(x < L/2, 0.8, 0.2)
    #________________________________________________
    # center = L / 2  # Centre de la gaussienne
    # sigma = 0.1 * L  # Écart-type contrôlant la dispersion de la gaussienne
    # return max(0.01,1.0*np.exp(-((x - center) ** 2) / (2 * sigma ** 2))) #intéressente pour montre le pb de pente
    #return 0.5 * max(0.01, 0.8 * np.exp(-((x - center) ** 2) / (2 * sigma ** 2))) modèle pourri
    #________________________________________________
    #return np.where(x < L / 2, 1.0, 0.5)
    #________________________________________________
    #return np.maximum(0, 1 - 0.2*np.abs((x - L / 2)) * 4 / L)
    #return np.maximum(0, 1 - 0.5*np.abs((x - L / 2)) * 4 / L) * 0.5 #modèle pourri
    #________________________________________________
    # center = L / 2  # Centre du pic
    # return np.where(np.abs(x - center) < L / 10, 1.0, 0.2) #mettre 0.5 pour modèle pourri
    


# Functions for velocity and pressure
def vf(rho):
    return (1 - (rho / R)) * Vmax

def p(rho):
    return V_ref * np.log(np.maximum(rho / R, 1e-6))  # Using np.maximum to avoid log(0)

# Euler Explicit Traffic Flow simulation function
def EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R):
    maxT = int(T / deltaT) + 1
    maxL = int(L / deltaX) + 1
    
    U = np.zeros((maxT, maxL))
    U[0, :] = [u_0_x(x) for x in np.linspace(0, L, maxL)]
    print(max(U[0, :]))
    #exit()
    if isBOundaryCOnd:
        U[:, 0] = [0.2 * np.sin(2 * np.pi *  t / L) + 0.5 for t in np.linspace(0, T, maxT)]
        
        for t in range(1, maxT):
            #U[t, 0] = U[t-1,-1]
            for j in range(1, maxL):
                rho_i_n = U[t-1, j]
                rho_i_minus_1_n = U[t-1, j-1]
                
                # Calculate v_i_n and v_i_minus_1_n using the given formula
                v_i_n = vf(rho_i_n)
                v_i_minus_1_n = vf(rho_i_minus_1_n)
                
                # Calculate rho_i_n_plus_1 using the explicit Euler method
                U[t, j] = rho_i_n - (deltaT / deltaX) * (rho_i_n * (v_i_n + p(rho_i_n)) - rho_i_minus_1_n * (v_i_minus_1_n + p(rho_i_minus_1_n)))
                #U[t, j] = rho_i_n - (deltaT / deltaX) * (rho_i_n * (v_i_n ) - rho_i_minus_1_n * (v_i_minus_1_n ))
    else:
        for t in range(1, maxT):
            #U[t, 0] = U[t-1,-1]
            for j in range(0, maxL):
                rho_i_n = U[t-1, j]
                rho_i_minus_1_n = U[t-1, j-1]
                
                # Calculate v_i_n and v_i_minus_1_n using the given formula
                v_i_n = vf(rho_i_n)
                v_i_minus_1_n = vf(rho_i_minus_1_n)
                
                
                #U[t, j] = rho_i_n - ((deltaT / deltaX) * (rho_i_n * (v_i_n ) - rho_i_minus_1_n * (v_i_minus_1_n )))
                if(j+1<maxL):
                    U[t,j]=(1/2)*(U[t-1,j+1]+U[t-1,j-1]) - (deltaT/2*deltaX)*((U[t-1,j+1])*(1-U[t-1,j+1]/R)*Vmax-(U[t-1,j-1])*(1-U[t-1,j-1]/R)*Vmax)
                else:
                    U[t,j]=(1/2)*(U[t-1,0]+U[t-1,j-1]) - (deltaT/2*deltaX)*((U[t-1,0])*(1-U[t-1,0]/R)*Vmax-(U[t-1,j-1])*(1-U[t-1,j-1]/R)*Vmax)
                
                # if(U[t, j]>=1):
                #     print("t ",t,", j",j)
                #     print("U[t, j]",U[t, j])
                    # print("rho_i_n",rho_i_n)
                    # print("v_i_n",v_i_n)
                    # print("rho_i_minus_1_n",rho_i_minus_1_n)
                    # print("v_i_minus_1_n",v_i_minus_1_n)
                    
    return U

# Simulating traffic flow
U = EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R)

# Plotting the results at the last time step
maxT = int(T / deltaT)  # Number of time steps
maxL = int(L / deltaX)  # Number of spatial points
x = np.linspace(0, L, maxL + 1)  # Adjusted to include both boundaries
time_steps = np.linspace(0, T, maxT + 1)


# Initialize your figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Position (x)')
ax.set_ylabel('Time')
ax.set_title('Traffic Flow Simulation - Density Heatmap')
ax.grid()

# Create a meshgrid for space and time
time_steps_mesh, space_mesh = np.meshgrid(time_steps, x)

# Plotting the density as a heatmap
im = ax.imshow(U.T, aspect='auto', origin='lower', cmap='plasma', extent=[0, T, 0, L])

# Add a colorbar
cbar = plt.colorbar(im)
cbar.set_label('Density (rho)')

plt.show()


# Initialize your figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Position (x)')
ax.set_ylabel('Density (rho)')
ax.set_title('Traffic Flow Simulation')
ax.grid()

x = np.linspace(0, maxL, U.shape[1])  # Assuming the x-axis range is from 0 to 1

# Define time_steps array (you may have this defined in your code)
time_steps = np.linspace(0, T, maxT + 1)  # Replace maxT with your actual value

# Create a function to update the plots for each frame of the animation
def update(frame):
    ax.clear()  # Clear the previous plot
    ax.grid()
    ax.plot(x, U[frame, :])
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Density (rho)')
    ax.set_title('Traffic Flow Simulation - Time Step {}'.format(time_steps[frame]))
    return ax

# Create the animation using time steps as frames
num_frames = len(time_steps)
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, interval=100)

#ani.save('traffic_flow_animation.gif', writer='pillow', fps=30)

plt.show()

#plot the gaussian function : 
def f(x):
    center = L / 2  # Centre de la gaussienne
    sigma = 0.1 * L  # Écart-type contrôlant la dispersion de la gaussienne
    return 0.8*np.exp(-((x - center) ** 2) / (2 * sigma ** 2))

def g(x):
    center = L / 2  # Centre de la gaussienne
    sigma = 0.1 * L  # Écart-type contrôlant la dispersion de la gaussienne
    return 0.2*np.exp(-((x - center) ** 2) / (2 * sigma ** 2))

#plot f and g
x = np.linspace(0, L, maxL + 1)  # Adjusted to include both boundaries
plt.plot(x, f(x), label='f(x)')
plt.plot(x, g(x), label='g(x)')
plt.legend()
plt.show()
