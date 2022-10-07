while True:  # validate user input
    print('Enter the sph or spherical value')
    sphere = input()
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
    print('Enter the cyl or cylinder value')
    cylinder = input()
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
    print('Enter the axis value')
    axis = input()
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
transposed_rx = [0, 0, 0]
print(f'Here is the given Rx:\n{sphere:.2f}', f'{cylinder:.2f}', f"@{str(axis).rjust(3, '0')}")
while True:  # transpose Rx
    sph = input_rx[0]
    cyl = input_rx[1]
    axis = input_rx[2]
    if cyl > 0:  # Checking if the number is positive
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
              f"@{str(transposed_rx[2]).rjust(3, '0')}")
    else:
        print("Zero cyl means there is no astigmatism to transpose")
    break
