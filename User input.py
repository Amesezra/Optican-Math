from oblique_axis import oblique_axis_180
from oblique_axis import oblique_axis_90
from transpose import transpose
from vertex import vertex_calc
from Tilt_compensation import tilt

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
print(f'Here is the given Rx:\n{sphere:.2f}', f'{cylinder:.2f}', f"@{str(axis).rjust(3, '0')}")
print(f'Now what do you want to do?')
print('1. Transpose rx')
print('2. Find prismatic imbalance')
print('3. Vertex rx')
print('4. Tilt or Warp angle calculator')
#  TODO: choice what type of refractive error is this Rx? myopia, hyperopia, presbyopia, simple/compound/mixed etc.
#       use transpose function to check both meridians for delta in power, and positivity.
#  TODO: Contact lens conversion
#        use vertex function at 0mm BVD, round axis based on with/against rule astigmatism.
#  TODO: Lens tilt/wrap calc
#  TODO: recommendations on eye-wear based on Rx
#  TODO: frame PD/OC calculator
#  TODO: ANSI Pass-Fail?
#  TODO: Focal length calc
#  TODO: SV blank size
#  TODO: Crossed cylinders
#  TODO: Spectacle Magnification Calculation
#  TODO: lens thickness calculator
#  TODO: Vertical imbalance
#  TODO: compounding prisms calculation (360 notation)
#  TODO: Resolving Prisms calculation (360 notation)
#  TODO: Surface curve conversion
choice = str(input())
while choice not in ['1', '2', '3', '4']:
    print("Your choice is invalid. Please try again.")
    choice = input("Choose 1 or 2: ")
if choice == '1':
    transposed_rx = transpose(input_rx)
elif choice == '2':
    oblique180 = oblique_axis_180(input_rx)
    oblique90 = oblique_axis_90(input_rx)
elif choice == '3':
    vertexed_rx = vertex_calc(input_rx)
elif choice == '4':
    tilted_rx = tilt(input_rx)
