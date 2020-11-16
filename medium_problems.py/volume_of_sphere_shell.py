''' The volume of a spherical shell is the difference between the enclosed volume
    of the outer sphere and the enclosed volume of the inner sphere:

    V = 4/3*pi*(R^3 - r^3)

    Create a function that takes r1 and r2 as arguements and returns the volume
    of a spherical shell rounded to the nearest thousandth. '''

import math
def vol_shell(r1, r2):
    if r1 > r2:
        return round(4/3 * math.pi * (r1 ** 3 - r2 ** 3), 3)
    else:
        return round(4/3 * math.pi * (r2 ** 3 - r1 ** 3), 3)

print(vol_shell(3, 3))
print(vol_shell(7, 2))
print(vol_shell(3, 800))