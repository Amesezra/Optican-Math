import math
input_rx = []


def oblique_axis_90():
    while True:
        print("Decentration up (mm)?")
        decen_vert_input = input()
        axis = 180 - input_rx[2]
        try:
            decen_vert_input = float(decen_vert_input)
        except ValueError:
            print('Please use numeric digits.')
        try:
            axis = 180 - input_rx[2]
            axis = (math.sin(math.radians(axis)) ** 2) * input_rx[1] + input_rx[0]
            print("The sphere power @90 is:", axis)
        finally:
            vprism = ((decen_vert_input * axis) / 10) - input_rx[0]
            vprism += input_rx[0]
            print(f"{vprism:.2f}", "is the amount of vertical prism")
            break


def oblique_axis_180():
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
    print("The sphere power @180 is:", axis)
    hprism = ((axis * decen_horz_input) / 10) - input_rx[0]
    print(axis, decen_horz_input, input_rx[0])
    hprism += input_rx[0]
    print(f"{hprism:.2f}", "is the amount of horizontal prism")
