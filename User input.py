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
transposed_rx = [0, 0, 0]
print(f'Here is the given Rx:\n{sphere:.2f}', f'{cylinder:.2f}', f"@{str(axis).rjust(3, '0')}")
