# Archivo: mecanicaceleste.py
# Autor: Javier Garcia Algarra 
# Fecha: 12 de agosto de 2023
# Descripción: Ejemplo de animacion

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 5,5
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # gravitational constant in m^3/kg/s^2
M_sun = 1.989e30  # mass of the Sun in kg
M_earth = 5.972e24  # mass of the Earth in kg
AU = 1.496e11  # astronomical unit in meters




# Initial conditions
init_pos_earth = np.array([1*AU, 0])  # initial position of Earth in meters
init_vel_earth = np.array([0, 29783])  # initial velocity of Earth in m/s

# Time parameters
t_max = 365 * 24 * 60 * 60  # simulate for one year in seconds
dt = 24* 60 * 60  # time step in seconds
num_steps = int(t_max / dt)

# Arrays to store positions
positions_earth = np.zeros((num_steps, 2))
positions_earth[0] = init_pos_earth

# Perform simulation
for i in range(1, num_steps):
    r_earth = np.linalg.norm(positions_earth[i - 1])
    acceleration_earth = -G * M_sun / r_earth**3 * positions_earth[i - 1]
    new_vel_earth = init_vel_earth + acceleration_earth * dt
    new_pos_earth = positions_earth[i - 1] + new_vel_earth * dt
    positions_earth[i] = new_pos_earth
    init_vel_earth = new_vel_earth

# Create animation
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo')
linesun, = ax.plot([0], [0], 'yo', markersize = 20)


def init():
    ax.set_xlim(-1.5 * AU, 1.5 * AU)
    ax.set_ylim(-1.5 * AU, 1.5 * AU)
    # set equal aspect such that the circle is not shown as ellipse
    ax.set_aspect("equal")
    return line,

def animate(i):
    line.set_data(positions_earth[i, 0], positions_earth[i, 1])
    return line,

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, interval=10)

plt.show()
