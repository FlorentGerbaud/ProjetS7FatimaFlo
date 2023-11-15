import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def u_0_x(x):
    return 0.2 * np.sin(2 * np.pi * x / 10.0) + 0.5


# Function to set boundary condition a(t)
def a(t):
    return 0.5

# Function to set boundary condition b(t)
def b(t):
    return 0.7

# Euler Explicit Traffic Flow simulation function
def EulerExplicitTrafficFlow(a, b, u_0_x, deltaX, deltaT, T, L, Vmax, R):
    maxT = int(T / deltaT) + 1
    maxL = int(L / deltaX) + 1
    
    U = np.zeros((maxT, maxL))
    U[0, :] = [u_0_x(x) for x in np.linspace(0, L, maxL)]
    
    for t in range(1, maxT):
        # Update boundary conditions based on time
        U[t, 0] = a(t * deltaT)
        U[t, -1] = b(t * deltaT)
        
    for t in range(1, maxT):
        for j in range(1, maxL - 1):
            rho_i_n = U[t-1, j]
            rho_i_minus_1_n = U[t-1, j-1]
            
            
            # Calculate v_i_n and v_i_minus_1_n using the given formula
            v_i_n = (1 - 2 * rho_i_n / R) * Vmax
            v_i_minus_1_n = (1 - 2 * rho_i_minus_1_n / R) * Vmax
            
            # Calculate rho_i_n_plus_1 using the explicit Euler method
            U[t, j] = rho_i_n - (deltaT / deltaX) * (-rho_i_n * v_i_n + rho_i_minus_1_n * v_i_minus_1_n)
    return U

# Parameters for the simulation
deltaX = 1.0   # Spatial step
deltaT = 0.01  # Time step
T = 10.0        # Total simulation time
L = 1000.0       # Length of the domain
Vmax = 130*1000/3600  # Maximum velocity
R = 1.0        # Some constant value

# Simulating traffic flow
U = EulerExplicitTrafficFlow(a, b, u_0_x, deltaX, deltaT, T, L, Vmax, R)

# Plotting the results at the last time step
maxT = int(T / deltaT)  # Number of time steps
print("maxT : ",maxT)
maxL = int(L / deltaX)  # Number of spatial points
x = np.linspace(0, L, maxL + 1)  # Adjusted to include both boundaries
time_steps = np.linspace(0, T, maxT + 1)
#plt.plot(x, U[1, :])  # Plotting the density at the last time step
plt.plot(x, U[0, :])  # Plotting the density at the last time step
plt.plot(x, U[50, :])  # Plotting the density at the last time step
plt.plot(x, U[100, :])  # Plotting the density at the last time step
plt.plot(x, U[500, :])  # Plotting the density at the last time step
plt.plot(x, U[maxT-2, :])  # Plotting the density at the last time step
plt.xlabel('Position (x)')
plt.ylabel('Density (rho)')
plt.title('Traffic Flow Simulation')
plt.show()

# Initialize your figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Position (x)')
ax.set_ylabel('Density (rho)')
ax.set_title('Traffic Flow Simulation')

x = np.linspace(0, 1, U.shape[1])  # Assuming the x-axis range is from 0 to 1

# Define time_steps array (you may have this defined in your code)
time_steps = np.linspace(0, T, maxT + 1)  # Replace maxT with your actual value

# Create a function to update the plots for each frame of the animation
def update(frame):
    ax.clear()  # Clear the previous plot
    ax.plot(x, U[frame, :])
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Density (rho)')
    ax.set_title('Traffic Flow Simulation - Time Step {}'.format(time_steps[frame]))
    return ax

# Create the animation using time steps as frames
num_frames = len(time_steps)
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, interval=100)

# Save the animation as a GIF using Pillow
#ani.save('traffic_flow_animation.gif', writer='pillow', fps=30)

plt.show()
