import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
# Enable LaTeX rendering

isDebug=False

#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________

if len(sys.argv) != 3:
    print("Usage: python your_script_name.py a2 h")
    sys.exit(1)


accident=False
a2 = float(sys.argv[1])
h = float(sys.argv[2])



T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________



#______________________________________________________ Set of values (position, time) ______________________________________________________
#____________________________________________________________________________________________________________________________________________
x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
time = np.zeros(n_steps)

# Initial conditions
time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified

#____________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________


#______________________________________________________ Functions ______________________________________________________________________
#____________________________________________________________________________________________________________________________________________

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

def x1_prime():
    return 130 * (1000 / 3600)

def AnalitycalSolution(t0,t,a,x_t_0):
    return (x1_prime() - x1_prime() * np.exp(-a*(t-t0)) + a*x_t_0 * np.exp(-a*(t-t0)))/a

#____________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________

#______________________________________________________ Resolution of the position for the carsEuler's explicit method ______________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    time[t] = time[t-1] + h
    if(x2Pos[t] >= x1Pos[t]):
        accident=True
        break
        
#____________________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________________


#______________________________________________________ Plotting ______________________________________________________________
#____________________________________________________________________________________________________________________________

if(accident==True):
    plt.figure(figsize=(10, 6))
    plt.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
    plt.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)
    plt.show()
else:
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1Pos, label='x1(t)')
    plt.plot(time, x2Pos, label='x2(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Position of the cars')
    plt.grid(True)
    plt.show()

#____________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________

#______________________________________________________ Analysis of the equilibrium ______________________________________________________________
#____________________________________________________________________________________________________________________________________________

#___________________________________ Plotting the analytical solutions ______________________________________________________


a=-2
t=np.linspace(0,n_steps,10000)
y_values=np.zeros((10, 10000))

if isDebug:
    print("taile : ",len(t))
for i in range(0,10):
    y_values[i] = AnalitycalSolution(0, t, a, 1)
    a=a+0.5
a=-2.0
# Plot the figure with all ten graphs
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
for i in range(5):
    plt.plot(t, y_values[i], label=f'x2(t) with a={a}')
    a=a+0.5
    if isDebug:
        print("valeur de a : ", a)

plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()
rc('text', usetex=True)
plt.title('Analytical solutions of the equilibrium for different ' + r"$\alpha$" + ' values')
rc('text', usetex=False)
plt.grid(True)
plt.yscale('log')
plt.show()

for i in range(5,10):
    plt.plot(t, y_values[i], label=f'x2(t) with a={a}')
    #plt.xlim(0, 5)
    a=a+0.5
    if isDebug:
        print("valeur de a : ", a)
    
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()
rc('text', usetex=True)
plt.title('Analytical solutions of the equilibrium for different ' + r"$\alpha$" + ' values')
rc('text', usetex=False)
plt.grid(True)
plt.show()

#___________________________________ Plotting the vector field ______________________________________________________
#____________________________________________________________________________________________________________________

# Define the vector field function
def d1_point(f, t):
    return x1_prime() - a2 * f

#__ Create the vector field plot __
f = np.linspace(0, 400, 20)
t = np.linspace(0, 25, 20)
F, T = np.meshgrid(f, t)

#__ Calculate the derivatives for the existing 'f' values __
df = d1_point(F, T)
dt = np.ones_like(df)

#__ Normalize the vectors for plotting __
length = np.sqrt(df**2 + dt**2)
df /= length
dt /= length

#__ Create the vector field plot __
plt.figure(figsize=(8, 6))
plt.quiver(T, F, dt, df, angles='xy', scale=30, color='blue')

# Add the red line f(t) = V1/a2
rc('text', usetex=True)
plt.plot(t, x1_prime() / a2 * np.ones_like(t), 'r', label=f'f(t) = $\\frac{{V_1}}{{\\alpha_2}}$ = {x1_prime() / a2}')
rc('text', usetex=False)

plt.xlabel('time (s)')
plt.ylabel('distance (m)')

rc('text', usetex=True)
plt.title('Vector Field for ' + r"$\dot{d}_1 = V_1 - \alpha_2 \cdot f$")
rc('text', usetex=False)
plt.legend()
plt.grid()
plt.show()
