''' Given radius r and height h (in cm), calculate the mass of a cylinder when it's 
    filled with water and the cylinder itself doesn't weigh anything. The desired output
    should be given in kg and rounded to two decimal places.
    
    How to solve:
        - calculate the volume of the cylinder.
        - Convert cm^3 into dm^3
        - 1dm^3 = 1L, 1L is 1Kg.
    '''

import math
def weight(r, h):
    return round(math.pi * r**2 * h / 1000, 2)

print(weight(4, 10))
print(weight(30, 60))
print(weight(15, 10))