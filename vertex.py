#  TODO: lens vertex distance calculator.
"""When a spectacle lens is moved either closer to or further away from the eye, its effective power is changed.
This means that in order for the lens to give the same refractive effect at the new vertex distance, there must
be a compensating power change.
The compensated (or effective) lens power is the adjusted power of the lens according to the new vertex distance.
The compensated power is given by the following equation given that:

D = Diopter (lens power)
De = effective diometric power
Dl = diometric power of the lens
d = distance (in meters) that the lens has moved from the refracted position to as worn.

De = Dl / (1 + (d * Dl))"""


def vertex_calc(input_rx):
    while True:
        print(f"What is the refracted vertex distance RVD (in mm)?: ")
        rvd = input()
        print(f"What is the back vertex distance BVD (in mm) of the glasses?: ")
        bvd = input()
        try:
            rvd = float(rvd)
            bvd = float(bvd)
            eff_d = input_rx[0] / (1 + (((bvd - rvd)/1000) * input_rx[0]))
            print(f"{eff_d:.2f}", f"is the expressed power at", f"{bvd:.2f}", "mm")
        except ValueError:
            print('Please use numeric digits.')
        break

# TODO: add astigmatism vertex calculations
# TODO: contact Rx from spectacle Rx.  Need warning script.
#   single vision correction
#   toric/ astigmatic correction
#       With or against rule, rounding to nearest 10 towards major meridians
#       spherical equivalent
#   Mono Vision correction
#       Dom/Non Dom eye
#   Multifocal correction
#   import JSON of tyler quarterly lens specifications
