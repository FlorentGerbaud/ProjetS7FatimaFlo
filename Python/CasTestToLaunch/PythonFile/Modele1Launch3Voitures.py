import sys
import numpy as np
import matplotlib.pyplot as plt

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python your_script_name.py a2 h")
    sys.exit(1)

# Parse the command-line arguments
accident=False
a2 = float(sys.argv[1])
h = float(sys.argv[2])
a3 = float(sys.argv[3])

# Rest of your script remains the same
# ...

T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

# Initialize arrays to store the results
x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
x3Pos = np.zeros(n_steps)
time = np.zeros(n_steps)
accident = False

# Initial conditions
time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified
x3Pos[0] = 0.5  # Initial value for x2 as specified

# Define the functions
def x1_prime():
    return 130 * (1000 / 3600)

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

def x3_prime(t):
    return a3 * (x2Pos[t] - x3Pos[t])

# Euler's explicit method
for t in range(1, n_steps):
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    x3Pos[t] = x3Pos[t-1] + x3_prime(t-1) * h
    time[t] = time[t-1] + h
    if x2Pos[t] >= x1Pos[t]:
        accident = True
        break

# Create two subplots
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

# Initialize arrays to store the speeds of the cars
v1 = np.zeros(n_steps)
v2 = np.zeros(n_steps)
v3 = np.zeros(n_steps)

# Calculate speeds
for t in range(1, n_steps):
    v1[t] = x1_prime()
    v2[t] = x2_prime(t)
    v3[t] = x3_prime(t)

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
