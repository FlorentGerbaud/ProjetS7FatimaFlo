#_____________________________________________________ import libraries ______________________________________________________
#________________________________________________________________________________________________________________________

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 
import sys
from tkinter import Tk, filedialog


#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________

if len(sys.argv) != 3:
    print("Usage: python your_script_name.py a2 h a3")
    sys.exit(1)

isSave=bool(int(sys.argv[2]))
typeSimu=sys.argv[1]
deltaX = 1.0   # Spatial step
deltaT = 0.01  # Time step
T = 10.0       # Total simulation time
L = 100.0     # Length of the domain
Vmax=40.0
R = 1.0       # Some constant value
V_ref = 39.99  # Given reference velocity

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________



#_________________________________________________ Define the functions  ___________________________________________________
#______________________________________________________________________________________________________________________________

#u_0_x :
    #input : x (position at the time t=0)
    #output : u_0_x(x) (initial condition for the density of the car at the position x and at the time t=0)
    #description : return the initial condition for the density of the car at the position x

def u_0_x(x):
    
    if typeSimu=="EE":
        return np.maximum(0, 1 - 0.5*np.abs((x - L / 2)) * 4 / L) * 0.5 
    elif typeSimu=="LF":
        return np.maximum(0, 1 - 0.5*np.abs((x - L / 2)) * 4 / L) 

#vf :
    #input : rho (density of the car at the position x and at the time t)
    #output : vf(rho) (velocity of the car at the position x and at the time t)
    #description : return the velocity of the car at the position x and at the time t
def vf(rho):
    return (1 - (rho / R)) * Vmax

#p :
    #input : rho (density of the car at the position x and at the time t)
    #output : p(rho) (pressure of the car at the position x and at the time t)
    #description : return the pressure of the car at the position x and at the time t

def p(rho):
    return V_ref * np.log(np.maximum(rho / R, 1e-6))  # Using np.maximum to avoid log(0)

#EulerExplicitTrafficFlow :
    #input : u_0_x, deltaX, deltaT, T, L, Vmax, R
    #output : U (array of the density of the car at the position x and at the time t)
    #description : return the array of the density of the car at the position x and at the time t
    
def EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R):
    maxT = int(T / deltaT) + 1
    maxL = int(L / deltaX) + 1
    
    U = np.zeros((maxT, maxL))
    U[0, :] = [u_0_x(x) for x in np.linspace(0, L, maxL)]
    
    for t in range(1, maxT):
        #U[t, 0] = U[t-1,-1]
        for j in range(0, maxL):
            rho_i_n = U[t-1, j]
            rho_i_minus_1_n = U[t-1, j-1]
            

            v_i_n = vf(rho_i_n)
            v_i_minus_1_n = vf(rho_i_minus_1_n)
            
            if typeSimu=="EE":
                U[t, j] = rho_i_n - ((deltaT / deltaX) * (rho_i_n * (v_i_n ) - rho_i_minus_1_n * (v_i_minus_1_n )))
            elif typeSimu=="LF":
                if(j+1<maxL):
                    U[t,j]=(1/2)*(U[t-1,j+1]+U[t-1,j-1]) - (deltaT/2*deltaX)*((U[t-1,j+1])*(1-U[t-1,j+1]/R)*Vmax-(U[t-1,j-1])*(1-U[t-1,j-1]/R)*Vmax)
                else:
                    U[t,j]=(1/2)*(U[t-1,0]+U[t-1,j-1]) - (deltaT/2*deltaX)*((U[t-1,0])*(1-U[t-1,0]/R)*Vmax-(U[t-1,j-1])*(1-U[t-1,j-1]/R)*Vmax)
    return U

#update :
    #input : frame (time step)
    #output : ax (plot)
    #description : update the plot for each frame of the animation

def update(frame):
    ax.clear()  # Clear the previous plot
    ax.grid()
    ax.plot(x, U[frame, :])
    ax.set_xlabel('Position (m)')
    ax.set_ylabel('Density ($\\rho$)')
    ax.set_title('Traffic Flow Simulation - Time Step {:.3f}'.format(time_steps[frame]))
    return ax
    

#_________________________________________________ Plotting the results  ___________________________________________________
#______________________________________________________________________________________________________________________________

if isSave:
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

#_________________________________________________ Plotting the density map  ___________________________________________________
U = EulerExplicitTrafficFlow(u_0_x, deltaX, deltaT, T, L, Vmax, R)

# Plotting the results at the last time step
maxT = int(T / deltaT)  # Number of time steps
maxL = int(L / deltaX)  # Number of spatial points
x = np.linspace(0, L, maxL + 1)  # Adjusted to include both boundaries
time_steps = np.linspace(0, T, maxT + 1)



fig, ax = plt.subplots()
ax.set_xlabel('Position (m)')
ax.set_ylabel('Time (s)')
ax.set_title('Traffic Flow Simulation - Density Heatmap')
ax.grid()

time_steps_mesh, space_mesh = np.meshgrid(time_steps, x)

# Plot the density map with position on x-axis and time on y-axis
im = ax.imshow(U, aspect='auto', origin='lower', cmap='plasma', extent=[0, L, 0, T])

cbar = plt.colorbar(im)
cbar.set_label('Density ($\\rho$)')

if isSave:
    if folder_selected:  # If a directory is selected
        file_path = folder_selected + '/traffic_flow_density_map.png'
        plt.savefig(file_path)
        print(f"Animation saved to: {file_path}")
    else:
        print("Directory selection cancelled. Animation not saved.")

plt.show()




#_________________________________________________ Plotting the animation  ___________________________________________________
fig, ax = plt.subplots()
ax.set_xlabel('Position (m)')
ax.set_ylabel('Density ($\\rho$)')
ax.set_title('Traffic Flow Simulation')
ax.grid()

x = np.linspace(0, maxL, U.shape[1])  # Assuming the x-axis range is from 0 to 1

# Define time_steps array (you may have this defined in your code)
time_steps = np.linspace(0, T, maxT + 1)  # Replace maxT with your actual value

# Create a function to update the plots for each frame of the animation


# Create the animation using time steps as frames
num_frames = len(time_steps)
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, interval=100)

if isSave:
    if folder_selected:  # If a directory is selected
        file_path = folder_selected + '/traffic_flow_animation.gif'
        ani.save(file_path, writer='pillow', fps=30)
        print(f"Animation saved to: {file_path}")
    else:
        print("Directory selection cancelled. Animation not saved.")

plt.show()













