"""The transpose function converts the Rx from opthalmic standard notation to optometric
standard notation.  Sometimes called plus/minus cylinder forms, both are equivalent but express correction
from either the maximum or minimum corrective power needed rotated by 90 degrees or pi/2 radians"""

def transpose(input_rx):
    transposed_rx = [0, 0, 0]
    while True:
        sph = input_rx[0]
        cyl = input_rx[1]
        axis = input_rx[2]
        if cyl > 0:
            sign = -1 if cyl > 0 else 1
            transposed_rx[0] = cyl + sph  # transpose power
            cyl = cyl * sign  # reverse signs
            transposed_rx[1] = cyl  # update cylinder in list with new positivity
            if axis >= 91:
                axis -= 90
                transposed_rx[2] = axis
            elif axis <= 90:
                axis += 90
                transposed_rx[2] = axis
            print(f'Here is the Rx in negative cyl form:\n{transposed_rx[0]:.2f}', f'{transposed_rx[1]:.2f}',
                  f"@{str(transposed_rx[2]).rjust(3, '0')}")
        elif cyl < 0:
            transposed_rx[0] = cyl + sph
            cyl *= -1
            transposed_rx[1] = cyl
            if axis >= 91:
                axis -= 90
                transposed_rx[2] = axis
            elif axis <= 90:
                axis += 90
                transposed_rx[2] = axis
            print(f'Here is the transposed Rx:\n{transposed_rx[0]:.2f}', f'{transposed_rx[1]:.2f}',
                  f"@{str(transposed_rx[2]).rjust(3, '0')}\n")
        else:
            print("Zero cyl means there is no astigmatism to transpose")
        break
