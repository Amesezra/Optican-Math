import math


def oblique_axis_90(input_rx):
    while True:
        print("Decentration up (mm)?")
        decen_vert_input = input()
        axis = 90 - input_rx[2]
        try:
            decen_vert_input = float(decen_vert_input)
        except ValueError:
            print('Please use numeric digits.')
        try:
            axis = 90 - input_rx[2]
            axis = (math.sin(math.radians(axis)) ** 2) * input_rx[1] + input_rx[0]
            print(f"{axis:.2}", "D @ 90")
        finally:
            vprism = ((decen_vert_input * axis) / 10) - input_rx[0]
            vprism += input_rx[0]
            print(f"{vprism:.2f}", "is the amount of vertical prism induced")
            break


def oblique_axis_180(input_rx):
    while True:
        print("Decentration in (mm)?")
        decen_horz_input = input()
        try:
            decen_horz_input = float(decen_horz_input)
        except ValueError:
            print('Please use numeric digits.')
        break
    axis = 180 - input_rx[2]
    axis = (math.sin(math.radians(axis)) ** 2) * input_rx[1] + input_rx[0]
    print(f"{axis:.2f}", "D @ 180")
    hprism = ((axis * decen_horz_input) / 10) - input_rx[0]
    print("here is the Rx @90:", axis, decen_horz_input, input_rx[0])
    #  the line above gives the correct sph, but cyl and axis are wrong.
    hprism += input_rx[0]
    print(f"{hprism:.2f}", "is the amount of horizontal prism induced")
