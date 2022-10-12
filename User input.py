import math
print("Welcome to the optician math helper.")


while True:  # validate user input
    sphere = input(f"Enter the sph or spherical value: ")
    try:
        sphere = float(sphere)
    except ValueError:
        print('Please use numeric digits.')
        continue
    if sphere > 20:
        print('Are you sure? Enter a power between +/-20.00.')
        continue
    elif sphere < -20:
        print('Are you sure? Enter a power between +/-20.00.')
        continue
    break
while True:
    cylinder = input(f'Enter the cyl or cylinder value: ')
    try:
        cylinder = float(cylinder)
    except ValueError:
        print('Please use numeric digits.')
        continue
    if cylinder > 20:
        print('Are you sure? Enter a power between +/-20.00.')
        continue
    elif cylinder < -20:
        print('Are you sure? Enter a power between +/-20.00.')
        continue
    break
while True:
    axis = input(f'Enter the axis value: ')
    try:
        axis = int(axis)
    except ValueError:
        print('Please use a numeric digit')
        continue
    if axis < 0:
        print('Please enter an axis between 0-180.')
        continue
    elif axis > 180:
        print('Please enter an axis between 0-180.')
        continue
    break
input_rx = [sphere, cylinder, axis]
"""The transpose function converts the Rx from opthalmic standard notation to optometric
standard notation.  Sometimes called plus/minus cylinder forms, both are equivalent but express correction
from either the maximum or minimum corrective power needed rotated by 90 degrees or pi/2 radians"""


def transpose():
    transposed_rx = [0, 0, 0]
    while True:
        t_sph = input_rx[0]
        t_cyl = input_rx[1]
        t_axis = input_rx[2]
        if t_cyl > 0:
            sign = -1 if t_cyl > 0 else 1
            transposed_rx[0] = t_cyl + t_sph  # transpose power
            t_cyl = t_cyl * sign  # reverse signs
            transposed_rx[1] = t_cyl  # update cylinder in list with new positivity
            if t_axis >= 91:
                t_axis -= 90
                transposed_rx[2] = t_axis
            elif t_axis <= 90:
                t_axis += 90
                transposed_rx[2] = t_axis
            print(f'Here is the Rx in negative cyl form:\n{transposed_rx[0]:.2f}', f'{transposed_rx[1]:.2f}',
                  f"@{str(transposed_rx[2]).rjust(3, '0')}")
        elif t_cyl < 0:
            transposed_rx[0] = t_cyl + t_sph
            t_cyl *= -1
            transposed_rx[1] = t_cyl
            if t_axis >= 91:
                t_axis -= 90
                transposed_rx[2] = t_axis
            elif t_axis <= 90:
                t_axis += 90
                transposed_rx[2] = t_axis
            print(f'Here is the transposed Rx:\n{transposed_rx[0]:.2f}', f'{transposed_rx[1]:.2f}',
                  f"@{str(transposed_rx[2]).rjust(3, '0')}\n")
        else:
            print("Zero cyl means there is no astigmatism to transpose")
        break


"""When a spectacle lens is moved either closer to or further away from the eye, its effective power is changed.
This means that in order for the lens to give the same refractive effect at the new vertex distance, there must
be a compensating power change.
The compensated (or effective) lens power is the adjusted power of the lens according to the new vertex distance.
The compensated power is given by the following equation given that:

input_rx[0] = D = Diopter (lens power)
eff_d = De = effective diometric power
Dl = diometric power of the lens
(bvd - rvd) = d = distance (in meters) that the lens has moved from the refracted position to as worn.

De = Dl / (1 + (d * Dl))"""


def vertex_calc():
    while True:
        print(f"What is the refracted vertex distance RVD (in mm)?: ")
        rvd = input()
        print(f"What is the back vertex distance BVD (in mm) of the glasses?: ")
        bvd = input()
        try:
            rvd = float(rvd)
            bvd = float(bvd)
            eff_d = input_rx[0] / (1 + (((bvd - rvd)/1000) * input_rx[0]))  # /1000 ia a unit conversion mm to m.
            print(f"{eff_d:.2f}", f"is the expressed power at", f"{bvd:.2f}", "mm")
        except ValueError:
            print('Please use numeric digits.')
        break


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


def tilt():
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


def wrap():
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


"""When light passes through a lens, it refracts.  If the point of refraction or the optical center of a lens
is misaligned with the wearer's pupil it causes a prismatic error. Prism is measured in the vertical and
horizontal meridians (90/180).  Rx's with astigmatism do not always align with these points, this function uses
trigonometry to find the power at those meridians."""


def oblique_axis_90():
    while True:
        print("Decentration up (mm)?")
        decen_vert_input = input()
        vetical_axis = 90 - input_rx[2]
        try:
            decen_vert_input = float(decen_vert_input)
        except ValueError:
            print('Please use numeric digits.')
        break
    cyl_expressed = input_rx[1] - ((math.sin(math.radians(vetical_axis)) ** 2) * input_rx[1])
    vetical_axis = 90 - input_rx[2]
    vetical_axis = (math.sin(math.radians(vetical_axis)) ** 2) * input_rx[1] + input_rx[0]
    print(f"{vetical_axis:.2f}", "D @ 90")
    print("here is the Rx expressed @90:", f"{vetical_axis:.2f}", f"{cyl_expressed:.2f}", 90)
    vprism = ((decen_vert_input * vetical_axis) / 10) - input_rx[0]
    vprism += input_rx[0]
    print(f"{vprism:.3f}", "is the amount of vertical prism induced")


def oblique_axis_180():
    while True:
        print("Decentration in (mm)?")
        decen_horz_input = input()
        try:
            decen_horz_input = float(decen_horz_input)
        except ValueError:
            print('Please use numeric digits.')
        break
    horizontal_axis = 180 - input_rx[2]
    cyl_expressed = input_rx[1] - ((math.sin(math.radians(horizontal_axis)) ** 2) * input_rx[1])
    horizontal_axis = (math.sin(math.radians(horizontal_axis)) ** 2) * input_rx[1] + input_rx[0]
    print(f"{horizontal_axis:.2f}", "D @ 180")
    print("here is the Rx expressed @180:", f"{horizontal_axis:.2f}", f"{cyl_expressed:.2f}", 180)
    hprism = ((horizontal_axis * decen_horz_input) / 10) - input_rx[0]
    hprism += input_rx[0]
    print(f"{hprism:.3f}", "is the amount of horizontal prism induced")


def svblank():
    print("The PD is the distance between pupils, An 'A' measurement is the vertical height of the lens, the DBL is \n"
          "the distance between lenses, or the bridge size.  The ED of a frame is twice the longest radius from the \n"
          "geometric center of lens to the farthest edge; the smallest circle that will completely enclose the lens.")
    cust_pd = int(input("What is the customer's PD? "))
    frame_a = int(input("What is the frame's A? "))
    frame_dbl = int(input("What is the frame's DBL? "))
    frame_ed = int(input("What is the frame's ED? "))
    svblanksize = 1 + frame_ed + ((frame_a + frame_dbl) - cust_pd)
    print(f'The minimum blank size required to fabricate a lens for this order is:', svblanksize, 'mm')


def basecurve():
    """spherical_equivalent = sphere + (cylinder / 2)
    print(spherical_equivalent)
    plus_vogels_curve = spherical_equivalent + 6
    minus_vogels_curve = (sphere + spherical_equivalent) / 2) + 6"""
    while True:
        if sphere >= 0:
            print("Based on Vogel's rule, the base curve shouold be:")
            spherical_equivalent = sphere + (cylinder / 2)
            vogels_curve = spherical_equivalent + 6
            print(f'{vogels_curve:.3f}')
        elif sphere < 0:
            print("Based on Vogel's rule, the base curve shouold be:")
            spherical_equivalent = sphere + (cylinder / 2)
            vogels_curve = spherical_equivalent / 2
            vogels_curve += 6
            print(f'{vogels_curve:.3f}')
        break


print(f'Here is the given Rx:\n{sphere:.2f}', f'{cylinder:.2f}', f"@{str(axis).rjust(3, '0')}")
print(f'Now what do you want to do?')
print('1. Transpose rx')
print('2. Find prismatic imbalance')
print('3. Vertex rx')
print('4. Tilt angle calculator')
print('5. Wrap angle calculator')
print('6. SV minimum blank size')
print('7. Base curve calculator/Nominal lens formula')

choice = str(input())
while choice not in ['1', '2', '3', '4', '5', '6', '7']:
    print("Your choice is invalid. Please try again.")
    choice = input("Choose 1 or 2: ")
if choice == '1':
    transpose()
elif choice == '2':
    oblique_axis_180()
    oblique_axis_90()
elif choice == '3':
    vertex_calc()
elif choice == '4':
    tilt()
elif choice == '5':
    wrap()
elif choice == '6':
    svblank()
elif choice == '7':
    basecurve()
