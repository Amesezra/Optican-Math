import math
import json
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
"""Although frames and faces may come in a wide variety of styles and sizes, engineers working with traditional 
single vision and progressive designs had little choice in deciding what distance, tilt and wrap angle values a
frame would place the lenses. Therefore they settled on averaged values calculated from vast amounts of 
real-world fitting data. Examining this data, they found that on average, most lenses would be positioned
approximately 13mm in front of the eyes for vertex distance, 10 degrees for Pantoscopic lens tilt and 5 degrees
for frame wrap angle, otherwise called position of wear, or POW.  Freeform or 'HD' lenses allow us to customize 
these measurements"""

def tilt(input_rx):
    origin_sph = input_rx[0]
    index = 1.586  # this is polycarbonate TODO add material choice, and list with n values for each.
    alpha = 15  # this is a filler value.  TODO add input prompt for pantoscopic and retroscopic tilt
    new_sph = origin_sph * (1 + ((math.sin(math.radians(alpha)) ** 2) / (2 * index)))
    induced_cyl = new_sph * (math.sin(math.radians(alpha)) ** 2)
    print(f"{new_sph:.2f}", f"{induced_cyl:.2f}", 180)

def wrap(input_rx):
    origin_sph = input_rx[0]
    index = 1.586
    alpha = 15  # this is a filler value.  TODO add input prompt for pantoscopic and retroscopic tilt
    new_sph = origin_sph * (1 + ((math.sin(math.radians(alpha)) ** 2) / (2 * index)))
    induced_cyl = new_sph * (math.sin(math.radians(alpha)) ** 2)
    print(f"{new_sph:.2f}", f"{induced_cyl:.2f}", 90)

