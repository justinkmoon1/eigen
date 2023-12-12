import scipy.constants as csts
import math

def exit_vel(original_height, original_mass, height, side, mass):
    """
    original_height: height of the dropped object
    original mass: mass of the dropped object
    height: the height that the launched object reached
    side: the horizontal movement of the launched object
    mass: the mass of the launched object
    """

    y_vel = math.sqrt(csts.kgf * 2 * height)

    t = csts.kgf / y_vel

    x_vel = side / t

    vel = math.sqrt(y_vel**2 + x_vel**2)
    return x_vel, y_vel, vel

def new_energy(x_vel, y_vel, vel, mass, height):
    ke = 0.5 * mass * x_vel**2
    pe = mass * height * csts.kgf
    te = ke + pe

    return ke, pe, te
    

