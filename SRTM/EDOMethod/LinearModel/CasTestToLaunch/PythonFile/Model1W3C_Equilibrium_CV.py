import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

isDebug=False

# Define the parameters
a2 = 2.0  #capacity of acceleration deceleration
h = 1.0 # Time step
T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

# Initialize arrays to store the results
x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
time = np.zeros(n_steps)
accident=False

# Initial conditions
time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified

#def of the function

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

def x1_prime():
    return 130 * (1000 / 3600)

def AnalitycalSolution(t0,t,a,x_t_0):
    return (x1_prime() - x1_prime() * np.exp(-a*(t-t0)) + a*x_t_0 * np.exp(-a*(t-t0)))/a
# Euler's explicit method
for t in range(1, n_steps):
    
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    time[t] = time[t-1] + h
    if(x2Pos[t] >= x1Pos[t]):
        accident=True
        break;
        
print("deltaPos : ", x1Pos[-1]-x2Pos[-1])

if(accident==True):
    plt.figure(figsize=(10, 6))
    plt.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
    plt.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)
    plt.show()
else:
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1Pos, label='x1(t)')
    plt.plot(time, x2Pos, label='x2(t)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.title('Euler Explicit Method for x2\' = a2(x1(t) - x2(t)) with Constant x1\'')
    plt.grid(True)
    plt.show()

#Analysis of the equilibrium

# Define the parameters
t0=0
a=-2
t=np.linspace(0,n_steps,10000)
y_values=np.zeros((10, 10000))
if isDebug:
    print("taile : ",len(t))
for i in range(0,10):
    y_values[i] = AnalitycalSolution(t0, t, a, 1)
    a=a+0.5
a=-2.0
# Plot the figure with all ten graphs
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
for i in range(5):
    plt.plot(t, y_values[i], label=f'x2(t) with a={a}')
    a=a+0.5
    if isDebug:
        print("valeur de a : ", a)

plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.title('Analytical solutions of the equilibrium for different "a" values')
plt.grid(True)
plt.yscale('log')
plt.show()

for i in range(5,10):
    plt.plot(t, y_values[i], label=f'x2(t) with a={a}')
    #plt.xlim(0, 5)
    a=a+0.5
    if isDebug:
        print("valeur de a : ", a)
    
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.title('Analytical solutions of the equilibrium for different "a" values')
plt.grid(True)
plt.show()

#graph of the equilibrium f=V1/a2

# Enable LaTeX rendering
rc('text', usetex=True)

# Define the parameters

# Define the vector field function
def df_dt(f, t):
    return x1_prime() - a2 * f

# Create a grid of f and t values
f = np.linspace(0, 400, 20)
t = np.linspace(0, 25, 20)
F, T = np.meshgrid(f, t)

# Calculate the derivatives for the existing 'f' values
df = df_dt(F, T)
dt = np.ones_like(df)

# Normalize the vectors for plotting
length = np.sqrt(df**2 + dt**2)
df /= length
dt /= length

# Create the vector field plot
plt.figure(figsize=(8, 6))
plt.quiver(T, F, dt, df, angles='xy', scale=30, color='blue')

# Add the red line f(t) = V1/a2
plt.plot(t, x1_prime()/a2 * np.ones_like(t), 'r', label=r"$\dot{d}_1 = \frac{V_1}{\alpha_2}$")

plt.xlabel('time')
plt.ylabel('f(t)')
plt.title(r"Vector Field for $\dot{d}_1 = V_1 - \alpha_2 \cdot d$")
plt.legend()
plt.grid()
plt.show()
