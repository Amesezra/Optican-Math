import math
#  TODO: configure base direction calculator, determine based on x positivity,
#   and given user input R/L or OD/OS.
#  TODO: make Rx Class, so it is easier to store known variables: sph, cyl, axis, OD/OS, PD, OC, etc.)
#  TODO: with known base directions, determine compounding or cancelling prism.
"""When light passes through a lens, it refracts.  If the point of refraction or the optical center of a lens
is misaligned with the wearer's pupil it causes a prismatic error. Prism is measured in the vertical and
horizontal meridians (90/180).  Rx's with astigmatism do not always align with these points, this function uses
trigonometry to find the power at those meridians."""


def oblique_axis_90(input_rx):
    while True:
        print("Decentration up (mm)?")
        decen_vert_input = input()
        axis = 90 - input_rx[2]
        try:
            decen_vert_input = float(decen_vert_input)
        except ValueError:
            print('Please use numeric digits.')
        break
    cyl_expressed = input_rx[1] - ((math.sin(math.radians(axis)) ** 2) * input_rx[1])
    axis = 90 - input_rx[2]
    axis = (math.sin(math.radians(axis)) ** 2) * input_rx[1] + input_rx[0]
    print(f"{axis:.2f}", "D @ 90")
    print("here is the Rx expressed @90:", f"{axis:.2f}", f"{cyl_expressed:.2f}", 90)
    vprism = ((decen_vert_input * axis) / 10) - input_rx[0]
    vprism += input_rx[0]
    print(f"{vprism:.3f}", "is the amount of vertical prism induced")


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
    cyl_expressed = input_rx[1] - ((math.sin(math.radians(axis)) ** 2) * input_rx[1])
    axis = (math.sin(math.radians(axis)) ** 2) * input_rx[1] + input_rx[0]
    print(f"{axis:.2f}", "D @ 180")
    print("here is the Rx expressed @180:", f"{axis:.2f}", f"{cyl_expressed:.2f}", 180)
    hprism = ((axis * decen_horz_input) / 10) - input_rx[0]
    hprism += input_rx[0]
    print(f"{hprism:.3f}", "is the amount of horizontal prism induced")
