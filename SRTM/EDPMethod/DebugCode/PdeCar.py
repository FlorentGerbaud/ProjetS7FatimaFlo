import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the simulation
deltaX = 1.0   # Spatial step
deltaT = 0.1  # Time step
T = 100.0       # Total simulation time
L = 1000.0     # Length of the domain
Vmax = 130*1000/3600  # Maximum velocity
R = 1.0       # Some constant value
V_ref = 30.0  # Given reference velocity

def u_0_x(x):
    return 0.2 * np.sin(2 * np.pi * x / L) + 0.5

# Functions for velocity and pressure
def vf(rho):
    return (1 - rho / R) * Vmax

def p(rho):
    return V_ref * np.log(np.maximum(rho / R, 1e-6))  # Using np.maximum to avoid log(0)

# Euler Explicit Traffic Flow simulation function
def EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R):
    maxT = int(T / deltaT) + 1
    maxL = int(L / deltaX) + 1
    
    U = np.zeros((maxT, maxL))
    U[0, :] = [u_0_x(x) for x in np.linspace(0, L, maxL)]
    
    # # Example of setting inflow and outflow boundary conditions
    # inflow_density = 0.5  # Example: High density representing incoming traffic
    # outflow_density = 0.4  # Example: Low density representing outgoing traffic
    #U[:, 0] = [0.2 * np.sin(2 * np.pi * t / L) + 0.5 for t in np.linspace(0, T, maxT)]  # Set inflow boundary condition
    # U[:, -1] = outflow_density  # Set outflow boundary condition
        
    for t in range(1, maxT):
        U[t,0]=U[t-1,1]
        for j in range(0, maxL):
            rho_i_n = U[t-1, j]
            rho_i_minus_1_n = U[t-1, j-1]
            
            # Calculate v_i_n and v_i_minus_1_n using the given formula
            v_i_n = vf(rho_i_n)
            v_i_minus_1_n = vf(rho_i_minus_1_n)
            
            # Calculate rho_i_n_plus_1 using the explicit Euler method
            U[t, j] = rho_i_n - (deltaT / deltaX) * (rho_i_n * (v_i_n + p(rho_i_n)) - rho_i_minus_1_n * (v_i_minus_1_n + p(rho_i_minus_1_n)))
    return U

# Simulating traffic flow
U = EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R)

# Plotting the results at the last time step
maxT = int(T / deltaT)  # Number of time steps
maxL = int(L / deltaX)  # Number of spatial points
x = np.linspace(0, L, maxL + 1)  # Adjusted to include both boundaries
time_steps = np.linspace(0, T, maxT + 1)

# plt.plot(x, U[0, :])  # Plotting the density at the last time step
# plt.plot(x, U[50, :])  # Plotting the density at the last time step
# plt.plot(x, U[100, :])  # Plotting the density at the last time step
# plt.plot(x, U[500, :])  # Plotting the density at the last time step
# plt.plot(x, U[maxT-2, :])  # Plotting the density at the last time step
# plt.xlabel('Position (x)')
# plt.ylabel('Density (rho)')
# plt.title('Traffic Flow Simulation')
# plt.show()

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

#ani.save('traffic_flow_animation.gif', writer='pillow', fps=30)

plt.show()
