import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def ping_pong_experiment(container_volume, initial_water_height, ping_pong_mass, ping_pong_radius):
    """
    Simulates the launch of a ping pong ball from a water-filled container.
    
    Parameters:
    - container_volume: Volume of the container (in liters).
    - initial_water_height: Initial height of water in the container (in meters).
    - ping_pong_mass: Mass of the ping pong ball (in kilograms).
    - ping_pong_radius: Radius of the ping pong ball (in meters).
    """
    # Constants
    g = 9.8  # Acceleration due to gravity (m/s^2)
    rho_water = 1000  # Density of water (kg/m^3)
    
    # Convert container volume to cubic meters
    container_volume = container_volume * 1e-3
    
    # Calculate the buoyant force
    buoyant_force = rho_water * g * container_volume
    
    # Initial conditions
    initial_velocity = 0  # Initial velocity of the ping pong ball
    
    # Time array
    time_interval = 0.01  # seconds
    time = np.arange(0, 10, time_interval)
    
    # Arrays to store position and velocity
    y = np.zeros_like(time)
    vy = np.zeros_like(time)
    
    # Initial conditions
    y[0] = initial_water_height
    vy[0] = initial_velocity
    
    # Simulation loop
    for i in range(1, len(time)):
        # Update velocity and position using physics equations
        vy[i] = vy[i-1] - (g - buoyant_force / ping_pong_mass) * time_interval
        y[i] = y[i-1] + vy[i] * time_interval
    
        # Stop simulation if the ball reaches the surface
        if y[i] <= 0:
            break
    
    # Plot the trajectory in 3D space
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(time[:i], np.zeros_like(time[:i]), y[:i], label='Trajectory')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Horizontal Distance (m)')
    ax.set_zlabel('Height (m)')
    ax.set_title('Ping Pong Ball Launch Experiment')
    ax.legend()
    plt.show()

# Example usage
container_volume = 2  # liters
initial_water_height = 1  # meters
ping_pong_mass = 0.0027  # kg (typical mass of a ping pong ball)
ping_pong_radius = 0.02  # meters (typical radius of a ping pong ball)

ping_pong_experiment(container_volume, initial_water_height, ping_pong_mass, ping_pong_radius)
