import math
'''This script can find find prism if the axis is on an oblique angle.
It does not take resultant prism into account from bidirectional displacement'''
while True:
    '''print("Right or Left eye? (r/l)")
    right_left_input = input()'''
    print("What is the sph power (D)?")
    sph_input = input()
    try:
        sph_input = float(sph_input)
    except ValueError:
        print('Please use numeric digits.')
    break
while True:
    print("What is the cyl power (D)?")
    cyl_input = input()
    try:
        cyl_input = float(cyl_input)
    except ValueError:
        print('Please use numeric digits.')
    break
while True:
    print("What is the axis?")
    axis_input = input()
    try:
        axis_input = float(axis_input)
    except ValueError:
        print('Please use numeric digits.')
    break
while True:
    print("Decentration up (mm)?")
    decen_vert_input = input()
    axis = 180 - axis_input
    try:
        decen_vert_input = float(decen_vert_input)
    except ValueError:
        print('Please use numeric digits.')
    try:
        axis = 180 - axis_input
        axis = (math.sin(math.radians(axis)) ** 2) * cyl_input + sph_input
        print("The sphere power @90 is:", axis)
    finally:
        vprism = ((decen_vert_input * axis) / 10) - sph_input
        vprism += sph_input
        print(f"{vprism:.2f}", "is the amount of vertical prism")
        break
while True:
    print("Decentration in (mm)?")
    decen_horz_input = input()
    try:
        decen_horz_input = float(decen_horz_input)
    except ValueError:
        print('Please use numeric digits.')
    try:
        axis = 180 - axis_input
        axis = (math.sin(math.radians(axis)) ** 2) * cyl_input + sph_input
        print("The sphere power @180 is:", axis)
    finally:
        hprism = ((axis * decen_horz_input) / 10) - sph_input
        print(axis, decen_horz_input, sph_input)
        hprism += sph_input
        print(f"{hprism:.2f}", "is the amount of horizontal prism")

    break
