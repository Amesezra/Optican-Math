import math
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
    while True:
        print("What is the pantoscopic tilt angle?")
        alpha = int(input())
        if alpha > 30:
            print('Are you sure? That is too much pantoscopic tilt.  Please try again.')
            continue
        elif alpha < -10:
            print('Are you sure? That is too much retroscopic tilt.  Please try again.')
            continue
        break
    origin_sph = input_rx[0]
    index = 1.586  # this is polycarbonate.
    new_sph = origin_sph * (1 + ((math.sin(math.radians(alpha)) ** 2) / (2 * index)))
    induced_cyl = new_sph * (math.sin(math.radians(alpha)) ** 2)
    print("The induced power from the tilt is:", f"{new_sph:.2f}", f"{induced_cyl:.2f}", 180)


def wrap(input_rx):
    while True:
        print("What is the face-form or wrap angle?")
        alpha = int(input())
        if alpha > 30:
            print('Are you sure? That is too much face-form.  Please try again.')
            continue
        elif alpha < -10:
            print('Are you sure? That is too much negative face-form.  Please try again.')
            continue
        break
    origin_sph = input_rx[0]
    index = 1.586
    new_sph = origin_sph * (1 + ((math.sin(math.radians(alpha)) ** 2) / (2 * index)))
    induced_cyl = new_sph * (math.sin(math.radians(alpha)) ** 2)
    print("The induced power from the wrap is:", f"{new_sph:.2f}", f"{induced_cyl:.2f}", 90)
