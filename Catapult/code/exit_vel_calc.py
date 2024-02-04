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

    t = y_vel/csts.kgf

    x_vel = (side)/ t

    vel = math.sqrt(y_vel**2 + x_vel**2)
    return x_vel, y_vel, vel

def new_energy(x_vel, y_vel, vel, mass, height):
    ke = 0.5 * mass * x_vel**2
    pe = mass * height * csts.kgf
    te = ke + pe

    return ke, pe, te
    

#input h and s in cm

h, s = map(float, input("Results: ").split())

h *= 0.01
s *= 0.01
x, y, xy = exit_vel(0, 0, h, s, 0)

print(xy)
print(new_energy(x, y, xy, 0.02, h))