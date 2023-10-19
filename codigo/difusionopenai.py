import numpy as np
import matplotlib.pyplot as plt

# Parameters
length = 3.2     # Length of the rod
num_points = 100  # Number of spatial points
num_steps = 1000  # Number of time steps
alpha = 0.01      # Thermal diffusivity

# Discretization
dx = length / (num_points - 1)
dt = alpha * dx**2

# Initial condition
u = np.zeros(num_points)
u = np.sin(np.linspace(0,length,num_points))

# Time-stepping loop
for step in range(num_steps):
    u = u + alpha * np.gradient(np.gradient(u, dx), dx) * dt

# Plot the final solution
x = np.linspace(0, length, num_points)
plt.plot(x, u)
plt.title("One-Dimensional Heat Equation (Using NumPy Gradient)")
plt.xlabel("Position")
plt.ylabel("Temperature")
plt.show()
