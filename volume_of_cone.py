''' Create a function that takes the height and radius of a cone as arguments and
    returns the volume of the cone rounded to the nearnest hundredth. '''

import math
def cone_volume(h, r):
    pi = math.pi
    return round(pi * r ** 2 * h / 3, 2)


print(cone_volume(3, 2))
print(cone_volume(15, 6))
print(cone_volume(18, 0))