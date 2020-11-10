# create a function that takes an angle in radians and converts it into degree.

import math
def to_degree(radian):
    return round(radian * 57.2958)

print(to_degree(math.pi))
print(to_degree(math.pi/2))
print(to_degree(math.pi/4))
