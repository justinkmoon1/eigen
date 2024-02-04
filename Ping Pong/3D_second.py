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
    
    # Arrays to store position and velocity of the ping pong ball
    y = np.zeros(2)
    vy = np.zeros(2)
    
    # Initial conditions for the ping pong ball
    y[0] = initial_water_height
    vy[0] = 0
    
    # Time array
    time_interval = 0.01  # seconds
    time = np.arange(0, 10, time_interval)
    
    # Arrays to store water displacement
    water_displacement = np.zeros_like(time)
    
    # Arrays to store water splash data
    splash_time = []
    splash_height = []
    
    # Simulation loop
    for i in range(1, len(time)):
        # Update velocity and position of the ping pong ball using physics equations
        vy[1] = vy[0] - g * time_interval
        y[1] = y[0] + vy[0] * time_interval - 0.5 * g * time_interval**2
        
        # Update water displacement based on the difference in water level
        water_displacement[i] = y[1] - y[0]
        
        # Check if the ball hits the water surface
        if y[0] > 0 and y[1] <= 0:
            splash_time.append(time[i])
            splash_height.append(0)
        
        # Update initial conditions for the next iteration
        y[0] = y[1]
        vy[0] = vy[1]
    
    # Plot the trajectory in 3D space
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(time[:i], np.zeros_like(time[:i]), y[1:i+1], label='Ball Trajectory')
    
    # Scatter plot for water splashes
    ax.scatter(splash_time, np.zeros_like(splash_time), splash_height, c='red', marker='o', label='Water Splash')
    
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Horizontal Distance (m)')
    ax.set_zlabel('Height (m)')
    ax.set_title('Ping Pong Ball Launch Experiment with Water Splashing')
    ax.legend()
    plt.show()
    
    # Plot water displacement
    plt.plot(time[:i], water_displacement[:i])
    plt.title('Water Displacement over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Water Displacement (m)')
    plt.grid(True)
    plt.show()

# Example usage
container_volume = 2  # liters
initial_water_height = 1  # meters
ping_pong_mass = 0.0027  # kg (typical mass of a ping pong ball)
ping_pong_radius = 0.02  # meters (typical radius of a ping pong ball)

ping_pong_experiment(container_volume, initial_water_height, ping_pong_mass, ping_pong_radius)
