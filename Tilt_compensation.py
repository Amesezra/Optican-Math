import math
# TODO: make another function for lens tilt/wrap calculations
# TODO: vertical vs horizontal movements
"""
new_sph = S' = new spherical power
origin_sph = S = original sphere power
alpha = degree of tilt
index = n = refractive index of the lens
induced_cyl = C' = induced cylinder on the axis of rotation

S' = S * (1 + ((sin(alpha) ** 2)/2n)
C' = S' * ((tan(alpha) ** 2))
"""


def tilt(input_rx):
    origin_sph = input_rx[0]
    index = 1.586  # this is polycarbonate TODO add material choice, and list with n values for each.
    alpha = 15  # this is a filler value.  TODO add input prompt for pantoscopic and retroscopic tilt
    new_sph = origin_sph * (1 + ((math.sin(math.radians(alpha)) ** 2) / (2 * index)))
    #  induced_cyl = new_sph * ((math.sin(math.radians(alpha)) ** 2)
    print(new_sph)
